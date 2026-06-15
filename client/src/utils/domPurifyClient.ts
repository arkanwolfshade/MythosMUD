import createDOMPurify, { type Config as DOMPurifyConfig } from 'dompurify';

type DOMPurifyInstance = ReturnType<typeof createDOMPurify>;

let domPurifyInstance: DOMPurifyInstance | undefined;

/**
 * Bind DOMPurify to the active window on first use.
 * Vitest happy-dom initializes window after ESM imports; eager imports in security.ts
 * would otherwise capture a pre-DOM fallback parser (behavior changed in dompurify 3.4.8+).
 */
export function getDomPurify(): DOMPurifyInstance {
  if (!domPurifyInstance) {
    const windowLike = globalThis.window;
    if (!windowLike?.document) {
      throw new Error('DOMPurify requires window.document');
    }
    domPurifyInstance = createDOMPurify(windowLike);
  }
  return domPurifyInstance;
}

/** Wrapper kept explicit for CodeQL XSS sink modeling at call sites (e.g. SafeHtml). */
export function sanitizeWithDomPurify(dirty: string, config?: DOMPurifyConfig): string {
  return getDomPurify().sanitize(dirty, config);
}
