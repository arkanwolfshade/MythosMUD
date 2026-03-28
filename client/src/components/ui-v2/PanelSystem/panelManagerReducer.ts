import type { PanelPosition, PanelSize, PanelState } from '../types';
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

export type PanelAction =
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

export function panelReducer(state: PanelManagerState, action: PanelAction): PanelManagerState {
  const handler = panelActionHandlers[action.type];
  return handler(state, action.payload);
}
