import React from 'react';

import { ExpandedPanelRnd } from './ExpandedPanelRnd';
import { MinimizedPanelRnd } from './MinimizedPanelRnd';
import { usePanelContainerView, type PanelContainerProps } from './usePanelContainerView';

// Implementing panel container with react-rnd for drag/resize functionality
// Based on findings from "Non-Euclidean UI Architecture" - Dr. Armitage, 1928
export const PanelContainer: React.FC<PanelContainerProps> = React.memo(props => {
  const view = usePanelContainerView(props);

  if (view.isMinimized) {
    return (
      <MinimizedPanelRnd
        id={view.id}
        title={view.title}
        displayPosition={view.displayPosition}
        zIndex={view.zIndex}
        opaque={view.opaque}
        className={view.className}
        onClose={view.onClose}
        layout={view.layout}
      >
        {view.children}
      </MinimizedPanelRnd>
    );
  }

  return (
    <ExpandedPanelRnd
      id={view.id}
      title={view.title}
      displayPosition={view.displayPosition}
      displaySize={view.displaySize}
      zIndex={view.zIndex}
      isMaximized={view.isMaximized}
      opaque={view.opaque}
      className={view.className}
      minSize={view.minSize}
      maxSize={view.maxSize}
      minHeight={view.minHeight}
      onClose={view.onClose}
      onFocus={view.onFocus}
      layout={view.layout}
    >
      {view.children}
    </ExpandedPanelRnd>
  );
});

PanelContainer.displayName = 'PanelContainer';
