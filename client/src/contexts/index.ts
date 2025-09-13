// Context Providers - MythosMUD Client
// This file exports all context providers and hooks for managing global state

// Game Terminal Context
export * from './GameTerminalContext';

// Theme Context
export * from './ThemeContext';

// Panel Context
export * from './PanelContext';

// Combined provider for easy setup
export { GameTerminalProvider } from './GameTerminalContext';
export { PanelProvider } from './PanelContext';
export { ThemeProvider } from './ThemeContext';

// Re-export commonly used types
export type { ColorScheme, FontSize, Theme, UIPreferences } from './ThemeContext';

export type { PanelLayout, PanelPosition, PanelSize, PanelState } from './PanelContext';
