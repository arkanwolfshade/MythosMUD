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
export function useRoomMapData(options: UseRoomMapDataOptions): UseRoomMapDataResult {
  const { plane, zone, subZone, includeExits = true, filterExplored = false, baseUrl = '', authToken } = options;

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

    try {
      setIsLoading(true);
      setError(null);

      // Build query parameters
      const params = new URLSearchParams({
        plane,
        zone,
        include_exits: includeExits.toString(),
        filter_explored: filterExplored.toString(),
      });

      if (subZone) {
        params.append('sub_zone', subZone);
      }

      // Build headers
      const headers: HeadersInit = {
        'Content-Type': 'application/json',
      };

      if (authToken) {
        headers['Authorization'] = `Bearer ${authToken}`;
      }

      // Fetch room data
      const response = await fetch(`${baseUrl}/api/rooms/list?${params.toString()}`, {
        method: 'GET',
        headers,
      });

      if (!response.ok) {
        const errorData = await response.json().catch(() => ({ detail: 'Failed to fetch rooms' }));
        throw new Error(errorData.detail || `Failed to fetch rooms: ${response.status}`);
      }

      const data = await response.json();
      setRooms(data.rooms || []);
      setTotal(data.total || 0);
    } catch (err) {
      const errorMessage = err instanceof Error ? err.message : 'Failed to fetch room data';
      setError(errorMessage);
      setRooms([]);
      setTotal(0);
    } finally {
      setIsLoading(false);
    }
  }, [plane, zone, subZone, includeExits, filterExplored, baseUrl, authToken]);

  // Fetch data when dependencies change
  useEffect(() => {
    fetchRooms();
  }, [fetchRooms]);

  return {
    rooms,
    isLoading,
    error,
    refetch: fetchRooms,
    total,
  };
}
