import React, { useCallback, useEffect, useMemo, useReducer } from 'react';

import type { PanelPosition, PanelSize, PanelState } from '../types';
import { PanelManagerContext } from './PanelManagerContext';
import { loadPanelLayout } from './panelLayoutValidation';
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
} from './panelReducerHandlers';

// Panel manager state and actions
// Implementing centralized panel state management using useReducer pattern
// Based on findings from "State Management in Non-Euclidean Interfaces" - Dr. Armitage, 1928

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

type PanelReducerHandler = (state: PanelManagerState, payload: unknown) => PanelManagerState;

const panelActionHandlers: Record<PanelAction['type'], PanelReducerHandler> = {
  INIT_PANELS: handleInitPanels as PanelReducerHandler,
  UPDATE_POSITION: handleUpdatePosition as PanelReducerHandler,
  UPDATE_SIZE: handleUpdateSize as PanelReducerHandler,
  TOGGLE_MINIMIZE: handleToggleMinimize as PanelReducerHandler,
  TOGGLE_MAXIMIZE: handleToggleMaximize as PanelReducerHandler,
  SET_VISIBILITY: handleSetVisibility as PanelReducerHandler,
  FOCUS_PANEL: handleFocusPanel as PanelReducerHandler,
  CLOSE_PANEL: handleClosePanel as PanelReducerHandler,
  SCALE_TO_VIEWPORT: handleScaleToViewport as PanelReducerHandler,
};

function panelReducer(state: PanelManagerState, action: PanelAction): PanelManagerState {
  const handler = panelActionHandlers[action.type];
  return handler(state, action.payload);
}

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
