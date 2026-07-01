import { defineShikiSetup } from '@slidev/types'

// Thème de coloration plus contrasté (github) : code et Magic Move bien lisibles,
// surtout projeté en amphi. Le clair est utilisé (colorSchema: light).
export default defineShikiSetup(() => ({
  themes: {
    light: 'github-light',
    dark: 'github-dark',
  },
}))
