import type { LucidityStatus, LucidityTier } from '../types/lucidity';

const DEFAULT_MAX_LCD = 100;

const sanitizeTier = (value: unknown, fallback: LucidityTier): LucidityTier => {
  if (typeof value !== 'string') {
    return fallback;
  }

  const normalized = value.toLowerCase() as LucidityTier;
  const tiers: LucidityTier[] = ['lucid', 'uneasy', 'fractured', 'deranged', 'catatonic'];
  return tiers.includes(normalized) ? normalized : fallback;
};

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

const resolveMaxLucidity = (
  data: Record<string, unknown>,
  previous: LucidityStatus | null,
  playerMaxLucidity?: number
): number => {
  const fallbackMax = previous?.max ?? playerMaxLucidity ?? DEFAULT_MAX_LCD;
  return parseNumber(data.max_lcd ?? data.maxLcd, fallbackMax);
};

const resolveCurrentRawValue = (data: Record<string, unknown>, previousCurrent: number, delta: number): unknown => {
  if (data.current_lcd != null) {
    return data.current_lcd;
  }
  if (data.currentLcd != null) {
    return data.currentLcd;
  }
  return previousCurrent + delta;
};

const resolveCurrentLucidity = (
  data: Record<string, unknown>,
  previous: LucidityStatus | null,
  delta: number,
  max: number
): number => {
  const previousCurrent = previous?.current ?? 0;
  const rawCurrent = resolveCurrentRawValue(data, previousCurrent, delta);
  const parsedCurrent = parseNumber(rawCurrent, previousCurrent);
  if (max > 0 && parsedCurrent > max) {
    return max;
  }
  return parsedCurrent;
};

const resolveLiabilities = (data: Record<string, unknown>, previous: LucidityStatus | null): string[] => {
  const liabilitiesSource = Array.isArray(data.liabilities) ? data.liabilities : (previous?.liabilities ?? []);
  return liabilitiesSource.map(entry => String(entry)).filter(Boolean);
};

const resolveOptionalText = (value: unknown): string | undefined => {
  return typeof value === 'string' ? value : undefined;
};

export const buildLucidityStatus = (
  previous: LucidityStatus | null,
  data: Record<string, unknown>,
  timestamp: string,
  playerMaxLucidity?: number
): { status: LucidityStatus; delta: number } => {
  const delta = parseNumber(data.delta, 0);
  const max = resolveMaxLucidity(data, previous, playerMaxLucidity);
  const current = resolveCurrentLucidity(data, previous, delta, max);
  const tier = sanitizeTier(data.tier, previous?.tier ?? 'lucid');
  const liabilities = resolveLiabilities(data, previous);
  const reason = resolveOptionalText(data.reason);
  const source = resolveOptionalText(data.source);

  const status: LucidityStatus = {
    current,
    max: max > 0 ? max : DEFAULT_MAX_LCD,
    tier,
    liabilities,
    lastChange: {
      delta,
      reason,
      source,
      timestamp,
    },
  };

  return { status, delta };
};

export const buildLucidityChangeMessage = (
  status: LucidityStatus,
  delta: number,
  data: Record<string, unknown>
): string => {
  const reason = typeof data.reason === 'string' ? data.reason.replace(/_/g, ' ') : undefined;
  const source = typeof data.source === 'string' ? data.source : undefined;
  const tier = status.tier.charAt(0).toUpperCase() + status.tier.slice(1);
  const direction = delta >= 0 ? 'gains' : 'loses';
  const magnitude = Math.abs(delta);
  const fragments = [`Lucidity ${direction} ${magnitude}`];

  if (reason) {
    fragments.push(`(${reason})`);
  }

  if (source) {
    fragments.push(`due to ${source}`);
  }

  fragments.push(`→ ${status.current}/${status.max} (${tier})`);

  return fragments.join(' ');
};
