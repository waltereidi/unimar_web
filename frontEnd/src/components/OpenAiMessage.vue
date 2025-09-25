<template>
  <div class="openai-message">
    <textarea v-model="userMessage" placeholder="Digite sua mensagem..." rows="3" class="input-message"></textarea>
    <button @click="sendMessage" :disabled="loading" class="btn-send">
      {{ loading ? "Enviando..." : "Enviar" }}
    </button>

    <div v-if="responseMessage" class="response-message">
      <strong>Resposta:</strong>
      <p>{{ responseMessage }}</p>
    </div>

    <div v-if="errorMessage" class="error-message">
      <strong>Erro:</strong>
      <p>{{ errorMessage }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { LavouraRequests } from "@/service/lavouraRequests.js"

const userMessage = ref("");
const responseMessage = ref("");
const errorMessage = ref("");
const loading = ref(false);

async function sendMessage() {
  if (!userMessage.value.trim()) return;

  loading.value = true;
  responseMessage.value = "";
  errorMessage.value = "";

  try {
    const lavouraRequest = new LavouraRequests()
    const res =await lavouraRequest.requestOpenAi(userMessage.value)

    // const data = await res.json();
    // A OpenAI geralmente retorna a mensagem em data.output[0].content[0].text
    responseMessage.value = res.message.toString() || "Sem resposta da API.";

  } catch (err) {
    errorMessage.value = err.message;
  } finally {
    loading.value = false;
  }
}
</script>

<style scoped>
.openai-message {
  display: flex;
  flex-direction: column;
  gap: 10px;
  padding:20px;
  overflow: auto;
}

.input-message {
  width: 100%;
  padding: 10px;
  border-radius: 6px;
  border: 1px solid #ccc;
  font-size: 14px;
  min-height: 30px;
}

.btn-send {
  padding: 8px 16px;
  background-color: #3b82f6;
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
}

.btn-send:disabled {
  background-color: #93c5fd;
  cursor: not-allowed;
}

.response-message, .error-message {
  padding: 10px;
  border-radius: 6px;
}

.response-message {
  background-color: #e0f2fe;
}

.error-message {
  background-color: #fee2e2;
}
</style>
