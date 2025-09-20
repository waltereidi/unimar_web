<template>
  <div class="min-h-screen p-6 bg-gradient-to-b from-green-50 to-green-100 font-sans">
    <header class="flex items-center justify-between mb-6">
      <div class="flex items-center gap-4">
        <div class="w-14 h-14 rounded-lg bg-green-700 flex items-center justify-center text-white text-2xl font-bold">🌾</div>
        <div>
          <h1 class="text-2xl font-extrabold text-gray-800">Dashboard Agrícola</h1>
          <p class="text-sm text-gray-600">Visão geral por ano, estado e município — produção e rendimento</p>
        </div>
      </div>

      <div class="flex gap-3">
        <button @click="exportCSV" class="px-4 py-2 rounded-lg bg-white shadow hover:shadow-md">Exportar CSV</button>
        <select v-model="selectedAno" class="px-3 py-2 rounded-lg bg-white shadow">
          <option value="">Todos os anos</option>
          <option v-for="a in anosUnicos" :key="a" :value="a">{{ a }}</option>
        </select>
      </div>
    </header>

    <main class="grid grid-cols-1 lg:grid-cols-3 gap-6">
      <!-- KPIs -->
      <section class="lg:col-span-1 grid gap-4">
        <div class="p-4 bg-white rounded-2xl shadow">
          <h3 class="text-sm text-gray-500">Área destinada à colheita (ha)</h3>
          <p class="text-2xl font-bold">{{ formatNumber(totalAreaDestinada) }}</p>
          <small class="text-gray-400">Soma filtrada</small>
        </div>

        <div class="p-4 bg-white rounded-2xl shadow">
          <h3 class="text-sm text-gray-500">Quantidade produzida (t)</h3>
          <p class="text-2xl font-bold">{{ formatNumber(totalQuantidade) }}</p>
          <small class="text-gray-400">Soma filtrada</small>
        </div>

        <div class="p-4 bg-white rounded-2xl shadow">
          <h3 class="text-sm text-gray-500">Rendimento médio (un/ha)</h3>
          <p class="text-2xl font-bold">{{ averageRendimento }}</p>
          <small class="text-gray-400">Média ponderada</small>
        </div>
      </section>

      <!-- Charts -->
      <section class="lg:col-span-2">
        <div class="p-4 bg-white rounded-2xl shadow mb-6">
          <h2 class="text-lg font-semibold text-gray-800 mb-2">Produção por Estado (valor / quantidade)</h2>
          <canvas id="ufChart"></canvas>
        </div>

        <div class="p-4 bg-white rounded-2xl shadow">
          <h2 class="text-lg font-semibold text-gray-800 mb-2">Tabela de dados (filtrável)</h2>
          <div class="overflow-x-auto">
            <table class="w-full text-sm">
              <thead class="text-left text-gray-500 border-b">
                <tr>
                  <th class="py-2">Ano</th>
                  <th>UF</th>
                  <th>Município</th>
                  <th>Produto</th>
                  <th class="text-right">Área destinada</th>
                  <th class="text-right">Área colhida</th>
                  <th class="text-right">Quantidade</th>
                  <th class="text-right">Rendimento</th>
                  <th class="text-right">Valor</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(r, idx) in filteredData" :key="idx" class="border-b hover:bg-gray-50">
                  <td class="py-2">{{ r.ano }}</td>
                  <td>{{ r.sigla_uf }}</td>
                  <td>{{ r.id_municipio }}</td>
                  <td>{{ r.produto }}</td>
                  <td class="text-right">{{ formatNumber(r.area_destinada_colheita) }}</td>
                  <td class="text-right">{{ formatNumber(r.area_colhida) }}</td>
                  <td class="text-right">{{ formatNumber(r.quantidade_produzida) }}</td>
                  <td class="text-right">{{ formatNumber(r.rendimento_medio_producao) }}</td>
                  <td class="text-right">{{ formatCurrency(r.valor_producao) }}</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </section>
    </main>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue'
import Chart from 'chart.js/auto'

