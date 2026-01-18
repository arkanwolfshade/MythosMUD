/**
 * Tests for useRoomMapData hook.
 *
 * Verifies that the hook properly fetches room data from the API
 * and handles loading/error states correctly.
 */

import { act, renderHook, waitFor } from '@testing-library/react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import type { Room } from '../../../../stores/gameStore';
import { useRoomMapData } from '../useRoomMapData';

// Mock fetch globally using vi.spyOn for proper cleanup
const fetchSpy = vi.spyOn(global, 'fetch');

describe('useRoomMapData', () => {
  beforeEach(() => {
    fetchSpy.mockClear();
    vi.clearAllMocks();
  });

  afterEach(() => {
    // Use mockReset instead of mockRestore to keep the spy active across tests
    // This prevents issues where mockRestore might restore an undefined/broken fetch implementation
    fetchSpy.mockReset();
    vi.clearAllMocks();
  });

  it('should fetch rooms with required plane and zone', async () => {
    const mockRooms: Room[] = [
      {
        id: 'earth_arkhamcity_campus_room_001',
        name: 'Test Room 1',
        description: 'A test room',
        plane: 'earth',
        zone: 'arkhamcity',
        sub_zone: 'campus',
        exits: {},
      },
    ];

    fetchSpy.mockResolvedValueOnce({
      ok: true,
      json: async () => ({
        rooms: mockRooms,
        total: 1,
        plane: 'earth',
        zone: 'arkhamcity',
      }),
    } as unknown as Response);

    const { result } = renderHook(() =>
      useRoomMapData({
        plane: 'earth',
        zone: 'arkhamcity',
      })
    );

    expect(result.current.isLoading).toBe(true);
    expect(result.current.rooms).toEqual([]);

    await waitFor(() => {
      expect(result.current.isLoading).toBe(false);
    });

    expect(result.current.rooms).toEqual(mockRooms);
    expect(result.current.total).toBe(1);
    expect(result.current.error).toBeNull();
    expect(fetchSpy).toHaveBeenCalledWith(
      expect.stringContaining('/api/rooms/list?plane=earth&zone=arkhamcity&include_exits=true'),
      expect.objectContaining({
        method: 'GET',
        headers: expect.objectContaining({
          'Content-Type': 'application/json',
        }),
      })
    );
  });

  it('should include subZone in query when provided', async () => {
    fetchSpy.mockResolvedValueOnce({
      ok: true,
      json: async () => ({
        rooms: [],
        total: 0,
        plane: 'earth',
        zone: 'arkhamcity',
        sub_zone: 'campus',
      }),
    } as unknown as Response);

    const { result } = renderHook(() =>
      useRoomMapData({
        plane: 'earth',
        zone: 'arkhamcity',
        subZone: 'campus',
      })
    );

    await waitFor(() => {
      expect(result.current.isLoading).toBe(false);
    });

    expect(fetchSpy).toHaveBeenCalledWith(expect.stringContaining('sub_zone=campus'), expect.any(Object));
  });

  it('should handle includeExits parameter', async () => {
    fetchSpy.mockResolvedValueOnce({
      ok: true,
      json: async () => ({
        rooms: [],
        total: 0,
      }),
    } as unknown as Response);

    const { result } = renderHook(() =>
      useRoomMapData({
        plane: 'earth',
        zone: 'arkhamcity',
        includeExits: false,
      })
    );

    await waitFor(() => {
      expect(result.current.isLoading).toBe(false);
    });

    expect(fetchSpy).toHaveBeenCalledWith(expect.stringContaining('include_exits=false'), expect.any(Object));
  });

  it('should handle API errors', async () => {
    fetchSpy.mockResolvedValueOnce({
      ok: false,
      status: 500,
      json: async () => ({
        detail: 'Internal server error',
      }),
    } as unknown as Response);

    const { result } = renderHook(() =>
      useRoomMapData({
        plane: 'earth',
        zone: 'arkhamcity',
      })
    );

    await waitFor(() => {
      expect(result.current.isLoading).toBe(false);
    });

    expect(result.current.error).toBe('Internal server error');
    expect(result.current.rooms).toEqual([]);
    expect(result.current.total).toBe(0);
  });

  it('should handle network errors', async () => {
    fetchSpy.mockRejectedValueOnce(new Error('Network error'));

    const { result } = renderHook(() =>
      useRoomMapData({
        plane: 'earth',
        zone: 'arkhamcity',
      })
    );

    await waitFor(() => {
      expect(result.current.isLoading).toBe(false);
    });

    expect(result.current.error).toBe('Network error');
    expect(result.current.rooms).toEqual([]);
  });

  it('should require plane and zone', async () => {
    const { result } = renderHook(() =>
      useRoomMapData({
        plane: '',
        zone: 'arkhamcity',
      })
    );

    await waitFor(() => {
      expect(result.current.isLoading).toBe(false);
    });

    expect(result.current.error).toBe('Plane and zone are required');
    expect(fetchSpy).not.toHaveBeenCalled();
  });

  it('should include auth token in headers when provided', async () => {
    fetchSpy.mockResolvedValueOnce({
      ok: true,
      json: async () => ({
        rooms: [],
        total: 0,
      }),
    } as unknown as Response);

    const { result } = renderHook(() =>
      useRoomMapData({
        plane: 'earth',
        zone: 'arkhamcity',
        authToken: 'test-token',
      })
    );

    await waitFor(() => {
      expect(result.current.isLoading).toBe(false);
    });

    expect(fetchSpy).toHaveBeenCalledWith(
      expect.any(String),
      expect.objectContaining({
        headers: expect.objectContaining({
          Authorization: 'Bearer test-token',
        }),
      })
    );
  });

  it('should provide refetch function', async () => {
    fetchSpy.mockResolvedValue({
      ok: true,
      json: async () => ({
        rooms: [],
        total: 0,
      }),
    } as unknown as Response);

    const { result } = renderHook(() =>
      useRoomMapData({
        plane: 'earth',
        zone: 'arkhamcity',
      })
    );

    await waitFor(() => {
      expect(result.current.isLoading).toBe(false);
    });

    expect(fetchSpy).toHaveBeenCalledTimes(1);

    // Call refetch
    await act(async () => {
      await result.current.refetch();
    });

    await waitFor(() => {
      expect(result.current.isLoading).toBe(false);
    });

    expect(fetchSpy).toHaveBeenCalledTimes(2);
  });

  it('should include filter_explored parameter when filterExplored is true', async () => {
    fetchSpy.mockResolvedValueOnce({
      ok: true,
      json: async () => ({
        rooms: [],
        total: 0,
      }),
    } as unknown as Response);

    const { result } = renderHook(() =>
      useRoomMapData({
        plane: 'earth',
        zone: 'arkhamcity',
        filterExplored: true,
        authToken: 'test-token',
      })
    );

    await waitFor(() => {
      expect(result.current.isLoading).toBe(false);
    });

    expect(fetchSpy).toHaveBeenCalledWith(expect.stringContaining('filter_explored=true'), expect.any(Object));
  });

  it('should not include filter_explored parameter when filterExplored is false', async () => {
    fetchSpy.mockResolvedValueOnce({
      ok: true,
      json: async () => ({
        rooms: [],
        total: 0,
      }),
    } as unknown as Response);

    const { result } = renderHook(() =>
      useRoomMapData({
        plane: 'earth',
        zone: 'arkhamcity',
        filterExplored: false,
      })
    );

    await waitFor(() => {
      expect(result.current.isLoading).toBe(false);
    });

    expect(fetchSpy).toHaveBeenCalledWith(expect.stringContaining('filter_explored=false'), expect.any(Object));
  });
});
