<template>
  <div class="p-6">
    <h1 class="text-2xl font-bold mb-6">📚 Meus Livros</h1>

    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <LivroCard 
        v-for="(livro, index) in livros" 
        :key="index" 
        :livro="livro" 
      />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue"
import LivroCard from "@/components/LivroCard.vue"

const livros = ref([
  { titulo: "Dom Casmurro", autor: "Machado de Assis", ano: 1899 },
  { titulo: "O Senhor dos Anéis", autor: "J.R.R. Tolkien", ano: 1954 },
  { titulo: "1984", autor: "George Orwell", ano: 1949 },
  { titulo: "O Pequeno Príncipe", autor: "Antoine de Saint-Exupéry", ano: 1943 }
])

onMounted(async () => {
  try {
    const res = await fetch("http://localhost:5000/api/products", {
      method: "GET",
      headers: {
        "Content-Type": "application/json"
      }
    })

    if (!res.ok) {
      throw new Error(`Erro HTTP: ${res.status}`)
    }

    const data = await res.json()

    // Atualiza a lista de livros com os dados do backend
    console.log(data);

    console.log("Livros carregados do backend:", data)
  } catch (err) {
    console.error("Erro ao buscar livros:", err)
  }
})
</script>


<style scoped>
/* Apenas um exemplo de estilização adicional */
</style>
