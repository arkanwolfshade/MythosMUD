/**
 * Hook for tracking Zustand store subscriptions.
 *
 * This hook helps identify memory leaks by tracking store subscriptions
 * and verifying unsubscription on component unmount.
 */

import { useEffect } from 'react';
import { getClientMetricsCollector } from '../utils/clientMetricsCollector';

/**
 * Hook to track Zustand store subscription
 *
 * Usage:
 * ```tsx
 * const store = useConnectionStore();
 * useStoreSubscriptionTracking('connectionStore', store);
 * ```
 */
export function useStoreSubscriptionTracking<T>(storeName: string, store: T): void {
  const collector = getClientMetricsCollector();

  useEffect(() => {
    if (process.env.NODE_ENV !== 'development') {
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
