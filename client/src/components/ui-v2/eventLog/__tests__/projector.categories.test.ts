/**
 * Message categories on room/system events (server-tagged) and client-authored text (fixed per event type).
 */
/// <reference lib="es2020" />
/// <reference types="vitest/globals" />

import type { GameEvent } from '../../eventHandlers/types';
import type { GameState } from '../../utils/stateUpdateUtils';
import { getInitialGameState, projectEvent } from '../projector';
import { buildLocalMessageEvent } from '../projectorMessageUtils';

const TS = '2026-10-11T12:00:00.000Z';

function ev(event_type: string, data: Record<string, unknown>, timestamp = TS): GameEvent {
  return { event_type, timestamp, sequence_number: 1, data };
}

function categories(state: GameState): (string | undefined)[] {
  return state.messages.map(m => m.category);
}

describe('server-tagged room and system events', () => {
  it('room_message passes data.category through', () => {
    const next = projectEvent(
      getInitialGameState(),
      ev('room_message', { message: 'Rat left north.', message_type: 'system', category: 'room.movement' })
    );
    expect(categories(next)).toEqual(['room.movement']);
  });

  it('room_message without a category still renders (legacy path)', () => {
    const next = projectEvent(getInitialGameState(), ev('room_message', { message: 'A rat scurries in.' }));
    expect(next.messages).toHaveLength(1);
    expect(next.messages[0].category).toBeUndefined();
  });

  it('keeps the 2 s duplicate filter for room.movement without the legacy system message_type', () => {
    const event = (timestamp: string) =>
      ev('room_message', { message: 'A rat scurries in.', category: 'room.movement' }, timestamp);
    let state = projectEvent(getInitialGameState(), event('2026-10-11T12:00:00.000Z'));
    state = projectEvent(state, event('2026-10-11T12:00:01.000Z'));
    expect(state.messages).toHaveLength(1);
    state = projectEvent(state, event('2026-10-11T12:00:05.000Z'));
    expect(state.messages).toHaveLength(2);
  });

  it('does not dedupe non-movement room messages', () => {
    const event = (timestamp: string) => ev('room_message', { message: 'The wind howls.' }, timestamp);
    let state = projectEvent(getInitialGameState(), event('2026-10-11T12:00:00.000Z'));
    state = projectEvent(state, event('2026-10-11T12:00:01.000Z'));
    expect(state.messages).toHaveLength(2);
  });

  it('system passes data.category through', () => {
    const next = projectEvent(
      getInitialGameState(),
      ev('system', { message: 'Careful.', message_type: 'warning', category: 'system.warning' })
    );
    expect(categories(next)).toEqual(['system.warning']);
  });

  it('player_entered / player_left use the server category', () => {
    let state = projectEvent(
      getInitialGameState(),
      ev('player_entered', { message: 'Ada enters the room.', category: 'room.movement' })
    );
    state = projectEvent(state, ev('player_left', { message: 'Ada leaves the room.', category: 'room.movement' }));
    expect(categories(state)).toEqual(['room.movement', 'room.movement']);
  });

  it('player_posture_change uses the server category', () => {
    const next = projectEvent(
      getInitialGameState(),
      ev('player_posture_change', { message: 'Ada settles into a seated position.', category: 'room.movement' })
    );
    expect(categories(next)).toEqual(['room.movement']);
  });
});

describe('client-authored messages get a fixed category per event type', () => {
  it.each([
    ['error', 'system.error'],
    ['warning', 'system.warning'],
    ['system', 'system.info'],
    ['info', 'system.info'],
  ])('client_message with messageType %s -> %s', (messageType, expected) => {
    const next = projectEvent(getInitialGameState(), buildLocalMessageEvent('Something happened.', messageType));
    expect(categories(next)).toEqual([expected]);
  });

  it('buildLocalMessageEvent default (system) is system.info', () => {
    const next = projectEvent(getInitialGameState(), buildLocalMessageEvent('Connection to server lost.'));
    expect(categories(next)).toEqual(['system.info']);
  });

  it('player_entered_game / player_left_game -> room.movement', () => {
    let state = projectEvent(getInitialGameState(), ev('player_entered_game', { player_name: 'Ada' }));
    state = projectEvent(state, ev('player_left_game', { player_name: 'Ada' }));
    expect(categories(state)).toEqual(['room.movement', 'room.movement']);
  });

  it('player_respawned message -> system.info', () => {
    const next = projectEvent(getInitialGameState(), ev('player_respawned', { message: 'You awaken.' }));
    expect(categories(next)).toEqual(['system.info']);
  });

  it('game_tick tick line and quarter-hour chime -> system.info', () => {
    const next = projectEvent(
      getInitialGameState(),
      ev('game_tick', {
        tick_number: 23,
        mythos_clock: '10:00',
        mythos_datetime: '1930-01-01T10:00:00.000Z',
      })
    );
    expect(next.messages.map(m => m.text)).toEqual(['[Time] The clock chimes 10:00 AM Mythos', '[Tick 23]']);
    expect(categories(next)).toEqual(['system.info', 'system.info']);
  });

  it('mythos_time_update daypart and holiday lines -> system.info', () => {
    const base = {
      mythos_clock: '06:00',
      mythos_datetime: '1930-01-01T06:00:00.000Z',
      daypart: 'morning',
      active_holidays: [] as { id: string; name: string }[],
    };
    let state = projectEvent(getInitialGameState(), ev('mythos_time_update', { ...base, daypart: 'pre-dawn' }));
    state = projectEvent(
      state,
      ev('mythos_time_update', { ...base, active_holidays: [{ id: 'h1', name: 'Samhain' }] })
    );
    state = projectEvent(state, ev('mythos_time_update', { ...base, daypart: 'morning' }));
    expect(state.messages.length).toBeGreaterThanOrEqual(2);
    expect(new Set(categories(state))).toEqual(new Set(['system.info']));
  });
});
