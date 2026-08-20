/**
 * Cross-tab lucidity tier relay (#626).
 *
 * The in-game tab publishes the player's current lucidity tier to localStorage; the standalone
 * /map tab (opened via window.open, no shared React state) reads it on mount and stays live via
 * the native cross-tab `storage` event. Not a credential -- plain informational relay.
 */

import { useEffect, useState } from 'react';
import type { LucidityTier } from '../types/lucidity';

const STORAGE_KEY = 'mythosmud_lucidity_tier';

/** Publish the current tier so other tabs (e.g. /map) can pick it up. Call from the in-game tab. */
export function publishTier(tier: LucidityTier | undefined): void {
  if (typeof window === 'undefined') {
    return;
  }
  if (!tier) {
    window.localStorage.removeItem(STORAGE_KEY);
    return;
  }
  window.localStorage.setItem(STORAGE_KEY, tier);
}

function readTier(): LucidityTier | null {
  if (typeof window === 'undefined') {
    return null;
  }
  const raw = window.localStorage.getItem(STORAGE_KEY);
  return raw as LucidityTier | null;
}

/** Read the relayed tier on mount and keep it live via the cross-tab `storage` event. */
export function useCrossTabLucidityTier(): LucidityTier | null {
  const [tier, setTier] = useState<LucidityTier | null>(() => readTier());

  useEffect(() => {
    const handleStorage = (event: StorageEvent) => {
      if (event.key === STORAGE_KEY || event.key === null) {
        setTier(readTier());
      }
    };
    window.addEventListener('storage', handleStorage);
    return () => window.removeEventListener('storage', handleStorage);
  }, []);

  return tier;
}
