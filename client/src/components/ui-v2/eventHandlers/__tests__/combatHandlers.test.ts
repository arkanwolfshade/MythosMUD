/**
 * Tests for combatHandlers.
 */

import { describe, expect, it, vi } from 'vitest';
import type { ChatMessage } from '../../types';
import {
  handleCombatEnded,
  handleCombatStarted,
  handleCombatDeath,
  handleNpcAttacked,
  handleNpcDied,
  handlePlayerAttacked,
} from '../combatHandlers';
import type { EventHandlerContext } from '../types';

// Mock messageUtils
vi.mock('../../utils/messageUtils', () => ({
  sanitizeChatMessageForState: (message: ChatMessage) => message,
}));

describe('combatHandlers', () => {
  const mockAppendMessage = vi.fn();
  // Create a minimal mock context with all required properties from EventHandlerContext
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

  describe('handleNpcAttacked', () => {
    it('should append message when attacker and damage are present', () => {
      const event = {
        event_type: 'npc_attacked',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: {
          attacker_name: 'Goblin',
          damage: 10,
        },
      };

      handleNpcAttacked(event, mockContext, mockAppendMessage);

      expect(mockAppendMessage).toHaveBeenCalled();
    });

    it('should use npc_name as fallback for attacker_name', () => {
      const event = {
        event_type: 'npc_attacked',
        timestamp: new Date().toISOString(),
        sequence_number: 2,
        data: {
          npc_name: 'Goblin',
          damage: 10,
        },
      };

      handleNpcAttacked(event, mockContext, mockAppendMessage);

      expect(mockAppendMessage).toHaveBeenCalled();
    });

    it('should include DP information when available', () => {
      const event = {
        event_type: 'npc_attacked',
        timestamp: new Date().toISOString(),
        sequence_number: 3,
        data: {
          attacker_name: 'Goblin',
          damage: 10,
          target_current_dp: 50,
          target_max_dp: 100,
        },
      };

      handleNpcAttacked(event, mockContext, mockAppendMessage);

      expect(mockAppendMessage).toHaveBeenCalled();
      const callArg = mockAppendMessage.mock.calls[0][0];
      expect(callArg.text).toContain('(50/100 DP)');
    });

    it('should use action_type when provided', () => {
      const event = {
        event_type: 'npc_attacked',
        timestamp: new Date().toISOString(),
        sequence_number: 4,
        data: {
          attacker_name: 'Goblin',
          damage: 10,
          action_type: 'strikes',
        },
      };

      handleNpcAttacked(event, mockContext, mockAppendMessage);

      expect(mockAppendMessage).toHaveBeenCalled();
      const callArg = mockAppendMessage.mock.calls[0][0];
      expect(callArg.text).toContain('strikes');
    });

    it('should not append message when attacker name is missing', () => {
      const event = {
        event_type: 'npc_attacked',
        timestamp: new Date().toISOString(),
        sequence_number: 5,
        data: {
          damage: 10,
        },
      };

      handleNpcAttacked(event, mockContext, mockAppendMessage);

      expect(mockAppendMessage).not.toHaveBeenCalled();
    });

    it('should not append message when damage is missing', () => {
      const event = {
        event_type: 'npc_attacked',
        timestamp: new Date().toISOString(),
        sequence_number: 6,
        data: {
          attacker_name: 'Goblin',
        },
      };

      handleNpcAttacked(event, mockContext, mockAppendMessage);

      expect(mockAppendMessage).not.toHaveBeenCalled();
    });
  });

  describe('handlePlayerAttacked', () => {
    it('should append message when attacker, target, and damage are present', () => {
      const event = {
        event_type: 'player_attacked',
        timestamp: new Date().toISOString(),
        sequence_number: 7,
        data: {
          attacker_name: 'Player',
          target_name: 'Goblin',
          damage: 15,
        },
      };

      handlePlayerAttacked(event, mockContext, mockAppendMessage);

      expect(mockAppendMessage).toHaveBeenCalled();
    });

    it('should include DP information when available', () => {
      const event = {
        event_type: 'player_attacked',
        timestamp: new Date().toISOString(),
        sequence_number: 8,
        data: {
          attacker_name: 'Player',
          target_name: 'Goblin',
          damage: 15,
          target_current_dp: 75,
          target_max_dp: 100,
        },
      };

      handlePlayerAttacked(event, mockContext, mockAppendMessage);

      expect(mockAppendMessage).toHaveBeenCalled();
      const callArg = mockAppendMessage.mock.calls[0][0];
      expect(callArg.text).toContain('(75/100 DP)');
    });

    it('should not append message when required fields are missing', () => {
      const event = {
        event_type: 'player_attacked',
        timestamp: new Date().toISOString(),
        sequence_number: 9,
        data: {
          attacker_name: 'Player',
        },
      };

      handlePlayerAttacked(event, mockContext, mockAppendMessage);

      expect(mockAppendMessage).not.toHaveBeenCalled();
    });
  });

  describe('handleCombatStarted', () => {
    it('should return updates when player exists', () => {
      const contextWithPlayer: EventHandlerContext = {
        currentPlayerRef: {
          current: {
            id: 'player1',
            name: 'Player',
            stats: {
              current_dp: 100,
              lucidity: 50,
              position: 'standing',
            },
          } as import('../../types').Player,
        },
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

      const event = {
        event_type: 'combat_started',
        timestamp: new Date().toISOString(),
        sequence_number: 10,
        data: {},
      };

      const result = handleCombatStarted(event, contextWithPlayer, mockAppendMessage);

      expect(result).toBeDefined();
    });

    it('should return undefined when player does not exist', () => {
      const event = {
        event_type: 'combat_started',
        timestamp: new Date().toISOString(),
        sequence_number: 11,
        data: {},
      };

      const result = handleCombatStarted(event, mockContext, mockAppendMessage);

      expect(result).toBeUndefined();
    });
  });

  describe('handleCombatEnded', () => {
    it('should return updates when player exists', () => {
      const contextWithPlayer: EventHandlerContext = {
        currentPlayerRef: {
          current: {
            id: 'player1',
            name: 'Player',
            stats: {
              current_dp: 100,
              lucidity: 50,
              position: 'standing',
            },
            in_combat: true,
          } as import('../../types').Player,
        },
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

      const event = {
        event_type: 'combat_ended',
        timestamp: new Date().toISOString(),
        sequence_number: 12,
        data: {},
      };

      const result = handleCombatEnded(event, contextWithPlayer, mockAppendMessage);

      expect(result).toBeDefined();
      expect(result?.player?.in_combat).toBe(false);
    });

    it('should return undefined when player does not exist', () => {
      const event = {
        event_type: 'combat_ended',
        timestamp: new Date().toISOString(),
        sequence_number: 13,
        data: {},
      };

      const result = handleCombatEnded(event, mockContext, mockAppendMessage);

      expect(result).toBeUndefined();
    });
  });

  describe('handleNpcDied', () => {
    it('should append death message when npc_name is present', () => {
      const event = {
        event_type: 'npc_died',
        timestamp: new Date().toISOString(),
        sequence_number: 14,
        data: {
          npc_name: 'Goblin',
        },
      };

      handleNpcDied(event, mockContext, mockAppendMessage);

      expect(mockAppendMessage).toHaveBeenCalled();
      const callArg = mockAppendMessage.mock.calls[0][0];
      expect(callArg.text).toContain('Goblin dies.');
    });

    it('should append XP reward message when xp_reward is positive', () => {
      const event = {
        event_type: 'npc_died',
        timestamp: new Date().toISOString(),
        sequence_number: 15,
        data: {
          npc_name: 'Goblin',
          xp_reward: 100,
        },
      };

      handleNpcDied(event, mockContext, mockAppendMessage);

      expect(mockAppendMessage).toHaveBeenCalledTimes(2);
      const xpCall = mockAppendMessage.mock.calls.find(call => call[0].text.includes('experience points'));
      expect(xpCall).toBeDefined();
    });

    it('should not append XP message when xp_reward is zero', () => {
      const event = {
        event_type: 'npc_died',
        timestamp: new Date().toISOString(),
        sequence_number: 16,
        data: {
          npc_name: 'Goblin',
          xp_reward: 0,
        },
      };

      handleNpcDied(event, mockContext, mockAppendMessage);

      expect(mockAppendMessage).toHaveBeenCalledTimes(1);
      const xpCall = mockAppendMessage.mock.calls.find(call => call[0].text.includes('experience points'));
      expect(xpCall).toBeUndefined();
    });

    it('should not append message when npc_name is missing', () => {
      const event = {
        event_type: 'npc_died',
        timestamp: new Date().toISOString(),
        sequence_number: 17,
        data: {},
      };

      handleNpcDied(event, mockContext, mockAppendMessage);

      expect(mockAppendMessage).not.toHaveBeenCalled();
    });
  });

  describe('handleCombatDeath', () => {
    it('should append death message when present', () => {
      const event = {
        event_type: 'combat_death',
        timestamp: new Date().toISOString(),
        sequence_number: 18,
        data: {
          messages: {
            death_message: 'You have been slain!',
          },
        },
      };

      handleCombatDeath(event, mockContext, mockAppendMessage);

      expect(mockAppendMessage).toHaveBeenCalled();
      const callArg = mockAppendMessage.mock.calls[0][0];
      expect(callArg.text).toBe('You have been slain!');
    });

    it('should append XP reward message when present', () => {
      const event = {
        event_type: 'combat_death',
        timestamp: new Date().toISOString(),
        sequence_number: 19,
        data: {
          messages: {
            xp_reward: 'You gain 50 experience points.',
          },
        },
      };

      handleCombatDeath(event, mockContext, mockAppendMessage);

      expect(mockAppendMessage).toHaveBeenCalled();
      const callArg = mockAppendMessage.mock.calls[0][0];
      expect(callArg.text).toBe('You gain 50 experience points.');
    });

    it('should append both messages when both are present', () => {
      const event = {
        event_type: 'combat_death',
        timestamp: new Date().toISOString(),
        sequence_number: 20,
        data: {
          messages: {
            death_message: 'You have been slain!',
            xp_reward: 'You gain 50 experience points.',
          },
        },
      };

      handleCombatDeath(event, mockContext, mockAppendMessage);

      expect(mockAppendMessage).toHaveBeenCalledTimes(2);
    });

    it('should not append message when messages object is missing', () => {
      const event = {
        event_type: 'combat_death',
        timestamp: new Date().toISOString(),
        sequence_number: 21,
        data: {},
      };

      handleCombatDeath(event, mockContext, mockAppendMessage);

      expect(mockAppendMessage).not.toHaveBeenCalled();
    });
  });
});
