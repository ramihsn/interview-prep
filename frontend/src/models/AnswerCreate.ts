import type { AnswerCreateType } from '@/types'

export default class AnswerCreate implements AnswerCreateType {
  answer: string
  review: string
  rating: number
  question_id: number

  constructor(answer: string, review: string, rating: number, question_id: number) {
    this.answer = answer
    this.review = review
    this.rating = rating
    this.question_id = question_id
  }
}
