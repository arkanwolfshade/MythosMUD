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

let cachedPurify: DOMPurifyInstance | undefined;
let cachedWindow: (Window & typeof globalThis) | undefined;

function verifiesDomPurifySanitize(purify: DOMPurifyInstance): boolean {
  try {
    const plain = purify.sanitize(PLAIN_CHAT_PROBE, INCOMING_HTML_PROBE_CONFIG);
    const html = purify.sanitize(HTML_CHAT_PROBE, INCOMING_HTML_PROBE_CONFIG);
    return plain === PLAIN_CHAT_PROBE && html.includes('Message with') && html.includes('HTML');
  } catch {
    return false;
  }
}

function collectWindowCandidates(): Array<Window & typeof globalThis> {
  const seen = new Set<Window & typeof globalThis>();
  const candidates: Array<Window & typeof globalThis> = [];
  const add = (windowLike: typeof globalThis.window | null | undefined): void => {
    if (windowLike?.document?.createElement && !seen.has(windowLike)) {
      seen.add(windowLike);
      candidates.push(windowLike);
    }
  };

  // Prefer document.defaultView first: Node 22 on Linux may expose a broken globalThis.window
  // while happy-dom's real window remains on document.defaultView.
  add(globalThis.document?.defaultView ?? undefined);
  add(globalThis.window);
  return candidates;
}

function getVitestHappyDomWindow(): (Window & typeof globalThis) | undefined {
  return globalThis.__MYTHOSMUD_DOMPURIFY_WINDOW__;
}

function resolveVitestSanitizeWindow(): Window & typeof globalThis {
  const vitestWindow = getVitestHappyDomWindow();
  if (!vitestWindow) {
    throw new Error('Vitest setup must initialize globalThis.__MYTHOSMUD_DOMPURIFY_WINDOW__');
  }
  if (!verifiesDomPurifySanitize(createDOMPurify(vitestWindow))) {
    throw new Error('Vitest DOMPurify window failed incoming HTML sanitize probe');
  }
  return vitestWindow;
}

/**
 * Pick a window that passes incoming HTML sanitize probes when possible.
 * In Vitest, always use the dedicated happy-dom window from setup.ts first. Node 22 on Linux may expose
 * a global window that false-passes probes but still mangles sanitize output.
 */
function resolveSanitizeWindow(): Window & typeof globalThis {
  if (import.meta.env.VITEST) {
    return resolveVitestSanitizeWindow();
  }

  const candidates = collectWindowCandidates();
  for (const candidate of candidates) {
    if (verifiesDomPurifySanitize(createDOMPurify(candidate))) {
      return candidate;
    }
  }

  const fallback = candidates[0];
  if (fallback) {
    return fallback;
  }

  throw new Error('DOMPurify requires a DOM window with HTML parsing (happy-dom in Vitest)');
}

/**
 * Bind DOMPurify to the active window on first use per window reference.
 * Vitest happy-dom initializes window after ESM imports; eager singleton binding in security.ts
 * would otherwise capture a pre-DOM fallback parser (behavior changed in dompurify 3.4.8+).
 */
export function getDomPurify(): DOMPurifyInstance {
  const windowLike = resolveSanitizeWindow();
  if (!cachedPurify || cachedWindow !== windowLike) {
    cachedPurify = createDOMPurify(windowLike);
    cachedWindow = windowLike;
  }
  return cachedPurify;
}

/** Clear cached instance when Vitest replaces or restores globalThis.window between tests. */
export function resetDomPurifyClientForTests(): void {
  cachedPurify = undefined;
  cachedWindow = undefined;
}

/** Wrapper kept explicit for CodeQL XSS sink modeling at call sites (e.g. SafeHtml). */
export function sanitizeWithDomPurify(dirty: string, config?: DOMPurifyConfig): string {
  return getDomPurify().sanitize(dirty, config);
}
