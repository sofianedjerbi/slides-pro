---
theme: seriph
title: LionX Migration
colorSchema: light
highlighter: shiki
transition: none
mdc: true
layout: center
class: text-center
fonts:
  sans: Inter
  serif: Inter
---

# LionX Migration

<div class="opacity-70 mt-2">Replatforming MNY to a cloud-native foundation on AWS.</div>

<div class="mt-12 flex items-center justify-center gap-8">
<div class="flex flex-col items-center gap-2"><div class="w-16 h-16 rounded-2xl flex items-center justify-center" style="background:#e8edf1"><lucide-server class="w-8 h-8" style="color:#29445A"/></div><span class="text-xs opacity-60">On-prem today</span></div>
<lucide-arrow-right class="w-8 h-8" style="color:var(--pictet-red)"/>
<div class="flex flex-col items-center gap-2"><div class="w-16 h-16 rounded-2xl flex items-center justify-center" style="background:#f6e7e8"><lucide-cloud class="w-8 h-8" style="color:var(--pictet-red)"/></div><span class="text-xs opacity-60">AWS cloud-native</span></div>
</div>

<!--
~10 min. The plan: why we move, where we are, the AWS target, the two phases, the cost and the
governance. Keep it factual, this is for the Cloud committee and stakeholders.
-->

---

# What is LionX

<div class="text-sm opacity-70 -mt-1">Pictet's trading platform for structured products (internal name: MNY).</div>

<div class="grid grid-cols-5 gap-6 mt-4 items-center">

<div class="col-span-3 flex justify-center">

```mermaid {scale: 0.56}
flowchart TB
  T["Traders<br/>PTS · PWM · EAMs"]
  L(("LionX"))
  I["Issuers<br/>BNP · Citi · JPM<br/>UBS · SG · RBC · MS"]
  D["Booking & Archive<br/>Amon · Avaloq · audit trail"]
  T <-->|request / quote| L
  L <-->|compete| I
  L -->|execute| D
  classDef trader fill:#2C5446,stroke:#1f3d33,color:#ffffff;
  classDef hub fill:#A04044,stroke:#7d3034,color:#ffffff;
  classDef issuer fill:#29445A,stroke:#1d3242,color:#ffffff;
  classDef ds fill:#ffffff,stroke:#A04044,color:#3D3A31;
  class T trader
  class L hub
  class I issuer
  class D ds
```

</div>

<div class="col-span-2 flex flex-col gap-2.5 text-sm">
<div class="px-3 py-2 rounded-lg bg-white border border-gray-200 border-l-4 shadow-sm flex items-start gap-3" style="border-left-color: var(--pictet-red)"><lucide-plug class="w-4 h-4 shrink-0 mt-0.5" style="color: var(--pictet-red)"/><div><b>Connect</b><br/><span class="text-xs opacity-55">one protocol to every issuer</span></div></div>
<div class="px-3 py-2 rounded-lg bg-white border border-gray-200 border-l-4 shadow-sm flex items-start gap-3" style="border-left-color: var(--pictet-red)"><lucide-git-compare class="w-4 h-4 shrink-0 mt-0.5" style="color: var(--pictet-red)"/><div><b>Quote</b><br/><span class="text-xs opacity-55">issuers compete, best execution</span></div></div>
<div class="px-3 py-2 rounded-lg bg-white border border-gray-200 border-l-4 shadow-sm flex items-start gap-3" style="border-left-color: var(--pictet-red)"><lucide-send class="w-4 h-4 shrink-0 mt-0.5" style="color: var(--pictet-red)"/><div><b>Execute</b><br/><span class="text-xs opacity-55">routed to internal booking (Amon, Avaloq)</span></div></div>
<div class="px-3 py-2 rounded-lg bg-white border border-gray-200 border-l-4 shadow-sm flex items-start gap-3" style="border-left-color: var(--pictet-red)"><lucide-archive class="w-4 h-4 shrink-0 mt-0.5" style="color: var(--pictet-red)"/><div><b>Archive</b><br/><span class="text-xs opacity-55">every quote and trade, full audit trail</span></div></div>
</div>

</div>

<div class="mt-3 text-center text-sm opacity-60">One interface for traders. One integration point for issuers, across PTS, PWM and EAMs.</div>

<!--
LionX gives traders a unified interface instead of one integration per issuer, and gives issuers
a single door into Pictet. Quotes and trades are documented automatically.
-->

---

# Why move to AWS

<div class="text-sm opacity-70 -mt-1">Our load peaks on market data and sits near zero off-hours and weekends.</div>

