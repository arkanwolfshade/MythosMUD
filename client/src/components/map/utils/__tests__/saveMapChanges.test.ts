/**
 * Tests for saveMapChanges utility.
 */

import type { Edge } from 'reactflow';
import { beforeEach, describe, expect, it, vi } from 'vitest';
import type { MapEditingChanges } from '../../hooks/useMapEditing';
import type { ExitEdgeData } from '../../types';
import { saveEdgeChanges, saveMapChanges, saveNodePositions, saveRoomUpdates } from '../saveMapChanges';

// Mock fetch
globalThis.fetch = vi.fn();

// Mock config
vi.mock('../../../utils/config', () => ({
  getVersionedApiBaseUrl: () => '/v1',
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

      expect(fetch).toHaveBeenCalledTimes(2);
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

    it('uses same-origin relative paths when baseUrl is cleartext http', async () => {
      const nodePositions = new Map([['room1', { x: 100, y: 200 }]]);

      await saveNodePositions(nodePositions, { baseUrl: 'http://localhost:54768/v1' });

      expect(fetch).toHaveBeenCalledWith('/v1/api/rooms/room1/position', expect.anything());
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

      expect(fetch).not.toHaveBeenCalled();
    });

    it('should save edge changes when present', async () => {
      const changes: MapEditingChanges = {
        nodePositions: new Map(),
        newEdges: [
          {
            id: 'room1-north-room2',
            source: 'room1',
            target: 'room2',
            data: { direction: 'north', sourceRoomId: 'room1', targetRoomId: 'room2' },
          } as Edge<ExitEdgeData>,
        ],
        deletedEdgeIds: [],
        edgeUpdates: new Map(),
        roomUpdates: new Map(),
      };

      await saveMapChanges(changes, {});

      expect(fetch).toHaveBeenCalledWith(
        expect.stringContaining('/api/rooms/room1/exits'),
        expect.objectContaining({ method: 'POST' })
      );
    });

    it('should save room updates when present', async () => {
      const changes: MapEditingChanges = {
        nodePositions: new Map(),
        newEdges: [],
        deletedEdgeIds: [],
        edgeUpdates: new Map(),
        roomUpdates: new Map([['room1', { name: 'Updated Room' }]]),
      };

      await saveMapChanges(changes, {});

      expect(fetch).toHaveBeenCalledWith(
        expect.stringContaining('/api/rooms/room1'),
        expect.objectContaining({ method: 'PUT' })
      );
    });
  });

  describe('saveEdgeChanges', () => {
    it('deletes before it creates, for a single fetch call sequence', async () => {
      const calls: string[] = [];
      vi.mocked(fetch).mockImplementation(async (_url, init) => {
        calls.push((init as RequestInit).method as string);
        return { ok: true, json: () => Promise.resolve({}) } as Response;
      });

      const newEdges: Edge<ExitEdgeData>[] = [
        {
          id: 'room1-north-room2',
          source: 'room1',
          target: 'room2',
          data: { direction: 'north', sourceRoomId: 'room1', targetRoomId: 'room2' },
        } as Edge<ExitEdgeData>,
      ];

      await saveEdgeChanges(newEdges, ['room3-south-room4'], new Map(), {});

      expect(calls).toEqual(['DELETE', 'POST']);
    });

    it('sends exactly one create call per new edge -- no reverse exit is synthesized', async () => {
      const newEdges: Edge<ExitEdgeData>[] = [
        {
          id: 'room1-north-room2',
          source: 'room1',
          target: 'room2',
          data: { direction: 'north', sourceRoomId: 'room1', targetRoomId: 'room2' },
        } as Edge<ExitEdgeData>,
      ];

      await saveEdgeChanges(newEdges, [], new Map(), {});

      expect(fetch).toHaveBeenCalledTimes(1);
      expect(fetch).toHaveBeenCalledWith(
        expect.stringContaining('/api/rooms/room1/exits'),
        expect.objectContaining({
          method: 'POST',
          body: JSON.stringify({
            direction: 'north',
            target_room_id: 'room2',
            flags: undefined,
            description: undefined,
          }),
        })
      );
    });

    it('deletes the old exit and creates the new one when direction changes', async () => {
      const calls: Array<{ url: string; method: string }> = [];
      vi.mocked(fetch).mockImplementation(async (url, init) => {
        calls.push({ url: url as string, method: (init as RequestInit).method as string });
        return { ok: true, json: () => Promise.resolve({}) } as Response;
      });

      const edgeUpdates = new Map<string, Partial<ExitEdgeData>>([['room1-north-room2', { direction: 'south' }]]);

      await saveEdgeChanges([], [], edgeUpdates, {});

      expect(calls).toHaveLength(2);
      expect(calls[0].method).toBe('DELETE');
      expect(calls[0].url).toContain('/api/rooms/room1/exits/north');
      expect(calls[1].method).toBe('POST');
      expect(calls[1].url).toContain('/api/rooms/room1/exits');
    });

    it('sends a PUT for an in-place update (same direction)', async () => {
      const edgeUpdates = new Map<string, Partial<ExitEdgeData>>([
        ['room1-north-room2', { description: 'A new description.' }],
      ]);

      await saveEdgeChanges([], [], edgeUpdates, {});

      expect(fetch).toHaveBeenCalledWith(
        expect.stringContaining('/api/rooms/room1/exits/north'),
        expect.objectContaining({ method: 'PUT' })
      );
    });

    it('fails fast: a delete failure stops before any create runs', async () => {
      vi.mocked(fetch).mockResolvedValue({
        ok: false,
        status: 404,
        json: () => Promise.resolve({ detail: 'Exit not found' }),
      } as Response);

      const newEdges: Edge<ExitEdgeData>[] = [
        {
          id: 'room1-north-room2',
          source: 'room1',
          target: 'room2',
          data: { direction: 'north', sourceRoomId: 'room1', targetRoomId: 'room2' },
        } as Edge<ExitEdgeData>,
      ];

      await expect(saveEdgeChanges(newEdges, ['room3-south-room4'], new Map(), {})).rejects.toThrow(
        /Failed to delete exit south from room room3/
      );
      expect(fetch).toHaveBeenCalledTimes(1);
    });
  });

  describe('saveRoomUpdates', () => {
    it('sends name/description/environment, but never zone/sub_zone', async () => {
      const roomUpdates = new Map([
        [
          'room1',
          { name: 'New Name', description: 'New description.', zone: 'should_not_be_sent', environment: 'arena' },
        ],
      ]);

      await saveRoomUpdates(roomUpdates, {});

      expect(fetch).toHaveBeenCalledWith(
        expect.stringContaining('/api/rooms/room1'),
        expect.objectContaining({
          method: 'PUT',
          body: JSON.stringify({ name: 'New Name', description: 'New description.', environment: 'arena' }),
        })
      );
    });

    it('sends an explicit empty-string environment as a clear, not a no-op', async () => {
      const roomUpdates = new Map([['room1', { environment: '' }]]);

      await saveRoomUpdates(roomUpdates, {});

      expect(fetch).toHaveBeenCalledWith(
        expect.stringContaining('/api/rooms/room1'),
        expect.objectContaining({ body: JSON.stringify({ environment: '' }) })
      );
    });

    it('skips the fetch entirely when an update has no name/description/environment fields', async () => {
      const roomUpdates = new Map([['room1', { zone: 'irrelevant_here' }]]);

      await saveRoomUpdates(roomUpdates, {});

      expect(fetch).not.toHaveBeenCalled();
    });

    it('fails fast with the room id in the error message', async () => {
      vi.mocked(fetch).mockResolvedValue({
        ok: false,
        status: 422,
        json: () => Promise.resolve({ detail: 'Invalid environment' }),
      } as Response);

      const roomUpdates = new Map([['room1', { environment: 'not_real' }]]);

      await expect(saveRoomUpdates(roomUpdates, {})).rejects.toThrow(/Failed to save properties for room room1/);
    });
  });
});
