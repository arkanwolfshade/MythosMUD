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

    it('injects connected self into empty room.players after room_occupants', () => {
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
        data: { players: [], npcs: [], count: 0 },
      });
      expect(next.room?.players).toContain('ArkanWolfshade');
      expect(next.room?.occupants).toContain('ArkanWolfshade');
    });

    it('preserves server occupant_count when injecting self into room.players', () => {
      // Server count can exceed visible players/NPCs (hidden occupants, other entities).
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
      expect(next.room?.players).toContain('ArkanWolfshade');
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

    it('follow_request_cleared clears pendingFollowRequest when projected', () => {
      const prev = getInitialGameState();
      const withFollow: GameState = {
        ...prev,
        pendingFollowRequest: { request_id: 'r1', requestor_name: 'Alice' },
      };
      const event: GameEvent = {
        event_type: 'follow_request_cleared',
        timestamp: new Date().toISOString(),
        sequence_number: 1,
        data: { request_id: 'r1' },
      };
      const next = projectEvent(withFollow, event);
      expect(next.pendingFollowRequest).toBeNull();
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
