<script setup>
import { onMounted, ref } from 'vue';
import HelloWorld from './components/HelloWorld.vue'
import TheWelcome from './components/TheWelcome.vue'

const logs = ref([]);

const socket = new WebSocket('ws://localhost:8001');
const contactServer = () => {
  socket.send("Initialize");
}

onMounted(() => {

  socket.addEventListener('open', function (event) {
    socket.send('Connection Established');
  });

  socket.addEventListener('message', function (event) {
    logs.value.push(event.data);
  });

  socket.addEventListener('close', function (event) {
    console.error('Connection closed');
  });

});
</script>

<template>
  <header>
    <img alt="Vue logo" class="logo" src="./assets/logo.svg" width="125" height="125" />

    <div class="wrapper">
      <button @click="contactServer">Send</button>
    </div>
  </header>

  <main>
    <ul v-if="logs" style="overflow: hidden;">
      <li v-for="log in logs" class="animate__animated animate__backInUp">{{ log }}</li>
    </ul>
  </main>
</template>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
