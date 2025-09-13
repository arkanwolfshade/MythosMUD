/**
 * State management exports
 *
 * This module provides a centralized export point for all Zustand stores
 * and related utilities used in the MythosMUD client application.
 */

// Store exports
export { useCommandStore } from './commandStore';
export { useConnectionStore } from './connectionStore';
export { useGameStore } from './gameStore';
export { useSessionStore } from './sessionStore';

// Type exports
export type {
  ConnectionActions,
  ConnectionHealth,
  ConnectionMetadata,
  ConnectionSelectors,
  ConnectionState,
  GameEvent,
} from './connectionStore';

export type { ChatMessage, GameActions, GameLogEntry, GameSelectors, GameState, Player, Room } from './gameStore';

export type { SessionActions, SessionSelectors, SessionState } from './sessionStore';

export type {
  CommandActions,
  CommandAlias,
  CommandHistoryEntry,
  CommandSelectors,
  CommandState,
  CommandTrigger,
} from './commandStore';

// State normalization exports
export {
  createEntityMap,
  denormalizeGameData,
  getEntitiesByIds,
  getEntitiesByType,
  getEntityById,
  mergeEntityMaps,
  normalizeGameData,
  removeEntitiesFromNormalizedData,
  removeEntityFromMap,
  updateEntityInMap,
  updateNormalizedData,
} from './stateNormalization';

export type { Entity, EntityMap, GameData, NormalizedGameData } from './stateNormalization';
