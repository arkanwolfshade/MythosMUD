/**
 * Tests for XState connection state machine.
 *
 * As documented in the Necronomicon's chapter on dimensional gateways,
 * connections must follow strict state transitions.
 *
 * AI: Tests XState v5 FSM for frontend connection management.
 */

import { beforeEach, describe, expect, it } from 'vitest';
import { createActor } from 'xstate';
import { connectionMachine } from '../useConnectionStateMachine';

describe('Connection State Machine', () => {
  let actor: ReturnType<typeof createActor<typeof connectionMachine>>;

  beforeEach(() => {
    actor = createActor(connectionMachine);
    actor.start();
  });

  it('initializes in disconnected state', () => {
    expect(actor.getSnapshot().value).toBe('disconnected');
  });

  it('transitions to connecting_sse on CONNECT event', () => {
    actor.send({ type: 'CONNECT' });
    expect(actor.getSnapshot().value).toBe('connecting_sse');
  });

  it('transitions to sse_connected on SSE_CONNECTED event', () => {
    actor.send({ type: 'CONNECT' });
    actor.send({ type: 'SSE_CONNECTED' });
    expect(actor.getSnapshot().value).toBe('sse_connected');
  });

  it('transitions to connecting_ws after SSE connection', () => {
    actor.send({ type: 'CONNECT' });
    actor.send({ type: 'SSE_CONNECTED' });
    actor.send({ type: 'WS_CONNECTING' });
    expect(actor.getSnapshot().value).toBe('connecting_ws');
  });

  it('transitions to fully_connected when both connections established', () => {
    actor.send({ type: 'CONNECT' });
    actor.send({ type: 'SSE_CONNECTED' });
    actor.send({ type: 'WS_CONNECTING' });
    actor.send({ type: 'WS_CONNECTED' });
    expect(actor.getSnapshot().value).toBe('fully_connected');
  });

  it('transitions to failed state on connection error', () => {
    actor.send({ type: 'CONNECT' });
    actor.send({ type: 'ERROR', error: 'Connection timeout' });
    expect(actor.getSnapshot().value).toBe('failed');
  });

  it('tracks reconnect attempts in context', () => {
    actor.send({ type: 'CONNECT' });
    actor.send({ type: 'ERROR', error: 'Test error' });
    actor.send({ type: 'RETRY' });

    const snapshot = actor.getSnapshot();
    expect(snapshot.context.reconnectAttempts).toBe(1);
  });

  it('resets reconnect attempts on successful connection', () => {
    actor.send({ type: 'CONNECT' });
    actor.send({ type: 'ERROR', error: 'Test error' });
    expect(actor.getSnapshot().context.reconnectAttempts).toBeGreaterThan(0);

    actor.send({ type: 'DISCONNECT' });
    actor.send({ type: 'CONNECT' });
    actor.send({ type: 'SSE_CONNECTED' });
    actor.send({ type: 'WS_CONNECTING' });
    actor.send({ type: 'WS_CONNECTED' });

    const snapshot = actor.getSnapshot();
    expect(snapshot.context.reconnectAttempts).toBe(0);
  });

  it('transitions to reconnecting on connection loss from fully_connected', () => {
    actor.send({ type: 'CONNECT' });
    actor.send({ type: 'SSE_CONNECTED' });
    actor.send({ type: 'WS_CONNECTING' });
    actor.send({ type: 'WS_CONNECTED' });
    actor.send({ type: 'RETRY' });

    expect(actor.getSnapshot().value).toBe('reconnecting');
  });

  it('stores connection start time in context', () => {
    const beforeTime = Date.now();
    actor.send({ type: 'CONNECT' });
    const afterTime = Date.now();

    const startTime = actor.getSnapshot().context.connectionStartTime;
    expect(startTime).toBeGreaterThanOrEqual(beforeTime);
    expect(startTime).toBeLessThanOrEqual(afterTime);
  });

  it('stores last connected time on successful connection', () => {
    actor.send({ type: 'CONNECT' });
    actor.send({ type: 'SSE_CONNECTED' });
    actor.send({ type: 'WS_CONNECTING' });
    actor.send({ type: 'WS_CONNECTED' });

    const lastConnected = actor.getSnapshot().context.lastConnectedTime;
    expect(lastConnected).toBeGreaterThan(0);
  });

  it('stores last error message in context', () => {
    const errorMessage = 'Test connection error';
    actor.send({ type: 'CONNECT' });
    actor.send({ type: 'ERROR', error: errorMessage });

    expect(actor.getSnapshot().context.lastError).toBe(errorMessage);
  });

  it('can disconnect from any state', () => {
    actor.send({ type: 'CONNECT' });
    actor.send({ type: 'DISCONNECT' });
    expect(actor.getSnapshot().value).toBe('disconnected');

    actor = createActor(connectionMachine);
    actor.start();
    actor.send({ type: 'CONNECT' });
    actor.send({ type: 'SSE_CONNECTED' });
    actor.send({ type: 'DISCONNECT' });
    expect(actor.getSnapshot().value).toBe('disconnected');

    actor = createActor(connectionMachine);
    actor.start();
    actor.send({ type: 'CONNECT' });
    actor.send({ type: 'SSE_CONNECTED' });
    actor.send({ type: 'WS_CONNECTING' });
    actor.send({ type: 'WS_CONNECTED' });
    actor.send({ type: 'DISCONNECT' });
    expect(actor.getSnapshot().value).toBe('disconnected');
  });
});
