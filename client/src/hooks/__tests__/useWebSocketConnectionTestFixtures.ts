/**
 * Shared mocks and helpers for useWebSocketConnection tests.
 */

import { vi } from 'vitest';

declare const global: typeof globalThis;

const { mockResourceManager, fetchSpy, mockedSetInterval, mockedClearInterval } = vi.hoisted(() => {
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

  const fetchSpy = vi.spyOn(global, 'fetch');

  const intervalIds = new Set<number>();
  let intervalIdCounter = 1;

  const originalSetInterval = global.setInterval;
  const originalClearInterval = global.clearInterval;

  const mockedSetInterval: ReturnType<typeof vi.fn> = vi.fn(
    (handler: TimerHandler, timeout?: number, ...args: unknown[]) => {
      const id = intervalIdCounter++;
      intervalIds.add(id);
      const actualSetInterval = global.setInterval;
      if (actualSetInterval === (mockedSetInterval as unknown as typeof setInterval)) {
        return originalSetInterval(handler, timeout, ...(args as Parameters<typeof setInterval>));
      }
      if (actualSetInterval !== originalSetInterval) {
        return actualSetInterval(handler, timeout, ...(args as Parameters<typeof setInterval>));
      }
      return originalSetInterval(handler, timeout, ...(args as Parameters<typeof setInterval>));
    }
  );

  if (typeof window !== 'undefined') {
    window.setInterval = mockedSetInterval as unknown as typeof window.setInterval;
  }

  let isClearing = false;
  const mockedClearInterval = vi.fn((id: number) => {
    if (isClearing) {
      originalClearInterval(id);
    }
    isClearing = true;
    try {
      intervalIds.delete(id);
      const currentClearInterval = global.clearInterval;
      if (currentClearInterval === mockedClearInterval) {
        originalClearInterval(id);
      } else {
        currentClearInterval(id);
      }
    } finally {
      isClearing = false;
    }
  }) as typeof clearInterval;

  if (typeof window !== 'undefined') {
    window.clearInterval = mockedClearInterval;
  }

  return { mockResourceManager, fetchSpy, mockedSetInterval, mockedClearInterval };
});

vi.mock('../../utils/logger', () => ({
  logger: {
    debug: vi.fn(),
    info: vi.fn(),
    warn: vi.fn(),
    error: vi.fn(),
  },
}));

vi.mock('../../utils/resourceCleanup', () => ({
  useResourceCleanup: () => mockResourceManager,
}));

vi.mock('../../utils/security', () => ({
  inputSanitizer: {
    sanitizeCommand: vi.fn((input: string) => input),
  },
}));

export class MockWebSocket {
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

export let latestWebSocketInstance: MockWebSocket | null = null;

export const wsTestState = {
  mockWebSocketInstance: null as MockWebSocket | null,
  originalWebSocket: null as typeof global.WebSocket | null,
};

export const defaultOptions = {
  authToken: 'test-token',
  sessionId: 'test-session-id',
};

export { fetchSpy, mockResourceManager, mockedClearInterval, mockedSetInterval };

export function wsConnectionBeforeEach(): void {
  vi.clearAllMocks();
  fetchSpy.mockClear();
  mockResourceManager.removeInterval.mockClear();
  mockResourceManager.removeTimer.mockClear();
  mockResourceManager.registerInterval.mockClear();
  mockResourceManager.registerTimer.mockClear();
  wsTestState.mockWebSocketInstance = null;
  latestWebSocketInstance = null;

  wsTestState.originalWebSocket = global.WebSocket;
  global.WebSocket = MockWebSocket as unknown as typeof global.WebSocket;

  (global.WebSocket as unknown as { CONNECTING: number }).CONNECTING = 0;
  (global.WebSocket as unknown as { OPEN: number }).OPEN = 1;
  (global.WebSocket as unknown as { CLOSING: number }).CLOSING = 2;
  (global.WebSocket as unknown as { CLOSED: number }).CLOSED = 3;

  vi.stubEnv('DEV', true);
}

export function wsConnectionAfterEach(): void {
  fetchSpy.mockReset();
  if (wsTestState.originalWebSocket) {
    global.WebSocket = wsTestState.originalWebSocket;
  }
  wsTestState.mockWebSocketInstance = null;
  latestWebSocketInstance = null;
  vi.restoreAllMocks();
  vi.unstubAllEnvs();
}
