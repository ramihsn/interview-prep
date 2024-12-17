import type { PositionType } from '@/types'
import PositionCreate from './PositionCreate'

export default class Position extends PositionCreate implements PositionType {
  id: number

  constructor(data: PositionType) {
    super(data)
    this.id = data.id
  }
}
