/**
 * Unit tests for map API client (fetchAsciiMap, fetchAsciiMinimap).
 * Guards against regressions in URL building, auth headers, and response validation.
 */

import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import { fetchAsciiMap, fetchAsciiMinimap } from '../maps';

describe('maps API', () => {
  const originalFetch = globalThis.fetch;

  beforeEach(() => {
    globalThis.fetch = vi.fn();
  });

  afterEach(() => {
    globalThis.fetch = originalFetch;
  });

  describe('fetchAsciiMinimap', () => {
    it('builds URL with plane, zone, sub_zone, current_room_id, size', async () => {
      vi.mocked(fetch).mockResolvedValue({
        ok: true,
        json: async () => ({ map_html: '' }),
      } as Response);

      await fetchAsciiMinimap({
        plane: 'material',
        zone: 'arkham',
        subZone: 'miskatonic',
        currentRoomId: 'material_arkham_miskatonic_101',
        size: 5,
        baseUrl: 'https://api.example.com',
        authToken: 'token',
      });

      const callUrl = (fetch as ReturnType<typeof vi.fn>).mock.calls[0][0];
      expect(callUrl).toContain('/api/maps/ascii/minimap');
      expect(callUrl).toContain('plane=material');
      expect(callUrl).toContain('zone=arkham');
      expect(callUrl).toContain('sub_zone=miskatonic');
      expect(callUrl).toContain('current_room_id=material_arkham_miskatonic_101');
      expect(callUrl).toContain('size=5');
    });

    it('sends Authorization header when authToken provided', async () => {
      vi.mocked(fetch).mockResolvedValue({
        ok: true,
        json: async () => ({ map_html: '' }),
      } as Response);

      await fetchAsciiMinimap({
        plane: 'p',
        zone: 'z',
        authToken: 'BearerToken',
      });

      const callOptions = (fetch as ReturnType<typeof vi.fn>).mock.calls[0][1];
      expect(callOptions?.headers).toBeDefined();
      const headers = callOptions?.headers as HeadersInit;
      const auth = Array.isArray(headers)
        ? headers.find(([k]) => k === 'Authorization')?.[1]
        : (headers as Record<string, string>)?.Authorization;
      expect(auth).toBe('Bearer BearerToken');
    });

    it('throws on non-OK response', async () => {
      vi.mocked(fetch).mockResolvedValue({
        ok: false,
        statusText: 'Unauthorized',
      } as Response);

      await expect(fetchAsciiMinimap({ plane: 'p', zone: 'z' })).rejects.toThrow(
        'Failed to fetch minimap: Unauthorized'
      );
    });

    it('throws when response shape is invalid (map_html not string)', async () => {
      vi.mocked(fetch).mockResolvedValue({
        ok: true,
        json: async () => ({ map_html: 123 }),
      } as Response);

      await expect(fetchAsciiMinimap({ plane: 'p', zone: 'z' })).rejects.toThrow('Invalid minimap response');
    });

    it('returns map_html and viewport when valid', async () => {
      vi.mocked(fetch).mockResolvedValue({
        ok: true,
        json: async () => ({ map_html: '<div>minimap</div>', viewport: { x: 0, y: 0 } }),
      } as Response);

      const result = await fetchAsciiMinimap({ plane: 'p', zone: 'z' });

      expect(result.map_html).toBe('<div>minimap</div>');
      expect(result.viewport).toEqual({ x: 0, y: 0 });
    });
  });

  describe('fetchAsciiMap', () => {
    it('builds URL with viewport and viewport dimensions', async () => {
      vi.mocked(fetch).mockResolvedValue({
        ok: true,
        json: async () => ({ map_html: '', viewport: { x: 0, y: 0 } }),
      } as Response);

      await fetchAsciiMap({
        plane: 'material',
        zone: 'arkham',
        viewportX: 1,
        viewportY: 2,
        viewportWidth: 40,
        viewportHeight: 12,
      });

      const callUrl = (fetch as ReturnType<typeof vi.fn>).mock.calls[0][0];
      expect(callUrl).toContain('/api/maps/ascii');
      expect(callUrl).toContain('viewport_x=1');
      expect(callUrl).toContain('viewport_y=2');
      expect(callUrl).toContain('viewport_width=40');
      expect(callUrl).toContain('viewport_height=12');
    });

    it('throws on non-OK response', async () => {
      vi.mocked(fetch).mockResolvedValue({
        ok: false,
        statusText: 'Internal Server Error',
      } as Response);

      await expect(fetchAsciiMap({ plane: 'p', zone: 'z' })).rejects.toThrow(
        'Failed to fetch map: Internal Server Error'
      );
    });

    it('throws when response shape is invalid (viewport not object)', async () => {
      vi.mocked(fetch).mockResolvedValue({
        ok: true,
        json: async () => ({ map_html: '', viewport: 'invalid' }),
      } as Response);

      await expect(fetchAsciiMap({ plane: 'p', zone: 'z' })).rejects.toThrow('Invalid map response');
    });
  });
});
