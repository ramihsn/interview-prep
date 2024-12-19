<script lang="ts" setup>
import { onMounted, ref } from 'vue'
import type { QuestionType } from '../../types'

const props = defineProps<{ question: QuestionType }>()
const emit = defineEmits(['close', 'submit'])

// Variables
const topicInput = ref<HTMLInputElement | null>(null)
const topic = ref<string>(props.question.topic)
const difficulty = ref<string>(props.question.difficulty)
const question = ref<string>(props.question.question)

// Functions
function onSubmit() {
  if (!question.value) return
  if (
    topic.value === props.question.topic &&
    difficulty.value === props.question.difficulty &&
    question.value === props.question.question
  ) {
    return
  }
  emit('submit', {
    id: props.question.id,
    topic: topic.value,
    difficulty: difficulty.value,
    question: question.value,
  })
}

onMounted(() => {
  topicInput.value?.focus()
})
</script>
<template>
  <div class="card shadow-lg w-full max-w-lg mx-auto bg-base-300 p-6">
    <h2 class="text-2xl font-bold mb-6 text-center">Edit Question</h2>

    <form class="space-y-4">
      <!-- Topic Field -->
      <div>
        <label class="label">
          <span class="label-text font-bold">Topic</span>
        </label>
        <input
          ref="topicInput"
          type="text"
          v-model="topic"
          class="input input-bordered w-full"
          placeholder="Enter the topic"
        />
      </div>

      <!-- Difficulty Field -->
      <div>
        <label class="label">
          <span class="label-text font-bold">Difficulty</span>
        </label>
        <input
          type="text"
          v-model="difficulty"
          class="input input-bordered w-full"
          placeholder="Enter the difficulty"
        />
      </div>

      <!-- Question Field -->
      <div>
        <label class="label">
          <span class="label-text font-bold">Question</span>
        </label>
        <textarea
          v-model="question"
          class="input input-bordered w-full"
          placeholder="Enter the question"
        ></textarea>
      </div>
    </form>

    <div class="card-actions justify-end mt-6">
      <button class="btn btn-primary" @click="onSubmit">Submit</button>
      <button class="btn btn-error ml-2" @click="$emit('close')">Cancel</button>
    </div>
  </div>
</template>
