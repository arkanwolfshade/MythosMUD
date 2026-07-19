import { describe, expect, it } from 'vitest';

import type { PanelState } from '../../types';
import {
  MINIMIZED_BAR_HEIGHT,
  MINIMIZED_BAR_WIDTH,
  MINIMIZED_DOCK_PADDING,
  computeMinimizedDockPosition,
  getMinimizedPanelIds,
  preparePanelForMinimize,
  preparePanelForRestore,
  relayoutMinimizedDock,
} from '../panelMinimizeDock';

function panelFixture(id: string, overrides: Partial<PanelState> = {}): PanelState {
  return {
    id,
    title: id,
    position: { x: 100, y: 200 },
    size: { width: 300, height: 250 },
    minSize: { width: 200, height: 150 },
    zIndex: 1000,
    isMinimized: false,
    isMaximized: false,
    isVisible: true,
    ...overrides,
  };
}

describe('panelMinimizeDock', () => {
  it('computeMinimizedDockPosition places bars along the bottom edge', () => {
    const viewportWidth = 1280;
    const viewportHeight = 800;

    expect(computeMinimizedDockPosition(0, viewportWidth, viewportHeight)).toEqual({
      x: MINIMIZED_DOCK_PADDING,
      y: viewportHeight - MINIMIZED_BAR_HEIGHT - MINIMIZED_DOCK_PADDING,
    });

    expect(computeMinimizedDockPosition(1, viewportWidth, viewportHeight).x).toBe(
      MINIMIZED_DOCK_PADDING + MINIMIZED_BAR_WIDTH + 8
    );
  });

  it('getMinimizedPanelIds returns visible minimized panels in stable order', () => {
    const panels = {
      zPanel: panelFixture('zPanel', { isMinimized: true }),
      aPanel: panelFixture('aPanel', { isMinimized: true }),
      openPanel: panelFixture('openPanel'),
      hiddenPanel: panelFixture('hiddenPanel', { isMinimized: true, isVisible: false }),
    };

    expect(getMinimizedPanelIds(panels)).toEqual(['aPanel', 'zPanel']);
  });

  it('preparePanelForMinimize saves layout snapshot', () => {
    const panel = panelFixture('chatHistory', { position: { x: 40, y: 80 }, size: { width: 420, height: 360 } });
    const minimized = preparePanelForMinimize(panel);

    expect(minimized.isMinimized).toBe(true);
    expect(minimized.preMinimizePosition).toEqual({ x: 40, y: 80 });
    expect(minimized.preMinimizeSize).toEqual({ width: 420, height: 360 });
  });

  it('preparePanelForRestore returns saved layout and clears snapshot fields', () => {
    const minimized = preparePanelForMinimize(panelFixture('chatHistory'));
    minimized.position = { x: 8, y: 752 };

    const restored = preparePanelForRestore(minimized);

    expect(restored.isMinimized).toBe(false);
    expect(restored.position).toEqual({ x: 100, y: 200 });
    expect(restored.size).toEqual({ width: 300, height: 250 });
    expect(restored.preMinimizePosition).toBeUndefined();
    expect(restored.preMinimizeSize).toBeUndefined();
  });

  it('relayoutMinimizedDock assigns dock slots to all minimized panels', () => {
    const panels = {
      chatHistory: panelFixture('chatHistory', { isMinimized: true }),
      gameInfo: panelFixture('gameInfo', { isMinimized: true }),
      commandInput: panelFixture('commandInput'),
    };

    const docked = relayoutMinimizedDock(panels, 1280, 800);

    expect(docked.chatHistory.position).toEqual(computeMinimizedDockPosition(0, 1280, 800));
    expect(docked.gameInfo.position).toEqual(computeMinimizedDockPosition(1, 1280, 800));
    expect(docked.commandInput.position).toEqual(panels.commandInput.position);
  });
});
