import React from 'react';

import type { PanelState } from '../types';
import { PanelManagerContext } from './PanelManagerContext';
import { usePanelManagerProviderState } from './usePanelManagerProviderState';

interface PanelManagerProviderProps {
  children: React.ReactNode;
  defaultPanels: Record<string, PanelState>;
}

export const PanelManagerProvider: React.FC<PanelManagerProviderProps> = ({ children, defaultPanels }) => {
  const value = usePanelManagerProviderState(defaultPanels);
  return <PanelManagerContext.Provider value={value}>{children}</PanelManagerContext.Provider>;
};
