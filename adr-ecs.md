---
theme: seriph
title: "ADR-0001: LionX on ECS"
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

# LionX compute: Amazon ECS

<div class="opacity-70 mt-2">LionX is moving to AWS. First decision to lock in: where its services run.</div>

<div class="mt-8 flex items-center justify-center gap-10">
<div class="flex flex-col items-center gap-2"><div class="w-16 h-16 rounded-2xl flex items-center justify-center bg-white border-2 shadow-md" style="border-color:var(--pictet-red)"><logos-aws-ecs class="w-9 h-9"/></div><span class="text-xs font-semibold">ECS Fargate</span></div>
<div class="flex flex-col items-center gap-2 opacity-40"><div class="w-16 h-16 rounded-2xl flex items-center justify-center bg-white border border-gray-200"><logos-aws-ec2 class="w-9 h-9"/></div><span class="text-xs">ECS on EC2</span></div>
<div class="flex flex-col items-center gap-2 opacity-40"><div class="w-16 h-16 rounded-2xl flex items-center justify-center bg-white border border-gray-200"><logos-aws-eks class="w-9 h-9"/></div><span class="text-xs">EKS</span></div>
</div>

<div class="mt-8 flex items-center justify-center gap-2 text-xs">
<span class="px-3 py-1.5 rounded-lg bg-white border border-gray-200 shadow-sm">The options</span>
<lucide-chevron-right class="w-3.5 h-3.5 opacity-30"/>
<span class="px-3 py-1.5 rounded-lg bg-white border border-gray-200 shadow-sm">The numbers</span>
<lucide-chevron-right class="w-3.5 h-3.5 opacity-30"/>
<span class="px-3 py-1.5 rounded-lg bg-white border border-gray-200 shadow-sm">Our recommendation</span>
<lucide-chevron-right class="w-3.5 h-3.5 opacity-30"/>
<span class="px-3 py-1.5 rounded-lg font-semibold text-white shadow-sm" style="background:var(--pictet-red)">Your GO</span>
</div>

<div class="mt-8 flex items-center justify-center gap-3 text-xs">
<span class="px-3 py-1 rounded-full font-semibold" style="background:#fdf3e3;color:#946200">ADR-0001, proposed</span>
<span class="opacity-50">2026-06-26</span>
<span class="opacity-50">Sofiane DJERBI, Bayarbileg BATBILEG, Rui SOUSA CALDAS, Laurent QUILLÉROU</span>
</div>

<!--
Set the frame in one breath: LionX moves to AWS, the compute platform is the first decision that
everything else hangs off, we compare three options with numbers, and we leave the room with a GO.
The full ADR is on the repo, this deck is the summary for ratification. About 5 minutes.
-->

---

# The decision, and what drives it

<div class="text-sm opacity-70 -mt-1">One choice to make: where LionX compute runs on AWS.</div>

<div class="mt-6 grid grid-cols-[2fr_3fr] gap-6 max-w-4xl mx-auto text-left items-stretch">

<div class="rounded-2xl border border-gray-200 bg-white shadow-md p-6 flex flex-col" style="border-top:3px solid var(--pictet-red)">
<div class="text-[0.65rem] uppercase tracking-widest opacity-50">The workload</div>
<div class="flex-1 flex flex-col justify-center gap-5">
<div class="flex items-center gap-3.5">
<div class="w-11 h-11 rounded-xl flex items-center justify-center shrink-0" style="background:#f6e7e8"><lucide-server class="w-6 h-6" style="color:var(--pictet-red)"/></div>
<div><div class="text-lg font-bold leading-tight" style="color:#3D3A31">8 services</div><div class="text-xs opacity-55">long-running, plus cron</div></div>
</div>
<div class="flex items-center gap-3.5">
<div class="w-11 h-11 rounded-xl flex items-center justify-center shrink-0" style="background:#f6e7e8"><lucide-activity class="w-6 h-6" style="color:var(--pictet-red)"/></div>
<div><div class="text-lg font-bold leading-tight" style="color:#3D3A31">8 vCPU, 32 GB</div><div class="text-xs opacity-55">per environment</div></div>
</div>
<div class="flex items-center gap-3.5">
<div class="w-11 h-11 rounded-xl flex items-center justify-center shrink-0" style="background:#f6e7e8"><lucide-layers class="w-6 h-6" style="color:var(--pictet-red)"/></div>
<div><div class="text-lg font-bold leading-tight" style="color:#3D3A31">5 environments</div><div class="text-xs opacity-55">integration to production</div></div>
</div>
</div>
<div class="border-t border-gray-100 pt-3 mt-4 text-xs opacity-55 text-center">Networking, CI/CD, observability and IAM all hang off this choice.</div>
</div>

