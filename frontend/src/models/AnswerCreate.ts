import type { AnswerCreateType } from '@/types'

export default class AnswerCreate implements AnswerCreateType {
  answer: string
  review: string
  rating: number
  question_id: number

  constructor(question_id: number, data?: Partial<AnswerCreateType>) {
    this.question_id = question_id
    this.answer = data?.answer || ''
    this.review = data?.review || ''
    this.rating = data?.rating || 0
  }
}
