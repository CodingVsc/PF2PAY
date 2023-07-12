<template>
  <div>
    <span>{{ paramName }}:</span>
    <div v-if="isObject(param)">
      <recursive-component
        v-for="(subparam, subparamName) in param"
        :key="subparamName"
        :param="subparam"
        :paramName="subparamName"
        @update="onUpdate(subparamName, $event)"
      ></recursive-component>
    </div>
    <div v-else>
      <input v-if="typeof param === 'string' || typeof param === 'number'" :value="param" @input="$emit('update', $event.target.value)">
      <input v-else-if="typeof param === 'boolean'" type="checkbox" :checked="param" @change="$emit('update', $event.target.checked)">
    </div>
  </div>
</template>

<script>
export default {
  props: {
    param: {
      required: true
    },
    paramName: {
      type: String,
      required: true
    }
  },
  methods: {
    isObject(value) {
      return typeof value === 'object' && value !== null;
    },
    onUpdate(subparamName, value) {
      this.$emit('update', {
        [subparamName]: value
      });
    }
  }
};
</script>

<style scoped>
/* Стили компонента */
</style>
