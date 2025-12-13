import { memo } from 'react';

export interface MagicPointsStatus {
  current: number;
  max: number;
  lastChange?: {
    delta: number;
    reason?: string;
  };
}

interface MagicPointsMeterProps {
  status: MagicPointsStatus | null;
  className?: string;
}

const formatDelta = (delta?: number): string => {
  if (delta === undefined || Number.isNaN(delta) || delta === 0) {
    return '';
  }

  const prefix = delta > 0 ? '+' : '−';
  return `${prefix}${Math.abs(delta)}`;
};

export const MagicPointsMeter = memo<MagicPointsMeterProps>(({ status, className }) => {
  if (!status) {
    return null;
  }

  const percentage = Math.max(0, Math.min(100, Math.round((status.current / status.max) * 100)));
  const changeText = formatDelta(status.lastChange?.delta);

  return (
    <div
      className={`space-y-2 rounded border border-mythos-terminal-border bg-mythos-terminal-surface/70 p-3 transition-colors duration-300 ${className ?? ''}`}
      role="group"
      aria-label="Magic Points status"
      data-testid="magic-points-meter"
    >
      <div className="flex items-center justify-between">
        <div className="flex flex-col">
          <span className="text-sm text-mythos-terminal-text-secondary">Magic Points</span>
          <strong className="text-lg text-mythos-terminal-text">
            {status.current}
            <span className="text-mythos-terminal-text-secondary text-sm"> / {status.max}</span>
          </strong>
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
          className="bg-blue-400 h-full transition-all duration-500 ease-out"
          style={{ width: `${percentage}%` }}
          aria-hidden="true"
        />
      </div>

      {changeText && (
        <div className="flex flex-col gap-1 text-xs text-mythos-terminal-text-secondary" aria-live="polite">
          <div className="flex items-center justify-between">
            <span>Recent change</span>
            <span className="font-semibold text-mythos-terminal-primary">
              {changeText}
              {status.lastChange?.reason ? ` (${status.lastChange.reason})` : ''}
            </span>
          </div>
        </div>
      )}
    </div>
  );
});

MagicPointsMeter.displayName = 'MagicPointsMeter';
