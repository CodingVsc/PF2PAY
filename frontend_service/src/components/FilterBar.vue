<template>
  <div class="filter">
    <div class="filter-item">
      <label for="platform">Platform:</label>
      <select id="platform" v-model="params.platform">
        <option value="">All</option>
        <option value="PC">PC</option>
        <option value="PS">PS</option>
        <option value="XBOX">XBOX</option>
      </select>
    </div>
    <div class="filter-item">
      <label for="price">Price:</label>
      <div class="price-input">
        <input type="text" id="price-from" v-model="params.priceFrom" placeholder="From" />
        <span class="price-separator">-</span>
        <input type="text" id="price-to" v-model="params.priceTo" placeholder="To" />
      </div>
    </div>
    <div class="filter-item">
      <label for="is_online">Online Sellers:</label>
      <input type="checkbox" id="is_online" v-model="params.isOnline" />
    </div>
    <div class="filter-item">
      <label for="category_choice">Category:</label>
      <select id="category_choice" v-model="params.categoryChoice">
        <option value="">All</option>
        <option v-for="category in categoryOptions" :key="category" :value="category">{{ category }}</option>
      </select>
    </div>

    <div class="filter-item">
      <label for="key_choice">Key:</label>
      <select id="key_choice" v-model="params.keyChoice">
        <option value="">All</option>
        <option v-for="key in keyOptions" :key="key" :value="key">{{ key }}</option>
      </select>
    </div>

    <div class="filter-item">
      <label for="value_choice">Value:</label>
      <select id="value_choice" v-model="params.valueChoice">
        <option value="">All</option>
        <option v-for="value in valueOptions" :key="value" :value="value">{{ value }}</option>
      </select>
    </div>
    <button class="apply-button" @click="applyFilter">Apply Filter</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      params: {
        priceFrom: 0,
        priceTo: 100000,
        platform: "",
        categoryChoice: null,
        keyChoice: null,
        valueChoice: null,
      }
    };
  },
  props: {
  categoryOptions: {
    type: Array,
    default: () => []
  },
  keyOptions: {
    type: Array,
    default: () => []
  },
  valueOptions: {
    type: Array,
    default: () => []
  }
},
  methods: {
    applyFilter() {
      this.$emit('filter-applied', this.params);
    }
  }
};
</script>
<style>
.filter {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 10px;
  background-color: #f0f0f0;
}

.filter-item {
  margin-right: 10px;
}

.price-input {
  display: flex;
  align-items: center;
  height: 25px;
  width: 150px;
}

.price-separator {
  margin: 0 5px;
}

.apply-button {
  padding: 5px 10px;
  background-color: #4caf50;
  color: #fff;
  border: none;
  border-radius: 3px;
  cursor: pointer;
  width: 150px;
  height: 50px;
}

.apply-button:hover {
  background-color: #45a049;
}
</style>
