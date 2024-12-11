<script lang="ts" setup>
import { ref } from 'vue'

import PositionForm from './positions/PositionForm.vue'
import PositionComponent from './positions/PositionComponent.vue'

// const positions = ref([])  // TODO: fetch positions
const cnt = ref(2)
</script>

<template>
  <div class="flex flex-col items-center justify-center pt-5 h-full">
    <div
      v-for="(pos, i) in Array.from({ length: cnt }, (_, i) => ({ koko: 'koko' }))"
      :key="i"
      :pos="pos"
    >
      <PositionComponent :pos="pos" />
      <hr class="my-5" />
    </div>

    <PositionForm class="mt-3 mb-12 w-2/3" />

    <div class="fixed bottom-6 right-10 flex space-x-4">
      <button
        @click="cnt++"
        class="w-14 h-14 rounded-full bg-orange-200 text-4xl font-bold leading-none"
      >
        +
      </button>
      <button
        @click="cnt--"
        class="w-14 h-14 rounded-full bg-orange-200 text-4xl font-bold leading-none"
      >
        -
      </button>
    </div>
  </div>
</template>
