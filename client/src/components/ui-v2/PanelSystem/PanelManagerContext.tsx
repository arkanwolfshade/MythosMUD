import { createContext } from 'react';
import type { PanelPosition, PanelSize, PanelState } from '../types';

export interface PanelManagerContextValue {
  panels: Record<string, PanelState>;
  updatePosition: (id: string, position: PanelPosition) => void;
  updateSize: (id: string, size: PanelSize) => void;
  toggleMinimize: (id: string) => void;
  toggleMaximize: (id: string) => void;
  setVisibility: (id: string, isVisible: boolean) => void;
  focusPanel: (id: string) => void;
  closePanel: (id: string) => void;
  getPanel: (id: string) => PanelState | undefined;
  scalePanelsToViewport: (
    viewportWidth: number,
    viewportHeight: number,
    scaleFunction: (width: number, height: number) => Record<string, PanelState>
  ) => void;
}

export const PanelManagerContext = createContext<PanelManagerContextValue | null>(null);
