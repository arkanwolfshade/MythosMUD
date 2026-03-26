import type { HealthStatus, HealthTier } from '../../../types/health';
import type { Player } from '../types';

/** Higher = worse. Aligned with HealthMeter tiers (vigorous ok, steady caution, etc.). */
function getDpSeverity(tier: HealthTier | undefined) {
  switch (tier) {
    case 'vigorous':
      return 1;
    case 'steady':
      return 2;
    case 'wounded':
      return 3;
    case 'critical':
      return 4;
    case 'incapacitated':
      return 4;
    default:
      return null;
  }
}

function getMpSeverity(player: Player | null) {
  const stats = player?.stats;
  if (!stats) return null;

  const mpCurrent = stats.magic_points;
  const mpMax = stats.max_magic_points;
  if (mpCurrent === undefined) return null;
  if (mpMax === undefined) return null;
  if (mpMax <= 0) return null;

  const ratio = mpCurrent / mpMax;
  if (ratio >= 0.75) return 1;
  if (ratio >= 0.45) return 2;
  return 3;
}

/**
 * Border + outer glow only (no transform / border-width animation) so the panel does not shift.
 * Severity is max(DP, MP): steady DP cannot be overridden by "high" MP alone.
 */
function getOutlineClassesForWorstSeverity(worst: number) {
  if (worst <= 0) return '';
  if (worst === 1) {
    return 'border-2 border-emerald-500/90 animate-mythos-glow-emerald';
  }
  if (worst === 2) {
    return 'border-2 border-amber-400/90 animate-mythos-glow-amber';
  }
  if (worst === 3) {
    return 'border-2 border-orange-500/90 animate-mythos-glow-orange';
  }
  return 'border-2 border-rose-600/90 animate-mythos-glow-danger';
}

export function getCharacterInfoPanelOutlineClassName(
  healthStatus: HealthStatus | null,
  player: Player | null
): string {
  const dpSev = getDpSeverity(healthStatus?.tier);
  const mpSev = getMpSeverity(player);
  const scores = [dpSev, mpSev].filter((s): s is number => s !== null);
  if (scores.length === 0) return '';
  const worst = Math.max(...scores);
  return getOutlineClassesForWorstSeverity(worst);
}

/**
 * Game Info frame accent when the character is in combat (server-authoritative flag).
 * Glow-only animation; fixed border width.
 */
export function getGameInfoPanelCombatClassName(inCombat: boolean): string {
  if (!inCombat) return '';
  return 'border-2 border-orange-500/90 animate-mythos-glow-combat';
}
