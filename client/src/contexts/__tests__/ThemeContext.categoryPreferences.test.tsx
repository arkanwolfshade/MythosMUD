// High-contrast and text-labels preferences drive classes on <html> that messageCategories.css keys off.

import { act, renderHook } from '@testing-library/react';
import type { ReactNode } from 'react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import { ThemeProvider } from '../ThemeContext';
import { useAccessibilityPreference, useTextLabelsPreference, useTheme } from '../hooks/useThemeContext';

const wrapper = ({ children }: { children: ReactNode }) => <ThemeProvider>{children}</ThemeProvider>;
const root = document.documentElement;

describe('ThemeContext message-category preferences', () => {
  beforeEach(() => {
    localStorage.clear();
    root.className = '';
  });

  afterEach(() => {
    vi.restoreAllMocks();
  });

  it('defaults both off and leaves the classes off <html>', () => {
    const { result } = renderHook(() => useTheme(), { wrapper });
    expect(result.current.preferences.highContrast).toBe(false);
    expect(result.current.preferences.textLabels).toBe(false);
    expect(root.classList.contains('high-contrast')).toBe(false);
    expect(root.classList.contains('text-labels')).toBe(false);
  });

  it('toggles the high-contrast class on <html>', async () => {
    const { result } = renderHook(() => useAccessibilityPreference(), { wrapper });
    await act(() => result.current.setHighContrast(true));
    expect(root.classList.contains('high-contrast')).toBe(true);
    await act(() => result.current.setHighContrast(false));
    expect(root.classList.contains('high-contrast')).toBe(false);
  });

  it('toggles the text-labels class on <html> and persists the flag', async () => {
    const { result } = renderHook(() => useTextLabelsPreference(), { wrapper });
    await act(() => result.current.setTextLabels(true));
    expect(result.current.textLabels).toBe(true);
    expect(root.classList.contains('text-labels')).toBe(true);
    expect(JSON.parse(localStorage.getItem('mythosmud-ui-preferences') ?? '{}').textLabels).toBe(true);
    await act(() => result.current.setTextLabels(false));
    expect(root.classList.contains('text-labels')).toBe(false);
  });

  it('applies saved preferences to <html> on load', () => {
    localStorage.setItem('mythosmud-ui-preferences', JSON.stringify({ highContrast: true, textLabels: true }));
    renderHook(() => useTheme(), { wrapper });
    expect(root.classList.contains('high-contrast')).toBe(true);
    expect(root.classList.contains('text-labels')).toBe(true);
  });

  it('survives localStorage throwing on read and write', async () => {
    vi.spyOn(Storage.prototype, 'getItem').mockImplementation(() => {
      throw new Error('blocked');
    });
    vi.spyOn(Storage.prototype, 'setItem').mockImplementation(() => {
      throw new Error('blocked');
    });
    const { result } = renderHook(() => useTextLabelsPreference(), { wrapper });
    expect(result.current.textLabels).toBe(false);
    await act(() => result.current.setTextLabels(true));
    expect(root.classList.contains('text-labels')).toBe(true);
  });
});
