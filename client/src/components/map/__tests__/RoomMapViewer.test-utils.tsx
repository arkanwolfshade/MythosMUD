/**
 * Shared test utilities and fixtures for RoomMapViewer tests.
 */

import { vi } from 'vitest';
import type { Room } from '../../../stores/gameStore';
import { useMapLayout } from '../hooks/useMapLayout';
import { useRoomMapData } from '../hooks/useRoomMapData';
import { createEdgesFromRooms, roomsToNodes } from '../utils/mapUtils';

export const mockRooms: Room[] = [
  {
    id: 'earth_arkhamcity_campus_room_001',
    name: 'Test Room 1',
    description: 'A test room',
    plane: 'earth',
    zone: 'arkhamcity',
    sub_zone: 'campus',
    exits: { north: 'earth_arkhamcity_campus_room_002' },
  },
  {
    id: 'earth_arkhamcity_campus_room_002',
    name: 'Test Room 2',
    description: 'Another test room',
    plane: 'earth',
    zone: 'arkhamcity',
    sub_zone: 'campus',
    exits: {},
  },
];

/**
 * Setup default mocks for RoomMapViewer tests.
 */
export const setupDefaultMocks = () => {
  vi.clearAllMocks();

  // Default mock implementations
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  (useRoomMapData as any).mockReturnValue({
    rooms: mockRooms,
    isLoading: false,
    error: null,
    refetch: vi.fn(),
    total: 2,
  });

  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  (useMapLayout as any).mockReturnValue({
    layoutNodes: [],
    hasUnsavedChanges: false,
    updateNodePosition: vi.fn(),
    savePositions: vi.fn(),
    resetToAutoLayout: vi.fn(),
    applyGridLayout: vi.fn(),
  });

  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  (roomsToNodes as any).mockReturnValue([]);
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  (createEdgesFromRooms as any).mockReturnValue([]);
};

/**
 * Create mock nodes for testing.
 */
export const createMockNodes = (count = 1, overrides = {}) => {
  return Array.from({ length: count }, (_, i) => ({
    id: `node${i + 1}`,
    type: 'room',
    position: { x: 0, y: 0 },
    data: { id: `room${i + 1}`, name: `Room ${i + 1}`, ...overrides },
  }));
};

/**
 * Create mock edges for testing.
 */
export const createMockEdges = (count = 1) => {
  return Array.from({ length: count }, (_, i) => ({
    id: `edge${i + 1}`,
    source: `node${i + 1}`,
    target: `node${i + 2}`,
    data: { direction: 'north' },
  }));
};
