import { memo } from 'react';
import type { LucidityStatus } from '../../types/lucidity';

interface LucidityMeterProps {
  status: LucidityStatus | null;
  className?: string;
}

const TIER_DESCRIPTIONS: Record<
  LucidityStatus['tier'],
  { label: string; tone: string; description: string; barClass: string }
> = {
  lucid: {
    label: 'Lucid',
    tone: 'text-emerald-300',
    description: 'Mind is steady and grounded.',
    barClass: 'bg-emerald-400',
  },
  uneasy: {
    label: 'Uneasy',
    tone: 'text-amber-300',
    description: 'A chill brushes the edge of perception.',
    barClass: 'bg-amber-300',
  },
  fractured: {
    label: 'Fractured',
    tone: 'text-orange-300',
    description: 'Reality frays; focus slips between fingers.',
    barClass: 'bg-orange-400',
  },
  deranged: {
    label: 'Deranged',
    tone: 'text-rose-300',
    description: 'Thoughts spiral into non-euclidean tangles.',
    barClass: 'bg-rose-500',
  },
  catatonic: {
    label: 'Catatonic',
    tone: 'text-fuchsia-300',
    description: 'Willpower is absent; body moves without intent.',
    barClass: 'bg-fuchsia-500',
  },
};

const formatChange = (delta: number | undefined) => {
  if (delta === undefined || Number.isNaN(delta)) {
    return '';
  }

  if (delta === 0) {
    return '±0';
  }

  const prefix = delta > 0 ? '+' : '−';
  return `${prefix}${Math.abs(delta)}`;
};

export const LucidityMeter = memo<LucidityMeterProps>(({ status, className }) => {
  if (!status) {
    return null;
  }

  const tierMetadata = TIER_DESCRIPTIONS[status.tier];
  const isNegativeRange = status.current < 0;
  const minValue = isNegativeRange ? -100 : 0;
  const maxValue = isNegativeRange ? 0 : Math.max(1, status.max);
  const boundedCurrent = Math.max(minValue, Math.min(maxValue, status.current));
  const range = maxValue - minValue || 1;
  const percentage = Math.max(0, Math.min(100, Math.round(((boundedCurrent - minValue) / range) * 100)));
  const deltaDisplay = formatChange(status.lastChange?.delta);
  const reason = status.lastChange?.reason?.replace(/_/g, ' ');

  return (
    <div
      className={`space-y-2 rounded border border-mythos-terminal-border bg-mythos-terminal-surface/70 p-3 transition-colors duration-300 ${className ?? ''}`}
      role="group"
      aria-label="Lucidity status"
    >
      <div className="flex items-center justify-between">
        <div className="flex flex-col">
          <span className="text-sm text-mythos-terminal-text-secondary">Lucidity</span>
          <strong className="text-lg text-mythos-terminal-text">
            {status.current}
            <span className="text-mythos-terminal-text-secondary text-sm"> / {status.max}</span>
          </strong>
        </div>
        <div className="text-right">
          <span className={`block text-sm font-semibold uppercase tracking-wide ${tierMetadata.tone}`}>
            {tierMetadata.label}
          </span>
          <span className="text-xs text-mythos-terminal-text-secondary">{tierMetadata.description}</span>
        </div>
      </div>
      <div
        className="relative h-2.5 overflow-hidden rounded bg-mythos-terminal-border"
        role="meter"
        aria-valuemin={minValue}
        aria-valuemax={maxValue}
        aria-valuenow={status.current}
        aria-valuetext={`${status.current} LCD`}
      >
        <div
          className={`${tierMetadata.barClass} h-full transition-all duration-500 ease-out`}
          style={{ width: `${percentage}%` }}
          aria-hidden="true"
        />
      </div>

      {(status.lastChange || status.liabilities.length > 0) && (
        <div className="flex flex-col gap-1 text-xs text-mythos-terminal-text-secondary" aria-live="polite">
          {status.lastChange && (
            <div className="flex items-center justify-between">
              <span>Recent change</span>
              <span className="font-semibold text-mythos-terminal-primary">
                {deltaDisplay}
                {reason ? ` (${reason})` : ''}
              </span>
            </div>
          )}
          {status.liabilities.length > 0 && (
            <div>
              <span className="block font-semibold text-mythos-terminal-warning mb-1">Liabilities</span>
              <ul className="flex flex-wrap gap-1">
                {status.liabilities.map(liability => (
                  <li
                    key={liability}
                    className="rounded bg-mythos-terminal-background px-2 py-1 text-[11px] uppercase tracking-wide text-mythos-terminal-warning"
                  >
                    {liability.replace(/_/g, ' ')}
                  </li>
                ))}
              </ul>
            </div>
          )}
        </div>
      )}
    </div>
  );
});

LucidityMeter.displayName = 'LucidityMeter';
