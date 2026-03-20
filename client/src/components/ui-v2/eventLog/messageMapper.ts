// Pure helpers: combat log lines and player stat merges from WebSocket payloads.
// Keep formatting here so projector handlers stay thin and testable.

import type { Player } from '../types';

export function formatNpcAttackedLine(d: Record<string, unknown>): string {
  const actionType = d.action_type as string | undefined;
  const npcName = (d.npc_name || d.target_name) as string | undefined;
  const damage = d.damage as number | undefined;
  const targetCurrentDp = d.target_current_dp as number | undefined;
  const targetMaxDp = d.target_max_dp as number | undefined;
  const verb = actionType === 'auto_attack' ? 'attack' : actionType || 'attack';
  let text = `You ${verb} ${npcName} for ${damage} damage.`;
  if (targetCurrentDp !== undefined && targetMaxDp !== undefined) {
    text += ` (${targetCurrentDp}/${targetMaxDp} DP)`;
  }
  return text;
}

export function formatPlayerAttackedLine(d: Record<string, unknown>): string {
  const actionType = d.action_type as string | undefined;
  const attackerName = d.attacker_name as string | undefined;
  const damage = d.damage as number | undefined;
  const targetCurrentDp = d.target_current_dp as number | undefined;
  const targetMaxDp = d.target_max_dp as number | undefined;
  const verb = actionType === 'auto_attack' ? 'attacks' : actionType || 'attacks';
  let text = `${attackerName} ${verb} you for ${damage} damage.`;
  if (targetCurrentDp !== undefined && targetMaxDp !== undefined) {
    text += ` (${targetCurrentDp}/${targetMaxDp} DP)`;
  }
  return text;
}

/**
 * When the server includes the victim's DP on `player_attacked`, merge into local player so the
 * Character Panel matches the Game Info line (single projector source of truth).
 */
export function mergePlayerDpFromPlayerAttackedPayload(
  prevPlayer: Player | null | undefined,
  d: Record<string, unknown>
): Player | null {
  const targetCurrentDp = d.target_current_dp as number | undefined;
  const targetMaxDp = d.target_max_dp as number | undefined;
  if (!prevPlayer?.stats || targetCurrentDp === undefined) {
    return null;
  }
  return {
    ...prevPlayer,
    stats: {
      ...prevPlayer.stats,
      current_dp: targetCurrentDp,
      ...(targetMaxDp !== undefined && { max_dp: targetMaxDp }),
    },
  };
}
