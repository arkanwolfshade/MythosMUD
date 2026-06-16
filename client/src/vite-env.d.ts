/// <reference types="vite/client" />

declare global {
  /** Vitest-only DOMPurify binding target; initialized in src/test/setup.ts. */
  var __MYTHOSMUD_DOMPURIFY_WINDOW__: (Window & typeof globalThis) | undefined;
}

export {};
