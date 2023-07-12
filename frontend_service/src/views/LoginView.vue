<template>
  <div class="login-page">
    <div class="login-container">
      <h2>Вход в систему</h2>
      <form v-on:submit.prevent="submitForm">
        <div class="form-group">
          <label for="name">Name:</label><br>
          <input type="text" id="name" v-model="form.name" required>
        </div>
        <div class="form-group">
          <label for="password">Пароль:</label><br>
          <input type="password" id="password" v-model="form.password" required>
        </div>
        <button type="submit">Войти</button>
      </form>
    </div>
  </div>
</template>

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

  data() {
    return {
      form: {
        name: '',
        password: '',
      },
      errors: []
    }
  },

  methods: {
    async submitForm() {
      this.errors = []

      if (this.form.name === '') {
        this.errors.push('Your name is missing')
      }

      if (this.form.password === '') {
        this.errors.push('Your password is missing')
      }

      const axiosInstance = axios.create({
        baseURL: 'http://127.0.0.1:7000'
      })

      if (this.errors.length === 0) {
        await axiosInstance
          .post('/api/login/', {
            username: this.form.name,
            password: this.form.password
          })
          .then(response => {
            this.userStore.setToken(response.data)
            axios.defaults.headers.common["Authorization"] = "Bearer " + response.data.access
          })
          .catch(error => {
            console.log('error', error)
            this.errors.push('The name or password is incorrect! Or the user is not activated!')
          })
      }

      if (this.errors.length === 0) {
        await axiosInstance
          .get('/api/me/')
          .then(response => {
            this.userStore.setUserInfo(response.data)
            this.$router.push('/home')
          })
          .catch(error => {
            console.log('error', error)
          })
      }
    }
  }
}
</script>

<style scoped>
.login-page {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.login-container {
  width: 300px;
  padding: 20px;
  background-color: #f0f0f0;
  border-radius: 5px;
}

h2 {
  text-align: center;
}

.form-group {
  margin-bottom: 10px;
}

label {
  display: block;
  font-weight: bold;
}

input[type="text"],
input[type="password"] {
  width: 100%;
  padding: 5px;
  border: 1px solid #ccc;
  border-radius: 3px;
}

button[type="submit"] {
  width: 100%;
  padding: 8px;
  background-color: #333;
  color: #fff;
  border: none;
  border-radius: 3px;
  cursor: pointer;
}
</style>
