import { describe, it, expect, vi, beforeEach, afterEach } from 'vitest';
import { renderHook, act } from '@testing-library/react';
import { useGameConnection } from '../useGameConnection';

// Minimal mocks for browser APIs used by the hook
class MockEventSource implements Partial<EventSource> {
  url: string;
  options?: EventSourceInit;
  onopen: ((this: EventSource, ev: Event) => unknown) | null = null;
  onmessage: ((this: EventSource, ev: MessageEvent) => unknown) | null = null;
  onerror: ((this: EventSource, ev: Event) => unknown) | null = null;
  readyState = 0;
  constructor(url: string, options?: EventSourceInit) {
    this.url = url;
    this.options = options;
    // do nothing by default
  }
  close() {}
}

class MockWebSocket implements Partial<WebSocket> {
  static OPEN = 1;
  readyState = 0;
  url: string;
  constructor(url: string) {
    this.url = url;
  }
  send() {}
  close() {}
}

describe('useGameConnection SSE URL security', () => {
  const originalEventSource = globalThis.EventSource;
  const originalWebSocket = globalThis.WebSocket;

  beforeEach(() => {
    vi.useFakeTimers();
    // @ts-expect-error override globals for test
    globalThis.EventSource = MockEventSource as unknown as typeof EventSource;
    // @ts-expect-error override globals for test
    globalThis.WebSocket = MockWebSocket as unknown as typeof WebSocket;
  });

  afterEach(() => {
    vi.useRealTimers();
    // @ts-expect-error restore
    globalThis.EventSource = originalEventSource;
    // @ts-expect-error restore
    globalThis.WebSocket = originalWebSocket;
  });

  it('does not include token in SSE URL and uses withCredentials', () => {
    const created: { url?: string; opts?: EventSourceInit } = {};

    // Intercept constructor to capture args
    const g = globalThis as unknown as { EventSource: typeof EventSource };
    const ctorSpy = vi.spyOn(g, 'EventSource').mockImplementation((url: string, opts?: EventSourceInit) => {
      created.url = url;
      created.opts = opts;
      return new MockEventSource(url, opts) as unknown as EventSource;
    });

    const { result } = renderHook(() =>
      useGameConnection({
        authToken: 'abc123',
        sessionId: 'session_xyz',
      } as unknown as Parameters<typeof useGameConnection>[0])
    );

    act(() => {
      result.current.connect();
    });

    expect(created.url).toBeDefined();
    expect(created.url).toContain('/api/events');
    expect(created.url).toContain('session_id=session_xyz');
    expect(created.url).toContain('token=abc123');
    expect(created.opts?.withCredentials).toBe(true);

    ctorSpy.mockRestore();
  });
});
