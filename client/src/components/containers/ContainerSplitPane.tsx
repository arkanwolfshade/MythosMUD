/**
 * Container Split-Pane component for unified container system.
 *
 * As documented in the restricted archives of Miskatonic University, container
 * split-pane components provide a dual-view interface for managing investigator
 * artifacts between containers and personal inventory.
 */

import React, { useCallback, useEffect, useMemo, useRef, useState } from 'react';
import type { InventoryStack } from '../../stores/containerStore';
import { useContainerStore } from '../../stores/containerStore';
import { useGameStore } from '../../stores/gameStore';
import { MythosPanel } from '../ui/MythosPanel';
import { TerminalButton } from '../ui/TerminalButton';

export interface ContainerSplitPaneProps {
  /** Container ID to display */
  containerId: string;
  /** Callback when item transfer is initiated */
  onTransfer?: (direction: 'to_container' | 'from_container', item: InventoryStack, quantity?: number) => void;
  /** Callback when container is closed */
  onClose?: () => void;
  /** Whether container is in modal mode (traps focus) */
  modal?: boolean;
  /** Custom class name */
  className?: string;
}

/**
 * ContainerSplitPane component displays a split view of container and player inventory.
 *
 * Features:
 * - Side-by-side display of container and player inventory
 * - Item transfer buttons
 * - Keyboard accessibility
 * - Loading and error states
 */
