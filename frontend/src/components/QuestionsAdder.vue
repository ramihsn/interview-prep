<script lang="ts" setup>
import { ref, defineEmits } from 'vue'

import FileUploader from './FileUploader.vue'

defineEmits(['close'])

const question = ref('')
</script>

<template>
  <textarea
    class="textarea h-30 w-full rounded-lg"
    placeholder="Type your question here..."
    v-model="question"
    rows="3"
  ></textarea>

  <button class="btn btn-primary mt-2" @click="$emit('close', question)">Add Question</button>

  <div class="flex">
    <div class="flex items-center justify-center">
      <p class="text-center text-xl font-bold">Or upload file</p>
    </div>
    <span class="mx-4 mt-4 border-2 border-lightgray"></span>
    <FileUploader type="json" icon="file-code" color="#9a7bab" />
    <span class="mx-4 mt-4 border-2 border-lightgray"></span>
    <FileUploader type="csv" icon="file-csv" color="#4bb25d" />
    <span class="mx-4 mt-4 border-2 border-lightgray"></span>
    <FileUploader type="excel" icon="file-excel" color="#097640" />
    <span class="mx-4 mt-4 border-2 border-lightgray"></span>
  </div>
</template>
