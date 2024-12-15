import httpClient from './httpClient'
import type { PositionType } from '@/types'

export const fetchPositions = async (): Promise<PositionType[]> => {
  const response = await httpClient.get('/v1/positions')
  return response.data
}

export const createPosition = async (position: PositionType): Promise<PositionType> => {
  const response = await httpClient.post('/v1/positions', position)
  return response.data
}

export const deletePosition = async (id: number): Promise<void> => {
  await httpClient.delete(`/v1/positions/${id}`)
}
