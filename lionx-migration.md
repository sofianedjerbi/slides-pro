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
<div class="px-3 py-2 rounded-lg border border-gray-200 border-l-4 shadow-sm flex items-start gap-3" style="border-left-color: var(--pictet-red); background:#fbeef0"><lucide-compass class="w-4 h-4 shrink-0 mt-0.5" style="color: var(--pictet-red)"/><div><b>Pictet's cloud strategy</b><br/><span class="text-xs opacity-55">LionX aligns with the group's move to AWS</span></div></div>
<div class="px-3 py-2 rounded-lg bg-white border border-gray-200 border-l-4 shadow-sm flex items-start gap-3" style="border-left-color: var(--pictet-red)"><lucide-minimize-2 class="w-4 h-4 shrink-0 mt-0.5" style="color: var(--pictet-red)"/><div><b>Simplify</b><br/><span class="text-xs opacity-55">on-prem infra back to industry standards</span></div></div>
<div class="px-3 py-2 rounded-lg bg-white border border-gray-200 border-l-4 shadow-sm flex items-start gap-3" style="border-left-color: var(--pictet-red)"><lucide-cloud class="w-4 h-4 shrink-0 mt-0.5" style="color: var(--pictet-red)"/><div><b>Cloud-native</b><br/><span class="text-xs opacity-55">AWS flexibility, autoscaling on peaks</span></div></div>
<div class="px-3 py-2 rounded-lg bg-white border border-gray-200 border-l-4 shadow-sm flex items-start gap-3" style="border-left-color: var(--pictet-red)"><lucide-sliders-horizontal class="w-4 h-4 shrink-0 mt-0.5" style="color: var(--pictet-red)"/><div><b>Full control</b><br/><span class="text-xs opacity-55">over development, operations and infrastructure</span></div></div></div>

</div>

<div class="mt-3 text-center text-sm opacity-60">Fixed on-prem capacity sits idle most of the week, yet still falls short at peaks. AWS scales up on spikes and down to zero when idle.</div>

<!--
The migration is about control and modernization, without breaking what works. Iso-functional
first, cloud-native gains next.

Strategie migrations pictet
-->

---

# Today's infrastructure limits

<div class="text-sm opacity-70 -mt-1">The on-prem stack works, but it shows its limits. AWS addresses each one.</div>

<div class="grid grid-cols-2 grid-rows-2 gap-5 mt-6 h-[21rem] text-left">

<div class="p-5 rounded-xl bg-white border border-gray-200 shadow-md flex items-center gap-4"><div class="w-11 h-11 rounded-xl flex items-center justify-center shrink-0" style="background:#f6e7e8"><lucide-database class="w-6 h-6" style="color:var(--pictet-red)"/></div><div><b class="text-base">Single-node MongoDB</b><br/><span class="text-sm opacity-60">reliability and architecture at risk</span><div class="flex items-center gap-1.5 mt-1.5 text-xs font-semibold" style="color:#2C5446"><lucide-check class="w-3.5 h-3.5 shrink-0"/><span>Managed, Multi-AZ, resilient and elastic</span></div></div></div>
<div class="p-5 rounded-xl bg-white border border-gray-200 shadow-md flex items-center gap-4"><div class="w-11 h-11 rounded-xl flex items-center justify-center shrink-0" style="background:#f6e7e8"><lucide-move-horizontal class="w-6 h-6" style="color:var(--pictet-red)"/></div><div><b class="text-base">No horizontal scaling</b><br/><span class="text-sm opacity-60">several components cannot absorb peaks</span><div class="flex items-center gap-1.5 mt-1.5 text-xs font-semibold" style="color:#2C5446"><lucide-check class="w-3.5 h-3.5 shrink-0"/><span>Elastic, scales with demand, no fixed capacity</span></div></div></div>
<div class="p-5 rounded-xl bg-white border border-gray-200 shadow-md flex items-center gap-4"><div class="w-11 h-11 rounded-xl flex items-center justify-center shrink-0" style="background:#f6e7e8"><lucide-power class="w-6 h-6" style="color:var(--pictet-red)"/></div><div><b class="text-base">No zero-downtime deploys</b><br/><span class="text-sm opacity-60">PROD is stopped for every upgrade</span><div class="flex items-center gap-1.5 mt-1.5 text-xs font-semibold" style="color:#2C5446"><lucide-check class="w-3.5 h-3.5 shrink-0"/><span>Blue/green rollouts, zero downtime</span></div></div></div>
<div class="p-5 rounded-xl bg-white border border-gray-200 shadow-md flex items-center gap-4"><div class="w-11 h-11 rounded-xl flex items-center justify-center shrink-0" style="background:#f6e7e8"><lucide-wrench class="w-6 h-6" style="color:var(--pictet-red)"/></div><div><b class="text-base">Pipeline to simplify</b><br/><span class="text-sm opacity-60">Puppet / Docker / Kubernetes =&gt; Terraform</span><div class="flex items-center gap-1.5 mt-1.5 text-xs font-semibold" style="color:#2C5446"><lucide-check class="w-3.5 h-3.5 shrink-0"/><span>One Terraform IaC, simple CI/CD</span></div></div></div>

</div>

<!--
These are the concrete pain points the migration addresses. The memory-leak restart and the
single-node MongoDB are the most visible.

Formulation : Pourquoi on va beneficier du cloud. Tourner ca en mode simplifier
-->

---

# Target architecture, step 1: replatform

<div class="text-sm opacity-70 -mt-1">Not a lift-and-shift: we retire the hybrid setup for managed services (Atlas, ALB) and a single deployment model.</div>

