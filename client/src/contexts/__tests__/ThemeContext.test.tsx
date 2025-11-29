import { describe, expect, it, beforeEach } from 'vitest';
import { renderHook, act } from '@testing-library/react';
import { ThemeProvider } from '../ThemeContext';
import { useTheme } from '../hooks/useThemeContext';

describe('ThemeContext', () => {
  beforeEach(() => {
    localStorage.clear();
    // Clear document classes
    document.documentElement.className = '';
  });

  it('should provide default preferences', () => {
    // Arrange & Act
    const wrapper = ({ children }: { children: React.ReactNode }) => <ThemeProvider>{children}</ThemeProvider>;
    const { result } = renderHook(() => useTheme(), { wrapper });

    // Assert
    expect(result.current.preferences.theme).toBe('terminal');
    expect(result.current.preferences.colorScheme).toBe('default');
    expect(result.current.preferences.fontSize).toBe('medium');
    expect(result.current.preferences.animations).toBe(true);
    expect(result.current.preferences.soundEffects).toBe(false);
    expect(result.current.preferences.compactMode).toBe(false);
    expect(result.current.preferences.showDebugInfo).toBe(false);
  });

  it('should load preferences from localStorage', () => {
    // Arrange
    const savedPreferences = {
      theme: 'dark' as const,
      colorScheme: 'high-contrast' as const,
      fontSize: 'large' as const,
      animations: false,
    };
    localStorage.setItem('mythosmud-ui-preferences', JSON.stringify(savedPreferences));

    // Act
    const wrapper = ({ children }: { children: React.ReactNode }) => <ThemeProvider>{children}</ThemeProvider>;
    const { result } = renderHook(() => useTheme(), { wrapper });

    // Assert
    expect(result.current.preferences.theme).toBe('dark');
    expect(result.current.preferences.colorScheme).toBe('high-contrast');
    expect(result.current.preferences.fontSize).toBe('large');
    expect(result.current.preferences.animations).toBe(false);
  });

  it('should merge initial preferences with defaults', () => {
    // Arrange
    const initialPreferences = {
      theme: 'light' as const,
      compactMode: true,
    };

    // Act
    const wrapper = ({ children }: { children: React.ReactNode }) => (
      <ThemeProvider initialPreferences={initialPreferences}>{children}</ThemeProvider>
    );
    const { result } = renderHook(() => useTheme(), { wrapper });

    // Assert
    expect(result.current.preferences.theme).toBe('light');
    expect(result.current.preferences.compactMode).toBe(true);
    expect(result.current.preferences.fontSize).toBe('medium'); // Default
  });

  it('should update preferences', async () => {
    // Arrange
    const wrapper = ({ children }: { children: React.ReactNode }) => <ThemeProvider>{children}</ThemeProvider>;
    const { result } = renderHook(() => useTheme(), { wrapper });

    // Act
    await act(() => {
      result.current.updatePreferences({ theme: 'dark', fontSize: 'large' });
    });

    // Assert
    expect(result.current.preferences.theme).toBe('dark');
    expect(result.current.preferences.fontSize).toBe('large');
  });

  it('should save preferences to localStorage', async () => {
    // Arrange
    const wrapper = ({ children }: { children: React.ReactNode }) => <ThemeProvider>{children}</ThemeProvider>;
    const { result } = renderHook(() => useTheme(), { wrapper });

    // Act
    await act(() => {
      result.current.updatePreferences({ theme: 'light' });
    });

    // Assert
    const saved = localStorage.getItem('mythosmud-ui-preferences');
    expect(saved).toBeTruthy();
    const parsed = JSON.parse(saved!);
    expect(parsed.theme).toBe('light');
  });

  it('should reset preferences to defaults', async () => {
    // Arrange
    const wrapper = ({ children }: { children: React.ReactNode }) => <ThemeProvider>{children}</ThemeProvider>;
    const { result } = renderHook(() => useTheme(), { wrapper });

    await act(() => {
      result.current.updatePreferences({ theme: 'dark', fontSize: 'large' });
    });

    // Act
    await act(() => {
      result.current.resetPreferences();
    });

    // Assert
    expect(result.current.preferences.theme).toBe('terminal');
    expect(result.current.preferences.fontSize).toBe('medium');
  });

  it('should apply theme classes to document', async () => {
    // Arrange
    const wrapper = ({ children }: { children: React.ReactNode }) => <ThemeProvider>{children}</ThemeProvider>;
    const { result } = renderHook(() => useTheme(), { wrapper });

    // Act
    await act(() => {
      result.current.updatePreferences({
        theme: 'dark',
        colorScheme: 'high-contrast',
        fontSize: 'large',
      });
    });

    // Assert
    expect(document.documentElement.classList.contains('theme-dark')).toBe(true);
    expect(document.documentElement.classList.contains('color-scheme-high-contrast')).toBe(true);
    expect(document.documentElement.classList.contains('font-size-large')).toBe(true);
  });

  it('should apply no-animations class when animations are disabled', async () => {
    // Arrange
    const wrapper = ({ children }: { children: React.ReactNode }) => <ThemeProvider>{children}</ThemeProvider>;
    const { result } = renderHook(() => useTheme(), { wrapper });

    // Act
    await act(() => {
      result.current.updatePreferences({ animations: false });
    });

    // Assert
    expect(document.documentElement.classList.contains('no-animations')).toBe(true);
  });

  it('should apply compact-mode class when compactMode is enabled', async () => {
    // Arrange
    const wrapper = ({ children }: { children: React.ReactNode }) => <ThemeProvider>{children}</ThemeProvider>;
    const { result } = renderHook(() => useTheme(), { wrapper });

    // Act
    await act(() => {
      result.current.updatePreferences({ compactMode: true });
    });

    // Assert
    expect(document.documentElement.classList.contains('compact-mode')).toBe(true);
  });

  it('should handle invalid localStorage data gracefully', () => {
    // Arrange
    localStorage.setItem('mythosmud-ui-preferences', 'invalid json');

    // Act - should not throw
    const wrapper = ({ children }: { children: React.ReactNode }) => <ThemeProvider>{children}</ThemeProvider>;
    const { result } = renderHook(() => useTheme(), { wrapper });

    // Assert - should use defaults
    expect(result.current.preferences.theme).toBe('terminal');
  });

  it('should remove old theme classes when updating', async () => {
    // Arrange
    const wrapper = ({ children }: { children: React.ReactNode }) => <ThemeProvider>{children}</ThemeProvider>;
    const { result } = renderHook(() => useTheme(), { wrapper });

    await act(() => {
      result.current.updatePreferences({ theme: 'light' });
    });

    // Act
    await act(() => {
      result.current.updatePreferences({ theme: 'dark' });
    });

    // Assert
    expect(document.documentElement.classList.contains('theme-light')).toBe(false);
    expect(document.documentElement.classList.contains('theme-dark')).toBe(true);
  });
});
