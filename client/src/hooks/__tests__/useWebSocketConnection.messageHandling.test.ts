import { act, renderHook, waitFor } from '@testing-library/react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
// Fixtures import must load before the hook (@/ paths survive organizeImports on save).
import {
  defaultOptions,
  latestWebSocketInstance,
  wsConnectionAfterEach,
  wsConnectionBeforeEach,
  wsTestState,
} from '@/hooks/__tests__/useWebSocketConnectionTestFixtures';
import { useWebSocketConnection } from '@/hooks/useWebSocketConnection';

describe('useWebSocketConnection - Message Handling', () => {
  beforeEach(wsConnectionBeforeEach);
  afterEach(wsConnectionAfterEach);

  it('should handle messages', async () => {
    const onMessage = vi.fn();
    const { result } = renderHook(() =>
      useWebSocketConnection({
        ...defaultOptions,
        onMessage,
      })
    );

    await act(() => {
      result.current.connect();
    });

    await waitFor(
      () => {
        wsTestState.mockWebSocketInstance = latestWebSocketInstance;
        expect(wsTestState.mockWebSocketInstance).not.toBeNull();
      },
      { timeout: 1000 }
    );

    await act(() => {
      wsTestState.mockWebSocketInstance?.simulateOpen();
    });

    await waitFor(
      () => {
        expect(result.current.isConnected).toBe(true);
      },
      { timeout: 1000 }
    );

    const testMessage = JSON.stringify({ type: 'test', data: 'hello' });

    await act(() => {
      wsTestState.mockWebSocketInstance?.simulateMessage(testMessage);
    });

    expect(onMessage).toHaveBeenCalledWith(expect.objectContaining({ data: testMessage }));
  });

  it('should send messages when connected', async () => {
    const { result } = renderHook(() => useWebSocketConnection(defaultOptions));

    await act(() => {
      result.current.connect();
    });

    await waitFor(
      () => {
        wsTestState.mockWebSocketInstance = latestWebSocketInstance;
        expect(wsTestState.mockWebSocketInstance).not.toBeNull();
      },
      { timeout: 1000 }
    );

    await act(() => {
      wsTestState.mockWebSocketInstance?.simulateOpen();
    });

    await waitFor(
      () => {
        expect(result.current.isConnected).toBe(true);
      },
      { timeout: 1000 }
    );

    await act(() => {
      result.current.sendMessage('test message');
    });

    await waitFor(() => {
      const sendCalls = wsTestState.mockWebSocketInstance?.getSendCalls();
      expect(sendCalls?.length).toBeGreaterThan(0);
      const sentData = JSON.parse(sendCalls?.[0]?.[0] as string);
      expect(sentData.message).toBe('test message');
      expect(sentData.csrfToken).toBe('test-token');
    });
  });

  it('should not send message when not connected', async () => {
    const { result } = renderHook(() => useWebSocketConnection(defaultOptions));

    expect(result.current.isConnected).toBe(false);

    await act(() => {
      result.current.sendMessage('test message');
    });

    // WebSocket should not exist yet
    expect(wsTestState.mockWebSocketInstance).toBeNull();
  });

  it('should sanitize messages before sending', async () => {
    const { inputSanitizer } = await import('../../utils/security');
    const sanitizeSpy = vi.spyOn(inputSanitizer, 'sanitizeCommand').mockReturnValue('sanitized');

    const { result } = renderHook(() => useWebSocketConnection(defaultOptions));

    await act(() => {
      result.current.connect();
    });

    await waitFor(
      () => {
        wsTestState.mockWebSocketInstance = latestWebSocketInstance;
        expect(wsTestState.mockWebSocketInstance).not.toBeNull();
      },
      { timeout: 1000 }
    );

    await act(() => {
      wsTestState.mockWebSocketInstance?.simulateOpen();
    });

    await waitFor(
      () => {
        expect(result.current.isConnected).toBe(true);
      },
      { timeout: 1000 }
    );

    await act(() => {
      result.current.sendMessage('unsafe message');
    });

    expect(sanitizeSpy).toHaveBeenCalledWith('unsafe message');

    await waitFor(() => {
      const sendCalls = wsTestState.mockWebSocketInstance?.getSendCalls();
      if (sendCalls && sendCalls.length > 0) {
        const sentData = JSON.parse(sendCalls[0][0] as string);
        expect(sentData.message).toBe('sanitized');
        expect(sentData.csrfToken).toBe('test-token');
      }
    });

    sanitizeSpy.mockRestore();
  });

  it('should reject messages that are too long', async () => {
    const { result } = renderHook(() => useWebSocketConnection(defaultOptions));

    await act(() => {
      result.current.connect();
    });

    await waitFor(
      () => {
        wsTestState.mockWebSocketInstance = latestWebSocketInstance;
        expect(wsTestState.mockWebSocketInstance).not.toBeNull();
      },
      { timeout: 1000 }
    );

    await act(() => {
      wsTestState.mockWebSocketInstance?.simulateOpen();
    });

    await waitFor(
      () => {
        expect(result.current.isConnected).toBe(true);
      },
      { timeout: 1000 }
    );

    const longMessage = 'x'.repeat(1001);

    await act(() => {
      result.current.sendMessage(longMessage);
    });

    // Should not send the message
    await waitFor(() => {
      const sendCalls = wsTestState.mockWebSocketInstance?.getSendCalls();
      // Should not have sent the long message
      expect(sendCalls?.length || 0).toBe(0);
    });
  });

  it('should reject messages that are heavily sanitized', async () => {
    const { inputSanitizer } = await import('../../utils/security');
    // Mock sanitizer to remove most of the message
    const sanitizeSpy = vi.spyOn(inputSanitizer, 'sanitizeCommand').mockReturnValue('x');

    const { result } = renderHook(() => useWebSocketConnection(defaultOptions));

    await act(() => {
      result.current.connect();
    });

    await waitFor(
      () => {
        wsTestState.mockWebSocketInstance = latestWebSocketInstance;
        expect(wsTestState.mockWebSocketInstance).not.toBeNull();
      },
      { timeout: 1000 }
    );

    await act(() => {
      wsTestState.mockWebSocketInstance?.simulateOpen();
    });

    await waitFor(
      () => {
        expect(result.current.isConnected).toBe(true);
      },
      { timeout: 1000 }
    );

    await act(() => {
      result.current.sendMessage('long unsafe message with many characters');
    });

    // Should not send the message because it was heavily sanitized
    await waitFor(() => {
      const sendCalls = wsTestState.mockWebSocketInstance?.getSendCalls();
      expect(sendCalls?.length || 0).toBe(0);
    });

    sanitizeSpy.mockRestore();
  });

  it('should reject invalid message types', async () => {
    const { result } = renderHook(() => useWebSocketConnection(defaultOptions));

    await act(() => {
      result.current.connect();
    });

    await waitFor(
      () => {
        wsTestState.mockWebSocketInstance = latestWebSocketInstance;
        expect(wsTestState.mockWebSocketInstance).not.toBeNull();
      },
      { timeout: 1000 }
    );

    await act(() => {
      wsTestState.mockWebSocketInstance?.simulateOpen();
    });

    await waitFor(
      () => {
        expect(result.current.isConnected).toBe(true);
      },
      { timeout: 1000 }
    );

    // Try to send invalid message types
    await act(() => {
      result.current.sendMessage(null as unknown as string);
      result.current.sendMessage(undefined as unknown as string);
      result.current.sendMessage(123 as unknown as string);
    });

    // Should not send any of these invalid messages
    await waitFor(() => {
      const sendCalls = wsTestState.mockWebSocketInstance?.getSendCalls();
      expect(sendCalls?.length || 0).toBe(0);
    });
  });

  it('should handle errors when sending messages', async () => {
    const { result } = renderHook(() => useWebSocketConnection(defaultOptions));

    await act(() => {
      result.current.connect();
    });

    await waitFor(
      () => {
        wsTestState.mockWebSocketInstance = latestWebSocketInstance;
        expect(wsTestState.mockWebSocketInstance).not.toBeNull();
      },
      { timeout: 1000 }
    );

    await act(() => {
      wsTestState.mockWebSocketInstance?.simulateOpen();
    });

    await waitFor(
      () => {
        expect(result.current.isConnected).toBe(true);
      },
      { timeout: 1000 }
    );

    // Mock WebSocket send to throw an error
    const originalSend = wsTestState.mockWebSocketInstance?.send;
    if (wsTestState.mockWebSocketInstance) {
      wsTestState.mockWebSocketInstance.send = vi.fn().mockImplementation(() => {
        throw new Error('Send failed');
      });
    }

    await act(() => {
      result.current.sendMessage('test message');
    });

    // Error should be caught and logged, but not crash
    expect(wsTestState.mockWebSocketInstance?.send).toHaveBeenCalled();

    // Restore original send
    if (wsTestState.mockWebSocketInstance && originalSend) {
      wsTestState.mockWebSocketInstance.send = originalSend;
    }
  });
});
