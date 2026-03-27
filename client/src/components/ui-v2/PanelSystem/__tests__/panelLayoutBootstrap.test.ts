import { beforeEach, describe, expect, it, vi } from 'vitest';
import type { PanelState } from '../../types';
import { mergePanelMetadataFromDefault, resolveInitialPanelLayout } from '../panelLayoutBootstrap';

const hoisted = vi.hoisted(() => ({
  loadPanelLayout: vi.fn(),
  savePanelLayout: vi.fn(),
  layoutFitsViewport: vi.fn(),
  clampPanelLayoutToViewport: vi.fn(),
}));

vi.mock('../panelLayoutValidation', () => ({
  loadPanelLayout: hoisted.loadPanelLayout,
  savePanelLayout: hoisted.savePanelLayout,
}));

vi.mock('../panelLayoutClamp', () => ({
  layoutFitsViewport: hoisted.layoutFitsViewport,
  clampPanelLayoutToViewport: hoisted.clampPanelLayoutToViewport,
}));

function basePanel(id: string, overrides: Partial<PanelState> = {}): PanelState {
  return {
    id,
    title: 'Panel',
    position: { x: 0, y: 0 },
    size: { width: 200, height: 150 },
    zIndex: 1,
    isMinimized: false,
    isMaximized: false,
    isVisible: true,
    ...overrides,
  };
}

describe('mergePanelMetadataFromDefault', () => {
  it('copies opaque from default when default defines it', () => {
    const stored = { chat: basePanel('chat', { opaque: false }) };
    const defaults = {
      chat: basePanel('chat', { opaque: true }),
    };
    const out = mergePanelMetadataFromDefault(stored, defaults);
    expect(out.chat.opaque).toBe(true);
    expect(out.chat.position).toEqual(stored.chat.position);
  });

  it('copies minHeight from default when default defines it', () => {
    const stored = { map: basePanel('map', {}) };
    const defaults = {
      map: basePanel('map', { minHeight: 240 }),
    };
    const out = mergePanelMetadataFromDefault(stored, defaults);
    expect(out.map.minHeight).toBe(240);
  });

  it('patches both opaque and minHeight when both are set on default', () => {
    const stored = { p1: basePanel('p1') };
    const defaults = {
      p1: basePanel('p1', { opaque: true, minHeight: 120 }),
    };
    const out = mergePanelMetadataFromDefault(stored, defaults);
    expect(out.p1.opaque).toBe(true);
    expect(out.p1.minHeight).toBe(120);
  });

  it('leaves stored panel unchanged when there is no matching default entry', () => {
    const stored = { orphan: basePanel('orphan', { opaque: true }) };
    const defaults = { other: basePanel('other') };
    const out = mergePanelMetadataFromDefault(stored, defaults);
    expect(out.orphan).toEqual(stored.orphan);
  });

  it('does not add metadata when default omits opaque and minHeight', () => {
    const stored = { chat: basePanel('chat', { opaque: false, minHeight: 50 }) };
    const defaults = { chat: basePanel('chat') };
    const out = mergePanelMetadataFromDefault(stored, defaults);
    expect(out.chat.opaque).toBe(false);
    expect(out.chat.minHeight).toBe(50);
  });

  it('does not mutate the original stored map', () => {
    const stored = { chat: basePanel('chat') };
    const snapshot = JSON.stringify(stored);
    const defaults = { chat: basePanel('chat', { opaque: true }) };
    mergePanelMetadataFromDefault(stored, defaults);
    expect(JSON.stringify(stored)).toBe(snapshot);
  });
});

describe('resolveInitialPanelLayout', () => {
  const defaults = { chat: basePanel('chat', { opaque: true, minHeight: 100 }) };

  beforeEach(() => {
    hoisted.loadPanelLayout.mockReset();
    hoisted.savePanelLayout.mockReset();
    hoisted.layoutFitsViewport.mockReset();
    hoisted.clampPanelLayoutToViewport.mockReset();
  });

  it('returns default panels when nothing is stored', () => {
    hoisted.loadPanelLayout.mockReturnValue(null);
    const out = resolveInitialPanelLayout(defaults, 800, 600);
    expect(out).toBe(defaults);
    expect(hoisted.savePanelLayout).not.toHaveBeenCalled();
  });

  it('merges metadata when stored layout fits the viewport', () => {
    const stored = { chat: basePanel('chat', { opaque: false }) };
    hoisted.loadPanelLayout.mockReturnValue(stored);
    hoisted.layoutFitsViewport.mockReturnValue(true);
    const out = resolveInitialPanelLayout(defaults, 800, 600);
    expect(out.chat.opaque).toBe(true);
    expect(hoisted.clampPanelLayoutToViewport).not.toHaveBeenCalled();
    expect(hoisted.savePanelLayout).not.toHaveBeenCalled();
  });

  it('clamps, merges, persists, and returns when stored layout does not fit', () => {
    const stored = { chat: basePanel('chat') };
    const clamped = { chat: basePanel('chat', { position: { x: 0, y: 0 } }) };
    hoisted.loadPanelLayout.mockReturnValue(stored);
    hoisted.layoutFitsViewport.mockReturnValue(false);
    hoisted.clampPanelLayoutToViewport.mockReturnValue(clamped);

    const out = resolveInitialPanelLayout(defaults, 400, 300);

    expect(hoisted.clampPanelLayoutToViewport).toHaveBeenCalledWith(stored, 400, 300);
    expect(hoisted.savePanelLayout).toHaveBeenCalledTimes(1);
    expect(hoisted.savePanelLayout.mock.calls[0][0]).toEqual(out);
    expect(out.chat.opaque).toBe(true);
  });
});
