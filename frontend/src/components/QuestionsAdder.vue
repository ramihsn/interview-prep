<script lang="ts" setup>
import { ref, defineEmits } from 'vue'

import FileUploader from './FileUploader.vue'

defineEmits(['close'])

const question = ref('')
</script>

<template>
  <h2 class="text-2xl font-bold">Add New Question</h2>
  <table class="border-spacing-4 border-separate">
    <tr>
      <th>
        <label class="text-nowrap">Question Topic</label>
      </th>
      <td class="w-full">
        <input type="text" class="input w-full" placeholder="Enter Question Topic" />
      </td>
    </tr>
    <tr>
      <th>
        <label class="text-nowrap">Difficulty Level</label>
      </th>
      <td class="w-full">
        <input type="text" class="input w-full" placeholder="Enter Difficulty Level" />
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
    <button class="btn btn-primary" @click="$emit('close', question)">Add Question</button>
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
    <FileUploader type="json" icon="file-code" color="#9a7bab" />
    <span class="h-0.5 w-10 bg-gray-300"></span>
    <FileUploader type="csv" icon="file-csv" color="#4bb25d" />
    <span class="h-0.5 w-10 bg-gray-300"></span>
    <FileUploader type="excel" icon="file-excel" color="#097640" />
  </div>
</template>
