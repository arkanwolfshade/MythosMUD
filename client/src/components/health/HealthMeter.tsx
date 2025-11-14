import { memo } from 'react';

import type { HealthMeterProps, HealthStatus } from '../../types/health';

type TierMetadata = Record<
  HealthStatus['tier'],
  { label: string; tone: string; description: string; barClass: string }
>;

const TIER_METADATA: TierMetadata = {
  vigorous: {
    label: 'Vigorous',
    tone: 'text-emerald-300',
    description: 'Pulse steady, no mortal wounds detected.',
    barClass: 'bg-emerald-400',
  },
  steady: {
    label: 'Steady',
    tone: 'text-amber-300',
    description: 'Bruised but battle-ready per M.U. field notes.',
    barClass: 'bg-amber-300',
  },
  wounded: {
    label: 'Wounded',
    tone: 'text-orange-300',
    description: 'Vital signs wavering; invoke first-aid rites.',
    barClass: 'bg-orange-400',
  },
  critical: {
    label: 'Critical',
    tone: 'text-rose-300',
    description: 'Life thread frays like the tales in Cultes des Goules.',
    barClass: 'bg-rose-500',
  },
};

const formatDelta = (delta?: number): string => {
  if (delta === undefined || Number.isNaN(delta) || delta === 0) {
    return '';
  }

  const prefix = delta > 0 ? '+' : '-';
  return `${prefix}${Math.abs(delta)}`;
};

export const HealthMeter = memo<HealthMeterProps>(({ status, className }) => {
  if (!status) {
    return null;
  }

  const tierMetadata = TIER_METADATA[status.tier];
  const percentage = Math.max(0, Math.min(100, Math.round((status.current / status.max) * 100)));
  const changeText = formatDelta(status.lastChange?.delta);

  return (
    <div
      className={`space-y-2 rounded border border-mythos-terminal-border bg-mythos-terminal-surface/70 p-3 transition-colors duration-300 ${className ?? ''}`}
      role="group"
      aria-label="Health status"
      data-testid="health-meter"
    >
      <div className="flex items-center justify-between">
        <div className="flex flex-col">
          <span className="text-sm text-mythos-terminal-text-secondary">Health</span>
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
        aria-valuemin={0}
        aria-valuemax={status.max}
        aria-valuenow={status.current}
        aria-valuetext={`${percentage}%`}
      >
        <div
          className={`${tierMetadata.barClass} h-full transition-all duration-500 ease-out`}
          style={{ width: `${percentage}%` }}
          aria-hidden="true"
        />
      </div>

      {(changeText || status.posture) && (
        <div className="flex flex-col gap-1 text-xs text-mythos-terminal-text-secondary" aria-live="polite">
          {changeText && (
            <div className="flex items-center justify-between">
              <span>Recent change</span>
              <span className="font-semibold text-mythos-terminal-primary">
                {changeText}
                {status.lastChange?.reason ? ` (${status.lastChange.reason})` : ''}
              </span>
            </div>
          )}
          {status.posture && (
            <div className="flex items-center justify-between">
              <span>Posture</span>
              <span className="font-semibold capitalize">{status.posture.replace(/_/g, ' ')}</span>
            </div>
          )}
        </div>
      )}
    </div>
  );
});

HealthMeter.displayName = 'HealthMeter';
