<script setup lang="ts">
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import MarkdownIt from 'markdown-it'
import type { PositionType } from '@/types'
import { computed } from 'vue'

const props = defineProps<{
  position: PositionType
  isSelected: boolean
}>()
defineEmits(['deletePosition', 'selectPosition'])

function toTitleCase(str: string) {
  return str
    .toString()
    .toLowerCase()
    .replace(/\b\w/g, (char) => char.toUpperCase())
}

// Markdown Rendering
const md = new MarkdownIt({
  html: true,
  linkify: true,
  typographer: true,
})
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
    :class="{ 'bg-primary': isSelected, 'bg-accent': !isSelected }"
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
        :class="{ 'text-primary-content': isSelected, 'text-accent-content': !isSelected }"
      />
    </div>

    <!-- Position Content -->
    <div class="card-body">
      <div class="flex flex-col items-center mb-5">
        <h1
          :class="{ 'text-primary-content': isSelected, 'text-accent-content': !isSelected }"
          class="text-2xl font-bold mb-1"
        >
          {{ toTitleCase(position.company) }}
        </h1>
        <h2
          :class="{ 'text-primary-content': isSelected, 'text-accent-content': !isSelected }"
          class="text-lg text-gray-700"
        >
          {{ toTitleCase(position.title) }}
        </h2>
      </div>

      <div>
        <div
          v-html="positionDesorption"
          class="prose max-w-none"
          :class="{ 'text-primary-content': isSelected, 'text-secondary-content': !isSelected }"
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
