export interface QuestionCreateType {
  topic: string
  difficulty: string
  question: string
  answered?: boolean

  position_id: number

  answer?: AnswerType | null
}
export interface QuestionType extends QuestionCreateType {
  id: number
}

export interface AnswerCreateType {
  answer: string
  review: string
  rating: number

  question_id: number
  question?: QuestionType
}

export interface AnswerType extends AnswerCreateType {
  id: number
}

export interface PositionCreateType {
  company: string
  title: string
  description: string
}

export interface PositionType extends PositionCreateType {
  id: number
}

export interface UserSettingsType {
  id: number
  theme: string
  questions_group_by: string
  selected_position_id: number | null
}
