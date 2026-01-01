/**
 * Room data transformation utilities for React Flow map editor.
 *
 * This module provides utilities to convert room data from the server
 * format into React Flow nodes and edges format, handling various exit
 * formats and coordinate storage.
 *
 * As documented in the Pnakotic Manuscripts, proper transformation of
 * dimensional data is essential for accurate visualization of our
 * eldritch architecture.
 */

import type { Edge, Node } from 'reactflow';
import type { Room } from '../../../stores/gameStore';
import type { ExitEdgeData, RoomNodeData } from '../types';
import { applyGridLayout, type GridLayoutConfig } from './layout';

/**
 * Exit value type - can be null, string (room ID), or object with target/flags/description.
 */
type ExitValue =
  | string
  | null
  | {
      target: string;
      flags?: string[];
      description?: string;
    };

/**
 * Room with optional map coordinates.
 */
type RoomWithCoordinates = Room & {
  map_x?: number | null;
  map_y?: number | null;
};

/**
 * Convert a single room to a React Flow node.
 */
export const roomToNode = (
  room: RoomWithCoordinates,
  currentRoomId?: string,
  _index: number = 0,
  _allRooms: RoomWithCoordinates[] = []
): Node<RoomNodeData> => {
  const isCurrentLocation = currentRoomId === room.id;

  // Determine node type based on environment
  const nodeType =
    room.environment === 'intersection' || room.sub_zone?.includes('intersection') ? 'intersection' : 'room';

  // Use stored coordinates if available, otherwise use default position (will be set by grid layout)
  const position =
    room.map_x !== null && room.map_x !== undefined && room.map_y !== null && room.map_y !== undefined
      ? { x: room.map_x, y: room.map_y }
      : { x: 0, y: 0 };

  const nodeData: RoomNodeData = {
    id: room.id,
    name: room.name,
    description: room.description,
    plane: room.plane,
    zone: room.zone,
    subZone: room.sub_zone,
    environment: room.environment,
    isCurrentLocation,
    occupants: room.occupants,
    occupantCount: room.occupant_count,
  };

  return {
    id: room.id,
    type: nodeType,
    data: nodeData,
    position,
  };
};

/**
 * Convert multiple rooms to React Flow nodes.
 */
export const roomsToNodes = (
  rooms: RoomWithCoordinates[],
  currentRoomId?: string,
  layoutConfig?: GridLayoutConfig
): Node<RoomNodeData>[] => {
  // First, create nodes without positions (or with stored positions)
  const nodes = rooms.map((room, index) => roomToNode(room, currentRoomId, index, rooms));

  // Separate nodes with stored positions from those needing grid layout
  const nodesWithPositions = nodes.filter(node => {
    const room = rooms.find(r => r.id === node.id) as RoomWithCoordinates | undefined;
    if (!room) return false;
    return room.map_x !== null && room.map_x !== undefined && room.map_y !== null && room.map_y !== undefined;
  });
  const nodesNeedingLayout = nodes.filter(node => !nodesWithPositions.some(n => n.id === node.id));

  // Apply grid layout to nodes that need it
  if (nodesNeedingLayout.length > 0) {
    const layoutedNodes = applyGridLayout(nodesNeedingLayout, layoutConfig);

    // Merge nodes with positions and layouted nodes
    return [...nodesWithPositions, ...layoutedNodes];
  }

  return nodes;
};

/**
 * Extract target room ID from exit value (handles both string and object formats).
 */
const extractExitTarget = (exitValue: ExitValue): string | null => {
  if (exitValue === null) {
    return null;
  }

  if (typeof exitValue === 'string') {
    return exitValue;
  }

  if (typeof exitValue === 'object' && 'target' in exitValue) {
    return exitValue.target;
  }

  return null;
};

/**
 * Extract flags from exit value.
 */
const extractExitFlags = (exitValue: ExitValue): string[] => {
  if (exitValue === null || typeof exitValue === 'string') {
    return [];
  }

  if (typeof exitValue === 'object' && 'flags' in exitValue) {
    return exitValue.flags || [];
  }

  return [];
};

/**
 * Extract description from exit value.
 */
