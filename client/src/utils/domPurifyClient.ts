import createDOMPurify, { type Config as DOMPurifyConfig } from 'dompurify';

type DOMPurifyInstance = ReturnType<typeof createDOMPurify>;

/** Mirror INCOMING_HTML_DOMPURIFY_CONFIG for binding probes (avoid circular import from security.ts). */
const INCOMING_HTML_PROBE_CONFIG: DOMPurifyConfig = {
  ALLOWED_TAGS: ['b', 'i', 'em', 'strong', 'br', 'p', 'span', 'div', 'ul', 'ol', 'li', 'code', 'pre'],
  ALLOWED_ATTR: ['class'],
  ALLOW_DATA_ATTR: false,
  ALLOW_UNKNOWN_PROTOCOLS: false,
  SAFE_FOR_TEMPLATES: false,
};

const PLAIN_CHAT_PROBE = '[local] Player1 says: Hello everyone!';
const HTML_CHAT_PROBE = 'Message with <strong>HTML</strong> content';

function verifiesDomPurifySanitize(purify: DOMPurifyInstance): boolean {
  try {
    const plain = purify.sanitize(PLAIN_CHAT_PROBE, INCOMING_HTML_PROBE_CONFIG);
    const html = purify.sanitize(HTML_CHAT_PROBE, INCOMING_HTML_PROBE_CONFIG);
    return plain === PLAIN_CHAT_PROBE && html.includes('Message with') && html.includes('HTML');
  } catch {
    return false;
  }
}

function isUsableDomWindow(windowLike: typeof globalThis.window): windowLike is Window & typeof globalThis {
  if (!windowLike?.document?.createElement) {
    return false;
  }
  return verifiesDomPurifySanitize(createDOMPurify(windowLike));
}

/**
 * Bind DOMPurify to the active window on each sanitize call.
 * Vitest happy-dom initializes window after ESM imports; eager singleton binding in security.ts
 * would otherwise capture a pre-DOM fallback parser (behavior changed in dompurify 3.4.8+).
 * Node 22 on Linux may expose an experimental window that passes createElement checks but still
 * strips chat text when cached; verify with real sanitize() probes and avoid caching instances.
 */
export function getDomPurify(): DOMPurifyInstance {
  const windowLike = globalThis.window;
  if (!isUsableDomWindow(windowLike)) {
    throw new Error('DOMPurify requires a DOM window with HTML parsing (happy-dom in Vitest)');
  }
  return createDOMPurify(windowLike);
}

/** No-op kept for Vitest setup hook compatibility (instances are not cached). */
export function resetDomPurifyClientForTests(): void {
  // Intentionally empty: createDOMPurify(window) is invoked per sanitize call.
}

/** Wrapper kept explicit for CodeQL XSS sink modeling at call sites (e.g. SafeHtml). */
export function sanitizeWithDomPurify(dirty: string, config?: DOMPurifyConfig): string {
  return getDomPurify().sanitize(dirty, config);
}
