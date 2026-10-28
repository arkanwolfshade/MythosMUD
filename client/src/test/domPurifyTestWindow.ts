import { JSDOM } from 'jsdom';

declare global {
  // Vitest-only slot for DOMPurify's preferred Window (also declared in src/vite-env.d.ts for app).

  var __MYTHOSMUD_DOMPURIFY_WINDOW__: (Window & typeof globalThis) | undefined;
}

/** Vitest-only jsdom window for DOMPurify (happy-dom is unreliable with dompurify 3.4.8+ on Node 22 Linux). */
function createDomPurifyTestWindow(): Window & typeof globalThis {
  return new JSDOM('<!DOCTYPE html><html><body></body></html>', {
    url: 'https://mythosmud.test/',
  }).window as unknown as Window & typeof globalThis;
}

export function installDomPurifyTestWindow(): void {
  if (globalThis.__MYTHOSMUD_DOMPURIFY_WINDOW__) {
    return;
  }
  globalThis.__MYTHOSMUD_DOMPURIFY_WINDOW__ = createDomPurifyTestWindow();
}
