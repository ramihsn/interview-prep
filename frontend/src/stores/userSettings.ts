import { defineStore } from 'pinia'

import Position from '@/models/Position'
import { GroupsEnum } from '@/enums/GroupsEnum'
import { Theme, getTheme, isDarkTheme, toggleTheme } from '@/themes'
import {
  fetchUserSettings,
  updateUserGroupBy,
  updateUserTheme,
  updateUserPosition,
} from '@/api/userSettingsService'

export const useUserSettingsStore = defineStore('userSettings', {
  state: () => ({
    theme: Theme.DARK as string,
    groupBy: GroupsEnum.none,
    _positionIndex: 0 as number | null,
    selectedPosition: null as Position | null,
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
      const userSettings = await fetchUserSettings()
      this.theme = getTheme(userSettings.theme)
      this.groupBy = userSettings.questions_group_by as GroupsEnum
      this._positionIndex = userSettings.selected_position_id
    },
    toggleTheme() {
      const newTheme = toggleTheme(this.theme)
      this.setTheme(newTheme)
    },
    setPositionIndex(index: number | null) {
      updateUserPosition(index)
        .then((newUserSettings) => {
          this._positionIndex = newUserSettings.selected_position_id
        })
        .catch((error) => {
          console.error(error)
        })
    },
    toString() {
      return JSON.stringify(
        {
          theme: this.theme,
          groupBy: this.groupBy,
          positionIndex: this._positionIndex,
        },
        null,
        2,
      )
    },
  },
  getters: {
    isDarkTheme: (state) => isDarkTheme(state.theme),
    positionIndex: (state) => state._positionIndex,
  },
})