const extractExitDescription = (exitValue: ExitValue): string | undefined => {
  if (exitValue === null || typeof exitValue === 'string') {
    return undefined;
  }

  if (typeof exitValue === 'object' && 'description' in exitValue) {
    return exitValue.description;
  }

  return undefined;
};

/**
 * Get source and target handle IDs for an edge based on exit direction.
 * Canvas orientation: Top=North, Bottom=South, Right=East, Left=West
 *
 * @param direction - The exit direction (north, south, east, west, etc.)
 * @returns Object with sourceHandle and targetHandle IDs
 */
const getEdgeHandles = (direction: string): { sourceHandle: string; targetHandle: string } => {
  const normalizedDirection = direction.toLowerCase();

  switch (normalizedDirection) {
    case 'north':
      // Source exits north, so edge starts at top of source, ends at bottom of target
      return { sourceHandle: 'source-top', targetHandle: 'target-bottom' };
    case 'south':
      // Source exits south, so edge starts at bottom of source, ends at top of target
      return { sourceHandle: 'source-bottom', targetHandle: 'target-top' };
    case 'east':
      // Source exits east, so edge starts at right of source, ends at left of target
      return { sourceHandle: 'source-right', targetHandle: 'target-left' };
    case 'west':
      // Source exits west, so edge starts at left of source, ends at right of target
      return { sourceHandle: 'source-left', targetHandle: 'target-right' };
    case 'northeast':
      return { sourceHandle: 'source-top', targetHandle: 'target-bottom' };
    case 'northwest':
      return { sourceHandle: 'source-top', targetHandle: 'target-bottom' };
    case 'southeast':
      return { sourceHandle: 'source-bottom', targetHandle: 'target-top' };
    case 'southwest':
      return { sourceHandle: 'source-bottom', targetHandle: 'target-top' };
    case 'up':
      return { sourceHandle: 'source-top', targetHandle: 'target-bottom' };
    case 'down':
      return { sourceHandle: 'source-bottom', targetHandle: 'target-top' };
    default:
      // For unknown directions, use default (top to bottom)
      return { sourceHandle: 'source-top', targetHandle: 'target-bottom' };
  }
};

/**
 * Create React Flow edges from room exits.
 */
export const createEdgesFromRooms = (rooms: Room[]): Edge<ExitEdgeData>[] => {
  const edges: Edge<ExitEdgeData>[] = [];
  const roomMap = new Map(rooms.map(room => [room.id, room]));

  for (const room of rooms) {
    if (!room.exits) {
      continue;
    }

    for (const [direction, exitValue] of Object.entries(room.exits)) {
      const targetRoomId = extractExitTarget(exitValue as ExitValue);

      // Skip null exits
      if (targetRoomId === null) {
        continue;
      }

      // Verify target room exists
      if (!roomMap.has(targetRoomId)) {
        continue;
      }

      const flags = extractExitFlags(exitValue as ExitValue);
      const description = extractExitDescription(exitValue as ExitValue);

      const edgeData: ExitEdgeData = {
        direction,
        sourceRoomId: room.id,
        targetRoomId,
        flags: flags.length > 0 ? flags : undefined,
        description,
      };

      // Get edge handle IDs based on exit direction
      const { sourceHandle, targetHandle } = getEdgeHandles(direction);

      edges.push({
        id: `${room.id}-${direction}-${targetRoomId}`,
        source: room.id,
        target: targetRoomId,
        type: 'exit',
        sourceHandle,
        targetHandle,
        data: edgeData,
      });
    }
  }

  return edges;
};

/**
 * Complete map data structure.
 */
export interface RoomMapData {
  nodes: Node<RoomNodeData>[];
  edges: Edge<ExitEdgeData>[];
}

/**
 * Transform rooms array to complete map data structure (nodes + edges).
 */
export const transformRoomsToMapData = (
  rooms: RoomWithCoordinates[],
  currentRoomId?: string,
  layoutConfig?: GridLayoutConfig
): RoomMapData => {
  const nodes = roomsToNodes(rooms, currentRoomId, layoutConfig);
  const edges = createEdgesFromRooms(rooms);

  return {
    nodes,
    edges,
  };
};
