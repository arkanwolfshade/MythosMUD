/**
 * Unit tests for useAsciiMap hook.
 * Guards against regressions of map fetch, viewport sync, and zone/room-driven resets.
 */

import { act, renderHook, waitFor } from '@testing-library/react';
import { beforeEach, describe, expect, it, vi } from 'vitest';
import { fetchAsciiMap } from '../../../api/maps';
import { useAsciiMap } from '../useAsciiMap';

vi.mock('../../../api/maps', () => ({
  fetchAsciiMap: vi.fn(),
}));

describe('useAsciiMap', () => {
  const defaultParams = {
    plane: 'material',
    zone: 'arkham',
    subZone: undefined,
    currentRoomId: undefined,
    viewportWidth: 80,
    viewportHeight: 24,
    baseUrl: '',
    authToken: undefined,
  };

  beforeEach(() => {
    vi.mocked(fetchAsciiMap).mockResolvedValue({
      map_html: '<div class="map">#</div>',
      viewport: { x: 0, y: 0 },
    });
  });

  it('starts in loading state then shows map HTML after fetch', async () => {
    const { result } = renderHook(() => useAsciiMap(defaultParams));

    expect(result.current.isLoading).toBe(true);
    expect(result.current.mapHtml).toBe('');

    await waitFor(() => {
      expect(result.current.isLoading).toBe(false);
    });

    expect(result.current.mapHtml).toContain('map');
    expect(fetchAsciiMap).toHaveBeenCalledWith(
      expect.objectContaining({
        plane: 'material',
        zone: 'arkham',
        viewportWidth: 80,
        viewportHeight: 24,
      })
    );
  });

  it('syncs viewport from server response when server returns different x,y', async () => {
    vi.mocked(fetchAsciiMap).mockResolvedValue({
      map_html: '',
      viewport: { x: 10, y: 5 },
    });

    const { result } = renderHook(() => useAsciiMap(defaultParams));

    await waitFor(() => {
      expect(result.current.isLoading).toBe(false);
    });

    expect(result.current.viewport).toEqual({ x: 10, y: 5 });
  });

  it('sets error and clears map HTML when fetch throws', async () => {
    vi.mocked(fetchAsciiMap).mockRejectedValue(new Error('Network error'));

    const { result } = renderHook(() => useAsciiMap(defaultParams));

    await waitFor(() => {
      expect(result.current.isLoading).toBe(false);
    });

    expect(result.current.error).toBe('Network error');
    expect(result.current.mapHtml).toBe('');
  });

  it('fetchMap can be called to retry', async () => {
    vi.mocked(fetchAsciiMap)
      .mockRejectedValueOnce(new Error('Fail'))
      .mockResolvedValueOnce({ map_html: '<div>ok</div>', viewport: { x: 0, y: 0 } });

    const { result } = renderHook(() => useAsciiMap(defaultParams));

    await waitFor(() => {
      expect(result.current.error).toBe('Fail');
    });

    await act(async () => {
      await result.current.fetchMap();
    });

    expect(result.current.mapHtml).toContain('ok');
    expect(result.current.error).toBeNull();
  });

  it('returns selected plane/zone/subZone matching initial params and setters', async () => {
    const { result } = renderHook(() => useAsciiMap(defaultParams));

    expect(result.current.selectedPlane).toBe('material');
    expect(result.current.selectedZone).toBe('arkham');
    expect(result.current.selectedSubZone).toBeUndefined();
    expect(typeof result.current.setSelectedPlane).toBe('function');
    expect(typeof result.current.setSelectedZone).toBe('function');
    expect(typeof result.current.setSelectedSubZone).toBe('function');
  });
});
