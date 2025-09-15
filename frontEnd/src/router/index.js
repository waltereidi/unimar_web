import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue' // importe a página de login
import { useAuthStore } from '@/stores/auth'
import { AuthenticationRequests } from '@/service/authenticationRequests.js'

// Simulação de estado de autenticação
// depois você pode trocar por Pinia/Vuex ou checar token no localStorage


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/login',
      name: 'login',
      component: LoginView,
    },
    {
      path: '/',
      name: 'home',
      component: HomeView,
      meta: { requiresAuth: true }, // exige login
    },
    {
      path: '/estatisticas',
      name: 'Estatisticas',
      component: () => import('../views/EstatisticasView.vue'),
      meta: { requiresAuth: true }, // exige login
    },
    {
      path: '/:pathMatch(.*)*',
      redirect: '/login', // qualquer rota inválida manda para login
    },
  ],
})

// Guard global de autenticação
router.beforeEach((to, from, next) => {
  const authStore = useAuthStore()
  const authRequest = new AuthenticationRequests()
  
  var isValid = authRequest.validateToken(authStore.token ?? "")
  console.log("validando token")
  console.log(isValid)
  if (to.meta.requiresAuth && !authStore.token && isValid.ok ) {
    next({ name: 'login' })
  } else if(to.name === 'login') {
    next('/')

  }else{
    next()

  }

})


export default router
