import { beforeEach, describe, expect, it, vi } from 'vitest';

import type { ChatMessage } from '../../types';
import type { GameEvent } from '../types';

const hoisted = vi.hoisted(() => ({
  mockHandler: vi.fn(),
  mockWarn: vi.fn(),
  mockInfo: vi.fn(),
  mockError: vi.fn(),
}));

vi.mock('../../../../utils/logger', () => ({
  logger: {
    warn: hoisted.mockWarn,
    info: hoisted.mockInfo,
    error: hoisted.mockError,
  },
}));

vi.mock('../playerHandlers', () => ({
  handlePlayerEnteredGame: hoisted.mockHandler,
  handlePlayerEntered: hoisted.mockHandler,
  handlePlayerLeftGame: hoisted.mockHandler,
  handlePlayerLeft: hoisted.mockHandler,
  handlePlayerDied: hoisted.mockHandler,
  handlePlayerRespawned: hoisted.mockHandler,
  handlePlayerDeliriumRespawned: hoisted.mockHandler,
  handlePlayerDpUpdated: hoisted.mockHandler,
  handlePlayerUpdate: hoisted.mockHandler,
}));

vi.mock('../roomHandlers', () => ({
  handleGameState: hoisted.mockHandler,
  handleFollowState: hoisted.mockHandler,
  handleRoomUpdate: hoisted.mockHandler,
  handleRoomOccupants: hoisted.mockHandler,
}));

vi.mock('../combatHandlers', () => ({
  handleNpcAttacked: hoisted.mockHandler,
  handlePlayerAttacked: hoisted.mockHandler,
  handleCombatStarted: hoisted.mockHandler,
  handleCombatEnded: hoisted.mockHandler,
  handleNpcDied: hoisted.mockHandler,
  handleCombatDeath: hoisted.mockHandler,
  handleCombatTargetSwitch: hoisted.mockHandler,
}));

vi.mock('../messageHandlers', () => ({
  handleCommandResponse: hoisted.mockHandler,
  handleChatMessage: hoisted.mockHandler,
  handleRoomMessage: hoisted.mockHandler,
  handleSystem: hoisted.mockHandler,
}));

vi.mock('../systemHandlers', () => ({
  handleLucidityChange: hoisted.mockHandler,
  handleRescueUpdate: hoisted.mockHandler,
  handleMythosTimeUpdate: hoisted.mockHandler,
  handleIntentionalDisconnect: hoisted.mockHandler,
}));

import { processGameEvent } from '../index';

function buildEvent(type: string): GameEvent {
  return {
    event_type: type,
    sequence_number: 1,
    timestamp: new Date().toISOString(),
    data: {},
  };
}

describe('eventHandlers index', () => {
  const appendMessage = vi.fn<(message: ChatMessage) => void>();
  const context = {} as never;
  const lastProcessedEvent = { current: '' };

  beforeEach(() => {
    vi.clearAllMocks();
    lastProcessedEvent.current = '';
  });

  it('processes known event types via registry', () => {
    hoisted.mockHandler.mockReturnValueOnce({ messages: [] });
    const event = buildEvent('chat_message');

    const updates = processGameEvent(event, context, appendMessage, lastProcessedEvent);

    expect(hoisted.mockHandler).toHaveBeenCalled();
    expect(updates).toEqual({ messages: [] });
  });

  it('ignores unknown event types', () => {
    const updates = processGameEvent(buildEvent('unknown_event'), context, appendMessage, lastProcessedEvent);

    expect(updates).toBeNull();
    expect(hoisted.mockWarn).toHaveBeenCalled();
  });

  it('deduplicates already processed events by key', () => {
    const event = buildEvent('chat_message');
    processGameEvent(event, context, appendMessage, lastProcessedEvent);
    const second = processGameEvent(event, context, appendMessage, lastProcessedEvent);

    expect(second).toBeNull();
  });

  it('returns null and logs when handler throws', () => {
    hoisted.mockHandler.mockImplementationOnce(() => {
      throw new Error('boom');
    });

    const updates = processGameEvent(buildEvent('chat_message'), context, appendMessage, lastProcessedEvent);

    expect(updates).toBeNull();
    expect(hoisted.mockError).toHaveBeenCalled();
  });
});
