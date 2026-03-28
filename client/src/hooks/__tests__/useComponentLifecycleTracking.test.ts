import { act, renderHook } from '@testing-library/react';
import { beforeEach, describe, expect, it, vi } from 'vitest';

const trackComponentMount = vi.fn();
const trackComponentUnmount = vi.fn();

vi.mock('../../utils/clientMetricsCollector.js', () => ({
  getClientMetricsCollector: () => ({
    trackComponentMount,
    trackComponentUnmount,
  }),
}));

import { useComponentLifecycleTracking } from '../useComponentLifecycleTracking';

describe('useComponentLifecycleTracking', () => {
  beforeEach(() => {
    vi.clearAllMocks();
  });

  it('tracks mount and unmount with cleanup presence', () => {
    const cleanupFn = vi.fn();
    const { result, unmount } = renderHook(() => useComponentLifecycleTracking({ componentName: 'GameClientV2' }));

    act(() => {
      result.current.setCleanup(cleanupFn);
    });

    expect(trackComponentMount).toHaveBeenCalledWith('GameClientV2');

    unmount();

    expect(trackComponentUnmount).toHaveBeenCalledWith('GameClientV2', true);
    expect(cleanupFn).toHaveBeenCalledTimes(1);
  });

  it('tracks unmount without cleanup when none is registered', () => {
    const { unmount } = renderHook(() => useComponentLifecycleTracking({ componentName: 'NoCleanupPanel' }));

    unmount();

    expect(trackComponentUnmount).toHaveBeenCalledWith('NoCleanupPanel', false);
  });
});
