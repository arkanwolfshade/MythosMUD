import { useContext } from 'react';
import { PanelContext, PanelContextType, PanelPosition, PanelSize, PanelState } from '../PanelContext';

// Hook to use panel context
export const usePanelContext = (): PanelContextType => {
  const context = useContext(PanelContext);
  if (!context) {
    throw new Error('usePanelContext must be used within a PanelProvider');
  }
  return context;
};

// Convenience hooks for specific panel operations
export const usePanel = (panelId: string) => {
  const { panels, updatePanel } = usePanelContext();
  const panel = panels[panelId];

  return {
    panel,
    updatePanel: (updates: Partial<PanelState>) => updatePanel(panelId, updates),
  };
};

export const usePanelActions = (panelId: string) => {
  const { togglePanelVisibility, togglePanelMinimized, togglePanelMaximized, movePanel, resizePanel, bringToFront } =
    usePanelContext();

  return {
    toggleVisibility: () => togglePanelVisibility(panelId),
    toggleMinimized: () => togglePanelMinimized(panelId),
    toggleMaximized: () => togglePanelMaximized(panelId),
    move: (position: PanelPosition) => movePanel(panelId, position),
    resize: (size: PanelSize) => resizePanel(panelId, size),
    bringToFront: () => bringToFront(panelId),
  };
};

export const usePanelLayout = () => {
  const { panels, resetPanelLayout } = usePanelContext();

  return {
    panels,
    resetLayout: resetPanelLayout,
  };
};
