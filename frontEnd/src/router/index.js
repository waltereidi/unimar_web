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

router.beforeEach(async (to, from, next) => {
  const authStore = useAuthStore()

  // Se a rota é "login" e não tem token → deixa entrar
  if (to.meta.name === 'login' && (!authStore.token || authStore.token === "")) {
    return next()
  }
  if (!authStore.token && to.name !== 'login') {
  console.log("Sem token → redirecionando para login")
  return next({ name: 'login' })
}

  // Se não tem token e não está indo para login → redireciona
  if (!authStore.token || authStore.token === "") {
    console.log("Sem token → redirecionando para login")
    return next({ name: 'login' })
  }

  // Se tem token, valida com o backend
  try {
    const isValid = await authRequest.validateToken(authStore.token)

    if (to.meta.requiresAuth && (isValid.error || isValid.success === false)) {
      authStore.clearToken()
      return next({ name: 'login' })
    }

    return next()
  } catch (err) {
    console.error("Erro ao validar token:", err)
    authStore.clearToken()
    return next({ name: 'login' })
  }
})


export default router
