import { describe, expect, it, beforeEach, afterEach, vi } from 'vitest';
import { renderHook, act, waitFor } from '@testing-library/react';
import { useWebSocketConnection } from '../useWebSocketConnection';

// Mock logger
vi.mock('../../utils/logger', () => ({
  logger: {
    debug: vi.fn(),
    info: vi.fn(),
    warn: vi.fn(),
    error: vi.fn(),
  },
}));

// Mock useResourceCleanup
const mockResourceManager = {
  registerEventSource: vi.fn(),
  registerWebSocket: vi.fn(),
  registerTimer: vi.fn(),
  registerInterval: vi.fn(),
  registerCustomResource: vi.fn(),
  removeTimer: vi.fn(),
  removeInterval: vi.fn(),
  cleanup: vi.fn(),
  getStats: vi.fn(() => ({
    timers: 0,
    intervals: 0,
    webSockets: 0,
    eventSources: 0,
    customResources: 0,
    total: 0,
  })),
};

vi.mock('../../utils/resourceCleanup', () => ({
  useResourceCleanup: () => mockResourceManager,
}));

// Mock inputSanitizer
vi.mock('../../utils/security', () => ({
  inputSanitizer: {
    sanitizeCommand: vi.fn((input: string) => input),
  },
}));

// Mock fetch for health checks
global.fetch = vi.fn();

// Mock setInterval and clearInterval
const originalSetInterval = global.setInterval;
const originalClearInterval = global.clearInterval;
const intervalIds = new Set<number>();
let intervalIdCounter = 1;

global.setInterval = vi.fn((callback: () => void, delay?: number) => {
  const id = intervalIdCounter++;
  intervalIds.add(id);
  return originalSetInterval(callback, delay);
}) as typeof setInterval;

global.clearInterval = vi.fn((id: number) => {
  intervalIds.delete(id);
  return originalClearInterval(id);
}) as typeof clearInterval;

// Global variable to track the latest WebSocket instance
let latestWebSocketInstance: MockWebSocket | null = null;

// Mock WebSocket
class MockWebSocket {
  static CONNECTING = 0;
  static OPEN = 1;
  static CLOSING = 2;
  static CLOSED = 3;

  url: string;
  protocols: string[];
  readyState: number = MockWebSocket.CONNECTING;
  onopen: ((this: MockWebSocket, ev: Event) => void) | null = null;
  onmessage: ((this: MockWebSocket, ev: MessageEvent) => void) | null = null;
  onerror: ((this: MockWebSocket, ev: Event) => void) | null = null;
  onclose: ((this: MockWebSocket, ev: CloseEvent) => void) | null = null;

  private sendSpy = vi.fn();
  private closeSpy = vi.fn();

  constructor(url: string | URL, protocols?: string | string[]) {
    this.url = typeof url === 'string' ? url : url.toString();
    this.protocols = Array.isArray(protocols) ? protocols : protocols ? [protocols] : [];
    // Track this instance globally for test assertions
    // eslint-disable-next-line @typescript-eslint/no-this-alias
    latestWebSocketInstance = this;
  }

  send(data: string | ArrayBuffer | Blob) {
    this.sendSpy(data);
  }

  close() {
    this.closeSpy();
    this.readyState = MockWebSocket.CLOSED;
    if (this.onclose) {
      this.onclose(new CloseEvent('close'));
    }
  }

  // Helper methods for testing
  simulateOpen() {
    this.readyState = MockWebSocket.OPEN;
    if (this.onopen) {
      this.onopen(new Event('open'));
    }
  }

  simulateMessage(data: string) {
    if (this.onmessage) {
      const event = new MessageEvent('message', { data });
      this.onmessage(event);
    }
  }

  simulateError() {
    if (this.onerror) {
      this.onerror(new Event('error'));
    }
  }

  simulateClose() {
    this.readyState = MockWebSocket.CLOSED;
    if (this.onclose) {
      this.onclose(new CloseEvent('close'));
    }
  }

  getSendCalls() {
    return this.sendSpy.mock.calls;
  }

  getCloseCalls() {
    return this.closeSpy.mock.calls;
  }
}

