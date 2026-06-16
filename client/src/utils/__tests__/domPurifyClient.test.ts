import { describe, expect, it } from 'vitest';

import { resetDomPurifyClientForTests, sanitizeWithDomPurify } from '../domPurifyClient';
import { INCOMING_HTML_DOMPURIFY_CONFIG } from '../security';

describe('domPurifyClient', () => {
  it('preserves plain chat text through incoming HTML sanitization', () => {
    const text = '[local] Player1 says: Hello everyone!';
    expect(sanitizeWithDomPurify(text, INCOMING_HTML_DOMPURIFY_CONFIG)).toBe(text);
  });

  it('preserves allowed HTML formatting tags', () => {
    const html = 'Message with <strong>HTML</strong> content';
    const sanitized = sanitizeWithDomPurify(html, INCOMING_HTML_DOMPURIFY_CONFIG);
    expect(sanitized).toContain('Message with');
    expect(sanitized).toContain('HTML');
    expect(sanitized).toContain('content');
  });

  it('uses a dedicated happy-dom window when globalThis.window is a stub', () => {
    const realWindow = globalThis.window;
    const realDefaultView = globalThis.document?.defaultView;
    if (!realDefaultView?.document?.createElement) {
      return;
    }

    Object.defineProperty(globalThis, 'window', {
      value: { document: { createElement: () => ({ innerHTML: '', textContent: '' }) } },
      configurable: true,
      writable: true,
    });

    try {
      const text = '[local] Player1 says: Hello everyone!';
      expect(sanitizeWithDomPurify(text, INCOMING_HTML_DOMPURIFY_CONFIG)).toBe(text);
    } finally {
      Object.defineProperty(globalThis, 'window', {
        value: realWindow,
        configurable: true,
        writable: true,
      });
      resetDomPurifyClientForTests();
    }
  });
});
