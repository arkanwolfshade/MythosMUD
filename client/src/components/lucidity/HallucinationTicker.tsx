import { memo } from 'react';
import type { HallucinationMessage } from '../../types/lucidity';

interface HallucinationTickerProps {
  hallucinations: HallucinationMessage[];
  onDismiss?: (id: string) => void;
  className?: string;
}

const severityClass: Record<HallucinationMessage['severity'], string> = {
  minor: 'border-emerald-400/40',
  moderate: 'border-amber-400/60',
  severe: 'border-rose-500/70',
};

export const HallucinationTicker = memo<HallucinationTickerProps>(({ hallucinations, onDismiss, className }) => {
  if (!hallucinations.length) {
    return null;
  }

  return (
    <div
      className={`space-y-2 rounded border border-mythos-terminal-border bg-mythos-terminal-background/60 p-3 backdrop-blur ${className ?? ''}`}
      aria-live="polite"
      aria-label="Recent hallucinations"
    >
      <div className="flex items-center justify-between">
        <span className="text-xs font-semibold uppercase tracking-wide text-mythos-terminal-warning">
          Hallucination Log
        </span>
      </div>
      <ul className="space-y-2 text-xs">
        {hallucinations.map(entry => {
          const timestamp = new Date(entry.timestamp);
          const timeDisplay = Number.isNaN(timestamp.getTime())
            ? entry.timestamp
            : timestamp.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit', second: '2-digit' });

          return (
            <li
              key={entry.id}
              className={[
                'rounded border bg-mythos-terminal-surface/80 p-2 shadow-sm transition-all hover:shadow-md',
                'focus-within:ring-2 focus-within:ring-mythos-terminal-primary/60',
                severityClass[entry.severity],
              ].join(' ')}
            >
              <div className="flex items-start justify-between gap-2">
                <div className="space-y-1">
                  <span className="text-sm font-semibold text-mythos-terminal-primary">{entry.title}</span>
                  {entry.description && (
                    <p className="text-mythos-terminal-text-secondary leading-snug">{entry.description}</p>
                  )}
                  <span className="text-[11px] uppercase tracking-wide text-mythos-terminal-text-secondary">
                    {entry.severity} vision · {timeDisplay}
                  </span>
                </div>
                {onDismiss && (
                  <button
                    type="button"
                    className="rounded bg-transparent px-2 py-1 text-[11px] uppercase tracking-wide text-mythos-terminal-text-secondary hover:text-mythos-terminal-error focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-mythos-terminal-primary/60"
                    onClick={() => onDismiss(entry.id)}
                  >
                    Dismiss
                  </button>
                )}
              </div>
            </li>
          );
        })}
      </ul>
    </div>
  );
});

HallucinationTicker.displayName = 'HallucinationTicker';
