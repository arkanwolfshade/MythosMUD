/**
 * Hook for tracking Zustand store subscriptions.
 *
 * This hook helps identify memory leaks by tracking store subscriptions
 * and verifying unsubscription on component unmount.
 */

import { useEffect } from 'react';
import { getClientMetricsCollector } from '../utils/clientMetricsCollector.js';

/**
 * Hook to track Zustand store subscription for metrics (e.g. leak detection).
 *
 * Pass a stable reference as the second argument so the component does not
 * subscribe to the entire store. Prefer the store's getState reference:
 *
 * Usage:
 * ```tsx
 * useStoreSubscriptionTracking('connectionStore', useConnectionStore.getState);
 * ```
 *
 * Avoid subscribing to the whole store just for tracking:
 * ```tsx
 * const state = useConnectionStore(); // BAD: re-renders on any connection change
 * useStoreSubscriptionTracking('connectionStore', state);
 * ```
 */
export function useStoreSubscriptionTracking<T>(storeName: string, store: T): void {
  const collector = getClientMetricsCollector();

  useEffect(() => {
    if (!import.meta.env.DEV) {
      return;
    }

    // Track subscription
    collector.trackStoreSubscription(storeName);

    return () => {
      // Track unsubscription
      collector.trackStoreUnsubscription(storeName);
    };
  }, [storeName, store, collector]);
}
