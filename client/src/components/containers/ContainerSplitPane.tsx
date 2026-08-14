/**
 * Container Split-Pane component for unified container system.
 */

import React from 'react';
import type { InventoryStack } from '../../stores/containerStore';
import { MythosPanel } from '../ui/MythosPanel';
import { ContainerSplitPaneView } from './ContainerSplitPaneView';
import { useContainerSplitPane } from './useContainerSplitPane';

export interface ContainerSplitPaneProps {
  containerId: string;
  onTransfer?: (direction: 'to_container' | 'from_container', item: InventoryStack, quantity?: number) => void;
  onClose?: () => void;
  modal?: boolean;
  className?: string;
}

export const ContainerSplitPane: React.FC<ContainerSplitPaneProps> = props => {
  const { onClose, modal = false, className = '' } = props;
  const vm = useContainerSplitPane(props);

  if (vm.isLoading) {
    return (
      <MythosPanel className={className}>
        <div className="p-4 text-center text-mythos-terminal-text">Loading container...</div>
      </MythosPanel>
    );
  }

  if (!vm.container) {
    return (
      <MythosPanel className={className}>
        <div className="p-4 text-center text-mythos-terminal-text text-mythos-error">Container not found</div>
      </MythosPanel>
    );
  }

  if (!vm.isContainerOpen) {
    return (
      <MythosPanel className={className}>
        <div className="p-4 text-center text-mythos-terminal-text text-mythos-error">Container is not open</div>
      </MythosPanel>
    );
  }

  return (
    <ContainerSplitPaneView
      vm={vm}
      container={vm.container}
      modal={modal}
      className={className}
      onClose={onClose}
      hasTransfer={!!props.onTransfer && !!vm.mutationToken}
    />
  );
};
