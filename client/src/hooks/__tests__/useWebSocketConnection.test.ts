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

// Mock inputSanitizer
vi.mock('../../utils/security', () => ({
  inputSanitizer: {
    sanitizeCommand: vi.fn((message: string) => message),
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

// Mock fetch for NATS health check (DEV mode)
global.fetch = vi.fn();

// Mock WebSocket
class MockWebSocket {
  static CONNECTING = 0;
  static OPEN = 1;
  static CLOSING = 2;
  static CLOSED = 3;

  url: string;
  protocols?: string[];
  readyState: number = MockWebSocket.CONNECTING;
  send: ReturnType<typeof vi.fn>;
  close: ReturnType<typeof vi.fn>;

  onopen: ((this: MockWebSocket, ev: Event) => void) | null = null;
  onmessage: ((this: MockWebSocket, ev: MessageEvent) => void) | null = null;
  onerror: ((this: MockWebSocket, ev: Event) => void) | null = null;
  onclose: ((this: MockWebSocket, ev: CloseEvent) => void) | null = null;

  constructor(url: string | URL, protocols?: string | string[]) {
    this.url = typeof url === 'string' ? url : url.toString();
    this.protocols = Array.isArray(protocols) ? protocols : protocols ? [protocols] : undefined;
    this.send = vi.fn();
    this.close = vi.fn(() => {
      this.readyState = MockWebSocket.CLOSED;
    });

    // Simulate connection immediately via microtask
    queueMicrotask(() => {
      if (this.readyState === MockWebSocket.CONNECTING) {
        this.readyState = MockWebSocket.OPEN;
        if (this.onopen) {
          this.onopen(new Event('open'));
        }
      }
    });
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

  simulateClose(code?: number, reason?: string) {
    this.readyState = MockWebSocket.CLOSED;
    if (this.onclose) {
      const closeEvent = new CloseEvent('close', { code, reason, wasClean: true });
      this.onclose(closeEvent);
    }
  }
}

describe('useWebSocketConnection', () => {
  let mockWebSocketInstance: MockWebSocket | null = null;
  let originalWebSocket: typeof global.WebSocket;
  let mockSetInterval: ReturnType<typeof vi.fn>;
  let mockClearInterval: ReturnType<typeof vi.fn>;
  let mockFetch: ReturnType<typeof vi.fn>;

  beforeEach(() => {
    vi.clearAllMocks();

    // Mock setInterval/clearInterval
    mockSetInterval = vi.fn((_callback: () => void | Promise<void>, _delay: number) => {
      return 12345 as unknown as number; // Return mock interval ID
    });
    mockClearInterval = vi.fn();
    window.setInterval = mockSetInterval;
    window.clearInterval = mockClearInterval;

    // Mock fetch
    mockFetch = vi.fn(() => Promise.resolve({ ok: true }));
    global.fetch = mockFetch;

    // Mock WebSocket
    originalWebSocket = global.WebSocket;
    global.WebSocket = MockWebSocket as unknown as typeof global.WebSocket;

    // Track WebSocket instances
    const OriginalWebSocket = MockWebSocket;
    vi.spyOn(global, 'WebSocket').mockImplementation((url: string | URL, protocols?: string | string[]) => {
      mockWebSocketInstance = new OriginalWebSocket(url, protocols);
      return mockWebSocketInstance as unknown as WebSocket;
    });
  });

  afterEach(() => {
    global.WebSocket = originalWebSocket;
    mockWebSocketInstance = null;
    vi.restoreAllMocks();
  });

  const defaultOptions = {
    authToken: 'test-token',
    sessionId: 'test-session-id',
  };

  describe('Connection Management', () => {
    it('should start disconnected', () => {
      // Arrange & Act
      const { result } = renderHook(() => useWebSocketConnection(defaultOptions));

      // Assert
      expect(result.current.isConnected).toBe(false);
      expect(result.current.lastError).toBeNull();
    });

    it('should connect successfully', async () => {
      // Arrange
      const onConnected = vi.fn();
      const { result } = renderHook(() =>
        useWebSocketConnection({
          ...defaultOptions,
          onConnected,
        })
      );

      // Act
      act(() => {
        result.current.connect();
      });

      // Assert
      await waitFor(
        () => {
          expect(result.current.isConnected).toBe(true);
        },
        { timeout: 1000 }
      );
      expect(onConnected).toHaveBeenCalled();
      expect(result.current.lastError).toBeNull();
      expect(mockWebSocketInstance).toBeDefined();
      expect(mockWebSocketInstance?.url).toContain('/api/ws');
      expect(mockWebSocketInstance?.protocols).toContain('bearer');
      expect(mockWebSocketInstance?.protocols).toContain('test-token');
    });

    it('should disconnect successfully', async () => {
      // Arrange
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
          expect(result.current.isConnected).toBe(true);
        },
        { timeout: 1000 }
      );

      // Act
      act(() => {
        result.current.disconnect();
      });

      // Assert
      expect(result.current.isConnected).toBe(false);
      expect(mockWebSocketInstance?.close).toHaveBeenCalled();
      expect(mockClearInterval).toHaveBeenCalled();
    });

    it('should not connect without auth token', () => {
      // Arrange
      const { result } = renderHook(() => useWebSocketConnection({ authToken: '', sessionId: null }));

      // Act
      act(() => {
        result.current.connect();
      });

      // Assert
      expect(result.current.isConnected).toBe(false);
      expect(mockWebSocketInstance).toBeNull();
    });

    it('should not connect without session ID', () => {
      // Arrange
      const { result } = renderHook(() => useWebSocketConnection({ authToken: 'test-token', sessionId: null }));

      // Act
      act(() => {
        result.current.connect();
      });

      // Assert
      expect(result.current.isConnected).toBe(false);
      expect(mockWebSocketInstance).toBeNull();
    });
  });

  describe('Message Handling', () => {
    it('should handle incoming messages', async () => {
      // Arrange
      const onMessage = vi.fn();
      const { result } = renderHook(() =>
        useWebSocketConnection({
          ...defaultOptions,
          onMessage,
        })
      );

      act(() => {
        result.current.connect();
      });

      await waitFor(
        () => {
          expect(result.current.isConnected).toBe(true);
        },
        { timeout: 1000 }
      );

      // Act
      act(() => {
        mockWebSocketInstance?.simulateMessage('{"type": "test", "data": "hello"}');
      });

      // Assert
      expect(onMessage).toHaveBeenCalled();
      const messageEvent = onMessage.mock.calls[0][0];
      expect(messageEvent.data).toBe('{"type": "test", "data": "hello"}');
    });

    it('should send messages', async () => {
      // Arrange
      const { result } = renderHook(() => useWebSocketConnection(defaultOptions));

      act(() => {
        result.current.connect();
      });

      await waitFor(
        () => {
          expect(result.current.isConnected).toBe(true);
        },
        { timeout: 1000 }
      );

      // Act
      act(() => {
        result.current.sendMessage('test message');
      });

      // Assert
      expect(mockWebSocketInstance?.send).toHaveBeenCalled();
      const sentData = mockWebSocketInstance?.send.mock.calls[0][0];
      const parsed = JSON.parse(sentData);
      expect(parsed.message).toBe('test message');
      expect(parsed.timestamp).toBeDefined();
    });

    it('should not send message when not connected', () => {
      // Arrange
      const { result } = renderHook(() => useWebSocketConnection(defaultOptions));

      // Act
      act(() => {
        result.current.sendMessage('test message');
      });

      // Assert
      expect(mockWebSocketInstance?.send).not.toHaveBeenCalled();
    });

    it('should reject invalid message types', async () => {
      // Arrange
      const { result } = renderHook(() => useWebSocketConnection(defaultOptions));

      act(() => {
        result.current.connect();
      });

      await waitFor(
        () => {
          expect(result.current.isConnected).toBe(true);
        },
        { timeout: 1000 }
      );

      // Act
      act(() => {
        result.current.sendMessage(null as unknown as string);
      });

      // Assert
      expect(mockWebSocketInstance?.send).not.toHaveBeenCalled();
    });

    it('should reject messages that are too long', async () => {
      // Arrange
      const { result } = renderHook(() => useWebSocketConnection(defaultOptions));

      act(() => {
        result.current.connect();
      });

      await waitFor(
        () => {
          expect(result.current.isConnected).toBe(true);
        },
        { timeout: 1000 }
      );

      // Act
      const longMessage = 'a'.repeat(1001);
      act(() => {
        result.current.sendMessage(longMessage);
      });

      // Assert
      expect(mockWebSocketInstance?.send).not.toHaveBeenCalled();
    });
  });

  describe('Error Handling', () => {
    it('should handle connection errors', async () => {
      // Arrange
      const onError = vi.fn();
      const { result } = renderHook(() =>
        useWebSocketConnection({
          ...defaultOptions,
          onError,
        })
      );

      act(() => {
        result.current.connect();
      });

      await waitFor(
        () => {
          expect(result.current.isConnected).toBe(true);
        },
        { timeout: 1000 }
      );

      // Act
      act(() => {
        mockWebSocketInstance?.simulateError();
      });

      // Assert
      await waitFor(
        () => {
          expect(result.current.lastError).toBe('WebSocket connection error');
        },
        { timeout: 1000 }
      );
      expect(result.current.isConnected).toBe(false);
      expect(onError).toHaveBeenCalled();
    });

    it('should handle connection close', async () => {
      // Arrange
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
          expect(result.current.isConnected).toBe(true);
        },
        { timeout: 1000 }
      );

      // Act
      act(() => {
        mockWebSocketInstance?.simulateClose();
      });

      // Assert
      await waitFor(
        () => {
          expect(result.current.isConnected).toBe(false);
          expect(onDisconnect).toHaveBeenCalled();
        },
        { timeout: 1000 }
      );
      expect(mockClearInterval).toHaveBeenCalled();
    });
  });

  describe('Ping/Heartbeat', () => {
    it('should start ping interval on connection', async () => {
      // Arrange
      const { result } = renderHook(() => useWebSocketConnection(defaultOptions));

      // Act
      act(() => {
        result.current.connect();
      });

      await waitFor(
        () => {
          expect(result.current.isConnected).toBe(true);
        },
        { timeout: 1000 }
      );

      // Assert
      expect(mockSetInterval).toHaveBeenCalled();
      expect(mockResourceManager.registerInterval).toHaveBeenCalled();
    });

    it('should send ping messages', async () => {
      // Arrange
      const { result } = renderHook(() => useWebSocketConnection(defaultOptions));

      act(() => {
        result.current.connect();
      });

      await waitFor(
        () => {
          expect(result.current.isConnected).toBe(true);
        },
        { timeout: 1000 }
      );

      // Act - simulate ping interval callback
      const pingCallback = mockSetInterval.mock.calls[0][0];
      await act(async () => {
        await pingCallback();
      });

      // Assert
      expect(mockWebSocketInstance?.send).toHaveBeenCalled();
      const sentData = mockWebSocketInstance?.send.mock.calls[0][0];
      const parsed = JSON.parse(sentData);
      expect(parsed.type).toBe('ping');
    });
  });

  describe('Reconnection Logic', () => {
    it('should not reconnect if already connected', async () => {
      // Arrange
      const onConnected = vi.fn();
      const { result } = renderHook(() =>
        useWebSocketConnection({
          ...defaultOptions,
          onConnected,
        })
      );

      act(() => {
        result.current.connect();
      });

      await waitFor(
        () => {
          expect(result.current.isConnected).toBe(true);
        },
        { timeout: 1000 }
      );

      onConnected.mockClear();
      const firstInstance = mockWebSocketInstance;

      // Act - try to connect again
      act(() => {
        result.current.connect();
      });

      // Assert - should not create new WebSocket, but should call onConnected
      expect(mockWebSocketInstance).toBe(firstInstance);
      expect(onConnected).toHaveBeenCalled();
    });

    it('should cleanup closed connection before reconnecting', async () => {
      // Arrange
      const { result } = renderHook(() => useWebSocketConnection(defaultOptions));

      act(() => {
        result.current.connect();
      });

      await waitFor(
        () => {
          expect(result.current.isConnected).toBe(true);
        },
        { timeout: 1000 }
      );

      // Close connection
      act(() => {
        mockWebSocketInstance?.simulateClose();
      });

      await waitFor(
        () => {
          expect(result.current.isConnected).toBe(false);
        },
        { timeout: 1000 }
      );

      // Act - reconnect
      const originalInstance = mockWebSocketInstance;
      act(() => {
        result.current.connect();
      });

      // Assert - should create new WebSocket instance
      await waitFor(
        () => {
          expect(mockWebSocketInstance).not.toBe(originalInstance);
          expect(mockWebSocketInstance).toBeDefined();
        },
        { timeout: 1000 }
      );
    });
  });

  describe('Cleanup', () => {
    it('should cleanup on unmount', async () => {
      // Arrange
      const onDisconnect = vi.fn();
      const { result, unmount } = renderHook(() =>
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
          expect(result.current.isConnected).toBe(true);
        },
        { timeout: 1000 }
      );

      // Act
      unmount();

      // Assert
      await waitFor(
        () => {
          expect(mockWebSocketInstance?.close).toHaveBeenCalled();
          expect(onDisconnect).toHaveBeenCalled();
        },
        { timeout: 1000 }
      );
    });

    it('should clear ping interval on disconnect', async () => {
      // Arrange
      const { result } = renderHook(() => useWebSocketConnection(defaultOptions));

      act(() => {
        result.current.connect();
      });

      await waitFor(
        () => {
          expect(result.current.isConnected).toBe(true);
        },
        { timeout: 1000 }
      );

      expect(mockSetInterval).toHaveBeenCalled();
      const intervalId = mockSetInterval.mock.results[0].value;

      // Act
      act(() => {
        result.current.disconnect();
      });

      // Assert
      expect(mockClearInterval).toHaveBeenCalledWith(intervalId);
      expect(mockResourceManager.removeInterval).toHaveBeenCalledWith(intervalId);
    });
  });
});
