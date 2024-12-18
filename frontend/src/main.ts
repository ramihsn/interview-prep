import '@/assets/tailwind.css'
import '@/assets/main.css'
import '../vite-env.d.ts'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'

// /* import the fontawesome core library */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { library } from '@fortawesome/fontawesome-svg-core'
import {
  faPlus,
  faFileCsv,
  faFileCode,
  faTrashCan,
  faFileExcel,
  faPenToSquare,
  faCircleExclamation,
  faXmark,
} from '@fortawesome/free-solid-svg-icons'

// /* add icons to the library */
library.add([
  faPlus,
  faXmark,
  faFileCsv,
  faFileCode,
  faFileExcel,
  faTrashCan,
  faPenToSquare,
  faCircleExclamation,
])

const pinia = createPinia()
createApp(App).use(pinia).component('font-awesome-icon', FontAwesomeIcon).use(router).mount('#app')
