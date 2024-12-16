import type { PositionCreateType } from '@/types'

export default class PositionCreate implements PositionCreateType {
  company: string
  title: string
  description: string

  constructor(data?: Partial<PositionCreateType>) {
    this.company = data?.company || ''
    this.title = data?.title || ''
    this.description = data?.description || ''
  }

  get isValid(): boolean {
    return this.company !== '' && this.title !== '' && this.description !== ''
  }

  clear(): void {
    this.company = ''
    this.title = ''
    this.description = ''
  }
}
