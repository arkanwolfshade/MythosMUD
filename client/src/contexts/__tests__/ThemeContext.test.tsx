import { describe, expect, it, beforeEach } from 'vitest';
import { renderHook, act } from '@testing-library/react';
import { ThemeProvider } from '../ThemeContext';
import {
  useTheme,
  useThemePreference,
  useColorSchemePreference,
  useFontSizePreference,
  useAnimationPreference,
  useCompactModePreference,
  useAccessibilityPreference,
  useDebugInfoPreference,
} from '../hooks/useThemeContext';

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

describe('useThemeContext convenience hooks', () => {
  beforeEach(() => {
    localStorage.clear();
    document.documentElement.className = '';
  });

  const wrapper = ({ children }: { children: React.ReactNode }) => <ThemeProvider>{children}</ThemeProvider>;

  describe('useThemePreference', () => {
    it('should return current theme and setTheme function', () => {
      const { result } = renderHook(() => useThemePreference(), { wrapper });

      expect(result.current.theme).toBe('terminal');
      expect(typeof result.current.setTheme).toBe('function');
    });

    it('should update theme using setTheme', async () => {
      const { result } = renderHook(() => useThemePreference(), { wrapper });

      await act(() => {
        result.current.setTheme('dark');
      });

      expect(result.current.theme).toBe('dark');
    });
  });

  describe('useColorSchemePreference', () => {
    it('should return current colorScheme and setColorScheme function', () => {
      const { result } = renderHook(() => useColorSchemePreference(), { wrapper });

      expect(result.current.colorScheme).toBe('default');
      expect(typeof result.current.setColorScheme).toBe('function');
    });

    it('should update colorScheme using setColorScheme', async () => {
      const { result } = renderHook(() => useColorSchemePreference(), { wrapper });

      await act(() => {
        result.current.setColorScheme('high-contrast');
      });

      expect(result.current.colorScheme).toBe('high-contrast');
    });
  });

  describe('useFontSizePreference', () => {
    it('should return current fontSize and setFontSize function', () => {
      const { result } = renderHook(() => useFontSizePreference(), { wrapper });

      expect(result.current.fontSize).toBe('medium');
      expect(typeof result.current.setFontSize).toBe('function');
    });

    it('should update fontSize using setFontSize', async () => {
      const { result } = renderHook(() => useFontSizePreference(), { wrapper });

      await act(() => {
        result.current.setFontSize('large');
      });

      expect(result.current.fontSize).toBe('large');
    });
  });

  describe('useAnimationPreference', () => {
    it('should return current animations and setAnimations function', () => {
      const { result } = renderHook(() => useAnimationPreference(), { wrapper });

      expect(result.current.animations).toBe(true);
      expect(typeof result.current.setAnimations).toBe('function');
    });

    it('should update animations using setAnimations', async () => {
      const { result } = renderHook(() => useAnimationPreference(), { wrapper });

      await act(() => {
        result.current.setAnimations(false);
      });

      expect(result.current.animations).toBe(false);
    });
  });

  describe('useCompactModePreference', () => {
    it('should return current compactMode and setCompactMode function', () => {
      const { result } = renderHook(() => useCompactModePreference(), { wrapper });

      expect(result.current.compactMode).toBe(false);
      expect(typeof result.current.setCompactMode).toBe('function');
    });

    it('should update compactMode using setCompactMode', async () => {
      const { result } = renderHook(() => useCompactModePreference(), { wrapper });

      await act(() => {
        result.current.setCompactMode(true);
      });

      expect(result.current.compactMode).toBe(true);
    });
  });

  describe('useAccessibilityPreference', () => {
    it('should return accessibility preferences and setters', () => {
      const { result } = renderHook(() => useAccessibilityPreference(), { wrapper });

      expect(result.current.highContrast).toBe(false);
      expect(result.current.reducedMotion).toBe(false);
      expect(typeof result.current.setHighContrast).toBe('function');
      expect(typeof result.current.setReducedMotion).toBe('function');
    });

    it('should update highContrast using setHighContrast', async () => {
      const { result } = renderHook(() => useAccessibilityPreference(), { wrapper });

      await act(() => {
        result.current.setHighContrast(true);
      });

      expect(result.current.highContrast).toBe(true);
    });

    it('should update reducedMotion using setReducedMotion', async () => {
      const { result } = renderHook(() => useAccessibilityPreference(), { wrapper });

      await act(() => {
        result.current.setReducedMotion(true);
      });

      expect(result.current.reducedMotion).toBe(true);
    });
  });

  describe('useDebugInfoPreference', () => {
    it('should return current showDebugInfo and setShowDebugInfo function', () => {
      const { result } = renderHook(() => useDebugInfoPreference(), { wrapper });

      expect(result.current.showDebugInfo).toBe(false);
      expect(typeof result.current.setShowDebugInfo).toBe('function');
    });

    it('should update showDebugInfo using setShowDebugInfo', async () => {
      const { result } = renderHook(() => useDebugInfoPreference(), { wrapper });

      await act(() => {
        result.current.setShowDebugInfo(true);
      });

      expect(result.current.showDebugInfo).toBe(true);
    });
  });
});

describe('useTheme error handling', () => {
  it('should throw error when used outside ThemeProvider', () => {
    // Arrange - Test line 8: useTheme error branch
    // Act & Assert - should throw error
    expect(() => {
      renderHook(() => useTheme());
    }).toThrow('useTheme must be used within a ThemeProvider');
  });
});
