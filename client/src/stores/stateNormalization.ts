/**
 * State normalization utilities for game data
 *
 * This module provides functions to normalize and denormalize game data
 * to prevent data duplication and improve performance when managing
 * complex nested game state.
 */

export interface Entity {
  id: string;
  [key: string]: unknown;
}

export interface EntityMap {
  [id: string]: Entity;
}

export interface NormalizedGameData {
  player: string | null;
  room: string | null;
  chatMessages: string[];
  gameLog: string[];
  entities: EntityMap;
}

export interface GameData {
  player?: Entity | null;
  room?: Entity | null;
  chatMessages?: Entity[];
  gameLog?: Entity[];
  [key: string]: unknown;
}

/**
 * Creates an entity map from an array of entities
 * @param entities Array of entities with id properties
 * @returns Entity map with id as key
 */
export function createEntityMap(entities: Entity[]): EntityMap {
  const entityMap: EntityMap = {};

  entities.forEach(entity => {
    if (entity.id) {
      entityMap[entity.id] = entity;
    }
  });

  return entityMap;
}

/**
 * Merges two entity maps, with the second map taking precedence for overlapping keys
 * @param map1 First entity map
 * @param map2 Second entity map
 * @returns Merged entity map
 */
export function mergeEntityMaps(map1: EntityMap, map2: EntityMap): EntityMap {
  return { ...map1, ...map2 };
}

/**
 * Gets an entity by ID from an entity map
 * @param entityMap Entity map to search
 * @param id Entity ID to find
 * @returns Entity or null if not found
 */
export function getEntityById(entityMap: EntityMap, id: string): Entity | null {
  return entityMap[id] || null;
}

/**
 * Updates an entity in an entity map
 * @param entityMap Entity map to update
 * @param id Entity ID to update
 * @param updates Partial entity data to merge
 * @returns Updated entity map
 */
export function updateEntityInMap(entityMap: EntityMap, id: string, updates: Partial<Entity>): EntityMap {
  return {
    ...entityMap,
    [id]: {
      ...entityMap[id],
      ...updates,
      id, // Ensure ID is preserved
    },
  };
}

/**
 * Removes an entity from an entity map
 * @param entityMap Entity map to update
 * @param id Entity ID to remove
 * @returns Updated entity map
 */
export function removeEntityFromMap(entityMap: EntityMap, id: string): EntityMap {
  if (!entityMap[id]) {
    return entityMap; // Return same reference if entity doesn't exist
  }

  const newMap = { ...entityMap };
  delete newMap[id];
  return newMap;
}

/**
 * Recursively extracts entities from nested data structures
 * @param data Data to extract entities from
 * @param entityMap Existing entity map to add to
 * @returns Updated entity map with extracted entities
 */
function extractEntities(data: unknown, entityMap: EntityMap = {}): EntityMap {
  if (!data || typeof data !== 'object') {
    return entityMap;
  }

  const obj = data as Record<string, unknown>;

  // If this object has an id, it's an entity
  if (obj.id && typeof obj.id === 'string') {
    entityMap[obj.id] = obj as Entity;
  }

  // Recursively process all properties
  Object.values(obj).forEach(value => {
    if (Array.isArray(value)) {
      // Process array items
      value.forEach(item => {
        extractEntities(item, entityMap);
      });
    } else if (value && typeof value === 'object') {
      // Process nested objects
      extractEntities(value, entityMap);
    }
  });

  return entityMap;
}

/**
 * Recursively replaces entity references with IDs
 * @param data Data to process
 * @param entityMap Entity map for reference
 * @returns Data with entity references replaced by IDs
 */
function replaceEntitiesWithIds(data: unknown, entityMap: EntityMap): unknown {
  if (!data || typeof data !== 'object') {
    return data;
  }

  const obj = data as Record<string, unknown>;

  // If this is an entity that's already in the map, return its ID
  // But only if it's a reference to an entity, not the entity itself we're processing
  if (obj.id && typeof obj.id === 'string' && entityMap[obj.id] && obj === entityMap[obj.id]) {
    return obj.id;
  }

  // Process arrays
  if (Array.isArray(obj)) {
    return obj.map(item => replaceEntitiesWithIds(item, entityMap));
  }

  // Process object properties
  const result: Record<string, unknown> = {};
  Object.entries(obj).forEach(([key, value]) => {
    if (Array.isArray(value)) {
      // Special handling for entities arrays - replace with IDs
      if (key === 'entities' && value.every(item => item && typeof item === 'object' && 'id' in item)) {
        result[key] = value.map(item => (item as Entity).id);
      } else {
        result[key] = value.map(item => replaceEntitiesWithIds(item, entityMap));
      }
    } else if (value && typeof value === 'object') {
      result[key] = replaceEntitiesWithIds(value, entityMap);
    } else {
      result[key] = value;
    }
  });

  return result;
}

/**
 * Normalizes game data by extracting entities and replacing references with IDs
 * @param gameData Game data to normalize
 * @returns Normalized game data structure
 */
