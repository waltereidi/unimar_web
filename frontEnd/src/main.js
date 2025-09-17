import './assets/main.css'
import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import Toast from "vue-toastification";
import "vue-toastification/dist/index.css";
const app = createApp(App)
const pinia = createPinia()  // ⚡ criar instância única

app.use(pinia)   // usar a instância
app.use(router)

const options = {
    // You can set your default options here
};

app.use(Toast, options);


app.mount('#app')
