/**
 * Convert waitForMessage expected text into a RegExp source.
 * Plain strings are matched literally (special chars like $^*() must not become regex).
 */

export function escapeRegExpLiteral(s: string): string {
  return s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

export function toMessageMatchPattern(expectedText: string | RegExp): { src: string; fl: string } {
  if (typeof expectedText === 'string') {
    return { src: escapeRegExpLiteral(expectedText), fl: 'i' };
  }
  const flags = expectedText.flags.includes('i') ? expectedText.flags : `${expectedText.flags}i`;
  return { src: expectedText.source, fl: flags };
}
