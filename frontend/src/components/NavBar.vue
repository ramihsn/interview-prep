<script lang="ts" setup>
import { defineProps, defineEmits, computed } from 'vue'
import { useRoute } from 'vue-router'

import { isDarkTheme, toggleTheme } from '@/themes'

defineEmits(['setTheme'])
const router = useRoute()
const props = defineProps(['theme'])
const isDark = computed(() => isDarkTheme(props.theme))
const pageName = computed(() => router.name)
console.log(pageName.value)
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