<div class="mt-6 flex items-center justify-center gap-3 text-xs">

<div class="flex flex-col items-center gap-1 w-20 shrink-0"><lucide-globe class="w-7 h-7" style="color:#6b6b6b"/><span class="font-semibold">Internet</span><span class="opacity-50 text-center leading-tight">issuers, EAMs</span></div>

<lucide-arrow-right class="w-5 h-5 opacity-40 shrink-0"/>

<div class="rounded-xl border-2 px-3 py-2.5 flex flex-col gap-2" style="border-color:#A04044;background:#fdf3f4">
<div class="flex items-center gap-1 text-[10px] font-bold tracking-wide" style="color:#A04044"><logos-aws class="w-3.5 h-3.5"/>EXTERNAL ACCOUNT</div>
<div class="flex flex-col items-center gap-1 px-3 py-2 rounded-lg bg-white shadow-sm"><logos-aws-waf class="w-6 h-6"/><span class="font-medium whitespace-nowrap">WAF + ALB</span></div>
<div class="flex flex-col items-center gap-1 px-3 py-2 rounded-lg bg-white shadow-sm"><logos-aws-fargate class="w-6 h-6"/><span class="font-medium whitespace-nowrap">Issuer adapters</span></div>
</div>

<div class="flex flex-col items-center gap-1 w-16 shrink-0"><logos-aws-vpc class="w-6 h-6"/><span class="opacity-50 text-center leading-tight">VPC inspector, HTTPS only</span></div>

<div class="rounded-xl border-2 px-3 py-2.5 flex flex-col gap-2" style="border-color:#A04044;background:#fdf3f4">
<div class="flex items-center gap-1 text-[10px] font-bold tracking-wide" style="color:#A04044"><logos-aws class="w-3.5 h-3.5"/>INTERNAL ACCOUNT</div>
<div class="grid grid-cols-2 gap-2">
<div class="flex flex-col items-center gap-1 px-3 py-2 rounded-lg bg-white shadow-sm"><logos-aws-fargate class="w-6 h-6"/><span class="font-medium whitespace-nowrap">Business logic</span></div>
<div class="flex flex-col items-center gap-1 px-3 py-2 rounded-lg bg-white shadow-sm"><lucide-database class="w-6 h-6" style="color:#6b6b6b"/><span class="font-medium whitespace-nowrap">In-memory grid</span></div>
<div class="flex flex-col items-center gap-1 px-3 py-2 rounded-lg bg-white shadow-sm"><logos-aws-ecs class="w-6 h-6"/><span class="font-medium whitespace-nowrap">Internal adapters</span></div>
<div class="flex flex-col items-center gap-1 px-3 py-2 rounded-lg bg-white shadow-sm"><logos-mongodb-icon class="w-6 h-6"/><span class="font-medium whitespace-nowrap">MongoDB Atlas</span></div>
</div>
</div>

<div class="flex flex-col items-center shrink-0 w-12"><lucide-arrow-right class="w-5 h-5 opacity-40"/><span class="opacity-50 text-center leading-tight mt-0.5">DX/VPN</span></div>

<div class="flex flex-col items-center gap-1 w-20 shrink-0"><lucide-building-2 class="w-7 h-7" style="color:#6b6b6b"/><span class="font-semibold text-center leading-tight">On-prem</span><span class="opacity-50 text-center leading-tight">PTS, PWM, data</span></div>

</div>

<div class="mt-4 text-center text-sm opacity-60">Issuers and EAMs enter through the external account. PTS and PWM traders reach the business logic from on-prem, over the private link.</div>

<div class="mt-3 flex justify-center"><span class="flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-medium border shadow-sm bg-white" style="border-color:var(--pictet-red);color:var(--pictet-red)"><lucide-file-check class="w-3.5 h-3.5"/>Each building block will be validated with an ADR</span></div>

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
issuer adapters. Internal account holds the core, internal adapters and Atlas, reaching on-prem via
DX/VPN. VPC inspector between, HTTPS only. Atlas keeps the same engine for the cutover, zero
compatibility risk. The in-memory grid and the switch to DocumentDB are phase 2 work.


Sous validation des ADRs en cours.
-->

---

# Target architecture, step 2: cloud-native

<div class="text-sm opacity-70 -mt-1">Same accounts, same flows, same security model as step 1. The refactor changes six things inside them.</div>

<div class="mt-5 max-w-4xl mx-auto">

<div class="grid grid-cols-[84px_235px_24px_235px_1fr] items-center gap-x-2 mb-1.5 text-xs">
<div></div>
<div class="text-[0.6rem] uppercase tracking-widest font-bold text-center" style="color:#A04044">After step 1</div>
<div></div>
<div class="text-[0.6rem] uppercase tracking-widest font-bold text-center" style="color:#29445A">After step 2</div>
<div></div>
</div>

<div class="flex flex-col gap-2 text-sm">

<div class="grid grid-cols-[84px_235px_24px_235px_1fr] items-center gap-x-2">
<div class="text-[0.65rem] uppercase tracking-widest opacity-50 text-right pr-1">Ingress</div>
<div class="flex items-center justify-center gap-2 px-3 py-1.5 rounded-lg border bg-white" style="border-color:#dcb0b3"><logos-aws-waf class="w-4 h-4"/>WAF + ALB</div>
<lucide-arrow-right class="w-4 h-4 opacity-40 mx-auto"/>
<div class="flex items-center justify-center gap-2 px-3 py-1.5 rounded-lg border-2 bg-white" style="border-color:#29445A"><logos-aws-api-gateway class="w-4 h-4"/>API Gateway + WAF</div>
<div class="text-xs opacity-55">throttling and auth at the edge</div>
</div>

