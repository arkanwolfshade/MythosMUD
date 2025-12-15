/**
 * Tests for combatHandlers.
 */

import { describe, expect, it, vi } from 'vitest';
import type { ChatMessage } from '../../types';
import { handleCombatStarted, handleNpcAttacked, handlePlayerAttacked } from '../combatHandlers';
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
});
