import { describe, expect, it } from 'vitest';

import { escapeRegExpLiteral, toMessageMatchPattern } from '../../tests/e2e/runtime/fixtures/message-match';

describe('toMessageMatchPattern', () => {
  it('escapes regex metacharacters in strings', () => {
    expect(escapeRegExpLiteral('!@#$%^&*()')).toBe('!@#\\$%\\^&\\*\\(\\)');
    expect(toMessageMatchPattern('say $here').src).toBe('say \\$here');
  });

  it('leaves RegExp sources unescaped', () => {
    const { src, fl } = toMessageMatchPattern(/You say locally:.*isolation/i);
    expect(src).toBe('You say locally:.*isolation');
    expect(fl).toContain('i');
  });
});
