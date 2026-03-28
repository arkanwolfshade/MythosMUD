import { describe, expect, it } from 'vitest';
import type { PanelState } from '../../types';
import { PANEL_VIEWPORT_PADDING, clampPanelLayoutToViewport, layoutFitsViewport } from '../panelLayoutClamp';

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

  it('returns false when a panel extends past the bottom edge', () => {
    const panels = {
      p1: basePanel({
        position: { x: 100, y: 100 },
        size: { width: 200, height: 2000 },
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

  it('clamps a panel that only overflows the right edge', () => {
    const vw = 800;
    const vh = 600;
    const maxRight = vw - PANEL_VIEWPORT_PADDING;
    const maxBottom = vh - PANEL_VIEWPORT_PADDING;
    const p = basePanel({
      id: 'rightOnly',
      position: { x: 400, y: 80 },
      size: { width: 500, height: 200 },
    });
    expect(p.position.x + p.size.width).toBeGreaterThan(maxRight);

    const clamped = clampPanelLayoutToViewport({ rightOnly: p }, vw, vh);
    const q = clamped.rightOnly;
    expect(q.position.y + q.size.height).toBeLessThanOrEqual(maxBottom);
    expect(q.position.x + q.size.width).toBeLessThanOrEqual(maxRight);
    expect(layoutFitsViewport(clamped, vw, vh)).toBe(true);
  });

  it('clamps a panel that only overflows the bottom edge', () => {
    const vw = 800;
    const vh = 600;
    const maxRight = vw - PANEL_VIEWPORT_PADDING;
    const maxBottom = vh - PANEL_VIEWPORT_PADDING;
    const p = basePanel({
      id: 'bottomOnly',
      position: { x: 80, y: 450 },
      size: { width: 200, height: 250 },
    });
    expect(p.position.y + p.size.height).toBeGreaterThan(maxBottom);

    const clamped = clampPanelLayoutToViewport({ bottomOnly: p }, vw, vh);
    const q = clamped.bottomOnly;
    expect(q.position.x + q.size.width).toBeLessThanOrEqual(maxRight);
    expect(q.position.y + q.size.height).toBeLessThanOrEqual(maxBottom);
    expect(layoutFitsViewport(clamped, vw, vh)).toBe(true);
  });

  it('raises height toward minHeight when the viewport can accommodate it', () => {
    const vw = 800;
    const vh = 600;
    const p = basePanel({
      id: 'tallContent',
      position: { x: 40, y: 40 },
      size: { width: 300, height: 80 },
      minSize: { width: 100, height: 100 },
      minHeight: 250,
    });
    const clamped = clampPanelLayoutToViewport({ tallContent: p }, vw, vh);
    expect(clamped.tallContent.size.height).toBe(250);
  });

  it('does not apply minHeight when the padded viewport is shorter than minHeight', () => {
    const vw = 800;
    const vh = 200;
    const p = basePanel({
      id: 'tooTall',
      position: { x: 40, y: 40 },
      size: { width: 300, height: 80 },
      minSize: { width: 100, height: 100 },
      minHeight: 500,
    });
    const clamped = clampPanelLayoutToViewport({ tooTall: p }, vw, vh);
    expect(clamped.tooTall.size.height).toBeLessThan(500);
  });
});
