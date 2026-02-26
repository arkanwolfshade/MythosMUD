/**
 * Panel reducer case handlers. Extracted from PanelManager to keep cyclomatic complexity
 * of the reducer switch under the limit (each handler is a separate function).
 */

import type { PanelPosition, PanelSize, PanelState } from '../types';
import { savePanelLayout } from './panelLayoutValidation';

export interface PanelManagerState {
  panels: Record<string, PanelState>;
  focusedPanelId: string | null;
  nextZIndex: number;
}

export function handleInitPanels(state: PanelManagerState, payload: Record<string, PanelState>): PanelManagerState {
  const nextZIndex = Math.max(...Object.values(payload).map(p => p.zIndex), 1000) + 1;
  return { ...state, panels: payload, nextZIndex };
}

export function handleUpdatePosition(
  state: PanelManagerState,
  payload: { id: string; position: PanelPosition }
): PanelManagerState {
  const { id, position } = payload;
  const panel = state.panels[id];
  if (!panel) return state;
  const updatedPanels = { ...state.panels, [id]: { ...panel, position } };
  savePanelLayout(updatedPanels);
  return { ...state, panels: updatedPanels };
}

export function handleUpdateSize(
  state: PanelManagerState,
  payload: { id: string; size: PanelSize }
): PanelManagerState {
  const { id, size } = payload;
  const panel = state.panels[id];
  if (!panel) return state;
  const updatedPanels = { ...state.panels, [id]: { ...panel, size } };
  savePanelLayout(updatedPanels);
  return { ...state, panels: updatedPanels };
}

export function handleToggleMinimize(state: PanelManagerState, payload: { id: string }): PanelManagerState {
  const { id } = payload;
  const panel = state.panels[id];
  if (!panel) return state;
  const updatedPanels = {
    ...state.panels,
    [id]: { ...panel, isMinimized: !panel.isMinimized, isMaximized: false },
  };
  savePanelLayout(updatedPanels);
  return { ...state, panels: updatedPanels };
}

export function handleToggleMaximize(state: PanelManagerState, payload: { id: string }): PanelManagerState {
  const { id } = payload;
  const panel = state.panels[id];
  if (!panel) return state;
  const updatedPanels = { ...state.panels };
  if (!panel.isMaximized) {
    Object.keys(updatedPanels).forEach(panelId => {
      if (panelId !== id && updatedPanels[panelId].isMaximized) {
        updatedPanels[panelId] = { ...updatedPanels[panelId], isMaximized: false };
      }
    });
  }
  updatedPanels[id] = {
    ...panel,
    isMaximized: !panel.isMaximized,
    isMinimized: false,
  };
  savePanelLayout(updatedPanels);
  return { ...state, panels: updatedPanels };
}

export function handleSetVisibility(
  state: PanelManagerState,
  payload: { id: string; isVisible: boolean }
): PanelManagerState {
  const { id, isVisible } = payload;
  const panel = state.panels[id];
  if (!panel) return state;
  const updatedPanels = { ...state.panels, [id]: { ...panel, isVisible } };
  savePanelLayout(updatedPanels);
  return { ...state, panels: updatedPanels };
}

export function handleFocusPanel(state: PanelManagerState, payload: { id: string }): PanelManagerState {
  const { id } = payload;
  const panel = state.panels[id];
  if (!panel) return state;
  const updatedPanels = {
    ...state.panels,
    [id]: { ...panel, zIndex: state.nextZIndex },
  };
  return {
    ...state,
    panels: updatedPanels,
    focusedPanelId: id,
    nextZIndex: state.nextZIndex + 1,
  };
}

export function handleClosePanel(state: PanelManagerState, payload: { id: string }): PanelManagerState {
  const { id } = payload;
  // Destructuring removes panel id from state; _removed intentionally unused
  // eslint-disable-next-line @typescript-eslint/no-unused-vars
  const { [id]: _removed, ...remainingPanels } = state.panels;
  savePanelLayout(remainingPanels);
  return {
    ...state,
    panels: remainingPanels,
    focusedPanelId: state.focusedPanelId === id ? null : state.focusedPanelId,
  };
}

export function handleScaleToViewport(
  state: PanelManagerState,
  payload: {
    viewportWidth: number;
    viewportHeight: number;
    scaleFunction: (width: number, height: number) => Record<string, PanelState>;
  }
): PanelManagerState {
  const { viewportWidth, viewportHeight, scaleFunction } = payload;
  const newLayout = scaleFunction(viewportWidth, viewportHeight);
  const updatedPanels = { ...state.panels };
  const headerHeight = 48;
  const padding = 20;

  Object.keys(newLayout).forEach(panelId => {
    const newPanel = newLayout[panelId];
    const currentPanel = updatedPanels[panelId];
    if (!currentPanel || currentPanel.isMinimized || currentPanel.isMaximized) {
      return;
    }

    const constrainedPosition = {
      x: Math.max(0, Math.min(newPanel.position.x, viewportWidth - padding)),
      y: Math.max(headerHeight, Math.min(newPanel.position.y, viewportHeight - padding)),
    };
    const maxWidth = viewportWidth - constrainedPosition.x - padding;
    const maxHeight = viewportHeight - constrainedPosition.y - padding;

    const constrainedHeight = constrainPanelHeight(newPanel, currentPanel, maxHeight);
    const constrainedSize = {
      width: Math.max(Math.min(newPanel.size.width, maxWidth), Math.min(currentPanel.minSize?.width || 200, maxWidth)),
      height: constrainedHeight,
    };

    updatedPanels[panelId] = {
      ...currentPanel,
      position: constrainedPosition,
      size: constrainedSize,
    };
  });

  savePanelLayout(updatedPanels);
  return { ...state, panels: updatedPanels };
}

function constrainPanelHeight(newPanel: PanelState, currentPanel: PanelState, maxHeight: number): number {
  let h = Math.max(Math.min(newPanel.size.height, maxHeight), Math.min(currentPanel.minSize?.height || 150, maxHeight));
  const minH = newPanel.minHeight;
  if (minH != null && h < minH && maxHeight >= minH) {
    h = minH;
  }
  return h;
}
