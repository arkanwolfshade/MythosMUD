import { renderHook, waitFor } from '@testing-library/react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import { useRespawnHandlers } from '../useRespawnHandlers';

// Mock dependencies
vi.mock('../../../utils/logger', () => ({
  logger: {
    info: vi.fn(),
    error: vi.fn(),
  },
}));

vi.mock('../utils/messageUtils', () => ({
  sanitizeChatMessageForState: (message: unknown) => message,
}));

// Mock fetch using vi.spyOn for proper cleanup
const fetchSpy = vi.spyOn(global, 'fetch');

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
        expect(mockSetGameState).toHaveBeenCalled();
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

    it('should update game state with respawned player data', async () => {
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
        expect(mockSetGameState).toHaveBeenCalled();
      });
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
        expect(mockSetGameState).toHaveBeenCalled();
      });

      expect(global.fetch).toHaveBeenCalledWith('/v1/api/players/respawn-delirium', {
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

    it('should use default message when respawn message is not provided', async () => {
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
        expect(mockSetGameState).toHaveBeenCalled();
      });
    });

    it('should update game state with respawned player data including lucidity', async () => {
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
        expect(mockSetGameState).toHaveBeenCalled();
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
