import { memo } from 'react';

/**
 * Banner shown while DP <= 0 ("incapacitated" health tier, see types/health.ts).
 * Self-clearing only: visibility is driven entirely by the authoritative DP tier
 * (see GameClientV2.tsx), so there is no dismiss control and no minimum dwell time.
 * A downed player leaves combat and bleeds 1 DP per second from 0 to -10 (death), so the
 * countdown is derived from the server's DP (`currentDp + 10`), never from a client timer (#1059).
 */
const BLEED_OUT_DEATH_DP = -10;

export const IncapacitatedBanner = memo<{ className?: string; currentDp?: number }>(({ className, currentDp }) => {
  const secondsRemaining = currentDp === undefined ? null : Math.max(0, currentDp - BLEED_OUT_DEATH_DP);
  return (
    <aside
      className={`relative flex flex-col gap-1 rounded px-4 py-3 text-sm text-mythos-terminal-text shadow-lg bg-red-950/80 border border-red-500/60 ${className ?? ''}`}
      role="status"
      aria-live="assertive"
      data-testid="incapacitated-banner"
    >
      <span className="text-xs font-semibold uppercase tracking-wide text-mythos-terminal-primary">Incapacitated</span>
      <p className="leading-relaxed text-mythos-terminal-text-secondary">
        Darkness closes in on your vision as your lifeforce ebbs away.
      </p>
      {secondsRemaining !== null && (
        <p className="font-semibold leading-relaxed text-mythos-terminal-text" data-testid="bleed-out-countdown">
          You are bleeding out: {secondsRemaining} {secondsRemaining === 1 ? 'second' : 'seconds'} remain
        </p>
      )}
      <p className="leading-relaxed text-mythos-terminal-text-secondary">
        You cannot attack or cast spells until you recover.
      </p>
    </aside>
  );
});

IncapacitatedBanner.displayName = 'IncapacitatedBanner';
