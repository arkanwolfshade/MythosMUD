// Mythos time bootstrap hook
// Extracted from GameClientV2Container to reduce complexity

import { useEffect } from 'react';
import type { MythosTimePayload, MythosTimeState } from '../../../types/mythosTime';
import { logger } from '../../../utils/logger';
import { buildMythosTimeState } from '../../../utils/mythosTime';

interface UseMythosTimeBootstrapParams {
  authToken: string;
  setMythosTime: (time: MythosTimeState) => void;
  lastDaypartRef: React.MutableRefObject<string | null>;
  lastHolidayIdsRef: React.MutableRefObject<string[]>;
}

export const useMythosTimeBootstrap = ({
  authToken,
  setMythosTime,
  lastDaypartRef,
  lastHolidayIdsRef,
}: UseMythosTimeBootstrapParams) => {
  useEffect(() => {
    if (typeof fetch !== 'function') {
      return undefined;
    }

    let cancelled = false;

    const bootstrapMythosTime = async () => {
      try {
        const headers: HeadersInit = { Accept: 'application/json' };
        if (authToken) {
          headers.Authorization = `Bearer ${authToken}`;
        }
        const response = await fetch('/game/time', { headers });
        if (!response.ok) {
          throw new Error(`HTTP ${response.status}`);
        }
        const payload = (await response.json()) as MythosTimePayload;
        if (cancelled) {
          return;
        }
        const nextState = buildMythosTimeState(payload);
        setMythosTime(nextState);
        lastDaypartRef.current = nextState.daypart;
        lastHolidayIdsRef.current = nextState.active_holidays.map(h => h.id);
      } catch (error) {
        logger.warn('GameClientV2Container', 'Failed to bootstrap Mythos time', { error: String(error) });
      }
    };

    void bootstrapMythosTime();
    return () => {
      cancelled = true;
    };
  }, [authToken, setMythosTime, lastDaypartRef, lastHolidayIdsRef]);
};