export const ContainerSplitPane: React.FC<ContainerSplitPaneProps> = ({
  containerId,
  onTransfer,
  onClose,
  modal = false,
  className = '',
}) => {
  const container = useContainerStore(state => state.getContainer(containerId));
  const mutationToken = useContainerStore(state => state.getMutationToken(containerId));
  const isContainerOpen = useContainerStore(state => state.isContainerOpen(containerId));
  const isLoading = useContainerStore(state => state.isLoading);
  const player = useGameStore(state => state.player);

  const playerInventory = useMemo(() => {
    // Type assertion: player.inventory may have a different type definition in gameStore,
    // but at runtime it should be InventoryStack[] based on how the component uses it.
    return (player?.inventory as unknown as InventoryStack[]) || [];
  }, [player?.inventory]);

  // All hooks must be called before any early returns
  const containerRef = useRef<HTMLDivElement>(null);
  const firstButtonRef = useRef<HTMLButtonElement>(null);
  const [draggedItem, setDraggedItem] = useState<InventoryStack | null>(null);
  const [dragSource, setDragSource] = useState<'container' | 'player' | null>(null);
  const [dragOverTarget, setDragOverTarget] = useState<'container' | 'player' | null>(null);

  // Focus management
  useEffect(() => {
    if (container && isContainerOpen && firstButtonRef.current) {
      // Focus first interactive element when container opens
      firstButtonRef.current.focus();
    }
  }, [container, isContainerOpen]);

  // Keyboard event handlers - must be before early returns
  const handleKeyDown = useCallback(
    (e: React.KeyboardEvent) => {
      if (e.key === 'Escape' && onClose) {
        e.preventDefault();
        e.stopPropagation();
        onClose();
        return;
      }

      // Focus trap for modal mode
      if (modal && e.key === 'Tab') {
        const focusableElements = containerRef.current?.querySelectorAll(
          'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
        );
        if (!focusableElements || focusableElements.length === 0) return;

        const firstElement = focusableElements[0] as HTMLElement;
        const lastElement = focusableElements[focusableElements.length - 1] as HTMLElement;

        if (e.shiftKey) {
          // Shift + Tab
          if (document.activeElement === firstElement) {
            e.preventDefault();
            lastElement.focus();
          }
        } else {
          // Tab
          if (document.activeElement === lastElement) {
            e.preventDefault();
            firstElement.focus();
          }
        }
      }
    },
    [modal, onClose]
  );

  // Drag and drop handlers - must be before early returns
  const handleDragStart = useCallback(
    (e: React.DragEvent, item: InventoryStack, source: 'container' | 'player') => {
      if (!mutationToken || !onTransfer) {
        e.preventDefault();
        return;
      }

      setDraggedItem(item);
      setDragSource(source);

      // Store item data in drag event
      if (e.dataTransfer) {
        e.dataTransfer.effectAllowed = 'move';
        e.dataTransfer.setData('application/json', JSON.stringify({ item, source }));
      }
    },
    [mutationToken, onTransfer]
  );

  const handleDragEnd = useCallback(() => {
    setDraggedItem(null);
    setDragSource(null);
    setDragOverTarget(null);
  }, []);

  const handleDragOver = useCallback(
    (e: React.DragEvent, target: 'container' | 'player') => {
      if (!draggedItem || !dragSource) {
        return;
      }

      // Only allow drop if dragging to different area
      if (dragSource === target) {
        return;
      }

      e.preventDefault();
      e.stopPropagation();

      if (e.dataTransfer) {
        e.dataTransfer.dropEffect = 'move';
      }

      setDragOverTarget(target);
    },
    [draggedItem, dragSource]
  );

  const handleDragLeave = useCallback(() => {
    setDragOverTarget(null);
  }, []);

  const handleDrop = useCallback(
    (e: React.DragEvent, target: 'container' | 'player') => {
      e.preventDefault();
      e.stopPropagation();

      if (!draggedItem || !dragSource || !mutationToken || !onTransfer) {
        return;
      }

      // Only allow drop if dragging to different area
      if (dragSource === target) {
        setDragOverTarget(null);
        return;
      }

      // Determine transfer direction
      const direction = target === 'container' ? 'to_container' : 'from_container';
      onTransfer(direction, draggedItem);

      // Reset drag state
      setDraggedItem(null);
      setDragSource(null);
      setDragOverTarget(null);
    },
    [draggedItem, dragSource, mutationToken, onTransfer]
  );

  // Error states - early returns after all hooks
  if (isLoading) {
    return (
      <MythosPanel className={className}>
        <div className="p-4 text-center text-mythos-terminal-text">Loading container...</div>
      </MythosPanel>
    );
  }

  if (!container) {
    return (
      <MythosPanel className={className}>
        <div className="p-4 text-center text-mythos-terminal-text text-mythos-error">Container not found</div>
      </MythosPanel>
    );
  }

  if (!isContainerOpen) {
    return (
      <MythosPanel className={className}>
        <div className="p-4 text-center text-mythos-terminal-text text-mythos-error">Container is not open</div>
      </MythosPanel>
    );
  }

  // Handler functions
  const handleTransferToContainer = (item: InventoryStack, quantity?: number) => {
    if (onTransfer && mutationToken) {
      onTransfer('to_container', item, quantity);
    }
  };

  const handleTransferFromContainer = (item: InventoryStack, quantity?: number) => {
    if (onTransfer && mutationToken) {
      onTransfer('from_container', item, quantity);
    }
  };

  const renderItem = (item: InventoryStack, isContainerItem: boolean) => {
    const handleTransfer = isContainerItem ? handleTransferFromContainer : handleTransferToContainer;
    const canTransfer = !!mutationToken && !!onTransfer;
    const isDragging = draggedItem?.item_instance_id === item.item_instance_id;
    const itemLabel =
      `${item.item_name}, ${item.quantity} ${item.quantity === 1 ? 'item' : 'items'}. ` + 'Drag to transfer.';

    return (
      <div
        key={item.item_instance_id}
        className={
          `flex items-center justify-between p-2 border-b border-mythos-terminal-border ` +
          `hover:bg-mythos-terminal-hover ${isDragging ? 'opacity-50' : ''}`
        }
        role="listitem"
        tabIndex={0}
        draggable={canTransfer}
        onDragStart={e => canTransfer && handleDragStart(e, item, isContainerItem ? 'container' : 'player')}
        onDragEnd={handleDragEnd}
        aria-label={itemLabel}
      >
        <div className="flex-1">
          <div className="font-semibold text-mythos-terminal-text">{item.item_name}</div>
          {item.quantity > 1 && (
            <div className="text-sm text-mythos-terminal-text-secondary">Quantity: {item.quantity}</div>
          )}
        </div>
        {canTransfer && (
          <TerminalButton
            ref={
              isContainerItem && container.items.indexOf(item) === 0
                ? firstButtonRef
                : !isContainerItem && container.items.length === 0 && playerInventory.indexOf(item) === 0
                  ? firstButtonRef
                  : undefined
            }
            onClick={() => {
              handleTransfer(item);
            }}
            disabled={!mutationToken}
            className="ml-2"
            aria-label={`Transfer ${item.item_name} ${isContainerItem ? 'from' : 'to'} container`}
            onKeyDown={e => {
              if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                handleTransfer(item);
              }
            }}
          >
            Transfer
          </TerminalButton>
        )}
      </div>
    );
  };

  return (
    <MythosPanel className={`flex flex-col ${className}`}>
      <div
        ref={containerRef}
        className="flex-1 grid grid-cols-2 gap-4 p-4"
        onKeyDown={handleKeyDown}
        role="region"
        aria-label={`Container: ${container.metadata?.item_name || container.source_type}`}
        tabIndex={-1}
      >
        {/* Container Side */}
        <div
          className={`flex flex-col border-r border-mythos-terminal-border pr-4 ${
            dragOverTarget === 'container' ? 'bg-mythos-terminal-primary/10 border-mythos-terminal-primary' : ''
          }`}
          aria-label="Container inventory"
          onDragOver={e => {
            handleDragOver(e, 'container');
          }}
          onDragLeave={handleDragLeave}
          onDrop={e => {
            handleDrop(e, 'container');
          }}
        >
          <h3 className="text-lg font-bold text-mythos-terminal-text mb-2">
            Container ({container.items.length}/{container.capacity_slots})
          </h3>
          <div className="flex-1 overflow-y-auto" role="list">
            {container.items.length === 0 ? (
              <div className="text-center text-mythos-terminal-text-secondary py-8">Container is empty</div>
            ) : (
              container.items.map(item => renderItem(item, true))
            )}
          </div>
        </div>

        {/* Player Inventory Side */}
        <div
          className={`flex flex-col pl-4 ${
            dragOverTarget === 'player' ? 'bg-mythos-terminal-primary/10 border-mythos-terminal-primary' : ''
          }`}
          aria-label="Player inventory"
          onDragOver={e => {
            handleDragOver(e, 'player');
          }}
          onDragLeave={handleDragLeave}
          onDrop={e => {
            handleDrop(e, 'player');
          }}
        >
          <h3 className="text-lg font-bold text-mythos-terminal-text mb-2">Inventory ({playerInventory.length}/20)</h3>
          <div className="flex-1 overflow-y-auto" role="list">
            {playerInventory.length === 0 ? (
              <div className="text-center text-mythos-terminal-text-secondary py-8">Inventory is empty</div>
            ) : (
              playerInventory.map(item => renderItem(item, false))
            )}
          </div>
        </div>
      </div>

      {/* Close Button */}
      {onClose && (
        <div className="p-4 border-t border-mythos-terminal-border">
          <TerminalButton onClick={onClose} className="w-full" aria-label="Close container">
            Close
          </TerminalButton>
        </div>
      )}
    </MythosPanel>
  );
};
