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
  <main :data-theme="userSettingsStore.theme" class="flex flex-col h-screen">
    <NavBar />
    <div class="flex-1 overflow-auto">
      <RouterView />
    </div>
  </main>
</template>
