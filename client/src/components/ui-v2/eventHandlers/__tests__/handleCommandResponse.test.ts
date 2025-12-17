/**
 * Tests for handleCommandResponse handler.
 */

import { beforeEach, describe, expect, it, vi } from 'vitest';
import { handleCommandResponse } from '../messageHandlers';
import { createMockAppendMessage, createMockContext } from './messageHandlers.test-utils';

describe('handleCommandResponse', () => {
  const mockAppendMessage = createMockAppendMessage();
  const mockContext = createMockContext();

  beforeEach(() => {
    vi.clearAllMocks();
  });

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

    expect(mockAppendMessage).toHaveBeenCalled();
  });

  it('should handle player_update in command response', () => {
    const contextWithPlayer = createMockContext({
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
    });

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
    const contextWithRoom = createMockContext({
      currentRoomRef: {
        current: {
          id: 'room1',
          name: 'Room Name',
          description: 'A room',
          exits: {},
        },
      },
    });

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
