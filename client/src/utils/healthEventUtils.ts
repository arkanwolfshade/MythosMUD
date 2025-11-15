import type { HealthStatus } from '../types/health';
import { determineHealthTier } from '../types/health';

const DEFAULT_MAX_HP = 100;

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

export const buildHealthStatusFromEvent = (
  previous: HealthStatus | null,
  data: Record<string, unknown>,
  timestamp: string
): { status: HealthStatus; delta: number } => {
  const oldHp = parseNumber(data.old_hp ?? data.oldHp ?? previous?.current ?? 0, previous?.current ?? 0);
  const newHp = parseNumber(data.new_hp ?? data.newHp ?? oldHp, oldHp);
  const delta = newHp - oldHp;
  const maxHp = parseNumber(
    data.max_hp ?? data.maxHp ?? previous?.max ?? DEFAULT_MAX_HP,
    previous?.max ?? DEFAULT_MAX_HP
  );
  const reasonFromData = toReasonString(data.reason);
  const damageTaken = parseNumber(data.damage_taken ?? data.damageTaken ?? 0, 0);

  let computedReason = reasonFromData;
  if (!computedReason) {
    if (damageTaken > 0 || delta < 0) {
      computedReason = 'damage';
    } else if (damageTaken < 0 || delta > 0) {
      computedReason = 'healing';
    }
  }

  const posture = typeof data.posture === 'string' ? data.posture : previous?.posture;
  const inCombat =
    typeof data.in_combat === 'boolean'
      ? data.in_combat
      : typeof previous?.inCombat === 'boolean'
        ? previous?.inCombat
        : undefined;

  const status: HealthStatus = {
    current: newHp,
    max: maxHp > 0 ? maxHp : DEFAULT_MAX_HP,
    tier: determineHealthTier(newHp, maxHp > 0 ? maxHp : DEFAULT_MAX_HP),
    posture,
    inCombat,
    lastChange: {
      delta,
      reason: computedReason,
      timestamp,
    },
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
