<script setup lang="ts">
import { defineProps, defineEmits } from 'vue'
import { deletePosition } from '@/api/positionService'

// Props
const props = defineProps({
  positionId: Number || undefined,
  companyName: String,
  positionTitle: String,
})

const relatedQuestionsCount = 5 // TODO: Fetch related questions count

// Emits
const emit = defineEmits(['confirm', 'close'])

function onConfirmDelete() {
  if (props.positionId) {
    deletePosition(props.positionId)
      .then(() => {
        emit('confirm')
      })
      .catch((error) => {
        console.error('Error deleting position:', error)
        // TODO: TBD || Show error message
      })
  } else {
    emit('close')
  }
}
</script>

<template>
  <div class="modal-box">
    <!-- Modal Header -->
    <h3 class="text-lg font-bold text-error">Confirm Deletion</h3>

    <!-- Modal Body -->
    <p class="py-4">
      Are you sure you want to delete the position
      <strong class="text-primary">{{ positionTitle }}</strong>
      at
      <strong class="text-primary">{{ companyName }}</strong>
      ?
      <br />
      This action will also delete <strong>{{ relatedQuestionsCount }}</strong> related question(s).
      This action cannot be undone.
    </p>

    <!-- Modal Actions -->
    <div class="modal-action flex justify-end space-x-4">
      <!-- Cancel Button -->
      <button class="btn btn-ghost" @click="$emit('close')">Cancel</button>
      <!-- Confirm Button -->
      <button class="btn btn-error" @click="onConfirmDelete">Delete</button>
    </div>
  </div>
</template>
