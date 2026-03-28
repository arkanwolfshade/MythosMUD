import { renderHook } from '@testing-library/react';
import { beforeEach, describe, expect, it, vi } from 'vitest';

const trackStoreSubscription = vi.fn();
const trackStoreUnsubscription = vi.fn();

vi.mock('../../utils/clientMetricsCollector.js', () => ({
  getClientMetricsCollector: () => ({
    trackStoreSubscription,
    trackStoreUnsubscription,
  }),
}));

import { useStoreSubscriptionTracking } from '../useStoreSubscriptionTracking';

describe('useStoreSubscriptionTracking', () => {
  beforeEach(() => {
    vi.clearAllMocks();
  });

  it('tracks subscription on mount and unsubscription on unmount', () => {
    const { unmount } = renderHook(() => useStoreSubscriptionTracking('connectionStore', { getState: () => ({}) }));

    expect(trackStoreSubscription).toHaveBeenCalledWith('connectionStore');

    unmount();

    expect(trackStoreUnsubscription).toHaveBeenCalledWith('connectionStore');
  });
});
