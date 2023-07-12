import { createApp } from 'vue'

import App from './App.vue'
import router from './router'
import axios from 'axios'
import { createPinia } from 'pinia'

import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap';
import 'jquery';
import 'popper.js';

axios.defaults.baseURL = 'http://127.0.0.1:8000'

const app = createApp(App);


app.use(createPinia())
app.use(router, axios)

app.mount('#app')