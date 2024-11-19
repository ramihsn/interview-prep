<script lang="ts" setup>
import { ref, defineEmits } from 'vue'

import FileUploader from './FileUploader.vue'
import type { QuestionType } from '../types'

const emit = defineEmits(['questionAdded', 'fileUploaded'])
defineProps({ embedded: { type: Boolean, default: true } })
const baseURL = import.meta.env.VITE_BASE_URL
const topic = ref('')
const difficulty = ref('')
const question = ref('')

const addQuestion = async () => {
  const headers = { 'Content-Type': 'application/json' }
  const requestParams = {
    method: 'POST',
    headers,
    body: JSON.stringify({
      topic: topic.value,
      difficulty: difficulty.value,
      question: question.value,
    }),
  }

  const res = await fetch(`${baseURL}/api/v1/questions`, requestParams)
  if (!res.ok) {
    throw new Error('Network response was not ok')
  }

  const questionCreated: QuestionType = await res.json()
  emit('questionAdded', questionCreated)
}
</script>

<template>
  <h2 class="text-2xl font-bold">Add New Question</h2>
  <table class="border-spacing-4 border-separate">
    <tr>
      <th>
        <label class="text-nowrap">Question Topic</label>
      </th>
      <td class="w-full">
        <input
          type="text"
          class="input w-full"
          v-model="topic"
          placeholder="Enter Question Topic"
        />
      </td>
    </tr>
    <tr>
      <th>
        <label class="text-nowrap">Difficulty Level</label>
      </th>
      <td class="w-full">
        <input
          type="text"
          class="input w-full"
          v-model="difficulty"
          placeholder="Enter Difficulty Level"
        />
      </td>
    </tr>
    <tr>
      <th>
        <div class="text-nowrap">Question</div>
      </th>
      <td class="w-full">
        <textarea
          class="textarea h-30 w-full rounded-lg"
          placeholder="Type your question here..."
          v-model="question"
          rows="3"
        ></textarea>
      </td>
    </tr>
  </table>

  <div class="flex justify-end mt-2 mr-4">
    <button
      class="btn"
      :class="{ 'btn-primary': embedded, 'btn-secondary': !embedded }"
      @click="addQuestion"
    >
      Add Question
    </button>
  </div>

  <div class="flex items-center my-4">
    <div class="flex-grow border-t border-gray-300"></div>
    <span class="mx-4 text-gray-500">OR</span>
    <div class="flex-grow border-t border-gray-300"></div>
  </div>

  <div class="flex items-center justify-center">
    <p class="text-center text-xl font-bold">Upload file of on of the following type:</p>
  </div>
  <div class="flex justify-evenly items-center w-full">
    <FileUploader
      type="json"
      icon="file-code"
      color="#9a7bab"
      @fileUploaded="(data) => $emit('fileUploaded', data)"
    />
    <span class="h-0.5 w-10 bg-gray-300"></span>
    <FileUploader
      type="csv"
      icon="file-csv"
      color="#4bb25d"
      @fileUploaded="(data) => $emit('fileUploaded', data)"
    />
    <span class="h-0.5 w-10 bg-gray-300"></span>
    <FileUploader
      type="excel"
      icon="file-excel"
      color="#097640"
      @fileUploaded="(data) => $emit('fileUploaded', data)"
    />
  </div>
</template>
