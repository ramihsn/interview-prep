<script lang="ts" setup>
import { ref } from 'vue'
import MarkdownIt from 'markdown-it'

import AnswerCreate from '@/models/AnswerCreate'
import Answer from '@/models/Answer'

const props = defineProps<{ answer: Answer | AnswerCreate }>()
const emit = defineEmits(['submitAnswer'])

// Markdown Rendering
const md = new MarkdownIt({
  html: true,
  linkify: true,
  typographer: true,
})

const answerText = ref<string>(md.render(props.answer?.answer) || '')
const editAnswer = ref(false)
const reviewText = ref<string>(md.render(props.answer?.review) || '')
const editReview = ref(false)
const rating = ref<number | null>(props.answer?.rating ?? null)
const ratingError = ref(false)

function emitAnswer() {
  if (rating.value === null || rating.value < 0 || rating.value > 10) {
    ratingError.value = true
    return
  }
  if (answerText.value === '') {
    // TODO: show error message
    return
  }
  ratingError.value = false

  emit('submitAnswer', {
    answer: answerText.value,
    review: reviewText.value,
    rating: rating.value,
    question_id: props.answer.question_id,
  } as AnswerCreate)
}

defineExpose({ emitAnswer })
</script>

<template>
  <div class="p-4 space-y-4">
    <!-- Textarea for answer input -->
    <div
      v-if="answerText && !editAnswer"
      v-html="answerText"
      class="prose"
      @dblclick="editAnswer = true"
    ></div>
    <textarea
      v-else
      v-model="answerText"
      class="textarea textarea-bordered w-full p-4"
      placeholder="Write your answer here..."
      @keyup.esc="editAnswer = false"
    ></textarea>

    <!-- Display the answer details if available -->
    <div class="card shadow-lg bg-base-100 p-4 space-y-4">
      <!-- Review Section -->
      <div class="space-y-2">
        <div class="font-bold text-lg">Review:</div>
        <div
          v-if="reviewText && !editReview"
          v-html="reviewText"
          class="prose"
          @dblclick="editReview = true"
        ></div>
        <textarea
          v-else
          v-model="reviewText"
          class="textarea w-full p-4"
          placeholder="Write your review here..."
          @keyup.esc="editReview = false"
        ></textarea>
      </div>

      <!-- Rating Section -->
      <div class="flex items-center space-x-2">
        <span class="font-bold text-lg">Rating:</span>
        <input
          v-model="rating"
          type="number"
          min="0"
          max="10"
          class="input input-primary w-16"
          :class="{ 'input-error': ratingError }"
          placeholder="10"
        />
        <span> / 10</span>
      </div>
    </div>
    <span v-if="ratingError">The rating value should be between 0 and 10</span>
  </div>
</template>