<div class="grid grid-cols-[84px_235px_24px_235px_1fr] items-center gap-x-2">
<div class="text-[0.65rem] uppercase tracking-widest opacity-50 text-right pr-1">Adapters</div>
<div class="flex items-center justify-center gap-2 px-3 py-1.5 rounded-lg border bg-white" style="border-color:#dcb0b3"><logos-aws-fargate class="w-4 h-4"/>Containers, always on</div>
<lucide-arrow-right class="w-4 h-4 opacity-40 mx-auto"/>
<div class="flex items-center justify-center gap-2 px-3 py-1.5 rounded-lg border-2 bg-white" style="border-color:#29445A"><logos-aws-lambda class="w-4 h-4"/>Lambda functions</div>
<div class="text-xs opacity-55">scale to zero, pay per call</div>
</div>

<div class="grid grid-cols-[84px_235px_24px_235px_1fr] items-center gap-x-2">
<div class="text-[0.65rem] uppercase tracking-widest opacity-50 text-right pr-1">Business logic</div>
<div class="flex items-center justify-center gap-2 px-3 py-1.5 rounded-lg border bg-white" style="border-color:#dcb0b3"><logos-aws-fargate class="w-4 h-4"/>Stateful, fixed size</div>
<lucide-arrow-right class="w-4 h-4 opacity-40 mx-auto"/>
<div class="flex items-center justify-center gap-2 px-3 py-1.5 rounded-lg border-2 bg-white" style="border-color:#29445A"><logos-aws-fargate class="w-4 h-4"/>Stateless, elastic</div>
<div class="text-xs opacity-55">sized to load, not to peak</div>
</div>

<div class="grid grid-cols-[84px_235px_24px_235px_1fr] items-center gap-x-2">
<div class="text-[0.65rem] uppercase tracking-widest opacity-50 text-right pr-1">State</div>
<div class="flex items-center justify-center gap-2 px-3 py-1.5 rounded-lg border bg-white" style="border-color:#dcb0b3"><lucide-database class="w-4 h-4"/>In-memory data grid</div>
<lucide-arrow-right class="w-4 h-4 opacity-40 mx-auto"/>
<div class="flex items-center justify-center gap-2 px-3 py-1.5 rounded-lg border-2 bg-white" style="border-color:#29445A"><logos-aws-documentdb class="w-4 h-4"/>DocumentDB</div>
<div class="text-xs opacity-55">state survives restarts</div>
</div>

<div class="grid grid-cols-[84px_235px_24px_235px_1fr] items-center gap-x-2">
<div class="text-[0.65rem] uppercase tracking-widest opacity-50 text-right pr-1">Database</div>
<div class="flex items-center justify-center gap-2 px-3 py-1.5 rounded-lg border bg-white" style="border-color:#dcb0b3"><logos-mongodb-icon class="w-4 h-4"/>MongoDB Atlas</div>
<lucide-arrow-right class="w-4 h-4 opacity-40 mx-auto"/>
<div class="flex items-center justify-center gap-2 px-3 py-1.5 rounded-lg border-2 bg-white" style="border-color:#29445A"><logos-aws-documentdb class="w-4 h-4"/>DocumentDB</div>
<div class="text-xs opacity-55">same API, a fraction of the run cost</div>
</div>

<div class="grid grid-cols-[84px_235px_24px_235px_1fr] items-center gap-x-2">
<div class="text-[0.65rem] uppercase tracking-widest opacity-50 text-right pr-1">Integration</div>
<div class="flex items-center justify-center gap-2 px-3 py-1.5 rounded-lg border bg-white" style="border-color:#dcb0b3"><lucide-arrow-left-right class="w-4 h-4"/>Point-to-point calls</div>
<lucide-arrow-right class="w-4 h-4 opacity-40 mx-auto"/>
<div class="flex items-center justify-center gap-2 px-3 py-1.5 rounded-lg border-2 bg-white" style="border-color:#29445A"><logos-aws-eventbridge class="w-4 h-4"/>EventBridge</div>
<div class="text-xs opacity-55">decoupled, replayable events</div>
</div>

</div>

<div class="mt-4 text-center text-[0.7rem] opacity-45">Everything else carries over from step 1: the two accounts, the VPC inspector, DX/VPN to on-prem, observability.</div>

<div class="mt-3 flex justify-center"><span class="flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-medium border shadow-sm bg-white" style="border-color:var(--pictet-red);color:var(--pictet-red)"><lucide-file-check class="w-3.5 h-3.5"/>Each change will be validated with an ADR</span></div>

</div>

<!--
After the cloud-native refactor: issuer and internal adapters run as Lambdas behind API Gateway,
the core is stateless and scales horizontally on Fargate, state lives in Amazon DocumentDB, and the
in-memory database is removed. Function workloads move to FaaS, event-driven through EventBridge.
-->

---

# A two-phase migration

<div class="text-sm opacity-70 -mt-1">Business continuity first, cloud-native gains next.</div>

<div class="grid grid-cols-2 gap-6 mt-5 text-left text-sm items-start">

