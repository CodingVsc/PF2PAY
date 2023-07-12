<template>
  <form class="space-y-6" v-on:submit.prevent="submitForm">
    <div class="col-xl-9 col-lg-9 col-md-12 col-sm-12 col-12">
      <div class="card h-100">
        <div class="card-body">
          <div class="row gutters">
            <div class="col-xl-6 col-lg-6 col-md-6 col-sm-6 col-12">
              <div class="form-group">
                <label for="password">Your old password</label>
                <input type="text" v-model="form.old_password" class="form-control" id="password"
                       placeholder="Enter old password">
              </div>
            </div>
            <div class="col-xl-6 col-lg-6 col-md-6 col-sm-6 col-12">
              <div class="form-group">
                <label for="password">Your new password</label>
                <input type="text" v-model="form.new_password1" class="form-control" id="password"
                       placeholder="Enter new password">
              </div>
            </div>
            <div class="col-xl-6 col-lg-6 col-md-6 col-sm-6 col-12">
              <div class="form-group">
                <label for="password">Repeat your new password</label>
                <input type="text" v-model="form.new_password2" class="form-control" id="password"
                       placeholder="Enter new password">
              </div>
            </div>
          </div>
          <div class="row gutters">
            <div class="col-xl-12 col-lg-12 col-md-12 col-sm-12 col-12">
              <div class="text-right">
                <button class="py-4 px-6 bg-purple-600 text-white rounded-lg">Save changes</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </form>
</template>

<script>
import axios from 'axios'

import {useUserStore} from '@/stores/user'

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
        old_password: '',
        new_password1: '',
        new_password2: '',
      },
      errors: [],
    }
  },

  methods: {
    submitForm() {
      this.errors = []

      if (this.form.password1 !== this.form.password2) {
        this.errors.push('The password does not match')
      }

      if (this.errors.length === 0) {
        let formData = new FormData()
        formData.append('old_password', this.form.old_password)
        formData.append('new_password1', this.form.new_password1)
        formData.append('new_password2', this.form.new_password2)

        const axiosInstance = axios.create({
          baseURL: 'http://127.0.0.1:7000'
        });

        axiosInstance
            .post('/api/editpassword/', formData, {
              headers: {
                "Content-Type": "multipart/form-data",
              }
            })
            .then(response => {
              if (response.data.message === 'success') {

                this.$router.push(`/profile/${this.userStore.user.id}`)
              } else {
                const data = JSON.parse(response.data.message)

                for (const key in data) {
                  this.errors.push(data[key][0].message)
                }
              }
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

</style>