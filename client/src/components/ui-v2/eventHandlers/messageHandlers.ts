// Message-related event handlers
// As documented in "Message Processing Utilities" - Dr. Armitage, 1928

import { logger } from '../../../utils/logger';
import { determineMessageType } from '../../../utils/messageTypeUtils';
import { convertToPlayerInterface, parseStatusResponse } from '../../../utils/statusParser';
import type { EventHandler, GameStateUpdates } from './types';

const GAME_LOG_CHANNEL = 'game-log';

/**
 * Channel to chat type mapping for O(1) lookup complexity.
 */
const CHANNEL_TO_TYPE_MAP: Record<string, string> = {
  whisper: 'whisper',
  shout: 'shout',
  emote: 'emote',
  party: 'tell',
  tell: 'tell',
  system: 'system',
  game: 'system',
  local: 'say',
  say: 'say',
};

/**
 * Resolve chat type from channel name.
 * Uses a lookup map for O(1) complexity instead of switch statement.
 */
const resolveChatTypeFromChannel = (channel: string): string => {
  return CHANNEL_TO_TYPE_MAP[channel] ?? 'say';
};

export const handleCommandResponse: EventHandler = (event, context, appendMessage) => {
  const suppressChat = Boolean(event.data.suppress_chat);
  const message = typeof event.data.result === 'string' ? (event.data.result as string) : '';
  const isHtml = Boolean(event.data.is_html);
  const gameLogChannel =
    typeof event.data.game_log_channel === 'string' && event.data.game_log_channel
      ? (event.data.game_log_channel as string)
      : GAME_LOG_CHANNEL;
  const gameLogMessage =
    (typeof event.data.game_log_message === 'string' && event.data.game_log_message.length > 0
      ? (event.data.game_log_message as string)
      : undefined) || message;

  const updates: GameStateUpdates = {};

  if (message) {
    if (message.includes('Name:') && message.includes('Health:') && message.includes('Lucidity:')) {
      try {
        const parsedPlayerData = parseStatusResponse(message);
        const playerData = convertToPlayerInterface(parsedPlayerData);
        updates.player = playerData;
      } catch (error) {
        logger.error('messageHandlers', 'Failed to parse status response', {
          error: error instanceof Error ? error.message : String(error),
        });
      }
    }
  }

  // Process player_update from command responses
  if (event.data.player_update && context.currentPlayerRef.current && context.currentPlayerRef.current.stats) {
    const playerUpdate = event.data.player_update as {
      position?: string;
      previous_position?: string;
      [key: string]: unknown;
    };
    updates.player = {
      ...context.currentPlayerRef.current,
      stats: {
        ...context.currentPlayerRef.current.stats,
        ...(playerUpdate.position && { position: playerUpdate.position }),
      },
    };
  }

  // Filter out room name-only messages
  const isRoomNameOnly =
    message &&
    message.trim().length > 0 &&
    message.trim().length < 100 &&
    !message.includes('\n') &&
    !message.includes('Exits:') &&
    !message.includes('Description:') &&
    context.currentRoomRef.current &&
    message.trim() === context.currentRoomRef.current.name;

  if (!suppressChat && message && !isRoomNameOnly) {
    const messageTypeResult = determineMessageType(message);
    appendMessage({
      text: message,
      timestamp: event.timestamp,
      isHtml,
      messageType: messageTypeResult.type,
      channel: messageTypeResult.channel ?? 'game',
      type: resolveChatTypeFromChannel(messageTypeResult.channel ?? 'game'),
    });
  } else if (gameLogMessage && !isRoomNameOnly) {
    appendMessage({
      text: gameLogMessage,
      timestamp: event.timestamp,
      isHtml,
      messageType: 'system',
      channel: gameLogChannel,
      type: 'system',
    });
  }

  return updates;
};

export const handleChatMessage: EventHandler = (_event, _context, appendMessage) => {
  const message = _event.data.message as string;
  const channel = _event.data.channel as string;
  if (message) {
    let messageType: string;
    switch (channel) {
      case 'whisper':
        messageType = 'whisper';
        break;
      case 'shout':
        messageType = 'shout';
        break;
      case 'emote':
        messageType = 'emote';
        break;
      case 'party':
        messageType = 'chat';
        break;
      case 'say':
      case 'local':
      default:
        messageType = 'chat';
        break;
    }

    appendMessage({
      text: message,
      timestamp: _event.timestamp,
      isHtml: false,
      messageType: messageType,
      channel: channel,
      type: resolveChatTypeFromChannel(channel),
    });
  }
};

export const handleRoomMessage: EventHandler = (event, _context, appendMessage) => {
  const message = typeof event.data.message === 'string' ? (event.data.message as string) : '';
  const messageTypeFromEvent =
    typeof event.data.message_type === 'string' ? (event.data.message_type as string) : undefined;
  const isHtml = Boolean(event.data.is_html);

  if (message) {
    let messageType: string;
    let channel: string;
    let type: string;

    if (messageTypeFromEvent === 'system') {
      messageType = 'system';
      channel = GAME_LOG_CHANNEL;
      type = 'system'; // System messages should always have type 'system'
    } else {
      const messageTypeResult = determineMessageType(message);
      messageType = messageTypeResult.type;
      channel = messageTypeResult.channel ?? 'game';
      type = resolveChatTypeFromChannel(channel);
    }

    appendMessage({
      text: message,
      timestamp: event.timestamp,
      isHtml,
      messageType: messageType,
      channel: channel,
      type: type,
    });
  }
};

export const handleSystem: EventHandler = (event, _context, appendMessage) => {
  const systemMessage = event.data.message;
  if (systemMessage && typeof systemMessage === 'string') {
    appendMessage({
      text: systemMessage,
      timestamp: event.timestamp,
      isHtml: false,
      messageType: 'system',
      channel: 'game',
      type: 'system',
    });
  }
};
