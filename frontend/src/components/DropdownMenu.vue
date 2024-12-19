<script setup lang="ts">
import { ref } from 'vue'

import { GroupsEnum } from '@/enums/GroupsEnum'
import { useUserSettingsStore } from '@/stores/userSettings'

const userSettingsStore = useUserSettingsStore()
const isDropdownOpen = ref(false)

function selectOption(option: GroupsEnum) {
  if (option !== userSettingsStore.groupBy) {
    userSettingsStore.setGroupBy(option)
    isDropdownOpen.value = false
  }
}
</script>

<template>
  <div class="inline-block ml-4 mt-3 no-select">
    <!-- Dropdown Trigger -->
    <button
      @click="isDropdownOpen = !isDropdownOpen"
      class="px-4 py-2 bg-blue-500 text-white font-semibold rounded hover:bg-blue-600 flex items-center justify-between w-50"
    >
      <!-- <span> Group By: {{ currentSelection.label }} </span> -->
      <span class="flex items-center space-x-2">
        <span>Group By:</span>
        <span>{{ userSettingsStore.groupBy ?? 'None' }}</span>
      </span>
      <svg
        xmlns="http://www.w3.org/2000/svg"
        class="h-5 w-5 ml-2 transform transition-transform duration-200"
        viewBox="0 0 20 20"
        fill="currentColor"
        :class="{ 'rotate-90': isDropdownOpen }"
      >
        <path
          fill-rule="evenodd"
          d="M7.21 5.23a.75.75 0 010 1.06L10.92 10l-3.71 3.71a.75.75 0 101.06 1.06l4-4a.75.75 0 000-1.06l-4-4a.75.75 0 00-1.06 0z"
          clip-rule="evenodd"
        />
      </svg>
    </button>

    <!-- Dropdown Menu -->
    <div
      v-if="isDropdownOpen"
      class="absolute top-full left-0 bg-white border rounded shadow-md mt-2 w-40"
    >
      <ul class="py-1">
        <li
          v-for="option in GroupsEnum"
          :key="option"
          @click="selectOption(option)"
          class="px-4 py-2 cursor-pointer transition-all duration-150 flex items-center justify-between"
          :class="{
            'bg-blue-500 text-white': option === userSettingsStore.groupBy,
            'hover:bg-blue-100 hover:text-blue-600': option !== userSettingsStore.groupBy,
          }"
        >
          {{ option }}
          <span v-if="option === userSettingsStore.groupBy" class="text-white font-bold"> ✔ </span>
        </li>
      </ul>
    </div>
  </div>
</template>
