<template>
  <div class="p-6">
    <h2 class="text-xl font-bold mb-4">Rendimento Ponderado por UF</h2>
    <canvas id="ufChart"></canvas>
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue"
import { Chart } from "chart.js/auto"
import { LavouraRequests } from "@/service/lavouraRequests.js"
let ufChart = null



const filteredData = ref()

async function getDadosRendimentoPonderadoUf(){
  var lavouraRequest = new LavouraRequests(); 
  var res = await lavouraRequest.getRendimentoPonderadoUf('2020');  

  return res;
}
const buildUfChart = async () => {
  const byUf = {}

  var lavouraRequest = new LavouraRequests(); 
  filteredData.value = await lavouraRequest.getRendimentoPonderadoUf('2020');  
  

  for (const r of filteredData.value) {
    const uf = r.uf || "N/A"
    if (!byUf[uf]) byUf[uf] = { soma: 0, count: 0 }
    byUf[uf].soma += Number(r.rendimento_ponderado || 0)
    byUf[uf].count += 1
  }

  const labels = Object.keys(byUf)
  const rendimentoData = labels.map(l => byUf[l].soma / byUf[l].count)

  const ctx = document.getElementById("ufChart")
  if (!ctx) return

  if (ufChart) ufChart.destroy()

  ufChart = new Chart(ctx, {
    type: "bar",
    data: {
      labels,
      datasets: [
        {
          label: "Rendimento ponderado (média)",
          data: rendimentoData,
          backgroundColor: "rgba(54, 162, 235, 0.6)",
          borderColor: "rgba(54, 162, 235, 1)",
          borderWidth: 1
        }
      ]
    },
    options: {
      responsive: true,
      interaction: { mode: "index", intersect: false },
      scales: {
        y: {
          beginAtZero: true,
          title: { display: true, text: "Rendimento ponderado" }
        }
      }
    }
  })
}

onMounted(() => {
  buildUfChart()
})
</script>

<style scoped>
/* Apenas para visual */
#ufChart {
  max-width: 1200px; /* antes era 800px */
  height: 600px;     /* adiciona altura maior */
  margin: auto;
}
</style>
