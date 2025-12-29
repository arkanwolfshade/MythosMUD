/**
 * Tests for playerHandlers.
 */

import { describe, expect, it, vi } from 'vitest';
import type { Player } from '../../types';
import {
  handlePlayerDeliriumRespawned,
  handlePlayerDied,
  handlePlayerDpUpdated,
  handlePlayerEntered,
  handlePlayerEnteredGame,
  handlePlayerLeft,
  handlePlayerLeftGame,
  handlePlayerRespawned,
  handlePlayerUpdate,
} from '../playerHandlers';
import type { EventHandlerContext } from '../types';

// Mock dependencies
vi.mock('../../../utils/healthEventUtils', () => ({
  buildHealthStatusFromEvent: vi.fn(() => ({
    current: 50,
    max: 100,
    tier: 'wounded',
    posture: 'standing',
    inCombat: false,
  })),
}));

vi.mock('../../../utils/logger', () => ({
  logger: {
    warn: vi.fn(),
  },
}));

describe('playerHandlers', () => {
  const mockAppendMessage = vi.fn();
  const mockContext: EventHandlerContext = {
    currentPlayerRef: { current: null },
    currentRoomRef: { current: null },
    currentMessagesRef: { current: [] },
    healthStatusRef: { current: null },
    lucidityStatusRef: { current: null },
    lastDaypartRef: { current: null },
    lastHourRef: { current: null },
    lastHolidayIdsRef: { current: [] },
    lastRoomUpdateTime: { current: 0 },
    setDpStatus: vi.fn(),
    setLucidityStatus: vi.fn(),
    setMythosTime: vi.fn(),
    setIsDead: vi.fn(),
    setIsMortallyWounded: vi.fn(),
    setIsRespawning: vi.fn(),
    setIsDelirious: vi.fn(),
    setIsDeliriumRespawning: vi.fn(),
    setDeathLocation: vi.fn(),
    setDeliriumLocation: vi.fn(),
    setRescueState: vi.fn(),
  };

  beforeEach(() => {
    vi.clearAllMocks();
  });

  describe('handlePlayerEnteredGame', () => {
    it('should append message when player_name is present', () => {
      const event = {
        event_type: 'player_entered_game',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { player_name: 'TestPlayer' },
      };
      handlePlayerEnteredGame(event, mockContext, mockAppendMessage);
      expect(mockAppendMessage).toHaveBeenCalledWith(
        expect.objectContaining({
          text: 'TestPlayer has entered the game.',
          messageType: 'system',
        })
      );
    });

    it('should not append message when player_name is missing', () => {
      const event = {
        event_type: 'player_entered_game',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: {},
      };
      handlePlayerEnteredGame(event, mockContext, mockAppendMessage);
      expect(mockAppendMessage).not.toHaveBeenCalled();
    });

    it('should not append message when player_name is empty string', () => {
      const event = {
        event_type: 'player_entered_game',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { player_name: '' },
      };
      handlePlayerEnteredGame(event, mockContext, mockAppendMessage);
      expect(mockAppendMessage).not.toHaveBeenCalled();
    });

    it('should not append message when player_name is whitespace', () => {
      const event = {
        event_type: 'player_entered_game',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { player_name: '   ' },
      };
      handlePlayerEnteredGame(event, mockContext, mockAppendMessage);
      expect(mockAppendMessage).not.toHaveBeenCalled();
    });
  });

  describe('handlePlayerEntered', () => {
    it('should append message when message and player_name are present', () => {
      const event = {
        event_type: 'player_entered',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { player_name: 'TestPlayer', message: 'TestPlayer enters the room.' },
      };
      handlePlayerEntered(event, mockContext, mockAppendMessage);
      expect(mockAppendMessage).toHaveBeenCalledWith(
        expect.objectContaining({
          text: 'TestPlayer enters the room.',
          messageType: 'system',
        })
      );
    });

    it('should not append message when message is missing', () => {
      const event = {
        event_type: 'player_entered',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { player_name: 'TestPlayer' },
      };
      handlePlayerEntered(event, mockContext, mockAppendMessage);
      expect(mockAppendMessage).not.toHaveBeenCalled();
    });

    it('should not append message when player_name is missing', () => {
      const event = {
        event_type: 'player_entered',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { message: 'Someone enters the room.' },
      };
      handlePlayerEntered(event, mockContext, mockAppendMessage);
      expect(mockAppendMessage).not.toHaveBeenCalled();
    });
  });

  describe('handlePlayerLeftGame', () => {
    it('should append message when player_name is present', () => {
      const event = {
        event_type: 'player_left_game',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { player_name: 'TestPlayer' },
      };
      handlePlayerLeftGame(event, mockContext, mockAppendMessage);
      expect(mockAppendMessage).toHaveBeenCalledWith(
        expect.objectContaining({
          text: 'TestPlayer has left the game.',
          messageType: 'system',
        })
      );
    });

    it('should not append message when player_name is missing', () => {
      const event = {
        event_type: 'player_left_game',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: {},
      };
      handlePlayerLeftGame(event, mockContext, mockAppendMessage);
      expect(mockAppendMessage).not.toHaveBeenCalled();
    });
  });

  describe('handlePlayerLeft', () => {
    it('should append message when message is present', () => {
      const event = {
        event_type: 'player_left',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { message: 'TestPlayer leaves the room.' },
      };
      handlePlayerLeft(event, mockContext, mockAppendMessage);
      expect(mockAppendMessage).toHaveBeenCalledWith(
        expect.objectContaining({
          text: 'TestPlayer leaves the room.',
          messageType: 'system',
        })
      );
    });

    it('should not append message when message is missing', () => {
      const event = {
        event_type: 'player_left',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: {},
      };
      handlePlayerLeft(event, mockContext, mockAppendMessage);
      expect(mockAppendMessage).not.toHaveBeenCalled();
    });
  });

  describe('handlePlayerDied', () => {
    it('should set death location and isDead when death_location is present', () => {
      const event = {
        event_type: 'player_died',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { death_location: 'Dark Forest' },
      };
      handlePlayerDied(event, mockContext, mockAppendMessage);
      expect(mockContext.setDeathLocation).toHaveBeenCalledWith('Dark Forest');
      expect(mockContext.setIsDead).toHaveBeenCalledWith(true);
    });

    it('should use room_id as death location when death_location is missing', () => {
      const event = {
        event_type: 'player_died',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { room_id: 'room_123' },
      };
      handlePlayerDied(event, mockContext, mockAppendMessage);
      expect(mockContext.setDeathLocation).toHaveBeenCalledWith('room_123');
      expect(mockContext.setIsDead).toHaveBeenCalledWith(true);
    });

    it('should use default location when neither death_location nor room_id is present', () => {
      const event = {
        event_type: 'player_died',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: {},
      };
      handlePlayerDied(event, mockContext, mockAppendMessage);
      expect(mockContext.setDeathLocation).toHaveBeenCalledWith('Unknown Location');
      expect(mockContext.setIsDead).toHaveBeenCalledWith(true);
    });
  });

  describe('handlePlayerRespawned', () => {
    it('should update player state and set isDead to false', () => {
      const mockPlayer = {
        id: 'player1',
        name: 'TestPlayer',
        stats: { current_dp: 100, max_dp: 100, position: 'standing' },
        in_combat: false,
      };
      mockContext.healthStatusRef.current = {
        current: 0,
        max: 100,
        tier: 'vigorous',
        posture: 'standing',
        inCombat: false,
      };
      const event = {
        event_type: 'player_respawned',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { player: mockPlayer },
      };
      const result = handlePlayerRespawned(event, mockContext, mockAppendMessage);
      expect(mockContext.setIsDead).toHaveBeenCalledWith(false);
      expect(mockContext.setIsMortallyWounded).toHaveBeenCalledWith(false);
      expect(mockContext.setIsRespawning).toHaveBeenCalledWith(false);
      expect(result?.player).toBeDefined();
      expect(mockContext.setDpStatus).toHaveBeenCalled();
    });

    it('should handle respawn without player data', () => {
      const event = {
        event_type: 'player_respawned',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: {},
      };
      const result = handlePlayerRespawned(event, mockContext, mockAppendMessage);
      expect(mockContext.setIsDead).toHaveBeenCalledWith(false);
      expect(result).toEqual({});
    });

    it('should handle respawn with player data but missing current_dp in stats', () => {
      const mockPlayer = {
        id: 'player1',
        name: 'TestPlayer',
        stats: { max_dp: 100, position: 'standing' }, // Missing current_dp
        in_combat: false,
      };
      const event = {
        event_type: 'player_respawned',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { player: mockPlayer },
      };
      const result = handlePlayerRespawned(event, mockContext, mockAppendMessage);
      expect(mockContext.setIsDead).toHaveBeenCalledWith(false);
      expect(result?.player).toBeDefined();
      expect(mockContext.setDpStatus).not.toHaveBeenCalled();
    });

    it('should handle respawn with message field', () => {
      const mockPlayer = {
        id: 'player1',
        name: 'TestPlayer',
        stats: { current_dp: 100, max_dp: 100, position: 'standing' },
        in_combat: false,
      };
      const event = {
        event_type: 'player_respawned',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { player: mockPlayer, message: 'You have respawned.' },
      };
      const result = handlePlayerRespawned(event, mockContext, mockAppendMessage);
      expect(result?.player).toBeDefined();
    });
  });

  describe('handlePlayerDeliriumRespawned', () => {
    it('should set isDelirious and isDeliriumRespawning to false', () => {
      const mockPlayer = {
        id: 'player1',
        name: 'TestPlayer',
        stats: { lucidity: 50, max_lucidity: 100 },
      };
      mockContext.lucidityStatusRef.current = { current: 0, max: 100, tier: 'lucid', liabilities: [] };
      const event = {
        event_type: 'player_delirium_respawned',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { player: mockPlayer },
      };
      const result = handlePlayerDeliriumRespawned(event, mockContext, mockAppendMessage);
      expect(mockContext.setIsDelirious).toHaveBeenCalledWith(false);
      expect(mockContext.setIsDeliriumRespawning).toHaveBeenCalledWith(false);
      expect(result?.player).toBeDefined();
    });

    it('should handle delirium respawn without lucidity status', () => {
      const mockPlayer = {
        id: 'player1',
        name: 'TestPlayer',
        stats: { lucidity: 50, max_lucidity: 100 },
      };
      mockContext.lucidityStatusRef.current = null;
      const event = {
        event_type: 'player_delirium_respawned',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { player: mockPlayer },
      };
      const result = handlePlayerDeliriumRespawned(event, mockContext, mockAppendMessage);
      expect(result?.player).toBeDefined();
    });
  });

  describe('handlePlayerUpdate', () => {
    it('should update player when currentPlayerRef exists', () => {
      const mockPlayer = {
        id: 'player1',
        name: 'TestPlayer',
        stats: { current_dp: 50, max_dp: 100, lucidity: 75 },
        in_combat: false,
      };
      mockContext.currentPlayerRef.current = mockPlayer as unknown as Player;
      const event = {
        event_type: 'player_update',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { in_combat: true, stats: { magic_points: 50 } },
      };
      const result = handlePlayerUpdate(event, mockContext, mockAppendMessage);
      expect(result?.player).toBeDefined();
      expect(result?.player?.in_combat).toBe(true);
    });

    it('should not update when currentPlayerRef is null', () => {
      mockContext.currentPlayerRef.current = null;
      const event = {
        event_type: 'player_update',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { in_combat: true },
      };
      const result = handlePlayerUpdate(event, mockContext, mockAppendMessage);
      expect(result).toEqual({});
    });

    it('should preserve existing stats when updating', () => {
      const mockPlayer = {
        id: 'player1',
        name: 'TestPlayer',
        stats: { current_dp: 50, max_dp: 100, lucidity: 75 },
        in_combat: false,
      };
      mockContext.currentPlayerRef.current = mockPlayer as unknown as Player;
      const event = {
        event_type: 'player_update',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { stats: { magic_points: 50 } },
      };
      const result = handlePlayerUpdate(event, mockContext, mockAppendMessage);
      expect(result?.player?.stats?.current_dp).toBe(50);
      expect(result?.player?.stats?.lucidity).toBe(75);
    });
  });

  describe('handlePlayerDpUpdated', () => {
    it('should update health status and player stats', () => {
      const mockPlayer = {
        id: 'player1',
        name: 'TestPlayer',
        stats: { current_dp: 50, max_dp: 100, lucidity: 75 },
      };
      mockContext.currentPlayerRef.current = mockPlayer as unknown as Player;
      mockContext.healthStatusRef.current = {
        current: 50,
        max: 100,
        tier: 'wounded',
        posture: 'standing',
        inCombat: false,
      };
      const event = {
        event_type: 'player_dp_updated',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { old_dp: 50, new_dp: 75, max_dp: 100, damage_taken: -25 },
      };
      const result = handlePlayerDpUpdated(event, mockContext, mockAppendMessage);
      expect(mockContext.setDpStatus).toHaveBeenCalled();
      expect(result?.player).toBeDefined();
    });

    it('should handle when currentPlayerRef is null', () => {
      mockContext.currentPlayerRef.current = null;
      mockContext.healthStatusRef.current = {
        current: 50,
        max: 100,
        tier: 'wounded',
        posture: 'standing',
        inCombat: false,
      };
      const event = {
        event_type: 'player_dp_updated',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { old_dp: 50, new_dp: 75, max_dp: 100 },
      };
      const result = handlePlayerDpUpdated(event, mockContext, mockAppendMessage);
      expect(mockContext.setDpStatus).toHaveBeenCalled();
      expect(result).toBeUndefined();
    });
  });

  describe('handlePlayerEnteredGame edge cases', () => {
    it('should not append message when player_name is not a string', () => {
      const event = {
        event_type: 'player_entered_game',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { player_name: 123 },
      };
      handlePlayerEnteredGame(event, mockContext, mockAppendMessage);
      expect(mockAppendMessage).not.toHaveBeenCalled();
    });

    it('should not append message when player_name is null', () => {
      const event = {
        event_type: 'player_entered_game',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { player_name: null },
      };
      handlePlayerEnteredGame(event, mockContext, mockAppendMessage);
      expect(mockAppendMessage).not.toHaveBeenCalled();
    });
  });

  describe('handlePlayerUpdate edge cases', () => {
    it('should handle update when stats are missing', () => {
      const mockPlayer = {
        id: 'player1',
        name: 'TestPlayer',
        stats: { current_dp: 50, max_dp: 100, lucidity: 75 },
        in_combat: false,
      };
      mockContext.currentPlayerRef.current = mockPlayer as unknown as Player;
      const event = {
        event_type: 'player_update',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { in_combat: true },
      };
      const result = handlePlayerUpdate(event, mockContext, mockAppendMessage);
      expect(result?.player).toBeDefined();
      expect(result?.player?.in_combat).toBe(true);
    });

    it('should handle update when existing stats are missing', () => {
      const mockPlayer = {
        id: 'player1',
        name: 'TestPlayer',
        // No stats property
        in_combat: false,
      };
      mockContext.currentPlayerRef.current = mockPlayer as unknown as Player;
      const event = {
        event_type: 'player_update',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { stats: { magic_points: 50 } },
      };
      const result = handlePlayerUpdate(event, mockContext, mockAppendMessage);
      expect(result?.player).toBeDefined();
    });

    it('should handle update when in_combat is undefined', () => {
      const mockPlayer = {
        id: 'player1',
        name: 'TestPlayer',
        stats: { current_dp: 50, max_dp: 100, lucidity: 75 },
        in_combat: false,
      };
      mockContext.currentPlayerRef.current = mockPlayer as unknown as Player;
      const event = {
        event_type: 'player_update',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { stats: { magic_points: 50 } }, // in_combat not provided
      };
      const result = handlePlayerUpdate(event, mockContext, mockAppendMessage);
      expect(result?.player).toBeDefined();
      expect(result?.player?.in_combat).toBe(false); // Should preserve existing value
    });

    it('should handle update when stats is undefined', () => {
      const mockPlayer = {
        id: 'player1',
        name: 'TestPlayer',
        stats: { current_dp: 50, max_dp: 100, lucidity: 75 },
        in_combat: false,
      };
      mockContext.currentPlayerRef.current = mockPlayer as unknown as Player;
      const event = {
        event_type: 'player_update',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { in_combat: true }, // stats not provided
      };
      const result = handlePlayerUpdate(event, mockContext, mockAppendMessage);
      expect(result?.player).toBeDefined();
      expect(result?.player?.in_combat).toBe(true);
      expect(result?.player?.stats).toBeDefined(); // Should preserve existing stats
    });
  });

  describe('handlePlayerDeliriumRespawned edge cases', () => {
    it('should handle respawn without player stats', () => {
      const mockPlayer = {
        id: 'player1',
        name: 'TestPlayer',
        // No stats property
      };
      mockContext.lucidityStatusRef.current = { current: 0, max: 100, tier: 'lucid', liabilities: [] };
      const event = {
        event_type: 'player_delirium_respawned',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { player: mockPlayer },
      };
      const result = handlePlayerDeliriumRespawned(event, mockContext, mockAppendMessage);
      expect(result?.player).toBeDefined();
    });

    it('should handle respawn without lucidity in stats', () => {
      const mockPlayer = {
        id: 'player1',
        name: 'TestPlayer',
        stats: { current_dp: 50 },
      };
      mockContext.lucidityStatusRef.current = { current: 0, max: 100, tier: 'lucid', liabilities: [] };
      const event = {
        event_type: 'player_delirium_respawned',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { player: mockPlayer },
      };
      const result = handlePlayerDeliriumRespawned(event, mockContext, mockAppendMessage);
      expect(result?.player).toBeDefined();
    });
  });
});
