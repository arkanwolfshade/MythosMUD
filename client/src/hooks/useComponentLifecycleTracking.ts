/**
 * Hook for tracking component mount/unmount and cleanup verification.
 *
 * This hook helps identify memory leaks by tracking component lifecycle
 * and verifying cleanup functions are called.
 */

import { useEffect, useRef } from 'react';
import { getClientMetricsCollector } from '../utils/clientMetricsCollector.js';

interface UseComponentLifecycleTrackingOptions {
  componentName: string;
  enabled?: boolean;
}

/**
 * Hook to track component lifecycle and verify cleanup
 */
export function useComponentLifecycleTracking(options: UseComponentLifecycleTrackingOptions): {
  hasCleanup: boolean;
  setCleanup: (cleanup: () => void) => void;
} {
  const { componentName, enabled = import.meta.env.DEV } = options;
  const cleanupRef = useRef<(() => void) | null>(null);
  const collector = getClientMetricsCollector();

  useEffect(() => {
    if (!enabled) {
      return;
    }

    // Track mount
    collector.trackComponentMount(componentName);

    return () => {
      // Track unmount with cleanup verification
      const hasCleanup = cleanupRef.current !== null;
      collector.trackComponentUnmount(componentName, hasCleanup);

      // Call cleanup if registered
      if (cleanupRef.current) {
        try {
          cleanupRef.current();
        } catch (error) {
          // Internal logging with component name from React component props, not user input
          // nosemgrep: javascript.lang.security.audit.unsafe-formatstring.unsafe-formatstring
          console.error(`[ComponentLifecycle] Error in cleanup for ${componentName}:`, error);
        }
      }
    };
  }, [componentName, enabled, collector]);

  const setCleanup = (cleanup: () => void) => {
    cleanupRef.current = cleanup;
  };

  return {
    hasCleanup: cleanupRef.current !== null,
    setCleanup,
  };
}
