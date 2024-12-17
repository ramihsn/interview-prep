import AnswerCreate from '@/models/AnswerCreate'
import httpClient from './httpClient'
import Answer from '@/models/Answer'

export const fetchAnswers = async (): Promise<Answer[]> => {
  const response = await httpClient.get('/v1/answers')
  return response.data as Answer[]
}

export const fetchAnswer = async (id: string): Promise<Answer> => {
  const response = await httpClient.get(`/v1/answers/${id}`)
  return response.data as Answer
}

export const createAnswer = async (question: AnswerCreate): Promise<Answer> => {
  const response = await httpClient.post('/v1/answers', question)
  return response.data as Answer
}

export const updateAnswer = async (id: string, question: AnswerCreate): Promise<Answer> => {
  const response = await httpClient.put(`/v1/answers/${id}`, question)
  return response.data as Answer
}

export const deleteAnswer = async (id: number): Promise<void> => {
  await httpClient.delete(`/v1/answers/${id}`)
}
