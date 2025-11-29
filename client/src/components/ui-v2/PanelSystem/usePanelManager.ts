import { useContext } from 'react';
import { PanelManagerContext, type PanelManagerContextValue } from './PanelManagerContext';

/**
 * Hook to access the panel manager context.
 *
 * Must be used within a PanelManagerProvider.
 */
export const usePanelManager = (): PanelManagerContextValue => {
  const context = useContext(PanelManagerContext);
  if (!context) {
    throw new Error('usePanelManager must be used within PanelManagerProvider');
  }
  return context;
};
