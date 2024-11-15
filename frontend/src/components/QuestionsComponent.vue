<script lang="ts" setup>
import { onMounted, ref, defineAsyncComponent } from 'vue'

import ModuleComponent from './ModuleComponent.vue'
import QuestionsAdder from './QuestionsAdder.vue'
import type { QuestionType } from '../types'

const baseURL = import.meta.env.VITE_BASE_URL
const addNewQuestion = ref(false)
const loading = ref<boolean>(true)
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
function onQuestionsAdded() {}
</script>

<template>
  <Teleport to=".question-adder" v-if="addNewQuestion">
    <ModuleComponent @close="addNewQuestion = false">
      <QuestionsAdder @questionAdded="onQuestionAdded" @fileUploaded="onQuestionsAdded" />
    </ModuleComponent>
  </Teleport>

  <div v-if="loading" class="pt-4 max-w-7xl w-full mx-auto container">
    <Question
      v-for="i in 3"
      :key="i"
      class="mb-4 animate-pulse loading-question"
      :question="{ id: i, topic: '...', difficulty: '...', question: 'Loading...' }"
    />
  </div>

  <div v-else-if="questions.length > 0" class="pt-4 max-w-7xl w-full mx-auto container">
    <Question class="mb-4" v-for="q in questions" :key="q.id" :question="q" />
  </div>

  <div v-else>
    <div class="wrapper bg-primary text-primary-content">
      <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 p-4 rounded">
        <div role="alert" class="alert">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            class="stroke-info h-6 w-6 shrink-0"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
            ></path>
          </svg>
          <span class="text-primary-content">
            It's lonely here. Add questions to get started.
          </span>
        </div>
      </div>
    </div>
  </div>

  <div class="fixed bottom-4 right-4">
    <button @click="addNewQuestion = true" class="btn btn-circle btn-primary text-4xl pb-2">
      +
    </button>
  </div>
</template>

<style scoped>
.container {
  background-color: var(--bg-base-500);
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
