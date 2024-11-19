<script lang="ts" setup>
import { onMounted, ref } from 'vue'
import type { AnswerType } from '@/types'

const props = defineProps<{ answer: AnswerType | undefined }>()
const answerText = ref<string>(props.answer?.answer || '')
const reviewText = ref<string>(props.answer?.review || '')
const rating = ref<number | null>(props.answer?.rating || null)

onMounted(() => {
  if (props.answer) {
    console.log(props.answer)
    const rating = props.answer?.rating
    console.log('is', rating, 'Integer?', Number.isInteger(rating), typeof rating)
  }
})
</script>

<template>
  <div class="p-4 space-y-4">
    <!-- Textarea for answer input -->
    <textarea
      v-model="answerText"
      class="textarea textarea-bordered w-full resize-none p-4"
      placeholder="Write your answer here..."
    ></textarea>

    <!-- Display the answer details if available -->
    <div class="card shadow-lg bg-base-100 p-4 space-y-4">
      <!-- Review Section -->
      <div class="space-y-2">
        <div class="font-bold text-lg">Review:</div>
        <pre class="text-sm text-gray-600 whitespace-pre-wrap">{{ reviewText }}</pre>
      </div>

      <!-- Rating Section -->
      <div class="flex items-center space-x-2">
        <span class="font-bold text-lg">Rating:</span>
        <span class="badge badge-primary">
          <span v-if="Number.isInteger(rating)">{{ rating }}</span>
          <span v-else>{{ rating }}</span>
          <span>/10</span>
        </span>
      </div>
    </div>
  </div>
</template>
