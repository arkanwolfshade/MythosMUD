import React, { useCallback, useEffect, useMemo, useReducer } from 'react';
import type { PanelPosition, PanelSize, PanelState } from '../types';
import { PanelManagerContext } from './PanelManagerContext';

// Panel manager state and actions
// Implementing centralized panel state management using useReducer pattern
// Based on findings from "State Management in Non-Euclidean Interfaces" - Dr. Armitage, 1928

interface PanelManagerState {
  panels: Record<string, PanelState>;
  focusedPanelId: string | null;
  nextZIndex: number;
}

type PanelAction =
  | { type: 'INIT_PANELS'; payload: Record<string, PanelState> }
  | { type: 'UPDATE_POSITION'; payload: { id: string; position: PanelPosition } }
  | { type: 'UPDATE_SIZE'; payload: { id: string; size: PanelSize } }
  | { type: 'TOGGLE_MINIMIZE'; payload: { id: string } }
  | { type: 'TOGGLE_MAXIMIZE'; payload: { id: string } }
  | { type: 'SET_VISIBILITY'; payload: { id: string; isVisible: boolean } }
  | { type: 'FOCUS_PANEL'; payload: { id: string } }
  | { type: 'CLOSE_PANEL'; payload: { id: string } }
  | {
      type: 'SCALE_TO_VIEWPORT';
      payload: {
        viewportWidth: number;
        viewportHeight: number;
        scaleFunction: (width: number, height: number) => Record<string, PanelState>;
      };
    };

const STORAGE_KEY = 'mythosmud-ui-v2-panel-layout';

// Load panel layout from localStorage
const loadPanelLayout = (): Record<string, PanelState> | null => {
  try {
    const stored = localStorage.getItem(STORAGE_KEY);
    if (stored) {
      return JSON.parse(stored);
    }
  } catch (error) {
    console.warn('Failed to load panel layout from localStorage', error);
  }
  return null;
};

// Stored layout may be from a different resolution (e.g. another machine). Use it only if it fits.
const storedLayoutFitsViewport = (
  panels: Record<string, PanelState>,
  viewportWidth: number,
  viewportHeight: number
): boolean => {
  const padding = 40;
  const maxRight = viewportWidth - padding;
  const maxBottom = viewportHeight - padding;
  return Object.values(panels).every(
    p =>
      p.position.x >= -padding &&
      p.position.y >= 0 &&
      p.position.x + p.size.width <= maxRight &&
      p.position.y + p.size.height <= maxBottom
  );
};

// Save panel layout to localStorage
const savePanelLayout = (panels: Record<string, PanelState>): void => {
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(panels));
  } catch (error) {
    console.warn('Failed to save panel layout to localStorage', error);
  }
};

