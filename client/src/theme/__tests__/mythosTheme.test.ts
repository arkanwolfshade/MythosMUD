import { describe, expect, it } from 'vitest';

import { mythosTheme } from '../mythosTheme';

describe('mythosTheme', () => {
  it('exports expected typography defaults', () => {
    expect(mythosTheme.typography.fontFamily).toContain('Courier New');
    expect(mythosTheme.typography.h1.fontWeight).toBe('bold');
    expect(mythosTheme.typography.body1.lineHeight).toBe(1.6);
    expect(mythosTheme.typography.caption.fontSize).toBe('0.875rem');
  });
});
