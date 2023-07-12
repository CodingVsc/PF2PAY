<template>
  <nav>
    <ul>
      <li>
        <a href="#">Home</a>
      </li>
      <li>
        <a href="#">About</a>
      </li>
      <li>
        <a href="#" @click="toggleDropdown">Dropdown link</a>
        <ul v-show="isDropdownOpen">
          <li>
            <a href=#>Profile</a>
          </li>
          <li>
            <a href="/create_product">Create an offer</a>
          </li>
          <li>
            <a href="/logout">Log Out</a>
          </li>
        </ul>
      </li>
    </ul>
  </nav>
</template>

<script>
export default {
  data() {
    return {
      isDropdownOpen: false
    };
  },
  methods: {
    toggleDropdown() {
      this.isDropdownOpen = !this.isDropdownOpen;
    }
  }
};
</script>