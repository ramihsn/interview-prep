export interface QuestionType {
  id: number
  topic: string
  difficulty: string
  question: string

  answer?: AnswerType
}

export interface AnswerType {
  id: number
  answer: string
  review: string
  rating: number

  question_id: number
  question: QuestionType
}
