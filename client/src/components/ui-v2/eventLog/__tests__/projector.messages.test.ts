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

  describe('server-assigned message category', () => {
    const commandResponse = (data: Record<string, unknown>): GameEvent => ({
      event_type: 'command_response',
      timestamp: new Date().toISOString(),
      sequence_number: 1,
      data,
    });

    it('command_response keeps the category the server sent', () => {
      const next = projectEvent(
        getInitialGameState(),
        commandResponse({ result: 'You have 3 items.', category: 'command.output' })
      );
      expect(next.messages).toHaveLength(1);
      expect(next.messages[0].category).toBe('command.output');
      expect(next.messages[0].channel).toBe('game');
    });

    it('command_response chat echo takes its channel from data.channel, not from the text', () => {
      // The text deliberately matches no chat pattern: only the server's channel can place it.
      const next = projectEvent(
        getInitialGameState(),
        commandResponse({ result: 'Arkan waves hello', category: 'chat.emote', channel: 'emote' })
      );
      expect(next.messages).toHaveLength(1);
      expect(next.messages[0].category).toBe('chat.emote');
      expect(next.messages[0].channel).toBe('emote');
    });

    it.each([
      ['You say: hello', 'chat.say', 'say'],
      ['You say locally: hello', 'chat.local', 'local'],
      ['You say (global): hello', 'chat.global', 'global'],
      ['You whisper to Bob: psst', 'chat.whisper', 'whisper'],
      ['You system: maintenance', 'chat.admin', 'system'],
    ])('command_response chat echo "%s" lands on channel %s/%s', (result, category, channel) => {
      const next = projectEvent(getInitialGameState(), commandResponse({ result, category, channel }));
      expect(next.messages[0].category).toBe(category);
      expect(next.messages[0].channel).toBe(channel);
    });

    it('command_response ignores data.channel when the category is not a chat category', () => {
      const next = projectEvent(
        getInitialGameState(),
        commandResponse({ result: 'Somewhere dim', category: 'room.description', channel: 'say' })
      );
      expect(next.messages[0].category).toBe('room.description');
      expect(next.messages[0].channel).toBe('game');
    });

    it('command_response without a category behaves as before (legacy text routing)', () => {
      const next = projectEvent(getInitialGameState(), commandResponse({ result: 'You say: hello' }));
      expect(next.messages).toHaveLength(1);
      expect(next.messages[0].category).toBeUndefined();
      expect(next.messages[0].messageType).toBe('chat');
      expect(next.messages[0].channel).toBe('say');
    });

    it('command_response ignores a non-string category', () => {
      const next = projectEvent(getInitialGameState(), commandResponse({ result: 'ok', category: 42 }));
      expect(next.messages[0].category).toBeUndefined();
    });

    it('command_response keeps the category on the suppress_chat game-log message', () => {
      const next = projectEvent(
        getInitialGameState(),
        commandResponse({ result: 'x', suppress_chat: true, game_log_message: 'Logged', category: 'system.info' })
      );
      expect(next.messages).toHaveLength(1);
      expect(next.messages[0].text).toBe('Logged');
      expect(next.messages[0].category).toBe('system.info');
    });

    it('chat_message keeps the category the server sent', () => {
      const event: GameEvent = {
        event_type: 'chat_message',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { message: 'Bob whispers to you: psst', channel: 'whisper', category: 'chat.whisper' },
      };
      const next = projectEvent(getInitialGameState(), event);
      expect(next.messages[0].category).toBe('chat.whisper');
      expect(next.messages[0].channel).toBe('whisper');
      expect(next.messages[0].messageType).toBe('whisper');
    });

    it('chat_message without a category stays uncategorised', () => {
      const event: GameEvent = {
        event_type: 'chat_message',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { message: 'Arkan says: hello', channel: 'say' },
      };
      const next = projectEvent(getInitialGameState(), event);
      expect(next.messages[0].category).toBeUndefined();
    });
  });
});
