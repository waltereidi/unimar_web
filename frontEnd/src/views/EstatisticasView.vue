<template>
  <div class="p-6">
    <h1 class="text-2xl font-bold mb-4">📚 Estatísticas de Livros</h1>

    <!-- Total de livros -->
    <div class="mb-6 p-4 bg-gray-100 rounded-lg shadow">
      <p class="text-lg">
        Total de livros cadastrados: 
        <span class="font-semibold">{{ totalLivros }}</span>
      </p>
    </div>

    <!-- Gráfico -->
    <div class="bg-white p-4 rounded-lg shadow">
      <h2 class="text-xl font-semibold mb-2">Livros por Ano</h2>
      <BarChart :chart-data="chartData" :chart-options="chartOptions" />
    </div>
  </div>
</template>

<script>
import { defineComponent, computed } from "vue";
import { Bar } from "vue-chartjs";
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale
} from "chart.js";

// Registrando os componentes do Chart.js
ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale);

export default defineComponent({
})
</script>

<style scoped>
</style>
