import React, { useCallback, useEffect, useState } from 'react';
import { Layout, Responsive, WidthProvider } from 'react-grid-layout';
import 'react-grid-layout/css/styles.css';
import 'react-resizable/css/styles.css';

const ResponsiveGridLayout = WidthProvider(Responsive);

// Define the layout configuration for different screen sizes
const layoutConfig = {
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

// Panel component interface
interface PanelComponent {
  id: string;
  title: string;
  component: React.ReactNode;
  variant?: 'eldritch' | 'default' | 'elevated';
}

interface GridLayoutManagerProps {
  panels: PanelComponent[];
  onLayoutChange?: (layout: Layout[]) => void;
  className?: string;
}

export const GridLayoutManager: React.FC<GridLayoutManagerProps> = ({ panels, onLayoutChange, className = '' }) => {
  // State for current layout
  const [currentLayout, setCurrentLayout] = useState<Layout[]>(layoutConfig.lg);
  const [breakpoint, setBreakpoint] = useState<string>('lg');

  // Handle layout changes
  const handleLayoutChange = useCallback(
    (layout: Layout[], _allLayouts: Record<string, Layout[]>) => {
      setCurrentLayout(layout);
      onLayoutChange?.(layout);
    },
    [onLayoutChange]
  );

  // Save layout to localStorage
  const saveLayout = useCallback(
    (layout: Layout[]) => {
      try {
        localStorage.setItem('mythosMUD-panel-layout', JSON.stringify(layout));
        localStorage.setItem('mythosMUD-panel-breakpoint', breakpoint);
      } catch (error) {
        console.warn('Failed to save panel layout:', error);
      }
    },
    [breakpoint]
  );

  // Load layout from localStorage
  const loadLayout = useCallback(() => {
    try {
      const savedLayout = localStorage.getItem('mythosMUD-panel-layout');
      const savedBreakpoint = localStorage.getItem('mythosMUD-panel-breakpoint');

      if (savedLayout && savedBreakpoint) {
        const parsedLayout = JSON.parse(savedLayout);
        setCurrentLayout(parsedLayout);
        setBreakpoint(savedBreakpoint);
      }
    } catch (error) {
      console.warn('Failed to load panel layout:', error);
    }
  }, []);

  // Reset layout to default
  const resetLayout = useCallback(() => {
    const defaultLayout = layoutConfig[breakpoint as keyof typeof layoutConfig] || layoutConfig.lg;
    setCurrentLayout(defaultLayout);
    localStorage.removeItem('mythosMUD-panel-layout');
    localStorage.removeItem('mythosMUD-panel-breakpoint');
  }, [breakpoint]);

  // Load saved layout on mount
  useEffect(() => {
    loadLayout();
  }, [loadLayout]);

  // Save layout when it changes
  useEffect(() => {
    saveLayout(currentLayout);
  }, [currentLayout, saveLayout]);

  // Handle breakpoint change
  const handleBreakpointChange = useCallback((newBreakpoint: string) => {
    setBreakpoint(newBreakpoint);
    const newLayout = layoutConfig[newBreakpoint as keyof typeof layoutConfig] || layoutConfig.lg;
    setCurrentLayout(newLayout);
  }, []);

  return (
    <div className={`grid-layout-manager ${className}`}>
      {/* Layout Controls */}
      <div className="layout-controls mb-4 flex gap-2">
        <button
          onClick={resetLayout}
          className="px-3 py-1 bg-mythos-terminal-surface text-mythos-terminal-text rounded border border-mythos-terminal-border hover:bg-mythos-terminal-primary/20"
        >
          Reset Layout
        </button>
        <span className="px-3 py-1 bg-mythos-terminal-surface text-mythos-terminal-text-secondary rounded border border-mythos-terminal-border">
          Breakpoint: {breakpoint.toUpperCase()}
        </span>
      </div>

      {/* React Grid Layout Container */}
      <ResponsiveGridLayout
        className="layout"
        layouts={layoutConfig}
        breakpoints={{ lg: 1200, md: 996, sm: 768, xs: 480 }}
        cols={{ lg: 16, md: 12, sm: 12, xs: 4 }}
        rowHeight={30}
        onLayoutChange={handleLayoutChange}
        onBreakpointChange={handleBreakpointChange}
        isDraggable={true}
        isResizable={true}
        preventCollision={true}
        compactType="vertical"
        margin={[20, 20]}
        containerPadding={[20, 20]}
        useCSSTransforms={true}
        transformScale={1}
        draggableHandle=".panel-drag-handle"
        resizeHandles={['se', 'sw', 'ne', 'nw']}
      >
        {panels.map(panel => (
          <div key={panel.id} className={`panel-container panel-${panel.id}`}>
            <div className="panel-drag-handle cursor-move p-2 bg-mythos-terminal-surface border-b border-mythos-terminal-border">
              <h3 className="text-mythos-terminal-text font-bold text-lg">{panel.title}</h3>
            </div>
            <div className="panel-content p-4 bg-mythos-terminal-surface">{panel.component}</div>
          </div>
        ))}
      </ResponsiveGridLayout>
    </div>
  );
};

export default GridLayoutManager;
