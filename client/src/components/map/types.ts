/**
 * Type definitions for the map editor components.
 *
 * These types define the structure of room nodes, exit edges, and
 * map configuration for the React Flow-based map editor.
 *
 * As noted in the Cultes des Goules, proper type definitions are
 * essential for maintaining the integrity of our dimensional mappings.
 */

/**
 * Room domain type used by the map editor/viewer (fetched via the map API, not the live
 * game-state Room in ui-v2/types.ts -- this one carries map_x/map_y and entities).
 */
export interface Room {
  id: string;
  name: string;
  description: string;
  plane?: string;
  zone?: string;
  sub_zone?: string;
  environment?: string;
  exits: Record<string, string>;
  occupants?: string[];
  players?: string[];
  npcs?: string[];
  occupant_count?: number;
  entities?: Array<{
    id: string;
    name: string;
    type: string;
    [key: string]: unknown;
  }>;
  /** Map X coordinate (admin-set position) */
  map_x?: number | null;
  /** Map Y coordinate (admin-set position) */
  map_y?: number | null;
}

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
  /**
   * Directions whose exit leaves the loaded area (another sub-zone or zone).
   *
   * The map is fetched for one sub-zone, so the room on the far side is not in the
   * response and no edge can be drawn to it. Without this the only way into a
   * building like the Sanitarium is invisible and the corner looks like a dead end.
   */
  departures?: string[];
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
