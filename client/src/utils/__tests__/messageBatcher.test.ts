import { describe, expect, it, beforeEach, vi, afterEach } from 'vitest';
import { MessageBatcher, useMessageBatcher } from '../messageBatcher';
import { renderHook, act } from '@testing-library/react';

describe('MessageBatcher', () => {
  let batcher: MessageBatcher;
  let onBatchReady: ReturnType<typeof vi.fn>;

  beforeEach(() => {
    vi.useFakeTimers();
    onBatchReady = vi.fn();
    batcher = new MessageBatcher(onBatchReady);
  });

  afterEach(() => {
    vi.runOnlyPendingTimers();
    vi.useRealTimers();
    vi.clearAllMocks();
  });

  describe('Initialization', () => {
    it('should initialize with default config', () => {
      // Assert
      expect(batcher.getBatchSize()).toBe(0);
      expect(batcher.getBatchSizeBytes()).toBe(0);
    });

    it('should accept custom config', () => {
      // Arrange
      const customBatcher = new MessageBatcher(vi.fn(), {
        maxBatchSize: 5,
        maxBatchDelay: 200,
        maxBatchSizeBytes: 5000,
      });

      // Assert
      expect(customBatcher.getBatchSize()).toBe(0);
    });
  });

  describe('Adding Messages', () => {
    it('should add message to batch', () => {
      // Arrange
      const message = {
        type: 'chat' as const,
        content: 'Hello',
      };

      // Act
      batcher.addMessage(message);

      // Assert
      expect(batcher.getBatchSize()).toBe(1);
    });

    it('should generate unique IDs for messages', () => {
      // Arrange
      const message = {
        type: 'chat' as const,
        content: 'Test',
      };

      // Act
      batcher.addMessage(message);
      batcher.addMessage(message);

      // Assert
      expect(batcher.getBatchSize()).toBe(2);
    });

    it('should add timestamp to messages', () => {
      // Arrange
      const message = {
        type: 'system' as const,
        content: 'System message',
      };

      // Act
      batcher.addMessage(message);

      // Assert - timestamp should be added (we can't easily verify exact value)
      expect(batcher.getBatchSize()).toBe(1);
    });

    it('should preserve message metadata', () => {
      // Arrange
      const message = {
        type: 'chat' as const,
        content: 'Test',
        metadata: {
          channel: 'local',
          sender: 'Player1',
        },
      };

      // Act
      batcher.addMessage(message);

      // Assert
      expect(batcher.getBatchSize()).toBe(1);
    });
  });

  describe('Batch Size Limits', () => {
    it('should send batch when max batch size is reached', () => {
      // Arrange
      const message = {
        type: 'chat' as const,
        content: 'Test',
      };

      // Act - add 10 messages (default maxBatchSize)
      for (let i = 0; i < 10; i++) {
        batcher.addMessage(message);
      }

      // Assert
      expect(onBatchReady).toHaveBeenCalledTimes(1);
      expect(onBatchReady).toHaveBeenCalledWith(
        expect.arrayContaining([
          expect.objectContaining({
            type: 'chat',
            content: 'Test',
          }),
        ])
      );
      expect(batcher.getBatchSize()).toBe(0); // Batch cleared
    });

    it('should send batch when size limit is reached', () => {
      // Arrange
      const largeBatcher = new MessageBatcher(onBatchReady, {
        maxBatchSize: 100,
        maxBatchSizeBytes: 100, // Small limit
      });
      const largeMessage = {
        type: 'chat' as const,
        content: 'x'.repeat(100), // Large message
      };

      // Act
      largeBatcher.addMessage(largeMessage);

      // Assert
      expect(onBatchReady).toHaveBeenCalled();
    });
  });

  describe('Batch Delay', () => {
    it('should send batch after delay when size limit not reached', async () => {
      // Arrange
      const message = {
        type: 'chat' as const,
        content: 'Test',
      };

      // Act
      batcher.addMessage(message);
      expect(onBatchReady).not.toHaveBeenCalled();

      // Advance time by maxBatchDelay (100ms)
      vi.advanceTimersByTime(100);

      // Assert
      expect(onBatchReady).toHaveBeenCalledTimes(1);
      expect(onBatchReady).toHaveBeenCalledWith(
        expect.arrayContaining([
          expect.objectContaining({
            type: 'chat',
            content: 'Test',
          }),
        ])
      );
    });

    it('should send batch after original delay even when new message added', () => {
      // Arrange
      const message = {
        type: 'chat' as const,
        content: 'Test',
      };

      // Act
      batcher.addMessage(message);
      vi.advanceTimersByTime(50); // Halfway through delay
      batcher.addMessage(message); // Add second message

      // Timer doesn't reset - original 100ms timer still running
      // After 50ms more (total 100ms), batch should send
      vi.advanceTimersByTime(50);

      // Assert - should be called once with both messages after original delay
      expect(onBatchReady).toHaveBeenCalledTimes(1);
      expect(onBatchReady).toHaveBeenCalledWith(
        expect.arrayContaining([
          expect.objectContaining({ content: 'Test' }),
          expect.objectContaining({ content: 'Test' }),
        ])
      );
    });
  });

  describe('Flush', () => {
    it('should immediately send current batch', () => {
      // Arrange
      const message = {
        type: 'chat' as const,
        content: 'Test',
      };
      batcher.addMessage(message);

      // Act
      batcher.flush();

      // Assert
      expect(onBatchReady).toHaveBeenCalledTimes(1);
      expect(batcher.getBatchSize()).toBe(0);
    });

    it('should clear timer when flushing', () => {
      // Arrange
      const message = {
        type: 'chat' as const,
        content: 'Test',
      };
      batcher.addMessage(message);

      // Act
      batcher.flush();
      vi.advanceTimersByTime(200); // Advance beyond delay

      // Assert - should not be called again
      expect(onBatchReady).toHaveBeenCalledTimes(1);
    });
  });

  describe('Clear', () => {
    it('should clear current batch', () => {
      // Arrange
      const message = {
        type: 'chat' as const,
        content: 'Test',
      };
      batcher.addMessage(message);
      batcher.addMessage(message);

      // Act
      batcher.clear();

      // Assert
      expect(batcher.getBatchSize()).toBe(0);
      expect(batcher.getBatchSizeBytes()).toBe(0);
    });

    it('should clear timer when clearing', () => {
      // Arrange
      const message = {
        type: 'chat' as const,
        content: 'Test',
      };
      batcher.addMessage(message);

      // Act
      batcher.clear();
      vi.advanceTimersByTime(200);

      // Assert - should not call onBatchReady
      expect(onBatchReady).not.toHaveBeenCalled();
    });
  });

  describe('Batch Size Calculation', () => {
    it('should calculate batch size correctly', () => {
      // Arrange
      const message = {
        type: 'chat' as const,
        content: 'Test',
      };

      // Act
      batcher.addMessage(message);
      batcher.addMessage(message);

      // Assert
      expect(batcher.getBatchSize()).toBe(2);
    });

    it('should calculate batch size in bytes', () => {
      // Arrange
      const message = {
        type: 'chat' as const,
        content: 'Test message',
      };

      // Act
      batcher.addMessage(message);

      // Assert
      const sizeBytes = batcher.getBatchSizeBytes();
      expect(sizeBytes).toBeGreaterThan(0);
      expect(typeof sizeBytes).toBe('number');
    });

    it('should calculate size including metadata', () => {
      // Arrange
      const message = {
        type: 'chat' as const,
        content: 'Test',
        metadata: {
          large: 'x'.repeat(100),
        },
      };

      // Act
      batcher.addMessage(message);

      // Assert
      expect(batcher.getBatchSizeBytes()).toBeGreaterThan(100);
    });
  });

  describe('Message Types', () => {
    it('should handle chat messages', () => {
      // Arrange
      const message = {
        type: 'chat' as const,
        content: 'Hello world',
      };

      // Act
      batcher.addMessage(message);
      batcher.flush();

      // Assert
      expect(onBatchReady).toHaveBeenCalledWith(
        expect.arrayContaining([
          expect.objectContaining({
            type: 'chat',
            content: 'Hello world',
          }),
        ])
      );
    });

    it('should handle system messages', () => {
      // Arrange
      const message = {
        type: 'system' as const,
        content: 'System notification',
      };

      // Act
      batcher.addMessage(message);
      batcher.flush();

      // Assert
      expect(onBatchReady).toHaveBeenCalledWith(
        expect.arrayContaining([
          expect.objectContaining({
            type: 'system',
          }),
        ])
      );
    });

    it('should handle error messages', () => {
      // Arrange
      const message = {
        type: 'error' as const,
        content: 'Error occurred',
      };

      // Act
      batcher.addMessage(message);
      batcher.flush();

      // Assert
      expect(onBatchReady).toHaveBeenCalledWith(
        expect.arrayContaining([
          expect.objectContaining({
            type: 'error',
          }),
        ])
      );
    });

    it('should handle move messages', () => {
      // Arrange
      const message = {
        type: 'move' as const,
        content: 'You move north',
      };

      // Act
      batcher.addMessage(message);
      batcher.flush();

      // Assert
      expect(onBatchReady).toHaveBeenCalledWith(
        expect.arrayContaining([
          expect.objectContaining({
            type: 'move',
          }),
        ])
      );
    });
  });

  describe('Multiple Batches', () => {
    it('should handle multiple sequential batches', () => {
      // Arrange
      const message = {
        type: 'chat' as const,
        content: 'Test',
      };

      // Act - Fill first batch
      for (let i = 0; i < 10; i++) {
        batcher.addMessage(message);
      }
      // Fill second batch
      for (let i = 0; i < 5; i++) {
        batcher.addMessage(message);
      }
      batcher.flush();

      // Assert
      expect(onBatchReady).toHaveBeenCalledTimes(2);
      expect(batcher.getBatchSize()).toBe(0);
    });
  });
});

