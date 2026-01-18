/**
 * Utility functions for saving map changes to the server.
 *
 * Handles API calls for saving node positions, edge changes, and room property updates.
 *
 * As documented in the Pnakotic Manuscripts, proper persistence of dimensional
 * modifications is essential for maintaining the integrity of our eldritch architecture.
 */

import type { Edge } from 'reactflow';
import { getApiBaseUrl } from '../../../utils/config';
import type { MapEditingChanges } from '../hooks/useMapEditing';
import type { ExitEdgeData, RoomNodeData } from '../types';

export interface SaveMapChangesOptions {
  /** Auth token for authenticated requests */
  authToken?: string;
  /** API base URL */
  baseUrl?: string;
}

/**
 * Save node position updates to the server.
 */
export async function saveNodePositions(
  nodePositions: Map<string, { x: number; y: number }>,
  options: SaveMapChangesOptions
): Promise<void> {
  const { authToken, baseUrl } = options;
  const apiBaseUrl = baseUrl || getApiBaseUrl();

  // Save each node position
  const savePromises = Array.from(nodePositions.entries()).map(async ([roomId, position]) => {
    const response = await fetch(`${apiBaseUrl}/api/rooms/${encodeURIComponent(roomId)}/position`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        ...(authToken ? { Authorization: `Bearer ${authToken}` } : {}),
      },
      body: JSON.stringify({
        map_x: position.x,
        map_y: position.y,
      }),
    });

    if (!response.ok) {
      let errorData: Record<string, unknown> = { detail: 'Unknown error' };
      try {
        const rawData: unknown = await response.json();
        errorData = typeof rawData === 'object' && rawData !== null ? (rawData as Record<string, unknown>) : errorData;
      } catch {
        // Use default error data if JSON parsing fails
      }
      throw new Error(`Failed to save position for room ${roomId}: ${errorData.detail || response.statusText}`);
    }
  });

  await Promise.all(savePromises);
}

/**
 * Save edge changes to the server.
 *
 * Note: Edge creation/deletion/updates may need to be handled through room exit updates.
 * This is a placeholder for future implementation when edge management APIs are available.
 */
export async function saveEdgeChanges(
  _newEdges: Edge<ExitEdgeData>[],
  _deletedEdgeIds: string[],
  _edgeUpdates: Map<string, Partial<ExitEdgeData>>,
  _options: SaveMapChangesOptions
): Promise<void> {
  // Placeholder for future implementation - all parameters intentionally unused for now
  // When implemented, will use: options.authToken, options.baseUrl, getApiBaseUrl()

  // TODO: Implement edge save functionality when API endpoints are available
  // For now, edges are managed through room exits, which may require
  // updating the room's exit data directly

  // This is a placeholder - actual implementation will depend on the API design
  console.warn('Edge save functionality not yet implemented. Changes will be lost on refresh.');

  // Future implementation might look like:
  // 1. For new edges: POST /api/rooms/{room_id}/exits
  // 2. For deleted edges: DELETE /api/rooms/{room_id}/exits/{direction}
  // 3. For updated edges: PUT /api/rooms/{room_id}/exits/{direction}
}

/**
 * Save room property updates to the server.
 *
 * Note: Room property updates may need to be handled through room update endpoints.
 * This is a placeholder for future implementation when room property update APIs are available.
 */
export async function saveRoomUpdates(
  _roomUpdates: Map<string, Partial<RoomNodeData>>,
  _options: SaveMapChangesOptions
): Promise<void> {
  // Placeholder for future implementation - all parameters intentionally unused for now
  // When implemented, will use: options.authToken, options.baseUrl, getApiBaseUrl()

  // TODO: Implement room property save functionality when API endpoints are available
  // For now, room properties are managed through room data files, which may require
  // a different update mechanism

  // This is a placeholder - actual implementation will depend on the API design
  console.warn('Room property save functionality not yet implemented. Changes will be lost on refresh.');

  // Future implementation might look like:
  // PUT /api/rooms/{room_id} with room property updates
}

/**
 * Save all map changes to the server.
 */
export async function saveMapChanges(changes: MapEditingChanges, options: SaveMapChangesOptions): Promise<void> {
  const { authToken, baseUrl } = options;

  // Check if there are any changes to save
  const hasChanges =
    changes.nodePositions.size > 0 ||
    changes.newEdges.length > 0 ||
    changes.deletedEdgeIds.length > 0 ||
    changes.edgeUpdates.size > 0 ||
    changes.roomUpdates.size > 0;

  // Early return if no changes
  if (!hasChanges) {
    return;
  }

  // Save node positions
  if (changes.nodePositions.size > 0) {
    await saveNodePositions(changes.nodePositions, { authToken, baseUrl });
  }

  // Save edge changes (placeholder - not yet implemented)
  if (changes.newEdges.length > 0 || changes.deletedEdgeIds.length > 0 || changes.edgeUpdates.size > 0) {
    await saveEdgeChanges(changes.newEdges, changes.deletedEdgeIds, changes.edgeUpdates, { authToken, baseUrl });
  }

  // Save room property updates (placeholder - not yet implemented)
  if (changes.roomUpdates.size > 0) {
    await saveRoomUpdates(changes.roomUpdates, { authToken, baseUrl });
  }
}
