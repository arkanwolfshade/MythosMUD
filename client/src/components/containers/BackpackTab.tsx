/**
 * BackpackTab component for wearable container access.
 *
 * As documented in the restricted archives of Miskatonic University, backpack
 * tab components provide quick access to wearable containers (backpacks, bandoliers, etc.)
 * within the inventory interface.
 */

import React, { useMemo } from 'react';
import type { ContainerComponent } from '../../stores/containerStore';
import { useContainerStore } from '../../stores/containerStore';
import { useGameStore } from '../../stores/gameStore';
import { EldritchIcon, MythosIcons } from '../ui/EldritchIcon';

export interface BackpackTabProps {
  /** Callback when container is selected */
  onSelect?: (containerId: string | null) => void;
  /** Custom class name */
  className?: string;
}

/**
 * BackpackTab component displays tabs/pills for wearable containers.
 *
 * Features:
 * - Shows all wearable containers (backpacks, bandoliers, etc.)
 * - Displays item count and capacity
 * - Highlights selected container
 * - Keyboard accessible
 */
export const BackpackTab: React.FC<BackpackTabProps> = ({ onSelect, className = '' }) => {
  const getWearableContainers = useContainerStore(state => state.getWearableContainersForPlayer);
  const selectContainer = useContainerStore(state => state.selectContainer);
  const deselectContainer = useContainerStore(state => state.deselectContainer);
  const selectedContainerId = useContainerStore(state => state.selectedContainerId);
  const player = useGameStore(state => state.player);

  const wearableContainers = useMemo(() => {
    if (!player?.id) {
      return [];
    }
    // Player ID is a string in the gameStore
    return getWearableContainers(player.id as string);
  }, [player?.id, getWearableContainers]);

  // Don't render if no wearable containers
  if (wearableContainers.length === 0) {
    return null;
  }

  const handleTabClick = (containerId: string) => {
    if (selectedContainerId === containerId) {
      // Deselecting: call deselectContainer instead of selectContainer(null)
      deselectContainer();
      onSelect?.(null);
    } else {
      // Selecting: call selectContainer with the container ID
      selectContainer(containerId);
      onSelect?.(containerId);
    }
  };

  const handleKeyDown = (e: React.KeyboardEvent, containerId: string, index: number) => {
    if (e.key === 'Enter' || e.key === ' ') {
      e.preventDefault();
      handleTabClick(containerId);
      return;
    }

    // Arrow key navigation
    if (e.key === 'ArrowRight' || e.key === 'ArrowLeft') {
      e.preventDefault();
      const tabs = document.querySelectorAll('[role="tab"]');
      const currentIndex = index;
      let nextIndex: number;

      if (e.key === 'ArrowRight') {
        nextIndex = currentIndex < tabs.length - 1 ? currentIndex + 1 : 0; // Wrap to first
      } else {
        nextIndex = currentIndex > 0 ? currentIndex - 1 : tabs.length - 1; // Wrap to last
      }

      const nextTab = tabs[nextIndex] as HTMLElement;
      nextTab.focus();
    }
  };

  const getContainerDisplayName = (container: ContainerComponent): string => {
    const itemName = container.metadata.item_name as string | undefined;
    const itemId = container.metadata.item_id as string | undefined;
    return itemName || itemId || 'Container';
  };

  return (
    <div className={`flex flex-wrap gap-2 ${className}`} role="tablist" aria-label="Wearable containers">
      {wearableContainers.map(container => {
        const isSelected = selectedContainerId === container.container_id;
        const displayName = getContainerDisplayName(container);
        const itemCount = container.items.length;
        const capacity = container.capacity_slots;

        return (
          <button
            key={container.container_id}
            role="tab"
            aria-selected={isSelected}
            aria-label={`${displayName} container, ${itemCount} of ${capacity} items`}
            onClick={() => {
              handleTabClick(container.container_id);
            }}
            onKeyDown={e => {
              handleKeyDown(e, container.container_id, wearableContainers.indexOf(container));
            }}
            className={`
              flex items-center gap-2 px-3 py-2 rounded border font-mono text-sm
              transition-eldritch duration-eldritch ease-eldritch
              focus:outline-hidden focus:ring-2 focus:ring-offset-2 focus:ring-mythos-terminal-primary
              ${
                isSelected
                  ? 'bg-mythos-terminal-primary text-mythos-terminal-background border-mythos-terminal-primary hover:bg-mythos-terminal-primary/90'
                  : 'bg-mythos-terminal-surface text-mythos-terminal-text border-mythos-terminal-border hover:bg-mythos-terminal-hover hover:border-mythos-terminal-primary'
              }
            `}
          >
            <EldritchIcon name={MythosIcons.inventory} size={16} variant={isSelected ? 'secondary' : 'primary'} />
            <span className="font-semibold">{displayName}</span>
            <span className="text-xs opacity-75">
              ({itemCount}/{capacity})
            </span>
          </button>
        );
      })}
    </div>
  );
};
