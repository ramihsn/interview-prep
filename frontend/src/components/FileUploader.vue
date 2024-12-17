<script lang="ts" setup>
import { ref, useTemplateRef, computed } from 'vue'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

import { uploadFile } from '@/api/questionsService'

const props = defineProps(['positionID', 'type', 'icon', 'color'])
const emit = defineEmits(['fileUploaded', 'fileUploadError'])
const accept = computed(() => {
  switch (props.type) {
    case 'json':
      return 'application/json'
    case 'csv':
      return 'text/csv'
    case 'excel':
      return 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    default:
      return '*/*'
  }
})
const inputRef = useTemplateRef<HTMLInputElement>('fileInput')
const file = ref<File | null>()
const isLoading = ref(false)

function onFileChanged($event: Event) {
  const target = $event.target as HTMLInputElement
  if (target && target.files) {
    file.value = target.files[0]

    if (file.value) {
      // Show loading spinner
      isLoading.value = true

      uploadFile(props.positionID, file.value, props.type)
        .then((data) => {
          emit('fileUploaded', data)
        })
        .catch((err) => {
          console.log('Upload failed:', err)
        })
        .finally(() => {
          // Hide loading spinner
          isLoading.value = false
        })
    }
  }
}

function triggerFileUpload() {
  inputRef.value?.click()
}
</script>

<template>
  <div class="flex flex-col pt-5 cursor-pointer" @click="triggerFileUpload">
    <FontAwesomeIcon :icon="icon" size="2xl" :style="[{ color }]" />
    <span class="text-center">{{ type }}</span>
    <input
      type="file"
      ref="fileInput"
      @change="onFileChanged($event)"
      style="display: none"
      :accept="accept"
    />
  </div>

  <!-- Loading Spinner -->
  <div
    v-if="isLoading"
    class="fixed inset-0 flex items-center justify-center bg-gray-800 bg-opacity-75 z-50"
  >
    <div class="w-16 h-16 border-4 border-dashed rounded-full animate-spin border-white"></div>
  </div>
</template>
