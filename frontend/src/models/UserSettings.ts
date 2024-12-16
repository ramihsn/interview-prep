import type { UserSettingsType } from '@/types'

export default class UserSettings implements UserSettingsType {
  id: number
  theme: string
  questions_group_by: string
  selected_position_id: number | null

  constructor(
    id: number,
    theme: string,
    questions_group_by: string,
    selected_position_id: number | null,
  ) {
    this.id = id
    this.theme = theme
    this.questions_group_by = questions_group_by
    this.selected_position_id = selected_position_id
  }
}
