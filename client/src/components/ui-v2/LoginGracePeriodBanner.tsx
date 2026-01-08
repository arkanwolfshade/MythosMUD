import { memo, useEffect, useRef, useState } from 'react';

interface LoginGracePeriodBannerProps {
  remainingSeconds: number;
  className?: string;
}

/**
 * Banner displayed when player is in login grace period.
 * Shows countdown timer for the 10-second immunity period.
 * Similar to IncapacitatedBanner but for login protection.
 */
export const LoginGracePeriodBanner = memo<LoginGracePeriodBannerProps>(({ remainingSeconds, className }) => {
  // Initialize state with prop value
  const [displaySeconds, setDisplaySeconds] = useState(remainingSeconds);
  const remainingSecondsRef = useRef(remainingSeconds);
  const needsResetRef = useRef(false);

  // Track when remainingSeconds changes to trigger reset
  // Use queueMicrotask to defer state update and avoid synchronous setState in effect
  useEffect(() => {
    if (remainingSecondsRef.current !== remainingSeconds) {
      remainingSecondsRef.current = remainingSeconds;
      needsResetRef.current = true;
      // Defer state update to next microtask to avoid cascading renders
      // This pattern is acceptable as it defers the update outside the effect body
      queueMicrotask(() => {
        setDisplaySeconds(remainingSeconds);
        needsResetRef.current = false;
      });
    }
  }, [remainingSeconds]);

  // Update countdown every second
  useEffect(() => {
    if (remainingSeconds <= 0) {
      return;
    }

    const interval = setInterval(() => {
      setDisplaySeconds(prev => {
        // Reset to new remainingSeconds if it changed
        if (needsResetRef.current) {
          needsResetRef.current = false;
          return remainingSecondsRef.current;
        }
        const newValue = Math.max(0, prev - 1);
        return newValue;
      });
    }, 1000);

    return () => clearInterval(interval);
  }, [remainingSeconds]);

  // Don't render if grace period has expired
  if (displaySeconds <= 0) {
    return null;
  }

  const formattedTime = displaySeconds.toFixed(1);

  return (
    <aside
      className={`relative flex flex-col gap-2 rounded px-4 py-3 text-sm text-mythos-terminal-text shadow-lg bg-blue-950/80 border border-blue-500/60 ${className ?? ''}`}
      role="status"
      aria-live="polite"
      data-testid="login-grace-period-banner"
      style={{ pointerEvents: 'none', userSelect: 'none' }}
    >
      <div className="flex items-start justify-between gap-3">
        <div>
          <span className="text-xs font-semibold uppercase tracking-wide text-mythos-terminal-primary">Warded</span>
          <p className="mt-1 leading-relaxed text-mythos-terminal-text-secondary">
            Protected by ancient wards. Immunity expires in {formattedTime}s.
          </p>
        </div>
      </div>
    </aside>
  );
});

LoginGracePeriodBanner.displayName = 'LoginGracePeriodBanner';
