/**
 * Tests for messageHandlers.
 */

import { HealthStatus } from '@/types/health';
import { LucidityStatus, RescueState } from '@/types/lucidity';
import { describe, expect, it, vi } from 'vitest';
import type { ChatMessage, MythosTimeState } from '../../types';
import { handleChatMessage, handleCommandResponse, handleRoomMessage, handleSystem } from '../messageHandlers';
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
      const contextWithRoom: EventHandlerContext = {
        ...mockContext,
        currentRoomRef: {
          current: {
            id: 'room1',
            name: 'Room Name',
            description: 'A room',
            exits: {},
          },
        },
      };

      const event = {
        event_type: 'command_response',
        timestamp: new Date().toISOString(),
        sequence_number: 7,
        data: {
          result: 'Room Name',
          is_html: false,
        },
      };

      handleCommandResponse(event, contextWithRoom, mockAppendMessage);

      // Should not append message if it's just the room name
      expect(mockAppendMessage).not.toHaveBeenCalled();
    });

    it('should handle empty message', () => {
      const event = {
        event_type: 'command_response',
        timestamp: new Date().toISOString(),
        sequence_number: 8,
        data: {
          result: '',
          is_html: false,
        },
      };

      handleCommandResponse(event, mockContext, mockAppendMessage);

      // Should not append empty message
      expect(mockAppendMessage).not.toHaveBeenCalled();
    });

    it('should handle non-string result', () => {
      const event = {
        event_type: 'command_response',
        timestamp: new Date().toISOString(),
        sequence_number: 9,
        data: {
          result: 123,
          is_html: false,
        },
      };

      handleCommandResponse(event, mockContext, mockAppendMessage);

      // Should handle gracefully
      expect(mockAppendMessage).not.toHaveBeenCalled();
    });

    it('should use game_log_channel when provided', () => {
      const event = {
        event_type: 'command_response',
        timestamp: new Date().toISOString(),
        sequence_number: 10,
        data: {
          result: 'Test',
          suppress_chat: true,
          game_log_channel: 'custom-channel',
          game_log_message: 'Game log',
          is_html: false,
        },
      };

      handleCommandResponse(event, mockContext, mockAppendMessage);

      expect(mockAppendMessage).toHaveBeenCalledWith(
        expect.objectContaining({
          channel: 'custom-channel',
        })
      );
    });
  });

  describe('handleChatMessage', () => {
    it('should handle whisper messages', () => {
      const event = {
        event_type: 'chat_message',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: {
          message: 'Whisper message',
          channel: 'whisper',
        },
      };

      handleChatMessage(event, mockContext, mockAppendMessage);

      expect(mockAppendMessage).toHaveBeenCalledWith(
        expect.objectContaining({
          text: 'Whisper message',
          messageType: 'whisper',
          channel: 'whisper',
          type: 'whisper',
        })
      );
    });

    it('should handle shout messages', () => {
      const event = {
        event_type: 'chat_message',
        timestamp: new Date().toISOString(),
        sequence_number: 2,
        data: {
          message: 'Shout message',
          channel: 'shout',
        },
      };

      handleChatMessage(event, mockContext, mockAppendMessage);

      expect(mockAppendMessage).toHaveBeenCalledWith(
        expect.objectContaining({
          text: 'Shout message',
          messageType: 'shout',
          channel: 'shout',
          type: 'shout',
        })
      );
    });

    it('should handle emote messages', () => {
      const event = {
        event_type: 'chat_message',
        timestamp: new Date().toISOString(),
        sequence_number: 3,
        data: {
          message: 'Emote message',
          channel: 'emote',
        },
      };

      handleChatMessage(event, mockContext, mockAppendMessage);

      expect(mockAppendMessage).toHaveBeenCalledWith(
        expect.objectContaining({
          text: 'Emote message',
          messageType: 'emote',
          channel: 'emote',
          type: 'emote',
        })
      );
    });

    it('should handle say/local messages', () => {
      const event = {
        event_type: 'chat_message',
        timestamp: new Date().toISOString(),
        sequence_number: 4,
        data: {
          message: 'Say message',
          channel: 'say',
        },
      };

      handleChatMessage(event, mockContext, mockAppendMessage);

      expect(mockAppendMessage).toHaveBeenCalledWith(
        expect.objectContaining({
          text: 'Say message',
          messageType: 'chat',
          channel: 'say',
          type: 'say',
        })
      );
    });

    it('should handle default channel', () => {
      const event = {
        event_type: 'chat_message',
        timestamp: new Date().toISOString(),
        sequence_number: 5,
        data: {
          message: 'Default message',
          channel: 'unknown',
        },
      };

      handleChatMessage(event, mockContext, mockAppendMessage);

      expect(mockAppendMessage).toHaveBeenCalledWith(
        expect.objectContaining({
          text: 'Default message',
          messageType: 'chat',
        })
      );
    });

    it('should not append message when message is empty', () => {
      const event = {
        event_type: 'chat_message',
        timestamp: new Date().toISOString(),
        sequence_number: 6,
        data: {
          message: '',
          channel: 'say',
        },
      };

      handleChatMessage(event, mockContext, mockAppendMessage);

      expect(mockAppendMessage).not.toHaveBeenCalled();
    });
  });

  describe('handleRoomMessage', () => {
    it('should handle system messages', () => {
      const event = {
        event_type: 'room_message',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: {
          message: 'System message',
          message_type: 'system',
          is_html: false,
        },
      };

      handleRoomMessage(event, mockContext, mockAppendMessage);

      expect(mockAppendMessage).toHaveBeenCalledWith(
        expect.objectContaining({
          text: 'System message',
          messageType: 'system',
          channel: 'game-log',
          type: 'system',
        })
      );
    });

    it('should handle non-system messages', () => {
      const event = {
        event_type: 'room_message',
        timestamp: new Date().toISOString(),
        sequence_number: 2,
        data: {
          message: 'Room message',
          is_html: false,
        },
      };

      handleRoomMessage(event, mockContext, mockAppendMessage);

      expect(mockAppendMessage).toHaveBeenCalledWith(
        expect.objectContaining({
          text: 'Room message',
        })
      );
    });

    it('should handle HTML messages', () => {
      const event = {
        event_type: 'room_message',
        timestamp: new Date().toISOString(),
        sequence_number: 3,
        data: {
          message: '<b>HTML message</b>',
          is_html: true,
        },
      };

      handleRoomMessage(event, mockContext, mockAppendMessage);

      expect(mockAppendMessage).toHaveBeenCalledWith(
        expect.objectContaining({
          text: '<b>HTML message</b>',
          isHtml: true,
        })
      );
    });

    it('should not append message when message is empty', () => {
      const event = {
        event_type: 'room_message',
        timestamp: new Date().toISOString(),
        sequence_number: 4,
        data: {
          message: '',
          is_html: false,
        },
      };

      handleRoomMessage(event, mockContext, mockAppendMessage);

      expect(mockAppendMessage).not.toHaveBeenCalled();
    });

    it('should handle non-string message', () => {
      const event = {
        event_type: 'room_message',
        timestamp: new Date().toISOString(),
        sequence_number: 5,
        data: {
          message: 123,
          is_html: false,
        },
      };

      handleRoomMessage(event, mockContext, mockAppendMessage);

      expect(mockAppendMessage).not.toHaveBeenCalled();
    });
  });

  describe('handleSystem', () => {
    it('should handle system messages', () => {
      const event = {
        event_type: 'system',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: {
          message: 'System message',
        },
      };

      handleSystem(event, mockContext, mockAppendMessage);

      expect(mockAppendMessage).toHaveBeenCalledWith(
        expect.objectContaining({
          text: 'System message',
          messageType: 'system',
          channel: 'game',
          type: 'system',
          isHtml: false,
        })
      );
    });

    it('should not append message when message is empty', () => {
      const event = {
        event_type: 'system',
        timestamp: new Date().toISOString(),
        sequence_number: 2,
        data: {
          message: '',
        },
      };

      handleSystem(event, mockContext, mockAppendMessage);

      expect(mockAppendMessage).not.toHaveBeenCalled();
    });

    it('should not append message when message is not a string', () => {
      const event = {
        event_type: 'system',
        timestamp: new Date().toISOString(),
        sequence_number: 3,
        data: {
          message: 123,
        },
      };

      handleSystem(event, mockContext, mockAppendMessage);

      expect(mockAppendMessage).not.toHaveBeenCalled();
    });

    it('should not append message when message is missing', () => {
      const event = {
        event_type: 'system',
        timestamp: new Date().toISOString(),
        sequence_number: 4,
        data: {},
      };

      handleSystem(event, mockContext, mockAppendMessage);

      expect(mockAppendMessage).not.toHaveBeenCalled();
    });
  });
});
