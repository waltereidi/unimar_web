import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    vueDevTools(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    },
  },
  server: {
    host: true, // permite acesso externo (ex: EC2, domínio)
  },
  preview: {
    allowedHosts: [
      'www.livrosexpo.site', // domínio liberado
      'livrosexpo.site', // domínio liberado
    ],
    port: 4173, // pode mudar se quiser
  },
})
