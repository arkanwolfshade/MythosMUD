import { useCallback, useEffect, useState } from 'react';
import { Layout } from 'react-grid-layout';

// Layout configuration for different screen sizes
export const layoutConfig = {
  lg: [
    { i: 'chat', x: 0, y: 0, w: 6, h: 8, minW: 4, minH: 6 },
    { i: 'gameLog', x: 6, y: 0, w: 6, h: 8, minW: 4, minH: 6 },
    { i: 'command', x: 12, y: 0, w: 4, h: 6, minW: 3, minH: 4 },
    { i: 'roomInfo', x: 0, y: 8, w: 6, h: 4, minW: 4, minH: 3 },
    { i: 'status', x: 12, y: 6, w: 4, h: 6, minW: 3, minH: 4 },
  ],
  md: [
    { i: 'chat', x: 0, y: 0, w: 8, h: 6, minW: 6, minH: 4 },
    { i: 'gameLog', x: 8, y: 0, w: 4, h: 6, minW: 3, minH: 4 },
    { i: 'command', x: 0, y: 6, w: 6, h: 4, minW: 4, minH: 3 },
    { i: 'roomInfo', x: 6, y: 6, w: 6, h: 4, minW: 4, minH: 3 },
    { i: 'status', x: 0, y: 10, w: 12, h: 3, minW: 8, minH: 2 },
  ],
  sm: [
    { i: 'chat', x: 0, y: 0, w: 12, h: 5, minW: 8, minH: 4 },
    { i: 'gameLog', x: 0, y: 5, w: 12, h: 5, minW: 8, minH: 4 },
    { i: 'command', x: 0, y: 10, w: 12, h: 4, minW: 8, minH: 3 },
    { i: 'roomInfo', x: 0, y: 14, w: 12, h: 4, minW: 8, minH: 3 },
    { i: 'status', x: 0, y: 18, w: 12, h: 3, minW: 8, minH: 2 },
  ],
};

// Storage keys for persistence
const STORAGE_KEYS = {
  LAYOUT: 'mythosMUD-panel-layout',
  BREAKPOINT: 'mythosMUD-panel-breakpoint',
  PANEL_STATES: 'mythosMUD-panel-states',
};

// Panel state interface
export interface PanelState {
  isMinimized: boolean;
  isMaximized: boolean;
  isVisible: boolean;
}

// Hook return interface
export interface UseGridLayoutReturn {
  currentLayout: Layout[];
  currentBreakpoint: string;
  panelStates: Record<string, PanelState>;
  onLayoutChange: (layout: Layout[]) => void;
  onBreakpointChange: (breakpoint: string) => void;
  resetLayout: () => void;
  togglePanelState: (panelId: string, state: keyof PanelState) => void;
  saveLayout: () => void;
  loadLayout: () => void;
}