// Panel reducer
const panelReducer = (state: PanelManagerState, action: PanelAction): PanelManagerState => {
  switch (action.type) {
    case 'INIT_PANELS': {
      return {
        ...state,
        panels: action.payload,
        nextZIndex: Math.max(...Object.values(action.payload).map(p => p.zIndex), 1000) + 1,
      };
    }

    case 'UPDATE_POSITION': {
      const { id, position } = action.payload;
      const panel = state.panels[id];
      if (!panel) return state;

      const updatedPanels = {
        ...state.panels,
        [id]: { ...panel, position },
      };

      savePanelLayout(updatedPanels);
      return {
        ...state,
        panels: updatedPanels,
      };
    }

    case 'UPDATE_SIZE': {
      const { id, size } = action.payload;
      const panel = state.panels[id];
      if (!panel) return state;

      const updatedPanels = {
        ...state.panels,
        [id]: { ...panel, size },
      };

      savePanelLayout(updatedPanels);
      return {
        ...state,
        panels: updatedPanels,
      };
    }

    case 'TOGGLE_MINIMIZE': {
      const { id } = action.payload;
      const panel = state.panels[id];
      if (!panel) return state;

      const updatedPanels = {
        ...state.panels,
        [id]: { ...panel, isMinimized: !panel.isMinimized, isMaximized: false },
      };

      savePanelLayout(updatedPanels);
      return {
        ...state,
        panels: updatedPanels,
      };
    }

    case 'TOGGLE_MAXIMIZE': {
      const { id } = action.payload;
      const panel = state.panels[id];
      if (!panel) return state;

      // If maximizing, minimize all other panels first
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
      return {
        ...state,
        panels: updatedPanels,
      };
    }

    case 'SET_VISIBILITY': {
      const { id, isVisible } = action.payload;
      const panel = state.panels[id];
      if (!panel) return state;

      const updatedPanels = {
        ...state.panels,
        [id]: { ...panel, isVisible },
      };

      savePanelLayout(updatedPanels);
      return {
        ...state,
        panels: updatedPanels,
      };
    }

    case 'FOCUS_PANEL': {
      const { id } = action.payload;
      const panel = state.panels[id];
      if (!panel) return state;

      // Bring focused panel to front
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

    case 'CLOSE_PANEL': {
      const { id } = action.payload;

      // Destructuring removes panel id from state, _removed variable intentionally unused
      // eslint-disable-next-line @typescript-eslint/no-unused-vars
      const { [id]: _removed, ...remainingPanels } = state.panels;

      savePanelLayout(remainingPanels);
      return {
        ...state,
        panels: remainingPanels,
        focusedPanelId: state.focusedPanelId === id ? null : state.focusedPanelId,
      };
    }

    case 'SCALE_TO_VIEWPORT': {
      const { viewportWidth, viewportHeight, scaleFunction } = action.payload;
      const newLayout = scaleFunction(viewportWidth, viewportHeight);
      const updatedPanels = { ...state.panels };
      const headerHeight = 48;
      const padding = 20;

      // Update panel positions and sizes based on new layout
      // Only update if panel exists in new layout and isn't minimized/maximized
      Object.keys(newLayout).forEach(panelId => {
        const newPanel = newLayout[panelId];
        const currentPanel = updatedPanels[panelId];

        if (currentPanel && !currentPanel.isMinimized && !currentPanel.isMaximized) {
          // Ensure panel fits within viewport bounds
          // Position must be within viewport
          const constrainedPosition = {
            x: Math.max(0, Math.min(newPanel.position.x, viewportWidth - padding)),
            y: Math.max(headerHeight, Math.min(newPanel.position.y, viewportHeight - padding)),
          };

          // Calculate maximum size that fits in viewport
          const maxWidth = viewportWidth - constrainedPosition.x - padding;
          const maxHeight = viewportHeight - constrainedPosition.y - padding;

          // Use the smaller of: new size, maximum fit size, or minimum size
          // Allow panels to be smaller than minimum if viewport is too small
          const constrainedSize = {
            width: Math.max(
              Math.min(newPanel.size.width, maxWidth),
              Math.min(currentPanel.minSize?.width || 200, maxWidth)
            ),
            height: Math.max(
              Math.min(newPanel.size.height, maxHeight),
              Math.min(currentPanel.minSize?.height || 150, maxHeight)
            ),
          };

          updatedPanels[panelId] = {
            ...currentPanel,
            position: constrainedPosition,
            size: constrainedSize,
          };
        }
      });

      savePanelLayout(updatedPanels);
      return {
        ...state,
        panels: updatedPanels,
      };
    }

    default:
      return state;
  }
};

interface PanelManagerProviderProps {
  children: React.ReactNode;
  defaultPanels: Record<string, PanelState>;
}

export const PanelManagerProvider: React.FC<PanelManagerProviderProps> = ({ children, defaultPanels }) => {
  const [state, dispatch] = useReducer(panelReducer, {
    panels: {},
    focusedPanelId: null,
    nextZIndex: 1000,
  });

  // Initialize panels from localStorage or defaults. Ignore stored layout if it was saved on a
  // different resolution (e.g. another machine) so the network machine gets a valid layout.
  useEffect(() => {
    const stored = loadPanelLayout();
    const vw = typeof window !== 'undefined' ? window.innerWidth : 1920;
    const vh = typeof window !== 'undefined' ? window.innerHeight : 1080;
    const panelsToUse = stored && storedLayoutFitsViewport(stored, vw, vh) ? stored : defaultPanels;
    dispatch({ type: 'INIT_PANELS', payload: panelsToUse });
  }, [defaultPanels]);

  const updatePosition = useCallback((id: string, position: PanelPosition) => {
    dispatch({ type: 'UPDATE_POSITION', payload: { id, position } });
  }, []);

  const updateSize = useCallback((id: string, size: PanelSize) => {
    dispatch({ type: 'UPDATE_SIZE', payload: { id, size } });
  }, []);

  const toggleMinimize = useCallback((id: string) => {
    dispatch({ type: 'TOGGLE_MINIMIZE', payload: { id } });
  }, []);

  const toggleMaximize = useCallback((id: string) => {
    dispatch({ type: 'TOGGLE_MAXIMIZE', payload: { id } });
  }, []);

  const setVisibility = useCallback((id: string, isVisible: boolean) => {
    dispatch({ type: 'SET_VISIBILITY', payload: { id, isVisible } });
  }, []);

  const focusPanel = useCallback((id: string) => {
    dispatch({ type: 'FOCUS_PANEL', payload: { id } });
  }, []);

  const closePanel = useCallback((id: string) => {
    dispatch({ type: 'CLOSE_PANEL', payload: { id } });
  }, []);

  const getPanel = useCallback(
    (id: string): PanelState | undefined => {
      return state.panels[id];
    },
    [state.panels]
  );

  const scalePanelsToViewport = useCallback(
    (
      viewportWidth: number,
      viewportHeight: number,
      scaleFunction: (width: number, height: number) => Record<string, PanelState>
    ) => {
      dispatch({
        type: 'SCALE_TO_VIEWPORT',
        payload: { viewportWidth, viewportHeight, scaleFunction },
      });
    },
    []
  );

  const value = useMemo(
    () => ({
      panels: state.panels,
      updatePosition,
      updateSize,
      toggleMinimize,
      toggleMaximize,
      setVisibility,
      focusPanel,
      closePanel,
      getPanel,
      scalePanelsToViewport,
    }),
    [
      state.panels,
      updatePosition,
      updateSize,
      toggleMinimize,
      toggleMaximize,
      setVisibility,
      focusPanel,
      closePanel,
      getPanel,
      scalePanelsToViewport,
    ]
  );

  return <PanelManagerContext.Provider value={value}>{children}</PanelManagerContext.Provider>;
};