<div>
<div class="text-xs uppercase tracking-widest mb-3" style="color: var(--pictet-red)">Phase 1: Replatform</div>
<div class="flex flex-col gap-3">
<div class="p-4 rounded-xl bg-white border border-gray-200 shadow-md flex items-center gap-3"><div class="w-10 h-10 rounded-lg flex items-center justify-center shrink-0" style="background:#f6e7e8"><lucide-copy class="w-5 h-5" style="color:var(--pictet-red)"/></div><div><b>Iso-functional, simpler stack</b><br/><span class="text-xs opacity-60">same app behavior, managed services replace the hybrid setup</span></div></div>
<div class="p-4 rounded-xl bg-white border border-gray-200 shadow-md flex items-center gap-3"><div class="w-10 h-10 rounded-lg flex items-center justify-center shrink-0" style="background:#f6e7e8"><lucide-scale class="w-5 h-5" style="color:var(--pictet-red)"/></div><div><b>Parity</b><br/><span class="text-xs opacity-60">performance, security, resilience and audit at least equivalent</span></div></div>
<div class="p-4 rounded-xl bg-white border border-gray-200 shadow-md flex items-center gap-3"><div class="w-10 h-10 rounded-lg flex items-center justify-center shrink-0" style="background:#f6e7e8"><lucide-workflow class="w-5 h-5" style="color:var(--pictet-red)"/></div><div><b>Modern operations</b><br/><span class="text-xs opacity-60">single push-based CI/CD, IaC, blue/green deploys</span></div></div>
</div>
</div>

<div>
<div class="text-xs uppercase tracking-widest mb-3 opacity-50">Phase 2: Leverage the cloud</div>
<div class="flex flex-col gap-3">
<div class="p-4 rounded-xl bg-white border border-gray-200 shadow-md flex items-center gap-3"><div class="w-10 h-10 rounded-lg flex items-center justify-center shrink-0" style="background:#f6e7e8"><lucide-trending-up class="w-5 h-5" style="color:var(--pictet-red)"/></div><div><b>Elasticity</b><br/><span class="text-xs opacity-60">autoscaling on demand, scale down to 20% on nights and weekends</span></div></div>
<div class="p-4 rounded-xl bg-white border border-gray-200 shadow-md flex items-center gap-3"><div class="w-10 h-10 rounded-lg flex items-center justify-center shrink-0" style="background:#f6e7e8"><lucide-heart-pulse class="w-5 h-5" style="color:var(--pictet-red)"/></div><div><b>High availability</b><br/><span class="text-xs opacity-60">multi-AZ, self-healing, automated DR and failover tests</span></div></div>
<div class="p-4 rounded-xl bg-white border border-gray-200 shadow-md flex items-center gap-3"><div class="w-10 h-10 rounded-lg flex items-center justify-center shrink-0" style="background:#f6e7e8"><lucide-zap class="w-5 h-5" style="color:var(--pictet-red)"/></div><div><b>Serverless and cloud-native</b><br/><span class="text-xs opacity-60">FaaS adapters on Lambda, DocumentDB, no in-memory database</span></div></div>
</div>
</div>

</div>

<!--
Phase 1 de-risks the cutover: same app, new ground. Phase 2 is where the cloud pays off,
once the Pictet AWS platform services are available.
-->

---

# Roadmap

<div class="text-sm opacity-70 -mt-1">An estimated timeline: migrate first to reach parity, then modernize. Phased from 2026 to mid 2029.</div>

<div class="mt-6 text-[13px]">

<div class="relative">

<div class="absolute top-0 bottom-0 pointer-events-none" style="left:200px;right:8px">
<div class="absolute top-0 bottom-0 w-px bg-gray-200" style="left:0%"></div>
<div class="absolute top-0 bottom-0 w-px bg-gray-200" style="left:28.6%"></div>
<div class="absolute top-0 bottom-0 w-px bg-gray-200" style="left:57.1%"></div>
<div class="absolute top-0 bottom-0 w-px bg-gray-200" style="left:85.7%"></div>
</div>

<div class="text-xs uppercase tracking-widest font-semibold mb-1" style="color:var(--pictet-red)">Migrate</div>

<div class="flex items-center h-7"><div class="shrink-0 pr-3 text-right opacity-80" style="width:200px">Preparation and POC</div><div class="flex-1 relative h-full"><div class="absolute top-1/2 -translate-y-1/2 h-4 rounded shadow-sm" style="left:9.5%;width:11.9%;background:#A04044"></div><div class="absolute top-1/2 -translate-y-1/2 text-[10px] italic opacity-70 whitespace-nowrap" style="left:22.2%">POC OK</div></div></div>
<div class="flex items-center h-7"><div class="shrink-0 pr-3 text-right opacity-80" style="width:200px">Migrate INTG</div><div class="flex-1 relative h-full"><div class="absolute top-1/2 -translate-y-1/2 h-4 rounded shadow-sm" style="left:21.4%;width:7.2%;background:#A04044"></div><div class="absolute top-1/2 -translate-y-1/2 text-[10px] italic opacity-70 whitespace-nowrap" style="left:29.4%">INTG live</div></div></div>
<div class="flex items-center h-7"><div class="shrink-0 pr-3 text-right opacity-80" style="width:200px">Migrate CTLQ</div><div class="flex-1 relative h-full"><div class="absolute top-1/2 -translate-y-1/2 h-4 rounded shadow-sm" style="left:28.6%;width:7.1%;background:#A04044"></div><div class="absolute top-1/2 -translate-y-1/2 text-[10px] italic opacity-70 whitespace-nowrap" style="left:36.5%">CTLQ live</div></div></div>
<div class="flex items-center h-7"><div class="shrink-0 pr-3 text-right opacity-80" style="width:200px">Migrate PROD</div><div class="flex-1 relative h-full"><div class="absolute top-1/2 -translate-y-1/2 h-4 rounded shadow-sm" style="left:35.7%;width:7.2%;background:#A04044"></div><div class="absolute top-1/2 -translate-y-1/2 text-[10px] italic font-semibold opacity-80 whitespace-nowrap" style="left:43.7%">PROD live</div></div></div>
<div class="flex items-center h-7"><div class="shrink-0 pr-3 text-right opacity-80" style="width:200px">Decommission on-prem</div><div class="flex-1 relative h-full"><div class="absolute top-1/2 -translate-y-1/2 h-4 rounded shadow-sm" style="left:38.1%;width:9.5%;background:#A04044"></div></div></div>

