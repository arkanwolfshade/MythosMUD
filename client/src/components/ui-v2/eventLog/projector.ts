// Event-sourced GameState projector: derives state from event log (pure, no refs)
// As documented in "Event Processing Architecture" - Dr. Armitage, 1928
// Server is authoritative; prefer server payloads (game_state, room_state, command_response) over client state.
// See .cursor/rules/server-authority.mdc
// Split into constants, messageUtils, and handler modules to keep file-nloc under limit.

import type { GameEvent } from '../eventHandlers/types';
import type { GameState } from '../utils/stateUpdateUtils';
import { getInitialGameState, PROJECTED_EVENT_TYPES } from './projectorConstants';
import { messageHandlers } from './projectorHandlersMessages';
import { stateHandlers } from './projectorHandlersState';
import type { EventLog } from './types';

const HANDLERS = { ...stateHandlers, ...messageHandlers };

export { getInitialGameState };

/**
 * Project a single event onto previous state. Pure function; no refs or side effects.
 */
/** Keep connected self in room.players so Occupants never looks empty after settle. */
function ensureSelfListedInRoomPlayers(state: GameState): GameState {
  const name = state.player?.name?.trim();
  const room = state.room;
  if (!name || !room?.id) {
    return state;
  }
  const players = room.players ?? [];
  if (players.some(p => p.toLowerCase() === name.toLowerCase())) {
    return state;
  }
  const nextPlayers = [...players, name];
  const npcs = room.npcs ?? [];
  // Do not recompute occupant_count: server value is authoritative and may include
  // hidden/other entities not present in players/npcs lists.
  return {
    ...state,
    room: {
      ...room,
      players: nextPlayers,
      occupants: [...nextPlayers, ...npcs],
    },
  };
}

export function projectEvent(prevState: GameState, event: GameEvent): GameState {
  const eventType = (event.event_type ?? '').toString().trim().toLowerCase();
  if (!PROJECTED_EVENT_TYPES.has(eventType)) {
    return prevState;
  }
  const handler = HANDLERS[eventType];
  const next = handler ? handler(prevState, event) : prevState;
  return ensureSelfListedInRoomPlayers(next);
}

/**
 * Derive full GameState from the event log. Pure function.
 */
export function projectState(log: EventLog): GameState {
  return log.reduce((state, event) => projectEvent(state, event), getInitialGameState());
}
