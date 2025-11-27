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

// Mock EventSource
class MockEventSource {
  public readyState = EventSource.CONNECTING;
  public onopen: ((event: Event) => void) | null = null;
  public onerror: ((event: Event) => void) | null = null;
  public onmessage: ((event: MessageEvent) => void) | null = null;

  constructor(public url: string) {
    setTimeout(() => {
      this.readyState = EventSource.OPEN;
      this.onopen?.(new Event('open'));
    }, 100);
  }

  close() {
    this.readyState = EventSource.CLOSED;
  }
}

// Mock global objects
Object.defineProperty(global, 'WebSocket', {
  value: MockWebSocket,
  writable: true,
});

Object.defineProperty(global, 'EventSource', {
  value: MockEventSource,
  writable: true,
});

// Import after mocking
import { ResourceManager, useResourceCleanup } from '../resourceCleanup';

describe('ResourceManager', () => {
  let resourceManager: ResourceManager;
  let mockWebSocket: MockWebSocket;
  let mockEventSource: MockEventSource;

  beforeEach(() => {
    vi.clearAllMocks();
    resourceManager = new ResourceManager();
    // nosemgrep: javascript.lang.security.detect-insecure-websocket.detect-insecure-websocket
    // This is a test mock, not a production WebSocket connection
    mockWebSocket = new MockWebSocket('ws://test');
    mockEventSource = new MockEventSource('http://test');
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

  describe('EventSource Management', () => {
    it('should register and cleanup EventSource connections', () => {
      resourceManager.registerEventSource(mockEventSource);

      expect(resourceManager.getActiveEventSources()).toHaveLength(1);

      resourceManager.cleanup();
      expect(resourceManager.getActiveEventSources()).toHaveLength(0);
      expect(mockEventSource.readyState).toBe(EventSource.CLOSED);
    });

    it('should handle multiple EventSource connections', () => {
      const es1 = new MockEventSource('http://test1');
      const es2 = new MockEventSource('http://test2');

      resourceManager.registerEventSource(es1);
      resourceManager.registerEventSource(es2);

      expect(resourceManager.getActiveEventSources()).toHaveLength(2);

      resourceManager.cleanup();
      expect(resourceManager.getActiveEventSources()).toHaveLength(0);
      expect(es1.readyState).toBe(EventSource.CLOSED);
      expect(es2.readyState).toBe(EventSource.CLOSED);
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
      const es = new MockEventSource('http://test');
      const customResource = { cleanup: vi.fn() };

      resourceManager.registerTimer(timer);
      resourceManager.registerInterval(interval);
      resourceManager.registerWebSocket(ws);
      resourceManager.registerEventSource(es);
      resourceManager.registerCustomResource(customResource);

      expect(resourceManager.getActiveTimers()).toHaveLength(1);
      expect(resourceManager.getActiveIntervals()).toHaveLength(1);
      expect(resourceManager.getActiveWebSockets()).toHaveLength(1);
      expect(resourceManager.getActiveEventSources()).toHaveLength(1);
      expect(resourceManager.getActiveCustomResources()).toHaveLength(1);

      resourceManager.cleanup();

      expect(resourceManager.getActiveTimers()).toHaveLength(0);
      expect(resourceManager.getActiveIntervals()).toHaveLength(0);
      expect(resourceManager.getActiveWebSockets()).toHaveLength(0);
      expect(resourceManager.getActiveEventSources()).toHaveLength(0);
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
      const es = new MockEventSource('http://test');
      const customResource = { cleanup: vi.fn() };

      resourceManager.registerTimer(timer);
      resourceManager.registerInterval(interval);
      resourceManager.registerWebSocket(ws);
      resourceManager.registerEventSource(es);
      resourceManager.registerCustomResource(customResource);

      const stats = resourceManager.getResourceStats();
      expect(stats).toEqual({
        timers: 1,
        intervals: 1,
        webSockets: 1,
        eventSources: 1,
        customResources: 1,
        total: 5,
      });
    });

    it('should return zero stats when no resources are registered', () => {
      const stats = resourceManager.getResourceStats();
      expect(stats).toEqual({
        timers: 0,
        intervals: 0,
        webSockets: 0,
        eventSources: 0,
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
