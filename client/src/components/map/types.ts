/**
 * Type definitions for the map editor components.
 *
 * These types define the structure of room nodes, exit edges, and
 * map configuration for the React Flow-based map editor.
 *
 * As noted in the Cultes des Goules, proper type definitions are
 * essential for maintaining the integrity of our dimensional mappings.
 */

import type { Edge, Node } from 'reactflow';

/**
 * Room node data structure for React Flow.
 */
export interface RoomNodeData {
  /** Room ID from the database */
  id: string;
  /** Human-readable room name */
  name: string;
  /** Room description */
  description: string;
  /** Plane identifier */
  plane?: string;
  /** Zone identifier */
  zone?: string;
  /** Sub-zone identifier */
  subZone?: string;
  /** Environment type (indoors, outdoors, underwater, etc.) */
  environment?: string;
  /** Whether this is the player's current location */
  isCurrentLocation?: boolean;
  /** Whether this room has unsaved position changes (admin edit mode) */
  hasUnsavedChanges?: boolean;
  /** Current occupants in the room */
  occupants?: string[];
  /** Occupant count */
  occupantCount?: number;
  /** Stored x position from layout (admin edit / persistence) */
  map_x?: number | null;
  /** Stored y position from layout (admin edit / persistence) */
  map_y?: number | null;
}

/**
 * Exit edge data structure for React Flow.
 */
export interface ExitEdgeData {
  /** Direction of the exit (north, south, east, west, up, down) */
  direction: string;
  /** Source room ID */
  sourceRoomId: string;
  /** Target room ID */
  targetRoomId: string;
  /** Exit flags (hidden, locked, one_way, self_reference) */
  flags?: string[];
  /** Custom exit description */
  description?: string;
}

/**
 * Custom room node type for React Flow.
 */
export type RoomNode = Node<RoomNodeData, 'room'>;

/**
 * Custom intersection node type for React Flow.
 */
export type IntersectionNode = Node<RoomNodeData, 'intersection'>;

/**
 * Custom exit edge type for React Flow.
 */
export type ExitEdge = Edge<ExitEdgeData>;

/**
 * Map layout configuration.
 */
export interface MapLayoutConfig {
  /** Layout algorithm type */
  algorithm: 'grid';
  /** Grid spacing for nodes */
  gridSpacing?: number;
  /** Zone-based grouping */
  groupByZone?: boolean;
  /** Sub-zone-based grouping */
  groupBySubZone?: boolean;
}

/**
 * Map view mode.
 */
export type MapViewMode = 'view' | 'edit';
