// State update utility functions
// Extracted from GameClientV2Container to reduce complexity
// As documented in "State Management Patterns" - Dr. Armitage, 1928

import type { ChatMessage, Player, Room } from '../types';
import { sanitizeChatMessageForState } from './messageUtils';
import { mergeRoomState } from './roomMergeUtils';
import type { GameStateUpdates } from '../eventHandlers/types';

export interface GameState {
  player: Player | null;
  room: Room | null;
  messages: ChatMessage[];
  commandHistory: string[];
}

// Helper function to merge occupant data from two room updates
export const mergeOccupantData = (newRoom: Room, existingRoom: Room) => {
  return {
    players: newRoom.players ?? existingRoom.players,
    npcs: newRoom.npcs ?? existingRoom.npcs,
    occupants: newRoom.occupants ?? existingRoom.occupants,
    occupant_count: newRoom.occupant_count ?? existingRoom.occupant_count,
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
export const applyMessageUpdates = (
  eventUpdates: GameStateUpdates,
  updates: Partial<GameState>,
  currentMessages: ChatMessage[]
): void => {
  if (!eventUpdates.messages) {
    return;
  }

  if (!updates.messages) {
    updates.messages = [...currentMessages];
  }
  updates.messages.push(...eventUpdates.messages);
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
    };
  });
};
