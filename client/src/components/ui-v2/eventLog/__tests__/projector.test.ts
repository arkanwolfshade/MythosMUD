/**
 * Unit tests for event-sourced projector: projectEvent and projectState.
 */

import { describe, expect, it, vi } from 'vitest';
import type { GameEvent } from '../../eventHandlers/types';
import type { ChatMessage } from '../../types';
import type { GameState } from '../../utils/stateUpdateUtils';
import { getInitialGameState, projectEvent, projectState } from '../projector';
import type { EventLog } from '../types';

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

describe('projector', () => {
  describe('getInitialGameState', () => {
    it('returns initial state with null player, null room, empty messages', () => {
      const state = getInitialGameState();
      expect(state.player).toBeNull();
      expect(state.room).toBeNull();
      expect(state.messages).toEqual([]);
      expect(state.commandHistory).toEqual([]);
      expect(state.loginGracePeriodActive).toBe(false);
      expect(state.loginGracePeriodRemaining).toBe(0);
      expect(state.mythosTime).toBeNull();
      expect(state.lastQuarterHourForChime).toBeNull();
    });
  });

  describe('projectEvent', () => {
    it('returns prevState unchanged for unknown event type', () => {
      const prev = getInitialGameState();
      const event: GameEvent = {
        event_type: 'unknown_type',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: {},
      };
      const next = projectEvent(prev, event);
      expect(next).toBe(prev);
    });

    it('game_state sets player, room, and grace period', () => {
      const prev = getInitialGameState();
      const event: GameEvent = {
        event_type: 'game_state',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: {
          player: { name: 'TestPlayer', stats: { current_dp: 50, lucidity: 80 } },
          room: {
            id: 'room1',
            name: 'Test Room',
            description: 'A room',
            exits: {},
            players: ['TestPlayer', 'OtherPlayer'],
            npcs: [],
          },
          login_grace_period_active: true,
          login_grace_period_remaining: 60,
        },
      };
      const next = projectEvent(prev, event);
      expect(next.player).not.toBeNull();
      expect(next.player?.name).toBe('TestPlayer');
      expect(next.room).not.toBeNull();
      expect(next.room?.id).toBe('room1');
      expect(next.room?.occupants).toEqual(['TestPlayer', 'OtherPlayer']);
      expect(next.loginGracePeriodActive).toBe(true);
      expect(next.loginGracePeriodRemaining).toBe(60);
    });

    it('room_occupants then room_update preserves occupants (entering-player scenario)', () => {
      const log: EventLog = [
        {
          event_type: 'room_occupants',
          timestamp: new Date().toISOString(),
          sequence_number: 1,
          room_id: 'room1',
          data: { players: ['ArkanWolfshade', 'Ithaqua'], npcs: [], count: 2 },
        },
        {
          event_type: 'room_update',
          timestamp: new Date().toISOString(),
          sequence_number: 2,
          data: {
            room: {
              id: 'room1',
              name: 'Sanitarium Entrance',
              description: 'A grand portico.',
              exits: { south: 'room2', north: 'room3' },
            },
          },
        },
      ];
      const state = projectState(log);
      expect(state.room).not.toBeNull();
      expect(state.room?.id).toBe('room1');
      expect(state.room?.occupants).toContain('ArkanWolfshade');
      expect(state.room?.occupants).toContain('Ithaqua');
      expect(state.room?.occupant_count).toBe(2);
    });

    it('game_state with empty room then room_occupants results in occupants', () => {
      const log: EventLog = [
        {
          event_type: 'game_state',
          timestamp: new Date().toISOString(),
          sequence_number: 1,
          data: {
            player: { name: 'Ithaqua' },
            room: {
              id: 'room1',
              name: 'Sanitarium Entrance',
              description: 'A grand portico.',
              exits: {},
            },
          },
        },
        {
          event_type: 'room_occupants',
          timestamp: new Date().toISOString(),
          sequence_number: 2,
          room_id: 'room1',
          data: { players: ['ArkanWolfshade', 'Ithaqua'], npcs: [], count: 2 },
        },
      ];
      const state = projectState(log);
      expect(state.room?.occupants).toEqual(['ArkanWolfshade', 'Ithaqua']);
      expect(state.room?.occupant_count).toBe(2);
    });

    it('system event appends message', () => {
      const prev = getInitialGameState();
      const event: GameEvent = {
        event_type: 'system',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { message: 'You have disconnected.' },
      };
      const next = projectEvent(prev, event);
      expect(next.messages).toHaveLength(1);
      expect(next.messages[0].text).toBe('You have disconnected.');
    });

    it('combat_started sets player in_combat true', () => {
      const prev = getInitialGameState();
      prev.player = { name: 'Test', in_combat: false };
      const event: GameEvent = {
        event_type: 'combat_started',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: {},
      };
      const next = projectEvent(prev, event);
      expect(next.player?.in_combat).toBe(true);
    });

    it('combat_ended sets player in_combat false', () => {
      const prev = getInitialGameState();
      prev.player = { name: 'Test', in_combat: true };
      const event: GameEvent = {
        event_type: 'combat_ended',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: {},
      };
      const next = projectEvent(prev, event);
      expect(next.player?.in_combat).toBe(false);
    });

    it('game_state with room replaces previous room (server-authoritative, no merge)', () => {
      const prev = getInitialGameState();
      const withRoom: GameState = {
        ...prev,
        room: {
          id: 'room1',
          name: 'Old Name',
          description: 'Old',
          exits: {},
          players: ['OldPlayer'],
          npcs: [],
          occupants: ['OldPlayer'],
          occupant_count: 1,
        },
      };
      const event: GameEvent = {
        event_type: 'game_state',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: {
          player: { name: 'NewPlayer' },
          room: {
            id: 'room1',
            name: 'New Name',
            description: 'New',
            exits: { north: 'room2' },
            players: ['NewPlayer'],
            npcs: [],
            occupants: ['NewPlayer'],
            occupant_count: 1,
          },
          occupants: ['NewPlayer'],
        },
      };
      const next = projectEvent(withRoom, event);
      expect(next.room?.id).toBe('room1');
      expect(next.room?.name).toBe('New Name');
      expect(next.room?.occupants).toEqual(['NewPlayer']);
      expect(next.room?.occupant_count).toBe(1);
    });
  });

  describe('projectState', () => {
    it('returns initial state for empty log', () => {
      const state = projectState([]);
      expect(state).toEqual(getInitialGameState());
    });

    it('player_respawned with player and room updates both player and room in projected state', () => {
      const log: EventLog = [
        {
          event_type: 'game_state',
          timestamp: new Date().toISOString(),
          sequence_number: 1,
          data: {
            player: { name: 'TestPlayer', stats: { current_dp: -10, lucidity: 50 } },
            room: {
              id: 'some_combat_room',
              name: 'Combat Room',
              description: 'Where you died.',
              exits: {},
            },
          },
        },
        {
          event_type: 'player_respawned',
          timestamp: new Date().toISOString(),
          sequence_number: 2,
          data: {
            player: {
              name: 'TestPlayer',
              stats: { current_dp: 27, lucidity: 50 },
            },
            room: {
              id: 'earth_arkhamcity_sanitarium_room_foyer_001',
              name: 'Sanitarium Foyer',
              description: 'You have been restored here.',
              exits: { south: 'other' },
            },
          },
        },
      ];
      const state = projectState(log);
      expect(state.player).not.toBeNull();
      expect(state.player?.stats?.current_dp).toBe(27);
      expect(state.player?.name).toBe('TestPlayer');
      expect(state.room).not.toBeNull();
      expect(state.room?.id).toBe('earth_arkhamcity_sanitarium_room_foyer_001');
      expect(state.room?.name).toBe('Sanitarium Foyer');
    });

    it('room_state is authoritative (replaces room for same id)', () => {
      const log: EventLog = [
        {
          event_type: 'room_occupants',
          timestamp: new Date().toISOString(),
          sequence_number: 1,
          room_id: 'room1',
          data: { players: ['A'], npcs: [], count: 1 },
        },
        {
          event_type: 'room_state',
          timestamp: new Date().toISOString(),
          sequence_number: 2,
          room_id: 'room1',
          data: {
            room: {
              id: 'room1',
              name: 'Sanitarium Entrance',
              description: 'A grand portico.',
              exits: {},
              players: ['ArkanWolfshade', 'Ithaqua'],
              npcs: [],
              occupants: ['ArkanWolfshade', 'Ithaqua'],
              occupant_count: 2,
            },
            occupants: ['ArkanWolfshade', 'Ithaqua'],
            occupant_count: 2,
          },
        },
      ];
      const state = projectState(log);
      expect(state.room?.id).toBe('room1');
      expect(state.room?.occupants).toEqual(['ArkanWolfshade', 'Ithaqua']);
      expect(state.room?.occupant_count).toBe(2);
    });

    it('derives state from single game_state event', () => {
      const log: EventLog = [
        {
          event_type: 'game_state',
          timestamp: new Date().toISOString(),
          sequence_number: 1,
          data: {
            player: { name: 'Player1' },
            room: { id: 'r1', name: 'Room 1', description: 'Desc', exits: {} },
          },
        },
      ];
      const state = projectState(log);
      expect(state.player?.name).toBe('Player1');
      expect(state.room?.id).toBe('r1');
    });

    it('command_response with room_state sets room from response (C3 enter-room request/response)', () => {
      const log = [
        {
          event_type: 'game_state',
          timestamp: new Date().toISOString(),
          sequence_number: 1,
          data: {
            player: { name: 'Player1' },
            room: { id: 'old', name: 'Old Room', description: 'D', exits: {} },
          },
        },
        {
          event_type: 'command_response',
          timestamp: new Date().toISOString(),
          sequence_number: 2,
          data: {
            result: 'You go north.',
            room_state: {
              event_type: 'room_state',
              room_id: 'new_room',
              data: {
                room: {
                  id: 'new_room',
                  name: 'New Room',
                  description: 'A new room.',
                  exits: { south: 'old' },
                  players: ['Player1', 'Other'],
                  npcs: [],
                },
                occupant_count: 2,
              },
            },
          },
        },
      ];
      const state = projectState(log);
      expect(state.room?.id).toBe('new_room');
      expect(state.room?.name).toBe('New Room');
      expect(state.room?.occupants).toEqual(['Player1', 'Other']);
      expect(state.room?.occupant_count).toBe(2);
    });

    it('command_response with full player_update applies all server fields (position, in_combat, stats)', () => {
      const log: EventLog = [
        {
          event_type: 'game_state',
          timestamp: new Date().toISOString(),
          sequence_number: 1,
          data: {
            player: {
              name: 'Player1',
              in_combat: false,
              stats: { current_dp: 100, lucidity: 50, position: 'standing' },
            },
            room: { id: 'r1', name: 'Room 1', description: 'D', exits: {} },
          },
        },
        {
          event_type: 'command_response',
          timestamp: new Date().toISOString(),
          sequence_number: 2,
          data: {
            result: 'You sit down.',
            player_update: {
              position: 'sitting',
              in_combat: true,
              stats: { current_dp: 95 },
            },
          },
        },
      ];
      const state = projectState(log);
      expect(state.player?.stats?.position).toBe('sitting');
      expect(state.player?.in_combat).toBe(true);
      expect(state.player?.stats?.current_dp).toBe(95);
      expect(state.player?.stats?.lucidity).toBe(50);
    });
  });

  describe('game_tick', () => {
    it('sets mythosTime when mythos_clock and mythos_datetime are present', () => {
      const prev = getInitialGameState();
      const event: GameEvent = {
        event_type: 'game_tick',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: {
          tick_number: 10,
          mythos_clock: '14:00 Mythos',
          mythos_datetime: '1920-01-01T14:00:00Z',
          month_name: 'January',
          day_of_month: 1,
          day_name: 'Wednesday',
          week_of_month: 1,
          season: 'winter',
          daypart: 'afternoon',
          is_daytime: true,
          is_witching_hour: false,
        },
      };
      const next = projectEvent(prev, event);
      expect(next.mythosTime).not.toBeNull();
      expect(next.mythosTime?.mythos_clock).toBe('14:00 Mythos');
      expect(next.mythosTime?.daypart).toBe('afternoon');
    });

    it('appends [Tick N] message every 23 ticks', () => {
      const prev = getInitialGameState();
      const event: GameEvent = {
        event_type: 'game_tick',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { tick_number: 23 },
      };
      const next = projectEvent(prev, event);
      expect(next.messages.length).toBe(1);
      expect(next.messages[0].text).toBe('[Tick 23]');
    });

    it('does not append tick message for non-23rd ticks', () => {
      const prev = getInitialGameState();
      const event: GameEvent = {
        event_type: 'game_tick',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { tick_number: 50 },
      };
      const next = projectEvent(prev, event);
      expect(next.messages.length).toBe(0);
    });

    it('appends quarter-hour chime when minute is :00 and lastQuarterHourForChime was null', () => {
      const prev = getInitialGameState();
      const event: GameEvent = {
        event_type: 'game_tick',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: {
          tick_number: 10,
          mythos_clock: '14:00 Mythos',
          mythos_datetime: '1920-01-01T14:00:00Z',
          month_name: 'January',
          day_of_month: 1,
          day_name: 'Wednesday',
          week_of_month: 1,
          season: 'winter',
          daypart: 'afternoon',
          is_daytime: true,
          is_witching_hour: false,
        },
      };
      const next = projectEvent(prev, event);
      const chimeMsg = next.messages.find(m => m.text.includes('The clock chimes'));
      expect(chimeMsg).toBeDefined();
      expect(next.lastQuarterHourForChime).toBe(0);
    });

    it('does not append duplicate quarter-hour chime for same minute', () => {
      const prev = getInitialGameState();
      const event: GameEvent = {
        event_type: 'game_tick',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: {
          tick_number: 10,
          mythos_clock: '14:00 Mythos',
          mythos_datetime: '1920-01-01T14:00:00Z',
          month_name: 'January',
          day_of_month: 1,
          day_name: 'Wednesday',
          week_of_month: 1,
          season: 'winter',
          daypart: 'afternoon',
          is_daytime: true,
          is_witching_hour: false,
        },
      };
      const afterFirst = projectEvent(prev, event);
      const afterSecond = projectEvent(afterFirst, { ...event, data: { ...event.data, tick_number: 20 } });
      const chimeCount = afterSecond.messages.filter(m => m.text.includes('The clock chimes')).length;
      expect(chimeCount).toBe(1);
    });

    it('leaves mythosTime unchanged when mythos_clock or mythos_datetime missing', () => {
      const prev = getInitialGameState();
      const event: GameEvent = {
        event_type: 'game_tick',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { tick_number: 10 },
      };
      const next = projectEvent(prev, event);
      expect(next.mythosTime ?? null).toBeNull();
    });
  });
});