<div class="text-xs uppercase tracking-widest font-semibold mt-5 mb-2" style="color:#29445A">Make LionX cloud native</div>

<div class="flex items-center h-7"><div class="shrink-0 pr-3 text-right opacity-80" style="width:200px">Elastic compute</div><div class="flex-1 relative h-full"><div class="absolute top-1/2 -translate-y-1/2 h-4 rounded-l shadow-sm" style="left:28.6%;width:28.5%;background:#29445A"></div><div class="absolute top-1/2 -translate-y-1/2 h-4 rounded-r" style="left:57.1%;width:5.7%;background:#29445A;opacity:0.35"></div></div></div>
<div class="flex items-center h-7"><div class="shrink-0 pr-3 text-right opacity-80" style="width:200px">Function workloads to FaaS</div><div class="flex-1 relative h-full"><div class="absolute top-1/2 -translate-y-1/2 h-4 rounded-l shadow-sm" style="left:42.9%;width:28.5%;background:#29445A"></div><div class="absolute top-1/2 -translate-y-1/2 h-4 rounded-r" style="left:71.4%;width:5.7%;background:#29445A;opacity:0.35"></div></div></div>
<div class="flex items-center h-7"><div class="shrink-0 pr-3 text-right opacity-80" style="width:200px">Replace in-memory database</div><div class="flex-1 relative h-full"><div class="absolute top-1/2 -translate-y-1/2 h-4 rounded-l shadow-sm" style="left:42.9%;width:34.5%;background:#29445A"></div><div class="absolute top-1/2 -translate-y-1/2 h-4 rounded-r" style="left:77.4%;width:7.1%;background:#29445A;opacity:0.35"></div></div></div>
<div class="flex items-center h-7"><div class="shrink-0 pr-3 text-right opacity-80" style="width:200px">Run and optimize</div><div class="flex-1 relative h-full"><div class="absolute top-1/2 -translate-y-1/2 h-4 rounded-l shadow-sm" style="left:71.4%;width:23.8%;background:#29445A"></div><div class="absolute top-1/2 -translate-y-1/2 h-4 rounded-r" style="left:95.2%;width:4.8%;background:#29445A;opacity:0.35"></div></div></div>

<div class="absolute top-0 bottom-0 pointer-events-none" style="left:200px;right:8px">
<div class="absolute top-0 bottom-0" style="left:14.3%">
<div class="absolute top-0 bottom-0 left-0 w-0.5 -translate-x-1/2" style="background:var(--pictet-red)"></div>
<div class="absolute top-0 left-0 -translate-x-1/2 -translate-y-1 whitespace-nowrap text-[10px] font-bold px-1.5 py-0.5 rounded shadow-sm" style="color:#ffffff;background:var(--pictet-red)">We are here</div>
</div>
<div class="absolute top-0 bottom-0" style="left:47.6%">
<div class="absolute top-0 bottom-0 left-0 w-0.5 -translate-x-1/2" style="background:#2C5446"></div>
<div class="absolute top-0 left-0 -translate-x-1/2 -translate-y-1 whitespace-nowrap text-[10px] font-bold px-2 py-0.5 rounded-full shadow-md" style="color:#ffffff;background:#2C5446">Migration complete</div>
</div>
<div class="absolute top-0 bottom-0" style="left:77.4%">
<div class="absolute top-0 bottom-0 left-0 -translate-x-1/2 border-l border-dashed" style="border-color:#3D3A31;opacity:0.4"></div>
<div class="absolute top-0 left-0 -translate-x-1/2 -translate-y-1 whitespace-nowrap text-[10px] font-bold px-1.5 py-0.5 rounded shadow-sm" style="color:#ffffff;background:#3D3A31">Cloud-native</div>
</div>
</div>

</div>

<div class="flex mt-1.5">
<div class="shrink-0" style="width:200px"></div>
<div class="flex-1 relative h-4 text-xs opacity-55" style="margin-right:8px">
<span class="absolute -translate-x-1/2" style="left:0%">2026</span>
<span class="absolute -translate-x-1/2" style="left:28.6%">2027</span>
<span class="absolute -translate-x-1/2" style="left:57.1%">2028</span>
<span class="absolute -translate-x-1/2" style="left:85.7%">2029</span>
</div>
</div>

</div>

<div class="mt-3 flex justify-center gap-6 text-xs">
<span class="flex items-center gap-1.5"><span class="w-3 h-3 rounded-sm inline-block" style="background:#A04044"></span>Phase 1: migrate</span>
<span class="flex items-center gap-1.5"><span class="w-3 h-3 rounded-sm inline-block" style="background:#29445A"></span>Phase 2: cloud-native</span>
</div>

<div class="mt-2 text-center text-sm opacity-60">First environment live by end 2026, production on AWS by mid 2027.</div>

<!--
The first four phases get every environment to AWS and decommission on-prem. The modernization
phases overlap and continue after PROD: observability and security, then exiting GigaSpaces.

Detailler  INTG / CTLQ / PROD. vAjouter les jalons
-->

---

