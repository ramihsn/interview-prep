<script lang="ts" setup>
import { ref } from 'vue'

import FileUploader from '../FileUploader.vue'
import { createQuestion } from '@/api/questionsService'
import QuestionCreate from '@/models/QuestionCreate'

const emit = defineEmits(['questionAdded', 'fileUploaded', 'fileUploadedError'])
const props = defineProps({
  positionID: { type: Number, required: true },
  embedded: { type: Boolean, default: true },
})
const topic = ref('')
const difficulty = ref('')
const question = ref('')

const addQuestion = async () => {
  const q = new QuestionCreate(topic.value, difficulty.value, question.value, props.positionID)
  createQuestion(q).then((questionCreated) => {
    emit('questionAdded', questionCreated)
  })
}
</script>

<template>
  <h2 class="text-2xl font-bold">Add New Question</h2>
  <table class="border-spacing-4 border-separate">
    <tbody>
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
    </tbody>
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
      :positionID="positionID"
      @fileUploaded="(data) => $emit('fileUploaded', data)"
      @fileUploadError="(error) => $emit('fileUploadedError', error)"
    />
    <span class="h-0.5 w-10 bg-gray-300"></span>
    <FileUploader
      type="csv"
      icon="file-csv"
      color="#4bb25d"
      :positionID="positionID"
      @fileUploaded="(data) => $emit('fileUploaded', data)"
      @fileUploadError="(error) => $emit('fileUploadedError', error)"
    />
    <span class="h-0.5 w-10 bg-gray-300"></span>
    <FileUploader
      type="excel"
      icon="file-excel"
      color="#097640"
      :positionID="positionID"
      @fileUploaded="(data) => $emit('fileUploaded', data)"
      @fileUploadError="(error) => $emit('fileUploadedError', error)"
    />
  </div>
</template>
