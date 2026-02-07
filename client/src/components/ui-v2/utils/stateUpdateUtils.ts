// State update utility functions
// Extracted from GameClientV2Container to reduce complexity
// As documented in "State Management Patterns" - Dr. Armitage, 1928

import type { MythosTimeState } from '../../../types/mythosTime';
import type { GameStateUpdates } from '../eventHandlers/types';
import type { ChatMessage, Player, Room } from '../types';
import { sanitizeChatMessageForState } from './messageUtils';
import { mergeRoomState } from './roomMergeUtils';

export interface GameState {
  player: Player | null;
  room: Room | null;
  messages: ChatMessage[];
  commandHistory: string[];
  loginGracePeriodActive?: boolean;
  loginGracePeriodRemaining?: number;
  /** Derived from game_tick; used for Mythos time display. Bootstrap may set initial until first tick. */
  mythosTime?: MythosTimeState | null;
  /** Last quarter-hour minute projected (for deduplicating clock chime messages). */
  lastQuarterHourForChime?: number | null;
  /**
   * Last sequence_number applied per room_id for room_occupants.
   * Server-authoritative: ignore room_occupants with older sequence to avoid
   * stale updates (e.g. second NPC stays after death).
   */
  lastRoomOccupantsSequenceByRoom?: Record<string, number>;
}

// Helper: treat empty arrays/count as "no data" so we preserve existing
// (room_update sends empty; room_occupants is authoritative).
function hasOccupantData(room: Room): boolean {
  const hasPlayers = room.players != null && room.players.length > 0;
  const hasNpcs = room.npcs != null && room.npcs.length > 0;
  const hasOccupants = room.occupants != null && room.occupants.length > 0;
  return hasPlayers || hasNpcs || hasOccupants;
}

// Helper function to merge occupant data from two room updates
export const mergeOccupantData = (newRoom: Room, existingRoom: Room) => {
  const useNewOccupants = hasOccupantData(newRoom);
  return {
    players: useNewOccupants ? (newRoom.players ?? existingRoom.players) : (existingRoom.players ?? []),
    npcs: useNewOccupants ? (newRoom.npcs ?? existingRoom.npcs) : (existingRoom.npcs ?? []),
    occupants: useNewOccupants ? (newRoom.occupants ?? existingRoom.occupants) : (existingRoom.occupants ?? []),
    occupant_count: useNewOccupants
      ? (newRoom.occupant_count ?? existingRoom.occupant_count ?? 0)
      : (existingRoom.occupant_count ?? 0),
  };
};

// Helper function to merge room updates
export const mergeRoomUpdate = (existingRoom: Room | null, newRoom: Room): Room => {
  if (!existingRoom || existingRoom.id !== newRoom.id) {
    return newRoom;
  }

  // Both updates are for the same room - merge occupant data
  return {
    ...existingRoom,
    ...newRoom,
    // Preserve occupant data from the more authoritative source (room_occupants)
    ...mergeOccupantData(newRoom, existingRoom),
  };
};

// Helper function to apply player update
export const applyPlayerUpdate = (eventUpdates: GameStateUpdates, updates: Partial<GameState>): void => {
  if (eventUpdates.player !== undefined) {
    updates.player = eventUpdates.player;
  }
};

// Helper function to apply room update
export const applyRoomUpdate = (
  eventUpdates: GameStateUpdates,
  updates: Partial<GameState>,
  mergeRoomUpdateFn: (existing: Room | null, newRoom: Room) => Room
): void => {
  if (!eventUpdates.room) {
    return;
  }

  updates.room = updates.room ? mergeRoomUpdateFn(updates.room, eventUpdates.room) : eventUpdates.room;
};

// Helper function to apply message updates
// Uses immutable patterns: creates new arrays instead of mutating existing ones
export const applyMessageUpdates = (
  eventUpdates: GameStateUpdates,
  updates: Partial<GameState>,
  currentMessages: ChatMessage[]
): void => {
  if (!eventUpdates.messages) {
    return;
  }

  // Create new array by spreading existing messages and new messages
  // This ensures we don't mutate the original currentMessages array
  updates.messages = [...(updates.messages || currentMessages), ...eventUpdates.messages];
};

// Helper function to apply grace period updates
export const applyGracePeriodUpdate = (eventUpdates: GameStateUpdates, updates: Partial<GameState>): void => {
  if (eventUpdates.loginGracePeriodActive !== undefined) {
    updates.loginGracePeriodActive = eventUpdates.loginGracePeriodActive;
  }
  if (eventUpdates.loginGracePeriodRemaining !== undefined) {
    updates.loginGracePeriodRemaining = eventUpdates.loginGracePeriodRemaining;
  }
};

// Helper function to apply updates from a single event
export const applyEventUpdates = (
  eventUpdates: GameStateUpdates | void,
  updates: Partial<GameState>,
  currentMessages: ChatMessage[]
): void => {
  if (!eventUpdates) {
    return;
  }

  applyPlayerUpdate(eventUpdates, updates);
  applyRoomUpdate(eventUpdates, updates, mergeRoomUpdate);
  applyMessageUpdates(eventUpdates, updates, currentMessages);
  applyGracePeriodUpdate(eventUpdates, updates);
};

// Helper function to sanitize and apply updates to state
export const sanitizeAndApplyUpdates = (
  updates: Partial<GameState>,
  setGameState: React.Dispatch<React.SetStateAction<GameState>>
): void => {
  if (Object.keys(updates).length === 0) {
    return;
  }

  // Sanitize messages
  const sanitizedMessages = updates.messages ? updates.messages.map(sanitizeChatMessageForState) : undefined;

  setGameState(prev => {
    const finalRoom = updates.room ? mergeRoomState(updates.room, prev.room) : prev.room;

    return {
      ...prev,
      ...updates,
      messages: sanitizedMessages || prev.messages,
      player: updates.player || prev.player,
      room: finalRoom,
      // Preserve grace period fields if not explicitly updated
      loginGracePeriodActive:
        updates.loginGracePeriodActive !== undefined ? updates.loginGracePeriodActive : prev.loginGracePeriodActive,
      loginGracePeriodRemaining:
        updates.loginGracePeriodRemaining !== undefined
          ? updates.loginGracePeriodRemaining
          : prev.loginGracePeriodRemaining,
    };
  });
};
