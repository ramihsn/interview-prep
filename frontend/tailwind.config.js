import daisyui from 'daisyui'
import typography from '@tailwindcss/typography'

import { themes } from './src/themes'

/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  theme: {
    extend: {},
  },
  plugins: [daisyui, typography],
  daisyui: {
    themes: themes,
  },
}
