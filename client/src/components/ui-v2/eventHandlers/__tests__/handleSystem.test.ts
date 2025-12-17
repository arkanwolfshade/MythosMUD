/**
 * Tests for handleSystem handler.
 */

import { beforeEach, describe, expect, it, vi } from 'vitest';
import { handleSystem } from '../messageHandlers';
import { createMockAppendMessage, createMockContext } from './messageHandlers.test-utils';

describe('handleSystem', () => {
  const mockAppendMessage = createMockAppendMessage();
  const mockContext = createMockContext();

  beforeEach(() => {
    vi.clearAllMocks();
  });

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
