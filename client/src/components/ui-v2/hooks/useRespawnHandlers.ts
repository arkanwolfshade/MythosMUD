// Respawn handlers hook
// Extracted from GameClientV2Container to reduce complexity

import { useCallback } from 'react';
import { isApiErrorWithDetail, isRespawnApiResponse } from '../../../utils/apiTypeGuards';
import { API_V1_BASE } from '../../../utils/config';
import { logger } from '../../../utils/logger';
import type { GameEvent } from '../eventHandlers/types';
import { buildLocalMessageEvent } from '../eventLog/projectorMessageUtils';

interface UseRespawnHandlersParams {
  authToken: string;
  setIsRespawning: (respawning: boolean) => void;
  setIsDeliriumRespawning: (respawning: boolean) => void;
  /** Routes local error messages through the event log; the server pushes player_respawned /
   *  player_delirium_respawned itself on success -- see .cursor/rules/server-authority.mdc. */
  appendLocalEvent: (event: GameEvent) => void;
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

async function runDeliriumRespawn(params: UseRespawnHandlersParams): Promise<void> {
  const { authToken, appendLocalEvent, setIsDeliriumRespawning } = params;
  logger.info('GameClientV2Container', 'Delirium respawn requested');
  setIsDeliriumRespawning(true);

  try {
    const result = await postRespawn(authToken, '/api/players/respawn-delirium');
    if (!result.ok) {
      logger.error('GameClientV2Container', 'Delirium respawn failed', {
        status: result.status,
        error: result.raw,
      });
      appendLocalEvent(buildLocalMessageEvent(`Delirium respawn failed: ${apiErrorDetail(result.raw)}`, 'error'));
      setIsDeliriumRespawning(false);
      return;
    }
    if (!isRespawnApiResponse(result.raw)) {
      setIsDeliriumRespawning(false);
      return;
    }
    // Success: the server pushes player_delirium_respawned over the websocket (player, room,
    // message). No client-side event fabrication -- see the projector's player_respawned handler.
    logger.info('GameClientV2Container', 'Delirium respawn successful', {
      room: result.raw.room,
      player: result.raw.player,
    });
    setIsDeliriumRespawning(false);
  } catch (error) {
    logger.error('GameClientV2Container', 'Error calling delirium respawn API', { error });
    appendLocalEvent(
      buildLocalMessageEvent('Failed to respawn from delirium due to network error. Please try again.', 'error')
    );
    setIsDeliriumRespawning(false);
  }
}

async function runDeathRespawn(params: UseRespawnHandlersParams): Promise<void> {
  const { authToken, appendLocalEvent, setIsRespawning } = params;
  logger.info('GameClientV2Container', 'Respawn requested');
  setIsRespawning(true);

  try {
    const result = await postRespawn(authToken, '/api/players/respawn');
    if (!result.ok) {
      logger.error('GameClientV2Container', 'Respawn failed', { status: result.status, error: result.raw });
      appendLocalEvent(buildLocalMessageEvent(`Respawn failed: ${apiErrorDetail(result.raw)}`, 'error'));
      setIsRespawning(false);
      return;
    }
    if (!isRespawnApiResponse(result.raw)) {
      setIsRespawning(false);
      return;
    }
    // Success: the server pushes player_respawned over the websocket. No client-side fabrication.
    logger.info('GameClientV2Container', 'Respawn successful', { room: result.raw.room, player: result.raw.player });
    setIsRespawning(false);
  } catch (error) {
    logger.error('GameClientV2Container', 'Error calling respawn API', { error });
    appendLocalEvent(buildLocalMessageEvent('Failed to respawn due to network error. Please try again.', 'error'));
    setIsRespawning(false);
  }
}

export const useRespawnHandlers = (params: UseRespawnHandlersParams) => {
  const handleDeliriumRespawn = useCallback(() => runDeliriumRespawn(params), [params]);
  const handleRespawn = useCallback(() => runDeathRespawn(params), [params]);
  return { handleRespawn, handleDeliriumRespawn };
};
