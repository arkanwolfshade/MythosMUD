// Mythos time bootstrap hook
// Extracted from GameClientV2Container to reduce complexity

import { useEffect } from 'react';
import { isMythosTimePayload, type MythosTimeState } from '../../../types/mythosTime';
import { API_V1_BASE } from '../../../utils/config';
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
        const response = await fetch(`${API_V1_BASE}/game/time`, { headers });
        if (!response.ok) {
          throw new Error(`HTTP ${response.status}`);
        }
        const raw: unknown = await response.json();
        if (cancelled) {
          return;
        }
        if (!isMythosTimePayload(raw)) {
          logger.warn('GameClientV2Container', 'Invalid Mythos time payload from server', { raw });
          return;
        }
        const nextState = buildMythosTimeState(raw);
        setMythosTime(nextState);
        lastDaypartRef.current = nextState.daypart;
        // Ensure active_holidays is always an array before calling .map() (defensive coding)
        lastHolidayIdsRef.current = (nextState.active_holidays ?? []).map(h => h.id);
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
