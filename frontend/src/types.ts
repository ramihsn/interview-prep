export interface QuestionType {
  id: number
  topic: string
  difficulty: string
  question: string

  answer?: AnswerType
}

export interface AnswerType {
  id?: number | null
  answer: string
  review: string
  rating: number

  question_id?: number
  question?: QuestionType
}

export interface PositionType {
  id?: number | null
  company: string
  title: string
  description: string
}