<div class="grid grid-cols-5 gap-6 mt-4 items-center">

<div class="col-span-3">
<WorkloadChart />
</div>

<div class="col-span-2 flex flex-col gap-2.5 text-sm">
<div class="px-3 py-2 rounded-lg bg-white border border-gray-200 border-l-4 shadow-sm flex items-start gap-3" style="border-left-color: var(--pictet-red)"><lucide-cloud class="w-4 h-4 shrink-0 mt-0.5" style="color: var(--pictet-red)"/><div><b>Cloud-native</b><br/><span class="text-xs opacity-55">AWS flexibility, autoscaling on peaks</span></div></div>
<div class="px-3 py-2 rounded-lg bg-white border border-gray-200 border-l-4 shadow-sm flex items-start gap-3" style="border-left-color: var(--pictet-red)"><lucide-sliders-horizontal class="w-4 h-4 shrink-0 mt-0.5" style="color: var(--pictet-red)"/><div><b>Full control</b><br/><span class="text-xs opacity-55">over development, operations and infrastructure</span></div></div>
<div class="px-3 py-2 rounded-lg bg-white border border-gray-200 border-l-4 shadow-sm flex items-start gap-3" style="border-left-color: var(--pictet-red)"><lucide-trending-up class="w-4 h-4 shrink-0 mt-0.5" style="color: var(--pictet-red)"/><div><b>Scalable &amp; auditable</b><br/><span class="text-xs opacity-55">a foundation built for growth and compliance</span></div></div>
<div class="px-3 py-2 rounded-lg bg-white border border-gray-200 border-l-4 shadow-sm flex items-start gap-3" style="border-left-color: var(--pictet-red)"><lucide-git-merge class="w-4 h-4 shrink-0 mt-0.5" style="color: var(--pictet-red)"/><div><b>Continuity first</b><br/><span class="text-xs opacity-55">replatform as-is, then improve over time</span></div></div>
</div>

</div>

<div class="mt-3 text-center text-sm opacity-60">Fixed on-prem capacity sits idle most of the week, yet still falls short at peaks. AWS scales up on spikes and down to zero when idle.</div>

<!--
The migration is about control and modernization, without breaking what works. Iso-functional
first, cloud-native gains next.
-->

---

# What holds us back today

<div class="text-sm opacity-70 -mt-1">The on-prem stack works, but it shows its limits.</div>

<div class="grid grid-cols-2 grid-rows-2 gap-5 mt-6 h-[21rem] text-left">

<div class="p-5 rounded-xl bg-white border border-gray-200 shadow-md flex items-center gap-4"><div class="w-11 h-11 rounded-xl flex items-center justify-center shrink-0" style="background:#f6e7e8"><lucide-database class="w-6 h-6" style="color:var(--pictet-red)"/></div><div><b class="text-base">Single-node MongoDB</b><br/><span class="text-sm opacity-60">reliability and architecture at risk</span></div></div>
<div class="p-5 rounded-xl bg-white border border-gray-200 shadow-md flex items-center gap-4"><div class="w-11 h-11 rounded-xl flex items-center justify-center shrink-0" style="background:#f6e7e8"><lucide-move-horizontal class="w-6 h-6" style="color:var(--pictet-red)"/></div><div><b class="text-base">No horizontal scaling</b><br/><span class="text-sm opacity-60">several components cannot absorb peaks</span></div></div>
<div class="p-5 rounded-xl bg-white border border-gray-200 shadow-md flex items-center gap-4"><div class="w-11 h-11 rounded-xl flex items-center justify-center shrink-0" style="background:#f6e7e8"><lucide-power class="w-6 h-6" style="color:var(--pictet-red)"/></div><div><b class="text-base">Stop-the-world deploys</b><br/><span class="text-sm opacity-60">PROD is stopped to upgrade, no blue/green</span></div></div>
<div class="p-5 rounded-xl bg-white border border-gray-200 shadow-md flex items-center gap-4"><div class="w-11 h-11 rounded-xl flex items-center justify-center shrink-0" style="background:#f6e7e8"><lucide-wrench class="w-6 h-6" style="color:var(--pictet-red)"/></div><div><b class="text-base">Complex pipeline</b><br/><span class="text-sm opacity-60">pull-based hybrid, Puppet-driven</span></div></div>

</div>

<!--
These are the concrete pain points the migration addresses. The memory-leak restart and the
single-node MongoDB are the most visible.
-->

---

# Target architecture, step 1: replatform

