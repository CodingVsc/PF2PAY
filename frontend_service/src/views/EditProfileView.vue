<template>
<div class="container">
<div class="row gutters">
<div class="col-xl-3 col-lg-3 col-md-12 col-sm-12 col-12">
<div class="card h-100">
	<div class="card-body">
		<div class="account-settings">
			<div class="user-profile">
				<div class="user-avatar">
					<img :src="userStore.user.avatar" alt="Maxwell Admin">
          <label>Upload Avatar</label><br>
            <input type="file" ref="file">
				</div>
				<h5 class="user-name">{{ userStore.user.username}}</h5>
				<h6 class="user-email">{{ userStore.user.email}}</h6>
			</div>
			<div class="about">
				<h5>About</h5>
				<p>...</p>
			</div>
		</div>
	</div>
</div>
</div>
  <form class="space-y-6" v-on:submit.prevent="submitForm">
<div class="col-xl-9 col-lg-9 col-md-12 col-sm-12 col-12">
<div class="card h-100">
	<div class="card-body">
		<div class="row gutters">
			<div class="col-xl-12 col-lg-12 col-md-12 col-sm-12 col-12">
				<h6 class="mb-2 text-primary">Personal Details</h6>
			</div>
			<div class="col-xl-6 col-lg-6 col-md-6 col-sm-6 col-12">
				<div class="form-group">
					<label for="fullName">Full Name</label>
					<input type="text" v-model="form.name" class="form-control" id="fullName" placeholder="Enter full name">
				</div>
			</div>
			<div class="col-xl-6 col-lg-6 col-md-6 col-sm-6 col-12">
				<div class="form-group">
					<label for="eMail">Email</label>
					<input type="email" v-model="form.email" class="form-control" id="eMail" placeholder="Enter email ID">
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
</div>
</div>
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
        email: this.userStore.user.email,
        name: this.userStore.user.username
      },
      errors: [],
    }
  },

  methods: {
    submitForm() {
      this.errors = []

      if (this.form.email === '') {
        this.errors.push('Your e-mail is missing')
      }

      if (this.form.name === '') {
        this.errors.push('Your name is missing')
      }

      if (this.errors.length === 0) {
        let formData = new FormData()
        formData.append('avatar', this.$refs.file.files[0])
        formData.append('name', this.form.name)
        formData.append('email', this.form.email)

        const axiosInstance = axios.create({
          baseURL: 'http://127.0.0.1:7000'
        });

        axiosInstance
            .post('/api/editprofile/', formData, {
              headers: {
                "Content-Type": "multipart/form-data",
              }
            })
            .then(response => {
              if (response.data.message === 'information updated') {

                this.userStore.setUserInfo({
                  id: this.userStore.user.id,
                  username: this.form.name,
                  email: this.form.email,
                  avatar: response.data.user.avatar
                })

                this.$router.push(`/profile/${this.userStore.user.id}`)
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