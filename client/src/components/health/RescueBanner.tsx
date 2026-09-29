import { memo, useEffect, useState } from 'react';

import { RESCUE_TERMINAL_DISPLAY_MS, type RescueStatus } from '../../types/rescue';

interface RescueBannerProps {
  /** Latest server rescue phase (GameState.rescueStatus); null when none. */
  rescueStatus: RescueStatus | null;
  /** From the authoritative lucidity tier; shown when no rescue phase is on screen. */
  isCatatonic: boolean;
  className?: string;
}

const CATATONIC_MESSAGE = 'Your senses collapse into static; only allies can reach you now.';

/** Headline per phase and side. The body text is the server's own line, already worded for the side. */
function headline({ status, role }: RescueStatus): string {
  switch (status) {
    case 'channeling':
      return role === 'rescuer' ? 'Grounding' : 'Being Grounded';
    case 'success':
      return role === 'rescuer' ? 'Grounding Complete' : 'Mind Steadied';
    case 'rescued':
      return role === 'rescuer' ? 'Rescue Complete' : 'Rescued';
    case 'failed':
      return 'Grounding Failed';
    case 'interrupted':
      return 'Grounding Interrupted';
    case 'sanitarium':
      return 'Arkham Sanitarium';
  }
}

const toneClass = (status: RescueStatus['status']): string =>
  status === 'failed' || status === 'interrupted' || status === 'sanitarium'
    ? 'bg-red-950/80 border-red-500/60'
    : 'bg-indigo-950/80 border-indigo-400/60';

/**
 * Persistent, glanceable rescue state, independent of chat scroll position (#713).
 * Server-authoritative: it renders the latest rescue_update and the lucidity tier, nothing inferred.
 * A phase clears itself after RESCUE_TERMINAL_DISPLAY_MS (channeling: its ETA plus the same grace,
 * in case the server never sends the terminal event); the catatonic state then shows again if the
 * tier still says so. The timer is keyed on the event's sequence number, so a new phase restarts it.
 */
export const RescueBanner = memo<RescueBannerProps>(({ rescueStatus, isCatatonic, className }) => {
  const [expiredSeq, setExpiredSeq] = useState<number | null>(null);

  useEffect(() => {
    if (!rescueStatus) return undefined;
    const { seq, status, etaSeconds } = rescueStatus;
    const delayMs = RESCUE_TERMINAL_DISPLAY_MS + (status === 'channeling' ? (etaSeconds ?? 0) * 1000 : 0);
    const timer = setTimeout(() => setExpiredSeq(seq), delayMs);
    return () => clearTimeout(timer);
  }, [rescueStatus]);

  const activeRescue = rescueStatus && rescueStatus.seq !== expiredSeq ? rescueStatus : null;
  if (!activeRescue && !isCatatonic) return null;

  const title = activeRescue ? headline(activeRescue) : 'Catatonic';
  const body = activeRescue ? activeRescue.message : CATATONIC_MESSAGE;
  const tone = activeRescue ? toneClass(activeRescue.status) : 'bg-slate-900/80 border-slate-500/60';

  return (
    <aside
      className={`pointer-events-auto relative flex flex-col gap-1 rounded border px-4 py-3 text-sm text-mythos-terminal-text shadow-lg ${tone} ${className ?? ''}`}
      role="status"
      aria-live="polite"
      data-testid="rescue-banner"
    >
      <span className="text-xs font-semibold uppercase tracking-wide text-mythos-terminal-primary">{title}</span>
      {body && <p className="leading-relaxed text-mythos-terminal-text-secondary">{body}</p>}
      {activeRescue?.status === 'channeling' && activeRescue.etaSeconds !== undefined && (
        <div className="mt-1 h-1 w-full overflow-hidden rounded bg-black/40" aria-hidden="true">
          <div
            key={activeRescue.seq}
            className="h-full animate-rescue-fill bg-mythos-terminal-primary"
            style={{ animationDuration: `${activeRescue.etaSeconds}s` }}
            data-testid="rescue-banner-progress"
          />
        </div>
      )}
    </aside>
  );
});

RescueBanner.displayName = 'RescueBanner';
