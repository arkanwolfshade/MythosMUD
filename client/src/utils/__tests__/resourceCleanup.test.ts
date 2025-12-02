import { renderHook } from '@testing-library/react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';

// Mock timers
vi.useFakeTimers();

// Mock WebSocket
class MockWebSocket {
  public readyState = WebSocket.CONNECTING;
  public onopen: ((event: Event) => void) | null = null;
  public onclose: ((event: CloseEvent) => void) | null = null;
  public onerror: ((event: Event) => void) | null = null;
  public onmessage: ((event: MessageEvent) => void) | null = null;

  constructor(public url: string) {
    setTimeout(() => {
      this.readyState = WebSocket.OPEN;
      this.onopen?.(new Event('open'));
    }, 100);
  }

  close() {
    this.readyState = WebSocket.CLOSED;
    this.onclose?.(new CloseEvent('close'));
  }

  send(_data: string) {
    // Mock send
  }
}

// Mock global objects
Object.defineProperty(global, 'WebSocket', {
  value: MockWebSocket,
  writable: true,
});

// Import after mocking
import {
  ResourceManager,
  useResourceCleanup,
  createTimerCleanup,
  createWebSocketCleanup,
  createCustomResourceCleanup,
} from '../resourceCleanup';

describe('ResourceManager', () => {
  let resourceManager: ResourceManager;
  let mockWebSocket: MockWebSocket;

  beforeEach(() => {
    vi.clearAllMocks();
    resourceManager = new ResourceManager();
    // nosemgrep: javascript.lang.security.detect-insecure-websocket.detect-insecure-websocket
    // This is a test mock, not a production WebSocket connection
    mockWebSocket = new MockWebSocket('ws://test');
  });

  afterEach(() => {
    resourceManager.cleanup();
    vi.clearAllTimers();
  });

  describe('Timer Management', () => {
    it('should register and cleanup timers', () => {
      const timerId = window.setTimeout(() => {}, 1000);
      resourceManager.registerTimer(timerId);

      expect(resourceManager.getActiveTimers()).toHaveLength(1);

      resourceManager.cleanup();
      expect(resourceManager.getActiveTimers()).toHaveLength(0);
    });

    it('should register and cleanup intervals', () => {
      const intervalId = window.setInterval(() => {}, 1000);
      resourceManager.registerInterval(intervalId);

      expect(resourceManager.getActiveIntervals()).toHaveLength(1);

      resourceManager.cleanup();
      expect(resourceManager.getActiveIntervals()).toHaveLength(0);
    });

    it('should handle multiple timers and intervals', () => {
      const timer1 = window.setTimeout(() => {}, 1000);
      const timer2 = window.setTimeout(() => {}, 2000);
      const interval1 = window.setInterval(() => {}, 1000);
      const interval2 = window.setInterval(() => {}, 2000);

      resourceManager.registerTimer(timer1);
      resourceManager.registerTimer(timer2);
      resourceManager.registerInterval(interval1);
      resourceManager.registerInterval(interval2);

      expect(resourceManager.getActiveTimers()).toHaveLength(2);
      expect(resourceManager.getActiveIntervals()).toHaveLength(2);

      resourceManager.cleanup();
      expect(resourceManager.getActiveTimers()).toHaveLength(0);
      expect(resourceManager.getActiveIntervals()).toHaveLength(0);
    });

    it('should not register duplicate timers', () => {
      const timerId = window.setTimeout(() => {}, 1000);
      resourceManager.registerTimer(timerId);
      resourceManager.registerTimer(timerId);

      expect(resourceManager.getActiveTimers()).toHaveLength(1);
    });
  });

  describe('WebSocket Management', () => {
    it('should register and cleanup WebSocket connections', () => {
      resourceManager.registerWebSocket(mockWebSocket);

      expect(resourceManager.getActiveWebSockets()).toHaveLength(1);

      resourceManager.cleanup();
      expect(resourceManager.getActiveWebSockets()).toHaveLength(0);
      expect(mockWebSocket.readyState).toBe(WebSocket.CLOSED);
    });

    it('should handle multiple WebSocket connections', () => {
      // nosemgrep: javascript.lang.security.detect-insecure-websocket.detect-insecure-websocket
      // These are test mocks, not production WebSocket connections
      const ws1 = new MockWebSocket('ws://test1');
      const ws2 = new MockWebSocket('ws://test2');

      resourceManager.registerWebSocket(ws1);
      resourceManager.registerWebSocket(ws2);

      expect(resourceManager.getActiveWebSockets()).toHaveLength(2);

      resourceManager.cleanup();
      expect(resourceManager.getActiveWebSockets()).toHaveLength(0);
      expect(ws1.readyState).toBe(WebSocket.CLOSED);
      expect(ws2.readyState).toBe(WebSocket.CLOSED);
    });
  });

  describe('Custom Resource Management', () => {
    it('should register and cleanup custom resources', () => {
      const customResource = {
        cleanup: vi.fn(),
        name: 'test-resource',
      };

      resourceManager.registerCustomResource(customResource);

      expect(resourceManager.getActiveCustomResources()).toHaveLength(1);

      resourceManager.cleanup();
      expect(resourceManager.getActiveCustomResources()).toHaveLength(0);
      expect(customResource.cleanup).toHaveBeenCalled();
    });

    it('should handle custom resources without cleanup method', () => {
      const customResource = {
        name: 'test-resource',
      };

      expect(() => {
        resourceManager.registerCustomResource(customResource);
        resourceManager.cleanup();
      }).not.toThrow();
    });
  });

  describe('Mixed Resource Management', () => {
    it('should cleanup all types of resources', () => {
      const timer = window.setTimeout(() => {}, 1000);
      const interval = window.setInterval(() => {}, 1000);
      // nosemgrep: javascript.lang.security.detect-insecure-websocket.detect-insecure-websocket
      // This is a test mock, not a production WebSocket connection
      const ws = new MockWebSocket('ws://test');
      const customResource = { cleanup: vi.fn() };

      resourceManager.registerTimer(timer);
      resourceManager.registerInterval(interval);
      resourceManager.registerWebSocket(ws);
      resourceManager.registerCustomResource(customResource);

      expect(resourceManager.getActiveTimers()).toHaveLength(1);
      expect(resourceManager.getActiveIntervals()).toHaveLength(1);
      expect(resourceManager.getActiveWebSockets()).toHaveLength(1);
      expect(resourceManager.getActiveCustomResources()).toHaveLength(1);

      resourceManager.cleanup();

      expect(resourceManager.getActiveTimers()).toHaveLength(0);
      expect(resourceManager.getActiveIntervals()).toHaveLength(0);
      expect(resourceManager.getActiveWebSockets()).toHaveLength(0);
      expect(resourceManager.getActiveCustomResources()).toHaveLength(0);
      expect(customResource.cleanup).toHaveBeenCalled();
    });
  });

  describe('Resource Statistics', () => {
    it('should provide resource statistics', () => {
      const timer = window.setTimeout(() => {}, 1000);
      const interval = window.setInterval(() => {}, 1000);
      // nosemgrep: javascript.lang.security.detect-insecure-websocket.detect-insecure-websocket
      // This is a test mock, not a production WebSocket connection
      const ws = new MockWebSocket('ws://test');
      const customResource = { cleanup: vi.fn() };

      resourceManager.registerTimer(timer);
      resourceManager.registerInterval(interval);
      resourceManager.registerWebSocket(ws);
      resourceManager.registerCustomResource(customResource);

      const stats = resourceManager.getResourceStats();
      expect(stats).toEqual({
        timers: 1,
        intervals: 1,
        webSockets: 1,
        customResources: 1,
        total: 4,
      });
    });

    it('should return zero stats when no resources are registered', () => {
      const stats = resourceManager.getResourceStats();
      expect(stats).toEqual({
        timers: 0,
        intervals: 0,
        webSockets: 0,
        customResources: 0,
        total: 0,
      });
    });
  });
});