export const useGridLayout = (): UseGridLayoutReturn => {
  // State management - initialize from localStorage to avoid setState in effect
  const [currentLayout, setCurrentLayout] = useState<Layout[]>(() => {
    try {
      const savedLayout = localStorage.getItem(STORAGE_KEYS.LAYOUT);
      if (savedLayout) {
        return JSON.parse(savedLayout);
      }
    } catch (error) {
      console.warn('Failed to load layout:', error);
    }
    return layoutConfig.lg;
  });

  const [currentBreakpoint, setCurrentBreakpoint] = useState<string>(() => {
    try {
      const savedBreakpoint = localStorage.getItem(STORAGE_KEYS.BREAKPOINT);
      if (savedBreakpoint) {
        return savedBreakpoint;
      }
    } catch (error) {
      console.warn('Failed to load breakpoint:', error);
    }
    return 'lg';
  });

  const [panelStates, setPanelStates] = useState<Record<string, PanelState>>(() => {
    try {
      const savedPanelStates = localStorage.getItem(STORAGE_KEYS.PANEL_STATES);
      if (savedPanelStates) {
        return JSON.parse(savedPanelStates);
      }
    } catch (error) {
      console.warn('Failed to load panel states:', error);
    }
    return {
      chat: { isMinimized: false, isMaximized: false, isVisible: true },
      gameLog: { isMinimized: false, isMaximized: false, isVisible: true },
      command: { isMinimized: false, isMaximized: false, isVisible: true },
      roomInfo: { isMinimized: false, isMaximized: false, isVisible: true },
      status: { isMinimized: false, isMaximized: false, isVisible: true },
    };
  });

  // Save layout to localStorage
  const saveLayout = useCallback(() => {
    try {
      localStorage.setItem(STORAGE_KEYS.LAYOUT, JSON.stringify(currentLayout));
      localStorage.setItem(STORAGE_KEYS.BREAKPOINT, currentBreakpoint);
      localStorage.setItem(STORAGE_KEYS.PANEL_STATES, JSON.stringify(panelStates));
    } catch (error) {
      console.warn('Failed to save panel layout:', error);
    }
  }, [currentLayout, currentBreakpoint, panelStates]);

  // Load layout from localStorage
  const loadLayout = useCallback(() => {
    try {
      const savedLayout = localStorage.getItem(STORAGE_KEYS.LAYOUT);
      const savedBreakpoint = localStorage.getItem(STORAGE_KEYS.BREAKPOINT);
      const savedPanelStates = localStorage.getItem(STORAGE_KEYS.PANEL_STATES);

      if (savedLayout) {
        setCurrentLayout(JSON.parse(savedLayout));
      }

      if (savedBreakpoint) {
        setCurrentBreakpoint(savedBreakpoint);
      }

      if (savedPanelStates) {
        setPanelStates(JSON.parse(savedPanelStates));
      }
    } catch (error) {
      console.warn('Failed to load panel layout:', error);
    }
  }, []);

  // Handle layout changes
  const onLayoutChange = useCallback((layout: Layout[]) => {
    setCurrentLayout(layout);
  }, []);

  // Handle breakpoint changes
  const onBreakpointChange = useCallback((breakpoint: string) => {
    setCurrentBreakpoint(breakpoint);
    const newLayout = layoutConfig[breakpoint as keyof typeof layoutConfig] || layoutConfig.lg;
    setCurrentLayout(newLayout);
  }, []);

  // Reset layout to default
  const resetLayout = useCallback(() => {
    const defaultLayout = layoutConfig[currentBreakpoint as keyof typeof layoutConfig] || layoutConfig.lg;
    setCurrentLayout(defaultLayout);

    // Reset panel states
    setPanelStates({
      chat: { isMinimized: false, isMaximized: false, isVisible: true },
      gameLog: { isMinimized: false, isMaximized: false, isVisible: true },
      command: { isMinimized: false, isMaximized: false, isVisible: true },
      roomInfo: { isMinimized: false, isMaximized: false, isVisible: true },
      status: { isMinimized: false, isMaximized: false, isVisible: true },
    });

    // Clear localStorage
    localStorage.removeItem(STORAGE_KEYS.LAYOUT);
    localStorage.removeItem(STORAGE_KEYS.BREAKPOINT);
    localStorage.removeItem(STORAGE_KEYS.PANEL_STATES);
  }, [currentBreakpoint]);

  // Toggle panel state (minimize, maximize, visibility)
  const togglePanelState = useCallback((panelId: string, state: keyof PanelState) => {
    setPanelStates(prev => ({
      ...prev,
      [panelId]: {
        ...prev[panelId],
        [state]: !prev[panelId][state],
      },
    }));
  }, []);

  // Auto-save layout when it changes
  useEffect(() => {
    saveLayout();
  }, [saveLayout]);

  // Layout is now loaded during state initialization, no need for effect

  return {
    currentLayout,
    currentBreakpoint,
    panelStates,
    onLayoutChange,
    onBreakpointChange,
    resetLayout,
    togglePanelState,
    saveLayout,
    loadLayout,
  };
};

export default useGridLayout;