<div class="flex flex-col">
<div class="text-[0.65rem] uppercase tracking-widest opacity-50 mb-2.5">What drives the decision</div>
<div class="flex-1 flex flex-col justify-between gap-2.5">

<div class="flex items-center gap-3.5 px-4 py-3 rounded-xl bg-white border border-gray-200 shadow-md">
<div class="w-8 h-8 rounded-lg flex items-center justify-center text-sm font-bold shrink-0" style="background:#f6e7e8;color:var(--pictet-red)">1</div>
<div class="text-sm leading-snug"><b>End-2026 cutover.</b><br/><span class="text-xs opacity-55">The platform has to fit the migration runway, not the other way around.</span></div>
</div>

<div class="flex items-center gap-3.5 px-4 py-3 rounded-xl bg-white border border-gray-200 shadow-md">
<div class="w-8 h-8 rounded-lg flex items-center justify-center text-sm font-bold shrink-0" style="background:#f6e7e8;color:var(--pictet-red)">2</div>
<div class="text-sm leading-snug"><b>A rewrite either way.</b><br/><span class="text-xs opacity-55">The deployment layer is rewritten regardless. Today's cluster is a delivery vehicle, not a commitment.</span></div>
</div>

<div class="flex items-center gap-3.5 px-4 py-3 rounded-xl bg-white border border-gray-200 shadow-md">
<div class="w-8 h-8 rounded-lg flex items-center justify-center text-sm font-bold shrink-0" style="background:#f6e7e8;color:var(--pictet-red)">3</div>
<div class="text-sm leading-snug"><b>Audit surface stays minimal.</b><br/><span class="text-xs opacity-55">Every extra component is more to audit, scan, log and upgrade.</span></div>
</div>

<div class="flex items-center gap-3.5 px-4 py-3 rounded-xl bg-white border border-gray-200 shadow-md">
<div class="w-8 h-8 rounded-lg flex items-center justify-center text-sm font-bold shrink-0" style="background:#f6e7e8;color:var(--pictet-red)">4</div>
<div class="text-sm leading-snug"><b>A single workload.</b><br/><span class="text-xs opacity-55">No co-tenants to amortize a cluster's overhead against.</span></div>
</div>

</div>
</div>

</div>

<!--
The workload is small and well understood: eight services, one ALB in front, Mongo behind, cron on
the side. The four drivers are straight from the ADR. Ops time and audit surface decide this, not
the vendor bill.
-->

---

# Three options

<div class="text-sm opacity-70 -mt-1">Same workload on each, judged on what costs engineer time.</div>

<div class="mt-5 max-w-4xl mx-auto grid grid-cols-[190px_1fr_1fr_1fr] gap-1.5 text-xs items-stretch">

<div></div>
<div class="rounded-xl border-2 bg-white shadow-md px-3 py-3 text-center" style="border-color:var(--pictet-red)">
<logos-aws-ecs class="w-7 h-7 mx-auto"/><div class="font-bold text-sm mt-1 flex items-center justify-center gap-1.5">ECS Fargate<lucide-circle-check class="w-4 h-4" style="color:var(--pictet-red)"/></div>
<div class="text-[0.68rem] leading-snug opacity-60 mt-1.5">AWS's container orchestrator, serverless: we ship containers, AWS runs the machines</div>
</div>
<div class="rounded-xl border border-gray-200 bg-white shadow-sm px-3 py-3 text-center opacity-80"><logos-aws-ec2 class="w-7 h-7 mx-auto"/><div class="font-semibold text-sm mt-1">ECS on EC2</div>
<div class="text-[0.68rem] leading-snug opacity-60 mt-1.5">the same orchestrator, on EC2 virtual machines that we own and patch</div>
</div>
<div class="rounded-xl border border-gray-200 bg-white shadow-sm px-3 py-3 text-center opacity-80"><logos-aws-eks class="w-7 h-7 mx-auto"/><div class="font-semibold text-sm mt-1">EKS <span class="font-normal text-[0.6rem] opacity-50">standard to Auto Mode</span></div>
<div class="text-[0.68rem] leading-snug opacity-60 mt-1.5">managed Kubernetes: AWS hosts the control plane, we operate the cluster</div>
</div>

