<script setup>
import { onMounted, onBeforeUnmount, ref } from 'vue'
import { Chart, registerables } from 'chart.js'

Chart.register(...registerables)

const RED = '#A04044'
const BLUE = '#29445A'

const el1 = ref()
const el2 = ref()
const charts = []

function doughnut(canvas, data) {
  return new Chart(canvas, {
    type: 'doughnut',
    data: {
      labels: ['Infrastructure', 'Team'],
      datasets: [{ data, backgroundColor: [RED, BLUE], borderColor: '#ffffff', borderWidth: 2 }],
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      animation: false,
      cutout: '64%',
      plugins: { legend: { display: false }, tooltip: { enabled: false } },
    },
  })
}

onMounted(() => {
  // USD. On-prem 2026 budget: infra 250k + team 400k = 650k (~1.0 FTE at
  // ~$414k/FTE-yr). AWS target: infra 200k + ops team 350k = 550k (~0.8 FTE).
  // ~ -15% overall: managed services trim infra and part of the ops load.
  // Totals are rendered as an HTML overlay (see template), not on the canvas.
  charts.push(doughnut(el1.value, [250, 400]))
  charts.push(doughnut(el2.value, [200, 350]))
})

onBeforeUnmount(() => charts.forEach(c => c.destroy()))
</script>

<template>
  <div class="flex items-stretch justify-center gap-5 text-left">

    <div class="rounded-2xl border border-gray-200 shadow-md bg-white px-6 pt-3 pb-4 flex flex-col items-center" style="border-top:3px solid #A04044">
      <div class="text-[11px] uppercase tracking-widest font-semibold mb-1" style="color:#A04044">On-prem, 2026</div>
      <div style="position:relative;width:150px;height:150px"><canvas ref="el1"></canvas><div class="absolute inset-0 flex flex-col items-center justify-center pointer-events-none"><div class="font-bold leading-none" style="font-size:20px;color:#3D3A31">$650k</div><div class="mt-0.5" style="font-size:9px;color:#9aa0a6">per year</div></div></div>
      <div class="text-[10px] opacity-50 mt-0.5 mb-2">infra + team, excludes dev</div>
      <div class="w-52 flex flex-col gap-1 text-xs">
        <div class="flex items-center justify-between"><span class="flex items-center gap-1.5"><span class="w-2.5 h-2.5 rounded-sm inline-block" style="background:#A04044"></span>Infrastructure</span><b>$250k</b></div>
        <div class="flex items-center justify-between"><span class="flex items-center gap-1.5"><span class="w-2.5 h-2.5 rounded-sm inline-block" style="background:#29445A"></span>Team, 1.0 FTE</span><b>$400k</b></div>
      </div>
    </div>

    <div class="flex flex-col items-center justify-center gap-2 shrink-0">
      <lucide-arrow-right class="w-6 h-6 opacity-30"/>
      <div class="px-3 py-1.5 rounded-full text-sm font-bold text-white shadow-sm" style="background:#2C5446">-15%</div>
    </div>

    <div class="rounded-2xl border border-gray-200 shadow-md bg-white px-6 pt-3 pb-4 flex flex-col items-center" style="border-top:3px solid #2C5446">
      <div class="text-[11px] uppercase tracking-widest font-semibold mb-1" style="color:#2C5446">AWS target</div>
      <div style="position:relative;width:150px;height:150px"><canvas ref="el2"></canvas><div class="absolute inset-0 flex flex-col items-center justify-center pointer-events-none"><div class="font-bold leading-none" style="font-size:20px;color:#3D3A31">$550k</div><div class="mt-0.5" style="font-size:9px;color:#9aa0a6">per year</div></div></div>
      <div class="text-[10px] opacity-50 mt-0.5 mb-2">managed, smaller team</div>
      <div class="w-52 flex flex-col gap-1 text-xs">
        <div class="flex items-center justify-between"><span class="flex items-center gap-1.5"><span class="w-2.5 h-2.5 rounded-sm inline-block" style="background:#A04044"></span>AWS infrastructure</span><b>$200k</b></div>
        <div class="flex items-center justify-between"><span class="flex items-center gap-1.5"><span class="w-2.5 h-2.5 rounded-sm inline-block" style="background:#29445A"></span>Ops team, 0.8 FTE</span><b>$350k</b></div>
      </div>
    </div>

  </div>
</template>
