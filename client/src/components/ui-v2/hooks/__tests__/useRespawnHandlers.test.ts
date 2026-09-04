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

vi.mock('../utils/messageUtils', () => ({
  sanitizeChatMessageForState: (message: unknown) => message,
}));

// Mock fetch using vi.spyOn for proper cleanup
const fetchSpy = vi.spyOn(globalThis, 'fetch');

describe('useRespawnHandlers', () => {
  const mockSetGameState = vi.fn();
  const mockSetIsDead = vi.fn();
  const mockSetIsMortallyWounded = vi.fn();
  const mockSetIsRespawning = vi.fn();
  const mockSetIsDelirious = vi.fn();
  const mockSetIsDeliriumRespawning = vi.fn();
  const mockSetHasRespawned = vi.fn();
  const mockAppendRespawnEvent = vi.fn();

  const defaultParams = {
    authToken: 'test-token',
    setGameState: mockSetGameState,
    setIsDead: mockSetIsDead,
    setIsMortallyWounded: mockSetIsMortallyWounded,
    setIsRespawning: mockSetIsRespawning,
    setIsDelirious: mockSetIsDelirious,
    setIsDeliriumRespawning: mockSetIsDeliriumRespawning,
    setHasRespawned: mockSetHasRespawned,
    appendRespawnEvent: mockAppendRespawnEvent,
  };

  beforeEach(() => {
    fetchSpy.mockClear();
    vi.clearAllMocks();
    mockSetGameState.mockImplementation((updater: unknown) => {
      if (typeof updater === 'function') {
        return updater({
          player: { id: 'player1', name: 'Player', stats: { current_dp: 0, lucidity: 0 } },
          room: { id: 'room1', name: 'Room', description: 'A room', exits: {} },
          messages: [],
        });
      }
    });
  });

  describe('handleRespawn', () => {
    it('should successfully respawn player', async () => {
      const mockRespawnData = {
        player: { id: 'player1', name: 'Player', dp: 100 },
        room: { id: 'room2', name: 'Hospital', description: 'Hospital room', exits: {} },
      };

      // Mock respawn API then optional agent-log fetch (hook issues a second fetch in success path)
      fetchSpy
        .mockResolvedValueOnce({
          ok: true,
          json: async () => mockRespawnData,
        } as unknown as Response)
        .mockResolvedValueOnce({ ok: true, json: async () => ({}) } as unknown as Response);

      const { result } = renderHook(() => useRespawnHandlers(defaultParams));

      await result.current.handleRespawn();

      await waitFor(() => {
        expect(mockSetIsRespawning).toHaveBeenCalledWith(true);
        expect(mockSetIsDead).toHaveBeenCalledWith(false);
        expect(mockSetIsMortallyWounded).toHaveBeenCalledWith(false);
        expect(mockSetIsRespawning).toHaveBeenCalledWith(false);
        // Success path routes state exclusively through the projector (#776) -- no direct write.
        expect(mockAppendRespawnEvent).toHaveBeenCalled();
        expect(mockSetGameState).not.toHaveBeenCalled();
      });

      expect(fetchSpy).toHaveBeenCalledWith('/v1/api/players/respawn', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: 'Bearer test-token',
        },
      });
    });

    it('should handle respawn API error', async () => {
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
        expect(mockSetGameState).toHaveBeenCalled();
      });
    });

    it('should handle network error during respawn', async () => {
      fetchSpy.mockRejectedValueOnce(new Error('Network error'));

      const { result } = renderHook(() => useRespawnHandlers(defaultParams));

      await result.current.handleRespawn();

      await waitFor(() => {
        expect(mockSetIsRespawning).toHaveBeenCalledWith(true);
        expect(mockSetIsRespawning).toHaveBeenCalledWith(false);
        expect(mockSetGameState).toHaveBeenCalled();
      });
    });

    it('appends a player_respawned event carrying player, room, and message (#776)', async () => {
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
        expect(mockAppendRespawnEvent).toHaveBeenCalledWith(
          expect.objectContaining({
            event_type: 'player_respawned',
            data: expect.objectContaining({
              player: expect.objectContaining({ id: 'player1', name: 'Player' }),
              room: mockRespawnData.room,
              message: expect.any(String),
            }),
          })
        );
      });
    });

    it('does not directly set a room with empty occupants on respawn success (#776)', async () => {
      // The invariant this issue is about: no write, direct or otherwise, should ever produce a
      // state with a room set and players empty. Since success now routes only through the
      // projector event (asserted above), the only way to violate that is a direct setGameState
      // call -- which must not happen at all on the success path.
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
        expect(mockAppendRespawnEvent).toHaveBeenCalled();
      });
      expect(mockSetGameState).not.toHaveBeenCalled();
    });
  });

  describe('handleDeliriumRespawn', () => {
    it('should successfully respawn from delirium', async () => {
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
        expect(mockSetIsDelirious).toHaveBeenCalledWith(false);
        expect(mockSetIsDeliriumRespawning).toHaveBeenCalledWith(false);
        // Success path routes state exclusively through the projector (#776) -- no direct write.
        expect(mockAppendRespawnEvent).toHaveBeenCalled();
        expect(mockSetGameState).not.toHaveBeenCalled();
      });

      expect(globalThis.fetch).toHaveBeenCalledWith('/v1/api/players/respawn-delirium', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: 'Bearer test-token',
        },
      });
    });

    it('should handle delirium respawn API error', async () => {
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
        expect(mockSetGameState).toHaveBeenCalled();
      });
    });

    it('should handle network error during delirium respawn', async () => {
      fetchSpy.mockRejectedValueOnce(new Error('Network error'));

      const { result } = renderHook(() => useRespawnHandlers(defaultParams));

      await result.current.handleDeliriumRespawn();

      await waitFor(() => {
        expect(mockSetIsDeliriumRespawning).toHaveBeenCalledWith(true);
        expect(mockSetIsDeliriumRespawning).toHaveBeenCalledWith(false);
        expect(mockSetGameState).toHaveBeenCalled();
      });
    });

    it('uses default message when respawn message is not provided', async () => {
      const mockRespawnData = {
        player: { id: 'player1', name: 'Player', lucidity: 50, dp: 100 },
        room: { id: 'room3', name: 'Sanitarium', description: 'Sanitarium room', exits: {} },
      };

      fetchSpy.mockResolvedValueOnce({
        ok: true,
        json: async () => mockRespawnData,
      } as unknown as Response);

      const { result } = renderHook(() => useRespawnHandlers(defaultParams));

      await result.current.handleDeliriumRespawn();

      await waitFor(() => {
        expect(mockAppendRespawnEvent).toHaveBeenCalledWith(
          expect.objectContaining({
            data: expect.objectContaining({
              message: 'You have been restored to lucidity and returned to the Sanitarium',
            }),
          })
        );
      });
    });

    it('appends a player_delirium_respawned event carrying player, room, and message (#776)', async () => {
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
        expect(mockAppendRespawnEvent).toHaveBeenCalledWith(
          expect.objectContaining({
            event_type: 'player_delirium_respawned',
            data: expect.objectContaining({
              player: expect.objectContaining({
                id: 'player1',
                name: 'Player',
                stats: expect.objectContaining({ lucidity: 50, current_dp: 100 }),
              }),
              room: mockRespawnData.room,
              message: 'You have been restored to lucidity',
            }),
          })
        );
      });
      expect(mockSetGameState).not.toHaveBeenCalled();
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
        expect(mockSetGameState).toHaveBeenCalled();
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
        expect(mockSetGameState).toHaveBeenCalled();
      });
    });
  });

  afterEach(() => {
    // Use mockReset instead of mockRestore to keep the spy active across tests
    // This prevents issues where mockRestore might restore an undefined/broken fetch implementation
    fetchSpy.mockReset();
  });
});
