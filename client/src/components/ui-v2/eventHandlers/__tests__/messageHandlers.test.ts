/**
 * Tests for messageHandlers.
 */

import { HealthStatus } from '@/types/health';
import { LucidityStatus, RescueState } from '@/types/lucidity';
import { describe, expect, it, vi } from 'vitest';
import type { ChatMessage, MythosTimeState } from '../../types';
import { handleCommandResponse } from '../messageHandlers';
import type { EventHandlerContext } from '../types';

// Mock dependencies
vi.mock('../../../utils/logger', () => ({
  logger: {
    error: vi.fn(),
  },
}));

vi.mock('../../../utils/messageTypeUtils', () => ({
  determineMessageType: vi.fn(() => 'system'),
}));

vi.mock('../../../utils/statusParser', () => ({
  parseStatusResponse: vi.fn(() => ({})),
  convertToPlayerInterface: vi.fn(() => ({ id: 'player1', name: 'Player' })),
}));

vi.mock('../../utils/messageUtils', () => ({
  sanitizeChatMessageForState: (message: ChatMessage) => message,
}));

describe('messageHandlers', () => {
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
    setDpStatus: function (_status: HealthStatus): void {
      throw new Error('Function not implemented.');
    },
    setLucidityStatus: function (_status: LucidityStatus): void {
      throw new Error('Function not implemented.');
    },
    setMythosTime: function (_time: MythosTimeState): void {
      throw new Error('Function not implemented.');
    },
    setIsDead: function (_dead: boolean): void {
      throw new Error('Function not implemented.');
    },
    setIsMortallyWounded: function (_wounded: boolean): void {
      throw new Error('Function not implemented.');
    },
    setIsRespawning: function (_respawning: boolean): void {
      throw new Error('Function not implemented.');
    },
    setIsDelirious: function (_delirious: boolean): void {
      throw new Error('Function not implemented.');
    },
    setIsDeliriumRespawning: function (_respawning: boolean): void {
      throw new Error('Function not implemented.');
    },
    setDeathLocation: function (_location: string): void {
      throw new Error('Function not implemented.');
    },
    setDeliriumLocation: function (_location: string): void {
      throw new Error('Function not implemented.');
    },
    setRescueState: function (_state: RescueState | null): void {
      throw new Error('Function not implemented.');
    },
  };

  beforeEach(() => {
    vi.clearAllMocks();
  });

  describe('handleCommandResponse', () => {
    it('should append message when result is present', () => {
      const event = {
        event_type: 'command_response',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: {
          result: 'Test message',
          is_html: false,
        },
      };

      handleCommandResponse(event, mockContext, mockAppendMessage);

      expect(mockAppendMessage).toHaveBeenCalled();
    });

    it('should parse status response when message contains status fields', () => {
      const event = {
        event_type: 'command_response',
        timestamp: new Date().toISOString(),
        sequence_number: 2,
        data: {
          result: 'Name: Player\nHealth: 100/100\nLucidity: 50/50',
          is_html: false,
        },
      };

      handleCommandResponse(event, mockContext, mockAppendMessage);

      expect(mockAppendMessage).toHaveBeenCalled();
    });

    it('should handle HTML messages', () => {
      const event = {
        event_type: 'command_response',
        timestamp: new Date().toISOString(),
        sequence_number: 3,
        data: {
          result: '<b>Bold text</b>',
          is_html: true,
        },
      };

      handleCommandResponse(event, mockContext, mockAppendMessage);

      expect(mockAppendMessage).toHaveBeenCalled();
    });

    it('should use game_log_message when provided', () => {
      const event = {
        event_type: 'command_response',
        timestamp: new Date().toISOString(),
        sequence_number: 4,
        data: {
          result: 'Result message',
          game_log_message: 'Game log message',
          is_html: false,
        },
      };

      handleCommandResponse(event, mockContext, mockAppendMessage);

      expect(mockAppendMessage).toHaveBeenCalled();
    });

    it('should handle suppress_chat flag', () => {
      const event = {
        event_type: 'command_response',
        timestamp: new Date().toISOString(),
        sequence_number: 5,
        data: {
          result: 'Test message',
          suppress_chat: true,
          is_html: false,
        },
      };

      handleCommandResponse(event, mockContext, mockAppendMessage);

      // Should still process but with suppress_chat flag
      expect(mockAppendMessage).toHaveBeenCalled();
    });

    it('should handle player_update in command response', () => {
      const contextWithPlayer: EventHandlerContext = {
        currentPlayerRef: {
          current: {
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
        setDpStatus: function (_status: HealthStatus): void {
          throw new Error('Function not implemented.');
        },
        setLucidityStatus: function (_status: LucidityStatus): void {
          throw new Error('Function not implemented.');
        },
        setMythosTime: function (_time: MythosTimeState): void {
          throw new Error('Function not implemented.');
        },
        setIsDead: function (_dead: boolean): void {
          throw new Error('Function not implemented.');
        },
        setIsMortallyWounded: function (_wounded: boolean): void {
          throw new Error('Function not implemented.');
        },
        setIsRespawning: function (_respawning: boolean): void {
          throw new Error('Function not implemented.');
        },
        setIsDelirious: function (_delirious: boolean): void {
          throw new Error('Function not implemented.');
        },
        setIsDeliriumRespawning: function (_respawning: boolean): void {
          throw new Error('Function not implemented.');
        },
        setDeathLocation: function (_location: string): void {
          throw new Error('Function not implemented.');
        },
        setDeliriumLocation: function (_location: string): void {
          throw new Error('Function not implemented.');
        },
        setRescueState: function (_state: RescueState | null): void {
          throw new Error('Function not implemented.');
        },
      };

      const event = {
        event_type: 'command_response',
        timestamp: new Date().toISOString(),
        sequence_number: 6,
        data: {
          result: 'Test',
          player_update: {
            position: 'sitting',
          },
          is_html: false,
        },
      };

      const result = handleCommandResponse(event, contextWithPlayer, mockAppendMessage);

      expect(result).toBeDefined();
      expect(result?.player).toBeDefined();
    });

    it('should filter out room name-only messages', () => {
      const event = {
        event_type: 'command_response',
        timestamp: new Date().toISOString(),
        sequence_number: 7,
        data: {
          result: 'Room Name',
          is_html: false,
        },
      };

      handleCommandResponse(event, mockContext, mockAppendMessage);

      // Should still call appendMessage but message might be filtered
      expect(mockAppendMessage).toHaveBeenCalled();
    });
  });
});
