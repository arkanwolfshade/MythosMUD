// Pure helpers: combat log lines and player stat merges from WebSocket payloads.
// Keep formatting here so projector handlers stay thin and testable.

import { isNpcDisposition, npcCategory } from '../../../types/messageCategory';
import type { Player } from '../types';
import { buildLine, type SegmentPart } from '../utils/messageSegments';

/**
 * An NPC's name as a line part: styled by `npc.<disposition>` when the server sent a disposition (#1025),
 * otherwise plain text. The server owns the tag; phantoms and real hostiles arrive tagged the same.
 */
function npcNamePart(name: unknown, disposition: unknown): SegmentPart {
  const text = String(name);
  return isNpcDisposition(disposition) ? { text, category: npcCategory(disposition) } : text;
}

function dpSuffix(currentDp: number | undefined, maxDp: number | undefined): string {
  return currentDp !== undefined && maxDp !== undefined ? ` (${currentDp}/${maxDp} DP)` : '';
}

/**
 * Spell / steal-life / other non-melee NPC damage: server sends npc_took_damage with current_dp after hit.
 * Aligns Game Info line with melee (npc_attacked) which uses target_current_dp / target_max_dp.
 * Empty when the payload lacks a name or damage.
 */
export function npcTookDamageParts(d: Record<string, unknown>): SegmentPart[] {
  const npcName = d.npc_name as string | undefined;
  const damage = d.damage as number | undefined;
  if (!npcName || damage === undefined) {
    return [];
  }
  const dp = dpSuffix(d.current_dp as number | undefined, d.max_dp as number | undefined);
  return [`Dealt ${damage} damage to `, npcNamePart(npcName, d.npc_disposition), `.${dp}`];
}

export function npcAttackedParts(d: Record<string, unknown>): SegmentPart[] {
  const actionType = d.action_type as string | undefined;
  const npcName = (d.npc_name || d.target_name) as string | undefined;
  const verb = actionType === 'auto_attack' ? 'attack' : actionType || 'attack';
  const dp = dpSuffix(d.target_current_dp as number | undefined, d.target_max_dp as number | undefined);
  return [
    `You ${verb} `,
    npcNamePart(npcName, d.npc_disposition),
    ` for ${d.damage as number | undefined} damage.${dp}`,
  ];
}

export function playerAttackedParts(d: Record<string, unknown>): SegmentPart[] {
  const actionType = d.action_type as string | undefined;
  const verb = actionType === 'auto_attack' ? 'attacks' : actionType || 'attacks';
  const dp = dpSuffix(d.target_current_dp as number | undefined, d.target_max_dp as number | undefined);
  return [
    npcNamePart(d.attacker_name, d.attacker_disposition),
    ` ${verb} you for ${d.damage as number | undefined} damage.${dp}`,
  ];
}

export const formatNpcTookDamageLine = (d: Record<string, unknown>): string => buildLine(npcTookDamageParts(d)).text;
export const formatNpcAttackedLine = (d: Record<string, unknown>): string => buildLine(npcAttackedParts(d)).text;
export const formatPlayerAttackedLine = (d: Record<string, unknown>): string => buildLine(playerAttackedParts(d)).text;

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
