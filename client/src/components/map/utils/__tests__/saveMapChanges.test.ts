/**
 * Tests for saveMapChanges utility.
 */

import type { Edge } from 'reactflow';
import { beforeEach, describe, expect, it, vi } from 'vitest';
import type { MapEditingChanges } from '../../hooks/useMapEditing';
import { saveMapChanges, saveNodePositions } from '../saveMapChanges';

// Mock fetch
globalThis.fetch = vi.fn();

// Mock config
vi.mock('../../../utils/config', () => ({
  getApiBaseUrl: () => 'http://localhost:54731',
}));

describe('saveMapChanges', () => {
  beforeEach(() => {
    vi.clearAllMocks();
    vi.mocked(fetch).mockResolvedValue({
      ok: true,
      json: () => Promise.resolve({}),
    } as Response);
  });

  describe('saveNodePositions', () => {
    it('should save node positions', async () => {
      const nodePositions = new Map([
        ['room1', { x: 100, y: 200 }],
        ['room2', { x: 300, y: 400 }],
      ]);

      await saveNodePositions(nodePositions, { authToken: 'test-token' });

      // Filter out debug logging calls (to debug endpoint) and count only API calls
      const apiCalls = vi
        .mocked(fetch)
        .mock.calls.filter(call => typeof call[0] === 'string' && call[0].includes('/api/rooms'));

      expect(apiCalls).toHaveLength(2);
      expect(fetch).toHaveBeenCalledWith(
        expect.stringContaining('/api/rooms/room1/position'),
        expect.objectContaining({
          method: 'POST',
          headers: expect.objectContaining({
            Authorization: 'Bearer test-token',
          }),
        })
      );
    });

    it('should handle errors when saving positions', async () => {
      vi.mocked(fetch).mockResolvedValue({
        ok: false,
        status: 500,
        json: () => Promise.resolve({ detail: 'Server error' }),
      } as Response);

      const nodePositions = new Map([['room1', { x: 100, y: 200 }]]);

      await expect(saveNodePositions(nodePositions, {})).rejects.toThrow();
    });

    it('should use custom baseUrl when provided', async () => {
      const nodePositions = new Map([['room1', { x: 100, y: 200 }]]);

      await saveNodePositions(nodePositions, { baseUrl: 'https://custom-url.com' });

      expect(fetch).toHaveBeenCalledWith(expect.stringContaining('https://custom-url.com'), expect.anything());
    });
  });

  describe('saveMapChanges', () => {
    it('should save node positions when present', async () => {
      const changes: MapEditingChanges = {
        nodePositions: new Map([['room1', { x: 100, y: 200 }]]),
        newEdges: [],
        deletedEdgeIds: [],
        edgeUpdates: new Map(),
        roomUpdates: new Map(),
      };

      await saveMapChanges(changes, { authToken: 'test-token' });

      expect(fetch).toHaveBeenCalled();
    });

    it('should handle empty changes', async () => {
      const changes: MapEditingChanges = {
        nodePositions: new Map(),
        newEdges: [],
        deletedEdgeIds: [],
        edgeUpdates: new Map(),
        roomUpdates: new Map(),
      };

      await saveMapChanges(changes, {});

      // With the fix, no fetch calls should be made (including debug logs) when there are no changes
      expect(fetch).not.toHaveBeenCalled();
    });

    it('should handle edge changes (placeholder)', async () => {
      const changes: MapEditingChanges = {
        nodePositions: new Map(),
        newEdges: [{ id: 'edge1', source: 'room1', target: 'room2' }] as Edge[],
        deletedEdgeIds: [],
        edgeUpdates: new Map(),
        roomUpdates: new Map(),
      };

      const consoleWarnSpy = vi.spyOn(console, 'warn').mockImplementation(() => {});

      await saveMapChanges(changes, {});

      expect(consoleWarnSpy).toHaveBeenCalled();
      consoleWarnSpy.mockRestore();
    });

    it('should handle room updates (placeholder)', async () => {
      const changes: MapEditingChanges = {
        nodePositions: new Map(),
        newEdges: [],
        deletedEdgeIds: [],
        edgeUpdates: new Map(),
        roomUpdates: new Map([['room1', { name: 'Updated Room' }]]),
      };

      const consoleWarnSpy = vi.spyOn(console, 'warn').mockImplementation(() => {});

      await saveMapChanges(changes, {});

      expect(consoleWarnSpy).toHaveBeenCalled();
      consoleWarnSpy.mockRestore();
    });
  });
});
