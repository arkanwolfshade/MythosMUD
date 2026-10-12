/* eslint-disable react-refresh/only-export-components */
// Disabled: Context files intentionally export both context and provider
import type { ReactNode } from 'react';
import React, { createContext, useEffect, useState } from 'react';

// Theme types
export type Theme = 'light' | 'dark' | 'terminal';
export type ColorScheme = 'default' | 'high-contrast' | 'eldritch';
export type FontSize = 'small' | 'medium' | 'large';

// UI preferences
interface UIPreferences {
  theme: Theme;
  colorScheme: ColorScheme;
  fontSize: FontSize;
  animations: boolean;
  soundEffects: boolean;
  compactMode: boolean;
  showDebugInfo: boolean;
  highContrast: boolean;
  reducedMotion: boolean;
  /** #804: corruption's chat-pane grain overlay. Presentation-only (ADR-025), so a client toggle
   * over it carries no fairness concern the way toggling a server-side effect would (ADR-024). */
  chatGrain: boolean;
  /** Message-category glyphs are swapped for bracketed text prefixes such as [Combat]. */
  textLabels: boolean;
}

// Context type
interface ThemeContextType {
  preferences: UIPreferences;
  updatePreferences: (updates: Partial<UIPreferences>) => void;
  resetPreferences: () => void;
}

// Default preferences
const defaultPreferences: UIPreferences = {
  theme: 'terminal',
  colorScheme: 'default',
  fontSize: 'medium',
  animations: true,
  soundEffects: false,
  compactMode: false,
  showDebugInfo: false,
  highContrast: false,
  reducedMotion: false,
  chatGrain: true,
  textLabels: false,
};

const PREFERENCES_STORAGE_KEY = 'mythosmud-ui-preferences';

// Create context
export const ThemeContext = createContext<ThemeContextType | null>(null);

// Export context type for hooks
export type { ThemeContextType };

// Context provider
interface ThemeProviderProps {
  children: ReactNode;
  initialPreferences?: Partial<UIPreferences>;
}

export const ThemeProvider: React.FC<ThemeProviderProps> = ({ children, initialPreferences = {} }) => {
  const [preferences, setPreferences] = useState<UIPreferences>(() => {
    // Load from localStorage if available; storage can be blocked or throw (private windows)
    try {
      const saved = localStorage.getItem(PREFERENCES_STORAGE_KEY);
      if (saved) {
        const parsed = JSON.parse(saved);
        return { ...defaultPreferences, ...parsed, ...initialPreferences };
      }
    } catch {
      // If storage is unavailable or parsing fails, use defaults
    }
    return { ...defaultPreferences, ...initialPreferences };
  });

  // Save to localStorage whenever preferences change
  useEffect(() => {
    try {
      localStorage.setItem(PREFERENCES_STORAGE_KEY, JSON.stringify(preferences));
    } catch {
      // Preferences still apply for this session when storage is unavailable
    }
  }, [preferences]);

  // Apply theme classes to document
  useEffect(() => {
    const root = document.documentElement;

    // Remove existing theme classes
    root.classList.remove('theme-light', 'theme-dark', 'theme-terminal');
    root.classList.remove('color-scheme-default', 'color-scheme-high-contrast', 'color-scheme-eldritch');
    root.classList.remove('font-size-small', 'font-size-medium', 'font-size-large');

    // Add new theme classes
    root.classList.add(`theme-${preferences.theme}`);
    root.classList.add(`color-scheme-${preferences.colorScheme}`);
    root.classList.add(`font-size-${preferences.fontSize}`);

    // Apply animations preference
    if (!preferences.animations) {
      root.classList.add('no-animations');
    } else {
      root.classList.remove('no-animations');
    }

    // Apply compact mode
    if (preferences.compactMode) {
      root.classList.add('compact-mode');
    } else {
      root.classList.remove('compact-mode');
    }

    // messageCategories.css keys its AAA palette and text-label mode off these classes
    root.classList.toggle('high-contrast', preferences.highContrast);
    root.classList.toggle('text-labels', preferences.textLabels);
  }, [preferences]);

  const updatePreferences = (updates: Partial<UIPreferences>) => {
    setPreferences(prev => ({ ...prev, ...updates }));
  };

  const resetPreferences = () => {
    setPreferences(defaultPreferences);
  };

  const value: ThemeContextType = {
    preferences,
    updatePreferences,
    resetPreferences,
  };

  return <ThemeContext.Provider value={value}>{children}</ThemeContext.Provider>;
};

// Convenience hooks for specific preferences
