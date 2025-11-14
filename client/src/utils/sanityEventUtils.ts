import { HallucinationMessage, RescueState, SanityStatus, SanityTier } from '../types/sanity';

const DEFAULT_MAX_SAN = 100;

const sanitizeTier = (value: unknown, fallback: SanityTier): SanityTier => {
  if (typeof value !== 'string') {
    return fallback;
  }

  const normalized = value.toLowerCase() as SanityTier;
  const tiers: SanityTier[] = ['lucid', 'uneasy', 'fractured', 'deranged', 'catatonic'];
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

export const buildSanityStatus = (
  previous: SanityStatus | null,
  data: Record<string, unknown>,
  timestamp: string
): { status: SanityStatus; delta: number } => {
  const delta = parseNumber(data.delta, 0);
  const current = parseNumber(
    data.current_san ?? data.currentSan ?? (previous?.current ?? 0) + delta,
    previous?.current ?? 0
  );
  const max = parseNumber(data.max_san ?? data.maxSan, previous?.max ?? DEFAULT_MAX_SAN);
  const tier = sanitizeTier(data.tier, previous?.tier ?? 'lucid');
  const liabilitiesSource = Array.isArray(data.liabilities) ? data.liabilities : (previous?.liabilities ?? []);
  const liabilities = liabilitiesSource.map(entry => String(entry)).filter(Boolean);
  const reason = typeof data.reason === 'string' ? data.reason : undefined;
  const source = typeof data.source === 'string' ? data.source : undefined;

  const status: SanityStatus = {
    current,
    max: max > 0 ? max : DEFAULT_MAX_SAN,
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

export const buildSanityChangeMessage = (
  status: SanityStatus,
  delta: number,
  data: Record<string, unknown>
): string => {
  const reason = typeof data.reason === 'string' ? data.reason.replace(/_/g, ' ') : undefined;
  const source = typeof data.source === 'string' ? data.source : undefined;
  const tier = status.tier.charAt(0).toUpperCase() + status.tier.slice(1);
  const direction = delta >= 0 ? 'gains' : 'loses';
  const magnitude = Math.abs(delta);
  const fragments = [`Sanity ${direction} ${magnitude}`];

  if (reason) {
    fragments.push(`(${reason})`);
  }

  if (source) {
    fragments.push(`due to ${source}`);
  }

  fragments.push(`→ ${status.current}/${status.max} (${tier})`);

  return fragments.join(' ');
};

const createHallucinationId = (data: Record<string, unknown>, timestamp: string): string => {
  if (typeof data.id === 'string' && data.id.trim().length > 0) {
    return data.id;
  }
  return `${timestamp}-${Math.random().toString(36).substring(2, 8)}`;
};

export const createHallucinationEntry = (data: Record<string, unknown>, timestamp: string): HallucinationMessage => {
  const title =
    typeof data.title === 'string' && data.title.trim().length > 0
      ? data.title.trim()
      : typeof data.message === 'string' && data.message.trim().length > 0
        ? data.message.trim()
        : 'An impossible vision flickers at the edge of perception.';

  const description =
    typeof data.description === 'string' && data.description.trim().length > 0 ? data.description.trim() : undefined;

  const severityRaw = typeof data.severity === 'string' ? data.severity.toLowerCase() : 'minor';
  const severity = (
    ['minor', 'moderate', 'severe'].includes(severityRaw) ? severityRaw : 'minor'
  ) as HallucinationMessage['severity'];

  const category = typeof data.category === 'string' ? data.category : undefined;

  return {
    id: createHallucinationId(data, timestamp),
    title,
    description,
    severity,
    category,
    timestamp,
  };
};

export const createRescueState = (data: Record<string, unknown>, timestamp: string): RescueState => {
  const statusRaw = typeof data.status === 'string' ? data.status.toLowerCase() : 'idle';
  const validStatuses = ['idle', 'catatonic', 'channeling', 'success', 'failed', 'sanitarium'] as const;
  const status = validStatuses.includes(statusRaw as (typeof validStatuses)[number])
    ? (statusRaw as (typeof validStatuses)[number])
    : 'idle';

  const targetName = typeof data.target_name === 'string' ? data.target_name : undefined;
  const rescuerName = typeof data.rescuer_name === 'string' ? data.rescuer_name : undefined;
  const progress = parseNumber(data.progress, Number.isFinite(data.progress) ? (data.progress as number) : 0);
  const etaSeconds = parseNumber(data.eta_seconds ?? data.etaSeconds, Number.NaN);
  const message = typeof data.message === 'string' ? data.message : undefined;

  const rescueState: RescueState = {
    status,
    targetName,
    rescuerName,
    progress: Number.isFinite(progress) ? Math.max(0, Math.min(100, progress)) : undefined,
    etaSeconds: Number.isFinite(etaSeconds) ? Math.max(0, etaSeconds) : undefined,
    message,
    timestamp,
  };

  return rescueState;
};
