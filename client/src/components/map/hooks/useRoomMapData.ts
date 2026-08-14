/**
 * React hook for fetching and managing room map data.
 *
 * Fetches room data from the server API and provides loading/error states
 * for the map visualization component.
 *
 * As documented in the Pnakotic Manuscripts, proper data retrieval is
 * essential for maintaining the integrity of our dimensional mappings.
 */

import { useCallback, useEffect, useState } from 'react';
import type { Room } from '../../../stores/gameStore';
import { isApiErrorWithDetail, isRoomsListApiResponse } from '../../../utils/apiTypeGuards';
import { getVersionedApiBaseUrl } from '../../../utils/config';

export interface UseRoomMapDataOptions {
  /** Plane name (required) */
  plane: string;
  /** Zone name (required) */
  zone: string;
  /** Optional sub-zone name for filtering */
  subZone?: string;
  /** Whether to include exit data (default: true) */
  includeExits?: boolean;
  /** Whether to filter to only show explored rooms (default: false, requires authToken) */
  filterExplored?: boolean;
  /** API base URL (default: uses relative URLs) */
  baseUrl?: string;
  /** Auth token for authenticated requests (required if filterExplored is true) */
  authToken?: string;
}

export interface UseRoomMapDataResult {
  /** Array of room data */
  rooms: Room[];
  /** Loading state */
  isLoading: boolean;
  /** Error message if fetch failed */
  error: string | null;
  /** Function to manually refetch data */
  refetch: () => Promise<void>;
  /** Total number of rooms returned */
  total: number;
}

/**
 * Hook for fetching room map data from the server.
 *
 * @param options - Configuration options for data fetching
 * @returns Room data, loading state, error state, and refetch function
 */
interface FetchRoomListConfig {
  plane: string;
  zone: string;
  subZone?: string;
  includeExits: boolean;
  filterExplored: boolean;
  effectiveBaseUrl: string;
  authToken?: string;
}

function buildRoomListRequest(config: FetchRoomListConfig): { url: string; headers: HeadersInit } {
  const params = new URLSearchParams({
    plane: config.plane,
    zone: config.zone,
    include_exits: config.includeExits.toString(),
    filter_explored: config.filterExplored.toString(),
  });
  if (config.subZone) {
    params.append('sub_zone', config.subZone);
  }
  const headers: HeadersInit = { 'Content-Type': 'application/json' };
  if (config.authToken) {
    headers['Authorization'] = `Bearer ${config.authToken}`;
  }
  return { url: `${config.effectiveBaseUrl}/api/rooms/list?${params.toString()}`, headers };
}

async function parseRoomListResponse(response: Response): Promise<{ rooms: Room[]; total: number } | null> {
  if (!response.ok) {
    const rawErr: unknown = await response.json().catch(() => ({ detail: 'Failed to fetch rooms' }));
    const message =
      isApiErrorWithDetail(rawErr) && rawErr.detail ? rawErr.detail : `Failed to fetch rooms: ${response.status}`;
    throw new Error(message);
  }
  const raw: unknown = await response.json();
  if (!isRoomsListApiResponse(raw)) {
    return null;
  }
  return {
    rooms: Array.isArray(raw.rooms) ? (raw.rooms as Room[]) : [],
    total: typeof raw.total === 'number' ? raw.total : 0,
  };
}

async function fetchRoomListData(config: FetchRoomListConfig): Promise<{ rooms: Room[]; total: number } | null> {
  const { url, headers } = buildRoomListRequest(config);
  return parseRoomListResponse(await fetch(url, { method: 'GET', headers }));
}

export function useRoomMapData(options: UseRoomMapDataOptions): UseRoomMapDataResult {
  const { plane, zone, subZone, includeExits = true, filterExplored = false, baseUrl = '', authToken } = options;
  const effectiveBaseUrl = baseUrl || getVersionedApiBaseUrl();

  const [rooms, setRooms] = useState<Room[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [total, setTotal] = useState(0);

  const fetchRooms = useCallback(async () => {
    if (!plane || !zone) {
      setError('Plane and zone are required');
      setIsLoading(false);
      return;
    }
    setIsLoading(true);
    setError(null);
    try {
      const result = await fetchRoomListData({
        plane,
        zone,
        subZone,
        includeExits,
        filterExplored,
        effectiveBaseUrl,
        authToken,
      });
      setRooms(result?.rooms ?? []);
      setTotal(result?.total ?? 0);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to fetch room data');
      setRooms([]);
      setTotal(0);
    } finally {
      setIsLoading(false);
    }
  }, [plane, zone, subZone, includeExits, filterExplored, effectiveBaseUrl, authToken]);

  /* eslint-disable react-hooks/set-state-in-effect -- refetch when deps change */
  useEffect(() => {
    void fetchRooms();
  }, [fetchRooms]);
  /* eslint-enable react-hooks/set-state-in-effect */

  return {
    rooms,
    isLoading,
    error,
    refetch: fetchRooms,
    total,
  };
}
