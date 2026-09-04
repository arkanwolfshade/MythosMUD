/**
 * Tests for handleRoomMessage handler.
 */

import { beforeEach, describe, expect, it, vi } from 'vitest';
import { handleRoomMessage } from '../messageHandlers';
import { createMockAppendMessage, createMockContext } from './messageHandlers.test-utils';

describe('handleRoomMessage', () => {
  const mockAppendMessage = createMockAppendMessage();
  const mockContext = createMockContext();

  beforeEach(() => {
    vi.clearAllMocks();
  });

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
