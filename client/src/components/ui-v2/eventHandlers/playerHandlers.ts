// Player-related event handlers
// As documented in "Player State Management" - Dr. Armitage, 1928

import { determineHealthTier } from '../../../types/health';
import { buildHealthStatusFromEvent } from '../../../utils/healthEventUtils';
import { logger } from '../../../utils/logger';
import type { Player } from '../types';
import type { EventHandler, GameStateUpdates } from './types';

export const handlePlayerEnteredGame: EventHandler = (event, _context, appendMessage) => {
  const playerName = event.data?.player_name as string | undefined;
  if (playerName && typeof playerName === 'string' && playerName.trim()) {
    appendMessage({
      text: `${playerName} has entered the game.`,
      timestamp: event.timestamp,
      isHtml: false,
      messageType: 'system',
      channel: 'game',
      type: 'system',
    });
  }
};

export const handlePlayerEntered: EventHandler = (event, _context, appendMessage) => {
  const playerName = event.data.player_name as string;
  const messageText = event.data?.message as string;
  if (messageText && playerName) {
    appendMessage({
      text: messageText,
      timestamp: event.timestamp,
      isHtml: false,
      messageType: 'system',
      channel: 'game',
      type: 'system',
    });
  }
};

export const handlePlayerLeftGame: EventHandler = (event, _context, appendMessage) => {
  const playerName = event.data?.player_name as string;
  if (playerName) {
    appendMessage({
      text: `${playerName} has left the game.`,
      timestamp: event.timestamp,
      isHtml: false,
      messageType: 'system',
      channel: 'game',
      type: 'system',
    });
  }
};

export const handlePlayerLeft: EventHandler = (event, _context, appendMessage) => {
  const messageText = event.data?.message as string;
  if (messageText) {
    appendMessage({
      text: messageText,
      timestamp: event.timestamp,
      isHtml: false,
      messageType: 'system',
      channel: 'game',
      type: 'system',
    });
  }
};

export const handlePlayerDied: EventHandler = (event, context) => {
  const deathData = event.data as { death_location?: string; room_id?: string; [key: string]: unknown };
  const extractedDeathLocation = deathData.death_location || deathData.room_id || 'Unknown Location';
  context.setDeathLocation(extractedDeathLocation);
  context.setIsDead(true);
};

export const handlePlayerRespawned: EventHandler = (event, context) => {
  const respawnData = event.data as {
    player?: Player;
    respawn_room_id?: string;
    old_dp?: number;
    new_dp?: number;
    message?: string;
    [key: string]: unknown;
  };

  context.setIsDead(false);
  context.setIsMortallyWounded(false);
  context.setIsRespawning(false);

  const updates: GameStateUpdates = {};

  if (respawnData.player) {
    updates.player = respawnData.player as Player;
    // Update health status from player data
    if (respawnData.player.stats?.current_dp !== undefined) {
      const playerStats = respawnData.player.stats;
      const currentHealth = playerStats.current_dp;
      const maxHealth = playerStats.max_health ?? 100;
      const healthStatusUpdate = {
        current: currentHealth,
        max: maxHealth,
        tier: determineHealthTier(currentHealth, maxHealth),
        posture: playerStats.position,
        inCombat: respawnData.player.in_combat ?? false,
        lastChange: {
          delta: currentHealth - (context.healthStatusRef.current?.current ?? 0),
          reason: 'respawn',
          timestamp: event.timestamp,
        },
      };
      context.setHealthStatus(healthStatusUpdate);
    }
  }

  if (respawnData.message) {
    // This will be handled by the caller via appendMessage if needed
  }

  return updates;
};

export const handlePlayerDeliriumRespawned: EventHandler = (event, context) => {
  const respawnData = event.data as {
    player?: Player;
    respawn_room_id?: string;
    old_lucidity?: number;
    new_lucidity?: number;
    message?: string;
    [key: string]: unknown;
  };

  context.setIsDelirious(false);
  context.setIsDeliriumRespawning(false);

  const updates: GameStateUpdates = {};

  if (respawnData.player) {
    updates.player = respawnData.player as Player;
    // Update lucidity status from player data
    if (respawnData.player.stats?.lucidity !== undefined) {
      const playerStats = respawnData.player.stats;
      const currentLucidity = playerStats.lucidity;
      if (context.lucidityStatusRef.current) {
        context.setLucidityStatus({
          ...context.lucidityStatusRef.current,
          current: currentLucidity,
        });
      }
    }
  }

  return updates;
};

export const handlePlayerUpdate: EventHandler = (event, context) => {
  const playerData = event.data as { in_combat?: boolean; [key: string]: unknown };
  if (context.currentPlayerRef.current && playerData.in_combat !== undefined) {
    return {
      player: {
        ...context.currentPlayerRef.current,
        in_combat: playerData.in_combat,
      },
    };
  }
};

export const handlePlayerDpUpdated: EventHandler = (event, context) => {
  logger.info('playerHandlers', 'Received player_dp_updated event', {
    old_dp: event.data.old_dp,
    new_dp: event.data.new_dp,
    max_dp: event.data.max_dp,
    damage_taken: event.data.damage_taken,
  });

  const { status: updatedHealthStatus } = buildHealthStatusFromEvent(
    context.healthStatusRef.current,
    event.data,
    event.timestamp
  );

  context.setHealthStatus(updatedHealthStatus);

  if (context.currentPlayerRef.current) {
    return {
      player: {
        ...context.currentPlayerRef.current,
        stats: {
          ...context.currentPlayerRef.current.stats,
          current_dp: updatedHealthStatus.current,
          max_health: updatedHealthStatus.max,
          lucidity: context.currentPlayerRef.current.stats?.lucidity ?? 0,
        },
      },
    };
  }
};
