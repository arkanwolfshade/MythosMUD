import { useContext } from 'react';
import { ColorScheme, FontSize, Theme, ThemeContext, ThemeContextType } from '../ThemeContext';

// Hook to use theme context
export const useTheme = (): ThemeContextType => {
  const context = useContext(ThemeContext);
  if (!context) {
    throw new Error('useTheme must be used within a ThemeProvider');
  }
  return context;
};

// Convenience hooks for specific preferences
export const useThemePreference = () => {
  const { preferences, updatePreferences } = useTheme();
  return {
    theme: preferences.theme,
    setTheme: (theme: Theme) => updatePreferences({ theme }),
  };
};

export const useColorSchemePreference = () => {
  const { preferences, updatePreferences } = useTheme();
  return {
    colorScheme: preferences.colorScheme,
    setColorScheme: (colorScheme: ColorScheme) => updatePreferences({ colorScheme }),
  };
};

export const useFontSizePreference = () => {
  const { preferences, updatePreferences } = useTheme();
  return {
    fontSize: preferences.fontSize,
    setFontSize: (fontSize: FontSize) => updatePreferences({ fontSize }),
  };
};

export const useAnimationPreference = () => {
  const { preferences, updatePreferences } = useTheme();
  return {
    animations: preferences.animations,
    setAnimations: (animations: boolean) => updatePreferences({ animations }),
  };
};

export const useCompactModePreference = () => {
  const { preferences, updatePreferences } = useTheme();
  return {
    compactMode: preferences.compactMode,
    setCompactMode: (compactMode: boolean) => updatePreferences({ compactMode }),
  };
};

export const useAccessibilityPreference = () => {
  const { preferences, updatePreferences } = useTheme();
  return {
    highContrast: preferences.highContrast,
    setHighContrast: (highContrast: boolean) => updatePreferences({ highContrast }),
    reducedMotion: preferences.reducedMotion,
    setReducedMotion: (reducedMotion: boolean) => updatePreferences({ reducedMotion }),
  };
};

export const useDebugInfoPreference = () => {
  const { preferences, updatePreferences } = useTheme();
  return {
    showDebugInfo: preferences.showDebugInfo,
    setShowDebugInfo: (showDebugInfo: boolean) => updatePreferences({ showDebugInfo }),
  };
};