// === Dados de exemplo (substitua pelos seus dados reais) ===
const rawData = ref([
  { ano: '2022', sigla_uf: 'SP', id_municipio: '3550308', produto: 'Soja', area_destinada_colheita: 1200, area_colhida: 1180, quantidade_produzida: 3000, rendimento_medio_producao: 2.54, valor_producao: 1500000 },
  { ano: '2022', sigla_uf: 'MG', id_municipio: '3106200', produto: 'Milho', area_destinada_colheita: 800, area_colhida: 780, quantidade_produzida: 2800, rendimento_medio_producao: 3.59, valor_producao: 980000 },
  { ano: '2023', sigla_uf: 'SP', id_municipio: '3550308', produto: 'Soja', area_destinada_colheita: 1350, area_colhida: 1330, quantidade_produzida: 3500, rendimento_medio_producao: 2.63, valor_producao: 1750000 },
  { ano: '2023', sigla_uf: 'PR', id_municipio: '4106902', produto: 'Trigo', area_destinada_colheita: 600, area_colhida: 590, quantidade_produzida: 900, rendimento_medio_producao: 1.52, valor_producao: 420000 },
])

const selectedAno = ref('')

const anosUnicos = computed(() => {
  const s = new Set(rawData.value.map(d => d.ano))
  return Array.from(s).sort()
})

const filteredData = computed(() => {
  if (!selectedAno.value) return rawData.value
  return rawData.value.filter(d => d.ano === selectedAno.value)
})

// === KPIs ===
const totalAreaDestinada = computed(() => filteredData.value.reduce((s, r) => s + Number(r.area_destinada_colheita || 0), 0))
const totalQuantidade = computed(() => filteredData.value.reduce((s, r) => s + Number(r.quantidade_produzida || 0), 0))

// Média ponderada de rendimento (por área colhida)
const averageRendimento = computed(() => {
  const numer = filteredData.value.reduce((s, r) => s + (Number(r.rendimento_medio_producao || 0) * Number(r.area_colhida || 0)), 0)
  const denom = filteredData.value.reduce((s, r) => s + Number(r.area_colhida || 0), 0)
  return denom ? (numer / denom).toFixed(2) : '0.00'
})

// === Gráfico por UF ===
let ufChart = null

const buildUfChart = () => {
  const byUf = {}
  for (const r of filteredData.value) {
    const uf = r.sigla_uf || 'N/A'
    if (!byUf[uf]) byUf[uf] = { quantidade: 0, valor: 0 }
    byUf[uf].quantidade += Number(r.quantidade_produzida || 0)
    byUf[uf].valor += Number(r.valor_producao || 0)
  }
  const labels = Object.keys(byUf)
  const quantidadeData = labels.map(l => byUf[l].quantidade)
  const valorData = labels.map(l => Math.round(byUf[l].valor))

  const ctx = document.getElementById('ufChart')
  if (!ctx) return

  if (ufChart) ufChart.destroy()

  ufChart = new Chart(ctx, {
    type: 'bar',
    data: {
      labels,
      datasets: [
        { label: 'Quantidade produzida', data: quantidadeData, yAxisID: 'y1' },
        { label: 'Valor produção (R$)', data: valorData, yAxisID: 'y2' }
      ]
    },
    options: {
      responsive: true,
      interaction: { mode: 'index', intersect: false },
      scales: {
        y1: { type: 'linear', position: 'left', title: { display: true, text: 'Quantidade' } },
        y2: { type: 'linear', position: 'right', title: { display: true, text: 'Valor (R$)' }, grid: { drawOnChartArea: false } }
      }
    }
  })
}

onMounted(() => buildUfChart())
watch([filteredData], () => buildUfChart())

// === Utilitários ===
const formatNumber = (n) => {
  if (n === null || n === undefined) return '-' 
  return Number(n).toLocaleString()
}
const formatCurrency = (n) => {
  if (n === null || n === undefined) return '-' 
  return Number(n).toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' })
}

function exportCSV() {
  const rows = filteredData.value
  if (!rows.length) return
  const header = Object.keys(rows[0])
  const csv = [header.join(',')].concat(rows.map(r => header.map(h => String(r[h] ?? '')).join(','))).join('\n')
  const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' })
  const url = URL.createObjectURL(blob)
  const a = document.createElement('a')
  a.href = url
  a.download = `dados_agricolas_${selectedAno.value || 'todos'}.csv`
  a.click()
  URL.revokeObjectURL(url)
}
</script>

<style scoped>
/* Pequenas melhorias visuais */
table th, table td { padding: 0.5rem }
</style>
