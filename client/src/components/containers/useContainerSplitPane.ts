import { useCallback, useEffect, useMemo, useRef, useState } from 'react';
import { useShallow } from 'zustand/react/shallow';
import type { InventoryStack } from '../../stores/containerStore';
import { useContainerStore } from '../../stores/containerStore';
import { useGameStore } from '../../stores/gameStore';

export interface ContainerSplitPaneHookProps {
  containerId: string;
  onTransfer?: (direction: 'to_container' | 'from_container', item: InventoryStack, quantity?: number) => void;
  onClose?: () => void;
  modal?: boolean;
}

type DraggedItemSetter = React.Dispatch<React.SetStateAction<InventoryStack | null>>;
type DragSourceSetter = React.Dispatch<React.SetStateAction<'container' | 'player' | null>>;
type DragTargetSetter = React.Dispatch<React.SetStateAction<'container' | 'player' | null>>;

function createTransferHandlers(onTransfer: ContainerSplitPaneHookProps['onTransfer'], mutationToken: string | null) {
  const transfer = (direction: 'to_container' | 'from_container', item: InventoryStack, quantity?: number) => {
    if (onTransfer && mutationToken) onTransfer(direction, item, quantity);
  };

  return {
    handleTransferToContainer: (item: InventoryStack, quantity?: number) => transfer('to_container', item, quantity),
    handleTransferFromContainer: (item: InventoryStack, quantity?: number) =>
      transfer('from_container', item, quantity),
  };
}

function createKeyDownHandler(
  modal: boolean,
  onClose: ContainerSplitPaneHookProps['onClose'],
  containerRef: React.RefObject<HTMLDivElement | null>
) {
  return (e: React.KeyboardEvent): void => {
    if (e.key === 'Escape' && onClose) {
      e.preventDefault();
      e.stopPropagation();
      onClose();
      return;
    }
    if (modal && e.key === 'Tab') trapFocusInContainer(e, containerRef);
  };
}

const resetDragState = (
  setDraggedItem: DraggedItemSetter,
  setDragSource: DragSourceSetter,
  setDragOverTarget: DragTargetSetter
): void => {
  setDraggedItem(null);
  setDragSource(null);
  setDragOverTarget(null);
};

const handleDragStartEvent = (
  e: React.DragEvent,
  item: InventoryStack,
  source: 'container' | 'player',
  mutationToken: string | null,
  onTransfer: ContainerSplitPaneHookProps['onTransfer'],
  setDraggedItem: DraggedItemSetter,
  setDragSource: DragSourceSetter
): void => {
  if (!mutationToken || !onTransfer) {
    e.preventDefault();
    return;
  }
  setDraggedItem(item);
  setDragSource(source);
  if (e.dataTransfer) {
    e.dataTransfer.effectAllowed = 'move';
    e.dataTransfer.setData('application/json', JSON.stringify({ item, source }));
  }
};

const handleDropEvent = (
  e: React.DragEvent,
  target: 'container' | 'player',
  draggedItem: InventoryStack | null,
  dragSource: 'container' | 'player' | null,
  mutationToken: string | null,
  onTransfer: ContainerSplitPaneHookProps['onTransfer'],
  setDraggedItem: DraggedItemSetter,
  setDragSource: DragSourceSetter,
  setDragOverTarget: DragTargetSetter
): void => {
  e.preventDefault();
  e.stopPropagation();
  if (!draggedItem || !dragSource || !mutationToken || !onTransfer || dragSource === target) {
    setDragOverTarget(null);
    return;
  }
  onTransfer(target === 'container' ? 'to_container' : 'from_container', draggedItem);
  resetDragState(setDraggedItem, setDragSource, setDragOverTarget);
};

const trapFocusInContainer = (e: React.KeyboardEvent, containerRef: React.RefObject<HTMLDivElement | null>): void => {
  const focusableElements = containerRef.current?.querySelectorAll(
    'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
  );
  if (!focusableElements || focusableElements.length === 0) return;

  const firstElement = focusableElements[0] as HTMLElement;
  const lastElement = focusableElements[focusableElements.length - 1] as HTMLElement;

  if (e.shiftKey && document.activeElement === firstElement) {
    e.preventDefault();
    lastElement.focus();
    return;
  }
  if (!e.shiftKey && document.activeElement === lastElement) {
    e.preventDefault();
    firstElement.focus();
  }
};

