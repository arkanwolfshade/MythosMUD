/**
 * Unit tests for connection state machine.
 *
 * Tests all state transitions, guards, and edge cases using XState testing utilities.
 */

import { describe, expect, it } from 'vitest';
import { createActor } from 'xstate';
import { connectionMachine } from './useConnectionStateMachine';

describe('Connection State Machine', () => {
  it('should start in disconnected state', () => {
    const actor = createActor(connectionMachine);
    actor.start();

    expect(actor.getSnapshot().value).toBe('disconnected');
    expect(actor.getSnapshot().context.reconnectAttempts).toBe(0);

    actor.stop();
  });

  it('should transition from disconnected to connecting_sse on CONNECT', () => {
    const actor = createActor(connectionMachine);
    actor.start();

    actor.send({ type: 'CONNECT' });

    expect(actor.getSnapshot().value).toBe('connecting_sse');

    actor.stop();
  });

  it('should transition to sse_connected on SSE_CONNECTED', () => {
    const actor = createActor(connectionMachine);
    actor.start();

    actor.send({ type: 'CONNECT' });
    actor.send({ type: 'SSE_CONNECTED', sessionId: 'test-session-123' });

    expect(actor.getSnapshot().value).toBe('sse_connected');
    expect(actor.getSnapshot().context.sessionId).toBe('test-session-123');

    actor.stop();
  });

  it('should transition to connecting_ws when SSE connected', () => {
    const actor = createActor(connectionMachine);
    actor.start();

    actor.send({ type: 'CONNECT' });
    actor.send({ type: 'SSE_CONNECTED', sessionId: 'test-session' });
    actor.send({ type: 'CONNECT' });

    expect(actor.getSnapshot().value).toBe('connecting_ws');

    actor.stop();
  });

  it('should transition to fully_connected on WS_CONNECTED', () => {
    const actor = createActor(connectionMachine);
    actor.start();

    actor.send({ type: 'CONNECT' });
    actor.send({ type: 'SSE_CONNECTED', sessionId: 'test-session' });
    actor.send({ type: 'CONNECT' });
    actor.send({ type: 'WS_CONNECTED' });

    expect(actor.getSnapshot().value).toBe('fully_connected');
    expect(actor.getSnapshot().context.reconnectAttempts).toBe(0);

    actor.stop();
  });

  it('should transition to reconnecting on SSE_FAILED', () => {
    const actor = createActor(connectionMachine);
    actor.start();

    actor.send({ type: 'CONNECT' });
    actor.send({ type: 'SSE_FAILED', error: 'Connection refused' });

    expect(actor.getSnapshot().value).toBe('reconnecting');
    expect(actor.getSnapshot().context.lastError).toBe('Connection refused');
    expect(actor.getSnapshot().context.reconnectAttempts).toBeGreaterThan(0);

    actor.stop();
  });

  it('should transition to reconnecting on WS_FAILED', () => {
    const actor = createActor(connectionMachine);
    actor.start();

    actor.send({ type: 'CONNECT' });
    actor.send({ type: 'SSE_CONNECTED', sessionId: 'test-session' });
    actor.send({ type: 'CONNECT' });
    actor.send({ type: 'WS_FAILED', error: 'WebSocket error' });

    expect(actor.getSnapshot().value).toBe('reconnecting');
    expect(actor.getSnapshot().context.lastError).toBe('WebSocket error');

    actor.stop();
  });

  it('should store session ID on SSE_CONNECTED', () => {
    const actor = createActor(connectionMachine);
    actor.start();

    actor.send({ type: 'CONNECT' });
    actor.send({ type: 'SSE_CONNECTED', sessionId: 'session-abc-123' });

    expect(actor.getSnapshot().context.sessionId).toBe('session-abc-123');

    actor.stop();
  });

  it('should preserve session ID after SSE connected', () => {
    const actor = createActor(connectionMachine);
    actor.start();

    actor.send({ type: 'CONNECT' });
    actor.send({ type: 'SSE_CONNECTED', sessionId: 'session-xyz' });
    actor.send({ type: 'CONNECT' }); // Move to connecting_ws

    expect(actor.getSnapshot().context.sessionId).toBe('session-xyz');

    actor.stop();
  });

  it('should reset reconnect attempts on successful connection', () => {
    const actor = createActor(connectionMachine);
    actor.start();

    // Fail once
    actor.send({ type: 'CONNECT' });
    actor.send({ type: 'SSE_FAILED', error: 'Test' });
    expect(actor.getSnapshot().context.reconnectAttempts).toBe(1);

    // Reset to disconnected first, then connect successfully
    actor.send({ type: 'DISCONNECT' });
    actor.send({ type: 'CONNECT' });
    actor.send({ type: 'SSE_CONNECTED', sessionId: 'test' });
    actor.send({ type: 'CONNECT' });
    actor.send({ type: 'WS_CONNECTED' });

    expect(actor.getSnapshot().context.reconnectAttempts).toBe(0);

    actor.stop();
  });

  it('should handle multiple connection/disconnection cycles', () => {
    const actor = createActor(connectionMachine);
    actor.start();

    for (let i = 0; i < 3; i++) {
      // Connect
      actor.send({ type: 'CONNECT' });
      actor.send({ type: 'SSE_CONNECTED', sessionId: `session-${i}` });
      actor.send({ type: 'CONNECT' });
      actor.send({ type: 'WS_CONNECTED' });

      expect(actor.getSnapshot().value).toBe('fully_connected');

      // Disconnect
      actor.send({ type: 'DISCONNECT' });
      expect(actor.getSnapshot().value).toBe('disconnected');
    }

    actor.stop();
  });

  it('should handle disconnection from reconnecting state', () => {
    const actor = createActor(connectionMachine);
    actor.start();

    // Start connecting
    actor.send({ type: 'CONNECT' });
    actor.send({ type: 'SSE_FAILED', error: 'Error' });

    expect(actor.getSnapshot().value).toBe('reconnecting');

    // Disconnect during reconnect
    actor.send({ type: 'DISCONNECT' });

    expect(actor.getSnapshot().value).toBe('disconnected');

    actor.stop();
  });

  it('should preserve error information', () => {
    const actor = createActor(connectionMachine);
    actor.start();

    actor.send({ type: 'CONNECT' });
    actor.send({ type: 'SSE_FAILED', error: 'Persistent error' });

    expect(actor.getSnapshot().context.lastError).toBe('Persistent error');

    actor.stop();
  });
});
