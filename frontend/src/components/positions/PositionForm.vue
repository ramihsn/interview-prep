<script setup lang="ts">
import { ref } from 'vue'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

const emit = defineEmits(['addPosition', 'close'])
defineProps({ inModule: { type: Boolean, required: false, default: false } })

// Variables
const company = ref('')
const title = ref('')
const description = ref('')
const hasError = ref(false)

// Functions
function addPosition() {
  if (!company.value || !title.value || !description.value) {
    hasError.value = true
    setTimeout(() => {
      hasError.value = false
    }, 5000)
    return
  }
  emit('addPosition', {
    company: company.value,
    title: title.value,
    description: description.value,
  })
  company.value = ''
  title.value = ''
  description.value = ''
}
</script>

<template>
  <div class="card bg-base-300 shadow-xl">
    <div
      v-if="inModule"
      class="absolute top-4 left-5 bg-red-500 text-white py-2 px-3 rounded-full cursor-pointer hover:bg-red-700"
    >
      <FontAwesomeIcon icon="xmark" size="xl" @click="$emit('close')" />
    </div>

    <div class="card-body">
      <div class="card-title justify-center mb-5">
        <h1>Add New Position</h1>
      </div>

      <table class="table w-full">
        <tr>
          <th class="flex max-w-max pr-4">
            <label for="title">Company</label>
          </th>
          <td>
            <input
              class="input input-bordered input-primary w-full"
              :class="{ 'border-2 border-rose-500': hasError && !company }"
              type="text"
              v-model="company"
            />
          </td>
        </tr>
        <tr>
          <th class="flex max-w-max pr-4">
            <label for="title">Title</label>
          </th>
          <td>
            <input
              class="input input-bordered input-primary w-full"
              :class="{ 'border-2 border-rose-500': hasError && !title }"
              type="text"
              v-model="title"
            />
          </td>
        </tr>
        <tr>
          <th class="flex max-w-max pr-4">
            <label for="description">Description</label>
          </th>
          <td>
            <textarea
              class="textarea textarea-primary w-full"
              :class="{ 'border-2 border-rose-500': hasError && !description }"
              rows="5"
              v-model="description"
            ></textarea>
          </td>
        </tr>
      </table>

      <div class="card-actions justify-end mt-3">
        <button
          :class="{ 'btn-primary': !hasError, 'btn-error': hasError }"
          @click="addPosition"
          class="btn rounded-lg"
        >
          Add Position
        </button>
      </div>

      <transition name="fade" appear>
        <div class="bg-warning border-2 border-rose-500 rounded-lg flex flex-row" v-if="hasError">
          <span class="mx-2">
            <FontAwesomeIcon icon="circle-exclamation" style="color: #e42807" />
          </span>
          <strong>All fields must be filled before adding the position</strong>
        </div>
      </transition>
    </div>
  </div>
</template>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
