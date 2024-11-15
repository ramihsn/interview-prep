<script lang="ts" setup>
import { onMounted, ref } from 'vue'

import type { QuestionType } from '../types'

const props = defineProps<{ question: QuestionType }>()
const markAsDone = ref(false)
const isLoading = ref(false)

function toggleMarkAsDone() {
  isLoading.value = true // Set loading to true before API call
  const newState = markAsDone.value ? 'mark-as-unanswered' : 'mark-as-answered'

  changeQuestionState(props.question.id, newState)
}

async function changeQuestionState(questionId: number, newState: string) {
  const headers = { 'Content-Type': 'application/json' }
  const requestParams = { method: 'POST', headers }

  try {
    const res = await fetch(
      `http://127.0.0.1:6970/api/v1/questions/${questionId}/${newState}`,
      requestParams,
    )
    if (!res.ok) {
      throw new Error('Network response was not ok')
    }
  } catch (err) {
    console.error('FU', err)
    markAsDone.value = !markAsDone.value
  } finally {
    isLoading.value = false // Reset loading after API call
  }
}

onMounted(() => {
  if (props.question.id === 1) {
    console.log(`Question with ID ${props.question.id} mounted`)
    console.log(props.question)
  }
})
</script>

<template>
  <div
    class="card bg-primary text-primary-content shadow custom relative"
    :class="{ done: markAsDone }"
  >
    <div class="card-body">
      <h2 class="card-title">
        <strong>Topic: {{ question.topic }}</strong>
      </h2>
      <p :hidden="markAsDone">
        <strong>Difficulty Level: {{ question.difficulty }}</strong>
      </p>
      <p :hidden="markAsDone">
        <strong>Question</strong>
        <span class="ml-1">:</span>
        <br />
        <span>{{ question.question }}</span>
      </p>
    </div>

    <div class="card-actions">
      <label class="btn btn-ghost">
        <input
          type="checkbox"
          @click="toggleMarkAsDone"
          v-model="markAsDone"
          :disabled="isLoading"
        />
        <span>Mark as Done</span>
      </label>
    </div>

    <!-- Loading Spinner Overlay -->
    <div
      v-if="isLoading"
      class="absolute inset-0 flex items-center justify-center bg-black bg-opacity-50"
    >
      <div class="spinner-border animate-spin inline-block w-8 h-8 border-4 rounded-full"></div>
    </div>
  </div>
</template>

<style scoped>
.custom {
  border-radius: 30px;
}

.done {
  text-decoration: line-through;
}

.spinner-border {
  border-color: white transparent transparent transparent;
}

textarea {
  transition: height 0.2s ease;
}
</style>
