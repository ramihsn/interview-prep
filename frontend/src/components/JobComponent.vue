<script setup lang="ts">
import { onMounted, ref } from 'vue'
import MarkdownIt from 'markdown-it'

import { fetchPosition } from '@/api/positionService'
import { useUserSettingsStore } from '@/stores/userSettings'

const userSettingsStore = useUserSettingsStore()
const md = MarkdownIt({
  html: true,
  linkify: true,
  typographer: true,
})

const position = ref(
  userSettingsStore.selectedPosition ?? {
    company: 'Company Name',
    title: 'Job Title',
    description: 'Job Description',
  },
)
const positionDescription = ref(position.value.description)

onMounted(() => {
  positionDescription.value = md.render(position.value.description)
  if (userSettingsStore.selectedPosition === null) {
    console.log(`Fetching position at index ${userSettingsStore.positionIndex}`)
    fetchPosition(userSettingsStore.positionIndex ?? 0).then((fetchedPos) => {
      userSettingsStore.selectedPosition = fetchedPos
      position.value = fetchedPos
      positionDescription.value = md.render(fetchedPos.description)
    })
  }
})
</script>

<template>
  <div class="min-h-screen flex items-center justify-center p-6 bg-primary w-full">
    <div class="w-2/3">
      <div class="bg-secondary text-secondary-content py-6 rounded-t-lg">
        <h2 class="text-2xl font-bold text-center">{{ position.company }}</h2>
      </div>

      <div class="p-6">
        <h3 class="text-xl font-semibold text-secondary-content text-center mb-6">
          {{ position.title }}
        </h3>

        <div v-html="positionDescription" class="prose max-w-none text-secondary-content"></div>
      </div>
    </div>
  </div>
</template>
