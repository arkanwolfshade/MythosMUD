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

const COMMAND_PROBE_CONFIG: DOMPurifyConfig = {
  ALLOWED_TAGS: [],
  ALLOWED_ATTR: [],
  ALLOW_DATA_ATTR: false,
  ALLOW_UNKNOWN_PROTOCOLS: false,
  SAFE_FOR_TEMPLATES: false,
  KEEP_CONTENT: true,
};

const PLAIN_CHAT_PROBE = '[local] Player1 says: Hello everyone!';
const HTML_CHAT_PROBE = 'Message with <strong>HTML</strong> content';

let cachedPurify: DOMPurifyInstance | undefined;
let cachedWindow: (Window & typeof globalThis) | undefined;

function verifiesDomPurifySanitize(purify: DOMPurifyInstance): boolean {
  try {
    const plain = purify.sanitize(PLAIN_CHAT_PROBE, INCOMING_HTML_PROBE_CONFIG);
    const html = purify.sanitize(HTML_CHAT_PROBE, INCOMING_HTML_PROBE_CONFIG);
    const command = purify.sanitize('say <img src=x onerror=alert(1)>', COMMAND_PROBE_CONFIG);
    const script = purify.sanitize('<script>alert("xss")</script>Hello World', {
      ALLOWED_TAGS: ['b'],
      ALLOWED_ATTR: [],
      FORBID_TAGS: ['script'],
      SAFE_FOR_TEMPLATES: true,
    } as DOMPurifyConfig);

    return (
      plain === PLAIN_CHAT_PROBE &&
      html.includes('Message with') &&
      html.includes('HTML') &&
      command.trim() === 'say' &&
      script === 'Hello World'
    );
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

  add(globalThis.__MYTHOSMUD_DOMPURIFY_WINDOW__);
  add(globalThis.document?.defaultView ?? undefined);
  add(globalThis.window);
  return candidates;
}

function resolveVitestSanitizeWindow(): Window & typeof globalThis {
  for (const candidate of collectWindowCandidates()) {
    if (verifiesDomPurifySanitize(createDOMPurify(candidate))) {
      return candidate;
    }
  }

  throw new Error('Vitest DOMPurify window failed sanitize probe; ensure setup.ts installs a jsdom test window');
}

/**
 * Pick a window that passes incoming HTML sanitize probes when possible.
 * In Vitest, prefer the dedicated jsdom window from setup.ts; Node 22 on Linux may expose globals that
 * false-pass simple probes but still mangle sanitize output.
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
