import type { QuestionCreateType } from '@/types'
import Answer from '@/models/Answer'

export default class QuestionCreate implements QuestionCreateType {
  topic: string
  difficulty: string
  question: string
  position_id: number

  answered?: boolean = false
  answer: Answer | undefined | null = undefined

  constructor(
    topic: string,
    difficulty: string,
    question: string,
    position_id: number,
    answered: boolean = false,
    answer: Answer | undefined | null = undefined,
  ) {
    this.topic = topic
    this.difficulty = difficulty
    this.question = question
    this.position_id = position_id
    this.answered = answered
    this.answer = answer
  }
}
