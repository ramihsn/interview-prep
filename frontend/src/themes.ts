const _LIGHT = 'nord'
const _DARK = 'business'

export enum Theme {
  LIGHT = _LIGHT,
  DARK = _DARK,
}

export function isDarkTheme(theme: Theme): boolean {
  return theme === Theme.DARK
}

export function toggleTheme(theme: Theme): string {
  return theme === Theme.DARK ? _LIGHT : _DARK
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
