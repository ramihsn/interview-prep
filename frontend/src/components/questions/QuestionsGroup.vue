<script setup lang="ts">
import { computed, ref } from 'vue'
import { defineAsyncComponent } from 'vue'

import Question from '@/models/Question'

const props = defineProps({
  groupName: String,
  questions: {
    type: Array as () => Question[],
    required: true,
  },
})
defineEmits(['delete', 'questionStatusChange'])

const QuestionComponent = defineAsyncComponent(() => import('./QuestionComponent.vue'))
const showGroup = ref(true)
const questionsCount = computed(() => props.questions.length)
const questionsSolvedCount = computed(() => props.questions.filter((q) => q.answered).length)
</script>

<template>
  <div class="card">
    <div
      v-if="groupName !== undefined"
      class="card-title no-select flex"
      @click="showGroup = !showGroup"
    >
      <span>{{ groupName }}</span>
      <span class="grow">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="h-5 w-5 ml-2 transform transition-transform duration-200"
          viewBox="0 0 20 20"
          fill="currentColor"
          :class="{ '-rotate-90': !showGroup }"
        >
          <path
            fill-rule="evenodd"
            d="M5.23 7.21a.75.75 0 011.06 0L10 10.92l3.71-3.71a.75.75 0 111.06 1.06l-4 4a.75.75 0 01-1.06 0l-4-4a.75.75 0 010-1.06z"
            clip-rule="evenodd"
          />
        </svg>
      </span>
      <span v-if="groupName !== undefined" class="mr-7"
        >{{ questionsSolvedCount }}/{{ questionsCount }}</span
      >
    </div>
    <div
      class="transition-all duration-300 ease-in-out overflow-hidden card-body"
      :class="{ collapsed: !showGroup }"
    >
      <QuestionComponent
        class="mb-4"
        v-for="q in questions"
        :key="q.id"
        :question="q"
        @delete="$emit('delete', q.id)"
        @changeStatus="(status) => $emit('questionStatusChange', status)"
      />
    </div>
  </div>
</template>

<style scoped>
.collapsed {
  height: 0;
  padding-bottom: 0;
}
</style>
