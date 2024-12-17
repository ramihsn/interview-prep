import AnswerCreate from './AnswerCreate'
import type { AnswerType } from '@/types'

export default class Answer extends AnswerCreate implements AnswerType {
  id: number

  constructor(id: number, question_id: number, data: AnswerType) {
    super(question_id, data)
    this.id = id
  }
}
