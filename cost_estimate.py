#!/usr/bin/env python3
"""
LionX (MNY) cloud cost estimate — AWS + database options.

Goal: an UPPER-BOUND (majorant). Everything 24/7, no discount, every env at
full size. Then a scenario where COMPUTE is scaled down to 20% (reduced by
80%, not to zero) at night and on weekends.

Database options:
  - MongoDB Atlas (~M50, 3 nodes) per env
  - Amazon DocumentDB (db.r6g.xlarge = 4 vCPU / 32 GB, 3 instances) per env
    DocumentDB cannot run at 20%: its only off-hours lever is to STOP the
    cluster (instances -> $0, storage still billed, 7-day max stop). Realistic
    for non-prod only; prod DB stays on 24/7.

All numbers are PUBLIC LIST PRICES. Edit and re-run: python3 cost_estimate.py
Region: eu-central-2 (Zurich). AWS prices from the public Price List API;
MongoDB Atlas is third-party (estimated).
"""

HOURS_PER_MONTH = 730
MONTHS = 12

ENVIRONMENTS = ["INTG", "INTG2", "CTLQ", "CTLQ2", "PROD"]
ALWAYS_ON_DB = ["PROD"]         # DB cannot be stopped off-hours (prod)
VCPU_PER_ENV = 8
GB_PER_ENV = 32
COMPUTE_DISCOUNT = 0.0

# ---- AWS Fargate, eu-central-2 (Zurich), Linux/x86 -- from AWS Price List API ----
FARGATE_VCPU_HOUR = 0.05448
FARGATE_GB_HOUR   = 0.00598
# (ARM/Graviton would be cheaper: 0.04358 / 0.00478)

# ---- MongoDB Atlas M50 (32 GB / 8 vCPU), USD per NODE-hour, 3-node replica set ----
# M50 base = $2.00/node confirmed on mongodb.com/pricing; Atlas docs: the tier rate
# is charged PER data-bearing node (replica set = 3 nodes). Zurich premium ~+30%,
# aligned with the measured AWS Zurich premium (DocumentDB +26%, Fargate +35% vs
# us-east-1). Atlas is third-party SaaS with no public Zurich rate -> estimate.
ATLAS_NODE_HOUR = 2.60
ATLAS_NODES = 3
# Right-sized: only PROD needs M50. Non-prod on M30 (8 GB / 2 vCPU),
# base $0.54/node -> ~$0.70 with the Zurich premium.
ATLAS_NONPROD_NODE_HOUR = 0.70

# ---- Amazon DocumentDB (db.r6g.xlarge = 4 vCPU / 32 GB), 3 instances ----
# Zurich, standard storage -- from AWS Price List API.
# Mongo is RAM-bound, so size on RAM (32 GB) -> r6g.xlarge.
DOCDB_INSTANCE_HOUR = 0.69806
DOCDB_INSTANCES = 3
DOCDB_STORAGE_MONTH = 60        # storage 0.1309/GB-mo + I/O 0.242/M + backup, generic per env

# ---- Generic monthly buckets, PER ENVIRONMENT ----
STORAGE_NETWORK_MONTH = 360
OTHER_MANAGED_MONTH   = 140

# ---- Night/weekend scaling (compute, and DocumentDB stop) ----
WEEKDAYS, WEEKEND_DAYS = 5, 2
ON_HOURS_PER_WEEKDAY = 24       # full all weekday; ONLY weekends scale down
REDUCED_FACTOR = 0.20           # weekend level for compute (20%); DB stop = 0%

# ---- One-time migration effort (replatform Phase 1 + CI/CD Bamboo->GitHub) ----
MIGRATION_MD = {
    "AWS landing zone and network": 55,
    "CI/CD Bamboo to GitHub Actions": 30,
    "App replatform on ECS/Fargate": 55,
    "Data migration and managed services": 40,
    "Testing, cutover and rollout": 75,
    "PM and contingency": 45,
}
DAY_RATE_USD = 1200             # blended day rate, assumed (edit)
FTE_DAYS_PER_YEAR = 220

# ---- Phase 2 development effort (cloud-native refactor) ----
MIGRATION_MD_P2 = {
    "Replace the in-memory data grid": 120,
    "Stateless, scalable core": 80,
    "Function workloads to FaaS": 70,
    "Event-driven and observability": 60,
    "Testing and hardening": 60,
    "Project management": 40,
}

N = len(ENVIRONMENTS)

def _week_split():
    total = 24 * (WEEKDAYS + WEEKEND_DAYS)
    full = ON_HOURS_PER_WEEKDAY * WEEKDAYS
    return full, total - full, total

def compute_fraction_scaled():
    full, off, total = _week_split()
    return (full + off * REDUCED_FACTOR) / total      # ~0.49

def db_on_fraction_stopped():
    full, off, total = _week_split()
    return full / total                               # instances on only on-hours

# ---- per-env monthly costs ----
def fargate_env(fraction=1.0):
    base = (VCPU_PER_ENV * FARGATE_VCPU_HOUR + GB_PER_ENV * FARGATE_GB_HOUR) * HOURS_PER_MONTH
    return base * (1 - COMPUTE_DISCOUNT) * fraction

def atlas_env():
    return ATLAS_NODE_HOUR * ATLAS_NODES * HOURS_PER_MONTH

