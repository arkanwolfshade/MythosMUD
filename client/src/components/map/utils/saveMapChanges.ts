/**
 * Utility functions for saving map changes to the server.
 *
 * Handles API calls for saving node positions, edge changes, and room property updates.
 *
 * As documented in the Pnakotic Manuscripts, proper persistence of dimensional
 * modifications is essential for maintaining the integrity of our eldritch architecture.
 */

import type { Edge } from 'reactflow';
import { getVersionedApiBaseUrl } from '../../../utils/config';
import type { MapEditingChanges } from '../hooks/useMapEditing';
import type { ExitEdgeData, RoomNodeData } from '../types';

export interface SaveMapChangesOptions {
  /** Auth token for authenticated requests */
  authToken?: string;
  /** API base URL */
  baseUrl?: string;
}

function buildJsonHeaders(authToken?: string): HeadersInit {
  return {
    'Content-Type': 'application/json',
    ...(authToken ? { Authorization: `Bearer ${authToken}` } : {}),
  };
}

/** Same-origin relative paths in dev/prod; only absolute https when explicitly configured. */
function resolveRoomsApiUrl(apiBase: string, resourcePath: string): string {
  const base = (apiBase.trim() !== '' ? apiBase : getVersionedApiBaseUrl()).replace(/\/$/, '');
  const path = resourcePath.startsWith('/') ? resourcePath : `/${resourcePath}`;
  if (/^https:\/\//i.test(base)) {
    return `${base}${path}`;
  }
  if (/^http:\/\//i.test(base)) {
    const pathname = base.replace(/^https?:\/\/[^/]+/i, '');
    return `${pathname}${path}`;
  }
  return `${base}${path}`;
}

async function readErrorDetail(response: Response): Promise<string> {
  try {
    const rawData: unknown = await response.json();
    if (typeof rawData === 'object' && rawData !== null && 'detail' in rawData) {
      const detail = (rawData as { detail: unknown }).detail;
      if (typeof detail === 'string') return detail;
    }
  } catch {
    // Fall through to statusText below.
  }
  return response.statusText;
}

/**
 * A room exit's id encodes exactly (sourceRoomId, direction, targetRoomId), joined with '-'
 * (see hooks/useMapEditing.ts's createEdge and utils/mapUtils.ts's createEdgesFromRooms, which
 * both build ids this way). Room stable_ids and directions never contain '-' in this codebase
 * (both use '_'), so splitting on '-' deterministically recovers all three parts.
 */
interface ParsedEdgeId {
  sourceRoomId: string;
  direction: string;
  targetRoomId: string;
}

function parseEdgeId(edgeId: string): ParsedEdgeId | null {
  const parts = edgeId.split('-');
  if (parts.length !== 3) return null;
  const [sourceRoomId, direction, targetRoomId] = parts;
  return { sourceRoomId, direction, targetRoomId };
}

/**
 * Save node position updates to the server.
 */
