// Message/chat/combat/tick event handlers for the projector (split from projector.ts for file-nloc)

import type { MythosTimePayload } from '../../../types/mythosTime';
import { logger } from '../../../utils/logger';
import { determineMessageType } from '../../../utils/messageTypeUtils';
import { buildMythosTimeState, formatMythosTime12Hour } from '../../../utils/mythosTime';
import type { GameEvent } from '../eventHandlers/types';
import {
  formatNpcAttackedLine,
  formatPlayerAttackedLine,
  mergePlayerDpFromPlayerAttackedPayload,
} from './messageMapper';
import type { ProjectorHandler } from './projectorHandlersState';
import { GAME_LOG_CHANNEL, appendMessage, appendMovementMessage, buildChatMessage } from './projectorMessageUtils';
import { deriveRoomFromRoomState } from './projectorRoom';

export const messageHandlers: Partial<Record<string, ProjectorHandler>> = {
  command_response(prevState, event) {
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
    let nextState = prevState;
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
    const roomStatePayload = event.data.room_state as GameEvent | undefined;
    if (roomStatePayload?.data?.room) {
      const room = deriveRoomFromRoomState(roomStatePayload);
      if (room) nextState = { ...nextState, room };
    }
    const playerUpdatePayload = (event.data as { player_update?: Record<string, unknown> }).player_update;
    if (playerUpdatePayload && nextState.player) {
      const current = nextState.player;
      const rawStats =
        playerUpdatePayload.stats && typeof playerUpdatePayload.stats === 'object' && playerUpdatePayload.stats !== null
          ? (playerUpdatePayload.stats as Record<string, unknown>)
          : {};
      const serverStats = {
        ...rawStats,
        ...(playerUpdatePayload.position !== undefined && { position: playerUpdatePayload.position }),
        ...(playerUpdatePayload.previous_position !== undefined && {
          previous_position: playerUpdatePayload.previous_position,
        }),
      };
      /* eslint-disable-next-line @typescript-eslint/no-unused-vars */
      const { stats: _s, position: _p, previous_position: _pp, ...topLevel } = playerUpdatePayload;
      nextState = {
        ...nextState,
        player: {
          ...current,
          ...topLevel,
          stats: { ...current.stats, ...serverStats } as NonNullable<typeof current.stats>,
        },
      };
    }
    return nextState;
  },

  chat_message(prevState, event) {
    const message = event.data.message as string | undefined;
    const channel = event.data.channel as string | undefined;
    if (!message || !channel) return prevState;
    const messageType =
      channel === 'whisper' ? 'whisper' : channel === 'shout' ? 'shout' : channel === 'emote' ? 'emote' : 'chat';
    const msg = buildChatMessage(message, event.timestamp, { messageType, channel });
    return { ...prevState, messages: appendMessage(prevState.messages, msg) };
  },

  room_message(prevState, event) {
    const message = typeof event.data.message === 'string' ? (event.data.message as string) : '';
    const messageTypeFromEvent =
      typeof event.data.message_type === 'string' ? (event.data.message_type as string) : undefined;
    const isHtml = Boolean(event.data.is_html);
    if (!message) return prevState;
    const messageType = messageTypeFromEvent === 'system' ? 'system' : determineMessageType(message).type;
    const channel =
      messageTypeFromEvent === 'system' ? GAME_LOG_CHANNEL : (determineMessageType(message).channel ?? 'game');
    const msg = buildChatMessage(message, event.timestamp, { isHtml, messageType, channel });
    return {
      ...prevState,
      messages:
        messageTypeFromEvent === 'system'
          ? appendMovementMessage(prevState.messages, msg)
          : appendMessage(prevState.messages, msg),
    };
  },

  system(prevState, event) {
    const systemMessage = event.data.message;
    if (!systemMessage || typeof systemMessage !== 'string') return prevState;
    const msg = buildChatMessage(systemMessage, event.timestamp, {
      messageType: 'system',
      channel: 'game',
    });
    return { ...prevState, messages: appendMessage(prevState.messages, msg) };
  },

  npc_attacked(prevState, event) {
    const d = (event.data?.event_data ?? event.data) as Record<string, unknown> | undefined;
    if (!d) return prevState;
    const npcName = (d.npc_name || d.target_name) as string | undefined;
    const damage = d.damage as number | undefined;
    if (!npcName || damage === undefined) return prevState;
    const text = formatNpcAttackedLine(d);
    const msg = buildChatMessage(text, event.timestamp, {
      messageType: 'system',
      channel: GAME_LOG_CHANNEL,
    });
    logger.info('projector', 'Combat message appended (npc_attacked)', {
      event_type: 'npc_attacked',
      text_preview: text.slice(0, 80),
    });
    return { ...prevState, messages: appendMessage(prevState.messages, msg) };
  },

  player_attacked(prevState, event) {
    const d = (event.data?.event_data ?? event.data) as Record<string, unknown> | undefined;
    if (!d) return prevState;
    const attackerName = d.attacker_name as string | undefined;
    const damage = d.damage as number | undefined;
    if (!attackerName || damage === undefined) return prevState;
    const mergedPlayer = mergePlayerDpFromPlayerAttackedPayload(prevState.player, d);
    let nextState = prevState;
    if (mergedPlayer) {
      nextState = { ...nextState, player: mergedPlayer };
    }
    const text = formatPlayerAttackedLine(d);
    const msg = buildChatMessage(text, event.timestamp, {
      messageType: 'system',
      channel: GAME_LOG_CHANNEL,
    });
    logger.info('projector', 'Combat message appended (player_attacked)', {
      event_type: 'player_attacked',
      text_preview: text.slice(0, 80),
    });
    return { ...nextState, messages: appendMessage(nextState.messages, msg) };
  },

  npc_died(prevState, event) {
    const message = event.data.message as string | undefined;
    if (!message) return prevState;
    const msg = buildChatMessage(message, event.timestamp, {
      messageType: 'system',
      channel: GAME_LOG_CHANNEL,
    });
    return { ...prevState, messages: appendMessage(prevState.messages, msg) };
  },
  combat_death(prevState, event) {
    return messageHandlers.npc_died!(prevState, event);
  },

  combat_target_switch(prevState, event) {
    const message = event.data.message as string | undefined;
    if (!message) return prevState;
    const msg = buildChatMessage(message, event.timestamp, {
      messageType: 'combat',
      channel: GAME_LOG_CHANNEL,
    });
    return { ...prevState, messages: appendMessage(prevState.messages, msg) };
  },

  intentional_disconnect(prevState, event) {
    const message = (event.data as { message?: string }).message || 'You have disconnected from the game.';
    const msg = buildChatMessage(message, event.timestamp, {
      messageType: 'system',
      channel: 'game',
    });
    return { ...prevState, messages: appendMessage(prevState.messages, msg) };
  },

  game_tick(prevState, event) {
    const data = event.data as Record<string, unknown>;
    const tickNumber = typeof data.tick_number === 'number' ? data.tick_number : 0;
    let nextState = prevState;

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

    if (tickNumber % 23 === 0 && tickNumber >= 0) {
      const tickMsg = buildChatMessage(`[Tick ${tickNumber}]`, event.timestamp, {
        messageType: 'system',
        channel: 'system',
      });
      nextState = { ...nextState, messages: appendMessage(nextState.messages, tickMsg) };
    }
    return nextState;
  },
};
