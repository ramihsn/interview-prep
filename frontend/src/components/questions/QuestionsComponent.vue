<script lang="ts" setup>
import { onMounted, ref, computed } from 'vue'

import { fetchQuestions, deleteQuestion } from '@/api/questionsService'
import { useUserSettingsStore } from '@/stores/userSettings'
import { fetchPosition } from '@/api/positionService'
import ModuleComponent from '../ModuleComponent.vue'
import QuestionsAdder from './QuestionsAdder.vue'
import QuestionsGroup from './QuestionsGroup.vue'
import { GroupsEnum } from '@/enums/GroupsEnum'
import type { QuestionType } from '../../types'
import DropdownMenu from '../DropdownMenu.vue'
import { toTitleCase } from '@/helpers/string'

interface QuestionsGroup {
  idx: number
  groupName?: string
  questions: QuestionType[]
}

const userSettingsStore = useUserSettingsStore()
const addNewQuestion = ref(false)
const loading = ref<boolean>(true)
const hasFileUploadError = ref<string | null>(null)
const questions = ref<QuestionType[]>([])

onMounted(async () => {
  questions.value = await fetchQuestions()
  loading.value = false

  // get the position company and title if it's not already set
  if (userSettingsStore.selectedPosition === null) {
    console.log(`Fetching position at index ${userSettingsStore.positionIndex}`)
    fetchPosition(userSettingsStore.positionIndex ?? 0).then((fetchedPos) => {
      userSettingsStore.selectedPosition = fetchedPos
    })
  }
})

const groupedQuestions = computed<QuestionsGroup[]>(() => {
  if (userSettingsStore.groupBy === null || userSettingsStore.groupBy === GroupsEnum.none) {
    return [{ idx: 0, questions: questions.value }]
  }

  const grouped = questions.value.reduce((acc: QuestionsGroup[], question: QuestionType) => {
    const groupName: string = question[
      userSettingsStore.groupBy.toLowerCase() as keyof QuestionType
    ] as string
    const idx = acc.findIndex((group) => group.groupName === groupName)

    if (idx === -1) {
      acc.push({ idx: acc.length, groupName, questions: [question] })
    } else {
      acc[idx].questions.push(question)
    }

    return acc
  }, [] as QuestionsGroup[])
  return grouped
})

function onQuestionAdded(newQuestion: QuestionType) {
  questions.value.push(newQuestion)
  addNewQuestion.value = false
}

function onQuestionsAdded(newQuestions: QuestionType[]) {
  questions.value = [...questions.value, ...newQuestions]
  addNewQuestion.value = false
}

function onDelete(questionId: number) {
  deleteQuestion(questionId).then(() => {
    questions.value = questions.value.filter((q) => q.id !== questionId)
  })
}

function onFileUploadedError(error: string) {
  hasFileUploadError.value = error
  setTimeout(() => {
    hasFileUploadError.value = null
  }, 3000)
}
</script>

<template>
  <div class="custom-container relative">
    <div class="w-full text-center text-accent py-4">
      <span class="px-2">{{ toTitleCase(userSettingsStore.selectedPosition?.company || '') }}</span>
      <span class="px-2">|</span>
      <span class="px-2">{{ toTitleCase(userSettingsStore.selectedPosition?.title || '') }}</span>
    </div>

    <Teleport to=".question-module" v-if="addNewQuestion">
      <ModuleComponent @close="addNewQuestion = false">
        <QuestionsAdder
          :positionID="userSettingsStore.positionIndex ?? -1"
          @questionAdded="onQuestionAdded"
          @fileUploaded="onQuestionsAdded"
          @fileUploadedError="onFileUploadedError"
        />
      </ModuleComponent>
    </Teleport>

    <DropdownMenu class="dropdown-top-left" />

    <!-- Loading the questions from the backend, show demy questions -->
    <div v-if="loading" class="pt-4 max-w-7xl w-full mx-auto custom-container">
      <QuestionsGroup
        :questions="
          Array.from({ length: 4 }, (_, i) => ({
            id: i,
            topic: '...',
            difficulty: '...',
            question: 'Loading...',
          }))
        "
      />
    </div>

    <!-- The Questions -->
    <div v-else-if="questions.length > 0" class="pt-4 max-w-7xl w-full mx-auto custom-container">
      <QuestionsGroup
        v-for="group in groupedQuestions"
        :key="group.idx"
        :questions="group.questions"
        :groupName="group.groupName"
        @delete="onDelete"
      />
    </div>

    <!-- There is no questions to show -->
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
          :positionID="userSettingsStore.positionIndex ?? -1"
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

  height: 92vh;
  overflow-y: auto;

  scrollbar-width: none;
  position: relative; /* Ensure the parent is positioned relatively */
}

.loading-question {
  width: 100%;
}

.dropdown-top-left {
  position: absolute;
  top: 0;
  left: 0;
}
</style>
