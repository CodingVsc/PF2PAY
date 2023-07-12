<template>
  <br>
  <div class="product-card line">
    <div class="col">{{ product.platform }}</div>
    <div class="col">{{ product.short_description }}</div>
    <div class="col">
      <a :href="getUserProfileLink(product.user_id)" class="profile-link">
        <div class="avatar-container">
          <img :src="user.get_avatar" alt="Avatar" class="avatar">
        </div>
      </a>
    </div>
    <div class="col">{{ product.price }}</div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  props: {
    product: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      user: []
    };
  },
  mounted() {
    this.getUserProfileAvatar();
  },
  methods: {
    getUserProfileLink(userId) {
      return `/user_profile/${userId}`;
    },
    getUserProfileAvatar() {
      const userId = this.product.user_id;
      const axiosInstance = axios.create({
        baseURL: 'http://127.0.0.1:7000'
      });
      axiosInstance.get(`api/user_detail/${userId}`)
        .then((response) => {
          this.user = response.data;
        })
        .catch((error) => {
          console.error("Error fetching user:", error);
        });
    }
  }
};
</script>

<style>
.product-card {
  display: flex;
  flex-direction: row;
}

.line {
    border-bottom: 1px solid #6200ff; /* Параметры линии */
   }
.col {
  flex: 1;
}

.avatar-container {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  overflow: hidden;
  margin-right: 10px;
}

.avatar {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.profile-link {
  color: blue;
  text-decoration: underline;
}
</style>
