/**
 * Tests for handleChatMessage handler.
 */

import { beforeEach, describe, expect, it, vi } from 'vitest';
import { handleChatMessage } from '../messageHandlers';
import { createMockAppendMessage, createMockContext } from './messageHandlers.test-utils';

describe('handleChatMessage', () => {
  const mockAppendMessage = createMockAppendMessage();
  const mockContext = createMockContext();

  beforeEach(() => {
    vi.clearAllMocks();
  });

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
