import { memo } from 'react';

interface IncapacitatedBannerProps {
  onDismiss?: () => void;
  className?: string;
  message?: string;
}

/**
 * Banner displayed when player health reaches zero or below.
 * Similar to RescueStatusBanner but for physical incapacitation.
 */
export const IncapacitatedBanner = memo<IncapacitatedBannerProps>(({ onDismiss, className, message }) => {
  return (
    <aside
      className={`relative flex flex-col gap-2 rounded px-4 py-3 text-sm text-mythos-terminal-text shadow-lg bg-red-950/80 border border-red-500/60 ${className ?? ''}`}
      role="status"
      aria-live="assertive"
      data-testid="incapacitated-banner"
    >
      <div className="flex items-start justify-between gap-3">
        <div>
          <span className="text-xs font-semibold uppercase tracking-wide text-mythos-terminal-primary">
            Incapacitated
          </span>
          {message ? (
            <p className="mt-1 leading-relaxed text-mythos-terminal-text-secondary">{message}</p>
          ) : (
            <p className="mt-1 leading-relaxed text-mythos-terminal-text-secondary">
              Command input is locked until you receive medical attention.
            </p>
          )}
        </div>
        {onDismiss && (
          <button
            type="button"
            onClick={onDismiss}
            className="rounded bg-transparent px-2 py-1 text-[11px] uppercase tracking-wide text-mythos-terminal-text-secondary hover:text-mythos-terminal-primary focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-mythos-terminal-primary/60"
          >
            Dismiss
          </button>
        )}
      </div>
    </aside>
  );
});

IncapacitatedBanner.displayName = 'IncapacitatedBanner';
