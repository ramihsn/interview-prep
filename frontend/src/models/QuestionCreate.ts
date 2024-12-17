import type { QuestionCreateType, AnswerType } from '@/types'

export default class QuestionCreate implements QuestionCreateType {
  topic: string
  difficulty: string
  question: string
  position_id: number

  answered?: boolean = false
  answer?: AnswerType | null = undefined

  constructor(
    topic: string,
    difficulty: string,
    question: string,
    position_id: number,
    answered: boolean = false,
    answer?: AnswerType | null,
  ) {
    this.topic = topic
    this.difficulty = difficulty
    this.question = question
    this.position_id = position_id
    this.answered = answered
    this.answer = answer
  }
}