describe('useResourceCleanup Hook', () => {
  beforeEach(() => {
    vi.clearAllMocks();
  });

  afterEach(() => {
    vi.clearAllTimers();
  });

  it('should create resource manager on mount', () => {
    const { result } = renderHook(() => useResourceCleanup());

    expect(result.current).toBeInstanceOf(ResourceManager);
  });

  it('should cleanup resources on unmount', () => {
    const { result, unmount } = renderHook(() => useResourceCleanup());

    const timer = window.setTimeout(() => {}, 1000);
    result.current.registerTimer(timer);

    expect(result.current.getActiveTimers()).toHaveLength(1);

    unmount();

    // Resources should be cleaned up
    expect(result.current.getActiveTimers()).toHaveLength(0);
  });

  it('should return the same resource manager instance', () => {
    const { result, rerender } = renderHook(() => useResourceCleanup());

    const manager1 = result.current;
    rerender();
    const manager2 = result.current;

    expect(manager1).toBe(manager2);
  });
});

describe('ResourceManager - Remove Methods', () => {
  let resourceManager: ResourceManager;

  beforeEach(() => {
    resourceManager = new ResourceManager();
  });

  afterEach(() => {
    resourceManager.cleanup();
  });

  it('should remove timer by id', () => {
    // Arrange - Test line 134: removeTimer branch
    const timerId = window.setTimeout(() => {}, 1000);
    resourceManager.registerTimer(timerId);
    expect(resourceManager.getActiveTimers()).toHaveLength(1);

    // Act
    resourceManager.removeTimer(timerId);

    // Assert
    expect(resourceManager.getActiveTimers()).toHaveLength(0);
  });

  it('should remove interval by id', () => {
    // Arrange - Test line 139: removeInterval branch
    const intervalId = window.setInterval(() => {}, 1000);
    resourceManager.registerInterval(intervalId);
    expect(resourceManager.getActiveIntervals()).toHaveLength(1);

    // Act
    resourceManager.removeInterval(intervalId);

    // Assert
    expect(resourceManager.getActiveIntervals()).toHaveLength(0);
  });

  it('should remove WebSocket', () => {
    // Arrange - Test line 144: removeWebSocket branch
    // nosemgrep: javascript.lang.security.detect-insecure-websocket.detect-insecure-websocket
    const ws = new MockWebSocket('ws://test');
    resourceManager.registerWebSocket(ws);
    expect(resourceManager.getActiveWebSockets()).toHaveLength(1);

    // Act
    resourceManager.removeWebSocket(ws);

    // Assert
    expect(resourceManager.getActiveWebSockets()).toHaveLength(0);
  });

  it('should remove custom resource', () => {
    // Arrange - Test line 149: removeCustomResource branch
    const customResource = { cleanup: vi.fn(), name: 'test' };
    resourceManager.registerCustomResource(customResource);
    expect(resourceManager.getActiveCustomResources()).toHaveLength(1);

    // Act
    resourceManager.removeCustomResource(customResource);

    // Assert
    expect(resourceManager.getActiveCustomResources()).toHaveLength(0);
  });

  it('should handle error when cleaning up custom resource', () => {
    // Arrange - Test line 124: error handling in cleanupCustomResources
    const consoleErrorSpy = vi.spyOn(console, 'error').mockImplementation(() => {});
    const customResource = {
      cleanup: vi.fn(() => {
        throw new Error('Cleanup failed');
      }),
      name: 'test',
    };
    resourceManager.registerCustomResource(customResource);

    // Act
    resourceManager.cleanup();

    // Assert - should handle error gracefully
    expect(consoleErrorSpy).toHaveBeenCalled();
    expect(consoleErrorSpy.mock.calls.some(call => call[0]?.includes('Error cleaning up custom resource'))).toBe(true);
    consoleErrorSpy.mockRestore();
  });
});

