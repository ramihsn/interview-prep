import { createRouter, createWebHistory } from 'vue-router'
import PositionsComponent from '@/components/positions/PositionsComponent.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: PositionsComponent,
    },
    {
      path: '/questions',
      name: 'questions',
      component: () => import('@/views/QuestionsView.vue'),
    },
    {
      path: '/job',
      name: 'job',
      component: () => import('@/views/JobView.vue'),
    },
  ],
})

export default router
