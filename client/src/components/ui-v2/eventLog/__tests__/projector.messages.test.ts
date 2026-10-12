/**
 * Projector GameInfo message category and posture projection tests.
 */
/// <reference lib="es2020" />
/// <reference types="vitest/globals" />

import type { GameEvent } from '../../eventHandlers/types';
import type { GameState } from '../../utils/stateUpdateUtils';
import { getInitialGameState, projectEvent } from '../projector';

const commandResponse = (data: Record<string, unknown>): GameEvent => ({
  event_type: 'command_response',
  timestamp: new Date().toISOString(),
  sequence_number: 1,
  data,
});

const chatEvent = (data: Record<string, unknown>): GameEvent => ({
  event_type: 'chat_message',
  timestamp: new Date().toISOString(),
  sequence_number: 1,
  data,
});

describe('projector messages', () => {
  it('chat_message with channel=system is a system notice, not chat, and keeps no channel (regression, #674)', () => {
    const next = projectEvent(
      getInitialGameState(),
      chatEvent({ message: '[SYSTEM] Quest completed: Leave the tutorial', channel: 'system', category: 'system.info' })
    );
    expect(next.messages).toHaveLength(1);
    expect(next.messages[0].category).toBe('system.info');
    expect(next.messages[0].channel).toBeUndefined();
  });

  it('chat_message with channel=say keeps its chat category (no regression)', () => {
    const next = projectEvent(
      getInitialGameState(),
      chatEvent({ message: 'Arkan says: hello', channel: 'say', category: 'chat.say' })
    );
    expect(next.messages).toHaveLength(1);
    expect(next.messages[0].category).toBe('chat.say');
  });

  it('player_dp_updated with posture_message appends to GameInfo (issue #395)', () => {
    const prev: GameState = {
      ...getInitialGameState(),
      player: {
        name: 'TestPlayer',
        stats: { current_dp: 10, max_dp: 100, lucidity: 50, position: 'standing' },
      },
    };
    const event: GameEvent = {
      event_type: 'player_dp_updated',
      timestamp: new Date().toISOString(),
      sequence_number: 1,
      data: {
        new_dp: 0,
        max_dp: 100,
        posture: 'lying',
        posture_message: 'You stretch out and lie down.',
        category: 'room.movement',
      },
    };
    const next = projectEvent(prev, event);
    expect(next.messages).toHaveLength(1);
    expect(next.messages[0].text).toBe('You stretch out and lie down.');
    expect(next.messages[0].category).toBe('room.movement');
    expect(next.player?.stats?.position).toBe('lying');
  });

  it('player_dp_decay posture line keeps the server category (status.health), not a hardcoded room.movement', () => {
    const event: GameEvent = {
      event_type: 'player_dp_decay',
      timestamp: new Date().toISOString(),
      sequence_number: 1,
      data: { posture_message: 'Your strength fails and you collapse.', category: 'status.health' },
    };
    const next = projectEvent(getInitialGameState(), event);
    expect(next.messages).toHaveLength(1);
    expect(next.messages[0].category).toBe('status.health');
  });

  it('player_posture_change appends third-person line to GameInfo (issue #395)', () => {
    const event: GameEvent = {
      event_type: 'player_posture_change',
      timestamp: new Date().toISOString(),
      sequence_number: 1,
      data: {
        message: 'Ada settles into a seated position.',
        player_name: 'Ada',
        position: 'sitting',
        category: 'room.movement',
      },
    };
    const next = projectEvent(getInitialGameState(), event);
    expect(next.messages).toHaveLength(1);
    expect(next.messages[0].text).toBe('Ada settles into a seated position.');
    expect(next.messages[0].category).toBe('room.movement');
  });

  describe('server-assigned message category', () => {
    it('command_response keeps the category the server sent', () => {
      const next = projectEvent(
        getInitialGameState(),
        commandResponse({ result: 'You have 3 items.', category: 'command.output' })
      );
      expect(next.messages).toHaveLength(1);
      expect(next.messages[0].category).toBe('command.output');
      expect(next.messages[0].channel).toBeUndefined();
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
      expect(next.messages[0].channel).toBeUndefined();
    });

    it('command_response without a category falls back to command.output', () => {
      const next = projectEvent(getInitialGameState(), commandResponse({ result: 'You say: hello' }));
      expect(next.messages).toHaveLength(1);
      expect(next.messages[0].category).toBe('command.output');
      expect(next.messages[0].channel).toBeUndefined();
    });

    it('command_response with a non-string or unknown category falls back to command.output', () => {
      const numeric = projectEvent(getInitialGameState(), commandResponse({ result: 'ok', category: 42 }));
      expect(numeric.messages[0].category).toBe('command.output');
      const unknown = projectEvent(getInitialGameState(), commandResponse({ result: 'ok', category: 'bogus.kind' }));
      expect(unknown.messages[0].category).toBe('command.output');
    });

    it('command_response whose text is only the room name is not logged when tagged room.name', () => {
      const prev: GameState = {
        ...getInitialGameState(),
        room: { id: 'r1', name: 'Dark Alley', description: '', exits: {} },
      };
      const same = projectEvent(prev, commandResponse({ result: '  Dark Alley ', category: 'room.name' }));
      expect(same.messages).toHaveLength(0);
      const otherName = projectEvent(prev, commandResponse({ result: 'Elsewhere', category: 'room.name' }));
      expect(otherName.messages).toHaveLength(1);
      const sameTextOtherCategory = projectEvent(
        prev,
        commandResponse({ result: 'Dark Alley', category: 'command.output' })
      );
      expect(sameTextOtherCategory.messages).toHaveLength(1);
    });

    it('command_response flagged is_html keeps isHtml so panels render finished markup', () => {
      const next = projectEvent(
        getInitialGameState(),
        commandResponse({ result: '<b>Help</b>', is_html: true, category: 'command.output' })
      );
      expect(next.messages[0].isHtml).toBe(true);
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
      const next = projectEvent(
        getInitialGameState(),
        chatEvent({ message: 'Bob whispers to you: psst', channel: 'whisper', category: 'chat.whisper' })
      );
      expect(next.messages[0].category).toBe('chat.whisper');
      expect(next.messages[0].channel).toBe('whisper');
    });

    it('chat_message without a category falls back to command.output', () => {
      const next = projectEvent(getInitialGameState(), chatEvent({ message: 'Arkan says: hello', channel: 'say' }));
      expect(next.messages[0].category).toBe('command.output');
    });
  });

  describe('room_message movement dedupe', () => {
    const roomMessage = (message: string, category: string, timestamp: string): GameEvent => ({
      event_type: 'room_message',
      timestamp,
      sequence_number: 1,
      data: { message, category },
    });

    it('drops an identical room.movement line within two seconds', () => {
      const first = projectEvent(
        getInitialGameState(),
        roomMessage('Bob arrives.', 'room.movement', '2026-01-01T00:00:00.000Z')
      );
      const second = projectEvent(first, roomMessage('Bob arrives.', 'room.movement', '2026-01-01T00:00:01.500Z'));
      expect(second.messages).toHaveLength(1);
      const later = projectEvent(second, roomMessage('Bob arrives.', 'room.movement', '2026-01-01T00:00:05.000Z'));
      expect(later.messages).toHaveLength(2);
    });

    it('does not dedupe other categories, even with identical text and timing', () => {
      const first = projectEvent(
        getInitialGameState(),
        roomMessage('A chill wind blows.', 'system.info', '2026-01-01T00:00:00.000Z')
      );
      const second = projectEvent(first, roomMessage('A chill wind blows.', 'system.info', '2026-01-01T00:00:01.000Z'));
      expect(second.messages).toHaveLength(2);
    });
  });
});
