<script lang="ts" setup>
import { ref, useTemplateRef } from 'vue'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

import { markQuestionAsAnswered, markQuestionAsUnanswered } from '@/api/questionsService'
import { createAnswer, updateAnswer } from '@/api/answersService'
import { deleteQuestion } from '@/api/questionsService'
import ModuleComponent from '../ModuleComponent.vue'
import AnswerComponent from '../AnswerComponent.vue'
import ConfirmDeletion from '../ConfirmDeletion.vue'
import QuestionEditor from './QuestionEditor.vue'
import AnswerCreate from '@/models/AnswerCreate'
import Question from '@/models/Question'
import Answer from '@/models/Answer'

const emit = defineEmits(['delete', 'changeStatus'])
const props = defineProps<{ question: Question }>()
const answer = ref<Answer | AnswerCreate>(
  props.question.answer || new AnswerCreate(props.question.id),
)
const markAsDone = ref(props.question.answered || false)
const isLoading = ref(false)
const editQuestion = ref(false)
const answerComponentRef = useTemplateRef<typeof AnswerComponent>('answerComponentRef')
const confirmDelete = ref(false)

/**
 * Toggles the mark as done state for a question.
 * Sets the loading state to true before making an API call to change the question state.
 *
 * @function toggleMarkAsDone
 */
function toggleMarkAsDone() {
  isLoading.value = true // Set loading to true before API call
  const func = markAsDone.value ? markQuestionAsUnanswered : markQuestionAsAnswered

  changeQuestionState(props.question.id, func)
}

/**
 * Changes the state of a question by calling the provided callback function.
 *
 * @async
 * @function changeQuestionState
 * @param {number} questionId - The ID of the question to change the state for.
 * @param {function} stateChangeFunction - The callback function to call for changing the question state.
 * @returns {Promise<void>}
 * @throws Will log an error message if the callback function throws an error.
 */
async function changeQuestionState(
  questionId: number,
  stateChangeFunction: (questionId: number) => Promise<void>,
) {
  try {
    await stateChangeFunction(questionId)
    emit('changeStatus', { questionID: props.question.id, isAnswered: markAsDone.value })
  } catch (err) {
    console.error('Error:', err)
    markAsDone.value = !markAsDone.value
  } finally {
    isLoading.value = false // Reset loading after API call
  }
}

function onSubmitChanges(newQuestion: Question) {
  editQuestion.value = false
  console.log('New Question:', newQuestion)
  // TODO: see what to do next with the new question
  // update the backend with the new question
  // update the question values in the list of questions
}

function onAnswerSubmit(answer: Answer | AnswerCreate) {
  if (answer !== props.question.answer) {
    if (props.question.answer) {
      console.log('Previous Answer:', props.question.answer)
      console.log('New Answer:', answer)
      updateAnswer(props.question.answer.id, answer)
        .then((data) => {
          console.log('Success:', data)
        })
        .catch((err) => {
          console.error('Error:', err)
        })
    } else {
      createAnswer(answer)
        .then((data) => {
          console.log('Success:', data)
        })
        .catch((err) => {
          console.error('Error:', err)
        })
    }
  }
}

function handleSubmit() {
  if (answerComponentRef.value) {
    answerComponentRef.value.emitAnswer()
  }
}
</script>

<template>
  <div
    class="card bg-primary text-primary-content shadow custom relative mb-10 pb-2"
    :id="`question-${question.id}`"
  >
    <Teleport to=".question-module" v-if="editQuestion">
      <ModuleComponent @close="editQuestion = false">
        <QuestionEditor
          :question="question"
          @close="editQuestion = false"
          @submit="onSubmitChanges"
        />
      </ModuleComponent>
    </Teleport>

    <Teleport to=".question-module" v-if="confirmDelete">
      <ModuleComponent @close="confirmDelete = false">
        <div class="flex items-center justify-center">
          <ConfirmDeletion
            :itemID="question.id"
            :deleteFunction="deleteQuestion"
            @close="confirmDelete = false"
            @confirm="$emit('delete', question.id)"
          >
            <span>Are you sure you want to delete the question?</span>
            <div>
              <strong class="text-primary">{{ question.topic }}</strong>
              with difficulty level
              <strong class="text-primary">{{ question.difficulty }}</strong>
            </div>
            <br class="my-1" />
            <div>
              {{ question.question }}
            </div>
          </ConfirmDeletion>
        </div>
      </ModuleComponent>
    </Teleport>

    <div v-if="!markAsDone" class="absolute bottom-2 right-2 mb-5 mr-3 cursor-pointer">
      <button class="btn btn-primary pr-5" @click="handleSubmit">Submit</button>
      <FontAwesomeIcon
        size="xl"
        icon="pen-to-square"
        class="mr-5 hover:text-red-500"
        @click="editQuestion = true"
      />
      <FontAwesomeIcon
        size="xl"
        icon="trash-can"
        class="mr-3 hover:text-red-500"
        @click="confirmDelete = true"
      />
    </div>

    <div class="card-body">
      <h2 class="card-title flex">
        <strong class="grow" :class="{ done: markAsDone }">
          <span>Topic: </span>
          <span>{{ question.topic }}</span>
        </strong>
        <div v-if="markAsDone">{{ answer.rating }} / 10</div>
      </h2>
      <div :hidden="markAsDone" class="mt-3">
        <p class="pb-3">
          <strong>Difficulty Level: {{ question.difficulty }}</strong>
        </p>
        <p class="pb-3">
          <strong>Question</strong>
          <span class="ml-1">:</span>
          <br />
          <span>{{ question.question }}</span>
        </p>
        <hr class="pb-3" />
        <h2>Answer:</h2>
        <AnswerComponent
          ref="answerComponentRef"
          :answer="answer"
          :question_id="question.id"
          @submitAnswer="onAnswerSubmit"
        />
      </div>
    </div>

    <div class="card-actions pl-3">
      <label class="btn btn-ghost">
        <input
          type="checkbox"
          @click="toggleMarkAsDone"
          v-model="markAsDone"
          :disabled="isLoading"
        />
        <span>Mark as Done</span>
      </label>
    </div>

    <!-- Loading Spinner Overlay -->
    <div
      v-if="isLoading"
      class="absolute inset-0 flex items-center justify-center bg-black bg-opacity-50"
    >
      <div class="spinner-border animate-spin inline-block w-8 h-8 border-4 rounded-full"></div>
    </div>
  </div>
</template>

<style scoped>
.custom {
  border-radius: 30px;
}

.done {
  text-decoration: line-through;
}

.spinner-border {
  border-color: white transparent transparent transparent;
}
</style>
