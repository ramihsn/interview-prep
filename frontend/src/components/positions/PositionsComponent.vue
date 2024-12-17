<script lang="ts" setup>
import { ref, onMounted } from 'vue'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

import Position from '@/models/Position'
import PositionForm from './PositionForm.vue'
import ConfirmDeletion from '../ConfirmDeletion.vue'
import PositionComponent from './PositionComponent.vue'
import { useUserSettingsStore } from '@/stores/userSettings'
import ModuleComponent from '@/components/ModuleComponent.vue'
import { countPositionQuestions } from '@/api/questionsService'
import { fetchPositions, deletePosition as deletePositionFunc } from '@/api/positionService'

const userSettingsStore = useUserSettingsStore()

// Variables
const positions = ref<Position[]>([])
const addNewPosition = ref(false)
const deletePosition = ref(false)
const selectedPosition = ref<Position | null>(null)
const toBeDeletedPosition = ref<Position | null>(null)
const toBeDeletedPositionQuestionsCount = ref(0)

// Lifecycle Hooks
onMounted(() => {
  fetchPositions().then((data) => {
    if (data.length === 0) {
      return
    }

    positions.value = data
    if (userSettingsStore.positionIndex === null) {
      selectedPosition.value = positions.value[0]
      userSettingsStore.setPositionIndex(positions.value[0].id)
    } else {
      selectedPosition.value =
        positions.value.find((pos) => pos.id === userSettingsStore.positionIndex) ??
        positions.value[0]
    }
  })
})

const onAddPosition = (newPosition: Position) => {
  positions.value.push(newPosition)
  addNewPosition.value = false
  if (positions.value.length === 1) {
    onSelectPosition(newPosition)
    userSettingsStore.setPositionIndex(newPosition.id)
  }
}

const onDeletePosition = (position: Position) => {
  console.log('Deleting position', position)
  deletePosition.value = true
  toBeDeletedPosition.value = position
  getPositionQuestionsCount(position.id).then((count) => {
    toBeDeletedPositionQuestionsCount.value = count
  })
}

const onPositionDeleted = () => {
  positions.value = positions.value.filter((pos) => pos !== toBeDeletedPosition.value)
  if (selectedPosition.value === toBeDeletedPosition.value && toBeDeletedPosition.value) {
    onSelectPosition(toBeDeletedPosition.value, { reset: true })
    deletePosition.value = false
  }

  if (positions.value.length === 0) {
    userSettingsStore.setPositionIndex(null)
  }
}

const onSelectPosition = (position: Position, options: { reset?: boolean } = { reset: false }) => {
  const { reset } = options

  if (selectedPosition.value === position) {
    if (reset) {
      if (positions.value.length > 0) {
        selectedPosition.value = positions.value[0]
        userSettingsStore.setPositionIndex(positions.value[0].id)
        userSettingsStore.selectedPosition = positions.value[0]
      } else {
        selectedPosition.value = null
        userSettingsStore.setPositionIndex(null)
        userSettingsStore.selectedPosition = null
      }
    }
  } else {
    selectedPosition.value = position
    userSettingsStore.setPositionIndex(position.id)
    userSettingsStore.selectedPosition = position
  }
}

const getPositionQuestionsCount = async (positionID: number) => {
  return await countPositionQuestions(positionID)
}
</script>

<template>
  <div class="flex flex-col items-center justify-center pt-5 h-full">
    <Teleport to=".question-module" v-if="addNewPosition">
      <ModuleComponent @close="addNewPosition = false">
        <PositionForm
          class="mt-3 mb-12 w-full"
          @addPosition="onAddPosition"
          @close="addNewPosition = false"
          :inModule="true"
        />
      </ModuleComponent>
    </Teleport>

    <Teleport to=".question-module" v-if="deletePosition">
      <ModuleComponent @close="deletePosition = false">
        <div class="flex items-center justify-center">
          <ConfirmDeletion
            :itemID="toBeDeletedPosition?.id"
            :deleteFunction="deletePositionFunc"
            @close="deletePosition = false"
            @confirm="onPositionDeleted"
          >
            Are you sure you want to delete the position
            <strong class="text-primary">{{ toBeDeletedPosition?.title }}</strong>
            at
            <strong class="text-primary">{{ toBeDeletedPosition?.company }}</strong>
            ?
            <br />
            This action will also delete
            <strong>{{ toBeDeletedPositionQuestionsCount }}</strong> related question(s). This
            action cannot be undone.
          </ConfirmDeletion>
        </div>
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
