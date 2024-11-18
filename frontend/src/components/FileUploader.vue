<script lang="ts" setup>
import { ref, defineProps, useTemplateRef, computed } from 'vue'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

const props = defineProps(['type', 'icon', 'color'])
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

function onFileChanged($event: Event) {
  const target = $event.target as HTMLInputElement
  if (target && target.files) {
    file.value = target.files[0]
    // TODO: send to the backend for processing
  }
}

function triggerFileUpload() {
  inputRef.value?.click()
}
</script>

<template>
  <div class="flex flex-col pt-5 cursor-pointer" @click="triggerFileUpload">
    <FontAwesomeIcon class="" :icon="icon" size="2xl" :style="[{ color }]" />
    <span class="text-center">{{ type }}</span>
    <input
      type="file"
      ref="fileInput"
      @change="onFileChanged($event)"
      style="display: none"
      :accept="accept"
    />
  </div>
</template>
