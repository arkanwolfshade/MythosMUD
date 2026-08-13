import React from 'react';
import type { PanelContainerProps } from './PanelContainerShared';
import { ExpandedPanelRnd, MinimizedPanelRnd } from './PanelContainerViews';
import { usePanelContainerBody } from './usePanelContainerBody';

export type { PanelContainerProps } from './PanelContainerShared';

function PanelContainerBody(props: PanelContainerProps): React.ReactElement {
  const { isMinimized, rndProps } = usePanelContainerBody(props);
  return isMinimized ? <MinimizedPanelRnd {...rndProps} /> : <ExpandedPanelRnd {...rndProps} />;
}

export const PanelContainer: React.FC<PanelContainerProps> = React.memo(PanelContainerBody);

PanelContainer.displayName = 'PanelContainer';