# Risks we are managing

<div class="text-sm opacity-70 -mt-1">Known upfront, with mitigation.</div>

<div class="grid grid-cols-2 grid-rows-2 gap-5 mt-5 h-[18rem] text-left">

<div class="p-5 rounded-xl bg-white border border-gray-200 shadow-md flex items-center gap-4"><div class="w-11 h-11 rounded-xl flex items-center justify-center shrink-0" style="background:#f6e7e8"><lucide-share-2 class="w-6 h-6" style="color:var(--pictet-red)"/></div><div><b class="text-base">Shared Pictet services</b><br/><span class="text-sm opacity-60">their maturity paces us, possible temporary dual monitoring</span></div></div>
<div class="p-5 rounded-xl bg-white border border-gray-200 shadow-md flex items-center gap-4"><div class="w-11 h-11 rounded-xl flex items-center justify-center shrink-0" style="background:#f6e7e8"><lucide-waypoints class="w-6 h-6" style="color:var(--pictet-red)"/></div><div><b class="text-base">Network complexity</b><br/><span class="text-sm opacity-60">on-prem links, issuer connectivity, firewall inspection</span></div></div>
<div class="p-5 rounded-xl bg-white border border-gray-200 shadow-md flex items-center gap-4"><div class="w-11 h-11 rounded-xl flex items-center justify-center shrink-0" style="background:#f6e7e8"><lucide-triangle-alert class="w-6 h-6" style="color:var(--pictet-red)"/></div><div><b class="text-base">Replatforming surprises</b><br/><span class="text-sm opacity-60">different IO, network and timeout behavior in the cloud</span></div></div>
<div class="p-5 rounded-xl bg-white border border-gray-200 shadow-md flex items-center gap-4"><div class="w-11 h-11 rounded-xl flex items-center justify-center shrink-0" style="background:#f6e7e8"><lucide-heart-pulse class="w-6 h-6" style="color:var(--pictet-red)"/></div><div><b class="text-base">Service continuity</b><br/><span class="text-sm opacity-60">adapting operations and on-call during ramp-up</span></div></div>

</div>

<div class="mt-5 text-center text-sm opacity-60">Each risk has an owner and a mitigation tracked in the migration plan.</div>

<!--
The biggest external dependency is the maturity of shared Pictet platform services. Ownership of
infra scanning and intrusion detection is still to be confirmed with the cyber-security team.|


Retirer point virguel
-->

---

# Migration effort: Phase 1

<div class="text-sm opacity-70 -mt-1">Estimated one-time effort to replatform onto AWS, CI/CD from Bamboo to GitHub included.</div>

<div class="mt-6 flex flex-col gap-2.5">

<div class="flex items-center gap-3"><div class="w-56 shrink-0 text-right text-sm opacity-80">AWS landing zone and network</div><div class="flex-1 h-5 rounded bg-gray-100 relative"><div class="absolute inset-y-0 left-0 rounded overflow-hidden flex" style="width:73%"><div class="h-full" style="width:83.33%;background:#A04044"></div><div class="h-full" style="width:16.67%;background:#A04044;opacity:0.38"></div></div></div><div class="w-16 text-right text-sm"><b>55</b> <span class="opacity-50 text-xs">MD</span></div></div>

<div class="flex items-center gap-3"><div class="w-56 shrink-0 text-right text-sm opacity-80">CI/CD, Bamboo to GitHub Actions</div><div class="flex-1 h-5 rounded bg-gray-100 relative"><div class="absolute inset-y-0 left-0 rounded overflow-hidden flex" style="width:40%"><div class="h-full" style="width:83.33%;background:#A04044"></div><div class="h-full" style="width:16.67%;background:#A04044;opacity:0.38"></div></div></div><div class="w-16 text-right text-sm"><b>30</b> <span class="opacity-50 text-xs">MD</span></div></div>

<div class="flex items-center gap-3"><div class="w-56 shrink-0 text-right text-sm opacity-80">App replatform on ECS/Fargate</div><div class="flex-1 h-5 rounded bg-gray-100 relative"><div class="absolute inset-y-0 left-0 rounded overflow-hidden flex" style="width:73%"><div class="h-full" style="width:83.33%;background:#A04044"></div><div class="h-full" style="width:16.67%;background:#A04044;opacity:0.38"></div></div></div><div class="w-16 text-right text-sm"><b>55</b> <span class="opacity-50 text-xs">MD</span></div></div>

<div class="flex items-center gap-3"><div class="w-56 shrink-0 text-right text-sm opacity-80">Data migration, managed services</div><div class="flex-1 h-5 rounded bg-gray-100 relative"><div class="absolute inset-y-0 left-0 rounded overflow-hidden flex" style="width:53%"><div class="h-full" style="width:83.33%;background:#A04044"></div><div class="h-full" style="width:16.67%;background:#A04044;opacity:0.38"></div></div></div><div class="w-16 text-right text-sm"><b>40</b> <span class="opacity-50 text-xs">MD</span></div></div>

<div class="flex items-center gap-3"><div class="w-56 shrink-0 text-right text-sm opacity-80">Testing, cutover and rollout</div><div class="flex-1 h-5 rounded bg-gray-100 relative"><div class="absolute inset-y-0 left-0 rounded overflow-hidden flex" style="width:100%"><div class="h-full" style="width:83.33%;background:#A04044"></div><div class="h-full" style="width:16.67%;background:#A04044;opacity:0.38"></div></div></div><div class="w-16 text-right text-sm"><b>75</b> <span class="opacity-50 text-xs">MD</span></div></div>

