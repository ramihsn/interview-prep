<script lang="ts" setup>
import { onMounted, ref, defineAsyncComponent } from 'vue'

import ModuleComponent from '../ModuleComponent.vue'
import QuestionsAdder from './QuestionsAdder.vue'
// import DropdownMenu from '../DropdownMenu.vue'
import type { QuestionType } from '../../types'

const baseURL = import.meta.env.VITE_BASE_URL
const addNewQuestion = ref(false)
const loading = ref<boolean>(true)
const hasFileUploadError = ref<string | null>(null)
const questions = ref<QuestionType[]>([])

const Question = defineAsyncComponent(() => import('./QuestionComponent.vue'))

onMounted(async () => {
  await fetchQuestions()
})

async function fetchQuestions() {
  const res = await fetch(`${baseURL}/api/v1/questions`, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
    },
  })
  questions.value = await res.json()
  loading.value = false
}

function onQuestionAdded(newQuestion: QuestionType) {
  console.log(newQuestion)
  questions.value.push(newQuestion)
  addNewQuestion.value = false
}
function onQuestionsAdded(newQuestions: QuestionType[]) {
  questions.value = [...questions.value, ...newQuestions]
  addNewQuestion.value = false
}

async function onDelete(questionId: number) {
  console.log('Remove Question with ID:', questionId)
  const res = await fetch(`${baseURL}/api/v1/questions/${questionId}`, {
    method: 'DELETE',
    headers: {
      'Content-Type': 'application/json',
    },
  })

  if (res.ok) {
    questions.value = questions.value.filter((q) => q.id !== questionId)
  }
}

function onFileUploadedError(error: string) {
  hasFileUploadError.value = error
  setTimeout(() => {
    hasFileUploadError.value = null
  }, 3000)
}
</script>

<template>
  <div class="koko">
    <Teleport to=".question-module" v-if="addNewQuestion">
      <ModuleComponent @close="addNewQuestion = false">
        <QuestionsAdder
          @questionAdded="onQuestionAdded"
          @fileUploaded="onQuestionsAdded"
          @fileUploadedError="onFileUploadedError"
        />
      </ModuleComponent>
    </Teleport>

    <!-- <DropdownMenu /> -->

    <div v-if="loading" class="pt-4 max-w-7xl w-full mx-auto custom-container">
      <Question
        v-for="i in 3"
        :key="i"
        class="mb-4 animate-pulse loading-question"
        :question="{ id: i, topic: '...', difficulty: '...', question: 'Loading...' }"
      />
    </div>

    <div v-else-if="questions.length > 0" class="pt-4 max-w-7xl w-full mx-auto custom-container">
      <Question class="mb-4" v-for="q in questions" :key="q.id" :question="q" @delete="onDelete" />
    </div>

    <div
      v-else
      class="wrapper bg-primary text-primary-content flex flex-col items-center justify-center p-6 custom-container"
      style="min-height: calc(100vh - var(--header-height))"
    >
      <!-- Alert Message -->
      <div
        class="flex items-center bg-blue-100 text-blue-800 px-6 py-4 mb-6 rounded-lg shadow-md max-w-lg text-center mb-12"
        role="alert"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 24 24"
          class="stroke-current h-6 w-6 mr-3"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
          />
        </svg>
        <span> <strong>It's lonely here.</strong> Add questions to get started. </span>
      </div>

      <!-- Questions Adder Component -->
      <div class="w-full max-w-2xl">
        <QuestionsAdder
          @questionAdded="onQuestionAdded"
          @fileUploaded="onQuestionsAdded"
          @fileUploadedError="onFileUploadedError"
          :embedded="false"
        />
      </div>
    </div>

    <!-- Error Alert -->
    <transition
      name="slide-up-down"
      enter-active-class="transition transform duration-300 ease-in-out"
      leave-active-class="transition transform duration-300 ease-in-out"
      enter-from-class="translate-y-full"
      enter-to-class="translate-y-0"
      leave-from-class="translate-y-0"
      leave-to-class="translate-y-full"
    >
      <div v-if="hasFileUploadError" class="fixed inset-x-0 bottom-0 p-4 bg-red-500 text-white">
        <div class="flex items-center justify-between">
          <span>{{ hasFileUploadError }}</span>
        </div>
      </div>
    </transition>

    <div class="fixed bottom-4 right-4">
      <button @click="addNewQuestion = true" class="btn btn-circle btn-primary text-4xl pb-2">
        +
      </button>
    </div>
  </div>
</template>

<style scoped>
.custom-container {
  padding-left: 10%;
  padding-right: 10%;

  height: 93vh;
  overflow-y: auto;

  scrollbar-width: none;
}

.loading-question {
  width: 100%;
}
</style>
