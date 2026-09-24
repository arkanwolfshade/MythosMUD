/**
 * Client-side metrics collector for development logging.
 *
 * Tracks resource usage and component lifecycle to help identify memory leaks in the client
 * application.
 */

import { ResourceManager } from './resourceCleanup.js';

interface ComponentLifecycleMetrics {
  componentName: string;
  mountCount: number;
  unmountCount: number;
  missingCleanupCount: number;
  lastMountTime: number;
  lastUnmountTime: number;
}

interface ClientMetrics {
  resourceStats: {
    timers: number;
    intervals: number;
    webSockets: number;
    customResources: number;
    total: number;
  };
  componentLifecycle: ComponentLifecycleMetrics[];
  timestamp: number;
}

class ClientMetricsCollector {
  private componentLifecycle: Map<string, ComponentLifecycleMetrics> = new Map();
  private resourceManager: ResourceManager | null = null;

  /**
   * Set the ResourceManager instance for tracking resources
   */
  setResourceManager(resourceManager: ResourceManager): void {
    this.resourceManager = resourceManager;
  }

  /**
   * Track component mount
   */
  trackComponentMount(componentName: string): void {
    const existing = this.componentLifecycle.get(componentName) || {
      componentName,
      mountCount: 0,
      unmountCount: 0,
      missingCleanupCount: 0,
      lastMountTime: 0,
      lastUnmountTime: 0,
    };
    existing.mountCount += 1;
    existing.lastMountTime = Date.now();
    this.componentLifecycle.set(componentName, existing);
  }

  /**
   * Track component unmount
   */
  trackComponentUnmount(componentName: string, hasCleanup: boolean): void {
    const existing = this.componentLifecycle.get(componentName);
    if (existing) {
      existing.unmountCount += 1;
      existing.lastUnmountTime = Date.now();
      if (!hasCleanup) {
        existing.missingCleanupCount += 1;
        console.warn(`[Metrics] Component ${componentName} unmounted without cleanup function`);
      }
      this.componentLifecycle.set(componentName, existing);
    }
  }

  /**
   * Get all metrics
   */
  getMetrics(): ClientMetrics {
    const resourceStats = this.resourceManager?.getResourceStats() || {
      timers: 0,
      intervals: 0,
      webSockets: 0,
      customResources: 0,
      total: 0,
    };

    return {
      resourceStats,
      componentLifecycle: Array.from(this.componentLifecycle.values()),
      timestamp: Date.now(),
    };
  }

  /**
   * Log metrics to console (for development)
   */
  logMetrics(): void {
    if (import.meta.env.DEV) {
      const metrics = this.getMetrics();
      console.log('[Client Metrics]', metrics);
    }
  }
}

// Singleton instance
let collectorInstance: ClientMetricsCollector | null = null;

export function getClientMetricsCollector(): ClientMetricsCollector {
  if (!collectorInstance) {
    collectorInstance = new ClientMetricsCollector();
  }
  return collectorInstance;
}
