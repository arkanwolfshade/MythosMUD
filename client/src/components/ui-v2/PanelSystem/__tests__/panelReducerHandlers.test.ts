import { beforeEach, describe, expect, it, vi } from 'vitest';

import type { PanelState } from '../../types';
import { savePanelLayout } from '../panelLayoutValidation';
import {
  handleClosePanel,
  handleFocusPanel,
  handleInitPanels,
  handleScaleToViewport,
  handleSetVisibility,
  handleToggleMaximize,
  handleToggleMinimize,
  handleUpdatePosition,
  handleUpdateSize,
  type PanelManagerState,
} from '../panelReducerHandlers';

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

  it('handleInitPanels sets next z-index above max panel z-index', () => {
    const state = stateFixture();
    const incoming = {
      alpha: { ...panelFixture('alpha'), zIndex: 1500 },
      beta: { ...panelFixture('beta'), zIndex: 1200 },
    };

    const next = handleInitPanels(state, incoming);

    expect(next.panels).toBe(incoming);
    expect(next.nextZIndex).toBe(1501);
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

  it('handleUpdateSize updates panel size and persists layout', () => {
    const state = stateFixture();

    const next = handleUpdateSize(state, { id: 'test', size: { width: 480, height: 320 } });

    expect(next.panels.test.size).toEqual({ width: 480, height: 320 });
    expect(savePanelLayout).toHaveBeenCalledTimes(1);
    expect(savePanelLayout).toHaveBeenCalledWith(next.panels);
  });

  it('handleUpdateSize is a no-op when panel id is missing', () => {
    const state = stateFixture();

    const next = handleUpdateSize(state, { id: 'missing', size: { width: 480, height: 320 } });

    expect(next).toBe(state);
    expect(savePanelLayout).not.toHaveBeenCalled();
  });

  it('handleToggleMinimize toggles minimized and clears maximized state', () => {
    const state = stateFixture();
    const next = handleToggleMinimize(state, { id: 'test' });

    expect(next.panels.test.isMinimized).toBe(true);
    expect(next.panels.test.isMaximized).toBe(false);
    expect(savePanelLayout).toHaveBeenCalledWith(next.panels);
  });

  it('handleToggleMinimize is a no-op when panel id is missing', () => {
    const state = stateFixture();
    const next = handleToggleMinimize(state, { id: 'missing' });

    expect(next).toBe(state);
    expect(savePanelLayout).not.toHaveBeenCalled();
  });

  it('handleToggleMaximize maximizes target and un-maximizes others', () => {
    const state: PanelManagerState = {
      ...stateFixture(),
      panels: {
        test: { ...panelFixture('test'), isMaximized: false },
        other: { ...panelFixture('other'), isMaximized: true },
      },
    };

    const next = handleToggleMaximize(state, { id: 'test' });

    expect(next.panels.test.isMaximized).toBe(true);
    expect(next.panels.test.isMinimized).toBe(false);
    expect(next.panels.other.isMaximized).toBe(false);
    expect(savePanelLayout).toHaveBeenCalledWith(next.panels);
  });

  it('handleToggleMaximize toggles off already maximized panel', () => {
    const state: PanelManagerState = {
      ...stateFixture(),
      panels: {
        test: { ...panelFixture('test'), isMaximized: true },
      },
    };

    const next = handleToggleMaximize(state, { id: 'test' });

    expect(next.panels.test.isMaximized).toBe(false);
    expect(next.panels.test.isMinimized).toBe(false);
    expect(savePanelLayout).toHaveBeenCalledWith(next.panels);
  });

  it('handleToggleMaximize is a no-op when panel id is missing', () => {
    const state = stateFixture();
    const next = handleToggleMaximize(state, { id: 'missing' });

    expect(next).toBe(state);
    expect(savePanelLayout).not.toHaveBeenCalled();
  });

  it('handleSetVisibility updates visibility and persists layout', () => {
    const state = stateFixture();
    const next = handleSetVisibility(state, { id: 'test', isVisible: false });

    expect(next.panels.test.isVisible).toBe(false);
    expect(savePanelLayout).toHaveBeenCalledWith(next.panels);
  });

  it('handleSetVisibility is a no-op when panel id is missing', () => {
    const state = stateFixture();
    const next = handleSetVisibility(state, { id: 'missing', isVisible: false });

    expect(next).toBe(state);
    expect(savePanelLayout).not.toHaveBeenCalled();
  });

  it('handleFocusPanel updates focus, z-index, and next z-index', () => {
    const state = stateFixture();
    const next = handleFocusPanel(state, { id: 'test' });

    expect(next.panels.test.zIndex).toBe(1001);
    expect(next.focusedPanelId).toBe('test');
    expect(next.nextZIndex).toBe(1002);
    expect(savePanelLayout).toHaveBeenCalledWith(next.panels);
  });

  it('handleFocusPanel is a no-op when panel id is missing', () => {
    const state = stateFixture();
    const next = handleFocusPanel(state, { id: 'missing' });

    expect(next).toBe(state);
    expect(savePanelLayout).not.toHaveBeenCalled();
  });

  it('handleClosePanel removes panel and clears focused id when needed', () => {
    const state: PanelManagerState = {
      ...stateFixture(),
      panels: {
        test: panelFixture('test'),
        other: panelFixture('other'),
      },
      focusedPanelId: 'test',
    };

    const next = handleClosePanel(state, { id: 'test' });

    expect(next.panels.test).toBeUndefined();
    expect(next.panels.other).toBeDefined();
    expect(next.focusedPanelId).toBeNull();
    expect(savePanelLayout).toHaveBeenCalledWith(next.panels);
  });

  it('handleClosePanel preserves focused id when closing a different panel', () => {
    const state: PanelManagerState = {
      ...stateFixture(),
      panels: {
        test: panelFixture('test'),
        other: panelFixture('other'),
      },
      focusedPanelId: 'other',
    };

    const next = handleClosePanel(state, { id: 'test' });

    expect(next.focusedPanelId).toBe('other');
    expect(next.panels.test).toBeUndefined();
    expect(savePanelLayout).toHaveBeenCalledWith(next.panels);
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

  it('handleScaleToViewport skips missing, minimized, and maximized panels', () => {
    const state: PanelManagerState = {
      ...stateFixture(),
      panels: {
        test: panelFixture('test'),
        minimized: { ...panelFixture('minimized'), isMinimized: true },
        maximized: { ...panelFixture('maximized'), isMaximized: true },
      },
    };
    const scaleFunction = () => ({
      missing: { ...panelFixture('missing'), position: { x: 500, y: 500 } },
      test: { ...panelFixture('test'), position: { x: 400, y: 300 }, size: { width: 350, height: 250 } },
      minimized: { ...panelFixture('minimized'), position: { x: 400, y: 300 }, size: { width: 350, height: 250 } },
      maximized: { ...panelFixture('maximized'), position: { x: 400, y: 300 }, size: { width: 350, height: 250 } },
    });

    const next = handleScaleToViewport(state, {
      viewportWidth: 800,
      viewportHeight: 600,
      scaleFunction,
    });

    expect(next.panels.test.position).toEqual({ x: 400, y: 300 });
    expect(next.panels.minimized.position).toEqual(state.panels.minimized.position);
    expect(next.panels.maximized.position).toEqual(state.panels.maximized.position);
    expect(next.panels.missing).toBeUndefined();
    expect(savePanelLayout).toHaveBeenCalledWith(next.panels);
  });

  it('handleScaleToViewport honors panel minHeight when viewport allows it', () => {
    const state: PanelManagerState = {
      ...stateFixture(),
      panels: {
        test: {
          ...panelFixture('test'),
          minSize: { width: 200, height: 120 },
        },
      },
    };
    const scaleFunction = () => ({
      test: {
        ...panelFixture('test'),
        minHeight: 260,
        position: { x: 10, y: 60 },
        size: { width: 300, height: 100 },
      },
    });

    const next = handleScaleToViewport(state, {
      viewportWidth: 800,
      viewportHeight: 600,
      scaleFunction,
    });

    expect(next.panels.test.size.height).toBe(260);
    expect(savePanelLayout).toHaveBeenCalledWith(next.panels);
  });
});
