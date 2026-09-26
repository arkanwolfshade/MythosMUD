import React, { useState } from 'react';
import {
  closeContainer,
  ContainerApiError,
  lootAll,
  transferItem,
  type TransferDirection,
} from '../../../api/containers';
import { ModalContainer } from '../primitives';
import type { ContainerSnapshot, InventoryStack } from '../types';
import type { OpenContainerState } from '../utils/stateUpdateUtils';

interface TransferRowProps {
  item: InventoryStack;
  direction: TransferDirection;
  busy: boolean;
  onTransfer: (item: InventoryStack, direction: TransferDirection, quantity: number) => void;
}

function TransferRow({ item, direction, busy, onTransfer }: TransferRowProps) {
  const [quantity, setQuantity] = useState(item.quantity);
  return (
    <li className="flex items-center justify-between gap-2 py-1.5 border-b border-mythos-terminal-primary/10 last:border-0">
      <span className="truncate">{item.item_name || item.item_id}</span>
      <span className="flex items-center gap-2 shrink-0">
        {item.quantity > 1 && (
          <input
            type="number"
            min={1}
            max={item.quantity}
            value={quantity}
            aria-label={`Quantity for ${item.item_name || item.item_id}`}
            onChange={e => {
              const next = Number(e.target.value);
              if (Number.isFinite(next)) setQuantity(Math.min(item.quantity, Math.max(1, Math.trunc(next))));
            }}
            className="w-14 text-xs px-1 py-0.5 rounded border border-mythos-terminal-border bg-mythos-terminal-background text-mythos-terminal-text"
          />
        )}
        <button
          type="button"
          disabled={busy}
          className="text-xs px-2 py-0.5 rounded border border-mythos-terminal-border hover:bg-mythos-terminal-border/30 disabled:opacity-50"
          onClick={() => onTransfer(item, direction, quantity)}
        >
          Transfer
        </button>
      </span>
    </li>
  );
}

function ItemColumn(props: {
  title: string;
  items: InventoryStack[];
  direction: TransferDirection;
  busy: boolean;
  onTransfer: (item: InventoryStack, direction: TransferDirection, quantity: number) => void;
  footer?: React.ReactNode;
}) {
  return (
    <div className="flex-1 min-w-0">
      <div className="text-xs font-semibold text-mythos-terminal-primary uppercase border-b border-mythos-terminal-primary/30 pb-1 mb-1">
        {props.title} ({props.items.length})
      </div>
      {props.items.length === 0 ? (
        <p className="text-sm text-mythos-terminal-text-secondary">Empty.</p>
      ) : (
        <ul>
          {props.items.map(item => (
            <TransferRow
              key={item.item_instance_id}
              item={item}
              direction={props.direction}
              busy={props.busy}
              onTransfer={props.onTransfer}
            />
          ))}
        </ul>
      )}
      {props.footer}
    </div>
  );
}

interface ContainerTransferModalProps {
  containerId: string;
  state: OpenContainerState;
  playerInventory: InventoryStack[];
  authToken: string;
  onClose: (containerId: string) => void;
}

function containerLabel(container: ContainerSnapshot): string {
  const nameFromMetadata = container.metadata?.item_name ?? container.metadata?.player_name;
  if (typeof nameFromMetadata === 'string' && nameFromMetadata) return nameFromMetadata;
  if (container.source_type === 'corpse') return 'Corpse';
  if (container.source_type === 'equipment') return 'Worn container';
  return 'Container';
}

/**
 * Transfer pane for one open container (#711). Driven entirely by container.opened /
 * container.updated events in GameState -- API calls here report success/failure only.
 */
export const ContainerTransferModal: React.FC<ContainerTransferModalProps> = ({
  containerId,
  state,
  playerInventory,
  authToken,
  onClose,
}) => {
  const [error, setError] = useState<string | null>(null);
  const [busy, setBusy] = useState(false);
  const { container, mutationToken } = state;

  const runApiCall = async (fn: () => Promise<void>) => {
    setBusy(true);
    setError(null);
    try {
      await fn();
    } catch (e) {
      setError(e instanceof ContainerApiError ? e.message : 'Something went wrong.');
    } finally {
      setBusy(false);
    }
  };

  const handleTransfer = (item: InventoryStack, direction: TransferDirection, quantity: number) => {
    void runApiCall(() =>
      transferItem(authToken, {
        containerId,
        mutationToken,
        direction,
        stack: { item_id: item.item_id, item_instance_id: item.item_instance_id },
        quantity,
      })
    );
  };

  const handleLootAll = () => {
    void runApiCall(() => lootAll(authToken, containerId, mutationToken));
  };

  const handleClose = () => {
    void runApiCall(() => closeContainer(authToken, containerId, mutationToken)).then(() => onClose(containerId));
  };

  return (
    <ModalContainer
      isOpen={true}
      onClose={handleClose}
      title={containerLabel(container)}
      maxWidth="2xl"
      showCloseButton={true}
    >
      <div className="p-4 space-y-3">
        {error && (
          <p
            role="alert"
            className="text-sm text-mythos-terminal-error border border-mythos-terminal-error/40 rounded p-2"
          >
            {error}
          </p>
        )}
        <div className="flex gap-4">
          <ItemColumn
            title="Container"
            items={container.items}
            direction="to_player"
            busy={busy}
            onTransfer={handleTransfer}
            footer={
              container.items.length > 0 ? (
                <button
                  type="button"
                  disabled={busy}
                  className="mt-2 text-xs px-2 py-1 rounded border border-mythos-terminal-border hover:bg-mythos-terminal-border/30 disabled:opacity-50"
                  onClick={handleLootAll}
                >
                  Loot all
                </button>
              ) : undefined
            }
          />
          <ItemColumn
            title="Inventory"
            items={playerInventory}
            direction="to_container"
            busy={busy}
            onTransfer={handleTransfer}
          />
        </div>
      </div>
    </ModalContainer>
  );
};

/** Renders one ContainerTransferModal per open container. */
export const ContainerTransferModals: React.FC<{
  openContainers: Record<string, OpenContainerState> | undefined;
  playerInventory: InventoryStack[] | undefined;
  authToken: string;
  onClose: (containerId: string) => void;
}> = ({ openContainers, playerInventory, authToken, onClose }) => {
  const entries = Object.entries(openContainers ?? {});
  if (entries.length === 0) return null;
  return (
    <>
      {entries.map(([containerId, state]) => (
        <ContainerTransferModal
          key={containerId}
          containerId={containerId}
          state={state}
          playerInventory={playerInventory ?? []}
          authToken={authToken}
          onClose={onClose}
        />
      ))}
    </>
  );
};
