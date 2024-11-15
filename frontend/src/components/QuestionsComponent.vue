<script lang="ts" setup>
import { onMounted, ref, defineAsyncComponent } from 'vue'
import type { QuestionType } from '../types'

const loading = ref<boolean>(true)
const questions = ref<QuestionType[]>([])

const Question = defineAsyncComponent(() => import('./QuestionComponent.vue'))

onMounted(async () => {
  const res = await fetch('http://127.0.0.1:6970/api/v1/questions', {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
    },
  })
  questions.value = await res.json()
  loading.value = false
})
</script>

<template>
  <div v-if="loading" class="pt-4 max-w-7xl w-full mx-auto container">
    <Question
      v-for="i in 3"
      :key="i"
      class="mb-4 animate-pulse loading-question"
      :question="{ id: i, topic: '...', difficulty: '...', question: 'Loading...' }"
    />
  </div>

  <div v-else class="pt-4 max-w-7xl w-full mx-auto container">
    <Question class="mb-4" v-for="q in questions" :key="q.id" :question="q" />
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
