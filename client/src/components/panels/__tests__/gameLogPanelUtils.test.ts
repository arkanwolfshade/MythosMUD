import { describe, expect, it } from 'vitest';
import {
  formatGameLogTimestamp,
  getGameLogMessageClassName,
  getGameLogMessageFilterSelectClassName,
  getGameLogMessageRowClassName,
  getGameLogSearchInputClassName,
  getGameLogTimeFilterSelectClassName,
} from '../gameLogPanelUtils';

describe('gameLogPanelUtils', () => {
  it('getGameLogMessageClassName returns classes per type', () => {
    expect(getGameLogMessageClassName('error')).toContain('error');
    expect(getGameLogMessageClassName('move')).toContain('success');
    expect(getGameLogMessageClassName(undefined)).toBe('text-mythos-terminal-text');
  });

  it('getGameLogMessageRowClassName returns row accent classes per type', () => {
    expect(getGameLogMessageRowClassName('error')).toContain('border-l-mythos-terminal-error');
    expect(getGameLogMessageRowClassName('combat')).toContain('border-l-mythos-terminal-error');
    expect(getGameLogMessageRowClassName('move')).toContain('border-l-mythos-terminal-success');
    expect(getGameLogMessageRowClassName(undefined)).toContain('border-l-emerald-900');
  });

  it('filter select helpers reflect active vs all state', () => {
    expect(getGameLogMessageFilterSelectClassName('all')).toContain('border-mythos-terminal-border');
    expect(getGameLogMessageFilterSelectClassName('combat')).toContain('border-mythos-terminal-secondary');
    expect(getGameLogTimeFilterSelectClassName('all')).toContain('border-mythos-terminal-border');
    expect(getGameLogTimeFilterSelectClassName('15')).toContain('border-mythos-terminal-warning');
    expect(getGameLogSearchInputClassName('')).toContain('border-mythos-terminal-border');
    expect(getGameLogSearchInputClassName('blood')).toContain('border-mythos-terminal-primary/50');
  });

  it('formatGameLogTimestamp formats valid ISO strings', () => {
    const out = formatGameLogTimestamp('2024-01-15T14:30:00.000Z');
    expect(out).toMatch(/\d{1,2}:\d{2}:\d{2}/);
  });
});
