import React, { createContext, ReactNode, useCallback, useState } from 'react';

// Panel types
export interface PanelPosition {
  x: number;
  y: number;
}

export interface PanelSize {
  width: number;
  height: number;
}

export interface PanelState {
  id: string;
  title: string;
  isVisible: boolean;
  isMinimized: boolean;
  isMaximized: boolean;
  position: PanelPosition;
  size: PanelSize;
  zIndex: number;
}

export interface PanelLayout {
  [panelId: string]: PanelState;
}

// Panel management context type
export interface PanelContextType {
  panels: PanelLayout;
  addPanel: (id: string, title: string, initialPosition?: PanelPosition, initialSize?: PanelSize) => void;
  removePanel: (id: string) => void;
  updatePanel: (id: string, updates: Partial<PanelState>) => void;
  togglePanelVisibility: (id: string) => void;
  togglePanelMinimized: (id: string) => void;
  togglePanelMaximized: (id: string) => void;
  movePanel: (id: string, position: PanelPosition) => void;
  resizePanel: (id: string, size: PanelSize) => void;
  bringToFront: (id: string) => void;
  resetPanelLayout: () => void;
  getNextZIndex: () => number;
}

// Default panel configurations
const defaultPanels: PanelLayout = {
  chat: {
    id: 'chat',
    title: 'Chat',
    isVisible: true,
    isMinimized: false,
    isMaximized: false,
    position: { x: 50, y: 50 },
    size: { width: 500, height: 400 },
    zIndex: 1,
  },
  'game-log': {
    id: 'game-log',
    title: 'Game Log',
    isVisible: true,
    isMinimized: false,
    isMaximized: false,
    position: { x: 600, y: 50 },
    size: { width: 500, height: 400 },
    zIndex: 2,
  },
  commands: {
    id: 'commands',
    title: 'Commands',
    isVisible: true,
    isMinimized: false,
    isMaximized: false,
    position: { x: 50, y: 500 },
    size: { width: 500, height: 200 },
    zIndex: 3,
  },
  'room-info': {
    id: 'room-info',
    title: 'Room Info',
    isVisible: true,
    isMinimized: false,
    isMaximized: false,
    position: { x: 600, y: 500 },
    size: { width: 300, height: 300 },
    zIndex: 4,
  },
  status: {
    id: 'status',
    title: 'Status',
    isVisible: true,
    isMinimized: false,
    isMaximized: false,
    position: { x: 950, y: 50 },
    size: { width: 300, height: 200 },
    zIndex: 5,
  },
};

// Create context
export const PanelContext = createContext<PanelContextType | null>(null);

// Context provider
interface PanelProviderProps {
  children: ReactNode;
  initialPanels?: PanelLayout;
}

export const PanelProvider: React.FC<PanelProviderProps> = ({ children, initialPanels = defaultPanels }) => {
  const [panels, setPanels] = useState<PanelLayout>(() => {
    // Load from localStorage if available
    const saved = localStorage.getItem('mythosmud-panel-layout');
    if (saved) {
      try {
        const parsed = JSON.parse(saved);
        return { ...initialPanels, ...parsed };
      } catch {
        // If parsing fails, use initial panels
      }
    }
    return initialPanels;
  });

  // Save to localStorage whenever panels change
  React.useEffect(() => {
    localStorage.setItem('mythosmud-panel-layout', JSON.stringify(panels));
  }, [panels]);

  const addPanel = useCallback(
    (id: string, title: string, initialPosition?: PanelPosition, initialSize?: PanelSize) => {
      setPanels(prev => ({
        ...prev,
        [id]: {
          id,
          title,
          isVisible: true,
          isMinimized: false,
          isMaximized: false,
          position: initialPosition || { x: 100, y: 100 },
          size: initialSize || { width: 400, height: 300 },
          zIndex: Math.max(...Object.values(prev).map(p => p.zIndex), 0) + 1,
        },
      }));
    },
    []
  );

  const removePanel = useCallback((id: string) => {
    setPanels(prev => {
      const newPanels = { ...prev };
      delete newPanels[id];
      return newPanels;
    });
  }, []);

  const updatePanel = useCallback((id: string, updates: Partial<PanelState>) => {
    setPanels(prev => ({
      ...prev,
      [id]: {
        ...prev[id],
        ...updates,
      },
    }));
  }, []);

  const togglePanelVisibility = useCallback((id: string) => {
    setPanels(prev => ({
      ...prev,
      [id]: {
        ...prev[id],
        isVisible: !prev[id].isVisible,
      },
    }));
  }, []);

  const togglePanelMinimized = useCallback((id: string) => {
    setPanels(prev => ({
      ...prev,
      [id]: {
        ...prev[id],
        isMinimized: !prev[id].isMinimized,
        isMaximized: false, // Can't be maximized and minimized at the same time
      },
    }));
  }, []);

  const togglePanelMaximized = useCallback((id: string) => {
    setPanels(prev => ({
      ...prev,
      [id]: {
        ...prev[id],
        isMaximized: !prev[id].isMaximized,
        isMinimized: false, // Can't be maximized and minimized at the same time
      },
    }));
  }, []);

  const movePanel = useCallback((id: string, position: PanelPosition) => {
    setPanels(prev => ({
      ...prev,
      [id]: {
        ...prev[id],
        position,
      },
    }));
  }, []);

  const resizePanel = useCallback((id: string, size: PanelSize) => {
    setPanels(prev => ({
      ...prev,
      [id]: {
        ...prev[id],
        size,
      },
    }));
  }, []);

  const bringToFront = useCallback((id: string) => {
    setPanels(prev => {
      const maxZIndex = Math.max(...Object.values(prev).map(p => p.zIndex));
      return {
        ...prev,
        [id]: {
          ...prev[id],
          zIndex: maxZIndex + 1,
        },
      };
    });
  }, []);

  const resetPanelLayout = useCallback(() => {
    setPanels(defaultPanels);
  }, []);

  const getNextZIndex = useCallback(() => {
    return Math.max(...Object.values(panels).map(p => p.zIndex), 0) + 1;
  }, [panels]);

  const value: PanelContextType = {
    panels,
    addPanel,
    removePanel,
    updatePanel,
    togglePanelVisibility,
    togglePanelMinimized,
    togglePanelMaximized,
    movePanel,
    resizePanel,
    bringToFront,
    resetPanelLayout,
    getNextZIndex,
  };

  return <PanelContext.Provider value={value}>{children}</PanelContext.Provider>;
};
