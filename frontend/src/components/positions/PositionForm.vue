<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

import { createPosition } from '@/api/positionService'
import PositionCreate from '@/models/PositionCreate';
import Position from '@/models/Position';

const emit = defineEmits(['addPosition', 'close'])
defineProps({ inModule: { type: Boolean, required: false, default: false } })

// Variables
const position = ref<PositionCreate>(new PositionCreate())
const companyInput = ref<HTMLInputElement | null>(null)
const hasError = ref(false)

// Functions
function addPosition() {
  if (!position.value.isValid) {
    hasError.value = true
    setTimeout(() => hasError.value = false, 5000)
    return
  }
  createPosition(position.value).then((data) => {
    emit('addPosition', data as Position)
    position.value.clear()
  }).catch((error) => {
    console.error(error)
    emit('close')
    // TODO: maybe we should show the error to the user
  })
}

onMounted(() => {
  companyInput.value?.focus()
})
</script>

<template>
  <div class="modal-box w-2/3 max-w-5xl">
    <!-- Modal Header -->
    <h3 class="text-lg font-bold text-info">Add New Position</h3>

    <!-- Modal Body -->
    <p class="py-4">
      <table class="table w-full">
        <tr>
          <th class="flex max-w-max pr-4">
            <label for="title">Company</label>
          </th>
          <td>
            <input
              ref="companyInput"
              class="input input-bordered input-primary w-full"
              :class="{ 'border-2 border-rose-500': hasError && !position.company }"
              type="text"
              v-model="position.company"
            />
          </td>
        </tr>
        <tr>
          <th class="flex max-w-max pr-4">
            <label for="title">Title</label>
          </th>
          <td>
            <input
              class="input input-bordered input-primary w-full"
              :class="{ 'border-2 border-rose-500': hasError && !position.title }"
              type="text"
              v-model="position.title"
            />
          </td>
        </tr>
        <tr>
          <th class="flex max-w-max pr-4">
            <label for="description">Description</label>
          </th>
          <td>
            <textarea
              class="textarea textarea-primary w-full"
              :class="{ 'border-2 border-rose-500': hasError && !position.description }"
              rows="5"
              v-model="position.description"
            ></textarea>
          </td>
        </tr>
      </table>

      <transition name="fade" appear>
        <div class="bg-warning border-2 border-rose-500 rounded-lg flex flex-row" v-if="hasError">
          <span class="mx-2">
            <FontAwesomeIcon icon="circle-exclamation" style="color: #e42807" />
          </span>
          <strong>All fields must be filled before adding the position</strong>
        </div>
      </transition>
    </p>

    <!-- Modal Actions -->
    <div class="modal-action flex justify-end space-x-4">
      <!-- Cancel Button -->
      <button class="btn btn-ghost" @click="$emit('close')">Cancel</button>
      <!-- Confirm Button -->
      <button class="btn btn-success" @click="addPosition">Add Position</button>
    </div>
  </div>
</template>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
