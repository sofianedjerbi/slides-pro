import { defineMermaidSetup } from '@slidev/types'
import mermaid from 'mermaid/dist/mermaid.esm.mjs'

// Register the Iconify `logos` pack so Mermaid `architecture-beta` diagrams can
// use `logos:aws-*` icon names — the same setup the ADR site (astro-mermaid)
// uses. mermaid is a singleton ES module, so registering here applies to the
// instance Slidev renders with.
mermaid.registerIconPacks([
  {
    name: 'logos',
    loader: () => import('@iconify-json/logos').then(m => m.icons),
  },
])

export default defineMermaidSetup(() => ({
  theme: 'default',
}))
