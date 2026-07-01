// Recadre une capture en gardant le HAUT (vire la toolbar dev Astro en bas).
// Usage : node scripts/crop-top.mjs <in.png> <out.png> <hauteurGardee>
import { chromium } from 'playwright'

const [inPath, outPath, keepH] = process.argv.slice(2)
const browser = await chromium.launch()
const page = await browser.newPage({ viewport: { width: 2880, height: 1800 } })
await page.goto('file://' + inPath)
await page.screenshot({ path: outPath, clip: { x: 0, y: 0, width: 2880, height: Number(keepH) } })
await browser.close()
console.log('cropped ->', outPath)
