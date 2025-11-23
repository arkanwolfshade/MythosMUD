/**
 * Tests for container WebSocket event handling in GameTerminalWithPanels.
 *
 * As documented in the restricted archives of Miskatonic University, container
 * WebSocket events require careful handling to ensure real-time synchronization
 * of container state across all connected players.
 */

import { describe, expect, it, vi, beforeEach, afterEach } from 'vitest';
import { render, waitFor } from '@testing-library/react';
import { GameTerminalWithPanels } from '../GameTerminalWithPanels';
import { useGameConnection } from '../../hooks/useGameConnectionRefactored';
import type { ContainerComponent } from '../../stores/containerStore';

// Mock the container store
const mockOpenContainer = vi.fn();
const mockCloseContainer = vi.fn();
const mockUpdateContainer = vi.fn();
const mockHandleContainerDecayed = vi.fn();
const mockGetContainer = vi.fn();
const mockIsContainerOpen = vi.fn();

vi.mock('../../stores/containerStore', () => ({
  useContainerStore: (selector: (state: unknown) => unknown) => {
    const mockState = {
      openContainer: mockOpenContainer,
      closeContainer: mockCloseContainer,
      updateContainer: mockUpdateContainer,
      handleContainerDecayed: mockHandleContainerDecayed,
      getContainer: mockGetContainer,
      isContainerOpen: mockIsContainerOpen,
    };
    return selector(mockState);
  },
}));

// Mock game connection hook
vi.mock('../../hooks/useGameConnectionRefactored');
const mockUseGameConnection = vi.mocked(useGameConnection);

vi.mock('../../utils/logger', () => ({
  logger: {
    info: vi.fn(),
    warn: vi.fn(),
    error: vi.fn(),
    debug: vi.fn(),
  },
}));

type MockGameEvent = {
  event_type: string;
  timestamp: string;
  sequence_number: number;
  data: Record<string, unknown>;
};