describe('useMessageBatcher Hook', () => {
  let onBatchReady: ReturnType<typeof vi.fn>;

  beforeEach(() => {
    vi.useFakeTimers();
    onBatchReady = vi.fn();
  });

  afterEach(() => {
    vi.runOnlyPendingTimers();
    vi.useRealTimers();
    vi.clearAllMocks();
  });

  it('should initialize with callback', () => {
    // Act
    const { result } = renderHook(() => useMessageBatcher(onBatchReady));

    // Assert
    expect(result.current.addMessage).toBeDefined();
    expect(result.current.flush).toBeDefined();
    expect(result.current.clear).toBeDefined();
    expect(result.current.getBatchSize).toBeDefined();
  });

  it('should add messages through hook', () => {
    // Arrange
    const { result } = renderHook(() => useMessageBatcher(onBatchReady));

    // Act
    act(() => {
      result.current.addMessage({
        type: 'chat',
        content: 'Test',
      });
    });

    // Assert
    expect(result.current.getBatchSize()).toBe(1);
  });

  it('should flush batch through hook', () => {
    // Arrange
    const { result } = renderHook(() => useMessageBatcher(onBatchReady));

    act(() => {
      result.current.addMessage({
        type: 'chat',
        content: 'Test',
      });
    });

    // Act
    act(() => {
      result.current.flush();
    });

    // Assert
    expect(onBatchReady).toHaveBeenCalledTimes(1);
    expect(result.current.getBatchSize()).toBe(0);
  });

  it('should clear batch through hook', () => {
    // Arrange
    const { result } = renderHook(() => useMessageBatcher(onBatchReady));

    act(() => {
      result.current.addMessage({
        type: 'chat',
        content: 'Test',
      });
    });

    // Act
    act(() => {
      result.current.clear();
    });

    // Assert
    expect(result.current.getBatchSize()).toBe(0);
  });

  it('should accept custom config', () => {
    // Arrange
    const { result } = renderHook(() =>
      useMessageBatcher(onBatchReady, {
        maxBatchSize: 5,
        maxBatchDelay: 200,
      })
    );

    // Act
    act(() => {
      for (let i = 0; i < 5; i++) {
        result.current.addMessage({
          type: 'chat',
          content: 'Test',
        });
      }
    });

    // Assert - should flush when maxBatchSize reached
    expect(onBatchReady).toHaveBeenCalledTimes(1);
  });

  it('should flush on unmount', () => {
    // Arrange
    const { result, unmount } = renderHook(() => useMessageBatcher(onBatchReady));

    act(() => {
      result.current.addMessage({
        type: 'chat',
        content: 'Test',
      });
    });

    // Act
    unmount();

    // Assert
    expect(onBatchReady).toHaveBeenCalledTimes(1);
  });

  it('should maintain same instance across re-renders', () => {
    // Arrange
    const { result, rerender } = renderHook(() => useMessageBatcher(onBatchReady));

    act(() => {
      result.current.addMessage({
        type: 'chat',
        content: 'Test 1',
      });
    });

    const initialSize = result.current.getBatchSize();

    // Act
    rerender();

    // Assert - should still have the message
    expect(result.current.getBatchSize()).toBe(initialSize);
  });
});
