const _LIGHT = 'nord'
const _DARK = 'business'

export enum Theme {
  LIGHT = _LIGHT,
  DARK = _DARK,
}

export function isDarkTheme(theme: string): boolean {
  return theme === Theme.DARK
}

export function toggleTheme(theme: string): string {
  return theme === Theme.DARK ? _LIGHT : _DARK
}

export function getTheme(theme?: string): Theme {
  if (!theme) {
    return Theme.DARK
  }

  return theme === _LIGHT ? Theme.LIGHT : Theme.DARK
}

export const themes = [
  'light',
  'dark',
  'cupcake',
  'bumblebee',
  'emerald',
  'corporate',
  'synthwave',
  'retro',
  'cyberpunk',
  'valentine',
  'halloween',
  'garden',
  'forest',
  'aqua',
  'lofi',
  'pastel',
  'fantasy',
  'wireframe',
  'black',
  'luxury',
  'dracula',
  'cmyk',
  'autumn',
  'business',
  'acid',
  'lemonade',
  'night',
  'coffee',
  'winter',
  'dim',
  'nord',
  'sunset',
]
