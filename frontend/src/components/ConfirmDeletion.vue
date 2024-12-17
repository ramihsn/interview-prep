<script setup lang="ts">
import type { PropType } from 'vue'

const emit = defineEmits(['confirm', 'close'])
const props = defineProps({
  itemID: Number,
  deleteFunction: Function as PropType<(itemID: number) => Promise<void>>,
})

function onConfirmDelete() {
  if (props.itemID) {
    const deleteFunction = props.deleteFunction as (itemID: number) => Promise<void>
    deleteFunction(props.itemID)
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
      <slot />
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
