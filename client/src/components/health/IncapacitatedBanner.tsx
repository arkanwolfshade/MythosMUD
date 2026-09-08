import { memo } from 'react';

/**
 * Banner shown while DP <= 0 ("incapacitated" health tier, see types/health.ts).
 * Self-clearing only: visibility is driven entirely by the authoritative DP tier
 * (see GameClientV2.tsx), so there is no dismiss control and no minimum dwell time.
 * Outside combat the window is typically ~1 real second before death or recovery.
 */
export const IncapacitatedBanner = memo<{ className?: string }>(({ className }) => {
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
      <p className="leading-relaxed text-mythos-terminal-text-secondary">
        You cannot attack or cast spells until you recover.
      </p>
    </aside>
  );
});

IncapacitatedBanner.displayName = 'IncapacitatedBanner';