<div class="text-sm opacity-70 -mt-1">Not a lift-and-shift: we retire the hybrid setup for managed services (Atlas, ALB) and a single deployment model.</div>

<div class="mt-5 flex justify-center">

```mermaid {scale: 0.62}
architecture-beta
  group ext(logos:aws)[External account internet facing]
  group int(logos:aws)[Internal account on prem access]

  service net(internet)[Issuers EAMs] 
  service waf(logos:aws-waf)[WAF ALB] in ext
  service arest(logos:aws-fargate)[Issuer adapters] in ext
  service fw(logos:aws-vpc)[VPC inspector HTTPS only]
  service core(logos:aws-fargate)[Core services] in int
  service iad(logos:aws-ecs)[Internal adapters] in int
  service db(logos:mongodb-icon)[MongoDB Atlas] in int
  service dc(server)[Pictet on prem DC]

  net:R --> L:waf
  waf:R --> L:arest
  arest:R --> L:fw
  fw:R --> L:core
  core:R --> L:iad
  core:B --> T:db
  iad:R --> L:dc
```

</div>

<div class="mt-3 text-center text-sm opacity-60">Issuers and EAMs enter through the external account. PTS and PWM traders reach the core from on-prem, over the private link.</div>

<div class="mt-4 flex items-center justify-center gap-2 text-xs">
<span class="opacity-45 mr-1">Shared across both accounts</span>
<span class="flex items-center gap-1.5 px-2.5 py-1 rounded-md bg-gray-50 border border-gray-200"><logos-aws-cloudwatch class="w-4 h-4"/>CloudWatch</span>
<span class="flex items-center gap-1.5 px-2.5 py-1 rounded-md bg-gray-50 border border-gray-200"><logos-aws-secrets-manager class="w-4 h-4"/>Secrets Manager</span>
<span class="flex items-center gap-1.5 px-2.5 py-1 rounded-md bg-gray-50 border border-gray-200"><logos-aws-certificate-manager class="w-4 h-4"/>ACM PCA</span>
<span class="flex items-center gap-1.5 px-2.5 py-1 rounded-md bg-gray-50 border border-gray-200"><logos-aws-s3 class="w-4 h-4"/>S3 snapshots</span>
</div>

<!--
Step 1 is a replatform, not a lift-and-shift. Today's hybrid is retired: the dedicated MongoDB and
HAProxy servers (push-based Puppet) plus the pull-based GitOps on Kubernetes give way to managed
MongoDB Atlas, AWS ALB, and one deployment model. External account holds the internet ingress and
issuer adapters; internal account holds the core, internal adapters and Atlas, reaching on-prem via
DX/VPN. VPC inspector between, HTTPS only.
-->

---

# Target architecture, step 2: cloud-native

<div class="text-sm opacity-70 -mt-1">After the refactor: Lambda adapters behind an API gateway, a simplified scalable core, no in-memory grid.</div>

<div class="mt-6 flex items-center justify-center gap-3 text-xs">

<div class="flex flex-col items-center gap-1 w-20 shrink-0"><lucide-globe class="w-7 h-7" style="color:#6b6b6b"/><span class="font-semibold">Internet</span><span class="opacity-50 text-center leading-tight">issuers, EAMs</span></div>

<lucide-arrow-right class="w-5 h-5 opacity-40 shrink-0"/>

<div class="rounded-xl border-2 px-3 py-2.5 flex flex-col gap-2" style="border-color:#A04044;background:#fbeef0">
<div class="flex items-center gap-1 text-[10px] font-bold tracking-wide" style="color:#A04044"><logos-aws class="w-3.5 h-3.5"/>EXTERNAL ACCOUNT</div>
<div class="flex flex-col items-center gap-1 px-3 py-2 rounded-lg bg-white shadow-sm"><logos-aws-api-gateway class="w-6 h-6"/><span class="font-medium whitespace-nowrap">API Gateway + WAF</span></div>
<div class="flex flex-col items-center gap-1 px-3 py-2 rounded-lg bg-white shadow-sm"><div class="flex gap-1"><logos-aws-lambda class="w-5 h-5"/><logos-aws-lambda class="w-5 h-5"/><logos-aws-lambda class="w-5 h-5"/></div><span class="font-medium whitespace-nowrap">Issuer adapters</span></div>
</div>

<div class="flex flex-col items-center gap-1 w-14 shrink-0"><logos-aws-vpc class="w-6 h-6"/><span class="opacity-50 text-center leading-tight">VPC inspector</span></div>

