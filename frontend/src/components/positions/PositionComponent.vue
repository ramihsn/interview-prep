<script setup lang="ts">
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { computed } from 'vue'

import { toTitleCase } from '@/helpers/string'
import Position from '@/models/Position'
import md from '@/utils/markdown'

const props = defineProps<{
  position: Position
  isSelected: boolean
}>()
defineEmits(['deletePosition', 'selectPosition'])

const renderedMarkdown = md.render(props.position.description)
const positionDesorption = computed(() => {
  if (renderedMarkdown.length <= 250) {
    return renderedMarkdown
  }
  return renderedMarkdown.slice(0, 250) + ' ...'
})
</script>

<template>
  <div
    class="card shadow-xl no-select"
    @click="$emit('selectPosition', position)"
    :class="{ 'bg-secondary': isSelected, 'bg-neutral': !isSelected }"
  >
    <!-- Delete button -->
    <div
      class="absolute top-3 right-4 p-1 cursor-pointer hover:animate-bounce-once"
      @click.stop="$emit('deletePosition', position)"
    >
      <FontAwesomeIcon
        icon="trash-can"
        size="lg"
        class="hover:text-red-600"
        :class="{ 'text-secondary-content': isSelected, 'text-neutral-content': !isSelected }"
      />
    </div>

    <!-- Position Content -->
    <div class="card-body">
      <div class="flex flex-col items-center mb-5">
        <h1
          :class="{ 'text-secondary-content': isSelected, 'text-neutral-content': !isSelected }"
          class="text-2xl font-bold mb-1"
        >
          {{ toTitleCase(position.company) }}
        </h1>
        <h2
          :class="{ 'text-secondary-content': isSelected, 'text-neutral-content': !isSelected }"
          class="text-lg"
        >
          {{ toTitleCase(position.title) }}
        </h2>
      </div>

      <div>
        <div
          v-html="positionDesorption"
          class="prose max-w-none"
          :class="{ 'text-secondary-content': isSelected, 'text-neutral-content': !isSelected }"
        ></div>
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
