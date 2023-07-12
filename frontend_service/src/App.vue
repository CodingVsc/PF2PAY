<template>
  <div id="app">
    <navbar></navbar>
    <router-view></router-view>
  </div>
</template>

<script>
import Navbar from './components/NavBar.vue';
export default {
  name: 'App',
  components: {
    Navbar
  },
  compatConfig: {
    MODE: 3
  },
}
</script>

<style>
#app {

}
</style>