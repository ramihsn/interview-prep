import { defineStore } from 'pinia'

import { GroupsEnum } from '@/enums/GroupsEnum'
import { Theme, getTheme, isDarkTheme, toggleTheme } from '@/themes'

const baseURL = import.meta.env.VITE_BASE_URL

async function getUserSettings() {
  const response = await fetch(`${baseURL}/api/v1/users/settings`)
  if (!response.ok) {
    console.error(await response.json())
    throw new Error('An error occurred while fetching the user settings')
  }
  const data: { theme?: string; questions_group_by?: string } = await response.json()

  return data
}

async function updateUserTheme(theme: string) {
  const url = `${baseURL}/api/v1/users/settings/theme?theme=${theme}`
  const requestParams = {
    method: 'PUT',
    headers: {
      Accept: 'application/json',
      'Content-Type': 'application/json',
    },
  }

  const response = await fetch(url, requestParams)
  if (!response.ok) {
    console.error(await response.json())
    throw new Error('An error occurred while updating the theme')
  }
  const data = await response.json()

  return data
}

async function updateUserGroupBy(groupBy: GroupsEnum) {
  const url = `${baseURL}/api/v1/users/settings/group_by?group_by=${groupBy}`
  const requestParams = {
    method: 'PUT',
    headers: {
      Accept: 'application/json',
      'Content-Type': 'application/json',
    },
  }

  const response = await fetch(url, requestParams)
  if (!response.ok) {
    console.error(await response.json())
    throw new Error('An error occurred while updating the group by')
  }
  const data = await response.json()

  return data
}

export const useUserSettingsStore = defineStore('userSettings', {
  state: () => ({
    theme: Theme.DARK as string,
    groupBy: GroupsEnum.none,
    _positionIndex: 0 as number | null,
  }),
  actions: {
    setTheme(theme: string) {
      updateUserTheme(theme).then(() => {
        this.theme = theme
      })
    },
    setGroupBy(groupBy: GroupsEnum) {
      updateUserGroupBy(groupBy).then(() => {
        this.groupBy = groupBy
      })
    },
    async fetchUserSettings() {
      getUserSettings().then((data) => {
        this.theme = getTheme(data.theme)
        this.groupBy = data.questions_group_by as GroupsEnum
        this._positionIndex = 0 // TODO: get the position index from the database
      })
    },
    toggleTheme() {
      const newTheme = toggleTheme(this.theme)
      this.setTheme(newTheme)
    },
    setPositionIndex(index: number | null) {
      this._positionIndex = index
      // TODO: save the position index in the database
    },
  },
  getters: {
    isDarkTheme: (state) => isDarkTheme(state.theme),
    positionIndex: (state) => state._positionIndex,
  },
})
