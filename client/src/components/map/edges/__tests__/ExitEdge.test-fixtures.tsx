/**
 * Shared test fixtures for ExitEdge tests.
 */

import { Position } from 'reactflow';
import type { ExitEdgeData } from '../../types';

/**
 * Default props for ExitEdge component.
 */
export const defaultExitEdgeProps = {
  id: 'edge1',
  source: 'room1',
  target: 'room2',
  sourceX: 0,
  sourceY: 0,
  targetX: 100,
  targetY: 100,
  sourcePosition: Position.Right,
  targetPosition: Position.Left,
  style: {},
  markerEnd: undefined,
  data: {
    direction: 'north',
    sourceRoomId: 'room1',
    targetRoomId: 'room2',
    flags: [],
  } as ExitEdgeData,
};
