// container.* and inventory_updated event handlers for the projector.
// Split from projectorHandlersState.ts to keep file-nloc under limit.
//
// Server contract (see server/services/container_websocket_events.py and
// server/services/inventory_websocket_events.py):
// - container.opened is sent personally to the opener (carries mutation_token) and, when the
//   container has a room_id, also broadcast to the room WITHOUT mutation_token/expires_at. Only
//   the personal copy creates an openContainers entry -- see .cursor/rules/server-authority.mdc.
// - container.updated / container.closed carry the full container snapshot (or just container_id
//   for closed) and are always sent personally to the actor, plus a room broadcast when room_id is
//   set. Both deliveries share the same payload, so the projector distinguishes them structurally:
//   it only ever applies updated/closed to a container_id already present in openContainers, which
//   -- because container sessions are exclusive -- is only ever the actor's own entry.
// - container.created / container.decayed are room-only broadcasts (corpse spawn / cleanup).
// - inventory_updated is personal only.

import type { ContainerSnapshot, InventoryStack, RoomContainerSummary } from '../types';
import type { ProjectorHandler } from './projectorHandlersState';

function asContainerSnapshot(value: unknown): ContainerSnapshot | null {
  if (!value || typeof value !== 'object') return null;
  const c = value as Partial<ContainerSnapshot>;
  return typeof c.container_id === 'string' ? (c as ContainerSnapshot) : null;
}

function toRoomContainerSummary(container: ContainerSnapshot): RoomContainerSummary {
  return {
    container_id: container.container_id,
    source_type: container.source_type,
    owner_id: container.owner_id ?? null,
    decay_at: container.decay_at ?? null,
    metadata: container.metadata,
  };
}

export const containerHandlers: Partial<Record<string, ProjectorHandler>> = {
  'container.opened'(prevState, event) {
    const mutationToken = event.data.mutation_token;
    if (typeof mutationToken !== 'string' || !mutationToken) return prevState;
    const container = asContainerSnapshot(event.data.container);
    if (!container) return prevState;
    return {
      ...prevState,
      openContainers: {
        ...prevState.openContainers,
        [container.container_id]: {
          container,
          mutationToken,
          sequenceNumber: event.sequence_number,
        },
      },
    };
  },

  'container.updated'(prevState, event) {
    const containerId = event.data.container_id;
    if (typeof containerId !== 'string') return prevState;
    const existing = prevState.openContainers?.[containerId];
    if (!existing) return prevState;
    const seq = event.sequence_number;
    if (typeof seq === 'number' && typeof existing.sequenceNumber === 'number' && seq <= existing.sequenceNumber) {
      return prevState;
    }
    const container = asContainerSnapshot(event.data.container);
    if (!container) return prevState;
    return {
      ...prevState,
      openContainers: {
        ...prevState.openContainers,
        [containerId]: { ...existing, container, sequenceNumber: seq },
      },
    };
  },

  'container.closed'(prevState, event) {
    const containerId = event.data.container_id;
    if (typeof containerId !== 'string' || !prevState.openContainers?.[containerId]) return prevState;
    const next = { ...prevState.openContainers };
    delete next[containerId];
    return { ...prevState, openContainers: next };
  },

  'container.created'(prevState, event) {
    const container = asContainerSnapshot(event.data.container);
    if (!container) return prevState;
    const existing = prevState.roomContainers ?? [];
    if (existing.some(c => c.container_id === container.container_id)) return prevState;
    return { ...prevState, roomContainers: [...existing, toRoomContainerSummary(container)] };
  },

  'container.decayed'(prevState, event) {
    const containerId = event.data.container_id;
    if (typeof containerId !== 'string') return prevState;
    let next = prevState;
    if (prevState.openContainers?.[containerId]) {
      const oc = { ...prevState.openContainers };
      delete oc[containerId];
      next = { ...next, openContainers: oc };
    }
    if (prevState.roomContainers?.some(c => c.container_id === containerId)) {
      next = { ...next, roomContainers: prevState.roomContainers!.filter(c => c.container_id !== containerId) };
    }
    return next;
  },

  inventory_updated(prevState, event) {
    const inventory = event.data.inventory;
    const equipped = event.data.equipped;
    return {
      ...prevState,
      ...(Array.isArray(inventory) && { playerInventory: inventory as InventoryStack[] }),
      ...(equipped !== undefined &&
        equipped !== null &&
        typeof equipped === 'object' && { playerEquipped: equipped as Record<string, InventoryStack> }),
    };
  },
};
