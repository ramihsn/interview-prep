<script lang="ts" setup>
import { onMounted, onUnmounted } from 'vue'

const emit = defineEmits(['close'])

const handleKeydown = (event: KeyboardEvent) => {
  if (event.key === 'Escape') emit('close')
}

onMounted(() => {
  window.addEventListener('keydown', handleKeydown)
})

onUnmounted(() => {
  window.removeEventListener('keydown', handleKeydown)
})
</script>

<template>
  <div class="backdrop" @click.self="$emit('close')">
    <div class="module w-9/12" @click.self="$emit('close')">
      <slot />
    </div>
  </div>
</template>

<style scoped>
.backdrop {
  background-color: rgba(0, 0, 0, 0.5);
  position: fixed;
  top: 7%;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.module {
  padding: 1rem;
  border-radius: 10px;
}
</style>
