<script lang="ts" setup>
import { onBeforeMount } from 'vue'
import { RouterView } from 'vue-router'

import NavBar from './components/NavBar.vue'
import { useUserSettingsStore } from './stores/userSettings'

const userSettingsStore = useUserSettingsStore()

onBeforeMount(() => {
  userSettingsStore.fetchUserSettings()
})
</script>

<template>
  <main :data-theme="userSettingsStore.theme">
    <NavBar />
    <RouterView />
  </main>
</template>
