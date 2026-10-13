// Parses styles/messageCategories.css (the single source of truth for the palette) and enforces
// WCAG contrast per category color against the panel background, so lowering a value fails here.

import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { describe, expect, it } from 'vitest';
import { MESSAGE_CATEGORIES } from '../../../../types/messageCategory';

const read = (relative: string): string => readFileSync(fileURLToPath(new URL(relative, import.meta.url)), 'utf-8');

const css = read('../../../../styles/messageCategories.css');

// Panels draw message rows on mythos-terminal-surface (#1a1a1a); the log area behind is darker (#0a0a0a).
const PANEL_BACKGROUND = '#1a1a1a';
const NORMAL_MIN = 4.5;
const HIGH_CONTRAST_MIN = 7;

function relativeLuminance(hex: string): number {
  const n = parseInt(hex.slice(1), 16);
  const channel = (value: number): number => {
    const c = value / 255;
    return c <= 0.03928 ? c / 12.92 : ((c + 0.055) / 1.055) ** 2.4;
  };
  return 0.2126 * channel(n >> 16) + 0.7152 * channel((n >> 8) & 255) + 0.0722 * channel(n & 255);
}

function contrastRatio(foreground: string, background: string): number {
  const a = relativeLuminance(foreground);
  const b = relativeLuminance(background);
  return (Math.max(a, b) + 0.05) / (Math.min(a, b) + 0.05);
}

/** `--cat-<domain>-<kind>: #hex;` declarations inside the block opened by `selector`. */
function paletteIn(selector: string): Record<string, string> {
  const start = css.indexOf(`${selector} {`);
  expect(start, `${selector} block present`).toBeGreaterThanOrEqual(0);
  const block = css.slice(start, css.indexOf('}', start));
  const palette: Record<string, string> = {};
  for (const match of block.matchAll(/--cat-([a-z]+-[a-z_]+):\s*(#[0-9a-fA-F]{6})\s*;/g)) {
    palette[match[1]] = match[2];
  }
  return palette;
}

const categories: readonly string[] = MESSAGE_CATEGORIES;
const normal = paletteIn(':root');
const highContrast = paletteIn('html.high-contrast');

describe('message category palette', () => {
  it('knows every category from the TS union', () => {
    expect(categories.length).toBeGreaterThanOrEqual(24);
  });

  it('defines a color for every category, normal and high contrast', () => {
    const expected = categories.map(c => c.replace('.', '-')).sort();
    expect(Object.keys(normal).sort()).toEqual(expected);
    expect(Object.keys(highContrast).sort()).toEqual(expected);
  });

  it.each(Object.entries(normal))('%s meets 4.5:1 against the panel background', (_name, color) => {
    expect(contrastRatio(color, PANEL_BACKGROUND)).toBeGreaterThanOrEqual(NORMAL_MIN);
  });

  it.each(Object.entries(highContrast))(
    '%s meets 7:1 against the panel background in high contrast',
    (_name, color) => {
      expect(contrastRatio(color, PANEL_BACKGROUND)).toBeGreaterThanOrEqual(HIGH_CONTRAST_MIN);
    }
  );

  it('also holds against the darker log background', () => {
    for (const color of Object.values(normal)) {
      expect(contrastRatio(color, '#0a0a0a')).toBeGreaterThanOrEqual(NORMAL_MIN);
    }
  });

  // chat.* kinds may share colours with each other, but no other category may reuse a chat colour: combat, status,
  // system, room and command lines must stay distinguishable from chat by colour too (their glyph and register are
  // a second cue, not the only one).
  const nonChat = Object.keys(normal).filter(key => !key.startsWith('chat-'));
  it.each(nonChat)('%s shares no colour with any chat.* category', name => {
    for (const [label, palette] of [
      ['normal', normal],
      ['high contrast', highContrast],
    ] as const) {
      const chatColors = Object.entries(palette)
        .filter(([key]) => key.startsWith('chat-'))
        .map(([, color]) => color.toLowerCase());
      expect(chatColors, `${name} in the ${label} palette`).not.toContain(palette[name].toLowerCase());
    }
  });

  it('measures contrast correctly (sanity check of the helper)', () => {
    expect(contrastRatio('#ffffff', '#000000')).toBeCloseTo(21, 0);
    expect(contrastRatio('#777777', '#1a1a1a')).toBeLessThan(NORMAL_MIN);
  });

  it('defines per-kind, domain and register classes for every category', () => {
    for (const category of categories) {
      const [domain] = category.split('.');
      expect(css).toContain(`.cat-${category.replace('.', '-')} {`);
      expect(css).toContain(`.cat-${domain} {`);
    }
    for (const register of ['alert', 'private', 'action', 'meta', 'plain', 'heading']) {
      expect(css).toContain(`.cat-reg-${register} {`);
    }
  });

  it('never underlines (reserved for interactive text)', () => {
    expect(css.replace(/\/\*[\s\S]*?\*\//g, '')).not.toMatch(/text-decoration:\s*underline/);
  });

  it('keeps the glyph fallback, alt-text form and text-label mode', () => {
    expect(css).toMatch(/@supports \(content: 'a' \/ 'b'\)/);
    expect(css).toContain('html.text-labels .cat::before');
    expect(css).toContain('font-display: swap');
  });

  it('keeps a gap after the text label (found in a real browser: the inline-block collapses a trailing space)', () => {
    const start = css.indexOf('html.text-labels .cat::before {');
    expect(start).toBeGreaterThanOrEqual(0);
    const block = css.slice(start, css.indexOf('}', start));
    const margin = /margin-inline-end:\s*([^;]+);/.exec(block)?.[1].trim();
    expect(margin, 'text-label mode sets margin-inline-end').toBeDefined();
    expect(parseFloat(margin ?? '0')).toBeGreaterThan(0);
  });
});
