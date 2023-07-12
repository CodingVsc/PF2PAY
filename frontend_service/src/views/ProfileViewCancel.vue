<template>
  <div class="profile">
    <div class="profile-header">
      <div class="avatar-wrapper">
        <img :src="user.avatar" alt="Avatar" class="avatar">
      </div>
      <div class="profile-info">
        <h2 class="username">{{ user.username }}</h2>
      </div>
    </div>
    <div class="profile-details">
      <div class="details-section">
        <h3 class="section-title">О себе</h3>
        <p class="section-content">{{ user.about }}</p>
      </div>
      <div class="details-section">
        <h3 class="section-title">Предложения</h3>
        <ul class="offer-list">
          <div class="offer-item">
        <product-card
          v-for="product in products"
          :key="product.id"
          :product="product"
          @click="goToProductDetail(product.id)"
        />
      </div>
        </ul>
      </div>
    </div>
  </div>
</template>
<script>
import { useUserStore } from "@/stores/user";
import axios from "axios";
import ProductCard from "@/components/ProductCard.vue";

export default {
  setup() {
    const userStore = useUserStore();

    return {
      userStore,
    };
  },
  components: {
    ProductCard,
  },
  data() {
    return {
      user: {
        username: this.userStore.user.username,
        avatar: this.userStore.user.avatar,
      },
      products: [],
    };
  },
  mounted() {
    this.fetchOffers();
  },
  methods: {
    fetchOffers() {
      const userId = this.userStore.user.id;
      axios
        .get(`api/v1/all_product/${userId}`)
        .then((response) => {
          this.products = response.data;
        })
        .catch((error) => {
          console.error("Error fetching offers:", error);
        });
    },
    goToProductDetail(productId) {
      this.$router.push(`/product_detail/${productId}`);
    },
  },
  watch: {
    "$route.params.gameId"() {
      this.fetchOffers();
    },
  },
};
</script>

<style>
.profile {
  background-color: #fff;
  padding: 20px;
  border-radius: 4px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.profile-header {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
}

.avatar-wrapper {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  overflow: hidden;
}

.avatar {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.profile-info {
  margin-left: 20px;
}

.username {
  font-size: 24px;
  font-weight: bold;
  color: #333;
}

.user-rating {
  font-size: 16px;
  color: #888;
  margin-top: 5px;
}

.profile-details {
  display: grid;
  grid-gap: 20px;
}

.details-section {
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 4px;
}

.section-title {
  font-size: 18px;
  font-weight: bold;
  color: #333;
  margin-bottom: 10px;
}

.section-content {
  font-size: 14px;
  color: #555;
}

.offer-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  grid-gap: 20px;
  list-style: none;
  padding: 0;
  margin: 0;
}

.offer-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.offer-image {
  width: 100%;
  max-height: 200px;
  object-fit: cover;
  margin-bottom: 10px;
}

.offer-title {
  font-size: 16px;
  font-weight: bold;
  color: #333;
  text-align: center;
  margin-bottom: 5px;
}

.offer-price {
  font-size: 14px;
  color: #888;
}

</style>