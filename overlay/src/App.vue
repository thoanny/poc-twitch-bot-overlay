<script setup>
import { onMounted } from 'vue';
import HelloWorld from './components/HelloWorld.vue'
import TheWelcome from './components/TheWelcome.vue'

const socket = new WebSocket('ws://localhost:8001');
const contactServer = () => {
  socket.send("Initialize");
}

onMounted(() => {


  socket.addEventListener('open', function (event) {
    socket.send('Connection Established');
  });

  socket.addEventListener('message', function (event) {
    console.log(event.data);
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
      <HelloWorld msg="You did it!" />
    </div>
  </header>

  <main>
    <TheWelcome />
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