def docdb_env(instance_fraction=1.0):
    return DOCDB_INSTANCE_HOUR * DOCDB_INSTANCES * HOURS_PER_MONTH * instance_fraction + DOCDB_STORAGE_MONTH

def storage_other_env():
    return STORAGE_NETWORK_MONTH + OTHER_MANAGED_MONTH

# ---- totals across all envs (per month) ----
def atlas_total():
    return atlas_env() * N

def atlas_rightsized_total():
    # PROD on M50, the 4 non-prod envs on M30
    prod = ATLAS_NODE_HOUR * ATLAS_NODES * HOURS_PER_MONTH
    nonprod = ATLAS_NONPROD_NODE_HOUR * ATLAS_NODES * HOURS_PER_MONTH * (N - 1)
    return prod + nonprod

def docdb_total(stop_nonprod=False):
    frac_off = db_on_fraction_stopped()
    total = 0.0
    for env in ENVIRONMENTS:
        f = frac_off if (stop_nonprod and env not in ALWAYS_ON_DB) else 1.0
        total += docdb_env(f)
    return total

def money(x):
    return f"${x:,.0f}"

def scenario(label, compute_frac, db_month):
    compute = fargate_env(compute_frac) * N
    storage_other = storage_other_env() * N
    total_m = compute + storage_other + db_month
    yr = total_m * MONTHS
    print(f"\n--- {label}")
    print(f"    Compute        {money(compute*MONTHS):>12} /yr")
    print(f"    Database       {money(db_month*MONTHS):>12} /yr")
    print(f"    Storage+net    {money(storage_other*MONTHS):>12} /yr")
    print(f"    TOTAL          {money(yr):>12} /yr   ({money(total_m)}/mo)")
    return yr

def main():
    print(f"{N} envs x 8 vCPU/32 GB | compute scaled factor = {compute_fraction_scaled():.2f} "
          f"| DB stop on-fraction = {db_on_fraction_stopped():.2f}")
    cf = compute_fraction_scaled()

    a = scenario("A  Atlas, 24/7 (MAJORANT)", 1.0, atlas_total())
    a2 = scenario("A' Atlas right-sized, 24/7 (prod M50, non-prod M30) -- REPLATFORM", 1.0, atlas_rightsized_total())
    b = scenario("B  Atlas + compute scaled 80% off-hours", cf, atlas_total())
    c = scenario("B' DocumentDB (24/7) + compute scaled", cf, docdb_total(stop_nonprod=False))
    d = scenario("B'' DocumentDB, non-prod STOPPED off-hours + compute scaled", cf, docdb_total(stop_nonprod=True))

    print("\n" + "#" * 60)
    print(f"  A  Atlas 24/7 (majorant)            {money(a)} /yr")
    print(f"  B  Atlas + compute scaled           {money(b)} /yr  (-{(a-b)/a*100:.0f}%)")
    print(f"  B' DocumentDB 24/7 + compute scaled {money(c)} /yr")
    print(f"  B'' DocumentDB non-prod stopped     {money(d)} /yr  (-{(a-d)/a*100:.0f}% vs A)")
    print("#" * 60)

    # Estimate is firm through 2027 (replatform, known infra). The cloud-native
    # years (2028+) are less certain -> add a contingency margin.
    cont = 0.25
    print(f"\nFirm through 2027. Cloud-native years (2028+): +{int(cont*100)}% contingency.")
    print(f"  Optimized target with margin: {money(d)} -> {money(d*(1+cont))} /yr")
    print(f"  Upper bound with margin:      {money(a)} -> {money(a*(1+cont))} /yr")

    print("\n" + "=" * 60)
    print("ONE-TIME MIGRATION EFFORT (replatform + CI/CD, Phase 1 only)")
    print("=" * 60)
    tot = sum(MIGRATION_MD.values())
    for name, md in MIGRATION_MD.items():
        print(f"  {name:<38} {md:>4} MD")
    print("-" * 60)
    marg = 0.20
    with_m = tot * (1 + marg)
    print(f"  {'Subtotal':<38} {tot:>4} MD")
    print(f"  {'+ ' + str(int(marg*100)) + '% margin':<38} {tot*marg:>4.0f} MD")
    print(f"  {'TOTAL with margin':<38} {with_m:>4.0f} MD  (~{with_m/FTE_DAYS_PER_YEAR:.1f} FTE-year)")

    print("\n" + "=" * 60)
    print("PHASE 2 DEVELOPMENT EFFORT (cloud-native refactor)")
    print("=" * 60)
    tot2 = sum(MIGRATION_MD_P2.values())
    for name, md in MIGRATION_MD_P2.items():
        print(f"  {name:<38} {md:>4} MD")
    print("-" * 60)
    with_m2 = tot2 * (1 + marg)
    print(f"  {'Subtotal':<38} {tot2:>4} MD")
    print(f"  {'+ ' + str(int(marg*100)) + '% margin':<38} {tot2*marg:>4.0f} MD")
    print(f"  {'TOTAL with margin':<38} {with_m2:>4.0f} MD  (~{with_m2/FTE_DAYS_PER_YEAR:.1f} FTE-year)")
    print("\nList prices, eu-central-2 (Zurich). DocumentDB has no 20% mode: off-hours = full")
    print("cluster stop (instances $0, storage still billed), non-prod only.")

if __name__ == "__main__":
    main()