<div class="flex items-center justify-end pr-2 text-[0.65rem] uppercase tracking-widest opacity-50 text-right">Kubernetes to run</div>
<div class="rounded-lg px-3 py-2 flex items-center gap-2" style="background:#fdf3f4"><span class="w-2 h-2 rounded-full shrink-0" style="background:#2C5446"></span>none</div>
<div class="rounded-lg bg-gray-50 px-3 py-2 flex items-center gap-2"><span class="w-2 h-2 rounded-full shrink-0" style="background:#2C5446"></span>none</div>
<div class="rounded-lg bg-gray-50 px-3 py-2 flex items-center gap-2"><span class="w-2 h-2 rounded-full shrink-0" style="background:#A04044"></span>cluster, upgrades, GitOps</div>

<div class="flex items-center justify-end pr-2 text-[0.65rem] uppercase tracking-widest opacity-50 text-right">Node operations</div>
<div class="rounded-lg px-3 py-2 flex items-center gap-2" style="background:#fdf3f4"><span class="w-2 h-2 rounded-full shrink-0" style="background:#2C5446"></span>AWS's job</div>
<div class="rounded-lg bg-gray-50 px-3 py-2 flex items-center gap-2"><span class="w-2 h-2 rounded-full shrink-0" style="background:#A04044"></span>ours: AMIs, patching, CVEs</div>
<div class="rounded-lg bg-gray-50 px-3 py-2 flex items-center gap-2"><span class="w-2 h-2 rounded-full shrink-0" style="background:#946200"></span>ours, or AWS's with Auto Mode</div>

<div class="flex items-center justify-end pr-2 text-[0.65rem] uppercase tracking-widest opacity-50 text-right">Audit surface</div>
<div class="rounded-lg px-3 py-2 flex items-center gap-2" style="background:#fdf3f4"><span class="w-2 h-2 rounded-full shrink-0" style="background:#2C5446"></span>CloudTrail only</div>
<div class="rounded-lg bg-gray-50 px-3 py-2 flex items-center gap-2"><span class="w-2 h-2 rounded-full shrink-0" style="background:#A04044"></span>plus OS-level evidence</div>
<div class="rounded-lg bg-gray-50 px-3 py-2 flex items-center gap-2"><span class="w-2 h-2 rounded-full shrink-0" style="background:#946200"></span>plus Kubernetes audit logs</div>

<div class="flex items-center justify-end pr-2 text-[0.65rem] uppercase tracking-widest opacity-50 text-right">Ecosystem</div>
<div class="rounded-lg px-3 py-2 flex items-center gap-2" style="background:#fdf3f4"><span class="w-2 h-2 rounded-full shrink-0" style="background:#946200"></span>cron via EventBridge, no Helm</div>
<div class="rounded-lg bg-gray-50 px-3 py-2 flex items-center gap-2"><span class="w-2 h-2 rounded-full shrink-0" style="background:#946200"></span>cron via EventBridge, no Helm</div>
<div class="rounded-lg bg-gray-50 px-3 py-2 flex items-center gap-2"><span class="w-2 h-2 rounded-full shrink-0" style="background:#2C5446"></span>CronJob, Helm, operators</div>

<div class="flex items-center justify-end pr-2 text-[0.65rem] uppercase tracking-widest opacity-50 text-right">Fit for LionX</div>
<div class="rounded-lg px-3 py-2 flex items-center gap-2" style="background:#fdf3f4"><span class="w-2 h-2 rounded-full shrink-0" style="background:#2C5446"></span>runs it all, nothing unused</div>
<div class="rounded-lg bg-gray-50 px-3 py-2 flex items-center gap-2"><span class="w-2 h-2 rounded-full shrink-0" style="background:#946200"></span>runs everything, ops attached</div>
<div class="rounded-lg bg-gray-50 px-3 py-2 flex items-center gap-2"><span class="w-2 h-2 rounded-full shrink-0" style="background:#A04044"></span>richer ecosystem, unused</div>


</div>

<div class="mt-4 text-center text-xs opacity-50">The cheapest bill buys the most ops. Numbers on the next slide, full pros and cons in the ADR.</div>

<!--
Read it column by column. EC2 wins the bill and loses everywhere ops and audit are concerned.
EKS pays a platform tax for capabilities nothing in LionX uses. Fargate is green on everything
that costs engineer time.
-->

---

# The numbers

<div class="text-sm opacity-70 -mt-1">Yearly, for the LionX footprint. Zurich list prices with a 1-year Savings Plan, ops at a conservative $1,000 a day.</div>

<div class="mt-4 max-w-4xl mx-auto text-sm">

