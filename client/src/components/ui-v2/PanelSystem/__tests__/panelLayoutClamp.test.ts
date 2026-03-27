import { describe, expect, it } from 'vitest';
import type { PanelState } from '../../types';
import { clampPanelLayoutToViewport, layoutFitsViewport } from '../panelLayoutClamp';

function basePanel(overrides: Partial<PanelState> = {}): PanelState {
  return {
    id: 'p1',
    title: 'Panel',
    position: { x: 100, y: 100 },
    size: { width: 400, height: 300 },
    zIndex: 1000,
    isMinimized: false,
    isMaximized: false,
    isVisible: true,
    ...overrides,
  };
}

describe('layoutFitsViewport', () => {
  it('returns true when all panels fit padded viewport', () => {
    const panels = { p1: basePanel() };
    expect(layoutFitsViewport(panels, 1920, 1080)).toBe(true);
  });

  it('returns false when a panel extends past the right edge', () => {
    const panels = {
      p1: basePanel({
        position: { x: 100, y: 100 },
        size: { width: 2000, height: 300 },
      }),
    };
    expect(layoutFitsViewport(panels, 800, 600)).toBe(false);
  });
});

describe('clampPanelLayoutToViewport', () => {
  it('produces a layout that passes layoutFitsViewport', () => {
    const wide = basePanel({
      id: 'wide',
      position: { x: 0, y: 0 },
      size: { width: 2000, height: 400 },
    });
    const stored = { wide };
    const vw = 800;
    const vh = 600;
    const clamped = clampPanelLayoutToViewport(stored, vw, vh);
    expect(layoutFitsViewport(clamped, vw, vh)).toBe(true);
    expect(clamped.wide.size.width).toBeLessThanOrEqual(vw);
  });

  it('shrinks and shifts panels that overflow bottom-right', () => {
    const p = basePanel({
      position: { x: 700, y: 500 },
      size: { width: 400, height: 400 },
    });
    const clamped = clampPanelLayoutToViewport({ p1: p }, 800, 600);
    expect(clamped.p1.position.x + clamped.p1.size.width).toBeLessThanOrEqual(800 - 40);
    expect(clamped.p1.position.y + clamped.p1.size.height).toBeLessThanOrEqual(600 - 40);
  });
});
