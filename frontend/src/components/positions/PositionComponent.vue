<script setup lang="ts">
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import MarkdownIt from 'markdown-it'
import type { PositionType } from '@/types'

const props = defineProps<{ position: PositionType }>()
defineEmits(['deletePosition'])

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
        <h1 class="text-2xl font-bold mb-1">{{ toTitleCase(position.company) }}</h1>
        <h2 class="text-lg text-gray-700">{{ toTitleCase(position.title) }}</h2>
      </div>

      <div>
        <div v-html="renderedMarkdown" class="prose max-w-none"></div>
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
