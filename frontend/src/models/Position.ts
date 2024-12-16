import type { PositionType } from '@/types'

export default class Position implements PositionType {
  id: number
  company: string
  title: string
  description: string

  constructor(id: number, company: string, title: string, description: string) {
    this.id = id
    this.company = company
    this.title = title
    this.description = description
  }
}
