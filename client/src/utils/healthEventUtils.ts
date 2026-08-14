import type { HealthStatus } from '../types/health';
import { determineDpTier } from '../types/health';

const DEFAULT_MAX_DP = 100;

const parseNumber = (value: unknown, fallback: number): number => {
  if (typeof value === 'number' && Number.isFinite(value)) {
    return value;
  }
  if (typeof value === 'string') {
    const parsed = Number.parseFloat(value);
    if (Number.isFinite(parsed)) {
      return parsed;
    }
  }
  return fallback;
};

const toReasonString = (value: unknown): string | undefined => {
  if (typeof value !== 'string') {
    return undefined;
  }
  const trimmed = value.trim();
  return trimmed.length > 0 ? trimmed : undefined;
};

const humanizeReason = (reason?: string): string | undefined => {
  if (!reason) {
    return undefined;
  }
  return reason.replace(/_/g, ' ');
};

const formatSource = (data: Record<string, unknown>): string | undefined => {
  if (typeof data.source_name === 'string' && data.source_name.trim().length > 0) {
    return data.source_name.trim();
  }
  if (typeof data.source === 'string' && data.source.trim().length > 0) {
    return data.source.trim();
  }
  if (typeof data.source_id === 'string' && data.source_id.trim().length > 0) {
    return data.source_id.trim();
  }
  return undefined;
};

const inferReasonFromDelta = (
  reasonFromData: string | undefined,
  damageTaken: number,
  delta: number
): string | undefined => {
  if (reasonFromData) {
    return reasonFromData;
  }
  if (damageTaken > 0 || delta < 0) {
    return 'damage';
  }
  if (damageTaken < 0 || delta > 0) {
    return 'healing';
  }
  return undefined;
};

const resolveInCombat = (data: Record<string, unknown>, previous: HealthStatus | null): boolean | undefined => {
  if (typeof data.in_combat === 'boolean') {
    return data.in_combat;
  }
  return typeof previous?.inCombat === 'boolean' ? previous.inCombat : undefined;
};

function readDpField(data: Record<string, unknown>, keys: string[], fallback: number): number {
  for (const key of keys) {
    if (data[key] !== undefined && data[key] !== null) {
      return parseNumber(data[key], fallback);
    }
  }
  return fallback;
}

function parseHealthEventNumbers(
  previous: HealthStatus | null,
  data: Record<string, unknown>
): { oldDp: number; newDp: number; delta: number; effectiveMax: number; damageTaken: number } {
  const oldDp = readDpField(data, ['old_dp', 'oldDp'], previous?.current ?? 0);
  const newDp = readDpField(data, ['new_dp', 'newDp'], oldDp);
  const maxDp = readDpField(data, ['max_dp', 'maxDp'], previous?.max ?? DEFAULT_MAX_DP);
  const effectiveMax = maxDp > 0 ? maxDp : DEFAULT_MAX_DP;
  return {
    oldDp,
    newDp,
    delta: newDp - oldDp,
    effectiveMax,
    damageTaken: readDpField(data, ['damage_taken', 'damageTaken'], 0),
  };
}

export const buildHealthStatusFromEvent = (
  previous: HealthStatus | null,
  data: Record<string, unknown>,
  timestamp: string
): { status: HealthStatus; delta: number } => {
  const { newDp, delta, effectiveMax, damageTaken } = parseHealthEventNumbers(previous, data);
  const computedReason = inferReasonFromDelta(toReasonString(data.reason), damageTaken, delta);
  const posture = typeof data.posture === 'string' ? data.posture : previous?.posture;

  const status: HealthStatus = {
    current: newDp,
    max: effectiveMax,
    tier: determineDpTier(newDp, effectiveMax),
    posture,
    inCombat: resolveInCombat(data, previous),
    lastChange: { delta, reason: computedReason, timestamp },
  };

  return { status, delta };
};

export const buildHealthChangeMessage = (
  status: HealthStatus,
  delta: number,
  data: Record<string, unknown>
): string => {
  const reason = humanizeReason(status.lastChange?.reason);
  const source = formatSource(data);
  const direction = delta >= 0 ? 'recovers' : 'loses';
  const magnitude = Math.abs(delta);
  const tierLabel = status.tier.charAt(0).toUpperCase() + status.tier.slice(1);
  const fragments = [`Health ${direction} ${magnitude}`];

  if (reason) {
    fragments.push(`(${reason})`);
  }

  if (source) {
    fragments.push(`from ${source}`);
  }

  fragments.push(`→ ${status.current}/${status.max} (${tierLabel})`);

  return fragments.join(' ');
};

export const HEALTH_LOG_TAGS = ['health'];
