<template>
  <div class="container">
    <h1>Create Offer</h1>
    <form @submit.prevent="createListing">
      <div class="form-group">
        <label for="shortDescription">Short Description</label>
        <input v-model="shortDescription" type="text" id="shortDescription" required>
      </div>
      <div class="form-group">
        <label for="description">Description</label>
        <textarea v-model="description" id="description" rows="4" required></textarea>
      </div>
      <div class="form-group">
        <label for="price">Price</label>
        <input v-model.number="price" type="number" id="price" required>
      </div>
      <div class="form-group">
        <label for="gameSelect">Game</label>
        <select v-model.number="selectedGameId" id="gameSelect" required @change="updateSelectedGameId">
          <option v-for="game in games" :key="game.id" :value="game.id">{{ game.game_name }}</option>
        </select>
      </div>
      <div v-if="selectedGameId && selectedGameParams">
        <div class="form-group">
          <label>Choose Category:</label>
          <select v-model="selectedCategory" @change="updateSelectedCategory">
            <option value="">Select Category</option>
            <option v-for="(category, categoryName) in selectedGameParams" :key="categoryName">{{ categoryName }}</option>
          </select>
        </div>
        <div v-if="selectedCategory">
          <div class="form-group">
            <label>Choose Key:</label>
            <select v-model="selectedKey" @change="updateSelectedKey">
              <option value="">Select Key</option>
              <option v-for="(value, key) in selectedGameParams[selectedCategory]" :key="key">{{ key }}</option>
            </select>
          </div>
          <div v-if="selectedKey">
            <div class="form-group">
              <label>Choose Value:</label>
              <select v-model="selectedValue">
                <option value="">Select Value</option>
                <option v-for="value in selectedGameParams[selectedCategory][selectedKey]" :key="value">{{ value }}</option>
              </select>
            </div>
          </div>
        </div>
      </div>
      <button type="submit">Create Listing</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';
import {useUserStore} from "@/stores/user";

export default {
  setup() {
    const userStore = useUserStore();

    return {
      userStore
    };
  },
  data() {
    return {
      shortDescription: '',
      description: '',
      price: 0,
      selectedGameId: null,
      games: [],
      selectedGameParams: null,
      selectedCategory: '',
      selectedKey: '',
      selectedValue: '',
    };
  },
  computed: {
    computedGameParams() {
    const selectedGame = this.games.find(game => game.id === this.selectedGameId);
    if (selectedGame) {
      return selectedGame.params || {};
    }
    return null;
  },
  },
  watch: {
    selectedGameId() {
    this.computedGameParams = this.getGameParamsById(this.selectedGameId);
  },
  },
  mounted() {
    this.fetchGames();
  },
  methods: {
    fetchGames() {
      axios
          .get('/api/v1/home/')
          .then(response => {
            this.games = response.data;
          })
          .catch(error => {
            console.error('Error fetching games:', error);
          });
    },
    updateSelectedGameId() {
  this.selectedGameParams = this.getGameParamsById(this.selectedGameId);
  for (const paramName in this.selectedGameParams) {
    const param = this.selectedGameParams[paramName];
    if (this.isObject(param)) {
      this.selectedGameParams[paramName] = param;
    }
  }
  for (const paramName in this.selectedGameParams) {
    const param = this.selectedGameParams[paramName];
    if (typeof param.value === 'undefined') {
      if (Array.isArray(param) && param.length > 0) {
        param.value = param[0];
      } else {
        param.value = '';
      }
    }
  }
},
    updateSelectedCategory() {
      this.selectedKey = '';
      this.selectedValue = '';
    },
    updateSelectedKey() {
      this.selectedValue = '';
    },
    onUpdate(subparamName, value) {
  this.$emit('update', {
    ...this.param,
    [subparamName]: value
  });
},
  isObject(value) {
    return typeof value === 'object' && value !== null && !Array.isArray(value);
  },
    getGameParamsById(gameId) {
      const selectedGame = this.games.find(game => game.id === gameId);
      if (selectedGame) {
        return selectedGame.params || {};
      }
      return null;
    },

    createListing() {
  const parametrs = {
        "Category": this.selectedCategory,
        "Key": this.selectedKey,
        "Value": this.selectedValue,
      };
  const data = {
    short_description: this.shortDescription,
    description: this.description,
    price: this.price,
    game_id: this.selectedGameId,
    user_id: this.userStore.user.id,
    params: parametrs
  };

      axios
          .post('api/v1/create/', data)
          .then(response => {
            console.log('Listing created:', response.data);
          })
          .catch(error => {
            console.error('Error creating listing:', error);
          });
    },
  },
};
</script>

<style>
.container {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  font-family: Arial, sans-serif;
}

.form-group {
  margin-bottom: 20px;
}

label {
  display: block;
  font-weight: bold;
  margin-bottom: 5px;
}

input[type="text"],
input[type="number"],
textarea,
select {
  width: 100%;
  padding: 5px;
  font-size: 16px;
}

button[type="submit"] {
  padding: 10px 20px;
  font-size: 16px;
  background-color: #4caf50;
  color: white;
  border: none;
  cursor: pointer;
}
</style>
