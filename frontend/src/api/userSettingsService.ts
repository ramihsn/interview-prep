import httpClient from './httpClient'
import UserSettings from '@/models/UserSettings'

export const fetchUserSettings = async (): Promise<UserSettings> => {
  const response = await httpClient.get('/v1/users/settings')
  return response.data as UserSettings
}

export const updateUserTheme = async (theme: string): Promise<UserSettings> => {
  const response = await httpClient.put('/v1/users/settings/theme', null, {
    params: { theme },
    headers: { 'Content-Type': 'application/json' },
  })
  return response.data as UserSettings
}

export const updateUserGroupBy = async (groupBy: string): Promise<UserSettings> => {
  const response = await httpClient.put('/v1/users/settings/group_by', null, {
    params: { group_by: groupBy },
    headers: { 'Content-Type': 'application/json' },
  })
  return response.data as UserSettings
}

export const updateUserPosition = async (positionId: number | null): Promise<UserSettings> => {
  const response = await httpClient.put('/v1/users/settings/position', null, {
    params: { position_id: positionId },
    headers: { 'Content-Type': 'application/json' },
  })
  return response.data as UserSettings
}