<div class="grid grid-cols-[190px_1fr_1fr_1fr] gap-1.5 items-stretch">
<div></div>
<div class="rounded-xl border-2 bg-white shadow-md px-3 py-2 text-center" style="border-color:var(--pictet-red)"><logos-aws-ecs class="w-6 h-6 mx-auto"/><div class="font-bold mt-0.5 flex items-center justify-center gap-1.5">ECS Fargate<lucide-circle-check class="w-4 h-4" style="color:var(--pictet-red)"/></div></div>
<div class="rounded-xl border border-gray-200 bg-white shadow-sm px-3 py-2 text-center opacity-80"><logos-aws-ec2 class="w-6 h-6 mx-auto"/><div class="font-semibold mt-0.5">ECS on EC2</div></div>
<div class="rounded-xl border border-gray-200 bg-white shadow-sm px-3 py-2 text-center opacity-80"><logos-aws-eks class="w-6 h-6 mx-auto"/><div class="font-semibold mt-0.5">EKS</div><div class="text-[0.6rem] opacity-50">standard to Auto Mode</div></div>
</div>

<div class="grid grid-cols-[190px_1fr_1fr_1fr] gap-1.5 items-stretch text-xs mt-2">
<div class="flex items-center justify-end pr-2 text-[0.65rem] uppercase tracking-widest opacity-50 text-right">Infra, per year</div>
<div class="rounded-lg px-3 py-2 text-center font-semibold" style="background:#fdf3f4">~$4.6K</div>
<div class="rounded-lg bg-gray-50 px-3 py-2 text-center font-semibold">~$3.1K</div>
<div class="rounded-lg bg-gray-50 px-3 py-2 text-center font-semibold">~$4.3K to 5.2K</div>
<div class="flex items-center justify-end pr-2 text-[0.65rem] uppercase tracking-widest opacity-50 text-right whitespace-nowrap">Ops, hours per month</div>
<div class="rounded-lg px-3 py-2 text-center font-semibold" style="background:#fdf3f4">~2 to 4</div>
<div class="rounded-lg bg-gray-50 px-3 py-2 text-center font-semibold">~10 to 20</div>
<div class="rounded-lg bg-gray-50 px-3 py-2 text-center font-semibold">~15 to 60</div>
<div class="flex items-center justify-end pr-2 text-[0.65rem] uppercase tracking-widest opacity-50 text-right">Ops, per year</div>
<div class="rounded-lg px-3 py-2 text-center font-semibold" style="background:#fdf3f4">~$3K to 6K</div>
<div class="rounded-lg bg-gray-50 px-3 py-2 text-center font-semibold">~$15K to 30K</div>
<div class="rounded-lg bg-gray-50 px-3 py-2 text-center font-semibold">~$23K to 90K</div>
</div>

<div class="grid grid-cols-[190px_1fr_1fr_1fr] gap-1.5 items-stretch mt-2.5">
<div class="flex items-center justify-end pr-2 text-[0.65rem] uppercase tracking-widest font-bold text-right whitespace-nowrap" style="color:#3D3A31">Fully loaded, per year</div>
<div class="rounded-lg px-3 py-2.5 text-center font-bold flex items-center justify-center gap-2" style="background:#fdf3f4"><span class="w-2 h-2 rounded-full shrink-0" style="background:#2C5446"></span>~$8K to 11K</div>
<div class="rounded-lg bg-gray-50 px-3 py-2.5 text-center font-bold flex items-center justify-center gap-2"><span class="w-2 h-2 rounded-full shrink-0" style="background:#946200"></span>~$18K to 33K</div>
<div class="rounded-lg bg-gray-50 px-3 py-2.5 text-center font-bold flex items-center justify-center gap-2"><span class="w-2 h-2 rounded-full shrink-0" style="background:#A04044"></span>~$27K to 95K</div>
</div>

</div>

<div class="mt-3 max-w-4xl mx-auto px-4 py-2 rounded-lg bg-white border border-gray-200 border-l-4 shadow-sm text-sm text-left" style="border-left-color:var(--pictet-red)"><b>Fully loaded, Fargate is the cheapest option, not the priciest.</b> <span class="text-xs opacity-55">Ops hours decide it.</span></div>

<div class="mt-2 text-center text-[0.68rem] opacity-45 whitespace-nowrap">Infra: eu-central-2 list prices, AWS Pricing API, July 2026. Ops: assumptions built from Encore, CloudAtler, CloudOptimo and Spectro Cloud.</div>
<div class="mt-0.5 text-center text-[0.68rem] opacity-45 whitespace-nowrap">Not measurements. Sourced and detailed per EKS variant in the ADR.</div>

