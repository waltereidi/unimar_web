<template>
   <header>
    <h1>🌱 AgroDash</h1>
    <nav>
      <button>Início</button>
      <button>Relatórios</button>
      <button>Configurações</button>
    </nav>
  </header>

  <!-- Layout principal -->
  <div class="container">
    <!-- Sidebar -->
    <aside>
      <h2>📊 Dashboards</h2>
      <ul>
        <li><button>Produção 🌾</button></li>
        <li><button>Área Plantada 🌍</button></li>
        <li><button>Rendimento 📈</button></li>
        <li><button>Previsão Climática ☀️</button></li>
      </ul>
    </aside>

    <!-- Conteúdo -->
    <main>
      <h2>Visão Geral</h2>
      <div class="chart-lavoura">
        <BarChartLavoura></BarChartLavoura>
      </div>
      <div class="big-card">
          <OpenAiMessage></OpenAiMessage>

      </div>
    </main>
  </div>
</template>


<script>
import { defineComponent } from "vue"
import BarChartLavoura from "@/components/BarChartLavoura.vue"
import OpenAiMessage from "@/components/OpenAiMessage.vue"
export default defineComponent({
  name: "PageWithChart",
  components: {
    BarChartLavoura
  }
})  
</script>
<style>
.chart-lavoura{
  max-width: 1600px;
}
  /* Reset básico */
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
      font-family: "Segoe UI", Arial, sans-serif;
    }

    body {
      min-height: 100vh;
      background: linear-gradient(135deg, #f0fdf4, #dcfce7, #f0fdf4);
      display: flex;
      flex-direction: column;
    }

    /* Header */
    header {
      background: linear-gradient(90deg, #166534, #059669);
      color: white;
      padding: 1rem 2rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }

    header h1 {
      font-size: 1.8rem;
      font-weight: bold;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    nav button {
      background: transparent;
      border: none;
      color: white;
      margin-left: 1rem;
      font-size: 1rem;
      cursor: pointer;
      padding: 0.5rem 1rem;
      border-radius: 6px;
      transition: background 0.3s;
    }

    nav button:hover {
      background: rgba(255,255,255,0.2);
    }

    /* Layout geral */
    .container {
      flex: 1;
      display: flex;
    }

    /* Sidebar */
    aside {
      width: 250px;
      background: rgba(255, 255, 255, 0.9);
      border-right: 1px solid #d1fae5;
      padding: 1.5rem;
      box-shadow: 2px 0 5px rgba(0,0,0,0.05);
    }

    aside h2 {
      font-size: 1.2rem;
      color: #166534;
      margin-bottom: 1rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    aside ul {
      list-style: none;
    }

    aside li {
      margin-bottom: 0.8rem;
    }

    aside button {
      width: 100%;
      background: #f0fdf4;
      border: 1px solid #d1fae5;
      padding: 0.8rem 1rem;
      border-radius: 8px;
      cursor: pointer;
      font-size: 1rem;
      color: #166534;
      text-align: left;
      transition: background 0.3s, transform 0.2s;
    }

    aside button:hover {
      background: #dcfce7;
      transform: translateX(5px);
    }

    /* Conteúdo principal */
    main {
      flex: 1;
      padding: 2rem;
      background: #f9fafb;
    }

    main h2 {
      font-size: 1.6rem;
      color: #065f46;
      margin-bottom: 1.5rem;
    }

    .cards {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 1.5rem;
    }

    .card {
      background: white;
      border-radius: 16px;
      box-shadow: 0 4px 10px rgba(0,0,0,0.08);
      height: 180px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      color: #9ca3af;
      font-style: italic;
      transition: transform 0.2s, box-shadow 0.2s;
    }

    .card:hover {
      transform: translateY(-5px);
      box-shadow: 0 8px 20px rgba(0,0,0,0.1);
    }

    .card span {
      font-size: 2rem;
      margin-bottom: 0.5rem;
    }

    .big-card {
      margin-top: 2rem;
      height: 280px;
      background: white;
      border-radius: 16px;
      box-shadow: 0 4px 10px rgba(0,0,0,0.08);
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      color: #9ca3af;
      font-style: italic;
      transition: transform 0.2s, box-shadow 0.2s;
    }

    .big-card:hover {
      transform: translateY(-5px);
      box-shadow: 0 8px 20px rgba(0,0,0,0.1);
    }

    .big-card span {
      font-size: 2.2rem;
      margin-bottom: 0.5rem;
    }</style>