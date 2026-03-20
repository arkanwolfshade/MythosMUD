export type HealthTier = 'vigorous' | 'steady' | 'wounded' | 'critical' | 'incapacitated';

export interface HealthChange {
  delta: number;
  reason?: string;
  timestamp?: string;
}

export interface HealthStatus {
  current: number;
  max: number;
  tier: HealthTier;
  lastChange?: HealthChange;
  posture?: string;
  inCombat?: boolean;
}

export interface HealthMeterProps {
  status: HealthStatus | null;
  className?: string;
}

/**
 * Deterministic tier calculation based on current percent of max DP.
 * Keep thresholds aligned with encounter design noted in the Pnakotic combat charts.
 * DP <= 0 is incapacitated (prone, cannot act); 1%..19% is critical.
 */
export const determineDpTier = (current: number, max: number): HealthTier => {
  if (max <= 0) {
    return 'critical';
  }

  if (current <= 0) {
    return 'incapacitated';
  }

  const ratio = current / max;

  if (ratio >= 0.75) {
    return 'vigorous';
  }

  if (ratio >= 0.45) {
    return 'steady';
  }

  if (ratio >= 0.2) {
    return 'wounded';
  }

  return 'critical';
};

/**
 * Pure UI projection: Character Panel health bar from authoritative player stats.
 * Single place for health meter inputs (see client docs: client-message-handling.md).
 */
export function deriveHealthStatusFromPlayer(
  player:
    | {
        stats?: { current_dp?: number; max_dp?: number; position?: string };
        in_combat?: boolean;
      }
    | null
    | undefined,
  previousLastChange: HealthChange | undefined
): HealthStatus | null {
  if (!player?.stats) return null;
  const stats = player.stats;
  const currentDp = stats.current_dp;
  const maxDp = stats.max_dp ?? 100;
  if (currentDp === undefined) return null;
  return {
    current: currentDp,
    max: maxDp,
    tier: determineDpTier(currentDp, maxDp),
    posture: stats.position,
    inCombat: player.in_combat ?? false,
    lastChange: previousLastChange,
  };
}
