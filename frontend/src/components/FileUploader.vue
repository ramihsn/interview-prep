<script lang="ts" setup>
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

defineProps(['type', 'icon', 'color'])
</script>

<template>
  <div class="flex flex-col pt-5 cursor-pointer">
    <FontAwesomeIcon class="" :icon="icon" size="2xl" :style="[{ color }]" />
    <span class="text-center">{{ type }}</span>
  </div>
</template>
