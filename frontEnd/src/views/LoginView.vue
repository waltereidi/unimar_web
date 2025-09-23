<template>
  <div class="login-page">
    <form class="login-card" @submit.prevent="onSubmit" novalidate>
      <h1 class="title">Entrar</h1>

      <label class="field">
        <span class="label">E‑mail</span>
        <input
          v-model="form.email"
          type="email"
          inputmode="email"
          autocomplete="email"
          required
          :class="{ invalid: errors.email }
          "
          placeholder="seu@email.com"
        />
        <small v-if="errors.email" class="error">{{ errors.email }}</small>
      </label>

      <label class="field">
        <span class="label">Senha</span>
        <div class="password-row">
          <input
            v-model="form.password"
            :type="showPassword ? 'text' : 'password'"
            autocomplete="current-password"
            required
            minlength="6"
            :class="{ invalid: errors.password }"
            placeholder="••••••••"
          />
          <button type="button" class="toggle" @click="showPassword = !showPassword">
            {{ showPassword ? 'ocultar' : 'mostrar' }}
          </button>
        </div>
        <small v-if="errors.password" class="error">{{ errors.password }}</small>
      </label>

      <button class="submit-btn" :disabled="loading">
        <span v-if="!loading">Entrar</span>
        <span v-else>Entrando...</span>
      </button>

      <p v-if="serverError" class="server-error">{{ serverError }}</p>

      <p class="links">
        <!-- <a href="#" @click.prevent="$emit('forgot')">Esqueceu a senha?</a>
        <a href="#" @click.prevent="$emit('register')">Criar conta</a> -->
      </p>
    </form>
  </div>
</template>

<script setup>
import { reactive, ref } from 'vue'
import { useAuthStore } from '@/stores/auth'
import { AuthenticationRequests }  from '@/service/authenticationRequests'
import { useToast } from "vue-toastification";
import router  from "@/router/index";

const authStore = useAuthStore()


const emit = defineEmits(['success', 'forgot', 'register'])

const form = reactive({
  email: '',
  password: '',
  remember: false,
})

const errors = reactive({
  email: '',
  password: '',
})

const serverError = ref('')
const loading = ref(false)
const showPassword = ref(false)

function validate() {
  errors.email = ''
  errors.password = ''
  serverError.value = ''

  // email basic
  if (!form.email) errors.email = 'E‑mail é obrigatório.'
  else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(form.email)) errors.email = 'E‑mail inválido.'

  // password basic
  if (!form.password) errors.password = 'Senha é obrigatória.'
  else if (form.password.length < 6) errors.password = 'A senha deve ter ao menos 6 caracteres.'

  return !errors.email && !errors.password
}

async function onSubmit() {
  if (!validate()) return
  const toast = useToast();

  loading.value = true
  serverError.value = ''

  try {
    
    var authRequests  = new AuthenticationRequests()
    var res = await authRequests.loginAuthentication(form.email, form.password) 
    if(!res.ok)
      throw 'Usuário ou senha inválidos';
    
    toast.success("Login efetuado com sucesso")
    emit('success')
    router.push({ name: 'home' })
    // você pode redirecionar aqui, armazenar token em localStorage, etc.
    
  } catch (err) {
    serverError.value = 'Usuário ou senha inválidos';
    toast.error(serverError.value);

  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.login-page {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 32px;
  box-sizing: border-box;
}

.login-card {
  width: 100%;
  max-width: 420px;
  background: #fff;
  border-radius: 12px;
  padding: 28px;
  box-shadow: 0 8px 30px rgba(20, 30, 60, 0.08);
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.title {
  margin: 0 0 6px 0;
  font-size: 1.5rem;
  font-weight: 600;
}

.field {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.label {
  font-size: 0.85rem;
  color: #444;
}

input[type="email"],
input[type="password"],
input[type="text"] {
  padding: 10px 12px;
  border-radius: 8px;
  border: 1px solid #d7dbe0;
  font-size: 0.95rem;
  outline: none;
}

input.invalid { border-color: #e06b6b; }

.password-row {
  display: flex;
  gap: 8px;
  align-items: center;
}

.password-row .toggle {
  padding: 8px 10px;
  border-radius: 8px;
  background: transparent;
  border: 1px solid #d7dbe0;
  cursor: pointer;
}

.remember {
  display: flex;
  gap: 8px;
  align-items: center;
  font-size: 0.9rem;
}

.submit-btn {
  margin-top: 6px;
  padding: 10px 12px;
  border-radius: 10px;
  border: none;
  font-weight: 600;
  cursor: pointer;
  background: linear-gradient(90deg,#4f46e5,#06b6d4);
  color: white;
}

.submit-btn[disabled] { opacity: 0.7; cursor: not-allowed; }

.error { color: #c0392b; font-size: 0.85rem; }
.server-error { color: #922; font-weight: 600; margin-top: 6px; }

.links {
  display:flex;
  justify-content: space-between;
  margin-top: 10px;
  font-size: 0.9rem;
}

.links a { color: #2563eb; text-decoration: none; }

@media (max-width: 480px) {
  .login-card { padding: 20px; }
}
</style>