<div class="flex items-center gap-3"><div class="w-56 shrink-0 text-right text-sm opacity-80">Project management</div><div class="flex-1 h-5 rounded bg-gray-100 relative"><div class="absolute inset-y-0 left-0 rounded overflow-hidden flex" style="width:60%"><div class="h-full" style="width:83.33%;background:#A04044"></div><div class="h-full" style="width:16.67%;background:#A04044;opacity:0.38"></div></div></div><div class="w-16 text-right text-sm"><b>45</b> <span class="opacity-50 text-xs">MD</span></div></div>

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
Migration effort phase 1. 
++ Couts aujourd'hui // Avant et apres pour le TCO ++++ Jour homme dev // pour mettre en evidence RED = Phase 1.
-->

---

# Migration effort: Phase 2

<div class="text-sm opacity-70 -mt-1">Development effort for the cloud-native refactor. A rougher estimate than Phase 1, higher uncertainty.</div>

<div class="mt-6 flex flex-col gap-2.5">

<div class="flex items-center gap-3"><div class="w-56 shrink-0 text-right text-sm opacity-80">Replace the in-memory database</div><div class="flex-1 h-5 rounded bg-gray-100 relative"><div class="absolute inset-y-0 left-0 rounded overflow-hidden flex" style="width:100%"><div class="h-full" style="width:83.33%;background:#29445A"></div><div class="h-full" style="width:16.67%;background:#29445A;opacity:0.38"></div></div></div><div class="w-16 text-right text-sm"><b>120</b> <span class="opacity-50 text-xs">MD</span></div></div>

<div class="flex items-center gap-3"><div class="w-56 shrink-0 text-right text-sm opacity-80">Stateless, elastic core</div><div class="flex-1 h-5 rounded bg-gray-100 relative"><div class="absolute inset-y-0 left-0 rounded overflow-hidden flex" style="width:66.7%"><div class="h-full" style="width:83.33%;background:#29445A"></div><div class="h-full" style="width:16.67%;background:#29445A;opacity:0.38"></div></div></div><div class="w-16 text-right text-sm"><b>80</b> <span class="opacity-50 text-xs">MD</span></div></div>

<div class="flex items-center gap-3"><div class="w-56 shrink-0 text-right text-sm opacity-80">Function workloads to FaaS</div><div class="flex-1 h-5 rounded bg-gray-100 relative"><div class="absolute inset-y-0 left-0 rounded overflow-hidden flex" style="width:58.3%"><div class="h-full" style="width:83.33%;background:#29445A"></div><div class="h-full" style="width:16.67%;background:#29445A;opacity:0.38"></div></div></div><div class="w-16 text-right text-sm"><b>70</b> <span class="opacity-50 text-xs">MD</span></div></div>

<div class="flex items-center gap-3"><div class="w-56 shrink-0 text-right text-sm opacity-80">Event-driven and observability</div><div class="flex-1 h-5 rounded bg-gray-100 relative"><div class="absolute inset-y-0 left-0 rounded overflow-hidden flex" style="width:50%"><div class="h-full" style="width:83.33%;background:#29445A"></div><div class="h-full" style="width:16.67%;background:#29445A;opacity:0.38"></div></div></div><div class="w-16 text-right text-sm"><b>60</b> <span class="opacity-50 text-xs">MD</span></div></div>

<div class="flex items-center gap-3"><div class="w-56 shrink-0 text-right text-sm opacity-80">Testing and hardening</div><div class="flex-1 h-5 rounded bg-gray-100 relative"><div class="absolute inset-y-0 left-0 rounded overflow-hidden flex" style="width:50%"><div class="h-full" style="width:83.33%;background:#29445A"></div><div class="h-full" style="width:16.67%;background:#29445A;opacity:0.38"></div></div></div><div class="w-16 text-right text-sm"><b>60</b> <span class="opacity-50 text-xs">MD</span></div></div>

<div class="flex items-center gap-3"><div class="w-56 shrink-0 text-right text-sm opacity-80">Project management</div><div class="flex-1 h-5 rounded bg-gray-100 relative"><div class="absolute inset-y-0 left-0 rounded overflow-hidden flex" style="width:33.3%"><div class="h-full" style="width:83.33%;background:#29445A"></div><div class="h-full" style="width:16.67%;background:#29445A;opacity:0.38"></div></div></div><div class="w-16 text-right text-sm"><b>40</b> <span class="opacity-50 text-xs">MD</span></div></div>

</div>

<div class="flex justify-center gap-6 text-xs mt-3">
<span class="flex items-center gap-1.5"><span class="w-3 h-3 rounded-sm inline-block" style="background:#29445A"></span>estimate</span>
<span class="flex items-center gap-1.5"><span class="w-3 h-3 rounded-sm inline-block" style="background:#29445A;opacity:0.38"></span>20% margin</span>
</div>

<div class="mt-5 flex items-center justify-center gap-16 text-center">
<div><div class="text-3xl font-bold" style="color:#29445A">~520</div><div class="text-xs opacity-55">man-days (430 + 20% margin)</div></div>
<div><div class="text-3xl font-bold" style="color:#29445A">~2.3</div><div class="text-xs opacity-55">FTE-year</div></div>
</div>

<!--
Phase 2 = cloud-native refactor. Development estimate, higher uncertainty than Phase 1. The
in-memory database removal is the main driver. Bottom-up, to be refined with the team.
-->

---

# The cost curve

<div class="text-sm opacity-70 -mt-1">An estimate of the run cost, in CHF per year, from Zurich list prices, plus 25% contingency.</div>

