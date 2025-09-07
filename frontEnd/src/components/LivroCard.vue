<template>
  <div class="p-4 rounded-2xl shadow-md bg-white hover:shadow-lg transition cursor-pointer">
    <img 
      :src="livro.capa" 
      :alt="livro.titulo" 
      class="w-full h-48 object-cover rounded-xl mb-3"
    />
    <h2 class="text-lg font-bold text-gray-800">{{ livro.titulo }}</h2>
    <p class="text-sm text-gray-600">✍ Autor: {{ livro.autor }}</p>
    <p class="text-sm text-gray-500">📅 Ano: {{ livro.ano }}</p>
  </div>
</template>

<script setup>
defineProps({
  livro: {
    type: Object,
    required: true
  }
})
</script>
