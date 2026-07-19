/**
 * Bottom dock tray for minimized panels (issue #170).
 * Pure helpers: stack title bars along the bottom edge and restore prior layout on expand.
 */

import type { PanelPosition, PanelSize, PanelState } from '../types';

export const MINIMIZED_BAR_WIDTH = 200;
export const MINIMIZED_BAR_HEIGHT = 40;
export const MINIMIZED_DOCK_PADDING = 8;
export const MINIMIZED_DOCK_GAP = 8;

export function getDefaultViewport(): { width: number; height: number } {
  if (typeof window !== 'undefined') {
    return { width: window.innerWidth, height: window.innerHeight };
  }
  return { width: 1920, height: 1080 };
}

/** Stable left-to-right order for minimized panels in the dock tray. */
export function getMinimizedPanelIds(panels: Record<string, PanelState>): string[] {
  return Object.values(panels)
    .filter(p => p.isMinimized && p.isVisible)
    .sort((a, b) => a.id.localeCompare(b.id))
    .map(p => p.id);
}

export function computeMinimizedDockPosition(
  slotIndex: number,
  viewportWidth: number,
  viewportHeight: number
): PanelPosition {
  const x = MINIMIZED_DOCK_PADDING + slotIndex * (MINIMIZED_BAR_WIDTH + MINIMIZED_DOCK_GAP);
  const y = viewportHeight - MINIMIZED_BAR_HEIGHT - MINIMIZED_DOCK_PADDING;
  const maxX = Math.max(MINIMIZED_DOCK_PADDING, viewportWidth - MINIMIZED_BAR_WIDTH - MINIMIZED_DOCK_PADDING);
  return { x: Math.min(x, maxX), y };
}

export function relayoutMinimizedDock(
  panels: Record<string, PanelState>,
  viewportWidth: number,
  viewportHeight: number
): Record<string, PanelState> {
  const minimizedIds = getMinimizedPanelIds(panels);
  const next = { ...panels };
  minimizedIds.forEach((panelId, index) => {
    const panel = next[panelId];
    if (panel) {
      next[panelId] = {
        ...panel,
        position: computeMinimizedDockPosition(index, viewportWidth, viewportHeight),
      };
    }
  });
  return next;
}

export function preparePanelForMinimize(panel: PanelState): PanelState {
  return {
    ...panel,
    isMinimized: true,
    isMaximized: false,
    preMinimizePosition: panel.preMinimizePosition ?? { ...panel.position },
    preMinimizeSize: panel.preMinimizeSize ?? { ...panel.size },
  };
}

export function preparePanelForRestore(panel: PanelState): PanelState {
  const position: PanelPosition = panel.preMinimizePosition ?? panel.position;
  const size: PanelSize = panel.preMinimizeSize ?? panel.size;
  return {
    ...panel,
    isMinimized: false,
    isMaximized: false,
    position,
    size,
    preMinimizePosition: undefined,
    preMinimizeSize: undefined,
  };
}
