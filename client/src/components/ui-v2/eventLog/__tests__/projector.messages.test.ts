/**
 * Projector GameInfo message typing and posture projection tests.
 */
/// <reference lib="es2020" />
/// <reference types="vitest/globals" />

import type { GameEvent } from '../../eventHandlers/types';
import type { ChatMessage } from '../../types';
import type { GameState } from '../../utils/stateUpdateUtils';
import { getInitialGameState, projectEvent } from '../projector';

vi.mock('../../utils/messageUtils', () => ({
  sanitizeChatMessageForState: (msg: unknown) => {
    const m = msg as ChatMessage;
    return {
      ...m,
      messageType: m.messageType ?? 'system',
      channel: m.channel ?? 'game',
      type: m.type ?? 'say',
    };
  },
}));

describe('projector messages', () => {
  it('chat_message with channel=system is typed system, not chat (regression, #674)', () => {
    const prev = getInitialGameState();
    const event: GameEvent = {
      event_type: 'chat_message',
      timestamp: new Date().toISOString(),
      sequence_number: 1,
      data: { message: '[SYSTEM] Quest completed: Leave the tutorial', channel: 'system' },
    };
    const next = projectEvent(prev, event);
    expect(next.messages).toHaveLength(1);
    expect(next.messages[0].messageType).toBe('system');
    expect(next.messages[0].channel).toBe('system');
  });

  it('chat_message with channel=say is still typed chat (no regression)', () => {
    const prev = getInitialGameState();
    const event: GameEvent = {
      event_type: 'chat_message',
      timestamp: new Date().toISOString(),
      sequence_number: 1,
      data: { message: 'Arkan says: hello', channel: 'say' },
    };
    const next = projectEvent(prev, event);
    expect(next.messages).toHaveLength(1);
    expect(next.messages[0].messageType).toBe('chat');
  });

  it('player_dp_updated with posture_message appends to GameInfo (issue #395)', () => {
    const prev: GameState = {
      ...getInitialGameState(),
      player: {
        name: 'TestPlayer',
        stats: { current_dp: 10, max_dp: 100, lucidity: 50, position: 'standing' },
      },
    };
    const ts = new Date().toISOString();
    const event: GameEvent = {
      event_type: 'player_dp_updated',
      timestamp: ts,
      sequence_number: 1,
      data: {
        new_dp: 0,
        max_dp: 100,
        posture: 'lying',
        posture_message: 'You stretch out and lie down.',
      },
    };
    const next = projectEvent(prev, event);
    expect(next.messages).toHaveLength(1);
    expect(next.messages[0].text).toBe('You stretch out and lie down.');
    expect(next.player?.stats?.position).toBe('lying');
  });

  it('player_posture_change appends third-person line to GameInfo (issue #395)', () => {
    const prev = getInitialGameState();
    const ts = new Date().toISOString();
    const event: GameEvent = {
      event_type: 'player_posture_change',
      timestamp: ts,
      sequence_number: 1,
      data: {
        message: 'Ada settles into a seated position.',
        player_name: 'Ada',
        position: 'sitting',
      },
    };
    const next = projectEvent(prev, event);
    expect(next.messages).toHaveLength(1);
    expect(next.messages[0].text).toBe('Ada settles into a seated position.');
  });
});
