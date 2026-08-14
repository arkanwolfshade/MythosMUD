import React from 'react';
import type { InventoryStack, WeaponStats } from '../../stores/containerStore';
import { MythosPanel } from '../ui/MythosPanel';
import { TerminalButton } from '../ui/TerminalButton';
import { useContainerSplitPane } from './useContainerSplitPane';

/** Format weapon stats for display (e.g. "1d4+0 slashing, piercing"). */
function formatWeaponStats(weapon: WeaponStats): string {
  const sides = weapon.max_damage - weapon.min_damage + 1;
  const dice = sides > 0 ? `1d${sides}` : '0';
  const mod = weapon.modifier ?? 0;
  const diceStr = `${dice}${mod !== 0 ? `+${mod}` : ''}`;
  const types = (weapon.damage_types ?? []).filter(Boolean).join(', ');
  return [diceStr, types].filter(Boolean).join(' ');
}

function getItemWeapon(item: InventoryStack): WeaponStats | undefined {
  return item.weapon ?? (item.metadata as { weapon?: WeaponStats } | undefined)?.weapon;
}

function ContainerItemRow(props: {
  item: InventoryStack;
  isContainerItem: boolean;
  canTransfer: boolean;
  isDragging: boolean;
  useFirstButtonRef: boolean;
  onDragStart: (e: React.DragEvent, item: InventoryStack, source: 'container' | 'player') => void;
  onDragEnd: () => void;
  onTransfer: (item: InventoryStack, quantity?: number) => void;
  firstButtonRef: React.RefObject<HTMLButtonElement | null>;
  mutationToken: string | null;
}): React.ReactElement {
  const {
    item,
    isContainerItem,
    canTransfer,
    isDragging,
    useFirstButtonRef,
    onDragStart,
    onDragEnd,
    onTransfer,
    firstButtonRef,
    mutationToken,
  } = props;
  const itemLabel =
    `${item.item_name}, ${item.quantity} ${item.quantity === 1 ? 'item' : 'items'}. ` + 'Drag to transfer.';
  const weapon = getItemWeapon(item);

  return (
    <div
      key={item.item_instance_id}
      className={
        `flex items-center justify-between p-2 border-b border-mythos-terminal-border ` +
        `hover:bg-mythos-terminal-hover ${isDragging ? 'opacity-50' : ''}`
      }
      role="listitem"
      draggable={canTransfer}
      onDragStart={e => canTransfer && onDragStart(e, item, isContainerItem ? 'container' : 'player')}
      onDragEnd={onDragEnd}
      aria-label={itemLabel}
    >
      <div className="flex-1">
        <div className="font-semibold text-mythos-terminal-text">{item.item_name}</div>
        {item.quantity > 1 && (
          <div className="text-sm text-mythos-terminal-text-secondary">Quantity: {item.quantity}</div>
        )}
        {weapon && <div className="text-sm text-mythos-terminal-text-secondary">{formatWeaponStats(weapon)}</div>}
      </div>
      {canTransfer && (
        <TerminalButton
          ref={useFirstButtonRef ? firstButtonRef : undefined}
          onClick={() => onTransfer(item)}
          disabled={!mutationToken}
          className="ml-2"
          aria-label={`Transfer ${item.item_name} ${isContainerItem ? 'from' : 'to'} container`}
          onKeyDown={e => {
            if (e.key === 'Enter' || e.key === ' ') {
              e.preventDefault();
              onTransfer(item);
            }
          }}
        >
          Transfer
        </TerminalButton>
      )}
    </div>
  );
}

type ContainerSplitPaneViewModel = ReturnType<typeof useContainerSplitPane>;

interface ContainerInventoryPaneProps {
  side: 'container' | 'player';
  title: string;
  items: InventoryStack[];
  isContainerSide: boolean;
  dragOverTarget: 'container' | 'player' | null;
  onDragOver: (event: React.DragEvent, target: 'container' | 'player') => void;
  onDragLeave: () => void;
  onDrop: (event: React.DragEvent, target: 'container' | 'player') => void;
  renderItem: (item: InventoryStack, isContainerItem: boolean) => React.ReactElement;
  emptyMessage: string;
}

export function ContainerInventoryPane(props: ContainerInventoryPaneProps): React.ReactElement {
  const {
    side,
    title,
    items,
    isContainerSide,
    dragOverTarget,
    onDragOver,
    onDragLeave,
    onDrop,
    renderItem,
    emptyMessage,
  } = props;
  const sideClass = side === 'container' ? 'border-r border-mythos-terminal-border pr-4' : 'pl-4';

  return (
    <div
      className={`flex flex-col ${sideClass} ${
        dragOverTarget === side ? 'bg-mythos-terminal-primary/10 border-mythos-terminal-primary' : ''
      }`}
      aria-label={side === 'container' ? 'Container inventory' : 'Player inventory'}
      onDragOver={event => onDragOver(event, side)}
      onDragLeave={onDragLeave}
      onDrop={event => onDrop(event, side)}
    >
      <h3 className="text-lg font-bold text-mythos-terminal-text mb-2">{title}</h3>
      <div className="flex-1 overflow-y-auto" role="list">
        {items.length === 0 ? (
          <div className="text-center text-mythos-terminal-text-secondary py-8">{emptyMessage}</div>
        ) : (
          items.map(item => renderItem(item, isContainerSide))
        )}
      </div>
    </div>
  );
}

interface ContainerSplitPaneViewProps {
  vm: ContainerSplitPaneViewModel;
  container: NonNullable<ContainerSplitPaneViewModel['container']>;
  modal: boolean;
  className: string;
  onClose?: () => void;
  hasTransfer: boolean;
}

