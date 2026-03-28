import { beforeEach, describe, expect, it, vi } from 'vitest';

import { getClientMetricsCollector } from '../clientMetricsCollector';

describe('clientMetricsCollector', () => {
  beforeEach(() => {
    vi.clearAllMocks();
  });

  it('tracks store subscription and unsubscription timestamps', () => {
    const collector = getClientMetricsCollector();
    collector.trackStoreSubscription('connectionStore');
    collector.trackStoreUnsubscription('connectionStore');

    const metrics = collector.getMetrics();
    const entry = metrics.storeSubscriptions.find(s => s.storeName === 'connectionStore');

    expect(entry).toBeDefined();
    expect(entry?.subscriptionCount).toBeGreaterThan(0);
    expect(entry?.lastSubscriptionTime).toBeGreaterThan(0);
    expect(entry?.lastUnsubscriptionTime).toBeGreaterThan(0);
  });

  it('tracks component mount/unmount and missing cleanup counts', () => {
    const collector = getClientMetricsCollector();
    collector.trackComponentMount('GameClientV2');
    collector.trackComponentUnmount('GameClientV2', false);

    const metrics = collector.getMetrics();
    const entry = metrics.componentLifecycle.find(c => c.componentName === 'GameClientV2');

    expect(entry).toBeDefined();
    expect(entry?.mountCount).toBeGreaterThan(0);
    expect(entry?.unmountCount).toBeGreaterThan(0);
    expect(entry?.missingCleanupCount).toBeGreaterThan(0);
  });

  it('returns default resource stats without resource manager', () => {
    const collector = getClientMetricsCollector();
    const metrics = collector.getMetrics();

    expect(metrics.resourceStats).toEqual({
      timers: 0,
      intervals: 0,
      webSockets: 0,
      customResources: 0,
      total: 0,
    });
  });
});
