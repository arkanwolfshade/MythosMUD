// State update utility functions
// Extracted from GameClientV2Container to reduce complexity
// As documented in "State Management Patterns" - Dr. Armitage, 1928

import type { MythosTimeState } from '../../../types/mythosTime';
import type { GameStateUpdates } from '../eventHandlers/types';
import type { ChatMessage, Player, Room } from '../types';
import { sanitizeChatMessageForState } from './messageUtils';
import { mergeRoomState } from './roomMergeUtils';

/** Single active effect for header display (server-authoritative). */
export interface ActiveEffectDisplay {
  effect_type: string;
  label?: string;
  remaining_seconds?: number;
}

export interface GameState {
  player: Player | null;
  room: Room | null;
  messages: ChatMessage[];
  commandHistory: string[];
  loginGracePeriodActive?: boolean;
  loginGracePeriodRemaining?: number;
  /** Active effects for header bar (e.g. LOGIN_WARDED). When absent, derived from grace period for backward compat. */
  activeEffects?: ActiveEffectDisplay[];
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
  /** Pending follow request (target player only). Cleared when user accepts/declines or request expires. */
  pendingFollowRequest?: { request_id: string; requestor_name: string } | null;
  /** Pending party invite (invitee only). Cleared when user accepts/declines or invite expires. */
  pendingPartyInvite?: { invite_id: string; inviter_name: string } | null;
  /** Who the player is following (for title panel). Server-authoritative. */
  followingTarget?: { target_name: string; target_type: 'player' | 'npc' } | null;
}

// Helper: treat empty arrays as "no data" so we preserve existing
// (room_update sends empty; room_occupants is authoritative).
function hasOccupantData(room: Room): boolean {
  const hasPlayers = room.players != null && room.players.length > 0;
  const hasNpcs = room.npcs != null && room.npcs.length > 0;
  return hasPlayers || hasNpcs;
}

// Helper function to merge occupant data from two room updates
export const mergeOccupantData = (newRoom: Room, existingRoom: Room) => {
  const useNewOccupants = hasOccupantData(newRoom);
  const players = useNewOccupants ? (newRoom.players ?? existingRoom.players ?? []) : (existingRoom.players ?? []);
  const npcs = useNewOccupants ? (newRoom.npcs ?? existingRoom.npcs ?? []) : (existingRoom.npcs ?? []);
  const playersArr = Array.isArray(players) ? players : [];
  const npcsArr = Array.isArray(npcs) ? npcs : [];
  const occupants = [...playersArr, ...npcsArr];
  const occupantCount = useNewOccupants
    ? (newRoom.occupant_count ?? occupants.length)
    : (existingRoom.occupant_count ?? occupants.length);
  return {
    players: playersArr,
    npcs: npcsArr,
    occupants,
    occupant_count: occupantCount,
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
  if (eventUpdates.followingTarget !== undefined) {
    updates.followingTarget = eventUpdates.followingTarget;
  }
};

/**
 * Sanitize and apply updates to game state.
 * Note: When updates.room comes from an authoritative server event (e.g. room_state), room should
 * replace rather than merge; this implementation always merges. Do not use for authoritative room
 * updates from server, or extend the API (e.g. replaceRoom flag) to support replace.
 */
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