<div class="rounded-xl border-2 px-3 py-2.5 flex flex-col gap-2" style="border-color:#29445A;background:#eef2f5">
<div class="flex items-center gap-1 text-[10px] font-bold tracking-wide" style="color:#29445A"><logos-aws class="w-3.5 h-3.5"/>INTERNAL ACCOUNT</div>
<div class="grid grid-cols-2 gap-2">
<div class="flex flex-col items-center gap-1 px-3 py-2 rounded-lg bg-white shadow-sm"><logos-aws-fargate class="w-6 h-6"/><span class="font-medium whitespace-nowrap">Scalable core</span></div>
<div class="flex flex-col items-center gap-1 px-3 py-2 rounded-lg bg-white shadow-sm"><logos-aws-eventbridge class="w-6 h-6"/><span class="font-medium whitespace-nowrap">EventBridge</span></div>
<div class="flex flex-col items-center gap-1 px-3 py-2 rounded-lg bg-white shadow-sm"><div class="flex gap-1"><logos-aws-lambda class="w-5 h-5"/><logos-aws-lambda class="w-5 h-5"/></div><span class="font-medium whitespace-nowrap">Internal adapters</span></div>
<div class="flex flex-col items-center gap-1 px-3 py-2 rounded-lg bg-white shadow-sm"><logos-aws-documentdb class="w-6 h-6"/><span class="font-medium whitespace-nowrap">DocumentDB</span></div>
</div>
</div>

<div class="flex flex-col items-center shrink-0 w-12"><lucide-arrow-right class="w-5 h-5 opacity-40"/><span class="opacity-50 text-center leading-tight mt-0.5">DX/VPN</span></div>

<div class="flex flex-col items-center gap-1 w-20 shrink-0"><lucide-building-2 class="w-7 h-7" style="color:#6b6b6b"/><span class="font-semibold text-center leading-tight">On-prem</span><span class="opacity-50 text-center leading-tight">PTS, PWM, data</span></div>

</div>

<div class="mt-3 text-center text-sm opacity-60">Issuers and EAMs hit the API gateway; PTS and PWM traders reach the core from on-prem. Adapters run as Lambdas, the core scales horizontally, and the in-memory grid is gone.</div>

<div class="mt-4 flex items-center justify-center gap-2 text-xs">
<span class="opacity-45 mr-1">Shared across both accounts</span>
<span class="flex items-center gap-1.5 px-2.5 py-1 rounded-md bg-gray-50 border border-gray-200"><logos-aws-eventbridge class="w-4 h-4"/>EventBridge</span>
<span class="flex items-center gap-1.5 px-2.5 py-1 rounded-md bg-gray-50 border border-gray-200"><logos-aws-cloudwatch class="w-4 h-4"/>CloudWatch</span>
<span class="flex items-center gap-1.5 px-2.5 py-1 rounded-md bg-gray-50 border border-gray-200"><logos-aws-secrets-manager class="w-4 h-4"/>Secrets Manager</span>
<span class="flex items-center gap-1.5 px-2.5 py-1 rounded-md bg-gray-50 border border-gray-200"><logos-aws-s3 class="w-4 h-4"/>S3</span>
</div>

<!--
After the cloud-native refactor: issuer and internal adapters run as Lambdas behind API Gateway,
the core is stateless and scales horizontally on Fargate, state lives in Amazon DocumentDB, and the
in-memory grid is removed. Function workloads move to FaaS, event-driven through EventBridge.
-->

---

# A two-phase migration

<div class="text-sm opacity-70 -mt-1">Business continuity first, cloud-native gains next.</div>

<div class="grid grid-cols-2 gap-6 mt-5 text-left text-sm items-start">

<div>
<div class="text-xs uppercase tracking-widest mb-3" style="color: var(--pictet-red)">Phase 1: Replatform</div>
<div class="flex flex-col gap-3">
<div class="p-4 rounded-xl bg-white border border-gray-200 shadow-md flex items-center gap-3"><div class="w-10 h-10 rounded-lg flex items-center justify-center shrink-0" style="background:#f6e7e8"><lucide-copy class="w-5 h-5" style="color:var(--pictet-red)"/></div><div><b>Iso-functional, simpler stack</b><br/><span class="text-xs opacity-60">same app behavior; managed services replace the hybrid setup</span></div></div>
<div class="p-4 rounded-xl bg-white border border-gray-200 shadow-md flex items-center gap-3"><div class="w-10 h-10 rounded-lg flex items-center justify-center shrink-0" style="background:#f6e7e8"><lucide-scale class="w-5 h-5" style="color:var(--pictet-red)"/></div><div><b>Parity</b><br/><span class="text-xs opacity-60">performance, security, resilience and audit at least equivalent</span></div></div>
<div class="p-4 rounded-xl bg-white border border-gray-200 shadow-md flex items-center gap-3"><div class="w-10 h-10 rounded-lg flex items-center justify-center shrink-0" style="background:#f6e7e8"><lucide-workflow class="w-5 h-5" style="color:var(--pictet-red)"/></div><div><b>Modern operations</b><br/><span class="text-xs opacity-60">single push-based CI/CD, IaC, blue/green deploys</span></div></div>
</div>
</div>

