import Answer from '@/models/Answer'
import type { QuestionType } from '@/types'
import QuestionCreate from './QuestionCreate'

export default class Question extends QuestionCreate implements QuestionType {
  id: number

  constructor(
    id: number,
    topic: string,
    difficulty: string,
    question: string,
    position_id: number,
    answered: boolean = false,
    answer: Answer | undefined | null = undefined,
  ) {
    super(topic, difficulty, question, position_id, answered, answer)
    this.id = id
  }
}
