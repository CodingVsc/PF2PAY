<template>
  <div class="registration">
    <h1>Регистрация пользователя</h1>
    <form @submit.prevent="registerUser">
      <div class="form-group">
        <label for="name">Имя:</label>
        <input type="text" id="name" v-model="name" required>
      </div>

      <div class="form-group">
        <label for="email">Email:</label>
        <input type="email" id="email" v-model="email" required>
      </div>

      <div class="form-group">
        <label for="password1">Пароль:</label>
        <input type="password" id="password1" v-model="password1" required>
      </div>

      <div class="form-group">
        <label for="password2">Подтверждение пароля:</label>
        <input type="password" id="password2" v-model="password2" required>
      </div>

      <button type="submit">Зарегистрироваться</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      name: '',
      email: '',
      password1: '',
      password2: ''
    };
  },
  methods: {
    registerUser() {
      const userData = {
        username: this.name,
        email: this.email,
        password1: this.password1,
        password2: this.password2
      };
      const axiosInstance = axios.create({
        baseURL: 'http://127.0.0.1:7000'
      });

      axiosInstance.post('api/signup/', userData)
        .then(response => {
          const message = response.data.message;
          console.log(message);
        })
        .catch(error => {
          console.error(error);
        });
    }
  }
};
</script>
<style>
.registration {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f5f5f5;
  border-radius: 4px;
}

h1 {
  text-align: center;
  margin-bottom: 20px;
}

.form-group {
  margin-bottom: 20px;
}

label {
  display: block;
  font-weight: bold;
}

input[type="text"],
input[type="email"],
input[type="password"] {
  width: 100%;
  padding: 8px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

button {
  display: block;
  width: 100%;
  padding: 10px;
  font-size: 16px;
  font-weight: bold;
  color: #fff;
  background-color: #007bff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}

button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
</style>