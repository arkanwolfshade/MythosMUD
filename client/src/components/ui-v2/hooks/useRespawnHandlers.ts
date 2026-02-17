// Respawn handlers hook
// Extracted from GameClientV2Container to reduce complexity

import { useCallback } from 'react';
import { isApiErrorWithDetail, isRespawnApiResponse } from '../../../utils/apiTypeGuards';
import { API_V1_BASE } from '../../../utils/config';
import { logger } from '../../../utils/logger';
import type { GameEvent } from '../eventHandlers/types';
import type { ChatMessage, Player, Room } from '../types';
import { sanitizeChatMessageForState } from '../utils/messageUtils';
import type { GameState } from '../utils/stateUpdateUtils';

interface UseRespawnHandlersParams {
  authToken: string;
  setGameState: React.Dispatch<React.SetStateAction<GameState>>;
  setIsDead: (dead: boolean) => void;
  setIsMortallyWounded: (wounded: boolean) => void;
  setIsRespawning: (respawning: boolean) => void;
  setIsDelirious: (delirious: boolean) => void;
  setIsDeliriumRespawning: (respawning: boolean) => void;
  setHasRespawned: (hasRespawned: boolean) => void;
  appendRespawnEvent: (event: GameEvent) => void;
}

export const useRespawnHandlers = ({
  authToken,
  setGameState,
  setIsDead,
  setIsMortallyWounded,
  setIsRespawning,
  setIsDelirious,
  setIsDeliriumRespawning,
  setHasRespawned,
  appendRespawnEvent,
}: UseRespawnHandlersParams) => {
  const handleDeliriumRespawn = useCallback(async () => {
    logger.info('GameClientV2Container', 'Delirium respawn requested');
    setIsDeliriumRespawning(true);

    try {
      const response = await fetch(`${API_V1_BASE}/api/players/respawn-delirium`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${authToken}`,
        },
      });

      if (!response.ok) {
        const rawErr: unknown = await response.json();
        logger.error('GameClientV2Container', 'Delirium respawn failed', {
          status: response.status,
          error: rawErr,
        });
        const detailMsg = isApiErrorWithDetail(rawErr) && rawErr.detail ? rawErr.detail : 'Unknown error';
        const errorMessage: ChatMessage = sanitizeChatMessageForState({
          text: `Delirium respawn failed: ${detailMsg}`,
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

      const raw: unknown = await response.json();
      if (!isRespawnApiResponse(raw)) {
        setIsDeliriumRespawning(false);
        return;
      }
      logger.info('GameClientV2Container', 'Delirium respawn successful', {
        room: raw.room,
        player: raw.player,
      });

      setIsDeliriumRespawning(false);
      setIsDelirious(false);

      // Update game state with respawned player data
      const playerData = raw.player as Record<string, unknown>;
      setGameState(prev => ({
        ...prev,
        player: {
          ...prev.player,
          ...(raw.player as object),
          stats: {
            ...prev.player?.stats,
            lucidity: playerData?.lucidity,
            current_dp: playerData?.dp,
          },
        } as Player,
        room: raw.room as Room,
      }));

      const respawnMessage: ChatMessage = sanitizeChatMessageForState({
        text: raw.message ?? 'You have been restored to lucidity and returned to the Sanitarium',
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
      const response = await fetch(`${API_V1_BASE}/api/players/respawn`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${authToken}`,
        },
      });

      if (!response.ok) {
        const rawErr: unknown = await response.json();
        logger.error('GameClientV2Container', 'Respawn failed', {
          status: response.status,
          error: rawErr,
        });
        const detailMsg = isApiErrorWithDetail(rawErr) && rawErr.detail ? rawErr.detail : 'Unknown error';
        const errorMessage: ChatMessage = sanitizeChatMessageForState({
          text: `Respawn failed: ${detailMsg}`,
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

      const raw: unknown = await response.json();
      if (!isRespawnApiResponse(raw)) {
        setIsRespawning(false);
        return;
      }
      logger.info('GameClientV2Container', 'Respawn successful', {
        room: raw.room,
        player: raw.player,
      });

      const playerObj = raw.player as Record<string, unknown> | undefined;
      // Normalize player so event log has stats.current_dp (API may return .dp at top level).
      const normalizedPlayer = {
        ...(raw.player as object),
        stats: {
          ...(playerObj?.stats as object),
          current_dp: playerObj?.dp ?? (playerObj?.stats as Record<string, unknown>)?.current_dp,
        },
      } as Player;

      // Update player/room first so usePlayerStatusEffects sees new DP before we clear isDead.
      setGameState(prev => ({
        ...prev,
        player: {
          ...prev.player,
          ...(raw.player as object),
          stats: {
            ...prev.player?.stats,
            current_dp: playerObj?.dp,
          },
        } as Player,
        room: raw.room as Room,
      }));

      // Append synthetic event so event-log projection keeps respawned state (stops later events from overwriting).
      appendRespawnEvent({
        event_type: 'player_respawned',
        timestamp: new Date().toISOString(),
        sequence_number: 0,
        data: { player: normalizedPlayer, room: raw.room },
      });

      setIsDead(false);
      setIsMortallyWounded(false);
      setIsRespawning(false);
      setHasRespawned(true);

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
  }, [authToken, setGameState, setIsDead, setIsMortallyWounded, setIsRespawning, setHasRespawned, appendRespawnEvent]);

  return { handleRespawn, handleDeliriumRespawn };
};