describe('createTimerCleanup', () => {
  it('should create setTimeout wrapper that registers timer', () => {
    // Arrange - Test lines 181-190: createTimerCleanup branches
    const resourceManager = new ResourceManager();
    const { setTimeout: customSetTimeout } = createTimerCleanup(resourceManager);

    // Act
    const timerId = customSetTimeout(() => {}, 1000);

    // Assert
    expect(resourceManager.getActiveTimers()).toContain(timerId);
    resourceManager.cleanup();
  });

  it('should create setInterval wrapper that registers interval', () => {
    // Arrange - Test lines 181-190: createTimerCleanup branches
    const resourceManager = new ResourceManager();
    const { setInterval: customSetInterval } = createTimerCleanup(resourceManager);

    // Act
    const intervalId = customSetInterval(() => {}, 1000);

    // Assert
    expect(resourceManager.getActiveIntervals()).toContain(intervalId);
    resourceManager.cleanup();
  });
});

describe('createWebSocketCleanup', () => {
  it('should create WebSocket wrapper that registers connection', () => {
    // Arrange - Test lines 199-202: createWebSocketCleanup branches
    const resourceManager = new ResourceManager();
    const createWebSocket = createWebSocketCleanup(resourceManager);

    // Act
    // nosemgrep: javascript.lang.security.detect-insecure-websocket.detect-insecure-websocket
    const ws = createWebSocket('ws://test');

    // Assert
    expect(resourceManager.getActiveWebSockets()).toContain(ws);
    resourceManager.cleanup();
  });

  it('should create WebSocket with protocols', () => {
    // Arrange - Test lines 199-202: createWebSocketCleanup with protocols
    const resourceManager = new ResourceManager();
    const createWebSocket = createWebSocketCleanup(resourceManager);

    // Act
    // nosemgrep: javascript.lang.security.detect-insecure-websocket.detect-insecure-websocket
    const ws = createWebSocket('ws://test', 'protocol1');

    // Assert
    expect(resourceManager.getActiveWebSockets()).toContain(ws);
    resourceManager.cleanup();
  });
});

describe('createCustomResourceCleanup', () => {
  it('should create custom resource cleanup function', () => {
    // Arrange - Test lines 209-212: createCustomResourceCleanup branch
    const resourceManager = new ResourceManager();
    const registerCustom = createCustomResourceCleanup(resourceManager);
    const customResource = { cleanup: vi.fn(), name: 'test' };

    // Act
    registerCustom(customResource);

    // Assert
    expect(resourceManager.getActiveCustomResources()).toContain(customResource);
    resourceManager.cleanup();
  });
});
