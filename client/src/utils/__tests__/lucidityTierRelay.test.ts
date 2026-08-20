import { act, renderHook } from '@testing-library/react';
import { afterEach, describe, expect, it, vi } from 'vitest';
import { publishTier, useCrossTabLucidityTier } from '../lucidityTierRelay';

const STORAGE_KEY = 'mythosmud_lucidity_tier';

describe('lucidityTierRelay', () => {
  afterEach(() => {
    window.localStorage.removeItem(STORAGE_KEY);
  });

  it('publishTier writes the tier to localStorage', () => {
    publishTier('deranged');
    expect(window.localStorage.getItem(STORAGE_KEY)).toBe('deranged');
  });

  it('publishTier(undefined) clears the stored tier', () => {
    window.localStorage.setItem(STORAGE_KEY, 'deranged');
    publishTier(undefined);
    expect(window.localStorage.getItem(STORAGE_KEY)).toBeNull();
  });

  it('useCrossTabLucidityTier reads the initial value on mount', () => {
    window.localStorage.setItem(STORAGE_KEY, 'fractured');
    const { result } = renderHook(() => useCrossTabLucidityTier());
    expect(result.current).toBe('fractured');
  });

  it('useCrossTabLucidityTier updates when a storage event fires (cross-tab)', () => {
    const { result } = renderHook(() => useCrossTabLucidityTier());
    expect(result.current).toBeNull();

    window.localStorage.setItem(STORAGE_KEY, 'deranged');
    act(() => {
      window.dispatchEvent(
        new StorageEvent('storage', { key: STORAGE_KEY, newValue: 'deranged', storageArea: window.localStorage })
      );
    });

    expect(result.current).toBe('deranged');
  });

  it('removes its storage listener on unmount', () => {
    const removeSpy = vi.spyOn(window, 'removeEventListener');
    const { unmount } = renderHook(() => useCrossTabLucidityTier());
    unmount();
    expect(removeSpy).toHaveBeenCalledWith('storage', expect.any(Function));
  });
});
