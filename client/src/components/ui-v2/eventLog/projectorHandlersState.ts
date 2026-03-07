// State/room/player/combat event handlers for the projector (split from projector.ts for file-nloc)

import type { GameEvent } from '../eventHandlers/types';
import type { Player, QuestLogEntry, Room } from '../types';
import { mergeRoomState } from '../utils/roomMergeUtils';
import type { GameState } from '../utils/stateUpdateUtils';
import { GAME_LOG_CHANNEL, appendMessage, appendMovementMessage, buildChatMessage } from './projectorMessageUtils';
import {
  deriveRoomFromGameState,
  deriveRoomFromRoomOccupants,
  deriveRoomFromRoomState,
  deriveRoomFromRoomUpdate,
} from './projectorRoom';

export type ProjectorHandler = (prevState: GameState, event: GameEvent) => GameState;

export const stateHandlers: Partial<Record<string, ProjectorHandler>> = {
  game_state(prevState, event) {
    const playerData = event.data.player as unknown;
    const room = deriveRoomFromGameState(event);
    const loginGracePeriodActive = event.data.login_grace_period_active as boolean | undefined;
    const loginGracePeriodRemaining = event.data.login_grace_period_remaining as number | undefined;
    const following = event.data.following as { target_name: string; target_type: 'player' | 'npc' } | null | undefined;
    const questLog = event.data.quest_log as unknown[] | undefined;
    const player =
      playerData &&
      typeof playerData === 'object' &&
      playerData !== null &&
      'name' in playerData &&
      typeof (playerData as Player).name === 'string'
        ? (playerData as Player)
        : null;
    return {
      ...prevState,
      player: player ?? prevState.player,
      room: room ?? prevState.room,
      ...(loginGracePeriodActive !== undefined && { loginGracePeriodActive }),
      ...(loginGracePeriodRemaining !== undefined && { loginGracePeriodRemaining }),
      ...(following !== undefined && { followingTarget: following ?? null }),
      ...(Array.isArray(questLog) && { questLog: questLog as QuestLogEntry[] }),
    };
  },

  quest_log_updated(prevState, event) {
    const questLog = event.data.quest_log as unknown[] | undefined;
    return {
      ...prevState,
      ...(Array.isArray(questLog) && { questLog: questLog as QuestLogEntry[] }),
    };
  },

  follow_state(prevState, event) {
    const following = event.data.following as { target_name: string; target_type: 'player' | 'npc' } | null | undefined;
    return { ...prevState, followingTarget: following ?? null };
  },

  effects_update(prevState, event) {
    const loginGracePeriodActive = event.data.login_grace_period_active as boolean | undefined;
    const loginGracePeriodRemaining = event.data.login_grace_period_remaining as number | undefined;
    return {
      ...prevState,
      ...(loginGracePeriodActive !== undefined && { loginGracePeriodActive }),
      ...(loginGracePeriodRemaining !== undefined && { loginGracePeriodRemaining }),
    };
  },

  room_state(prevState, event) {
    const room = deriveRoomFromRoomState(event);
    return room ? { ...prevState, room } : prevState;
  },

  room_update(prevState, event) {
    const room = deriveRoomFromRoomUpdate(event, prevState.room);
    return room ? { ...prevState, room: mergeRoomState(room, prevState.room) } : prevState;
  },

  room_occupants(prevState, event) {
    const roomId = event.room_id as string | undefined;
    const seq = event.sequence_number;
    const lastSeq =
      roomId && prevState.lastRoomOccupantsSequenceByRoom
        ? (prevState.lastRoomOccupantsSequenceByRoom[roomId] ?? 0)
        : 0;
    if (typeof seq === 'number' && seq <= lastSeq) return prevState;
    const room = deriveRoomFromRoomOccupants(event, prevState.room);
    if (!room) return prevState;
    return {
      ...prevState,
      room: mergeRoomState(room, prevState.room),
      lastRoomOccupantsSequenceByRoom:
        roomId != null && typeof seq === 'number'
          ? { ...prevState.lastRoomOccupantsSequenceByRoom, [roomId]: seq }
          : prevState.lastRoomOccupantsSequenceByRoom,
    };
  },

  player_update(prevState, event) {
    const data = event.data as { in_combat?: boolean; stats?: Record<string, unknown> };
    if (!prevState.player) return prevState;
    const mergedStats =
      data.stats && prevState.player.stats
        ? ({ ...prevState.player.stats, ...data.stats } as NonNullable<Player['stats']>)
        : prevState.player.stats;
    const updated: Player = {
      ...prevState.player,
      ...(data.in_combat !== undefined && { in_combat: data.in_combat }),
      ...(mergedStats !== undefined && { stats: mergedStats }),
    };
    return { ...prevState, player: updated };
  },

  combat_started(prevState) {
    if (!prevState.player) return prevState;
    return { ...prevState, player: { ...prevState.player, in_combat: true } };
  },

  combat_ended(prevState, event) {
    let next = prevState;
    if (prevState.player) {
      next = { ...prevState, player: { ...prevState.player, in_combat: false } };
    }
    const reason = event.data.reason as string | undefined;
    if (reason?.trim()) {
      const msg = buildChatMessage(reason.trim(), event.timestamp, {
        messageType: 'system',
        channel: GAME_LOG_CHANNEL,
      });
      next = { ...next, messages: appendMessage(prevState.messages, msg) };
    }
    return next;
  },

  player_died(prevState, event) {
    const deathData = event.data as { current_dp?: number };
    const deathCurrentDp = deathData.current_dp;
    if (!prevState.player?.stats || typeof deathCurrentDp !== 'number' || deathCurrentDp > -10) {
      return prevState;
    }
    return {
      ...prevState,
      player: {
        ...prevState.player,
        stats: {
          ...prevState.player.stats,
          current_dp: deathCurrentDp,
        },
      },
    };
  },
  playerdied(prevState, event) {
    return stateHandlers.player_died!(prevState, event);
  },

  player_respawned(prevState, event) {
    const player = event.data.player as Player | undefined;
    const room = event.data.room as Room | undefined;
    const messageText = typeof event.data.message === 'string' ? event.data.message.trim() : '';
    let next = prevState;
    if (player) next = { ...next, player };
    if (room) next = { ...next, room };
    if (messageText) {
      const msg = buildChatMessage(messageText, event.timestamp, {
        messageType: 'system',
        channel: GAME_LOG_CHANNEL,
      });
      next = { ...next, messages: appendMessage(next.messages, msg) };
    }
    return next;
  },
  playerrespawned(prevState, event) {
    return stateHandlers.player_respawned!(prevState, event);
  },
  player_delirium_respawned(prevState, event) {
    return stateHandlers.player_respawned!(prevState, event);
  },
  playerdeliriumrespawned(prevState, event) {
    return stateHandlers.player_respawned!(prevState, event);
  },

  player_entered_game(prevState, event) {
    const playerName = event.data.player_name as string | undefined;
    if (!playerName || typeof playerName !== 'string' || !playerName.trim()) return prevState;
    const msg = buildChatMessage(`${playerName} has entered the game.`, event.timestamp, {
      messageType: 'system',
      channel: 'game',
    });
    return { ...prevState, messages: appendMessage(prevState.messages, msg) };
  },

  player_entered(prevState, event) {
    const messageText = event.data.message as string | undefined;
    if (!messageText) return prevState;
    const msg = buildChatMessage(messageText, event.timestamp, {
      messageType: 'system',
      channel: 'game',
    });
    return { ...prevState, messages: appendMovementMessage(prevState.messages, msg) };
  },

  player_left_game(prevState, event) {
    const playerName = event.data.player_name as string | undefined;
    if (!playerName) return prevState;
    const msg = buildChatMessage(`${playerName} has left the game.`, event.timestamp, {
      messageType: 'system',
      channel: 'game',
    });
    return { ...prevState, messages: appendMessage(prevState.messages, msg) };
  },

  player_left(prevState, event) {
    const messageText = event.data.message as string | undefined;
    if (!messageText) return prevState;
    const msg = buildChatMessage(messageText, event.timestamp, {
      messageType: 'system',
      channel: 'game',
    });
    return { ...prevState, messages: appendMovementMessage(prevState.messages, msg) };
  },

  player_dp_updated(prevState, event) {
    const data = event.data as {
      new_dp?: number;
      max_dp?: number;
      posture?: string;
      player?: { stats?: { current_dp?: number; max_dp?: number; position?: string } };
    };
    const newDp = data.new_dp ?? data.player?.stats?.current_dp;
    const maxDp = data.max_dp ?? data.player?.stats?.max_dp;
    const position = data.posture ?? data.player?.stats?.position;
    const oldDp = prevState.player?.stats?.current_dp ?? 0;
    if (!prevState.player?.stats || newDp === undefined) return prevState;
    if (oldDp <= -10 && newDp > oldDp) return prevState;
    return {
      ...prevState,
      player: {
        ...prevState.player,
        stats: {
          ...prevState.player.stats,
          current_dp: newDp,
          ...(maxDp !== undefined && { max_dp: maxDp }),
          ...(position !== undefined && { position }),
        },
      },
    };
  },
  playerdpupdated(prevState, event) {
    return stateHandlers.player_dp_updated!(prevState, event);
  },

  lucidity_change(prevState, event) {
    const currentDp = event.data.current_dp as number | undefined;
    if (!prevState.player?.stats || currentDp === undefined) return prevState;
    return {
      ...prevState,
      player: {
        ...prevState.player,
        stats: { ...prevState.player.stats, current_dp: currentDp },
      },
    };
  },
  luciditychange(prevState, event) {
    return stateHandlers.lucidity_change!(prevState, event);
  },

  follow_request(prevState, event) {
    const requestId = typeof event.data.request_id === 'string' ? event.data.request_id : '';
    const requestorName = typeof event.data.requestor_name === 'string' ? event.data.requestor_name : 'Someone';
    if (!requestId) return prevState;
    return {
      ...prevState,
      pendingFollowRequest: { request_id: requestId, requestor_name: requestorName },
    };
  },

  follow_request_cleared(prevState) {
    return { ...prevState, pendingFollowRequest: null };
  },

  party_invite(prevState, event) {
    const inviteId = typeof event.data.invite_id === 'string' ? event.data.invite_id : '';
    const inviterName = typeof event.data.inviter_name === 'string' ? event.data.inviter_name : 'Someone';
    if (!inviteId) return prevState;
    return {
      ...prevState,
      pendingPartyInvite: { invite_id: inviteId, inviter_name: inviterName },
    };
  },

  party_invite_cleared(prevState) {
    return { ...prevState, pendingPartyInvite: null };
  },
};
