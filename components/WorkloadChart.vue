<script setup>
import { onMounted, onBeforeUnmount, ref } from 'vue'
import { Chart, registerables } from 'chart.js'
import annotationPlugin from 'chartjs-plugin-annotation'

Chart.register(...registerables, annotationPlugin)

const RED = '#A04044'
const BLUE = '#29445A'

const el = ref()
let chart

const data = [4, 6, 88, 6, 6, 96, 6, 6, 118, 6, 6, 92, 6, 6, 80, 6, 5, 4, 4, 5, 4]
const labels = ['', '', 'Mon', '', '', 'Tue', '', '', 'Wed', '', '', 'Thu', '', '', 'Fri', '', '', 'Sat', '', 'Sun', '']

onMounted(() => {
  chart = new Chart(el.value, {
    type: 'line',
    data: {
      labels,
      datasets: [{
        data,
        borderColor: RED,
        borderWidth: 2.5,
        fill: true,
        backgroundColor: 'rgba(160,64,68,0.12)',
        pointRadius: 0,
        tension: 0,
      }],
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      animation: false,
      layout: { padding: { top: 18, right: 10 } },
      plugins: {
        legend: { display: false },
        tooltip: { enabled: false },
        annotation: {
          annotations: {
            capacity: {
              type: 'line',
              yMin: 100, yMax: 100,
              borderColor: BLUE,
              borderWidth: 1.5,
              borderDash: [6, 4],
              label: {
                display: true,
                content: 'fixed capacity (on-prem)',
                position: 'start',
                color: BLUE,
                backgroundColor: 'transparent',
                font: { size: 11, weight: 'bold' },
                yAdjust: -8,
                padding: 0,
              },
            },
            peak: {
              type: 'label',
              xValue: 'Wed', yValue: 118,
              content: ['not enough compute'],
              color: RED,
              font: { size: 12, weight: 'bold' },
              backgroundColor: 'rgba(255,255,255,0.9)',
              padding: 3,
              yAdjust: -24,
              callout: { display: true, borderColor: RED, borderWidth: 1.4, margin: 3, side: 5 },
            },
            idle: {
              type: 'label',
              xValue: 'Sat', yValue: 5,
              content: ['idle: scale to zero'],
              color: BLUE,
              font: { size: 12, weight: 'bold' },
              backgroundColor: 'rgba(255,255,255,0.9)',
              padding: 3,
              yAdjust: -42,
              callout: { display: true, borderColor: BLUE, borderWidth: 1.4, margin: 3, side: 5 },
            },
          },
        },
      },
      scales: {
        y: {
          min: 0, max: 145,
          title: { display: true, text: 'Load', color: '#6b6b6b' },
          grid: { display: false },
          ticks: { font: { size: 10 }, color: '#9aa0a6' },
        },
        x: {
          grid: { display: false },
          ticks: { font: { size: 11 }, color: '#6b6b6b', autoSkip: false, maxRotation: 0 },
        },
      },
    },
  })
})

onBeforeUnmount(() => chart && chart.destroy())
</script>

<template>
  <div style="position: relative; width: 100%; height: 235px;">
    <canvas ref="el"></canvas>
  </div>
</template>
