import { chromium } from 'playwright'

const URL_ = 'http://localhost:4321/adr/0005-vignettes-upload/'
const OUT = '/Users/sdjerbi/Documents/adr-presentation/images/adr-snapcat.png'

const browser = await chromium.launch()
const page = await browser.newPage({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2 })
await page.goto(URL_, { waitUntil: 'domcontentloaded' })
await page.waitForLoadState('networkidle').catch(() => {})
await page.waitForSelector('.sl-markdown-content svg', { timeout: 8000 }).catch(() => {})
await page.waitForTimeout(3500)
await page.screenshot({ path: OUT })
await browser.close()
console.log('saved', OUT)
