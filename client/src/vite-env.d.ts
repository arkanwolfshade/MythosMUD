/// <reference types="vite/client" />

declare global {
  /** Vitest-only jsdom window for DOMPurify; initialized in src/test/setup.ts via domPurifyTestWindow.ts. */
  var __MYTHOSMUD_DOMPURIFY_WINDOW__: (Window & typeof globalThis) | undefined;
}

export {};
