import { useCallback, useEffect, useMemo, useReducer } from 'react';

import type { PanelPosition, PanelSize, PanelState } from '../types';
import type { PanelManagerContextValue } from './PanelManagerContext';
import { resolveInitialPanelLayout } from './panelLayoutBootstrap';
import { panelReducer } from './panelManagerReducer';

export function usePanelManagerProviderState(defaultPanels: Record<string, PanelState>): PanelManagerContextValue {
  const [state, dispatch] = useReducer(panelReducer, {
    panels: {},
    focusedPanelId: null,
    nextZIndex: 1000,
  });

  useEffect(() => {
    const vw = typeof window !== 'undefined' ? window.innerWidth : 1920;
    const vh = typeof window !== 'undefined' ? window.innerHeight : 1080;
    const panelsToUse = resolveInitialPanelLayout(defaultPanels, vw, vh);
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

  const getPanel = useCallback((id: string): PanelState | undefined => state.panels[id], [state.panels]);

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

  return useMemo(
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
}
