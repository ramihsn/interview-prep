import httpClient from './httpClient'
import Position from '@/models/Position'
import PositionCreate from '@/models/PositionCreate'

export const fetchPositions = async (): Promise<Position[]> => {
  const response = await httpClient.get('/v1/positions')
  return response.data as Position[]
}

export const createPosition = async (position: PositionCreate): Promise<Position> => {
  const response = await httpClient.post('/v1/positions', position)
  return response.data as Position
}

export const deletePosition = async (id: number): Promise<void> => {
  await httpClient.delete(`/v1/positions/${id}`)
}
