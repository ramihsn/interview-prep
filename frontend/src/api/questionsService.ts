import httpClient from './httpClient'
import Question from '@/models/Question'
import QuestionCreate from '@/models/QuestionCreate'

export const fetchQuestions = async (positionID: number): Promise<Question[]> => {
  const response = await httpClient.get(`v1/questions/position/${positionID}`)
  return response.data as Question[]
}

export const fetchQuestion = async (id: string): Promise<Question> => {
  const response = await httpClient.get(`/v1/questions/${id}`)
  return response.data as Question
}

export const createQuestion = async (question: QuestionCreate): Promise<Question> => {
  const response = await httpClient.post('/v1/questions', question)
  return response.data as Question
}

export const updateQuestion = async (id: string, question: QuestionCreate): Promise<Question> => {
  const response = await httpClient.put(`/v1/questions/${id}`, question)
  return response.data as Question
}

export const deleteQuestion = async (id: number): Promise<void> => {
  await httpClient.delete(`/v1/questions/${id}`)
}

export const markQuestionAsAnswered = async (id: number): Promise<void> => {
  await httpClient.post(`/v1/questions/${id}/mark-as-answered`)
}

export const markQuestionAsUnanswered = async (id: number): Promise<void> => {
  await httpClient.post(`/v1/questions/${id}/mark-as-unanswered`)
}

export const uploadFile = async (
  positionID: number,
  file: File,
  file_type: string,
): Promise<string> => {
  const formData = new FormData()
  formData.append('file', file)
  formData.append('file_type', file_type)

  const response = await httpClient.post(`v1/questions/upload-file`, formData, {
    headers: {
      Accept: 'application/json',
      'Content-Type': 'multipart/form-data',
    },
    params: {
      position_id: positionID,
      file_type,
    },
  })
  return response.data as string
}

export const countPositionQuestions = async (positionID: number): Promise<number> => {
  const response = await httpClient.get(`/v1/questions/position/${positionID}/count`)
  return response.data as number
}
