<script lang="ts" setup>
import { ref, onMounted } from 'vue'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

import type { PositionType } from '@/types'
import PositionForm from './PositionForm.vue'
import PositionComponent from './PositionComponent.vue'
import { useUserSettingsStore } from '@/stores/userSettings'
import ModuleComponent from '@/components/ModuleComponent.vue'

const userSettingsStore = useUserSettingsStore()

// Variables
const positions = ref<PositionType[]>([]) // TODO: fetch positions
const addNewPosition = ref(false)
const selectedPosition = ref<PositionType | null>(null)

// Lifecycle Hooks
onMounted(() => {
  selectedPosition.value = positions.value[userSettingsStore.positionIndex ?? 0]
})

// Functions
const onAddPosition = (position: PositionType) => {
  positions.value.push(position)
  addNewPosition.value = false
  // TODO: save to database
}

const onDeletePosition = (position: PositionType) => {
  console.log('Deleting position', position)
  positions.value = positions.value.filter((pos) => pos !== position)
  if (selectedPosition.value === position) onSelectPosition(position)
  // TODO: delete from database
}

const onSelectPosition = (position: PositionType) => {
  if (selectedPosition.value === position) {
    if (positions.value.length > 0) {
      selectedPosition.value = positions.value[0]
      userSettingsStore.setPositionIndex(0)
    } else {
      userSettingsStore.setPositionIndex(null)
    }
  } else {
    selectedPosition.value = position
    userSettingsStore.setPositionIndex(position.id ?? -1)
  }
}
</script>

<template>
  <div class="flex flex-col items-center justify-center pt-5 h-full">
    <Teleport to=".question-module" v-if="addNewPosition">
      <ModuleComponent @close="addNewPosition = false">
        <PositionForm
          class="mt-3 mb-12 w-2/3"
          @addPosition="onAddPosition"
          @close="addNewPosition = false"
          :inModule="true"
        />
      </ModuleComponent>
    </Teleport>

    <!-- show the positions here if exists -->
    <div
      v-if="positions.length !== 0"
      class="flex flex-col items-center justify-center h-full w-full"
    >
      <div v-for="pos in positions" :key="pos.id ?? -1" :pos="pos" class="my-3 w-2/3">
        <PositionComponent
          :position="pos"
          :isSelected="selectedPosition === pos || positions.length === 1"
          @deletePosition="onDeletePosition"
          @selectPosition="onSelectPosition"
        />
      </div>

      <div class="fixed bottom-6 right-10 flex space-x-4">
        <FontAwesomeIcon
          icon="plus"
          size="2xl"
          class="btn btn-circle btn-outline btn-primary p-1"
          @click="addNewPosition = true"
        />
      </div>
    </div>

    <!-- There are no positions to show -->
    <div
      v-else
      class="flex flex-col items-center justify-center pt-5 h-full w-full"
      style="min-height: calc(100vh - var(--header-height))"
    >
      <!-- Alert Message -->
      <div
        class="flex items-center bg-blue-100 text-blue-800 px-6 py-4 mb-6 rounded-lg shadow-md max-w-lg text-center mb-12"
        role="alert"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
          class="stroke-current h-6 w-6 mr-3"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
          />
        </svg>
        <span> <strong>It's lonely here.</strong> Add positions to get started. </span>
      </div>

      <PositionForm class="mt-3 mb-12 w-2/3" @addPosition="onAddPosition" />
    </div>
  </div>
</template>
