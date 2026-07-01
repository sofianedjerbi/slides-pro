<script setup>
import { onMounted, onBeforeUnmount, ref } from 'vue'
import { Chart, registerables } from 'chart.js'

Chart.register(...registerables)

const RED = '#A04044'
const BLUE = '#29445A'
const GRAY = '#b8bfc7'

const el1 = ref()
const el2 = ref()
const charts = []

function centerText(total) {
  return {
    id: 'center-' + total,
    afterDraw(chart) {
      const { ctx, chartArea: { left, right, top, bottom } } = chart
      const x = (left + right) / 2
      const y = (top + bottom) / 2
      ctx.save()
      ctx.textAlign = 'center'
      ctx.textBaseline = 'middle'
      ctx.fillStyle = '#3D3A31'
      ctx.font = 'bold 20px Inter, ui-sans-serif'
      ctx.fillText(total, x, y - 5)
      ctx.fillStyle = '#9aa0a6'
      ctx.font = '9px Inter, ui-sans-serif'
      ctx.fillText('per year', x, y + 12)
      ctx.restore()
    },
  }
}

function doughnut(canvas, data, total) {
  return new Chart(canvas, {
    type: 'doughnut',
    data: {
      labels: ['Compute', 'Database', 'Storage + network'],
      datasets: [{ data, backgroundColor: [RED, BLUE, GRAY], borderColor: '#ffffff', borderWidth: 2 }],
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      animation: false,
      cutout: '64%',
      plugins: { legend: { display: false }, tooltip: { enabled: false } },
    },
    plugins: [centerText(total)],
  })
}

onMounted(() => {
  // values from cost_estimate.py (Zurich list prices)
  charts.push(doughnut(el1.value, [27471, 341640, 30000], '$399k'))
  charts.push(doughnut(el2.value, [21192, 74359, 30000], '$126k'))
})

onBeforeUnmount(() => charts.forEach(c => c.destroy()))
</script>

<template>
  <div class="flex items-stretch justify-center gap-5 text-left">

    <div class="rounded-2xl border border-gray-200 shadow-md bg-white px-6 pt-3 pb-4 flex flex-col items-center" style="border-top:3px solid #A04044">
      <div class="text-[11px] uppercase tracking-widest font-semibold mb-1" style="color:#A04044">Upper bound</div>
      <div style="position:relative;width:132px;height:132px"><canvas ref="el1"></canvas></div>
      <div class="text-[10px] opacity-50 mt-0.5 mb-2">Atlas M50, 24/7</div>
      <div class="w-48 flex flex-col gap-1 text-xs">
        <div class="flex items-center justify-between"><span class="flex items-center gap-1.5"><span class="w-2.5 h-2.5 rounded-sm inline-block" style="background:#A04044"></span>Compute</span><b>$27k</b></div>
        <div class="flex items-center justify-between"><span class="flex items-center gap-1.5"><span class="w-2.5 h-2.5 rounded-sm inline-block" style="background:#29445A"></span>Database</span><b>$342k</b></div>
        <div class="flex items-center justify-between"><span class="flex items-center gap-1.5"><span class="w-2.5 h-2.5 rounded-sm inline-block" style="background:#b8bfc7"></span>Storage + network</span><b>$30k</b></div>
      </div>
    </div>

    <div class="flex flex-col items-center justify-center gap-2 shrink-0">
      <lucide-arrow-right class="w-6 h-6 opacity-30"/>
      <div class="px-3 py-1.5 rounded-full text-sm font-bold text-white shadow-sm" style="background:#2C5446">-69%</div>
    </div>

    <div class="rounded-2xl border border-gray-200 shadow-md bg-white px-6 pt-3 pb-4 flex flex-col items-center" style="border-top:3px solid #29445A">
      <div class="text-[11px] uppercase tracking-widest font-semibold mb-1" style="color:#29445A">Optimized</div>
      <div style="position:relative;width:132px;height:132px"><canvas ref="el2"></canvas></div>
      <div class="text-[10px] opacity-50 mt-0.5 mb-2">DocumentDB, non-prod off weekends</div>
      <div class="w-48 flex flex-col gap-1 text-xs">
        <div class="flex items-center justify-between"><span class="flex items-center gap-1.5"><span class="w-2.5 h-2.5 rounded-sm inline-block" style="background:#A04044"></span>Compute</span><b>$21k</b></div>
        <div class="flex items-center justify-between"><span class="flex items-center gap-1.5"><span class="w-2.5 h-2.5 rounded-sm inline-block" style="background:#29445A"></span>Database</span><b>$74k</b></div>
        <div class="flex items-center justify-between"><span class="flex items-center gap-1.5"><span class="w-2.5 h-2.5 rounded-sm inline-block" style="background:#b8bfc7"></span>Storage + network</span><b>$30k</b></div>
      </div>
    </div>

  </div>
</template>
