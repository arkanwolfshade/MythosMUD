import { renderHook, waitFor } from '@testing-library/react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import { useRespawnHandlers } from '../useRespawnHandlers';

// Mock logger so error-path tests do not write to stderr (same module as useRespawnHandlers)
vi.mock('@/utils/logger', () => ({
  logger: {
    info: vi.fn(),
    error: vi.fn(),
  },
}));

// Mock fetch using vi.spyOn for proper cleanup
const fetchSpy = vi.spyOn(globalThis, 'fetch');

describe('useRespawnHandlers', () => {
  const mockSetIsRespawning = vi.fn();
  const mockSetIsDeliriumRespawning = vi.fn();
  const mockAppendLocalEvent = vi.fn();

  const defaultParams = {
    authToken: 'test-token',
    setIsRespawning: mockSetIsRespawning,
    setIsDeliriumRespawning: mockSetIsDeliriumRespawning,
    appendLocalEvent: mockAppendLocalEvent,
  };

  beforeEach(() => {
    fetchSpy.mockClear();
    vi.clearAllMocks();
  });

  describe('handleRespawn', () => {
    it('should successfully respawn player without fabricating an event', async () => {
      const mockRespawnData = {
        player: { id: 'player1', name: 'Player', dp: 100 },
        room: { id: 'room2', name: 'Hospital', description: 'Hospital room', exits: {} },
      };

      fetchSpy.mockResolvedValueOnce({
        ok: true,
        json: async () => mockRespawnData,
      } as unknown as Response);

      const { result } = renderHook(() => useRespawnHandlers(defaultParams));

      await result.current.handleRespawn();

      await waitFor(() => {
        expect(mockSetIsRespawning).toHaveBeenCalledWith(true);
        expect(mockSetIsRespawning).toHaveBeenCalledWith(false);
        // Success is server-pushed (player_respawned over the websocket) -- the hook fabricates nothing.
        expect(mockAppendLocalEvent).not.toHaveBeenCalled();
      });

      expect(fetchSpy).toHaveBeenCalledWith('/v1/api/players/respawn', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: 'Bearer test-token',
        },
      });
    });

    it('should append a local error event on respawn API error', async () => {
      const errorData = { detail: 'Respawn failed' };

      fetchSpy.mockResolvedValueOnce({
        ok: false,
        status: 400,
        json: async () => errorData,
      } as unknown as Response);

      const { result } = renderHook(() => useRespawnHandlers(defaultParams));

      await result.current.handleRespawn();

      await waitFor(() => {
        expect(mockSetIsRespawning).toHaveBeenCalledWith(true);
        expect(mockSetIsRespawning).toHaveBeenCalledWith(false);
        expect(mockAppendLocalEvent).toHaveBeenCalledWith(
          expect.objectContaining({
            event_type: 'client_message',
            data: expect.objectContaining({ text: expect.stringContaining('Respawn failed'), messageType: 'error' }),
          })
        );
      });
    });

    it('should append a local error event on network error during respawn', async () => {
      fetchSpy.mockRejectedValueOnce(new Error('Network error'));

      const { result } = renderHook(() => useRespawnHandlers(defaultParams));

      await result.current.handleRespawn();

      await waitFor(() => {
        expect(mockSetIsRespawning).toHaveBeenCalledWith(true);
        expect(mockSetIsRespawning).toHaveBeenCalledWith(false);
        expect(mockAppendLocalEvent).toHaveBeenCalledWith(
          expect.objectContaining({ data: expect.objectContaining({ messageType: 'error' }) })
        );
      });
    });
  });

  describe('handleDeliriumRespawn', () => {
    it('should successfully respawn from delirium without fabricating an event', async () => {
      const mockRespawnData = {
        player: { id: 'player1', name: 'Player', lucidity: 50, dp: 100 },
        room: { id: 'room3', name: 'Sanitarium', description: 'Sanitarium room', exits: {} },
        message: 'You have been restored to lucidity',
      };

      fetchSpy.mockResolvedValueOnce({
        ok: true,
        json: async () => mockRespawnData,
      } as unknown as Response);

      const { result } = renderHook(() => useRespawnHandlers(defaultParams));

      await result.current.handleDeliriumRespawn();

      await waitFor(() => {
        expect(mockSetIsDeliriumRespawning).toHaveBeenCalledWith(true);
        expect(mockSetIsDeliriumRespawning).toHaveBeenCalledWith(false);
        expect(mockAppendLocalEvent).not.toHaveBeenCalled();
      });

      expect(globalThis.fetch).toHaveBeenCalledWith('/v1/api/players/respawn-delirium', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: 'Bearer test-token',
        },
      });
    });

    it('should append a local error event on delirium respawn API error', async () => {
      const errorData = { detail: 'Delirium respawn failed' };

      fetchSpy.mockResolvedValueOnce({
        ok: false,
        status: 400,
        json: async () => errorData,
      } as unknown as Response);

      const { result } = renderHook(() => useRespawnHandlers(defaultParams));

      await result.current.handleDeliriumRespawn();

      await waitFor(() => {
        expect(mockSetIsDeliriumRespawning).toHaveBeenCalledWith(true);
        expect(mockSetIsDeliriumRespawning).toHaveBeenCalledWith(false);
        expect(mockAppendLocalEvent).toHaveBeenCalled();
      });
    });

    it('should append a local error event on network error during delirium respawn', async () => {
      fetchSpy.mockRejectedValueOnce(new Error('Network error'));

      const { result } = renderHook(() => useRespawnHandlers(defaultParams));

      await result.current.handleDeliriumRespawn();

      await waitFor(() => {
        expect(mockSetIsDeliriumRespawning).toHaveBeenCalledWith(true);
        expect(mockSetIsDeliriumRespawning).toHaveBeenCalledWith(false);
        expect(mockAppendLocalEvent).toHaveBeenCalled();
      });
    });
  });

  describe('Error Handling', () => {
    it('should handle error without detail field', async () => {
      const errorData = {};

      fetchSpy.mockResolvedValueOnce({
        ok: false,
        status: 400,
        json: async () => errorData,
      } as unknown as Response);

      const { result } = renderHook(() => useRespawnHandlers(defaultParams));

      await result.current.handleRespawn();

      await waitFor(() => {
        expect(mockAppendLocalEvent).toHaveBeenCalledWith(
          expect.objectContaining({ data: expect.objectContaining({ text: expect.stringContaining('Unknown error') }) })
        );
      });
    });

    it('should handle JSON parse error', async () => {
      fetchSpy.mockResolvedValueOnce({
        ok: false,
        status: 400,
        json: async () => {
          throw new Error('Invalid JSON');
        },
      } as unknown as Response);

      const { result } = renderHook(() => useRespawnHandlers(defaultParams));

      // The function should handle the error gracefully
      await result.current.handleRespawn();

      await waitFor(() => {
        expect(mockSetIsRespawning).toHaveBeenCalledWith(false);
        expect(mockAppendLocalEvent).toHaveBeenCalled();
      });
    });
  });

  afterEach(() => {
    // Use mockReset instead of mockRestore to keep the spy active across tests
    // This prevents issues where mockRestore might restore an undefined/broken fetch implementation
    fetchSpy.mockReset();
  });
});
