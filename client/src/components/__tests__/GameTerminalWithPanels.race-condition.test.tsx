import { render, screen, waitFor } from '@testing-library/react';
import { beforeEach, describe, expect, it, vi } from 'vitest';
import { useGameConnection } from '../../hooks/useGameConnectionRefactored';
import type { GameEvent } from '../../types/game';
import { GameTerminalWithPanels } from '../GameTerminalWithPanels';

// Mock the useGameConnection hook
vi.mock('../../hooks/useGameConnectionRefactored');
const mockUseGameConnection = vi.mocked(useGameConnection);

// Mock the logger
vi.mock('../../utils/logger', () => ({
  logger: {
    info: vi.fn(),
    warn: vi.fn(),
    error: vi.fn(),
  },
}));

describe('GameTerminalWithPanels Race Condition Tests', () => {
  const mockPlayerName = 'TestPlayer';
  const mockAuthToken = 'test-token';

  beforeEach(() => {
    vi.clearAllMocks();

    // Default mock implementation
    mockUseGameConnection.mockReturnValue({
      isConnected: true,
      isConnecting: false,
      connect: vi.fn(),
      disconnect: vi.fn(),
      sendCommand: vi.fn(),
      onEvent: vi.fn(),
    });
  });

  describe('Room Title Update Race Condition', () => {
    it('should preserve room data from room_update event when processing room_occupants event', async () => {
      // Arrange: Set up initial state

      const newRoom = {
        id: 'new-room-001',
        name: 'New Room',
        description: 'This is the new room',
        zone: 'arkham',
        sub_zone: 'sanitarium',
        plane: 'material',
        environment: 'indoor',
        exits: { south: 'old-room-001' },
        occupants: ['TestPlayer'],
        occupant_count: 1,
      };

      // Mock the hook to simulate receiving events
      let eventCallback: ((event: GameEvent) => void) | null = null;
      mockUseGameConnection.mockImplementation(({ onEvent }) => {
        if (onEvent) {
          eventCallback = onEvent;
        }
        return {
          isConnected: true,
          isConnecting: false,
          connect: vi.fn(),
          disconnect: vi.fn(),
          sendCommand: vi.fn(),
          onEvent: vi.fn(),
        };
      });

      render(<GameTerminalWithPanels playerName={mockPlayerName} authToken={mockAuthToken} />);

      // Act: Simulate the race condition scenario
      // 1. First, send a room_update event with new room data
      if (eventCallback) {
        eventCallback({
          event_type: 'room_update',
          timestamp: '2025-09-14T20:00:00Z',
          sequence_number: 1,
          data: {
            room: newRoom,
            occupants: ['TestPlayer'],
            occupant_count: 1,
          },
        });
      }

      // 2. Then, send a room_occupants event (this should NOT overwrite the new room data)
      if (eventCallback) {
        eventCallback({
          event_type: 'room_occupants',
          timestamp: '2025-09-14T20:00:01Z',
          sequence_number: 2,
          data: {
            occupants: ['TestPlayer', 'AnotherPlayer'],
            count: 2,
          },
        });
      }

      // Assert: The room should show the new room data, not the old room data
      await waitFor(() => {
        const roomInfoPanel = screen.getByText('New Room');
        expect(roomInfoPanel).toBeInTheDocument();
      });

      // Verify the room name is correct (not "Old Room")
      expect(screen.queryByText('Old Room')).not.toBeInTheDocument();
      expect(screen.getByText('New Room')).toBeInTheDocument();
    });

    it('should handle room_occupants event when no room_update event has been processed', async () => {
      // Arrange: Set up initial state

      // Mock the hook to simulate receiving events
      let eventCallback: ((event: GameEvent) => void) | null = null;
      mockUseGameConnection.mockImplementation(({ onEvent }) => {
        if (onEvent) {
          eventCallback = onEvent;
        }
        return {
          isConnected: true,
          isConnecting: false,
          connect: vi.fn(),
          disconnect: vi.fn(),
          sendCommand: vi.fn(),
          onEvent: vi.fn(),
        };
      });

      render(<GameTerminalWithPanels playerName={mockPlayerName} authToken={mockAuthToken} />);

      // Act: Send only a room_occupants event (no room_update event)
      if (eventCallback) {
        eventCallback({
          event_type: 'room_occupants',
          timestamp: '2025-09-14T20:00:00Z',
          sequence_number: 1,
          data: {
            occupants: ['TestPlayer', 'AnotherPlayer'],
            count: 2,
          },
        });
      }

      // Assert: The room should show the fallback room data when no room data is available
      await waitFor(() => {
        // This test verifies that when no room_update event is pending,
        // the room_occupants event should use the fallback room data
        // (This is the expected behavior when no room data is available)
        expect(screen.getByText('Miskatonic University Library')).toBeInTheDocument();
      });
    });

    it('should not overwrite new room data with stale room data in race condition', async () => {
      // Arrange: Set up the race condition scenario

      const newRoom = {
        id: 'new-room-001',
        name: 'New Room',
        description: 'This is the new room',
        zone: 'arkham',
        sub_zone: 'sanitarium',
        plane: 'material',
        environment: 'indoor',
        exits: { south: 'stale-room-001' },
        occupants: ['TestPlayer'],
        occupant_count: 1,
      };

      // Mock the hook to simulate receiving events
      let eventCallback: ((event: GameEvent) => void) | null = null;
      mockUseGameConnection.mockImplementation(({ onEvent }) => {
        if (onEvent) {
          eventCallback = onEvent;
        }
        return {
          isConnected: true,
          isConnecting: false,
          connect: vi.fn(),
          disconnect: vi.fn(),
          sendCommand: vi.fn(),
          onEvent: vi.fn(),
        };
      });

      render(<GameTerminalWithPanels playerName={mockPlayerName} authToken={mockAuthToken} />);

      // Act: Simulate the problematic race condition
      // 1. Send room_update event with new room data
      if (eventCallback) {
        eventCallback({
          event_type: 'room_update',
          timestamp: '2025-09-14T20:00:00Z',
          sequence_number: 1,
          data: {
            room: newRoom,
            occupants: ['TestPlayer'],
            occupant_count: 1,
          },
        });
      }

      // 2. Send room_occupants event that should NOT overwrite with stale data
      if (eventCallback) {
        eventCallback({
          event_type: 'room_occupants',
          timestamp: '2025-09-14T20:00:01Z',
          sequence_number: 2,
          data: {
            occupants: ['TestPlayer', 'AnotherPlayer'],
            count: 2,
          },
        });
      }

      // Assert: The room should show the NEW room data, not the stale room data
      await waitFor(() => {
        expect(screen.getByText('New Room')).toBeInTheDocument();
        expect(screen.queryByText('Stale Room')).not.toBeInTheDocument();
      });

      // Verify the room description is from the new room
      expect(screen.getByText('This is the new room')).toBeInTheDocument();
      expect(screen.queryByText('This is stale room data')).not.toBeInTheDocument();
    });

    it('should handle rapid succession of room_update and room_occupants events', async () => {
      // Arrange: Set up multiple room transitions
      const room1 = {
        id: 'room-001',
        name: 'Room 1',
        description: 'First room',
        zone: 'arkham',
        sub_zone: 'sanitarium',
        plane: 'material',
        environment: 'indoor',
        exits: { north: 'room-002' },
        occupants: ['Player1'],
        occupant_count: 1,
      };

      const room2 = {
        id: 'room-002',
        name: 'Room 2',
        description: 'Second room',
        zone: 'arkham',
        sub_zone: 'sanitarium',
        plane: 'material',
        environment: 'indoor',
        exits: { south: 'room-001' },
        occupants: ['TestPlayer'],
        occupant_count: 1,
      };

      // Mock the hook to simulate receiving events
      let eventCallback: ((event: GameEvent) => void) | null = null;
      mockUseGameConnection.mockImplementation(({ onEvent }) => {
        if (onEvent) {
          eventCallback = onEvent;
        }
        return {
          isConnected: true,
          isConnecting: false,
          connect: vi.fn(),
          disconnect: vi.fn(),
          sendCommand: vi.fn(),
          onEvent: vi.fn(),
        };
      });

      render(<GameTerminalWithPanels playerName={mockPlayerName} authToken={mockAuthToken} />);

      // Act: Send rapid succession of events
      if (eventCallback) {
        // First transition
        eventCallback({
          event_type: 'room_update',
          timestamp: '2025-09-14T20:00:00Z',
          sequence_number: 1,
          data: {
            room: room1,
            occupants: ['TestPlayer'],
            occupant_count: 1,
          },
        });

        eventCallback({
          event_type: 'room_occupants',
          timestamp: '2025-09-14T20:00:01Z',
          sequence_number: 2,
          data: {
            occupants: ['TestPlayer', 'Player2'],
            count: 2,
          },
        });

        // Second transition
        eventCallback({
          event_type: 'room_update',
          timestamp: '2025-09-14T20:00:02Z',
          sequence_number: 3,
          data: {
            room: room2,
            occupants: ['TestPlayer'],
            occupant_count: 1,
          },
        });

        eventCallback({
          event_type: 'room_occupants',
          timestamp: '2025-09-14T20:00:03Z',
          sequence_number: 4,
          data: {
            occupants: ['TestPlayer'],
            count: 1,
          },
        });
      }

      // Assert: The final room should be Room 2
      await waitFor(() => {
        expect(screen.getByText('Room 2')).toBeInTheDocument();
        expect(screen.queryByText('Room 1')).not.toBeInTheDocument();
      });
    });
  });
});