export function normalizeGameData(gameData: GameData): NormalizedGameData {
  // Extract all entities from the game data
  const entities = extractEntities(gameData);

  // Create normalized structure with entity references replaced by IDs
  const normalized: NormalizedGameData = {
    player: null,
    room: null,
    chatMessages: [],
    gameLog: [],
    entities,
  };

  // Process player
  if (gameData.player && gameData.player.id) {
    normalized.player = gameData.player.id;
  }

  // Process room
  if (gameData.room && gameData.room.id) {
    normalized.room = gameData.room.id;
    // Create a copy of the room and replace entity references with IDs
    const roomCopy = { ...gameData.room };
    const roomWithIds = replaceEntitiesWithIds(roomCopy, entities) as Entity;
    normalized.entities[gameData.room.id] = roomWithIds;
  }

  // Process chat messages
  if (Array.isArray(gameData.chatMessages)) {
    normalized.chatMessages = gameData.chatMessages.filter(msg => msg.id).map(msg => msg.id as string);
  }

  // Process game log
  if (Array.isArray(gameData.gameLog)) {
    normalized.gameLog = gameData.gameLog.filter(entry => entry.id).map(entry => entry.id as string);
  }

  return normalized;
}

/**
 * Recursively restores entity references in data structures
 * @param data Data to process
 * @param entityMap Entity map for reference
 * @returns Data with entity IDs replaced by actual entities
 */
function restoreEntityReferences(data: unknown, entityMap: EntityMap): unknown {
  if (!data || typeof data !== 'object') {
    return data;
  }

  const obj = data as Record<string, unknown>;

  // Process arrays
  if (Array.isArray(obj)) {
    return obj.map(item => restoreEntityReferences(item, entityMap));
  }

  // Process object properties
  const result: Record<string, unknown> = {};
  Object.entries(obj).forEach(([key, value]) => {
    if (Array.isArray(value)) {
      // Special handling for entities arrays - restore from IDs
      if (key === 'entities' && value.every(item => typeof item === 'string')) {
        result[key] = value.map(id => entityMap[id]).filter(Boolean);
      } else {
        result[key] = value.map(item => restoreEntityReferences(item, entityMap));
      }
    } else if (value && typeof value === 'object') {
      result[key] = restoreEntityReferences(value, entityMap);
    } else {
      result[key] = value;
    }
  });

  return result;
}

/**
 * Denormalizes game data by replacing entity IDs with actual entities
 * @param normalizedData Normalized game data
 * @returns Denormalized game data structure
 */
export function denormalizeGameData(normalizedData: NormalizedGameData): GameData {
  const result: GameData = {};

  // Restore player
  if (normalizedData.player) {
    const playerEntity = normalizedData.entities[normalizedData.player];
    result.player = playerEntity ? (restoreEntityReferences(playerEntity, normalizedData.entities) as Entity) : null;
  } else {
    result.player = null;
  }

  // Restore room
  if (normalizedData.room) {
    const roomEntity = normalizedData.entities[normalizedData.room];
    result.room = roomEntity ? (restoreEntityReferences(roomEntity, normalizedData.entities) as Entity) : null;
  } else {
    result.room = null;
  }

  // Restore chat messages
  result.chatMessages = (normalizedData.chatMessages || []).map(id => normalizedData.entities[id]).filter(Boolean);

  // Restore game log
  result.gameLog = (normalizedData.gameLog || []).map(id => normalizedData.entities[id]).filter(Boolean);

  return result;
}

/**
 * Updates normalized game data with new entities
 * @param normalizedData Existing normalized data
 * @param newEntities New entities to add/update
 * @returns Updated normalized data
 */
export function updateNormalizedData(normalizedData: NormalizedGameData, newEntities: EntityMap): NormalizedGameData {
  return {
    ...normalizedData,
    entities: mergeEntityMaps(normalizedData.entities, newEntities),
  };
}

/**
 * Gets a subset of entities by type from normalized data
 * @param normalizedData Normalized game data
 * @param type Entity type to filter by
 * @returns Array of entities of the specified type
 */
export function getEntitiesByType(normalizedData: NormalizedGameData, type: string): Entity[] {
  return Object.values(normalizedData.entities).filter(entity => entity.type === type);
}

/**
 * Gets entities by IDs from normalized data
 * @param normalizedData Normalized game data
 * @param ids Array of entity IDs
 * @returns Array of entities
 */
export function getEntitiesByIds(normalizedData: NormalizedGameData, ids: string[]): Entity[] {
  return ids.map(id => normalizedData.entities[id]).filter(Boolean);
}

/**
 * Removes entities by IDs from normalized data
 * @param normalizedData Normalized game data
 * @param ids Array of entity IDs to remove
 * @returns Updated normalized data
 */
export function removeEntitiesFromNormalizedData(
  normalizedData: NormalizedGameData,
  ids: string[]
): NormalizedGameData {
  const updatedEntities = { ...normalizedData.entities };

  ids.forEach(id => {
    delete updatedEntities[id];
  });

  return {
    ...normalizedData,
    entities: updatedEntities,
  };
}