const useContainerDragHandlers = (
  mutationToken: string | null,
  onTransfer: ContainerSplitPaneHookProps['onTransfer'],
  draggedItem: InventoryStack | null,
  dragSource: 'container' | 'player' | null,
  setDraggedItem: DraggedItemSetter,
  setDragSource: DragSourceSetter,
  setDragOverTarget: DragTargetSetter
): {
  handleDragStart: (e: React.DragEvent, item: InventoryStack, source: 'container' | 'player') => void;
  handleDragEnd: () => void;
  handleDragOver: (e: React.DragEvent, target: 'container' | 'player') => void;
  handleDragLeave: () => void;
  handleDrop: (e: React.DragEvent, target: 'container' | 'player') => void;
} => {
  const handleDragStart = useCallback(
    (e: React.DragEvent, item: InventoryStack, source: 'container' | 'player') =>
      handleDragStartEvent(e, item, source, mutationToken, onTransfer, setDraggedItem, setDragSource),
    [mutationToken, onTransfer, setDragSource, setDraggedItem]
  );

  const handleDragEnd = useCallback(
    () => resetDragState(setDraggedItem, setDragSource, setDragOverTarget),
    [setDragOverTarget, setDragSource, setDraggedItem]
  );

  const handleDragOver = useCallback(
    (e: React.DragEvent, target: 'container' | 'player') => {
      if (!draggedItem || !dragSource || dragSource === target) return;
      e.preventDefault();
      e.stopPropagation();
      if (e.dataTransfer) e.dataTransfer.dropEffect = 'move';
      setDragOverTarget(target);
    },
    [draggedItem, dragSource, setDragOverTarget]
  );

  const handleDragLeave = useCallback(() => setDragOverTarget(null), [setDragOverTarget]);

  const handleDrop = useCallback(
    (e: React.DragEvent, target: 'container' | 'player') =>
      handleDropEvent(
        e,
        target,
        draggedItem,
        dragSource,
        mutationToken,
        onTransfer,
        setDraggedItem,
        setDragSource,
        setDragOverTarget
      ),
    [draggedItem, dragSource, mutationToken, onTransfer, setDragOverTarget, setDragSource, setDraggedItem]
  );

  return { handleDragStart, handleDragEnd, handleDragOver, handleDragLeave, handleDrop };
};

export function useContainerSplitPane(props: ContainerSplitPaneHookProps) {
  const { containerId, onTransfer, onClose, modal = false } = props;
  const { openContainers } = useContainerStore(useShallow(state => ({ openContainers: state.openContainers })));
  const { mutationTokens } = useContainerStore(useShallow(state => ({ mutationTokens: state.mutationTokens })));
  const isLoading = useContainerStore(state => state.isLoading);
  const { player } = useGameStore(useShallow(state => ({ player: state.player })));

  const container = useMemo(() => openContainers[containerId] || null, [openContainers, containerId]);
  const mutationToken = useMemo(() => mutationTokens[containerId] || null, [mutationTokens, containerId]);
  const isContainerOpen = containerId in openContainers;
  const playerInventory = (player?.inventory as unknown as InventoryStack[]) || [];

  const containerRef = useRef<HTMLDivElement>(null);
  const firstButtonRef = useRef<HTMLButtonElement>(null);
  const [draggedItem, setDraggedItem] = useState<InventoryStack | null>(null);
  const [dragSource, setDragSource] = useState<'container' | 'player' | null>(null);
  const [dragOverTarget, setDragOverTarget] = useState<'container' | 'player' | null>(null);

  useEffect(() => {
    if (container && isContainerOpen && firstButtonRef.current) {
      firstButtonRef.current.focus();
    }
  }, [container, isContainerOpen]);

  const handleKeyDown = useCallback(
    (e: React.KeyboardEvent) => createKeyDownHandler(modal, onClose, containerRef)(e),
    [modal, onClose]
  );

  const { handleDragStart, handleDragEnd, handleDragOver, handleDragLeave, handleDrop } = useContainerDragHandlers(
    mutationToken,
    onTransfer,
    draggedItem,
    dragSource,
    setDraggedItem,
    setDragSource,
    setDragOverTarget
  );

  const { handleTransferToContainer, handleTransferFromContainer } = createTransferHandlers(onTransfer, mutationToken);

  return {
    isLoading,
    container,
    isContainerOpen,
    playerInventory,
    containerRef,
    firstButtonRef,
    draggedItem,
    dragOverTarget,
    mutationToken,
    handleKeyDown,
    handleDragStart,
    handleDragEnd,
    handleDragOver,
    handleDragLeave,
    handleDrop,
    handleTransferToContainer,
    handleTransferFromContainer,
  };
}
