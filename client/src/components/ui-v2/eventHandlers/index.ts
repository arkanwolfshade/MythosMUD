// Event handler registry and processor
// As documented in "Event Processing Architecture" - Dr. Armitage, 1928

import type { GameEvent } from './types';
import * as playerHandlers from './playerHandlers';
import * as roomHandlers from './roomHandlers';
import * as combatHandlers from './combatHandlers';
import * as messageHandlers from './messageHandlers';
import * as systemHandlers from './systemHandlers';
import type { EventHandler, EventHandlerContext, GameStateUpdates } from './types';
import type { ChatMessage } from '../types';
import { logger } from '../../../utils/logger';

// Event handler registry mapping event types to handlers
const eventHandlers: Record<string, EventHandler> = {
  // Player events
  player_entered_game: playerHandlers.handlePlayerEnteredGame,
  player_entered: playerHandlers.handlePlayerEntered,
  player_left_game: playerHandlers.handlePlayerLeftGame,
  player_left: playerHandlers.handlePlayerLeft,
  player_died: playerHandlers.handlePlayerDied,
  playerdied: playerHandlers.handlePlayerDied,
  player_respawned: playerHandlers.handlePlayerRespawned,
  playerrespawned: playerHandlers.handlePlayerRespawned,
  player_delirium_respawned: playerHandlers.handlePlayerDeliriumRespawned,
  playerdeliriumrespawned: playerHandlers.handlePlayerDeliriumRespawned,
  player_dp_updated: playerHandlers.handlePlayerDpUpdated,
  playerdpupdated: playerHandlers.handlePlayerDpUpdated,
  player_update: playerHandlers.handlePlayerUpdate,

  // Room events
  game_state: roomHandlers.handleGameState,
  room_update: roomHandlers.handleRoomUpdate,
  room_state: roomHandlers.handleRoomUpdate,
  room_occupants: roomHandlers.handleRoomOccupants,

  // Combat events
  npc_attacked: combatHandlers.handleNpcAttacked,
  player_attacked: combatHandlers.handlePlayerAttacked,
  combat_started: combatHandlers.handleCombatStarted,
  combat_ended: combatHandlers.handleCombatEnded,
  npc_died: combatHandlers.handleNpcDied,
  combat_death: combatHandlers.handleCombatDeath,

  // Message events
  command_response: messageHandlers.handleCommandResponse,
  chat_message: messageHandlers.handleChatMessage,
  room_message: messageHandlers.handleRoomMessage,
  system: messageHandlers.handleSystem,

  // System events
  lucidity_change: systemHandlers.handleLucidityChange,
  luciditychange: systemHandlers.handleLucidityChange,
  rescue_update: systemHandlers.handleRescueUpdate,
  mythos_time_update: systemHandlers.handleMythosTimeUpdate,
  game_tick: systemHandlers.handleGameTick,
  intentional_disconnect: systemHandlers.handleIntentionalDisconnect,
};

/**
 * Process a single game event and return state updates
 */
export const processGameEvent = (
  event: GameEvent,
  context: EventHandlerContext,
  appendMessage: (message: ChatMessage) => void,
  lastProcessedEvent: React.MutableRefObject<string>
): GameStateUpdates | null => {
  const eventKey = `${event.event_type}_${event.sequence_number}`;
  if (eventKey === lastProcessedEvent.current) {
    return null; // Already processed
  }
  lastProcessedEvent.current = eventKey;

  const eventType = (event.event_type || '').toString().trim().toLowerCase();
  logger.info('eventHandlers', 'Processing event', { event_type: eventType });

  // Validate event type against allowlist to prevent unsafe dynamic method calls
  // Only allow event types that are explicitly defined in the eventHandlers registry
  if (!(eventType in eventHandlers)) {
    logger.warn('eventHandlers', 'Unknown event type, ignoring', { event_type: eventType });
    return null;
  }

  const handler = eventHandlers[eventType];
  if (handler) {
    try {
      const updates = handler(event, context, appendMessage);
      return updates || null;
    } catch (error) {
      logger.error('eventHandlers', 'Error processing event', {
        event_type: eventType,
        error: error instanceof Error ? error.message : String(error),
      });
      return null;
    }
  } else {
    logger.info('eventHandlers', 'Unhandled event type', {
      event_type: event.event_type,
      data_keys: event.data ? Object.keys(event.data) : [],
    });
    return null;
  }
};
