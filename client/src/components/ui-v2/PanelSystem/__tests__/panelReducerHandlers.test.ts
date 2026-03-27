import { beforeEach, describe, expect, it, vi } from 'vitest';

import type { PanelState } from '../../types';
import { savePanelLayout } from '../panelLayoutValidation';
import { handleScaleToViewport, handleUpdatePosition, type PanelManagerState } from '../panelReducerHandlers';

vi.mock('../panelLayoutValidation', () => ({
  savePanelLayout: vi.fn(),
}));

function panelFixture(id: string): PanelState {
  return {
    id,
    title: id,
    position: { x: 10, y: 60 },
    size: { width: 300, height: 200 },
    minSize: { width: 200, height: 150 },
    zIndex: 1000,
    isMinimized: false,
    isMaximized: false,
    isVisible: true,
  };
}

function stateFixture(): PanelManagerState {
  return {
    panels: { test: panelFixture('test') },
    focusedPanelId: null,
    nextZIndex: 1001,
  };
}

describe('panelReducerHandlers', () => {
  beforeEach(() => {
    vi.clearAllMocks();
  });

  it('handleUpdatePosition updates panel position and persists layout', () => {
    const state = stateFixture();

    const next = handleUpdatePosition(state, { id: 'test', position: { x: 120, y: 180 } });

    expect(next.panels.test.position).toEqual({ x: 120, y: 180 });
    expect(savePanelLayout).toHaveBeenCalledTimes(1);
    expect(savePanelLayout).toHaveBeenCalledWith(next.panels);
  });

  it('handleUpdatePosition is a no-op when panel id is missing', () => {
    const state = stateFixture();

    const next = handleUpdatePosition(state, { id: 'missing', position: { x: 120, y: 180 } });

    expect(next).toBe(state);
    expect(savePanelLayout).not.toHaveBeenCalled();
  });

  it('handleScaleToViewport clamps layout and persists updates', () => {
    const state = stateFixture();
    const scaleFunction = () => ({
      test: {
        ...panelFixture('test'),
        position: { x: 900, y: 900 },
        size: { width: 700, height: 700 },
      },
    });

    const next = handleScaleToViewport(state, {
      viewportWidth: 800,
      viewportHeight: 600,
      scaleFunction,
    });

    expect(next.panels.test.position.x).toBeLessThanOrEqual(780);
    expect(next.panels.test.position.y).toBeLessThanOrEqual(580);
    expect(next.panels.test.size.width).toBeLessThanOrEqual(800);
    expect(next.panels.test.size.height).toBeLessThanOrEqual(600);
    expect(savePanelLayout).toHaveBeenCalledTimes(1);
    expect(savePanelLayout).toHaveBeenCalledWith(next.panels);
  });
});