<div class="mt-12 flex justify-center" style="height:310px">
<div style="position:relative;width:760px;height:235px;transform:scale(1.3);transform-origin:top center">
<svg viewBox="0 0 760 235" width="760" height="235" style="position:absolute;inset:0">
<defs>
<linearGradient id="phase1" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#A04044" stop-opacity="0.16"/><stop offset="100%" stop-color="#A04044" stop-opacity="0"/></linearGradient>
<linearGradient id="phase2" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#29445A" stop-opacity="0.16"/><stop offset="100%" stop-color="#29445A" stop-opacity="0"/></linearGradient>
</defs>
<path d="M120,62 L400,71 L400,180 L120,180 Z" fill="url(#phase1)"/>
<path d="M400,71 L660,88 L660,180 L400,180 Z" fill="url(#phase2)"/>
<line x1="120" y1="180" x2="660" y2="180" stroke="#e3e3e3" stroke-width="1"/>
<line x1="120" y1="62" x2="672" y2="62" stroke="#cfcfcf" stroke-width="1" stroke-dasharray="3 4"/>
<path d="M120,135 L400,144" fill="none" stroke="#A04044" stroke-width="2" stroke-dasharray="6 5" stroke-linecap="round" stroke-opacity="0.75"/>
<path d="M400,144 L660,152" fill="none" stroke="#29445A" stroke-width="2" stroke-dasharray="6 5" stroke-linecap="round" stroke-opacity="0.75"/>
<circle cx="120" cy="135" r="3" fill="#A04044"/><circle cx="400" cy="144" r="3" fill="#A04044"/><circle cx="660" cy="152" r="3" fill="#29445A"/>
<path d="M120,62 L400,71" fill="none" stroke="#A04044" stroke-width="4" stroke-linecap="round"/>
<path d="M400,71 L660,88" fill="none" stroke="#29445A" stroke-width="4" stroke-linecap="round" stroke-dasharray="10 8"/>
<circle cx="120" cy="62" r="6" fill="#A04044" stroke="#fff" stroke-width="2.5"/>
<circle cx="400" cy="71" r="6" fill="#A04044" stroke="#fff" stroke-width="2.5"/>
<circle cx="660" cy="88" r="8" fill="#29445A" stroke="#fff" stroke-width="2.5"/>
</svg>
<div style="position:absolute;left:120px;top:48px;transform:translate(-50%,-100%);font-weight:bold;font-size:17px;color:#3D3A31">650k</div>
<div style="position:absolute;left:400px;top:57px;transform:translate(-50%,-100%);font-weight:bold;font-size:16px;color:#3D3A31">~600k</div>
<div style="position:absolute;left:432px;top:39px;font-weight:bold;font-size:11px;color:#fff;background:#A04044;border-radius:10px;padding:1px 8px">-8%</div>
<div style="position:absolute;left:645px;top:73px;transform:translate(-50%,-100%);font-weight:bold;font-size:16px;color:#3D3A31">~505k</div>
<div style="position:absolute;left:684px;top:54px;font-weight:bold;font-size:11px;color:#fff;background:#29445A;border-radius:10px;padding:1px 8px">-22%</div>
<div style="position:absolute;left:260px;top:97px;transform:translateX(-50%);font-size:11px;letter-spacing:0.08em;text-transform:uppercase;color:#8a8f95">Team</div>
<div style="position:absolute;left:400px;top:101px;transform:translateX(-50%);font-size:11px;font-weight:600;color:#9aa0a6">400k</div>
<div style="position:absolute;left:600px;top:111px;transform:translateX(-50%);font-size:11px;font-weight:600;color:#9aa0a6">~350k</div>
<div style="position:absolute;left:255px;top:153px;font-size:11px;letter-spacing:0.08em;text-transform:uppercase;color:#8a8f95">Infra</div>
<div style="position:absolute;left:120px;top:140px;transform:translateX(-50%);font-size:11px;font-weight:600;color:#9aa0a6">250k</div>
<div style="position:absolute;left:400px;top:149px;transform:translateX(-50%);font-size:11px;font-weight:600;color:#9aa0a6">~200k</div>
<div style="position:absolute;left:660px;top:156px;transform:translateX(-50%);font-size:11px;font-weight:600;color:#9aa0a6">~155k</div>
<div style="position:absolute;left:120px;top:190px;transform:translateX(-50%);text-align:center"><div style="font-size:13px;font-weight:600;color:#3D3A31">On-prem</div><div style="font-size:11px;color:#9aa0a6">today</div></div>
<div style="position:absolute;left:400px;top:190px;transform:translateX(-50%);text-align:center"><div style="font-size:13px;font-weight:600;color:#A04044">Replatform</div><div style="font-size:11px;color:#9aa0a6">Phase 1, iso-functional</div></div>
<div style="position:absolute;left:660px;top:190px;transform:translateX(-50%);text-align:center"><div style="font-size:13px;font-weight:600;color:#29445A">Cloud-native</div><div style="font-size:11px;color:#9aa0a6">Phase 2, optimised</div></div>
</div>
</div>


<!--
Run cost is operations only. Infra is provisional and pre-PoC. The decisive milestone is the
integration environment on AWS at the end of 2026, inside a real pipeline.


Ca ressemble trop a un avant apres.
Ajouter une marge. Replatforming, entre 180-200. Actuel vs futur
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

<!--
Manquant:

Partie dev (Migration chiffrage),
TCO actuel,
Revoir les marges, ne pas que ca ressemble a un avant apres.
Ajouter les jalons projet. Ajouter "sous validation des ADRs" dans la slide archi
-->