export async function saveNodePositions(
  nodePositions: Map<string, { x: number; y: number }>,
  options: SaveMapChangesOptions
): Promise<void> {
  const { authToken, baseUrl } = options;
  const apiBaseUrl = baseUrl || getVersionedApiBaseUrl();

  // Save each node position
  const savePromises = Array.from(nodePositions.entries()).map(async ([roomId, position]) => {
    const response = await fetch(resolveRoomsApiUrl(apiBaseUrl, `/api/rooms/${encodeURIComponent(roomId)}/position`), {
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

async function deleteExit(
  apiBaseUrl: string,
  sourceRoomId: string,
  direction: string,
  headers: HeadersInit
): Promise<void> {
  const response = await fetch(
    resolveRoomsApiUrl(
      apiBaseUrl,
      `/api/rooms/${encodeURIComponent(sourceRoomId)}/exits/${encodeURIComponent(direction)}`
    ),
    { method: 'DELETE', headers }
  );
  if (!response.ok) {
    const detail = await readErrorDetail(response);
    throw new Error(`Failed to delete exit ${direction} from room ${sourceRoomId}: ${detail}`);
  }
}

async function createExit(apiBaseUrl: string, edgeData: ExitEdgeData, headers: HeadersInit): Promise<void> {
  const response = await fetch(
    resolveRoomsApiUrl(apiBaseUrl, `/api/rooms/${encodeURIComponent(edgeData.sourceRoomId)}/exits`),
    {
      method: 'POST',
      headers,
      body: JSON.stringify({
        direction: edgeData.direction,
        target_room_id: edgeData.targetRoomId,
        flags: edgeData.flags,
        description: edgeData.description,
      }),
    }
  );
  if (!response.ok) {
    const detail = await readErrorDetail(response);
    throw new Error(`Failed to create exit ${edgeData.direction} from room ${edgeData.sourceRoomId}: ${detail}`);
  }
}

async function updateExit(
  apiBaseUrl: string,
  sourceRoomId: string,
  direction: string,
  update: Partial<ExitEdgeData>,
  headers: HeadersInit
): Promise<void> {
  const response = await fetch(
    resolveRoomsApiUrl(
      apiBaseUrl,
      `/api/rooms/${encodeURIComponent(sourceRoomId)}/exits/${encodeURIComponent(direction)}`
    ),
    {
      method: 'PUT',
      headers,
      body: JSON.stringify({
        target_room_id: update.targetRoomId,
        flags: update.flags,
        description: update.description,
      }),
    }
  );
  if (!response.ok) {
    const detail = await readErrorDetail(response);
    throw new Error(`Failed to update exit ${direction} from room ${sourceRoomId}: ${detail}`);
  }
}

/**
 * Save edge (room exit) changes to the server.
 *
 * Sequential and ordered: deletes, then creates, then in-place updates -- awaited one at a time,
 * fail-fast. This matters because room_links has a UNIQUE (from_room_id, direction) constraint:
 * re-pointing an exit produces a delete and a create on the same key, and firing them concurrently
 * (e.g. via Promise.all) races that constraint. On the first failure this throws immediately,
 * leaving later operations un-attempted; the caller is expected to refetch the map so the UI
 * reflects exactly what landed rather than an optimistic guess. See #627.
 *
 * A single room_links row is one direction: this never synthesizes a reverse exit for a two-way
 * corridor -- that is two separate create calls, matching how the read path
 * (get_rooms_with_exits) never infers a reverse either.
 *
 * An edgeUpdate whose direction differs from the edge's original direction is a structural move
 * (room_links has no direction-mutation operation) -- it is resolved here as a delete of the old
 * exit followed by a create of the new one, not a PUT.
 */
export async function saveEdgeChanges(
  newEdges: Edge<ExitEdgeData>[],
  deletedEdgeIds: string[],
  edgeUpdates: Map<string, Partial<ExitEdgeData>>,
  options: SaveMapChangesOptions
): Promise<void> {
  const { authToken, baseUrl } = options;
  const apiBaseUrl = baseUrl || getVersionedApiBaseUrl();
  const headers = buildJsonHeaders(authToken);

  // 1. Explicit deletes.
  for (const edgeId of deletedEdgeIds) {
    const parsed = parseEdgeId(edgeId);
    if (!parsed) {
      throw new Error(`Cannot resolve deleted exit "${edgeId}" to a room and direction; save aborted.`);
    }
    await deleteExit(apiBaseUrl, parsed.sourceRoomId, parsed.direction, headers);
  }

  // 2. Re-pointed exits (direction changed) also delete here, before any create runs, so the
  // global delete-before-create ordering holds even for exits that are conceptually "updated".
  const effectiveCreates: ExitEdgeData[] = newEdges
    .map(edge => edge.data)
    .filter((data): data is ExitEdgeData => !!data);
  const inPlaceUpdates: Array<{ sourceRoomId: string; direction: string; update: Partial<ExitEdgeData> }> = [];

  for (const [edgeId, update] of edgeUpdates) {
    const parsed = parseEdgeId(edgeId);
    if (!parsed) {
      throw new Error(`Cannot resolve updated exit "${edgeId}" to a room and direction; save aborted.`);
    }
    const newDirection = update.direction ?? parsed.direction;
    if (newDirection !== parsed.direction) {
      await deleteExit(apiBaseUrl, parsed.sourceRoomId, parsed.direction, headers);
      effectiveCreates.push({
        direction: newDirection,
        sourceRoomId: parsed.sourceRoomId,
        targetRoomId: update.targetRoomId ?? parsed.targetRoomId,
        flags: update.flags,
        description: update.description,
      });
    } else {
      inPlaceUpdates.push({ sourceRoomId: parsed.sourceRoomId, direction: parsed.direction, update });
    }
  }

  // 3. Creates (explicit new edges, plus re-pointed exits demoted from "update" above).
  for (const edgeData of effectiveCreates) {
    await createExit(apiBaseUrl, edgeData, headers);
  }

  // 4. In-place updates (same direction; target room and/or flags/description only).
  for (const { sourceRoomId, direction, update } of inPlaceUpdates) {
    await updateExit(apiBaseUrl, sourceRoomId, direction, update, headers);
  }
}

/**
 * Save room property updates to the server.
 *
 * Sequential, fail-fast, one PUT per room -- matches saveEdgeChanges' ordering discipline.
 * Only name/description/environment are sent; zone/sub_zone are not editable through this
 * endpoint (re-parenting a room to a different subzone is a structural move, out of scope for
 * a properties save -- see #627). An environment of '' means "Not Set" in the client UI and is
 * sent through as-is: the server translates '' to an explicit clear (NULL), while omitting the
 * key entirely means "leave unchanged".
 */
export async function saveRoomUpdates(
  roomUpdates: Map<string, Partial<RoomNodeData>>,
  options: SaveMapChangesOptions
): Promise<void> {
  const { authToken, baseUrl } = options;
  const apiBaseUrl = baseUrl || getVersionedApiBaseUrl();
  const headers = buildJsonHeaders(authToken);

  for (const [roomId, update] of roomUpdates) {
    const body: Record<string, string> = {};
    if (update.name !== undefined) body.name = update.name;
    if (update.description !== undefined) body.description = update.description;
    if (update.environment !== undefined) body.environment = update.environment;

    if (Object.keys(body).length === 0) continue;

    const response = await fetch(resolveRoomsApiUrl(apiBaseUrl, `/api/rooms/${encodeURIComponent(roomId)}`), {
      method: 'PUT',
      headers,
      body: JSON.stringify(body),
    });
    if (!response.ok) {
      const detail = await readErrorDetail(response);
      throw new Error(`Failed to save properties for room ${roomId}: ${detail}`);
    }
  }
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

  // Save edge changes
  if (changes.newEdges.length > 0 || changes.deletedEdgeIds.length > 0 || changes.edgeUpdates.size > 0) {
    await saveEdgeChanges(changes.newEdges, changes.deletedEdgeIds, changes.edgeUpdates, { authToken, baseUrl });
  }

  // Save room property updates
  if (changes.roomUpdates.size > 0) {
    await saveRoomUpdates(changes.roomUpdates, { authToken, baseUrl });
  }
}
