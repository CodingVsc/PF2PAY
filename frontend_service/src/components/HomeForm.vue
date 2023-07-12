<template>
  <div>
    <div v-for="(group, index) in groups" :key="index" class="record-group">
      <div v-for="record in group" :key="record.id" class="record-item">
        <div class="card">
          <div class="card-body">
            <router-link :to="`/game/${record.id}`" class="card-title">
              {{ record.game_name }}
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";

export default {
  data() {
    return {
      records: [] // Ваши данные записей из API
    };
  },
  computed: {
    groups() {
      const groups = [];
      const groupSize = 4;

      for (let i = 0; i < this.records.length; i += groupSize) {
        groups.push(this.records.slice(i, i + groupSize));
      }

      return groups;
    }
  },
  mounted() {
        axios.get('/api/v1/home').then(response => {
          this.records = response.data;
        });
  }
};
</script>

<style>
.record-group {
  display: flex;
  flex-wrap: wrap;
  margin-bottom: 10px;
}

.record-item {
  flex: 1 0 25%;
  padding: 10px;
  box-sizing: border-box;
}

.record-title {
  font-weight: bold;
}
</style>