<div>
<div class="text-xs uppercase tracking-widest mb-3 opacity-50">Phase 2: Leverage the cloud</div>
<div class="flex flex-col gap-3">
<div class="p-4 rounded-xl bg-white border border-gray-200 shadow-md flex items-center gap-3"><div class="w-10 h-10 rounded-lg flex items-center justify-center shrink-0" style="background:#f6e7e8"><lucide-trending-up class="w-5 h-5" style="color:var(--pictet-red)"/></div><div><b>Elasticity</b><br/><span class="text-xs opacity-60">autoscaling on demand; scale down to 20% on nights and weekends</span></div></div>
<div class="p-4 rounded-xl bg-white border border-gray-200 shadow-md flex items-center gap-3"><div class="w-10 h-10 rounded-lg flex items-center justify-center shrink-0" style="background:#f6e7e8"><lucide-heart-pulse class="w-5 h-5" style="color:var(--pictet-red)"/></div><div><b>High availability</b><br/><span class="text-xs opacity-60">multi-AZ, self-healing, automated DR and failover tests</span></div></div>
<div class="p-4 rounded-xl bg-white border border-gray-200 shadow-md flex items-center gap-3"><div class="w-10 h-10 rounded-lg flex items-center justify-center shrink-0" style="background:#f6e7e8"><lucide-zap class="w-5 h-5" style="color:var(--pictet-red)"/></div><div><b>Serverless and cloud-native</b><br/><span class="text-xs opacity-60">FaaS adapters on Lambda, DocumentDB, no in-memory grid</span></div></div>
</div>
</div>

</div>

<!--
Phase 1 de-risks the cutover: same app, new ground. Phase 2 is where the cloud pays off,
once the Pictet AWS platform services are available.
-->

---

# Roadmap

<div class="text-sm opacity-70 -mt-1">Migrate first to reach parity, then modernize. Phased from 2026 to 2028.</div>

<div class="mt-6 text-[13px]">

<div class="relative">

<div class="absolute top-0 bottom-0 pointer-events-none" style="left:200px;right:8px">
<div class="absolute top-0 bottom-0 w-px bg-gray-200" style="left:0%"></div>
<div class="absolute top-0 bottom-0 w-px bg-gray-200" style="left:33.3%"></div>
<div class="absolute top-0 bottom-0 w-px bg-gray-200" style="left:66.7%"></div>
<div class="absolute top-0 bottom-0 w-px bg-gray-200" style="left:100%"></div>
</div>

<div class="text-xs uppercase tracking-widest font-semibold mb-1" style="color:var(--pictet-red)">Migrate</div>

<div class="flex items-center h-7"><div class="shrink-0 pr-3 text-right opacity-80" style="width:200px">Preparation and POC</div><div class="flex-1 relative h-full"><div class="absolute top-1/2 -translate-y-1/2 h-4 rounded shadow-sm" style="left:11.1%;width:11.1%;background:#A04044"></div></div></div>
<div class="flex items-center h-7"><div class="shrink-0 pr-3 text-right opacity-80" style="width:200px">Replatforming on INTG</div><div class="flex-1 relative h-full"><div class="absolute top-1/2 -translate-y-1/2 h-4 rounded shadow-sm" style="left:22.2%;width:5.6%;background:#A04044"></div></div></div>
<div class="flex items-center h-7"><div class="shrink-0 pr-3 text-right opacity-80" style="width:200px">Cutover INTG</div><div class="flex-1 relative h-full"><div class="absolute top-1/2 -translate-y-1/2 h-4 rounded shadow-sm" style="left:27.8%;width:5.6%;background:#A04044"></div></div></div>
<div class="flex items-center h-7"><div class="shrink-0 pr-3 text-right opacity-80" style="width:200px">Roll out all envs to PROD</div><div class="flex-1 relative h-full"><div class="absolute top-1/2 -translate-y-1/2 h-4 rounded shadow-sm" style="left:33.3%;width:16.7%;background:#A04044"></div></div></div>
<div class="flex items-center h-7"><div class="shrink-0 pr-3 text-right italic opacity-70" style="width:200px">Migration complete</div><div class="flex-1 relative h-full"><div class="absolute top-1/2 w-3 h-3 rotate-45 shadow-sm" style="left:50%;transform:translate(-50%,-50%) rotate(45deg);background:#A04044"></div></div></div>

