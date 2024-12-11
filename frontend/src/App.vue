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
    <NavBar class="h-[8vh]" />
    <div class="h-[93vh] overflow-auto">
      <RouterView />
    </div>
  </main>
</template>
