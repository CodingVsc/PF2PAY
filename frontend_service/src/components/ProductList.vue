<template>
  <div>
    <div class="product-list">
      <product-card v-for="product in products" :key="product.id" :product="product" />
    </div>
  </div>
</template>

<script>
import ProductCard from "./ProductCard.vue";

export default {
  components: {
    ProductCard
  },
  props: {
    products: {
      type: Array,
      required: true
    }
  }
};
</script>

<style>
.product-list {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 10px;
}
</style>
