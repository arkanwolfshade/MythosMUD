// Event-sourced GameState projector: derives state from event log (pure, no refs)
// As documented in "Event Processing Architecture" - Dr. Armitage, 1928

import type { MythosTimePayload } from '../../../types/mythosTime';
import { logger } from '../../../utils/logger';
import { determineMessageType } from '../../../utils/messageTypeUtils';
import { buildMythosTimeState, formatMythosTime12Hour } from '../../../utils/mythosTime';
import type { GameEvent } from '../eventHandlers/types';
import type { ChatMessage, Player, Room } from '../types';
import { sanitizeChatMessageForState } from '../utils/messageUtils';
import { mergeRoomState } from '../utils/roomMergeUtils';
import type { GameState } from '../utils/stateUpdateUtils';
import {
  deriveRoomFromGameState,
  deriveRoomFromRoomOccupants,
  deriveRoomFromRoomState,
  deriveRoomFromRoomUpdate,
} from './projectorRoom';
import type { EventLog } from './types';

const GAME_LOG_CHANNEL = 'game-log';

function buildChatMessage(
  text: string,
  timestamp: string,
  opts: { isHtml?: boolean; messageType?: string; channel?: string } = {}
): ChatMessage {
  const messageType = opts.messageType ?? 'system';
  const channel = opts.channel ?? 'game';
  const type =
    channel === 'whisper' ? 'whisper' : channel === 'shout' ? 'shout' : channel === 'emote' ? 'emote' : 'say';
  return {
    text,
    timestamp,
    isHtml: opts.isHtml ?? false,
    messageType,
    channel,
    type,
  };
}

function appendMessage(prevMessages: ChatMessage[], message: ChatMessage): ChatMessage[] {
  return [...prevMessages, sanitizeChatMessageForState(message)];
}

/** Dedupe window (ms): same movement text within this window is treated as duplicate. */
const MOVEMENT_DEDUPE_MS = 2000;

function appendMovementMessage(prevMessages: ChatMessage[], message: ChatMessage): ChatMessage[] {
  const sanitized = sanitizeChatMessageForState(message);
  const last = prevMessages[prevMessages.length - 1];
  if (last.text === sanitized.text) {
    const lastTs = new Date(last.timestamp).getTime();
    const newTs = new Date(sanitized.timestamp).getTime();
    if (Math.abs(newTs - lastTs) <= MOVEMENT_DEDUPE_MS) {
      return prevMessages;
    }
  }
  return [...prevMessages, sanitized];
}

/** Initial GameState before any events */
export function getInitialGameState(): GameState {
  return {
    player: null,
    room: null,
    messages: [],
    commandHistory: [],
    loginGracePeriodActive: false,
    loginGracePeriodRemaining: 0,
    mythosTime: null,
    lastQuarterHourForChime: null,
  };
}

/** Known event types that affect state (allowlist for projector) */
const PROJECTED_EVENT_TYPES = new Set([
  'game_state',
  'effects_update',
  'room_update',
  'room_state',
  'room_occupants',
  'player_entered_game',
  'player_entered',
  'player_left_game',
  'player_left',
  'player_died',
  'playerdied',
  'player_respawned',
  'playerrespawned',
  'player_delirium_respawned',
  'playerdeliriumrespawned',
  'player_dp_updated',
  'playerdpupdated',
  'player_update',
  'command_response',
  'chat_message',
  'room_message',
  'system',
  'npc_attacked',
  'player_attacked',
  'combat_started',
  'combat_ended',
  'npc_died',
  'combat_death',
  'lucidity_change',
  'luciditychange',
  'intentional_disconnect',
  'game_tick',
  'follow_request',
  'follow_state',
]);

/**
 * Project a single event onto previous state. Pure function; no refs or side effects.
 */
