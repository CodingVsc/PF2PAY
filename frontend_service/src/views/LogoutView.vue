<template>
  <div>
    <h1> ВЫ ВЫШЛИ ИЗ АККАУНТА </h1>
  </div>
</template>

<style>
</style>

<script>
    import { useUserStore } from '@/stores/user'

    export default {
        setup() {
            const userStore = useUserStore()

            return {
                userStore
            }
        },
        beforeCreate() {
            console.log('Log out')
            this.userStore.removeToken()
        }
    }
</script>