<div class="text-xs uppercase tracking-widest font-semibold mt-2 mb-1" style="color:#29445A">Make LionX cloud native</div>

<div class="flex items-center h-7"><div class="shrink-0 pr-3 text-right opacity-80" style="width:200px">Horizontally scalable compute</div><div class="flex-1 relative h-full"><div class="absolute top-1/2 -translate-y-1/2 h-4 rounded shadow-sm" style="left:33.3%;width:33.3%;background:#29445A"></div></div></div>
<div class="flex items-center h-7"><div class="shrink-0 pr-3 text-right opacity-80" style="width:200px">Function workloads to FaaS</div><div class="flex-1 relative h-full"><div class="absolute top-1/2 -translate-y-1/2 h-4 rounded shadow-sm" style="left:50%;width:33.3%;background:#29445A"></div></div></div>
<div class="flex items-center h-7"><div class="shrink-0 pr-3 text-right opacity-80" style="width:200px">Replace in-memory data grid</div><div class="flex-1 relative h-full"><div class="absolute top-1/2 -translate-y-1/2 h-4 rounded shadow-sm" style="left:50%;width:41.7%;background:#29445A"></div></div></div>
<div class="flex items-center h-7"><div class="shrink-0 pr-3 text-right opacity-80" style="width:200px">Run and optimize</div><div class="flex-1 relative h-full"><div class="absolute top-1/2 -translate-y-1/2 h-4 rounded shadow-sm" style="left:83.3%;width:13.9%;background:#29445A"></div></div></div>

<div class="absolute top-0 bottom-0 pointer-events-none" style="left:200px;right:8px">
<div class="absolute top-0 bottom-0" style="left:16.7%">
<div class="absolute top-0 bottom-0 left-0 w-0.5 -translate-x-1/2" style="background:var(--pictet-red)"></div>
<div class="absolute top-0 left-0 -translate-x-1/2 -translate-y-1 whitespace-nowrap text-[10px] font-bold px-1.5 py-0.5 rounded shadow-sm" style="color:#ffffff;background:var(--pictet-red)">We are here</div>
</div>
</div>

</div>

<div class="flex mt-1.5">
<div class="shrink-0" style="width:200px"></div>
<div class="flex-1 relative h-4 text-xs opacity-55" style="margin-right:8px">
<span class="absolute -translate-x-1/2" style="left:0%">2026</span>
<span class="absolute -translate-x-1/2" style="left:33.3%">2027</span>
<span class="absolute -translate-x-1/2" style="left:66.7%">2028</span>
<span class="absolute -translate-x-1/2" style="left:100%">2029</span>
</div>
</div>

</div>

<div class="mt-3 text-center text-sm opacity-60">Production on AWS by mid 2027, fully cloud-native by end 2028.</div>

<!--
The first four phases get every environment to AWS and decommission on-prem. The modernization
phases overlap and continue after PROD: observability and security, then exiting GigaSpaces.
-->

---

# Risks we are managing

<div class="text-sm opacity-70 -mt-1">Known upfront, with mitigation.</div>

<div class="grid grid-cols-2 grid-rows-2 gap-5 mt-5 h-[18rem] text-left">

