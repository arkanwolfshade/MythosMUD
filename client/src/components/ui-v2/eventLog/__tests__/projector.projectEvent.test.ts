/**
 * Unit tests for event-sourced projector: getInitialGameState and projectEvent.
 */
/// <reference lib="es2020" />
/// <reference types="vitest/globals" />

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

    it('trusts the server room_occupants payload even when self is absent (no client injection)', () => {
      // The server's occupant lists always include the connected player (see
      // player_event_handlers_room.py get_room_occupants(ensure_player_included=...)). If a
      // payload genuinely omits self, the client must not paper over it -- that would mask a
      // real server bug. See CLIENT_SERVER_AUTHORITY_REGISTER_2026-09.
      const prev = {
        ...getInitialGameState(),
        player: { name: 'ArkanWolfshade', id: 'p1' },
        room: {
          id: 'room1',
          name: 'Foyer',
          description: '',
          exits: {},
          players: [],
          npcs: [],
          occupants: [],
          occupant_count: 0,
        },
      };
      const next = projectEvent(prev, {
        event_type: 'room_occupants',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        room_id: 'room1',
        data: { players: ['SomeoneElse'], npcs: [], count: 1 },
      });
      expect(next.room?.players).toEqual(['SomeoneElse']);
      expect(next.room?.occupants).toEqual(['SomeoneElse']);
    });

    it('keeps the server occupant_count as-is (no client-side recomputation)', () => {
      const prev = {
        ...getInitialGameState(),
        player: { name: 'ArkanWolfshade', id: 'p1' },
        room: {
          id: 'room1',
          name: 'Foyer',
          description: '',
          exits: {},
          players: ['Ithaqua'],
          npcs: ['Morgan'],
          occupants: ['Ithaqua', 'Morgan'],
          occupant_count: 5,
        },
      };
      const next = projectEvent(prev, {
        event_type: 'chat_message',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { message: 'hello', channel: 'say' },
      });
      expect(next.room?.occupant_count).toBe(5);
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

    it('player_attacked merges target_current_dp into player stats for Character Panel sync', () => {
      const prev = getInitialGameState();
      prev.player = {
        name: 'Hero',
        stats: { current_dp: 100, max_dp: 100, lucidity: 80 },
      };
      const event: GameEvent = {
        event_type: 'player_attacked',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: {
          attacker_name: 'Shoggoth',
          action_type: 'auto_attack',
          damage: 12,
          target_current_dp: 55,
          target_max_dp: 100,
        },
      };
      const next = projectEvent(prev, event);
      expect(next.player?.stats?.current_dp).toBe(55);
      expect(next.player?.stats?.max_dp).toBe(100);
      expect(next.messages).toHaveLength(1);
      expect(next.messages[0].text).toContain('55/100');
    });

    it('npc_took_damage appends spell damage line with NPC current_dp', () => {
      const prev = getInitialGameState();
      const event: GameEvent = {
        event_type: 'npc_took_damage',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: {
          npc_name: 'Nightgaunt',
          damage: 25,
          current_dp: 55,
          max_dp: 80,
        },
      };
      const next = projectEvent(prev, event);
      expect(next.messages).toHaveLength(1);
      expect(next.messages[0].text).toContain('Dealt 25 damage to Nightgaunt');
      expect(next.messages[0].text).toContain('55/80');
    });

    it('combat_target_switch appends room message to messages', () => {
      const prev = getInitialGameState();
      const event: GameEvent = {
        event_type: 'combat_target_switch',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { message: 'The horror turns its gaze to Soandso.' },
      };
      const next = projectEvent(prev, event);
      expect(next.messages).toHaveLength(1);
      expect(next.messages[0].text).toBe('The horror turns its gaze to Soandso.');
      expect(next.messages[0].messageType).toBe('combat');
    });

    it('player_respawned merges onto previous player (#776: thin RespawnPlayerData must not wipe stats)', () => {
      const prev = getInitialGameState();
      prev.player = {
        name: 'ArkanWolfshade',
        id: 'p1',
        profession_id: 3,
        profession_name: 'Antiquarian',
        level: 5,
        experience: 1200,
        stats: {
          current_dp: 10,
          max_dp: 100,
          lucidity: 40,
          strength: 12,
          luck: 15,
          occult: 20,
        },
      };
      const event: GameEvent = {
        event_type: 'player_respawned',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: {
          // Thin RespawnPlayerData shape: id/name/dp/max_dp/current_room_id only.
          player: {
            id: 'p1',
            name: 'ArkanWolfshade',
            stats: { current_dp: 100 },
          },
          room: { id: 'room1', name: 'Main Foyer', description: '', exits: {} },
        },
      };
      const next = projectEvent(prev, event);
      expect(next.player?.profession_id).toBe(3);
      expect(next.player?.profession_name).toBe('Antiquarian');
      expect(next.player?.level).toBe(5);
      expect(next.player?.experience).toBe(1200);
      expect(next.player?.stats?.max_dp).toBe(100);
      expect(next.player?.stats?.lucidity).toBe(40);
      expect(next.player?.stats?.strength).toBe(12);
      expect(next.player?.stats?.luck).toBe(15);
      expect(next.player?.stats?.occult).toBe(20);
      // The incoming field itself still applies.
      expect(next.player?.stats?.current_dp).toBe(100);
    });

    it('player_respawned applies the server room payload as-is (no client-side self injection)', () => {
      // The server's room payload for respawn already includes self (it's built the same way as
      // room_state's occupant list) -- the client trusts it rather than injecting.
      const prev = getInitialGameState();
      prev.player = { name: 'ArkanWolfshade', id: 'p1', stats: { current_dp: 10, lucidity: 40 } };
      const event: GameEvent = {
        event_type: 'player_respawned',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: {
          player: { id: 'p1', name: 'ArkanWolfshade', stats: { current_dp: 100 } },
          room: { id: 'room1', name: 'Main Foyer', description: '', exits: {}, players: ['ArkanWolfshade'] },
        },
      };
      const next = projectEvent(prev, event);
      expect(next.room?.players).toContain('ArkanWolfshade');
    });

    it('player_respawned clears isDead/deathLocation and player_died sets them from the payload', () => {
      const prev = {
        ...getInitialGameState(),
        player: { name: 'ArkanWolfshade', id: 'p1', stats: { current_dp: 10, lucidity: 50 } },
      };
      const died = projectEvent(prev, {
        event_type: 'player_died',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { death_location: 'Main Foyer' },
      });
      expect(died.isDead).toBe(true);
      expect(died.deathLocation).toBe('Main Foyer');

      const respawned = projectEvent(died, {
        event_type: 'player_respawned',
        timestamp: new Date().toISOString(),
        sequence_number: 2,
        data: { player: { id: 'p1', name: 'ArkanWolfshade', stats: { current_dp: 100 } } },
      });
      expect(respawned.isDead).toBe(false);
      expect(respawned.deathLocation).toBeNull();
    });

    it('applies a DP increase after death (no client-side discard)', () => {
      const dead = {
        ...getInitialGameState(),
        isDead: true,
        player: { name: 'ArkanWolfshade', id: 'p1', stats: { current_dp: -10, max_dp: 100, lucidity: 50 } },
      };
      const next = projectEvent(dead, {
        event_type: 'player_dp_updated',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { new_dp: 5 },
      });
      expect(next.player?.stats?.current_dp).toBe(5);
    });

    it('rescue_update(delirium) sets isDelirious and appends the server message', () => {
      const prev = { ...getInitialGameState(), room: { id: 'room1', name: 'Sanitarium', description: '', exits: {} } };
      const next = projectEvent(prev, {
        event_type: 'rescue_update',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { status: 'delirium', message: 'Your mind fractures completely.' },
      });
      expect(next.isDelirious).toBe(true);
      expect(next.deliriumLocation).toBe('Sanitarium');
      expect(next.messages[0].text).toBe('Your mind fractures completely.');
    });

    it('player_delirium_respawned clears isDelirious and applies the server room', () => {
      const prev = { ...getInitialGameState(), isDelirious: true, deliriumLocation: 'Sanitarium' };
      const next = projectEvent(prev, {
        event_type: 'player_delirium_respawned',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: {
          player: { id: 'p1', name: 'ArkanWolfshade', stats: { current_dp: 100 } },
          room: { id: 'room1', name: 'Sanitarium', description: '', exits: {} },
        },
      });
      expect(next.isDelirious).toBe(false);
      expect(next.deliriumLocation).toBeNull();
      expect(next.room?.id).toBe('room1');
    });

    it('lucidity_change reads the real server payload shape and updates lucidityStatus/stats', () => {
      const prev = {
        ...getInitialGameState(),
        player: { name: 'ArkanWolfshade', id: 'p1', stats: { current_dp: 50, lucidity: 60 } },
      };
      const next = projectEvent(prev, {
        event_type: 'lucidity_change',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { current_lcd: 45, max_lcd: 100, delta: -15, tier: 'uneasy' },
      });
      expect(next.lucidityStatus?.current).toBe(45);
      expect(next.lucidityStatus?.tier).toBe('uneasy');
      expect(next.player?.stats?.lucidity).toBe(45);
      // Must never touch current_dp (the old bug read event.data.current_dp, a field lucidity_change never sends).
      expect(next.player?.stats?.current_dp).toBe(50);
    });

    it('game_state seeds lucidityStatus from lucidity_tier/current_lcd', () => {
      const next = projectEvent(getInitialGameState(), {
        event_type: 'game_state',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: {
          player: { name: 'ArkanWolfshade', stats: {} },
          lucidity_tier: 'fractured',
          current_lcd: -5,
        },
      });
      expect(next.lucidityStatus?.tier).toBe('fractured');
      expect(next.lucidityStatus?.current).toBe(-5);
    });

    it('mythos_time_update sets mythosTime', () => {
      const next = projectEvent(getInitialGameState(), {
        event_type: 'mythos_time_update',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: {
          mythos_datetime: '1928-09-23T14:00:00Z',
          mythos_clock: '14:00 Mythos',
          month_name: 'September',
          day_of_month: 23,
          day_name: 'Sunday',
          week_of_month: 4,
          season: 'Autumn',
          daypart: 'afternoon',
          is_daytime: true,
          is_witching_hour: false,
        },
      });
      expect(next.mythosTime?.daypart).toBe('afternoon');
    });

    it('mythos_time_update appends a daypart-change message when the daypart differs from before', () => {
      const withDaypart = projectEvent(getInitialGameState(), {
        event_type: 'mythos_time_update',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: {
          mythos_datetime: '1928-09-23T10:00:00Z',
          mythos_clock: '10:00 Mythos',
          month_name: 'September',
          day_of_month: 23,
          day_name: 'Sunday',
          week_of_month: 4,
          season: 'Autumn',
          daypart: 'morning',
          is_daytime: true,
          is_witching_hour: false,
        },
      });
      const next = projectEvent(withDaypart, {
        event_type: 'mythos_time_update',
        timestamp: new Date().toISOString(),
        sequence_number: 2,
        data: {
          mythos_datetime: '1928-09-23T14:00:00Z',
          mythos_clock: '14:00 Mythos',
          month_name: 'September',
          day_of_month: 23,
          day_name: 'Sunday',
          week_of_month: 4,
          season: 'Autumn',
          daypart: 'afternoon',
          is_daytime: true,
          is_witching_hour: false,
        },
      });
      expect(next.messages.some(m => m.text.includes('afternoon watch') || m.text.startsWith('[Time]'))).toBe(true);
    });

    it('a room ID change on room_update keeps the payload occupants instead of zeroing', () => {
      const prev = {
        ...getInitialGameState(),
        room: {
          id: 'room1',
          name: 'Old Room',
          description: '',
          exits: {},
          players: ['ArkanWolfshade'],
          npcs: [],
          occupants: ['ArkanWolfshade'],
          occupant_count: 1,
        },
      };
      const next = projectEvent(prev, {
        event_type: 'room_update',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: {
          room: {
            id: 'room2',
            name: 'New Room',
            description: '',
            exits: {},
            players: ['ArkanWolfshade'],
            npcs: [],
          },
        },
      });
      expect(next.room?.id).toBe('room2');
      expect(next.room?.players).toEqual(['ArkanWolfshade']);
    });

    it('client_message survives a later replay and client_messages_cleared empties the log', () => {
      const withMessage = projectEvent(getInitialGameState(), {
        event_type: 'client_message',
        timestamp: new Date().toISOString(),
        sequence_number: 0,
        data: { text: 'Connection lost.', messageType: 'system' },
      });
      expect(withMessage.messages).toHaveLength(1);

      const cleared = projectEvent(withMessage, {
        event_type: 'client_messages_cleared',
        timestamp: new Date().toISOString(),
        sequence_number: 0,
        data: {},
      });
      expect(cleared.messages).toHaveLength(0);
    });

    it('player_respawned does not clobber lucidity with an omitted/null value', () => {
      const prev = getInitialGameState();
      prev.player = { name: 'ArkanWolfshade', id: 'p1', stats: { current_dp: 10, lucidity: 40 } };
      const event: GameEvent = {
        event_type: 'player_respawned',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: {
          // Death respawn payload: no lucidity field at all.
          player: { id: 'p1', name: 'ArkanWolfshade', stats: { current_dp: 100 } },
          room: { id: 'room1', name: 'Main Foyer', description: '', exits: {} },
        },
      };
      const next = projectEvent(prev, event);
      expect(next.player?.stats?.lucidity).toBe(40);
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
});
