<script setup>
import { onMounted, ref } from 'vue';

const logs = ref([]);

const socket = new WebSocket('ws://localhost:8001');
function contactServer() {
  socket.send("Initialize");
}

function resetLogs() {
  logs.value = [];
}

onMounted(() => {

  socket.addEventListener('open', function (event) {
    socket.send('Connection Established');
  });

  socket.addEventListener('message', function (event) {
    logs.value.push(event.data);
  });

  socket.addEventListener('close', function () {
    logs.value.push('Connection closed');
  });

});
</script>

<template>
  <div class="max-w-xl flex gap-2 mx-auto justify-center p-6 pb-0">
    <button @click="contactServer">Send</button>
    <button @click="resetLogs">Reset</button>
  </div>
  <ul v-if="logs" class="overflow-hidden flex flex-col gap-3 max-w-xl mx-auto p-6">
    <li v-for="log in logs" class="animate__animated animate__fadeIn border rounded shadow-lg p-2 block">{{ log }}</li>
  </ul>
</template>

<style scoped>
button {
  @apply py-2 px-3 bg-blue-500 text-white font-semibold rounded w-full;
}
</style>
