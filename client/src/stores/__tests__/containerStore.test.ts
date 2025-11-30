/**
 * Tests for container store.
 *
 * As documented in the restricted archives of Miskatonic University, container
 * state management requires thorough testing to ensure proper handling of
 * investigator artifacts and forbidden containers.
 */

import { describe, expect, it, beforeEach } from 'vitest';
import { useContainerStore } from '../containerStore';
import type { ContainerComponent, ContainerLockState, ContainerSourceType } from '../containerStore';

describe('ContainerStore', () => {
  beforeEach(() => {
    // Reset store state before each test
    useContainerStore.getState().reset();
  });

  describe('Initial State', () => {
    it('should have empty initial state', () => {
      const state = useContainerStore.getState();
      expect(state.openContainers).toEqual({});
      expect(state.mutationTokens).toEqual({});
      expect(state.selectedContainerId).toBeNull();
      expect(state.isLoading).toBe(false);
    });
  });

  describe('Container Management', () => {
    it('should open a container', () => {
      const container: ContainerComponent = {
        container_id: 'test-container-1',
        source_type: 'environment' as ContainerSourceType,
        room_id: 'test-room-1',
        capacity_slots: 10,
        lock_state: 'unlocked' as ContainerLockState,
        items: [],
        metadata: {},
        allowed_roles: [],
      };

      const mutationToken = 'test-token-123';

      useContainerStore.getState().openContainer(container, mutationToken);

      const state = useContainerStore.getState();
      expect(state.openContainers['test-container-1']).toEqual(container);
      expect(state.mutationTokens['test-container-1']).toBe(mutationToken);
    });

    it('should close a container', () => {
      const container: ContainerComponent = {
        container_id: 'test-container-1',
        source_type: 'environment' as ContainerSourceType,
        room_id: 'test-room-1',
        capacity_slots: 10,
        lock_state: 'unlocked' as ContainerLockState,
        items: [],
        metadata: {},
        allowed_roles: [],
      };

      useContainerStore.getState().openContainer(container, 'test-token');
      useContainerStore.getState().closeContainer('test-container-1');

      const state = useContainerStore.getState();
      expect(state.openContainers['test-container-1']).toBeUndefined();
      expect(state.mutationTokens['test-container-1']).toBeUndefined();
    });

    it('should update container contents', () => {
      const container: ContainerComponent = {
        container_id: 'test-container-1',
        source_type: 'environment' as ContainerSourceType,
        room_id: 'test-room-1',
        capacity_slots: 10,
        lock_state: 'unlocked' as ContainerLockState,
        items: [],
        metadata: {},
        allowed_roles: [],
      };

      useContainerStore.getState().openContainer(container, 'test-token');

      const updatedContainer: ContainerComponent = {
        ...container,
        items: [
          {
            item_instance_id: 'item-1',
            prototype_id: 'test-item',
            item_id: 'test-item',
            item_name: 'Test Item',
            slot_type: 'backpack',
            quantity: 1,
          },
        ],
      };

      useContainerStore.getState().updateContainer(updatedContainer);

      const state = useContainerStore.getState();
      expect(state.openContainers['test-container-1'].items).toHaveLength(1);
      expect(state.openContainers['test-container-1'].items[0].item_id).toBe('test-item');
    });

    it('should handle container decay', () => {
      const container: ContainerComponent = {
        container_id: 'test-container-1',
        source_type: 'corpse' as ContainerSourceType,
        room_id: 'test-room-1',
        capacity_slots: 20,
        lock_state: 'unlocked' as ContainerLockState,
        items: [],
        metadata: {},
        allowed_roles: [],
      };

      useContainerStore.getState().openContainer(container, 'test-token');
      useContainerStore.getState().handleContainerDecayed('test-container-1');

      const state = useContainerStore.getState();
      expect(state.openContainers['test-container-1']).toBeUndefined();
      expect(state.mutationTokens['test-container-1']).toBeUndefined();
    });
  });

  describe('Selection Management', () => {
    it('should select a container', () => {
      const container: ContainerComponent = {
        container_id: 'test-container-1',
        source_type: 'environment' as ContainerSourceType,
        room_id: 'test-room-1',
        capacity_slots: 10,
        lock_state: 'unlocked' as ContainerLockState,
        items: [],
        metadata: {},
        allowed_roles: [],
      };

      useContainerStore.getState().openContainer(container, 'test-token');
      useContainerStore.getState().selectContainer('test-container-1');

      const state = useContainerStore.getState();
      expect(state.selectedContainerId).toBe('test-container-1');
    });

    it('should deselect a container', () => {
      const container: ContainerComponent = {
        container_id: 'test-container-1',
        source_type: 'environment' as ContainerSourceType,
        room_id: 'test-room-1',
        capacity_slots: 10,
        lock_state: 'unlocked' as ContainerLockState,
        items: [],
        metadata: {},
        allowed_roles: [],
      };

      useContainerStore.getState().openContainer(container, 'test-token');
      useContainerStore.getState().selectContainer('test-container-1');
      useContainerStore.getState().deselectContainer();

      const state = useContainerStore.getState();
      expect(state.selectedContainerId).toBeNull();
    });
  });

  describe('Loading State', () => {
    it('should set loading state', () => {
      useContainerStore.getState().setLoading(true);
      expect(useContainerStore.getState().isLoading).toBe(true);

      useContainerStore.getState().setLoading(false);
      expect(useContainerStore.getState().isLoading).toBe(false);
    });
  });

  describe('Selectors', () => {
    it('should get container by ID', () => {
      const container: ContainerComponent = {
        container_id: 'test-container-1',
        source_type: 'environment' as ContainerSourceType,
        room_id: 'test-room-1',
        capacity_slots: 10,
        lock_state: 'unlocked' as ContainerLockState,
        items: [],
        metadata: {},
        allowed_roles: [],
      };

      useContainerStore.getState().openContainer(container, 'test-token');

      const retrieved = useContainerStore.getState().getContainer('test-container-1');
      expect(retrieved).toEqual(container);
    });

    it('should return null for non-existent container', () => {
      const retrieved = useContainerStore.getState().getContainer('non-existent');
      expect(retrieved).toBeNull();
    });

    it('should get mutation token for container', () => {
      const container: ContainerComponent = {
        container_id: 'test-container-1',
        source_type: 'environment' as ContainerSourceType,
        room_id: 'test-room-1',
        capacity_slots: 10,
        lock_state: 'unlocked' as ContainerLockState,
        items: [],
        metadata: {},
        allowed_roles: [],
      };

      useContainerStore.getState().openContainer(container, 'test-token-123');

      const token = useContainerStore.getState().getMutationToken('test-container-1');
      expect(token).toBe('test-token-123');
    });

    it('should return null for non-existent mutation token', () => {
      const token = useContainerStore.getState().getMutationToken('non-existent');
      expect(token).toBeNull();
    });

    it('should get all open container IDs', () => {
      const container1: ContainerComponent = {
        container_id: 'test-container-1',
        source_type: 'environment' as ContainerSourceType,
        room_id: 'test-room-1',
        capacity_slots: 10,
        lock_state: 'unlocked' as ContainerLockState,
        items: [],
        metadata: {},
        allowed_roles: [],
      };

      const container2: ContainerComponent = {
        container_id: 'test-container-2',
        source_type: 'equipment' as ContainerSourceType,
        entity_id: 'test-entity-1',
        capacity_slots: 5,
        lock_state: 'unlocked' as ContainerLockState,
        items: [],
        metadata: {},
        allowed_roles: [],
      };

      useContainerStore.getState().openContainer(container1, 'token-1');
      useContainerStore.getState().openContainer(container2, 'token-2');

      const containerIds = useContainerStore.getState().getOpenContainerIds();
      expect(containerIds).toHaveLength(2);
      expect(containerIds).toContain('test-container-1');
      expect(containerIds).toContain('test-container-2');
    });

    it('should check if container is open', () => {
      const container: ContainerComponent = {
        container_id: 'test-container-1',
        source_type: 'environment' as ContainerSourceType,
        room_id: 'test-room-1',
        capacity_slots: 10,
        lock_state: 'unlocked' as ContainerLockState,
        items: [],
        metadata: {},
        allowed_roles: [],
      };

      expect(useContainerStore.getState().isContainerOpen('test-container-1')).toBe(false);

      useContainerStore.getState().openContainer(container, 'test-token');
      expect(useContainerStore.getState().isContainerOpen('test-container-1')).toBe(true);
    });
  });

  describe('Reset', () => {
    it('should reset all state', () => {
      const container: ContainerComponent = {
        container_id: 'test-container-1',
        source_type: 'environment' as ContainerSourceType,
        room_id: 'test-room-1',
        capacity_slots: 10,
        lock_state: 'unlocked' as ContainerLockState,
        items: [],
        metadata: {},
        allowed_roles: [],
      };

      useContainerStore.getState().openContainer(container, 'test-token');
      useContainerStore.getState().selectContainer('test-container-1');
      useContainerStore.getState().setLoading(true);

      useContainerStore.getState().reset();

      const state = useContainerStore.getState();
      expect(state.openContainers).toEqual({});
      expect(state.mutationTokens).toEqual({});
      expect(state.selectedContainerId).toBeNull();
      expect(state.isLoading).toBe(false);
    });
  });

  describe('Selectors - getWearableContainersForPlayer', () => {
    it('should return only equipment containers for a specific player', () => {
      const playerContainer: ContainerComponent = {
        container_id: 'player-backpack',
        source_type: 'equipment' as ContainerSourceType,
        entity_id: 'player-1',
        capacity_slots: 10,
        lock_state: 'unlocked' as ContainerLockState,
        items: [],
        metadata: {},
        allowed_roles: [],
      };

      const otherPlayerContainer: ContainerComponent = {
        container_id: 'other-player-backpack',
        source_type: 'equipment' as ContainerSourceType,
        entity_id: 'player-2',
        capacity_slots: 10,
        lock_state: 'unlocked' as ContainerLockState,
        items: [],
        metadata: {},
        allowed_roles: [],
      };

      const environmentContainer: ContainerComponent = {
        container_id: 'environment-container',
        source_type: 'environment' as ContainerSourceType,
        room_id: 'test-room-1',
        capacity_slots: 10,
        lock_state: 'unlocked' as ContainerLockState,
        items: [],
        metadata: {},
        allowed_roles: [],
      };

      useContainerStore.getState().openContainer(playerContainer, 'token-1');
      useContainerStore.getState().openContainer(otherPlayerContainer, 'token-2');
      useContainerStore.getState().openContainer(environmentContainer, 'token-3');

      const wearableContainers = useContainerStore.getState().getWearableContainersForPlayer('player-1');

      expect(wearableContainers).toHaveLength(1);
      expect(wearableContainers[0].container_id).toBe('player-backpack');
    });

    it('should return empty array when no equipment containers exist for player', () => {
      const wearableContainers = useContainerStore.getState().getWearableContainersForPlayer('player-1');
      expect(wearableContainers).toEqual([]);
    });

    it('should return multiple equipment containers for same player', () => {
      const backpack: ContainerComponent = {
        container_id: 'backpack',
        source_type: 'equipment' as ContainerSourceType,
        entity_id: 'player-1',
        capacity_slots: 10,
        lock_state: 'unlocked' as ContainerLockState,
        items: [],
        metadata: {},
        allowed_roles: [],
      };

      const pouch: ContainerComponent = {
        container_id: 'pouch',
        source_type: 'equipment' as ContainerSourceType,
        entity_id: 'player-1',
        capacity_slots: 5,
        lock_state: 'unlocked' as ContainerLockState,
        items: [],
        metadata: {},
        allowed_roles: [],
      };

      useContainerStore.getState().openContainer(backpack, 'token-1');
      useContainerStore.getState().openContainer(pouch, 'token-2');

      const wearableContainers = useContainerStore.getState().getWearableContainersForPlayer('player-1');

      expect(wearableContainers).toHaveLength(2);
      expect(wearableContainers.map(c => c.container_id)).toContain('backpack');
      expect(wearableContainers.map(c => c.container_id)).toContain('pouch');
    });
  });

  describe('Selectors - getCorpseContainersInRoom', () => {
    it('should return only corpse containers in a specific room', () => {
      const corpseContainer: ContainerComponent = {
        container_id: 'corpse-1',
        source_type: 'corpse' as ContainerSourceType,
        room_id: 'room-1',
        capacity_slots: 20,
        lock_state: 'unlocked' as ContainerLockState,
        items: [],
        metadata: {},
        allowed_roles: [],
      };

      const otherRoomCorpse: ContainerComponent = {
        container_id: 'corpse-2',
        source_type: 'corpse' as ContainerSourceType,
        room_id: 'room-2',
        capacity_slots: 20,
        lock_state: 'unlocked' as ContainerLockState,
        items: [],
        metadata: {},
        allowed_roles: [],
      };

      const environmentContainer: ContainerComponent = {
        container_id: 'environment-container',
        source_type: 'environment' as ContainerSourceType,
        room_id: 'room-1',
        capacity_slots: 10,
        lock_state: 'unlocked' as ContainerLockState,
        items: [],
        metadata: {},
        allowed_roles: [],
      };

      useContainerStore.getState().openContainer(corpseContainer, 'token-1');
      useContainerStore.getState().openContainer(otherRoomCorpse, 'token-2');
      useContainerStore.getState().openContainer(environmentContainer, 'token-3');

      const corpseContainers = useContainerStore.getState().getCorpseContainersInRoom('room-1');

      expect(corpseContainers).toHaveLength(1);
      expect(corpseContainers[0].container_id).toBe('corpse-1');
    });

    it('should return empty array when no corpse containers exist in room', () => {
      const corpseContainers = useContainerStore.getState().getCorpseContainersInRoom('room-1');
      expect(corpseContainers).toEqual([]);
    });

    it('should return multiple corpse containers in same room', () => {
      const corpse1: ContainerComponent = {
        container_id: 'corpse-1',
        source_type: 'corpse' as ContainerSourceType,
        room_id: 'room-1',
        capacity_slots: 20,
        lock_state: 'unlocked' as ContainerLockState,
        items: [],
        metadata: {},
        allowed_roles: [],
      };

      const corpse2: ContainerComponent = {
        container_id: 'corpse-2',
        source_type: 'corpse' as ContainerSourceType,
        room_id: 'room-1',
        capacity_slots: 15,
        lock_state: 'unlocked' as ContainerLockState,
        items: [],
        metadata: {},
        allowed_roles: [],
      };

      useContainerStore.getState().openContainer(corpse1, 'token-1');
      useContainerStore.getState().openContainer(corpse2, 'token-2');

      const corpseContainers = useContainerStore.getState().getCorpseContainersInRoom('room-1');

      expect(corpseContainers).toHaveLength(2);
      expect(corpseContainers.map(c => c.container_id)).toContain('corpse-1');
      expect(corpseContainers.map(c => c.container_id)).toContain('corpse-2');
    });
  });

  describe('Close Container - Selection Handling', () => {
    it('should clear selected container when closing the selected container', () => {
      const container: ContainerComponent = {
        container_id: 'test-container-1',
        source_type: 'environment' as ContainerSourceType,
        room_id: 'test-room-1',
        capacity_slots: 10,
        lock_state: 'unlocked' as ContainerLockState,
        items: [],
        metadata: {},
        allowed_roles: [],
      };

      useContainerStore.getState().openContainer(container, 'test-token');
      useContainerStore.getState().selectContainer('test-container-1');

      expect(useContainerStore.getState().selectedContainerId).toBe('test-container-1');

      useContainerStore.getState().closeContainer('test-container-1');

      expect(useContainerStore.getState().selectedContainerId).toBeNull();
      expect(useContainerStore.getState().openContainers['test-container-1']).toBeUndefined();
    });

    it('should preserve selected container when closing a different container', () => {
      const container1: ContainerComponent = {
        container_id: 'container-1',
        source_type: 'environment' as ContainerSourceType,
        room_id: 'test-room-1',
        capacity_slots: 10,
        lock_state: 'unlocked' as ContainerLockState,
        items: [],
        metadata: {},
        allowed_roles: [],
      };

      const container2: ContainerComponent = {
        container_id: 'container-2',
        source_type: 'environment' as ContainerSourceType,
        room_id: 'test-room-1',
        capacity_slots: 10,
        lock_state: 'unlocked' as ContainerLockState,
        items: [],
        metadata: {},
        allowed_roles: [],
      };

      useContainerStore.getState().openContainer(container1, 'token-1');
      useContainerStore.getState().openContainer(container2, 'token-2');
      useContainerStore.getState().selectContainer('container-1');

      useContainerStore.getState().closeContainer('container-2');

      expect(useContainerStore.getState().selectedContainerId).toBe('container-1');
      expect(useContainerStore.getState().openContainers['container-1']).toBeDefined();
      expect(useContainerStore.getState().openContainers['container-2']).toBeUndefined();
    });
  });
});