<div class="p-5 rounded-xl bg-white border border-gray-200 shadow-md flex items-center gap-4"><div class="w-11 h-11 rounded-xl flex items-center justify-center shrink-0" style="background:#f6e7e8"><lucide-share-2 class="w-6 h-6" style="color:var(--pictet-red)"/></div><div><b class="text-base">Shared Pictet services</b><br/><span class="text-sm opacity-60">their maturity paces us; possible temporary dual monitoring</span></div></div>
<div class="p-5 rounded-xl bg-white border border-gray-200 shadow-md flex items-center gap-4"><div class="w-11 h-11 rounded-xl flex items-center justify-center shrink-0" style="background:#f6e7e8"><lucide-waypoints class="w-6 h-6" style="color:var(--pictet-red)"/></div><div><b class="text-base">Network complexity</b><br/><span class="text-sm opacity-60">on-prem links, issuer connectivity, firewall inspection</span></div></div>
<div class="p-5 rounded-xl bg-white border border-gray-200 shadow-md flex items-center gap-4"><div class="w-11 h-11 rounded-xl flex items-center justify-center shrink-0" style="background:#f6e7e8"><lucide-triangle-alert class="w-6 h-6" style="color:var(--pictet-red)"/></div><div><b class="text-base">Replatforming surprises</b><br/><span class="text-sm opacity-60">different IO, network and timeout behavior in the cloud</span></div></div>
<div class="p-5 rounded-xl bg-white border border-gray-200 shadow-md flex items-center gap-4"><div class="w-11 h-11 rounded-xl flex items-center justify-center shrink-0" style="background:#f6e7e8"><lucide-heart-pulse class="w-6 h-6" style="color:var(--pictet-red)"/></div><div><b class="text-base">Service continuity</b><br/><span class="text-sm opacity-60">adapting operations and on-call during ramp-up</span></div></div>

</div>

<div class="mt-5 text-center text-sm opacity-60">Each risk has an owner and a mitigation tracked in the migration plan.</div>

<!--
The biggest external dependency is the maturity of shared Pictet platform services. Ownership of
infra scanning and intrusion detection is still to be confirmed with the cyber-security team.
-->

---

# Migration effort

<div class="text-sm opacity-70 -mt-1">One-time effort to replatform onto AWS, CI/CD from Bamboo to GitHub included. Phase 1 only, not the cloud-native refactor.</div>

<div class="mt-6 flex flex-col gap-2.5">

<div class="flex items-center gap-3"><div class="w-56 shrink-0 text-right text-sm opacity-80">AWS landing zone and network</div><div class="flex-1 h-5 rounded bg-gray-100 relative"><div class="absolute inset-y-0 left-0 rounded overflow-hidden flex" style="width:73%"><div class="h-full" style="width:83.33%;background:#A04044"></div><div class="h-full" style="width:16.67%;background:#A04044;opacity:0.38"></div></div></div><div class="w-16 text-right text-sm"><b>55</b> <span class="opacity-50 text-xs">MD</span></div></div>

<div class="flex items-center gap-3"><div class="w-56 shrink-0 text-right text-sm opacity-80">CI/CD, Bamboo to GitHub Actions</div><div class="flex-1 h-5 rounded bg-gray-100 relative"><div class="absolute inset-y-0 left-0 rounded overflow-hidden flex" style="width:40%"><div class="h-full" style="width:83.33%;background:#A04044"></div><div class="h-full" style="width:16.67%;background:#A04044;opacity:0.38"></div></div></div><div class="w-16 text-right text-sm"><b>30</b> <span class="opacity-50 text-xs">MD</span></div></div>

<div class="flex items-center gap-3"><div class="w-56 shrink-0 text-right text-sm opacity-80">App replatform on ECS/Fargate</div><div class="flex-1 h-5 rounded bg-gray-100 relative"><div class="absolute inset-y-0 left-0 rounded overflow-hidden flex" style="width:73%"><div class="h-full" style="width:83.33%;background:#A04044"></div><div class="h-full" style="width:16.67%;background:#A04044;opacity:0.38"></div></div></div><div class="w-16 text-right text-sm"><b>55</b> <span class="opacity-50 text-xs">MD</span></div></div>

<div class="flex items-center gap-3"><div class="w-56 shrink-0 text-right text-sm opacity-80">Data migration, managed services</div><div class="flex-1 h-5 rounded bg-gray-100 relative"><div class="absolute inset-y-0 left-0 rounded overflow-hidden flex" style="width:53%"><div class="h-full" style="width:83.33%;background:#A04044"></div><div class="h-full" style="width:16.67%;background:#A04044;opacity:0.38"></div></div></div><div class="w-16 text-right text-sm"><b>40</b> <span class="opacity-50 text-xs">MD</span></div></div>

<div class="flex items-center gap-3"><div class="w-56 shrink-0 text-right text-sm opacity-80">Testing, cutover and rollout</div><div class="flex-1 h-5 rounded bg-gray-100 relative"><div class="absolute inset-y-0 left-0 rounded overflow-hidden flex" style="width:100%"><div class="h-full" style="width:83.33%;background:#A04044"></div><div class="h-full" style="width:16.67%;background:#A04044;opacity:0.38"></div></div></div><div class="w-16 text-right text-sm"><b>75</b> <span class="opacity-50 text-xs">MD</span></div></div>

