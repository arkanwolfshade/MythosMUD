/**
 * Installs the `__mythosE2e*` window helpers (see multiplayer-browser-window.d.ts) into a
 * BrowserContext via an init script. Every context this suite creates must call this --
 * `window.__mythosE2eIsGameUiLoaded`/`__mythosE2eCaptureGameUiDiagnostics` have no DOM-based
 * fallback (unlike `__mythosE2eHasConnectedStatus`'s callers), so a context that skips this
 * leaves `waitForPlayerGameUi` polling `undefined?.() === true` forever -- a guaranteed timeout
 * even when the underlying login/WebSocket connection is perfectly healthy (#297).
 */

import { dirname, join } from 'path';
import { fileURLToPath } from 'url';

import type { Browser, BrowserContext } from '@playwright/test';

const __dirname = dirname(fileURLToPath(import.meta.url));
const BROWSER_HELPERS_BUNDLE = join(__dirname, 'multiplayer-browser-helpers.bundle.js');

async function installE2eBrowserHelpers(context: BrowserContext): Promise<void> {
  await context.addInitScript({ path: BROWSER_HELPERS_BUNDLE });
}

/**
 * The one place this suite should call `browser.newContext()`. Every fresh context needs the
 * helpers installed -- a call site that mints its own `browser.newContext()` and forgets this is
 * exactly how #297's "waitForPlayerGameUi times out forever" bug happened. Routing context
 * creation through here makes that structurally impossible instead of relying on each call site
 * to remember a second call.
 */
export async function createInstrumentedContext(browser: Browser): Promise<BrowserContext> {
  const context = await browser.newContext();
  await installE2eBrowserHelpers(context);
  return context;
}
