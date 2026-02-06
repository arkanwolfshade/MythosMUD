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
