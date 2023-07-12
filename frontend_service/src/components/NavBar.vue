<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <router-link to="/home" class="navbar-brand">Home</router-link>
    <button class="navbar-toggler" type="button" @click="toggleDropdown">
      <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" :class="{ 'show': isDropdownOpen }">
      <ul class="navbar-nav ml-auto">
        <li class="nav-item">
          <router-link to="/about" class="nav-link">About</router-link>
        </li>
        <li v-if="userStore.user.isAuthenticated && userStore.user.id" class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" @click="toggleDropdown" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Dropdown link</a>
          <ul class="dropdown-menu" v-show="isDropdownOpen">
            <li>
              <router-link :to="`/profile/${userStore.user.id}`" class="dropdown-item">Profile</router-link>
            </li>
            <li>
              <router-link to="/create_product" class="dropdown-item">Create an offer</router-link>
            </li>
            <li>
              <router-link to="/logout" class="dropdown-item">Log Out</router-link>
            </li>
          </ul>
        </li>
        <li v-else class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" @click="toggleDropdown" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Dropdown link</a>
          <ul class="dropdown-menu" v-show="isDropdownOpen">
            <li>
              <router-link to="/login" class="dropdown-item">Log In</router-link>
            </li>
            <li>
              <router-link to="/signup" class="dropdown-item">Sign Up</router-link>
            </li>
          </ul>
        </li>
      </ul>
    </div>
  </nav>
</template>




<style>

</style>

<script>
    import axios from 'axios'
    import { useUserStore } from '@/stores/user'

    export default {
        setup() {
            const userStore = useUserStore()

            return {
                userStore
            }
        },
        beforeCreate() {
            this.userStore.initStore()

            const token = this.userStore.user.access

            if (token) {
                axios.defaults.headers.common["Authorization"] = "Bearer " + token;
            } else {
                axios.defaults.headers.common["Authorization"] = "";
            }
        },
    data() {
    return {
      isDropdownOpen: false
    };
  },
  methods: {
    toggleDropdown() {
      this.isDropdownOpen = !this.isDropdownOpen;
    }
  }
    }
</script>