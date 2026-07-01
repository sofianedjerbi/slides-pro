import { chromium } from 'playwright'
import { mkdirSync } from 'node:fs'

const BASE = 'http://localhost:4321'
const OUT = new URL('../images/', import.meta.url).pathname
mkdirSync(OUT, { recursive: true })

const browser = await chromium.launch()
const page = await browser.newPage({
  viewport: { width: 1440, height: 900 },
  deviceScaleFactor: 2,
})

async function settle() {
  await page.waitForLoadState('networkidle').catch(() => {})
  // wait for at least one rendered mermaid SVG, then let icons/layout settle
  await page.waitForSelector('.sl-markdown-content svg, .mermaid svg', { timeout: 8000 }).catch(() => {})
  await page.waitForTimeout(3500)
}

async function shoot(path, file, { full = false } = {}) {
  await page.goto(BASE + path, { waitUntil: 'domcontentloaded' })
  await settle()
  await page.screenshot({ path: OUT + file, fullPage: full })
  console.log('saved', file, full ? '(full page)' : '')
}

async function shootEl(path, selector, file) {
  await page.goto(BASE + path, { waitUntil: 'domcontentloaded' })
  await settle()
  const el = await page.$(selector)
  if (!el) { console.log('MISSING selector', selector, 'on', path); return }
  await el.screenshot({ path: OUT + file })
  console.log('saved', file, `(${selector})`)
}

// Landing / target architecture
await shoot('/', 'home-hero.png')              // viewport: sidebar + page + first diagram
await shoot('/', 'home-full.png', { full: true }) // whole page incl. big diagrams

// ADR-0001 ECS over EKS
await shoot('/adr/0001-ecs-over-eks/', 'adr-top.png')               // sidebar badges + title + status
await shoot('/adr/0001-ecs-over-eks/', 'adr-full.png', { full: true }) // full ADR incl. mermaid + cost table

// Focused elements
await shootEl('/adr/0001-ecs-over-eks/', '.sl-markdown-content table', 'adr-cost-table.png')
await shootEl('/adr/0001-ecs-over-eks/', 'starlight-menu-content, nav.sidebar, #starlight__sidebar', 'sidebar.png')

await browser.close()
console.log('DONE →', OUT)
