// Hallucination feed cleanup hook
// Extracted from GameClientV2Container to reduce complexity

import { useEffect } from 'react';
import type { HallucinationMessage } from '../../../types/lucidity';

export const useHallucinationFeedCleanup = (
  setHallucinationFeed: React.Dispatch<React.SetStateAction<HallucinationMessage[]>>
) => {
  useEffect(() => {
    const interval = window.setInterval(() => {
      setHallucinationFeed(prev =>
        prev.filter(entry => {
          const timestamp = new Date(entry.timestamp).getTime();
          return Number.isFinite(timestamp) ? Date.now() - timestamp < 60_000 : false;
        })
      );
    }, 10_000);

    return () => window.clearInterval(interval);
  }, [setHallucinationFeed]);
};