<!--
Rates re-verified against the Pricing API: Fargate 0.05448/vCPU-h and 0.00598/GB-h, m5.xlarge
0.253/h, EKS control plane 0.10/h, Auto Mode fee 0.03036/h per m5.xlarge. The cost line does not
decide this ADR, the ops line does.
-->

---

# Decision: ECS Fargate

<div class="text-sm opacity-70 -mt-1">The smallest operational surface that runs all of LionX.</div>

<div class="mt-8 flex justify-center">
<div class="flex items-center gap-5 px-8 py-4 rounded-2xl bg-white border-2 shadow-md" style="border-color:var(--pictet-red)">
<logos-aws-ecs class="w-12 h-12"/>
<div class="text-left">
<div class="text-xl font-bold flex items-center gap-2" style="color:#3D3A31">ECS Fargate<lucide-circle-check class="w-5 h-5" style="color:var(--pictet-red)"/></div>
<div class="text-xs opacity-55">all eight services and the scheduled tasks, one runtime, zero nodes</div>
</div>
</div>
</div>

<div class="mt-8 grid grid-cols-3 gap-4 max-w-4xl mx-auto text-left text-xs">
<div class="px-4 py-3 rounded-lg bg-white border border-gray-200 border-l-4 shadow-sm" style="border-left-color:#2C5446"><b class="text-sm">Zero Kubernetes to run</b><br/><span class="opacity-55">no cluster, no CNI, no GitOps reconciler, no upgrade calendar</span></div>
<div class="px-4 py-3 rounded-lg bg-white border border-gray-200 border-l-4 shadow-sm" style="border-left-color:#2C5446"><b class="text-sm">One audit surface</b><br/><span class="opacity-55">CloudTrail end to end, host patching is AWS's responsibility</span></div>
<div class="px-4 py-3 rounded-lg bg-white border border-gray-200 border-l-4 shadow-sm" style="border-left-color:#2C5446"><b class="text-sm">Nothing blocks landing</b><br/><span class="opacity-55">no cluster standup on the critical path to end 2026</span></div>
</div>

<div class="mt-4 max-w-4xl mx-auto text-left text-xs px-4 py-2.5 rounded-lg bg-gray-50 border border-gray-200"><b>Accepted trade-offs.</b> Each schedule is an EventBridge rule plus an IAM role, more Terraform than a CronJob. The ecosystem is narrower than Kubernetes, and the difference would sit unused.</div>

<!--
The decision is only the compute platform. How traffic, cron and telemetry wire up belongs to the
target-architecture deck, not this ADR. The trade-offs are declaration-time verbosity, not
run-time risk.
-->

---

# Next steps

<div class="text-sm opacity-70 -mt-1">What we ask of you today.</div>

<div class="mt-8 grid grid-cols-3 gap-5 max-w-4xl mx-auto text-left">

<div class="p-5 rounded-xl bg-white border border-gray-200 shadow-md flex flex-col gap-3 h-full"><div class="w-11 h-11 rounded-xl flex items-center justify-center" style="background:#f6e7e8"><lucide-circle-help class="w-6 h-6" style="color:var(--pictet-red)"/></div><div><b class="text-base">Questions and objections</b><br/><span class="text-sm opacity-60">here and now, let's settle them in the room</span></div></div>

<div class="p-5 rounded-xl bg-white border border-gray-200 shadow-md flex flex-col gap-3 h-full"><div class="w-11 h-11 rounded-xl flex items-center justify-center" style="background:#f6e7e8"><lucide-circle-check class="w-6 h-6" style="color:var(--pictet-red)"/></div><div><b class="text-base">Ratify today</b><br/><span class="text-sm opacity-60">the ADR moves from proposed to accepted</span></div></div>

<div class="p-5 rounded-xl bg-white border border-gray-200 shadow-md flex flex-col gap-3 h-full"><div class="w-11 h-11 rounded-xl flex items-center justify-center" style="background:#f6e7e8"><lucide-rocket class="w-6 h-6" style="color:var(--pictet-red)"/></div><div><b class="text-base">PoC</b><br/><span class="text-sm opacity-60">pipeline, IAM boundaries and the cron path, end to end in the new AWS account</span></div></div>

</div>

<div class="mt-12 text-center">
<div class="text-xl font-semibold" style="color:var(--pictet-red)">The ask today: your GO on ECS Fargate.</div>
<div class="mt-2 text-sm opacity-60">Any questions? Let's settle them now and call it.</div>
</div>

<!--
Close on the ask. Review, ratify, then the PoC proves it end to end. The formal revisit conditions
live in the ADR, this room is about getting to accepted.
-->
