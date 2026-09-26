import React from 'react';
import type { InventoryStack, RoomContainerSummary } from '../types';

interface InventoryPanelProps {
  /** Player's carried items (from inventory_updated). */
  inventory: InventoryStack[] | undefined;
  /** Player's equipped-slot items, keyed by slot_type (from inventory_updated). */
  equipped: Record<string, InventoryStack> | undefined;
  /** Containers known to be in the current room (corpses seen since arrival). */
  roomContainers: RoomContainerSummary[] | undefined;
  /** Sends a raw text command (e.g. "equip sword", "unequip main_hand", "drop 1"). */
  onSendCommand: (command: string) => void;
  /** Opens a container by id (HTTP /api/containers/open; result arrives via container.opened). */
  onOpenContainer: (containerId: string) => void;
}

function itemLabel(item: InventoryStack): string {
  return item.item_name || item.item_id;
}

function InventoryRow({ item, onSendCommand }: { item: InventoryStack; onSendCommand: (c: string) => void }) {
  // Equip is offered for every carried item -- the server's own `equip` command validates
  // whether the item is actually equippable and just returns an error message if not, so the
  // client doesn't need to duplicate that logic here.
  return (
    <li className="flex items-center justify-between gap-2 py-1 border-b border-mythos-terminal-primary/10 last:border-0">
      <span className="truncate">
        {itemLabel(item)}
        {item.quantity > 1 ? ` x${item.quantity}` : ''}
      </span>
      <span className="flex gap-1 shrink-0">
        <button
          type="button"
          className="text-xs px-2 py-0.5 rounded border border-mythos-terminal-border hover:bg-mythos-terminal-border/30"
          onClick={() => onSendCommand(`equip ${item.item_instance_id}`)}
        >
          Equip
        </button>
        <button
          type="button"
          className="text-xs px-2 py-0.5 rounded border border-mythos-terminal-border hover:bg-mythos-terminal-border/30"
          onClick={() => onSendCommand(`drop ${item.item_instance_id}`)}
        >
          Drop
        </button>
      </span>
    </li>
  );
}

function EquippedRow({
  slot,
  item,
  onSendCommand,
  onOpenContainer,
}: {
  slot: string;
  item: InventoryStack;
  onSendCommand: (c: string) => void;
  onOpenContainer: (containerId: string) => void;
}) {
  const wornContainerId = item.inner_container ? item.item_instance_id : null;
  return (
    <li className="flex items-center justify-between gap-2 py-1 border-b border-mythos-terminal-primary/10 last:border-0">
      <span className="truncate">
        <span className="text-mythos-terminal-text-secondary text-xs uppercase mr-2">{slot}</span>
        {itemLabel(item)}
      </span>
      <span className="flex gap-1 shrink-0">
        {wornContainerId && (
          <button
            type="button"
            className="text-xs px-2 py-0.5 rounded border border-mythos-terminal-border hover:bg-mythos-terminal-border/30"
            onClick={() => onOpenContainer(wornContainerId)}
          >
            Open
          </button>
        )}
        <button
          type="button"
          className="text-xs px-2 py-0.5 rounded border border-mythos-terminal-border hover:bg-mythos-terminal-border/30"
          onClick={() => onSendCommand(`unequip ${slot}`)}
        >
          Unequip
        </button>
      </span>
    </li>
  );
}

function RoomContainerRow({
  container,
  onOpenContainer,
}: {
  container: RoomContainerSummary;
  onOpenContainer: (containerId: string) => void;
}) {
  const label = container.source_type === 'corpse' ? 'Corpse' : 'Container';
  return (
    <li className="flex items-center justify-between gap-2 py-1 border-b border-mythos-terminal-primary/10 last:border-0">
      <span className="truncate">{label}</span>
      <button
        type="button"
        className="text-xs px-2 py-0.5 rounded border border-mythos-terminal-border hover:bg-mythos-terminal-border/30"
        onClick={() => onOpenContainer(container.container_id)}
      >
        Open
      </button>
    </li>
  );
}

/**
 * Player inventory dock panel (#711): carried items, equipped slots, and any containers
 * (corpses) known to be in the current room. Equip/unequip/drop go through the text command
 * pipeline (onSendCommand); opening a container goes through the HTTP API and its state arrives
 * via container.opened.
 */
export const InventoryPanel: React.FC<InventoryPanelProps> = ({
  inventory,
  equipped,
  roomContainers,
  onSendCommand,
  onOpenContainer,
}) => {
  const carried = inventory ?? [];
  const equippedEntries = Object.entries(equipped ?? {});
  const containers = roomContainers ?? [];

  if (carried.length === 0 && equippedEntries.length === 0 && containers.length === 0) {
    return (
      <div className="p-4 text-mythos-terminal-text-secondary">
        <p>You are carrying nothing.</p>
        <p className="text-xs mt-2">Use the &quot;inventory&quot; command in-game to refresh.</p>
      </div>
    );
  }

  return (
    <div className="p-4 space-y-4 overflow-y-auto max-h-full">
      {equippedEntries.length > 0 && (
        <div>
          <div className="text-xs font-semibold text-mythos-terminal-primary uppercase border-b border-mythos-terminal-primary/30 pb-1 mb-1">
            Equipped
          </div>
          <ul>
            {equippedEntries.map(([slot, item]) => (
              <EquippedRow
                key={slot}
                slot={slot}
                item={item}
                onSendCommand={onSendCommand}
                onOpenContainer={onOpenContainer}
              />
            ))}
          </ul>
        </div>
      )}

      <div>
        <div className="text-xs font-semibold text-mythos-terminal-primary uppercase border-b border-mythos-terminal-primary/30 pb-1 mb-1">
          Carried ({carried.length})
        </div>
        {carried.length === 0 ? (
          <p className="text-sm text-mythos-terminal-text-secondary">Empty.</p>
        ) : (
          <ul>
            {carried.map(item => (
              <InventoryRow key={item.item_instance_id} item={item} onSendCommand={onSendCommand} />
            ))}
          </ul>
        )}
      </div>

      {containers.length > 0 && (
        <div>
          <div className="text-xs font-semibold text-mythos-terminal-primary uppercase border-b border-mythos-terminal-primary/30 pb-1 mb-1">
            In this room
          </div>
          <ul>
            {containers.map(c => (
              <RoomContainerRow key={c.container_id} container={c} onOpenContainer={onOpenContainer} />
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};
