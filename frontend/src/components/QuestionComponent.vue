<script lang="ts" setup>
import { ref } from 'vue'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

import ModuleComponent from './ModuleComponent.vue'
import QuestionEditor from './QuestionEditor.vue'
import AnswerComponent from './AnswerComponent.vue'
import type { QuestionType } from '../types'

defineEmits(['delete'])
const props = defineProps<{ question: QuestionType }>()
const baseURL = import.meta.env.VITE_BASE_URL
const markAsDone = ref(false)
const isLoading = ref(false)
const editQuestion = ref(false)

function toggleMarkAsDone() {
  isLoading.value = true // Set loading to true before API call
  const newState = markAsDone.value ? 'mark-as-unanswered' : 'mark-as-answered'

  changeQuestionState(props.question.id, newState)
}

async function changeQuestionState(questionId: number, newState: string) {
  const headers = { 'Content-Type': 'application/json' }
  const requestParams = { method: 'POST', headers }

  try {
    const res = await fetch(`${baseURL}/api/v1/questions/${questionId}/${newState}`, requestParams)
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
</script>

<template>
  <div
    class="card bg-primary text-primary-content shadow custom relative mb-10 pb-2"
    :class="{ done: markAsDone }"
    :id="`question-${question.id}`"
  >
    <Teleport to=".question-module" v-if="editQuestion">
      <ModuleComponent @close="editQuestion = false">
        <QuestionEditor />
      </ModuleComponent>
    </Teleport>

    <div class="absolute bottom-2 right-2 mb-5 mr-3 cursor-pointer">
      <FontAwesomeIcon
        size="xl"
        icon="pen-to-square"
        class="mr-5 hover:text-red-500"
        @click="editQuestion = true"
      />
      <FontAwesomeIcon
        size="xl"
        icon="trash-can"
        class="mr-3 hover:text-red-500"
        @click="$emit('delete', question.id)"
      />
    </div>

    <div class="card-body">
      <h2 class="card-title">
        <strong>
          <span>Topic: </span>
          <span>{{ question.topic }}</span>
        </strong>
      </h2>
      <div :hidden="markAsDone" class="mt-3">
        <p class="pb-3">
          <strong>Difficulty Level: {{ question.difficulty }}</strong>
        </p>
        <p class="pb-3">
          <strong>Question</strong>
          <span class="ml-1">:</span>
          <br />
          <span>{{ question.question }}</span>
        </p>
        <hr class="pb-3" />
        <h2>Answer:</h2>
        <AnswerComponent :answer="question.answer" />
      </div>
    </div>

    <div class="card-actions pl-3">
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
</style>