export function projectEvent(prevState: GameState, event: GameEvent): GameState {
  const eventType = (event.event_type ?? '').toString().trim().toLowerCase();
  if (!PROJECTED_EVENT_TYPES.has(eventType)) {
    return prevState;
  }

  let nextState = prevState;

  switch (eventType) {
    case 'game_state': {
      const playerData = event.data.player as unknown;
      const room = deriveRoomFromGameState(event);
      const loginGracePeriodActive = event.data.login_grace_period_active as boolean | undefined;
      const loginGracePeriodRemaining = event.data.login_grace_period_remaining as number | undefined;
      const following = event.data.following as
        | { target_name: string; target_type: 'player' | 'npc' }
        | null
        | undefined;
      const player =
        playerData &&
        typeof playerData === 'object' &&
        playerData !== null &&
        'name' in playerData &&
        typeof (playerData as Player).name === 'string'
          ? (playerData as Player)
          : null;
      nextState = {
        ...prevState,
        player: player ?? prevState.player,
        room: room ? mergeRoomState(room, prevState.room) : prevState.room,
        ...(loginGracePeriodActive !== undefined && { loginGracePeriodActive }),
        ...(loginGracePeriodRemaining !== undefined && { loginGracePeriodRemaining }),
        ...(following !== undefined && { followingTarget: following ?? null }),
      };
      break;
    }
    case 'follow_state': {
      const following = event.data.following as
        | { target_name: string; target_type: 'player' | 'npc' }
        | null
        | undefined;
      nextState = {
        ...prevState,
        followingTarget: following ?? null,
      };
      break;
    }
    case 'effects_update': {
      const loginGracePeriodActive = event.data.login_grace_period_active as boolean | undefined;
      const loginGracePeriodRemaining = event.data.login_grace_period_remaining as number | undefined;
      nextState = {
        ...prevState,
        ...(loginGracePeriodActive !== undefined && { loginGracePeriodActive }),
        ...(loginGracePeriodRemaining !== undefined && { loginGracePeriodRemaining }),
      };
      break;
    }
    case 'room_state': {
      // Authoritative: replace room for this room_id (do not merge with room_update/room_occupants)
      const room = deriveRoomFromRoomState(event);
      if (room) {
        nextState = { ...prevState, room };
      }
      break;
    }
    case 'room_update': {
      const room = deriveRoomFromRoomUpdate(event, prevState.room);
      if (room) {
        nextState = {
          ...prevState,
          room: mergeRoomState(room, prevState.room),
        };
      }
      break;
    }
    case 'room_occupants': {
      const roomId = event.room_id as string | undefined;
      const seq = event.sequence_number;
      const lastSeq =
        roomId && prevState.lastRoomOccupantsSequenceByRoom
          ? (prevState.lastRoomOccupantsSequenceByRoom[roomId] ?? 0)
          : 0;
      if (typeof seq === 'number' && seq <= lastSeq) {
        break;
      }
      const room = deriveRoomFromRoomOccupants(event, prevState.room);
      if (room) {
        nextState = {
          ...prevState,
          room: mergeRoomState(room, prevState.room),
          lastRoomOccupantsSequenceByRoom:
            roomId != null && typeof seq === 'number'
              ? { ...prevState.lastRoomOccupantsSequenceByRoom, [roomId]: seq }
              : prevState.lastRoomOccupantsSequenceByRoom,
        };
      }
      break;
    }
    case 'player_update': {
      const data = event.data as { in_combat?: boolean; stats?: Record<string, unknown> };
      if (prevState.player) {
        const mergedStats =
          data.stats && prevState.player.stats
            ? ({ ...prevState.player.stats, ...data.stats } as NonNullable<Player['stats']>)
            : prevState.player.stats;
        const updated: Player = {
          ...prevState.player,
          ...(data.in_combat !== undefined && { in_combat: data.in_combat }),
          ...(mergedStats !== undefined && { stats: mergedStats }),
        };
        nextState = { ...prevState, player: updated };
      }
      break;
    }
    case 'combat_started':
      if (prevState.player) {
        nextState = { ...prevState, player: { ...prevState.player, in_combat: true } };
      }
      break;
    case 'combat_ended':
      if (prevState.player) {
        nextState = { ...prevState, player: { ...prevState.player, in_combat: false } };
      }
      break;
    case 'player_respawned':
    case 'playerrespawned':
    case 'player_delirium_respawned':
    case 'playerdeliriumrespawned': {
      const player = event.data.player as Player | undefined;
      const room = event.data.room as Room | undefined;
      if (player) {
        nextState = { ...prevState, player };
      }
      if (room) {
        nextState = { ...nextState, room };
      }
      break;
    }
    case 'player_entered_game': {
      const playerName = event.data.player_name as string | undefined;
      if (playerName && typeof playerName === 'string' && playerName.trim()) {
        const msg = buildChatMessage(`${playerName} has entered the game.`, event.timestamp, {
          messageType: 'system',
          channel: 'game',
        });
        nextState = { ...prevState, messages: appendMessage(prevState.messages, msg) };
      }
      break;
    }
    case 'player_entered': {
      const messageText = event.data.message as string | undefined;
      if (messageText) {
        const msg = buildChatMessage(messageText, event.timestamp, {
          messageType: 'system',
          channel: 'game',
        });
        nextState = { ...prevState, messages: appendMovementMessage(prevState.messages, msg) };
      }
      break;
    }
    case 'player_left_game': {
      const playerName = event.data.player_name as string | undefined;
      if (playerName) {
        const msg = buildChatMessage(`${playerName} has left the game.`, event.timestamp, {
          messageType: 'system',
          channel: 'game',
        });
        nextState = { ...prevState, messages: appendMessage(prevState.messages, msg) };
      }
      break;
    }
    case 'player_left': {
      const messageText = event.data.message as string | undefined;
      if (messageText) {
        const msg = buildChatMessage(messageText, event.timestamp, {
          messageType: 'system',
          channel: 'game',
        });
        nextState = { ...prevState, messages: appendMovementMessage(prevState.messages, msg) };
      }
      break;
    }
    case 'command_response': {
      const suppressChat = Boolean(event.data.suppress_chat);
      const message = typeof event.data.result === 'string' ? (event.data.result as string) : '';
      const isHtml = Boolean(event.data.is_html);
      const gameLogMessage =
        (typeof event.data.game_log_message === 'string' && (event.data.game_log_message as string).length > 0
          ? (event.data.game_log_message as string)
          : undefined) || message;
      const gameLogChannel =
        typeof event.data.game_log_channel === 'string' && event.data.game_log_channel
          ? (event.data.game_log_channel as string)
          : GAME_LOG_CHANNEL;
      const isRoomNameOnly =
        prevState.room &&
        message &&
        message.trim().length > 0 &&
        message.trim().length < 100 &&
        !message.includes('\n') &&
        !message.includes('Exits:') &&
        !message.includes('Description:') &&
        message.trim() === prevState.room.name;
      if (!suppressChat && message && !isRoomNameOnly) {
        const messageTypeResult = determineMessageType(message);
        const msg = buildChatMessage(message, event.timestamp, {
          isHtml,
          messageType: messageTypeResult.type,
          channel: messageTypeResult.channel ?? 'game',
        });
        nextState = { ...prevState, messages: appendMessage(prevState.messages, msg) };
      } else if (gameLogMessage && !isRoomNameOnly) {
        const msg = buildChatMessage(gameLogMessage, event.timestamp, {
          isHtml,
          messageType: 'system',
          channel: gameLogChannel,
        });
        nextState = { ...prevState, messages: appendMessage(prevState.messages, msg) };
      }
      // C3 enter-room request/response: set room from response so we do not rely on push event ordering
      const roomStatePayload = event.data.room_state as GameEvent | undefined;
      if (roomStatePayload && roomStatePayload.data?.room) {
        const room = deriveRoomFromRoomState(roomStatePayload);
        if (room) {
          nextState = { ...nextState, room };
        }
      }
      // Apply player_update from command response (e.g. position from /sit, /stand, /lie) so Character panel updates
      const playerUpdatePayload = (event.data as { player_update?: { position?: string } }).player_update;
      if (playerUpdatePayload?.position && nextState.player?.stats) {
        nextState = {
          ...nextState,
          player: {
            ...nextState.player,
            stats: { ...nextState.player.stats, position: playerUpdatePayload.position },
          },
        };
      }
      break;
    }
    case 'chat_message': {
      const message = event.data.message as string | undefined;
      const channel = event.data.channel as string | undefined;
      if (message && channel) {
        const messageType =
          channel === 'whisper' ? 'whisper' : channel === 'shout' ? 'shout' : channel === 'emote' ? 'emote' : 'chat';
        const msg = buildChatMessage(message, event.timestamp, {
          messageType,
          channel,
        });
        nextState = { ...prevState, messages: appendMessage(prevState.messages, msg) };
      }
      break;
    }
    case 'room_message': {
      const message = typeof event.data.message === 'string' ? (event.data.message as string) : '';
      const messageTypeFromEvent =
        typeof event.data.message_type === 'string' ? (event.data.message_type as string) : undefined;
      const isHtml = Boolean(event.data.is_html);
      if (message) {
        const messageType = messageTypeFromEvent === 'system' ? 'system' : determineMessageType(message).type;
        const channel =
          messageTypeFromEvent === 'system' ? GAME_LOG_CHANNEL : (determineMessageType(message).channel ?? 'game');
        const msg = buildChatMessage(message, event.timestamp, {
          isHtml,
          messageType,
          channel,
        });
        nextState = {
          ...prevState,
          messages:
            messageTypeFromEvent === 'system'
              ? appendMovementMessage(prevState.messages, msg)
              : appendMessage(prevState.messages, msg),
        };
      }
      break;
    }
    case 'system': {
      const systemMessage = event.data.message;
      if (systemMessage && typeof systemMessage === 'string') {
        const msg = buildChatMessage(systemMessage, event.timestamp, {
          messageType: 'system',
          channel: 'game',
        });
        nextState = { ...prevState, messages: appendMessage(prevState.messages, msg) };
      }
      break;
    }
    case 'npc_attacked': {
      const attackerName = (event.data.attacker_name || event.data.npc_name) as string | undefined;
      const damage = event.data.damage as number | undefined;
      const actionType = event.data.action_type as string | undefined;
      const targetCurrentDp = event.data.target_current_dp as number | undefined;
      const targetMaxDp = event.data.target_max_dp as number | undefined;
      if (attackerName && damage !== undefined) {
        let text = `${attackerName} ${actionType || 'attacks'} you for ${damage} damage.`;
        if (targetCurrentDp !== undefined && targetMaxDp !== undefined) {
          text += ` (${targetCurrentDp}/${targetMaxDp} DP)`;
        }
        const msg = buildChatMessage(text, event.timestamp, {
          messageType: 'system',
          channel: GAME_LOG_CHANNEL,
        });
        nextState = { ...prevState, messages: appendMessage(prevState.messages, msg) };
        logger.info('projector', 'Combat message appended (npc_attacked)', {
          event_type: 'npc_attacked',
          text_preview: text.slice(0, 80),
        });
      }
      break;
    }
    case 'player_attacked': {
      const attackerName = event.data.attacker_name as string | undefined;
      const targetName = event.data.target_name as string | undefined;
      const damage = event.data.damage as number | undefined;
      const actionType = event.data.action_type as string | undefined;
      const targetCurrentDp = event.data.target_current_dp as number | undefined;
      const targetMaxDp = event.data.target_max_dp as number | undefined;
      if (attackerName && targetName && damage !== undefined) {
        let text = `You ${actionType || 'attack'} ${targetName} for ${damage} damage.`;
        if (targetCurrentDp !== undefined && targetMaxDp !== undefined) {
          text += ` (${targetCurrentDp}/${targetMaxDp} DP)`;
        }
        const msg = buildChatMessage(text, event.timestamp, {
          messageType: 'system',
          channel: GAME_LOG_CHANNEL,
        });
        nextState = { ...prevState, messages: appendMessage(prevState.messages, msg) };
        logger.info('projector', 'Combat message appended (player_attacked)', {
          event_type: 'player_attacked',
          text_preview: text.slice(0, 80),
        });
      }
      break;
    }
    case 'npc_died':
    case 'combat_death': {
      const message = event.data.message as string | undefined;
      if (message) {
        const msg = buildChatMessage(message, event.timestamp, {
          messageType: 'system',
          channel: GAME_LOG_CHANNEL,
        });
        nextState = { ...prevState, messages: appendMessage(prevState.messages, msg) };
      }
      break;
    }
    case 'player_dp_updated':
    case 'playerdpupdated': {
      const data = event.data as {
        new_dp?: number;
        max_dp?: number;
        player?: { stats?: { current_dp?: number; max_dp?: number } };
      };
      const newDp = data.new_dp ?? data.player?.stats?.current_dp;
      const maxDp = data.max_dp ?? data.player?.stats?.max_dp;
      if (prevState.player && prevState.player.stats && newDp !== undefined) {
        nextState = {
          ...prevState,
          player: {
            ...prevState.player,
            stats: {
              ...prevState.player.stats,
              current_dp: newDp,
              ...(maxDp !== undefined && { max_dp: maxDp }),
            },
          },
        };
      }
      break;
    }
    case 'lucidity_change':
    case 'luciditychange': {
      const currentDp = event.data.current_dp as number | undefined;
      if (prevState.player && prevState.player.stats && currentDp !== undefined) {
        nextState = {
          ...prevState,
          player: {
            ...prevState.player,
            stats: { ...prevState.player.stats, current_dp: currentDp },
          },
        };
      }
      break;
    }
    case 'intentional_disconnect': {
      const message = (event.data as { message?: string }).message || 'You have disconnected from the game.';
      const msg = buildChatMessage(message, event.timestamp, {
        messageType: 'system',
        channel: 'game',
      });
      nextState = { ...prevState, messages: appendMessage(prevState.messages, msg) };
      break;
    }
    case 'game_tick': {
      const data = event.data as Record<string, unknown>;
      const tickNumber = typeof data.tick_number === 'number' ? data.tick_number : 0;

      if (data.mythos_clock && data.mythos_datetime) {
        const mythosPayload: MythosTimePayload = {
          mythos_datetime: data.mythos_datetime as string,
          mythos_clock: data.mythos_clock as string,
          month_name: (data.month_name as string) || '',
          day_of_month: (data.day_of_month as number) || 1,
          day_name: (data.day_name as string) || '',
          week_of_month: (data.week_of_month as number) || 1,
          season: (data.season as string) || '',
          daypart: (data.daypart as string) || '',
          is_daytime: typeof data.is_daytime === 'boolean' ? data.is_daytime : true,
          is_witching_hour: typeof data.is_witching_hour === 'boolean' ? data.is_witching_hour : false,
          server_timestamp: (data.timestamp as string) || event.timestamp,
          active_holidays: Array.isArray(data.active_holidays)
            ? (data.active_holidays as MythosTimePayload['active_holidays'])
            : [],
          upcoming_holidays: Array.isArray(data.upcoming_holidays)
            ? (data.upcoming_holidays as MythosTimePayload['upcoming_holidays'])
            : [],
          active_schedules: Array.isArray(data.active_schedules)
            ? (data.active_schedules as MythosTimePayload['active_schedules'])
            : undefined,
        };
        const mythosState = buildMythosTimeState(mythosPayload);
        nextState = { ...nextState, mythosTime: mythosState };

        try {
          const mythosDate = new Date(mythosPayload.mythos_datetime);
          const currentMinute = mythosDate.getUTCMinutes();
          const isQuarterHour = currentMinute % 15 === 0;
          const lastQuarter = prevState.lastQuarterHourForChime ?? null;

          if (isQuarterHour && lastQuarter !== currentMinute) {
            const formattedClock = formatMythosTime12Hour(mythosPayload.mythos_clock);
            const chimeMsg = buildChatMessage(`[Time] The clock chimes ${formattedClock} Mythos`, event.timestamp, {
              messageType: 'system',
              channel: 'system',
            });
            nextState = {
              ...nextState,
              messages: appendMessage(nextState.messages, chimeMsg),
              lastQuarterHourForChime: currentMinute,
            };
          } else {
            nextState = { ...nextState, lastQuarterHourForChime: prevState.lastQuarterHourForChime };
          }
        } catch {
          nextState = { ...nextState, lastQuarterHourForChime: prevState.lastQuarterHourForChime };
        }
      }

      // Server broadcasts game_tick; show [Tick N] every 23 ticks (0, 23, 46, ...).
      if (tickNumber % 23 === 0 && tickNumber >= 0) {
        const tickMsg = buildChatMessage(`[Tick ${tickNumber}]`, event.timestamp, {
          messageType: 'system',
          channel: 'system',
        });
        nextState = { ...nextState, messages: appendMessage(nextState.messages, tickMsg) };
      }
      break;
    }
    case 'follow_request': {
      const requestId = typeof event.data.request_id === 'string' ? event.data.request_id : '';
      const requestorName = typeof event.data.requestor_name === 'string' ? event.data.requestor_name : 'Someone';
      if (requestId) {
        nextState = {
          ...prevState,
          pendingFollowRequest: { request_id: requestId, requestor_name: requestorName },
        };
      }
      break;
    }
    case 'follow_request_cleared': {
      nextState = { ...prevState, pendingFollowRequest: null };
      break;
    }
    default:
      break;
  }

  return nextState;
}

/**
 * Derive full GameState from the event log. Pure function.
 */
export function projectState(log: EventLog): GameState {
  return log.reduce((state, event) => projectEvent(state, event), getInitialGameState());
}
