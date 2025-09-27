<template>
  <div class="p-6">
    <h2 class="text-xl font-bold mb-4">Rendimento Ponderado por UF</h2>

    <!-- seletor de ano -->
    <div class="mb-4">
      <label for="ano" class="mr-2 font-semibold">Selecione o Ano:</label>
      <select
        id="ano"
        v-model="anoSelecionado"
        @change="buildUfChart(anoSelecionado)"
        class="border rounded p-1"
      >
        <option v-for="ano in anosDisponiveis" :key="ano" :value="ano">
          {{ ano }}
        </option>
      </select>
    </div>

    <canvas ref="ufChartRef"></canvas>
  </div>
</template>

<script setup>
import { onMounted, ref, watch } from "vue"
import { Chart } from "chart.js/auto"
import { LavouraRequests } from "@/service/lavouraRequests.js"

const props = defineProps({
  ano: {
    type: String,
    default: "2020"
  }
})

let ufChart = null
const ufChartRef = ref(null)
const filteredData = ref([])

var anosDisponiveis = ref(["2020", "2021", "2022", "2023", "2024", "2025"])
const anoSelecionado = ref(props.ano)

async function getDadosRendimentoPonderadoUf(ano) {
  const lavouraRequest = new LavouraRequests()
  return await lavouraRequest.getRendimentoPonderadoUf(ano)
}
async function getAnosDisponiveis() {
  const lavouraRequest = new LavouraRequests()
  return await lavouraRequest.getAnosDisponiveis()
}

async function buildUfChart(ano) {
  filteredData.value = await getDadosRendimentoPonderadoUf(ano)
  anosDisponiveis.value = await getAnosDisponiveis();

  const byUf = {}
  for (const r of filteredData.value) {
    const uf = r.uf || "N/A"
    if (!byUf[uf]) byUf[uf] = { soma: 0, count: 0 }
    byUf[uf].soma += Number(r.rendimento_ponderado || 0)
    byUf[uf].count += 1
  }

  const labels = Object.keys(byUf)
  const rendimentoData = labels.map(l => byUf[l].soma / byUf[l].count)

  if (!ufChartRef.value) return

  if (ufChart) ufChart.destroy()

  ufChart = new Chart(ufChartRef.value, {
    type: "bar",
    data: {
      labels,
      datasets: [
        {
          label: `Rendimento ponderado (${ano})`,
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
  buildUfChart(anoSelecionado.value)
})

watch(() => props.ano, ano => {
  anoSelecionado.value = ano
  buildUfChart(ano)
})
</script>

<style scoped>
canvas {
  width: 100% !important;
  height: 100% !important;
}
</style>
