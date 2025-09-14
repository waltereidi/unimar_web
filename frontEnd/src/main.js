import './assets/main.css'
import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

const app = createApp(App)
const pinia = createPinia()  // ⚡ criar instância única

app.use(pinia)   // usar a instância
app.use(router)

app.mount('#app')
