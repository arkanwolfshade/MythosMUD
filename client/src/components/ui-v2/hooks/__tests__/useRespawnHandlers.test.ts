import { renderHook, waitFor } from '@testing-library/react';
import { beforeEach, describe, expect, it, vi } from 'vitest';
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

// Mock fetch
global.fetch = vi.fn();

describe('useRespawnHandlers', () => {
  const mockSetGameState = vi.fn();
  const mockSetIsDead = vi.fn();
  const mockSetIsMortallyWounded = vi.fn();
  const mockSetIsRespawning = vi.fn();
  const mockSetIsDelirious = vi.fn();
  const mockSetIsDeliriumRespawning = vi.fn();

  const defaultParams = {
    authToken: 'test-token',
    setGameState: mockSetGameState,
    setIsDead: mockSetIsDead,
    setIsMortallyWounded: mockSetIsMortallyWounded,
    setIsRespawning: mockSetIsRespawning,
    setIsDelirious: mockSetIsDelirious,
    setIsDeliriumRespawning: mockSetIsDeliriumRespawning,
  };

  beforeEach(() => {
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

      (global.fetch as ReturnType<typeof vi.fn>).mockResolvedValueOnce({
        ok: true,
        json: async () => mockRespawnData,
      });

      const { result } = renderHook(() => useRespawnHandlers(defaultParams));

      await result.current.handleRespawn();

      await waitFor(() => {
        expect(mockSetIsRespawning).toHaveBeenCalledWith(true);
        expect(mockSetIsDead).toHaveBeenCalledWith(false);
        expect(mockSetIsMortallyWounded).toHaveBeenCalledWith(false);
        expect(mockSetIsRespawning).toHaveBeenCalledWith(false);
        expect(mockSetGameState).toHaveBeenCalled();
      });

      expect(global.fetch).toHaveBeenCalledWith('/api/players/respawn', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: 'Bearer test-token',
        },
      });
    });

    it('should handle respawn API error', async () => {
      const errorData = { detail: 'Respawn failed' };

      (global.fetch as ReturnType<typeof vi.fn>).mockResolvedValueOnce({
        ok: false,
        status: 400,
        json: async () => errorData,
      });

      const { result } = renderHook(() => useRespawnHandlers(defaultParams));

      await result.current.handleRespawn();

      await waitFor(() => {
        expect(mockSetIsRespawning).toHaveBeenCalledWith(true);
        expect(mockSetIsRespawning).toHaveBeenCalledWith(false);
        expect(mockSetGameState).toHaveBeenCalled();
      });
    });

    it('should handle network error during respawn', async () => {
      (global.fetch as ReturnType<typeof vi.fn>).mockRejectedValueOnce(new Error('Network error'));

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

      (global.fetch as ReturnType<typeof vi.fn>).mockResolvedValueOnce({
        ok: true,
        json: async () => mockRespawnData,
      });

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

      (global.fetch as ReturnType<typeof vi.fn>).mockResolvedValueOnce({
        ok: true,
        json: async () => mockRespawnData,
      });

      const { result } = renderHook(() => useRespawnHandlers(defaultParams));

      await result.current.handleDeliriumRespawn();

      await waitFor(() => {
        expect(mockSetIsDeliriumRespawning).toHaveBeenCalledWith(true);
        expect(mockSetIsDelirious).toHaveBeenCalledWith(false);
        expect(mockSetIsDeliriumRespawning).toHaveBeenCalledWith(false);
        expect(mockSetGameState).toHaveBeenCalled();
      });

      expect(global.fetch).toHaveBeenCalledWith('/api/players/respawn-delirium', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: 'Bearer test-token',
        },
      });
    });

    it('should handle delirium respawn API error', async () => {
      const errorData = { detail: 'Delirium respawn failed' };

      (global.fetch as ReturnType<typeof vi.fn>).mockResolvedValueOnce({
        ok: false,
        status: 400,
        json: async () => errorData,
      });

      const { result } = renderHook(() => useRespawnHandlers(defaultParams));

      await result.current.handleDeliriumRespawn();

      await waitFor(() => {
        expect(mockSetIsDeliriumRespawning).toHaveBeenCalledWith(true);
        expect(mockSetIsDeliriumRespawning).toHaveBeenCalledWith(false);
        expect(mockSetGameState).toHaveBeenCalled();
      });
    });

    it('should handle network error during delirium respawn', async () => {
      (global.fetch as ReturnType<typeof vi.fn>).mockRejectedValueOnce(new Error('Network error'));

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

      (global.fetch as ReturnType<typeof vi.fn>).mockResolvedValueOnce({
        ok: true,
        json: async () => mockRespawnData,
      });

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

      (global.fetch as ReturnType<typeof vi.fn>).mockResolvedValueOnce({
        ok: true,
        json: async () => mockRespawnData,
      });

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

      (global.fetch as ReturnType<typeof vi.fn>).mockResolvedValueOnce({
        ok: false,
        status: 400,
        json: async () => errorData,
      });

      const { result } = renderHook(() => useRespawnHandlers(defaultParams));

      await result.current.handleRespawn();

      await waitFor(() => {
        expect(mockSetGameState).toHaveBeenCalled();
      });
    });

    it('should handle JSON parse error', async () => {
      (global.fetch as ReturnType<typeof vi.fn>).mockResolvedValueOnce({
        ok: false,
        status: 400,
        json: async () => {
          throw new Error('Invalid JSON');
        },
      });

      const { result } = renderHook(() => useRespawnHandlers(defaultParams));

      // The function should handle the error gracefully
      await result.current.handleRespawn();

      await waitFor(() => {
        expect(mockSetIsRespawning).toHaveBeenCalledWith(false);
        expect(mockSetGameState).toHaveBeenCalled();
      });
    });
  });
});
