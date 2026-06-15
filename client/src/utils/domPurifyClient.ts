import createDOMPurify, { type Config as DOMPurifyConfig } from 'dompurify';

type DOMPurifyInstance = ReturnType<typeof createDOMPurify>;

let domPurifyInstance: DOMPurifyInstance | undefined;
let boundWindow: (Window & typeof globalThis) | undefined;

function isUsableDomWindow(windowLike: typeof globalThis.window): windowLike is Window & typeof globalThis {
  if (!windowLike?.document?.createElement) {
    return false;
  }
  try {
    const probe = windowLike.document.createElement('div');
    probe.innerHTML = 'Message with <strong>HTML</strong> content';
    return probe.textContent === 'Message with HTML content';
  } catch {
    return false;
  }
}

/**
 * Bind DOMPurify to the active window on first use.
 * Vitest happy-dom initializes window after ESM imports; eager imports in security.ts
 * would otherwise capture a pre-DOM fallback parser (behavior changed in dompurify 3.4.8+).
 * Node 22+ may expose an experimental global window before happy-dom is ready; probe parsing
 * so we never cache DOMPurify against a non-HTML DOM.
 */
export function getDomPurify(): DOMPurifyInstance {
  const windowLike = globalThis.window;
  if (!isUsableDomWindow(windowLike)) {
    throw new Error('DOMPurify requires a DOM window with HTML parsing (happy-dom in Vitest)');
  }
  if (!domPurifyInstance || boundWindow !== windowLike) {
    domPurifyInstance = createDOMPurify(windowLike);
    boundWindow = windowLike;
  }
  return domPurifyInstance;
}

/** Clear cached instance so Vitest can re-bind after happy-dom initializes (CI/Linux). */
export function resetDomPurifyClientForTests(): void {
  domPurifyInstance = undefined;
  boundWindow = undefined;
}

/** Wrapper kept explicit for CodeQL XSS sink modeling at call sites (e.g. SafeHtml). */
export function sanitizeWithDomPurify(dirty: string, config?: DOMPurifyConfig): string {
  return getDomPurify().sanitize(dirty, config);
}
