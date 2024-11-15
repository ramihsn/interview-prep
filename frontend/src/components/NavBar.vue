<script lang="ts" setup>
import { defineProps, defineEmits, computed } from 'vue'

import { isDarkTheme, toggleTheme } from '@/themes'

defineEmits(['setTheme'])
const props = defineProps(['theme'])
const isDark = computed(() => isDarkTheme(props.theme))
const isQuestionsPage = computed(() => window.location.pathname === '/')
</script>

<template>
  <nav class="navbar bg-gray-500">
    <div class="navbar-start ml-4">
      <div class="flex items-center space-x-3">
        <img src="/public/icon.svg" alt="Nvidia Logo" class="w-10 h-10" />
        <span class="text-2xl font-semibold dark:text-white">Interview Prep</span>
      </div>
    </div>

    <div class="navbar-end mr-4">
      <div class="flex items-center space-x-0">
        <a
          @click="$router.push({ name: 'home' })"
          :class="{ shadow: isQuestionsPage }"
          class="btn btn-ghost"
          >Home</a
        >

        <div class="btn btn-ghost" @click="$emit('setTheme', toggleTheme(props.theme))">
          <img
            v-if="isDark"
            src="/public/dark-theme-svgrepo-com.svg"
            alt="Nvidia Logo"
            class="w-6 h-6"
          />
          <img v-else src="/public/light-mode-svgrepo-com.svg" alt="Nvidia Logo" class="w-6 h-6" />
        </div>
      </div>
    </div>
  </nav>
</template>
