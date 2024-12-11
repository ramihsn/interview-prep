<script setup lang="ts">
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import type { PositionType } from '@/types'

defineProps<{ position: PositionType }>()
defineEmits(['deletePosition'])
</script>

<template>
  <div class="card bg-base-300 shadow-xl">
    <!-- Delete button -->
    <div class="absolute top-4 right-5">
      <FontAwesomeIcon
        icon="trash-can"
        size="lg"
        @click="$emit('deletePosition', position)"
        class="text-gray-600 hover:text-red-600 hover:animate-bounce-once cursor-pointer"
      />
    </div>

    <!-- Position Content -->
    <div class="card-body">
      <div class="flex flex-col items-center mb-5">
        <h1 class="text-2xl font-bold mb-1">{{ position.company }}</h1>
        <h2 class="text-lg text-gray-700">{{ position.title }}</h2>
      </div>

      <div>
        {{ position.description }}
      </div>
    </div>
  </div>
</template>

<style scoped>
@keyframes bounce-once {
  0%,
  20%,
  50%,
  80%,
  100% {
    transform: translateY(0);
  }
  40% {
    transform: translateY(-10px);
  }
  60% {
    transform: translateY(-5px);
  }
}

.hover\:animate-bounce-once:hover {
  animation: bounce-once 0.6s ease;
}
</style>