describe('useWebSocketConnection', () => {
  let mockWebSocketInstance: MockWebSocket | null = null;
  let originalWebSocket: typeof global.WebSocket;

  beforeEach(() => {
    vi.clearAllMocks();
    mockResourceManager.removeInterval.mockClear();
    mockResourceManager.removeTimer.mockClear();
    mockResourceManager.registerInterval.mockClear();
    mockResourceManager.registerTimer.mockClear();
    mockWebSocketInstance = null;
    latestWebSocketInstance = null;

    // Mock WebSocket - directly assign the class
    originalWebSocket = global.WebSocket;
    global.WebSocket = MockWebSocket as unknown as typeof global.WebSocket;

    // Set up WebSocket constants
    (global.WebSocket as unknown as { CONNECTING: number }).CONNECTING = 0;
    (global.WebSocket as unknown as { OPEN: number }).OPEN = 1;
    (global.WebSocket as unknown as { CLOSING: number }).CLOSING = 2;
    (global.WebSocket as unknown as { CLOSED: number }).CLOSED = 3;

    // Mock environment
    vi.stubEnv('DEV', 'true');
  });

  afterEach(() => {
    global.WebSocket = originalWebSocket;
    mockWebSocketInstance = null;
    latestWebSocketInstance = null;
    vi.restoreAllMocks();
    vi.unstubAllEnvs();
  });

  const defaultOptions = {
    authToken: 'test-token',
    sessionId: 'test-session-id',
  };

  describe('Connection Management', () => {
    it('should start disconnected', () => {
      const { result } = renderHook(() => useWebSocketConnection(defaultOptions));

      expect(result.current.isConnected).toBe(false);
      expect(result.current.lastError).toBeNull();
    });

    it('should connect successfully', async () => {
      const onConnected = vi.fn();
      const { result } = renderHook(() =>
        useWebSocketConnection({
          ...defaultOptions,
          onConnected,
        })
      );

      expect(result.current.isConnected).toBe(false);
      expect(result.current.lastError).toBe(null);

      act(() => {
        result.current.connect();
      });

      // Wait for WebSocket to be created - use latestWebSocketInstance from constructor
      await waitFor(
        () => {
          mockWebSocketInstance = latestWebSocketInstance;
          expect(mockWebSocketInstance).not.toBeNull();
        },
        { timeout: 1000 }
      );

      // Manually trigger open event
      act(() => {
        mockWebSocketInstance?.simulateOpen();
      });

      await waitFor(
        () => {
          expect(result.current.isConnected).toBe(true);
        },
        { timeout: 1000 }
      );

      expect(onConnected).toHaveBeenCalled();
      expect(mockResourceManager.registerInterval).toHaveBeenCalled();
    });

    it('should disconnect successfully', async () => {
      const onDisconnect = vi.fn();
      const { result } = renderHook(() =>
        useWebSocketConnection({
          ...defaultOptions,
          onDisconnect,
        })
      );

      act(() => {
        result.current.connect();
      });

      await waitFor(
        () => {
          mockWebSocketInstance = latestWebSocketInstance;
          expect(mockWebSocketInstance).not.toBeNull();
        },
        { timeout: 1000 }
      );

      act(() => {
        mockWebSocketInstance?.simulateOpen();
      });

      await waitFor(
        () => {
          expect(result.current.isConnected).toBe(true);
        },
        { timeout: 1000 }
      );

      act(() => {
        result.current.disconnect();
      });

      expect(result.current.isConnected).toBe(false);
      expect(mockWebSocketInstance?.getCloseCalls().length).toBeGreaterThan(0);
      expect(mockResourceManager.removeInterval).toHaveBeenCalled();
    });

    it('should not connect without auth token', async () => {
      const { result } = renderHook(() =>
        useWebSocketConnection({
          authToken: '',
          sessionId: 'test-session-id',
        })
      );

      await act(() => {
        result.current.connect();
      });

      expect(mockWebSocketInstance).toBeNull();
      expect(result.current.isConnected).toBe(false);
    });

    it('should not connect without session ID', async () => {
      const { result } = renderHook(() =>
        useWebSocketConnection({
          authToken: 'test-token',
          sessionId: null,
        })
      );

      await act(() => {
        result.current.connect();
      });

      expect(mockWebSocketInstance).toBeNull();
      expect(result.current.isConnected).toBe(false);
    });

    it('should not reconnect if already connected', async () => {
      const onConnected = vi.fn();
      const { result } = renderHook(() =>
        useWebSocketConnection({
          ...defaultOptions,
          onConnected,
        })
      );

      await act(() => {
        result.current.connect();
      });

      await waitFor(
        () => {
          mockWebSocketInstance = latestWebSocketInstance;
          expect(mockWebSocketInstance).not.toBeNull();
        },
        { timeout: 1000 }
      );

      await act(() => {
        mockWebSocketInstance?.simulateOpen();
      });

      await waitFor(
        () => {
          expect(result.current.isConnected).toBe(true);
        },
        { timeout: 1000 }
      );

      const firstInstance = mockWebSocketInstance;

      await act(() => {
        result.current.connect();
      });

      // Should not create a new WebSocket
      expect(mockWebSocketInstance).toBe(firstInstance);
    });

    it('should cleanup closed connection before reconnecting', async () => {
      const { result } = renderHook(() => useWebSocketConnection(defaultOptions));

      await act(() => {
        result.current.connect();
      });

      await waitFor(
        () => {
          mockWebSocketInstance = latestWebSocketInstance;
          expect(mockWebSocketInstance).not.toBeNull();
        },
        { timeout: 1000 }
      );

      await act(() => {
        mockWebSocketInstance?.simulateOpen();
      });

      await waitFor(
        () => {
          expect(result.current.isConnected).toBe(true);
        },
        { timeout: 1000 }
      );

      // Close the connection
      await act(() => {
        mockWebSocketInstance?.simulateClose();
      });

      await waitFor(
        () => {
          expect(result.current.isConnected).toBe(false);
        },
        { timeout: 1000 }
      );

      const firstInstance = mockWebSocketInstance;

      // Reconnect
      await act(() => {
        result.current.connect();
      });

      // Should create a new WebSocket after cleanup
      await waitFor(
        () => {
          mockWebSocketInstance = latestWebSocketInstance;
          expect(mockWebSocketInstance).not.toBeNull();
          expect(mockWebSocketInstance).not.toBe(firstInstance);
        },
        { timeout: 1000 }
      );
    });
  });

  describe('Message Handling', () => {
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
          mockWebSocketInstance = latestWebSocketInstance;
          expect(mockWebSocketInstance).not.toBeNull();
        },
        { timeout: 1000 }
      );

      await act(() => {
        mockWebSocketInstance?.simulateOpen();
      });

      await waitFor(
        () => {
          expect(result.current.isConnected).toBe(true);
        },
        { timeout: 1000 }
      );

      const testMessage = JSON.stringify({ type: 'test', data: 'hello' });

      await act(() => {
        mockWebSocketInstance?.simulateMessage(testMessage);
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
          mockWebSocketInstance = latestWebSocketInstance;
          expect(mockWebSocketInstance).not.toBeNull();
        },
        { timeout: 1000 }
      );

      await act(() => {
        mockWebSocketInstance?.simulateOpen();
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
        const sendCalls = mockWebSocketInstance?.getSendCalls();
        expect(sendCalls?.length).toBeGreaterThan(0);
        const sentData = JSON.parse(sendCalls?.[0]?.[0] as string);
        expect(sentData.message).toBe('test message');
      });
    });

    it('should not send message when not connected', async () => {
      const { result } = renderHook(() => useWebSocketConnection(defaultOptions));

      expect(result.current.isConnected).toBe(false);

      await act(() => {
        result.current.sendMessage('test message');
      });

      // WebSocket should not exist yet
      expect(mockWebSocketInstance).toBeNull();
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
          mockWebSocketInstance = latestWebSocketInstance;
          expect(mockWebSocketInstance).not.toBeNull();
        },
        { timeout: 1000 }
      );

      await act(() => {
        mockWebSocketInstance?.simulateOpen();
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
        const sendCalls = mockWebSocketInstance?.getSendCalls();
        if (sendCalls && sendCalls.length > 0) {
          const sentData = JSON.parse(sendCalls[0][0] as string);
          expect(sentData.message).toBe('sanitized');
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
          mockWebSocketInstance = latestWebSocketInstance;
          expect(mockWebSocketInstance).not.toBeNull();
        },
        { timeout: 1000 }
      );

      await act(() => {
        mockWebSocketInstance?.simulateOpen();
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
        const sendCalls = mockWebSocketInstance?.getSendCalls();
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
          mockWebSocketInstance = latestWebSocketInstance;
          expect(mockWebSocketInstance).not.toBeNull();
        },
        { timeout: 1000 }
      );

      await act(() => {
        mockWebSocketInstance?.simulateOpen();
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
        const sendCalls = mockWebSocketInstance?.getSendCalls();
        expect(sendCalls?.length || 0).toBe(0);
      });

      sanitizeSpy.mockRestore();
    });
  });

  describe('Error Handling', () => {
    it('should handle connection errors', async () => {
      const onError = vi.fn();
      const { result } = renderHook(() =>
        useWebSocketConnection({
          ...defaultOptions,
          onError,
        })
      );

      await act(() => {
        result.current.connect();
      });

      await waitFor(
        () => {
          mockWebSocketInstance = latestWebSocketInstance;
          expect(mockWebSocketInstance).not.toBeNull();
        },
        { timeout: 1000 }
      );

      await act(() => {
        mockWebSocketInstance?.simulateError();
      });

      await waitFor(
        () => {
          expect(result.current.lastError).toBe('WebSocket connection error');
          expect(result.current.isConnected).toBe(false);
        },
        { timeout: 1000 }
      );

      expect(onError).toHaveBeenCalled();
    });

    it('should handle WebSocket creation errors', async () => {
      const onError = vi.fn();
      const { result } = renderHook(() =>
        useWebSocketConnection({
          ...defaultOptions,
          onError,
        })
      );

      // Mock WebSocket constructor to throw - use a class that throws in constructor
      const originalWebSocket = global.WebSocket;
      class ThrowingWebSocket {
        constructor() {
          throw new Error('WebSocket creation failed');
        }
      }
      global.WebSocket = ThrowingWebSocket as unknown as typeof WebSocket;

      await act(() => {
        result.current.connect();
      });

      await waitFor(
        () => {
          expect(result.current.lastError).toBe('WebSocket creation failed');
        },
        { timeout: 1000 }
      );

      expect(onError).toHaveBeenCalled();

      // Restore original WebSocket
      global.WebSocket = originalWebSocket;
    });
  });

  describe('Ping/Heartbeat', () => {
    it('should send ping messages periodically', async () => {
      // Use fake timers from the start so the interval is created with fake timers
      vi.useFakeTimers();
      const { result } = renderHook(() => useWebSocketConnection(defaultOptions));

      act(() => {
        result.current.connect();
      });

      // Manually advance timers to allow WebSocket creation
      act(() => {
        vi.advanceTimersByTime(0);
      });

      // Get the WebSocket instance
      mockWebSocketInstance = latestWebSocketInstance;
      expect(mockWebSocketInstance).not.toBeNull();

      act(() => {
        mockWebSocketInstance?.simulateOpen();
      });

      // Advance timers to allow state updates
      act(() => {
        vi.advanceTimersByTime(0);
      });

      expect(result.current.isConnected).toBe(true);

      // Advance time by 30 seconds (ping interval)
      act(() => {
        vi.advanceTimersByTime(30000);
      });

      // Check that ping was sent
      const sendCalls = mockWebSocketInstance?.getSendCalls();
      expect(sendCalls?.length).toBeGreaterThan(0);
      const pingMessage = JSON.parse(sendCalls?.[0]?.[0] as string);
      expect(pingMessage.type).toBe('ping');

      vi.useRealTimers();
    });

    it('should perform health check in dev mode', async () => {
      vi.useFakeTimers();
      vi.stubEnv('DEV', 'true');
      (global.fetch as ReturnType<typeof vi.fn>).mockResolvedValue({ ok: true });

      const { result } = renderHook(() => useWebSocketConnection(defaultOptions));

      act(() => {
        result.current.connect();
      });

      // Manually advance timers to allow WebSocket creation
      act(() => {
        vi.advanceTimersByTime(0);
      });

      // Get the WebSocket instance
      mockWebSocketInstance = latestWebSocketInstance;
      expect(mockWebSocketInstance).not.toBeNull();

      act(() => {
        mockWebSocketInstance?.simulateOpen();
      });

      // Advance timers to allow state updates
      act(() => {
        vi.advanceTimersByTime(0);
      });

      expect(result.current.isConnected).toBe(true);

      // Advance time by 30 seconds to trigger ping interval
      act(() => {
        vi.advanceTimersByTime(30000);
      });

      // Advance timers to allow async fetch to complete
      act(() => {
        vi.advanceTimersByTime(0);
      });

      // Check that fetch was called
      expect(global.fetch).toHaveBeenCalledWith('/api/monitoring/health', {
        method: 'GET',
        headers: { Authorization: 'Bearer test-token' },
      });

      vi.useRealTimers();
      vi.unstubAllEnvs();
    });
  });

  describe('Cleanup', () => {
    it('should cleanup on unmount', async () => {
      const { result, unmount } = renderHook(() => useWebSocketConnection(defaultOptions));

      act(() => {
        result.current.connect();
      });

      await waitFor(
        () => {
          mockWebSocketInstance = latestWebSocketInstance;
          expect(mockWebSocketInstance).not.toBeNull();
        },
        { timeout: 1000 }
      );

      act(() => {
        mockWebSocketInstance?.simulateOpen();
      });

      await waitFor(
        () => {
          expect(result.current.isConnected).toBe(true);
        },
        { timeout: 1000 }
      );

      // Unmount should trigger cleanup synchronously
      act(() => {
        unmount();
      });

      // Cleanup should happen immediately on unmount
      expect(mockWebSocketInstance?.getCloseCalls().length).toBeGreaterThan(0);
      expect(mockResourceManager.removeInterval).toHaveBeenCalled();
    });

    it('should cleanup ping interval on disconnect', async () => {
      const { result } = renderHook(() => useWebSocketConnection(defaultOptions));

      act(() => {
        result.current.connect();
      });

      await waitFor(
        () => {
          mockWebSocketInstance = latestWebSocketInstance;
          expect(mockWebSocketInstance).not.toBeNull();
        },
        { timeout: 1000 }
      );

      act(() => {
        mockWebSocketInstance?.simulateOpen();
      });

      await waitFor(
        () => {
          expect(result.current.isConnected).toBe(true);
        },
        { timeout: 1000 }
      );

      // Disconnect should trigger cleanup synchronously
      act(() => {
        result.current.disconnect();
      });

      // Cleanup should happen immediately on disconnect
      expect(mockResourceManager.removeInterval).toHaveBeenCalled();
    });
  });

  describe('Callback Updates', () => {
    it('should use latest callbacks', async () => {
      const onConnected1 = vi.fn();
      const onConnected2 = vi.fn();

      const { result, rerender } = renderHook(
        ({ onConnected }) => useWebSocketConnection({ ...defaultOptions, onConnected }),
        {
          initialProps: { onConnected: onConnected1 },
        }
      );

      // Ensure hook is initialized
      expect(result.current).not.toBeNull();

      act(() => {
        result.current.connect();
      });

      await waitFor(
        () => {
          mockWebSocketInstance = latestWebSocketInstance;
          expect(mockWebSocketInstance).not.toBeNull();
        },
        { timeout: 1000 }
      );

      // Update callback before opening
      await act(async () => {
        rerender({ onConnected: onConnected2 });
        // Flush effects to ensure refs are updated
        await new Promise(resolve => setTimeout(resolve, 0));
      });

      act(() => {
        mockWebSocketInstance?.simulateOpen();
      });

      // Wait for the callback to be called
      await waitFor(
        () => {
          expect(onConnected2).toHaveBeenCalled();
          expect(onConnected1).not.toHaveBeenCalled();
        },
        { timeout: 1000 }
      );
    });
  });
});