type SplitPaneItemCtx = {
  containerItems: InventoryStack[];
  playerInventory: InventoryStack[];
  hasTransfer: boolean;
  draggedItem: InventoryStack | null;
  handleDragStart: ContainerSplitPaneViewModel['handleDragStart'];
  handleDragEnd: ContainerSplitPaneViewModel['handleDragEnd'];
  handleTransferFromContainer: ContainerSplitPaneViewModel['handleTransferFromContainer'];
  handleTransferToContainer: ContainerSplitPaneViewModel['handleTransferToContainer'];
  firstButtonRef: React.RefObject<HTMLButtonElement | null>;
  mutationToken: string | null;
};

function isFirstPaneItem(
  item: InventoryStack,
  isContainerItem: boolean,
  containerItems: InventoryStack[],
  playerInventory: InventoryStack[]
): boolean {
  if (isContainerItem) return containerItems.indexOf(item) === 0;
  return containerItems.length === 0 && playerInventory.indexOf(item) === 0;
}

function renderSplitPaneItem(
  item: InventoryStack,
  isContainerItem: boolean,
  ctx: SplitPaneItemCtx
): React.ReactElement {
  return (
    <ContainerItemRow
      key={item.item_instance_id}
      item={item}
      isContainerItem={isContainerItem}
      canTransfer={ctx.hasTransfer}
      isDragging={ctx.draggedItem?.item_instance_id === item.item_instance_id}
      useFirstButtonRef={isFirstPaneItem(item, isContainerItem, ctx.containerItems, ctx.playerInventory)}
      onDragStart={ctx.handleDragStart}
      onDragEnd={ctx.handleDragEnd}
      onTransfer={isContainerItem ? ctx.handleTransferFromContainer : ctx.handleTransferToContainer}
      firstButtonRef={ctx.firstButtonRef}
      mutationToken={ctx.mutationToken}
    />
  );
}

function ContainerSplitPanePanes(props: {
  container: ContainerSplitPaneViewProps['container'];
  playerInventory: InventoryStack[];
  dragOverTarget: ContainerSplitPaneViewModel['dragOverTarget'];
  onDragOver: ContainerSplitPaneViewModel['handleDragOver'];
  onDragLeave: ContainerSplitPaneViewModel['handleDragLeave'];
  onDrop: ContainerSplitPaneViewModel['handleDrop'];
  renderItem: (item: InventoryStack, isContainerItem: boolean) => React.ReactElement;
}): React.ReactElement {
  const { container, playerInventory, dragOverTarget, onDragOver, onDragLeave, onDrop, renderItem } = props;
  return (
    <>
      <ContainerInventoryPane
        side="container"
        title={`Container (${container.items.length}/${container.capacity_slots})`}
        items={container.items}
        isContainerSide
        dragOverTarget={dragOverTarget}
        onDragOver={onDragOver}
        onDragLeave={onDragLeave}
        onDrop={onDrop}
        renderItem={renderItem}
        emptyMessage="Container is empty"
      />
      <ContainerInventoryPane
        side="player"
        title={`Inventory (${playerInventory.length}/20)`}
        items={playerInventory}
        isContainerSide={false}
        dragOverTarget={dragOverTarget}
        onDragOver={onDragOver}
        onDragLeave={onDragLeave}
        onDrop={onDrop}
        renderItem={renderItem}
        emptyMessage="Inventory is empty"
      />
    </>
  );
}

function ContainerCloseBar({ onClose }: { onClose?: () => void }): React.ReactElement | null {
  if (!onClose) return null;
  return (
    <div className="p-4 border-t border-mythos-terminal-border">
      <TerminalButton onClick={onClose} className="w-full" aria-label="Close container">
        Close
      </TerminalButton>
    </div>
  );
}

export function ContainerSplitPaneView(props: ContainerSplitPaneViewProps): React.ReactElement {
  const { container, modal, className, onClose, hasTransfer } = props;
  const {
    containerRef,
    firstButtonRef,
    draggedItem,
    playerInventory,
    dragOverTarget,
    mutationToken,
    handleDragStart,
    handleDragEnd,
    handleTransferFromContainer,
    handleTransferToContainer,
    handleKeyDown,
    handleDragOver,
    handleDragLeave,
    handleDrop,
  } = props.vm;
  const itemCtx: SplitPaneItemCtx = {
    containerItems: container.items,
    playerInventory,
    hasTransfer,
    draggedItem,
    handleDragStart,
    handleDragEnd,
    handleTransferFromContainer,
    handleTransferToContainer,
    firstButtonRef,
    mutationToken,
  };
  const renderItem = (item: InventoryStack, isContainerItem: boolean) =>
    renderSplitPaneItem(item, isContainerItem, itemCtx);
  return (
    <MythosPanel className={`flex flex-col ${className}`}>
      {/* role=dialog is the keyboard focus root for transfer shortcuts */}
      {/* eslint-disable-next-line jsx-a11y/no-noninteractive-element-interactions -- dialog key routing */}
      <div
        ref={containerRef}
        className="flex-1 grid grid-cols-2 gap-4 p-4"
        onKeyDown={handleKeyDown}
        role="dialog"
        aria-modal={modal}
        aria-label={`Container: ${container.metadata?.item_name || container.source_type}`}
        tabIndex={-1}
      >
        <ContainerSplitPanePanes
          container={container}
          playerInventory={playerInventory}
          dragOverTarget={dragOverTarget}
          onDragOver={handleDragOver}
          onDragLeave={handleDragLeave}
          onDrop={handleDrop}
          renderItem={renderItem}
        />
      </div>
      <ContainerCloseBar onClose={onClose} />
    </MythosPanel>
  );
}
