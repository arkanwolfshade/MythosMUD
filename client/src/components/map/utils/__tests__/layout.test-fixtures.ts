/**
 * Shared test fixtures for layout tests.
 */

import type { Node } from 'reactflow';
import type { RoomNodeData } from '../../types';

/**
 * Create a basic test node.
 */
export const createTestNode = (id: string, overrides: Partial<Node<RoomNodeData>> = {}): Node<RoomNodeData> => ({
  id,
  type: 'room',
  position: { x: 0, y: 0 },
  data: {
    id: `room-${id}`,
    name: `Room ${id}`,
    description: '',
    ...overrides.data,
  },
  ...overrides,
});
