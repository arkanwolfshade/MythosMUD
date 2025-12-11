// Respawn handlers hook
// Extracted from GameClientV2Container to reduce complexity

import { useCallback } from 'react';
import { logger } from '../../../utils/logger';
import { sanitizeChatMessageForState } from '../utils/messageUtils';
import type { ChatMessage, Player, Room } from '../types';
import type { GameState } from '../utils/stateUpdateUtils';

interface UseRespawnHandlersParams {
  authToken: string;
  setGameState: React.Dispatch<React.SetStateAction<GameState>>;
  setIsDead: (dead: boolean) => void;
  setIsMortallyWounded: (wounded: boolean) => void;
  setIsRespawning: (respawning: boolean) => void;
  setIsDelirious: (delirious: boolean) => void;
  setIsDeliriumRespawning: (respawning: boolean) => void;
}

export const useRespawnHandlers = ({
  authToken,
  setGameState,
  setIsDead,
  setIsMortallyWounded,
  setIsRespawning,
  setIsDelirious,
  setIsDeliriumRespawning,
}: UseRespawnHandlersParams) => {
  const handleDeliriumRespawn = useCallback(async () => {
    logger.info('GameClientV2Container', 'Delirium respawn requested');
    setIsDeliriumRespawning(true);

    try {
      const response = await fetch('/api/players/respawn-delirium', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${authToken}`,
        },
      });

      if (!response.ok) {
        const errorData = await response.json();
        logger.error('GameClientV2Container', 'Delirium respawn failed', {
          status: response.status,
          error: errorData,
        });

        const errorMessage: ChatMessage = sanitizeChatMessageForState({
          text: `Delirium respawn failed: ${errorData.detail || 'Unknown error'}`,
          timestamp: new Date().toISOString(),
          messageType: 'error',
          isHtml: false,
        });

        setGameState(prev => ({
          ...prev,
          messages: [...prev.messages, errorMessage],
        }));

        setIsDeliriumRespawning(false);
        return;
      }

      const respawnData = await response.json();
      logger.info('GameClientV2Container', 'Delirium respawn successful', {
        room: respawnData.room,
        player: respawnData.player,
      });

      setIsDeliriumRespawning(false);
      setIsDelirious(false);

      // Update game state with respawned player data
      setGameState(prev => ({
        ...prev,
        player: {
          ...prev.player,
          ...respawnData.player,
          stats: {
            ...prev.player?.stats,
            lucidity: respawnData.player.lucidity,
            current_dp: respawnData.player.dp,
          },
        } as Player,
        room: respawnData.room as Room,
      }));

      const respawnMessage: ChatMessage = sanitizeChatMessageForState({
        text: respawnData.message || 'You have been restored to lucidity and returned to the Sanitarium',
        timestamp: new Date().toISOString(),
        messageType: 'system',
        isHtml: false,
      });

      setGameState(prev => ({
        ...prev,
        messages: [...prev.messages, respawnMessage],
      }));
    } catch (error) {
      logger.error('GameClientV2Container', 'Error calling delirium respawn API', { error });
      const errorMessage: ChatMessage = sanitizeChatMessageForState({
        text: 'Failed to respawn from delirium due to network error. Please try again.',
        timestamp: new Date().toISOString(),
        messageType: 'error',
        isHtml: false,
      });

      setGameState(prev => ({
        ...prev,
        messages: [...prev.messages, errorMessage],
      }));

      setIsDeliriumRespawning(false);
    }
  }, [authToken, setGameState, setIsDelirious, setIsDeliriumRespawning]);

  const handleRespawn = useCallback(async () => {
    logger.info('GameClientV2Container', 'Respawn requested');
    setIsRespawning(true);

    try {
      const response = await fetch('/api/players/respawn', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${authToken}`,
        },
      });

      if (!response.ok) {
        const errorData = await response.json();
        logger.error('GameClientV2Container', 'Respawn failed', {
          status: response.status,
          error: errorData,
        });

        const errorMessage: ChatMessage = sanitizeChatMessageForState({
          text: `Respawn failed: ${errorData.detail || 'Unknown error'}`,
          timestamp: new Date().toISOString(),
          messageType: 'error',
          isHtml: false,
        });

        setGameState(prev => ({
          ...prev,
          messages: [...prev.messages, errorMessage],
        }));

        setIsRespawning(false);
        return;
      }

      const respawnData = await response.json();
      logger.info('GameClientV2Container', 'Respawn successful', {
        room: respawnData.room,
        player: respawnData.player,
      });

      setIsDead(false);
      setIsMortallyWounded(false);
      setIsRespawning(false);

      setGameState(prev => ({
        ...prev,
        player: {
          ...prev.player,
          ...respawnData.player,
          stats: {
            ...prev.player?.stats,
            current_dp: respawnData.player.dp,
          },
        } as Player,
        room: respawnData.room as Room,
      }));

      const respawnMessage: ChatMessage = sanitizeChatMessageForState({
        text: 'You feel a chilling wind as your form reconstitutes in Arkham General Hospital...',
        timestamp: new Date().toISOString(),
        messageType: 'system',
        isHtml: false,
      });

      setGameState(prev => ({
        ...prev,
        messages: [...prev.messages, respawnMessage],
      }));
    } catch (error) {
      logger.error('GameClientV2Container', 'Error calling respawn API', { error });

      const errorMessage: ChatMessage = sanitizeChatMessageForState({
        text: 'Failed to respawn due to network error. Please try again.',
        timestamp: new Date().toISOString(),
        messageType: 'error',
        isHtml: false,
      });

      setGameState(prev => ({
        ...prev,
        messages: [...prev.messages, errorMessage],
      }));

      setIsRespawning(false);
    }
  }, [authToken, setGameState, setIsDead, setIsMortallyWounded, setIsRespawning]);

  return { handleRespawn, handleDeliriumRespawn };
};
