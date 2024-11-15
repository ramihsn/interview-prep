<script lang="ts" setup>
import { ref } from 'vue'
import { RouterView } from 'vue-router'

import NavBar from './components/NavBar.vue'
import { Theme } from './themes'

const theme = ref(Theme.DARK)
const onThemeSet = (newTheme: Theme) => (theme.value = newTheme)
</script>

<template>
  <main :data-theme="theme">
    <NavBar @setTheme="onThemeSet" :theme="theme" />
    <RouterView />
  </main>
</template>