describe('GameTerminalWithPanels Container Events', () => {
  let eventCallback: ((event: MockGameEvent) => void) | null;

  const triggerEvent = (event: MockGameEvent) => {
    if (!eventCallback) {
      throw new Error('Event callback not registered');
    }
    eventCallback(event);
  };

  const renderTerminal = () => render(<GameTerminalWithPanels playerName="TestPlayer" authToken="test-token" />);

  beforeEach(() => {
    vi.clearAllMocks();
    eventCallback = null;
    mockIsContainerOpen.mockReturnValue(false);
    mockGetContainer.mockReturnValue(null);

    mockUseGameConnection.mockImplementation(({ onEvent }) => {
      if (onEvent) {
        eventCallback = onEvent as (event: MockGameEvent) => void;
      }
      return {
        isConnected: true,
        isConnecting: false,
        error: null,
        reconnectAttempts: 0,
        connect: vi.fn(),
        disconnect: vi.fn(),
        sendCommand: vi.fn(),
      } as unknown as ReturnType<typeof useGameConnection>;
    });
  });

  afterEach(() => {
    vi.restoreAllMocks();
    eventCallback = null;
  });

  const createContainerEvent = (eventType: string, data: Record<string, unknown>): MockGameEvent => ({
    event_type: eventType,
    timestamp: new Date().toISOString(),
    sequence_number: 1,
    data,
  });

  const mockContainer: ContainerComponent = {
    container_id: 'container-1',
    source_type: 'environment',
    lock_state: 'unlocked',
    capacity_slots: 10,
    items: [],
    allowed_roles: [],
    metadata: {},
  };

  describe('container.opened event', () => {
    it('should handle container.opened event for personal message', async () => {
      renderTerminal();
      expect(eventCallback).not.toBeNull();

      const event = createContainerEvent('container.opened', {
        container: mockContainer,
        mutation_token: 'token-1',
        expires_at: new Date(Date.now() + 60000).toISOString(),
      });

      triggerEvent(event);

      await waitFor(() => {
        expect(mockOpenContainer).toHaveBeenCalledWith(mockContainer, 'token-1');
      });
    });

    it('should handle container.opened event with room broadcast', async () => {
      renderTerminal();
      expect(eventCallback).not.toBeNull();

      const event = createContainerEvent('container.opened', {
        container: mockContainer,
        actor_id: 'player-1',
        mutation_token: 'token-1',
        expires_at: new Date(Date.now() + 60000).toISOString(),
      });

      triggerEvent(event);

      // Room broadcast events should also update the container store
      await waitFor(() => {
        expect(mockOpenContainer).toHaveBeenCalled();
      });
    });

    it('should handle container.opened event for equipment containers', async () => {
      renderTerminal();
      expect(eventCallback).not.toBeNull();

      const equipmentContainer: ContainerComponent = {
        ...mockContainer,
        container_id: 'backpack-1',
        source_type: 'equipment',
        entity_id: 'player-1',
      };

      const event = createContainerEvent('container.opened', {
        container: equipmentContainer,
        mutation_token: 'token-2',
        expires_at: new Date(Date.now() + 60000).toISOString(),
      });

      triggerEvent(event);

      await waitFor(() => {
        expect(mockOpenContainer).toHaveBeenCalledWith(equipmentContainer, 'token-2');
      });
    });
  });

  describe('container.updated event', () => {
    it('should handle container.updated event with diff', async () => {
      renderTerminal();
      expect(eventCallback).not.toBeNull();

      // First, set up container as open
      mockIsContainerOpen.mockReturnValue(true);
      mockGetContainer.mockReturnValue(mockContainer);

      const event = createContainerEvent('container.updated', {
        container_id: 'container-1',
        diff: {
          items_added: [
            {
              item_instance_id: 'item-1',
              item_id: 'test-item',
              item_name: 'Test Item',
              quantity: 1,
            },
          ],
        },
        actor_id: 'player-1',
      });

      triggerEvent(event);

      // Should update container with new items
      await waitFor(() => {
        expect(mockUpdateContainer).toHaveBeenCalled();
      });
    });

    it('should reconcile diff for items removed', async () => {
      renderTerminal();
      expect(eventCallback).not.toBeNull();

      const containerWithItems: ContainerComponent = {
        ...mockContainer,
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

      mockIsContainerOpen.mockReturnValue(true);
      mockGetContainer.mockReturnValue(containerWithItems);

      const event = createContainerEvent('container.updated', {
        container_id: 'container-1',
        diff: {
          items_removed: ['item-1'],
        },
        actor_id: 'player-1',
      });

      triggerEvent(event);

      await waitFor(() => {
        expect(mockUpdateContainer).toHaveBeenCalled();
        const updatedContainer = mockUpdateContainer.mock.calls[0][0];
        expect(updatedContainer.items).not.toContainEqual(expect.objectContaining({ item_instance_id: 'item-1' }));
      });
    });

    it('should handle container.updated event when container is not open', async () => {
      renderTerminal();
      expect(eventCallback).not.toBeNull();

      mockIsContainerOpen.mockReturnValue(false);
      mockGetContainer.mockReturnValue(null);

      const event = createContainerEvent('container.updated', {
        container_id: 'container-1',
        diff: { items_added: [] },
        actor_id: 'player-1',
      });

      triggerEvent(event);

      // Should not update if container is not open
      await waitFor(() => {
        expect(mockUpdateContainer).not.toHaveBeenCalled();
      });
    });
  });

  describe('container.closed event', () => {
    it('should handle container.closed event', async () => {
      renderTerminal();
      expect(eventCallback).not.toBeNull();

      mockIsContainerOpen.mockReturnValue(true);

      const event = createContainerEvent('container.closed', {
        container_id: 'container-1',
      });

      triggerEvent(event);

      await waitFor(() => {
        expect(mockCloseContainer).toHaveBeenCalledWith('container-1');
      });
    });

    it('should handle container.closed event for multiple containers', async () => {
      renderTerminal();
      expect(eventCallback).not.toBeNull();

      const event1: MockGameEvent = {
        event_type: 'container.closed',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: {
          container_id: 'container-1',
        },
      };
      const event2: MockGameEvent = {
        event_type: 'container.closed',
        timestamp: new Date().toISOString(),
        sequence_number: 2, // Different sequence number to avoid deduplication
        data: {
          container_id: 'container-2',
        },
      };

      triggerEvent(event1);
      triggerEvent(event2);

      await waitFor(() => {
        expect(mockCloseContainer).toHaveBeenCalledWith('container-1');
        expect(mockCloseContainer).toHaveBeenCalledWith('container-2');
      });
    });
  });

  describe('container.decayed event', () => {
    it('should handle container.decayed event', async () => {
      renderTerminal();
      expect(eventCallback).not.toBeNull();

      mockIsContainerOpen.mockReturnValue(true);

      const event = createContainerEvent('container.decayed', {
        container_id: 'container-1',
        room_id: 'room-1',
      });

      triggerEvent(event);

      await waitFor(() => {
        expect(mockHandleContainerDecayed).toHaveBeenCalledWith('container-1');
      });
    });

    it('should handle container.decayed event for corpse containers', async () => {
      renderTerminal();
      expect(eventCallback).not.toBeNull();

      const corpseContainer: ContainerComponent = {
        ...mockContainer,
        container_id: 'corpse-1',
        source_type: 'corpse',
        owner_id: 'dead-player-1',
        room_id: 'room-1',
      };

      mockIsContainerOpen.mockReturnValue(true);
      mockGetContainer.mockReturnValue(corpseContainer);

      const event = createContainerEvent('container.decayed', {
        container_id: 'corpse-1',
        room_id: 'room-1',
      });

      triggerEvent(event);

      await waitFor(() => {
        expect(mockHandleContainerDecayed).toHaveBeenCalledWith('corpse-1');
      });
    });
  });

  describe('Event handling edge cases', () => {
    it('should handle malformed container events gracefully', async () => {
      renderTerminal();
      expect(eventCallback).not.toBeNull();

      const event = createContainerEvent('container.opened', {
        // Missing required fields
        container: null,
      });

      triggerEvent(event);

      // Should not crash, but may not call store methods
      await waitFor(() => {
        expect(mockOpenContainer).not.toHaveBeenCalled();
      });
    });

    it('should handle duplicate events', async () => {
      renderTerminal();
      expect(eventCallback).not.toBeNull();

      const event = createContainerEvent('container.opened', {
        container: mockContainer,
        mutation_token: 'token-1',
        expires_at: new Date(Date.now() + 60000).toISOString(),
      });

      // Send same event twice with same sequence number
      triggerEvent(event);
      triggerEvent(event); // Duplicate

      // Should only process once (deduplication by sequence number)
      await waitFor(() => {
        expect(mockOpenContainer).toHaveBeenCalledTimes(1);
      });
    });
  });
});
