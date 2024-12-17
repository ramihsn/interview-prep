import AnswerCreate from './AnswerCreate'
import type { AnswerType } from '@/types'

export default class Answer extends AnswerCreate implements AnswerType {
  id: number

  constructor(id: number, answer: string, review: string, rating: number, question_id: number) {
    super(answer, review, rating, question_id)
    this.id = id
  }
}
