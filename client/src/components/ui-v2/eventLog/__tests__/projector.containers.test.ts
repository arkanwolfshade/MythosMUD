/**
 * Unit tests for container.* / inventory_updated projector handlers (#711).
 */
/// <reference types="vitest/globals" />

import type { GameEvent } from '../../eventHandlers/types';
import type { ContainerSnapshot } from '../../types';
import { getInitialGameState, projectEvent } from '../projector';

function baseEvent(overrides: Partial<GameEvent>): GameEvent {
  return {
    event_type: 'container.opened',
    timestamp: new Date().toISOString(),
    sequence_number: 1,
    data: {},
    ...overrides,
  };
}

function sampleContainer(overrides: Partial<ContainerSnapshot> = {}): ContainerSnapshot {
  return {
    container_id: 'c1',
    source_type: 'environment',
    owner_id: null,
    room_id: 'room1',
    entity_id: null,
    lock_state: 'unlocked',
    capacity_slots: 10,
    allowed_roles: [],
    items: [],
    metadata: {},
    ...overrides,
  };
}

describe('projector container/inventory handlers', () => {
  describe('container.opened', () => {
    it('creates an openContainers entry from the personal delivery (mutation_token present)', () => {
      const prev = getInitialGameState();
      const container = sampleContainer();
      const event = baseEvent({
        event_type: 'container.opened',
        data: { container, mutation_token: 'tok-1', owner_id: null },
      });
      const next = projectEvent(prev, event);
      expect(next.openContainers?.c1).toEqual({ container, mutationToken: 'tok-1', sequenceNumber: 1 });
    });

    it('ignores the room broadcast (no mutation_token) -- does not create an entry', () => {
      const prev = getInitialGameState();
      const event = baseEvent({
        event_type: 'container.opened',
        data: { container: sampleContainer(), owner_id: null, actor_id: 'other-player' },
      });
      const next = projectEvent(prev, event);
      expect(next.openContainers).toBeUndefined();
    });
  });

  describe('container.updated', () => {
    it('applies to a container already open (the actor own entry)', () => {
      const container = sampleContainer();
      const prev = {
        ...getInitialGameState(),
        openContainers: { c1: { container, mutationToken: 'tok-1', sequenceNumber: 1 } },
      };
      const updatedContainer = sampleContainer({ items: [] });
      const event = baseEvent({
        event_type: 'container.updated',
        sequence_number: 2,
        data: { container_id: 'c1', container: updatedContainer, actor_id: 'me' },
      });
      const next = projectEvent(prev, event);
      expect(next.openContainers?.c1.container).toEqual(updatedContainer);
      expect(next.openContainers?.c1.sequenceNumber).toBe(2);
    });

    it('is a no-op for a container the client has not opened (bystander room broadcast)', () => {
      const prev = getInitialGameState();
      const event = baseEvent({
        event_type: 'container.updated',
        data: { container_id: 'c1', container: sampleContainer(), actor_id: 'someone-else' },
      });
      const next = projectEvent(prev, event);
      expect(next).toBe(prev);
    });

    it('rejects a stale update (sequence_number <= last applied)', () => {
      const container = sampleContainer();
      const prev = {
        ...getInitialGameState(),
        openContainers: { c1: { container, mutationToken: 'tok-1', sequenceNumber: 5 } },
      };
      const staleContainer = sampleContainer({ capacity_slots: 999 });
      const event = baseEvent({
        event_type: 'container.updated',
        sequence_number: 3,
        data: { container_id: 'c1', container: staleContainer, actor_id: 'me' },
      });
      const next = projectEvent(prev, event);
      expect(next).toBe(prev);
    });
  });

  describe('container.closed', () => {
    it('removes an open container entry', () => {
      const prev = {
        ...getInitialGameState(),
        openContainers: { c1: { container: sampleContainer(), mutationToken: 'tok-1' } },
      };
      const event = baseEvent({ event_type: 'container.closed', data: { container_id: 'c1' } });
      const next = projectEvent(prev, event);
      expect(next.openContainers?.c1).toBeUndefined();
    });

    it('is a no-op for a container not open', () => {
      const prev = getInitialGameState();
      const event = baseEvent({ event_type: 'container.closed', data: { container_id: 'c1' } });
      const next = projectEvent(prev, event);
      expect(next).toBe(prev);
    });
  });

  describe('container.created', () => {
    it('adds a room container summary (e.g. a fresh corpse)', () => {
      const prev = getInitialGameState();
      const corpse = sampleContainer({
        source_type: 'corpse',
        owner_id: 'player-1',
        decay_at: '2026-01-01T00:00:00Z',
        metadata: { grace_period_start: '2026-01-01T00:00:00Z', grace_period_seconds: 300 },
      });
      const event = baseEvent({ event_type: 'container.created', data: { container: corpse } });
      const next = projectEvent(prev, event);
      expect(next.roomContainers).toEqual([
        {
          container_id: 'c1',
          source_type: 'corpse',
          owner_id: 'player-1',
          decay_at: '2026-01-01T00:00:00Z',
          metadata: { grace_period_start: '2026-01-01T00:00:00Z', grace_period_seconds: 300 },
        },
      ]);
    });

    it('does not duplicate an already-known container', () => {
      const corpse = sampleContainer({ source_type: 'corpse' });
      const prev = {
        ...getInitialGameState(),
        roomContainers: [{ container_id: 'c1', source_type: 'corpse' as const }],
      };
      const event = baseEvent({ event_type: 'container.created', data: { container: corpse } });
      const next = projectEvent(prev, event);
      expect(next.roomContainers).toHaveLength(1);
    });
  });

  describe('container.decayed', () => {
    it('removes the container from both openContainers and roomContainers', () => {
      const prev = {
        ...getInitialGameState(),
        openContainers: { c1: { container: sampleContainer(), mutationToken: 'tok-1' } },
        roomContainers: [{ container_id: 'c1', source_type: 'corpse' as const }],
      };
      const event = baseEvent({
        event_type: 'container.decayed',
        data: { container_id: 'c1', room_id: 'room1' },
      });
      const next = projectEvent(prev, event);
      expect(next.openContainers?.c1).toBeUndefined();
      expect(next.roomContainers).toEqual([]);
    });
  });

  describe('inventory_updated', () => {
    it('sets playerInventory and playerEquipped', () => {
      const prev = getInitialGameState();
      const inventory = [
        {
          item_instance_id: 'i1',
          prototype_id: 'torch',
          item_id: 'torch',
          item_name: 'Torch',
          slot_type: 'inventory',
          quantity: 1,
        },
      ];
      const equipped = {
        main_hand: {
          item_instance_id: 'i2',
          prototype_id: 'sword',
          item_id: 'sword',
          item_name: 'Sword',
          slot_type: 'main_hand',
          quantity: 1,
        },
      };
      const event = baseEvent({ event_type: 'inventory_updated', data: { inventory, equipped } });
      const next = projectEvent(prev, event);
      expect(next.playerInventory).toEqual(inventory);
      expect(next.playerEquipped).toEqual(equipped);
    });

    it('leaves prior state untouched when fields are missing', () => {
      const prev = { ...getInitialGameState(), playerInventory: [], playerEquipped: {} };
      const event = baseEvent({ event_type: 'inventory_updated', data: {} });
      const next = projectEvent(prev, event);
      expect(next.playerInventory).toEqual([]);
      expect(next.playerEquipped).toEqual({});
    });
  });
});
