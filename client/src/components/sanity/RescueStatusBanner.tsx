import { memo } from 'react';
import type { RescueState } from '../../types/sanity';

interface RescueStatusBannerProps {
  state: RescueState | null;
  onDismiss?: () => void;
  className?: string;
}

const statusStyles: Record<
  Exclude<RescueState['status'], 'idle'>,
  { container: string; label: string; description: string }
> = {
  catatonic: {
    container: 'bg-rose-950/80 border border-rose-500/60',
    label: 'Catatonic',
    description: 'Command input is locked until a rescuer intervenes.',
  },
  channeling: {
    container: 'bg-amber-950/80 border border-amber-500/60',
    label: 'Rescue Ritual in Progress',
    description: 'Hold steady while companions attempt to ground your mind.',
  },
  success: {
    container: 'bg-emerald-950/80 border border-emerald-500/60',
    label: 'Rescue Successful',
    description: 'Sanity tether restored. Breathe slowly.',
  },
  failed: {
    container: 'bg-rose-950/80 border border-rose-600/70',
    label: 'Rescue Failed',
    description: 'The ritual faltered. Another attempt may stabilize the target.',
  },
  sanitarium: {
    container: 'bg-fuchsia-950/80 border border-fuchsia-500/60',
    label: 'Transfer to Sanitarium',
    description: 'Caretakers escort you to the Arkham Sanitarium for recovery.',
  },
};

export const RescueStatusBanner = memo<RescueStatusBannerProps>(({ state, onDismiss, className }) => {
  if (!state || state.status === 'idle') {
    return null;
  }

  const style = statusStyles[state.status];

  return (
    <aside
      className={`relative flex flex-col gap-2 rounded px-4 py-3 text-sm text-mythos-terminal-text shadow-lg ${style.container} ${className ?? ''}`}
      role="status"
      aria-live="assertive"
    >
      <div className="flex items-start justify-between gap-3">
        <div>
          <span className="text-xs font-semibold uppercase tracking-wide text-mythos-terminal-primary">
            {style.label}
          </span>
          {state.message ? (
            <p className="mt-1 leading-relaxed text-mythos-terminal-text-secondary">{state.message}</p>
          ) : (
            <p className="mt-1 leading-relaxed text-mythos-terminal-text-secondary">{style.description}</p>
          )}
          {(state.rescuerName || state.targetName) && (
            <p className="text-[11px] uppercase tracking-wide text-mythos-terminal-text-secondary/80 mt-1">
              {state.rescuerName && <span>Rescuer: {state.rescuerName}</span>}
              {state.rescuerName && state.targetName && <span className="mx-1">•</span>}
              {state.targetName && <span>Target: {state.targetName}</span>}
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

      {state.status === 'channeling' && typeof state.progress === 'number' && (
        <div className="space-y-1">
          <div className="flex items-center justify-between text-[11px] text-mythos-terminal-text-secondary">
            <span>Stability tether</span>
            <span>{Math.round(state.progress)}%</span>
          </div>
          <div className="h-2.5 overflow-hidden rounded bg-mythos-terminal-border">
            <div
              className="h-full bg-amber-400 transition-all duration-500 ease-out"
              style={{ width: `${Math.max(0, Math.min(100, state.progress))}%` }}
              aria-hidden="true"
            />
          </div>
          {typeof state.etaSeconds === 'number' && (
            <div className="text-[11px] text-mythos-terminal-text-secondary">
              Estimated stabilization: ~{Math.max(0, Math.round(state.etaSeconds))}s
            </div>
          )}
        </div>
      )}
    </aside>
  );
});

RescueStatusBanner.displayName = 'RescueStatusBanner';