<div class="flex items-center gap-3"><div class="w-56 shrink-0 text-right text-sm opacity-80">Project management</div><div class="flex-1 h-5 rounded bg-gray-100 relative"><div class="absolute inset-y-0 left-0 rounded overflow-hidden flex" style="width:60%"><div class="h-full" style="width:83.33%;background:#29445A"></div><div class="h-full" style="width:16.67%;background:#29445A;opacity:0.38"></div></div></div><div class="w-16 text-right text-sm"><b>45</b> <span class="opacity-50 text-xs">MD</span></div></div>

</div>

<div class="flex justify-center gap-6 text-xs mt-3">
<span class="flex items-center gap-1.5"><span class="w-3 h-3 rounded-sm inline-block" style="background:#A04044"></span>estimate</span>
<span class="flex items-center gap-1.5"><span class="w-3 h-3 rounded-sm inline-block" style="background:#A04044;opacity:0.38"></span>20% margin</span>
</div>

<div class="mt-5 flex items-center justify-center gap-16 text-center">
<div><div class="text-3xl font-bold" style="color:var(--pictet-red)">~360</div><div class="text-xs opacity-55">man-days (300 + 20% margin)</div></div>
<div><div class="text-3xl font-bold" style="color:var(--pictet-red)">~1.6</div><div class="text-xs opacity-55">FTE-year</div></div>
</div>

<!--
One-time build cost for the replatform, CI/CD migration included. Excludes the cloud-native
refactor (Phase 2). Man-days are a bottom-up estimate; the day rate is a placeholder to adjust.
-->

---

# Cost, milestone and governance

<div class="text-sm opacity-70 -mt-1">Zurich list prices, 5 environments at 8 vCPU / 32 GB. Atlas is billed per node; DocumentDB non-prod pauses on weekends.</div>

<div class="mt-5"><CostPie /></div>

<div class="mt-4 text-center text-xs opacity-55">Figures are firm through 2027. For the cloud-native years (2028+), budget a ~25% contingency, so plan ~$157k for the optimized target.</div>

<div class="mt-4 flex items-center justify-center gap-3 text-xs">
<span class="flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-gray-50 border border-gray-200"><lucide-users class="w-3.5 h-3.5" style="color:var(--pictet-red)"/>Run ~1.5 FTE/year</span>
<span class="flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-gray-50 border border-gray-200"><lucide-flag class="w-3.5 h-3.5" style="color:var(--pictet-red)"/>Integration env on AWS, end 2026</span>
<span class="flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-gray-50 border border-gray-200"><lucide-users-round class="w-3.5 h-3.5" style="color:var(--pictet-red)"/>Cloud committee</span>
</div>

<!--
Run cost is operations only. Infra is provisional and pre-PoC. The decisive milestone is the
integration environment on AWS at the end of 2026, inside a real pipeline.
-->

---

# Next steps

<div class="text-sm opacity-70 -mt-1">What we are asking for today.</div>

<div class="grid grid-cols-3 gap-5 mt-6 text-left">

<div class="p-5 rounded-xl bg-white border border-gray-200 shadow-md flex flex-col gap-3 h-full"><div class="w-11 h-11 rounded-xl flex items-center justify-center" style="background:#f6e7e8"><lucide-circle-check class="w-6 h-6" style="color:var(--pictet-red)"/></div><div><b class="text-base">Green-light the plan</b><br/><span class="text-sm opacity-60">approve the two-phase migration and its budget envelope</span></div></div>

<div class="p-5 rounded-xl bg-white border border-gray-200 shadow-md flex flex-col gap-3 h-full"><div class="w-11 h-11 rounded-xl flex items-center justify-center" style="background:#f6e7e8"><lucide-file-check class="w-6 h-6" style="color:var(--pictet-red)"/></div><div><b class="text-base">Chain the ADRs</b><br/><span class="text-sm opacity-60">record the architecture decisions back to back to validate and start fast</span></div></div>

<div class="p-5 rounded-xl bg-white border border-gray-200 shadow-md flex flex-col gap-3 h-full"><div class="w-11 h-11 rounded-xl flex items-center justify-center" style="background:#f6e7e8"><lucide-flag class="w-6 h-6" style="color:var(--pictet-red)"/></div><div><b class="text-base">Integration env by end 2026</b><br/><span class="text-sm opacity-60">running on AWS inside a real deployment pipeline</span></div></div>

</div>

<div class="mt-12 text-center">
<div class="text-2xl font-semibold" style="color:var(--pictet-red)">Questions and discussion welcome</div>
</div>
