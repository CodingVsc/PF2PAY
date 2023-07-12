<template>
  <div>
    <h1>Список Предложений</h1>
    <div><ex-filter-bar @filter-applied="handleFilterApplied"/></div><br>
    <div v-if="products.length">
      <div class="row product-header">
        <div class="col">Платформа</div>
        <div class="col">Описание</div>
        <div class="col">Продавец</div>
        <div class="col">Цена</div>
      </div>
      <div class="product-list">
        <product-card
          v-for="product in products"
          :key="product.id"
          :product="product"
          @click="goToProductDetail(product.id)"
        />
      </div>
    </div>
    <div v-else>
      <p>Нет доступных продуктов.</p>
    </div>
  </div>
</template>

<script>
import ProductCard from "../components/ProductCard.vue";
import axios from "axios";
import FilterBar from "@/components/FilterBar.vue";
import ExFilterBar from "@/components/ExFilterBar.vue";

export default {
  components: {
    ProductCard,
    FilterBar,
    ExFilterBar
  },
  data() {
    return {
      products: [],
      avatar: [],
      filterParams: {
        priceFrom: 0,
        priceTo: 100000,
        platform: "",
        categoryChoice: "",
        keyChoice: "",
        valueChoice: "",
      }
    };
  },
  mounted() {
    this.fetchProducts();
  },
  methods: {
    fetchProducts() {
      const gameId = this.$route.params.gameId;
      axios
        .get(`/api/v1/game/${gameId}/`, { params: this.filterParams })
        .then(response => {
          this.products = response.data;
        });
    },
    goToProductDetail(productId) {
      this.$router.push(`/product_detail/${productId}`);
    },
    handleFilterApplied(params) {
      this.filterParams = params;
      this.fetchProducts();
    }
  },
  watch: {
    "$route.params.gameId"() {
      this.fetchProducts();
    }
  }
};
</script>

<style>

.product-list {
  display: flex;
  flex-direction: column;
}

.product-card {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
}

.col {
  flex: 1;
}
</style>