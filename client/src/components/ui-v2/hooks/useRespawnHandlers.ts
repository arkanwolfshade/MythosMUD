// Respawn handlers hook
// Extracted from GameClientV2Container to reduce complexity

import { useCallback } from 'react';
import { isApiErrorWithDetail, isRespawnApiResponse, type RespawnApiResponse } from '../../../utils/apiTypeGuards';
import { API_V1_BASE } from '../../../utils/config';
import { logger } from '../../../utils/logger';
import type { GameEvent } from '../eventHandlers/types';
import type { ChatMessage, Player } from '../types';
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

function appendChatError(setGameState: React.Dispatch<React.SetStateAction<GameState>>, text: string): void {
  const errorMessage: ChatMessage = sanitizeChatMessageForState({
    text,
    timestamp: new Date().toISOString(),
    messageType: 'error',
    isHtml: false,
  });
  setGameState(prev => ({ ...prev, messages: [...prev.messages, errorMessage] }));
}

async function postRespawn(
  authToken: string,
  path: string
): Promise<{ ok: true; raw: unknown } | { ok: false; status: number; raw: unknown }> {
  const response = await fetch(`${API_V1_BASE}${path}`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${authToken}`,
    },
  });
  const raw: unknown = await response.json();
  if (!response.ok) {
    return { ok: false, status: response.status, raw };
  }
  return { ok: true, raw };
}

function apiErrorDetail(raw: unknown): string {
  return isApiErrorWithDetail(raw) && raw.detail ? raw.detail : 'Unknown error';
}

function applyDeliriumRespawnSuccess(
  appendRespawnEvent: (event: GameEvent) => void,
  raw: RespawnApiResponse,
  setIsDelirious: (v: boolean) => void,
  setIsDeliriumRespawning: (v: boolean) => void
): void {
  setIsDeliriumRespawning(false);
  setIsDelirious(false);
  const playerData = raw.player as Record<string, unknown>;
  const normalizedPlayer = {
    ...(raw.player as object),
    stats: {
      ...(playerData?.stats as object),
      lucidity: playerData?.lucidity,
      current_dp: playerData?.dp,
    },
  } as Player;

  appendRespawnEvent({
    event_type: 'player_delirium_respawned',
    timestamp: new Date().toISOString(),
    sequence_number: 0,
    data: {
      player: normalizedPlayer,
      room: raw.room,
      message: raw.message ?? 'You have been restored to lucidity and returned to the Sanitarium',
    },
  });
}

function applyDeathRespawnSuccess(params: UseRespawnHandlersParams, raw: RespawnApiResponse): void {
  const playerObj = raw.player as Record<string, unknown> | undefined;
  const normalizedPlayer = {
    ...(raw.player as object),
    stats: {
      ...(playerObj?.stats as object),
      current_dp: playerObj?.dp ?? (playerObj?.stats as Record<string, unknown>)?.current_dp,
    },
  } as Player;

  params.appendRespawnEvent({
    event_type: 'player_respawned',
    timestamp: new Date().toISOString(),
    sequence_number: 0,
    data: {
      player: normalizedPlayer,
      room: raw.room,
      message: 'You feel a chilling wind as your form reconstitutes in Arkham General Hospital...',
    },
  });

  params.setIsDead(false);
  params.setIsMortallyWounded(false);
  params.setIsRespawning(false);
  params.setHasRespawned(true);
}

async function runDeliriumRespawn(params: UseRespawnHandlersParams): Promise<void> {
  const { authToken, setGameState, setIsDelirious, setIsDeliriumRespawning, appendRespawnEvent } = params;
  logger.info('GameClientV2Container', 'Delirium respawn requested');
  setIsDeliriumRespawning(true);

  try {
    const result = await postRespawn(authToken, '/api/players/respawn-delirium');
    if (!result.ok) {
      logger.error('GameClientV2Container', 'Delirium respawn failed', {
        status: result.status,
        error: result.raw,
      });
      appendChatError(setGameState, `Delirium respawn failed: ${apiErrorDetail(result.raw)}`);
      setIsDeliriumRespawning(false);
      return;
    }
    if (!isRespawnApiResponse(result.raw)) {
      setIsDeliriumRespawning(false);
      return;
    }
    logger.info('GameClientV2Container', 'Delirium respawn successful', {
      room: result.raw.room,
      player: result.raw.player,
    });
    applyDeliriumRespawnSuccess(appendRespawnEvent, result.raw, setIsDelirious, setIsDeliriumRespawning);
  } catch (error) {
    logger.error('GameClientV2Container', 'Error calling delirium respawn API', { error });
    appendChatError(setGameState, 'Failed to respawn from delirium due to network error. Please try again.');
    setIsDeliriumRespawning(false);
  }
}

async function runDeathRespawn(params: UseRespawnHandlersParams): Promise<void> {
  const { authToken, setGameState, setIsRespawning } = params;
  logger.info('GameClientV2Container', 'Respawn requested');
  setIsRespawning(true);

  try {
    const result = await postRespawn(authToken, '/api/players/respawn');
    if (!result.ok) {
      logger.error('GameClientV2Container', 'Respawn failed', { status: result.status, error: result.raw });
      appendChatError(setGameState, `Respawn failed: ${apiErrorDetail(result.raw)}`);
      setIsRespawning(false);
      return;
    }
    if (!isRespawnApiResponse(result.raw)) {
      setIsRespawning(false);
      return;
    }
    logger.info('GameClientV2Container', 'Respawn successful', { room: result.raw.room, player: result.raw.player });
    applyDeathRespawnSuccess(params, result.raw);
  } catch (error) {
    logger.error('GameClientV2Container', 'Error calling respawn API', { error });
    appendChatError(setGameState, 'Failed to respawn due to network error. Please try again.');
    setIsRespawning(false);
  }
}

export const useRespawnHandlers = (params: UseRespawnHandlersParams) => {
  const handleDeliriumRespawn = useCallback(() => runDeliriumRespawn(params), [params]);
  const handleRespawn = useCallback(() => runDeathRespawn(params), [params]);
  return { handleRespawn, handleDeliriumRespawn };
};
