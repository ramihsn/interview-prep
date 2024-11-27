<script lang="ts" setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'

import { useUserSettingsStore } from '@/stores/userSettings'

const router = useRoute()
const pageName = computed(() => router.name)

const userSettingsStore = useUserSettingsStore()
const isDark = computed(() => userSettingsStore.isDarkTheme)
</script>

<template>
  <nav class="navbar bg-gray-500">
    <div class="navbar-start ml-4">
      <div class="flex items-center space-x-3">
        <img src="/icon.svg" alt="Nvidia Logo" class="w-10 h-10" />
        <span class="text-2xl font-semibold dark:text-white no-select">Interview Prep</span>
      </div>
    </div>

    <div class="navbar-end mr-4">
      <div class="flex items-center space-x-0">
        <a
          @click="$router.push({ name: 'home' })"
          :class="{ shadow: pageName !== 'home' }"
          class="btn btn-ghost"
          >Home</a
        >
        <a
          @click="$router.push({ name: 'questions' })"
          :class="{ shadow: pageName !== 'questions' }"
          class="btn btn-ghost"
          >Questions</a
        >
        <a
          @click="$router.push({ name: 'job' })"
          :class="{ shadow: pageName !== 'job' }"
          class="btn btn-ghost"
          >Job</a
        >

        <div class="btn btn-ghost" @click="() => userSettingsStore.toggleTheme()">
          <img v-if="isDark" src="/dark-theme-svgrepo-com.svg" alt="Nvidia Logo" class="w-6 h-6" />
          <img v-else src="/light-mode-svgrepo-com.svg" alt="Nvidia Logo" class="w-6 h-6" />
        </div>
      </div>
    </div>
  </nav>
</template>
