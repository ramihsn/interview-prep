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
  <div class="modal-box w-full max-w-5xl">
    <h3 class="text-lg font-bold text-info">Add New Question</h3>

    <!-- Inputs -->
    <p class="py-4">
      <table class="border-spacing-4 border-separate">
        <tbody>
          <tr>
            <th>
              <label class="text-nowrap">Question Topic</label>
            </th>
            <td class="w-full">
              <input
                type="text"
                class="input input-bordered input-primary w-full"
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
                class="input input-bordered input-primary w-full"
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
                class="textarea textarea-primary w-full"
                placeholder="Type your question here..."
                v-model="question"
                rows="3"
              ></textarea>
            </td>
          </tr>
        </tbody>
      </table>
    </p>

    <!-- Submit Button -->
    <div class="modal-action flex justify-end space-x-4">
      <button
        class="btn"
        :class="{ 'btn-primary': embedded, 'btn-secondary': !embedded }"
        @click="addQuestion"
      >
        Add Question
      </button>
    </div>

    <!-- Bottom Section -->
    <div class="modal-action flex flex-col justify-center space-x-4">
      <!-- Divider -->
      <div class="flex items-center my-4 w-full">
        <div class="flex-grow border-t border-gray-300"></div>
        <span class="mx-4 text-gray-500">OR</span>
        <div class="flex-grow border-t border-gray-300"></div>
      </div>

      <!-- Some info -->
      <div class="flex items-center justify-center">
        <p class="text-center text-xl font-bold">Upload file of on of the following type:</p>
      </div>

      <!-- The Files Inputs components -->
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
    </div>
  </div>
</template>
