import React, { useEffect, useLayoutEffect, useRef, useState } from 'react';
import { DraggablePanelResizeHandles } from './DraggablePanelResizeHandles';
import { relativeSizeToAbsolute, relativeToAbsolute } from './draggablePanelUtils';
import { EldritchIcon, MythosIcons } from './ui/EldritchIcon';
import { TerminalButton } from './ui/TerminalButton';
import { useDraggablePanelInteractions } from './useDraggablePanelInteractions';

export interface DraggablePanelProps {
  children: React.ReactNode;
  title: string;
  panelId?: string; // Optional identifier for CSS classes or debugging (no longer used for persistence)
  defaultPosition?: { x: number; y: number };
  defaultSize?: { width: number; height: number };
  minSize?: { width: number; height: number };
  maxSize?: { width: number; height: number };
  onClose?: () => void;
  onMinimize?: () => void;
  onMaximize?: () => void;
  className?: string;
  variant?: 'default' | 'eldritch' | 'elevated';
  zIndex?: number;
  autoSize?: boolean; // New prop for automatic content-based sizing
}

// Drag header and resize handles use mousedown only; window controls use buttons (keyboard-accessible).
/* eslint-disable jsx-a11y/no-static-element-interactions */

export const DraggablePanel: React.FC<DraggablePanelProps> = ({
  children,
  title,
  panelId: _panelId,
  defaultPosition = { x: 50, y: 50 },
  defaultSize = { width: 400, height: 300 },
  minSize = { width: 200, height: 150 },
  maxSize = { width: 800, height: 600 },
  onClose,
  onMinimize,
  onMaximize,
  className = '',
  variant = 'default',
  zIndex = 1000,
  autoSize = false, // Default to false for backward compatibility
}) => {
  // Use CSS Grid positioning if className is provided, otherwise use absolute positioning
  // Check this early to skip unnecessary calculations for grid-positioned panels
  const isGridPositioned = Boolean(className && className.includes('panel-'));

  // Get viewport dimensions
  const getViewportDimensions = () => {
    if (typeof window === 'undefined') return { width: 1920, height: 1080 };
    return { width: window.innerWidth, height: window.innerHeight };
  };

  // Note: viewport state removed as it was unused - code uses getViewportDimensions() instead

  // Skip position/size calculations for grid-positioned panels
  // Note: absoluteDefaultPosition, absoluteDefaultSize, and padding were removed as unused
  // The actual initialization happens inside useState below

  // Initialize position and size state with safe defaults
  // Calculate immediately using current viewport to prevent initial overlap
  const [position, setPosition] = useState(() => {
    if (isGridPositioned) {
      // Grid panels don't use position state for layout
      return { x: 0, y: 0 };
    }
    const vp = getViewportDimensions();
    const w = Math.max(vp.width || window.innerWidth || 1920, 1920);
    const h = Math.max(vp.height || window.innerHeight || 1080, 1080);
    const absPos = relativeToAbsolute(defaultPosition, w, h);
    const absSize = relativeSizeToAbsolute(defaultSize, w, h);
    const padding = 50;
    return {
      x: Math.max(padding, Math.min(absPos.x, w - absSize.width - padding)),
      y: Math.max(padding, Math.min(absPos.y, h - absSize.height - padding)),
    };
  });

  const [size, setSize] = useState(() => {
    if (isGridPositioned) {
      // Grid panels don't use size state for layout
      return { width: 0, height: 0 };
    }
    const vp = getViewportDimensions();
    const w = Math.max(vp.width || window.innerWidth || 1920, 1920);
    const h = Math.max(vp.height || window.innerHeight || 1080, 1080);
    const absSize = relativeSizeToAbsolute(defaultSize, w, h);
    return absSize;
  });

  // Ensure panels are on-screen after mount and when viewport/defaults change
  // For grid panels, this effect is skipped since CSS Grid handles positioning
  // Use useLayoutEffect to run synchronously before paint, preventing visual flash
  // Use refs to track previous values and prevent infinite loops
  const prevDefaultPositionRef = useRef(defaultPosition);
  const prevDefaultSizeRef = useRef(defaultSize);
  const hasInitializedRef = useRef(false);

  useLayoutEffect(() => {
    // Skip position fixing for grid-positioned panels - CSS Grid handles it
    if (isGridPositioned) return;

    // Check if defaults have actually changed (object reference comparison)
    const positionChanged =
      prevDefaultPositionRef.current.x !== defaultPosition.x || prevDefaultPositionRef.current.y !== defaultPosition.y;
    const sizeChanged =
      prevDefaultSizeRef.current.width !== defaultSize.width ||
      prevDefaultSizeRef.current.height !== defaultSize.height;

    // Only update if defaults changed or this is the first initialization
    if (!hasInitializedRef.current || positionChanged || sizeChanged) {
      const fixPosition = () => {
        const currentViewport = getViewportDimensions();
        if (currentViewport.width === 0 || currentViewport.height === 0) {
          // If viewport not ready, use fallback and schedule retry
          const fallbackPos = relativeToAbsolute(defaultPosition, 1920, 1080);
          const fallbackSize = relativeSizeToAbsolute(defaultSize, 1920, 1080);
          const padding = 50;
          const newPos = {
            x: Math.max(padding, Math.min(fallbackPos.x, 1920 - fallbackSize.width - padding)),
            y: Math.max(padding, Math.min(fallbackPos.y, 1080 - fallbackSize.height - padding)),
          };
          // Only update if values actually changed
          setPosition(prev => {
            if (prev.x !== newPos.x || prev.y !== newPos.y) {
              return newPos;
            }
            return prev;
          });
          setSize(prev => {
            if (prev.width !== fallbackSize.width || prev.height !== fallbackSize.height) {
              return fallbackSize;
            }
            return prev;
          });
          // Retry with actual viewport once available
          setTimeout(fixPosition, 0);
          return;
        }

        const currentAbsolutePosition = relativeToAbsolute(
          defaultPosition,
          currentViewport.width,
          currentViewport.height
        );
        const currentAbsoluteSize = relativeSizeToAbsolute(defaultSize, currentViewport.width, currentViewport.height);

        const padding = 50;
        const safePos = {
          x: Math.max(
            padding,
            Math.min(currentAbsolutePosition.x, currentViewport.width - currentAbsoluteSize.width - padding)
          ),
          y: Math.max(
            padding,
            Math.min(currentAbsolutePosition.y, currentViewport.height - currentAbsoluteSize.height - padding)
          ),
        };

        // Only update if values actually changed to prevent infinite loops
        setPosition(prev => {
          if (prev.x !== safePos.x || prev.y !== safePos.y) {
            return safePos;
          }
          return prev;
        });
        setSize(prev => {
          if (prev.width !== currentAbsoluteSize.width || prev.height !== currentAbsoluteSize.height) {
            return currentAbsoluteSize;
          }
          return prev;
        });
      };

      // Run immediately - useLayoutEffect runs synchronously before paint
      fixPosition();
      hasInitializedRef.current = true;
      prevDefaultPositionRef.current = defaultPosition;
      prevDefaultSizeRef.current = defaultSize;
    }
  }, [defaultPosition, defaultSize, isGridPositioned]);
  const isRelativePositionRef = useRef(defaultPosition.x <= 1 && defaultPosition.y <= 1);
  const isRelativeSizeRef = useRef(defaultSize.width <= 1 && defaultSize.height <= 1);

  // Handle window resize - recalculate positions if using relative positioning
  // Skip entirely for grid-positioned panels
  useEffect(() => {
    if (isGridPositioned) return;
    if (!isRelativePositionRef.current && !isRelativeSizeRef.current) {
      // Using absolute positioning, no need to recalculate on resize
      return;
    }

    const handleResize = () => {
      const viewport = getViewportDimensions();

      // If using relative positioning, recalculate absolute position
      if (isRelativePositionRef.current) {
        const newAbsolutePosition = relativeToAbsolute(defaultPosition, viewport.width, viewport.height);
        const padding = 50;
        const safePos = {
          x: Math.max(padding, Math.min(newAbsolutePosition.x, viewport.width - size.width - padding)),
          y: Math.max(padding, Math.min(newAbsolutePosition.y, viewport.height - size.height - padding)),
        };
        setPosition(safePos);
      }

      // If using relative sizing, recalculate absolute size
      if (isRelativeSizeRef.current) {
        const newAbsoluteSize = relativeSizeToAbsolute(defaultSize, viewport.width, viewport.height);
        setSize(newAbsoluteSize);
      }
    };

    window.addEventListener('resize', handleResize);
    return () => {
      window.removeEventListener('resize', handleResize);
    };
  }, [defaultPosition, defaultSize, size.width, size.height, isGridPositioned]);
  const [isMinimized, setIsMinimized] = useState(false);
  const [headerHeight, setHeaderHeight] = useState(40); // Track header height to avoid ref access during render

  const panelRef = useRef<HTMLDivElement>(null);
  const headerRef = useRef<HTMLDivElement>(null);
  const contentRef = useRef<HTMLDivElement>(null);

  // Measure header height to avoid ref access during render
  useEffect(() => {
    if (headerRef.current) {
      setHeaderHeight(headerRef.current.offsetHeight);
    }
  }, [isMinimized]); // Re-measure when minimize state changes

  // Auto-size panel based on content if enabled
  // Skip for grid-positioned panels (grid handles sizing automatically)
  useEffect(() => {
    if (isGridPositioned) return;
    if (autoSize && contentRef.current && !isMinimized) {
      const contentRect = contentRef.current.getBoundingClientRect();
      const contentWidth = contentRect.width;
      const contentHeight = contentRect.height;

      // Calculate optimal size based on content
      const optimalWidth = Math.max(
        minSize.width,
        Math.min(maxSize.width, contentWidth + 40) // Add padding
      );
      const optimalHeight = Math.max(
        minSize.height,
        Math.min(maxSize.height, contentHeight + 80) // Add header height and padding
      );

      // Only resize if the current size is significantly different
      if (Math.abs(size.width - optimalWidth) > 20 || Math.abs(size.height - optimalHeight) > 20) {
        setSize({ width: optimalWidth, height: optimalHeight });
      }
    }
  }, [
    autoSize,
    isMinimized,
    // isMaximized removed from dependencies
    size.width,
    size.height,
    minSize.width,
    minSize.height,
    maxSize.width,
    maxSize.height,
    isGridPositioned,
  ]);

  // baseClasses determined by isGridPositioned (defined earlier)
  const baseClasses = isGridPositioned
    ? 'font-mono bg-mythos-terminal-surface border border-mythos-terminal-border rounded shadow-lg overflow-hidden transition-eldritch duration-eldritch ease-eldritch'
    : 'font-mono bg-mythos-terminal-surface border border-mythos-terminal-border rounded shadow-lg absolute overflow-hidden transition-eldritch duration-eldritch ease-eldritch relative';

  const variantClasses = {
    default: 'text-mythos-terminal-text',
    eldritch:
      'text-mythos-terminal-text border-mythos-terminal-primary shadow-green-900/30 hover:shadow-green-900/50 hover:animate-eldritch-shadow',
    elevated:
      'text-mythos-terminal-text border-mythos-terminal-primary shadow-xl shadow-green-900/20 hover:shadow-2xl hover:shadow-green-900/30',
  };

  const headerClasses = {
    default: 'bg-mythos-terminal-background border-b border-mythos-terminal-border cursor-move select-none',
    eldritch:
      'bg-mythos-terminal-background border-b border-mythos-terminal-primary cursor-move select-none animate-eldritch-glow',
    elevated: 'bg-mythos-terminal-background border-b border-mythos-terminal-primary cursor-move select-none',
  };

  const classes = `draggable-panel ${baseClasses} ${variantClasses[variant]} ${className}`;

  const { handleMouseDown, handleResizeHandleKeyDown, handleHeaderMouseDown } = useDraggablePanelInteractions({
    isGridPositioned,
    position,
    size,
    minSize,
    maxSize,
    setPosition,
    setSize,
    panelRef,
    headerRef,
  });

  const handleMinimize = () => {
    setIsMinimized(!isMinimized);
    onMinimize?.();
  };

  // handleMaximize function removed - maximize button calls onMaximize directly

  const panelStyle: React.CSSProperties = isGridPositioned
    ? {
        // CSS Grid positioning - use relative positioning, let CSS Grid handle layout
        position: 'relative', // Relative positioning works with CSS Grid
        width: '100%', // Fill grid cell width
        height: '100%', // Fill grid cell height
        zIndex,
        // Explicitly prevent any absolute positioning properties
        left: 'auto',
        top: 'auto',
        right: 'auto',
        bottom: 'auto',
      }
    : {
        // Absolute positioning for draggable panels
        position: 'absolute',
        left: position.x,
        top: position.y,
        width: isMinimized ? size.width : size.width,
        height: isMinimized ? 'auto' : size.height,
        zIndex,
      };

  return (
    <div ref={panelRef} className={classes} style={panelStyle}>
      {/* Header */}
      <div
        ref={headerRef}
        className={`flex items-center justify-between px-3 py-2 ${headerClasses[variant]}`}
        onMouseDown={handleHeaderMouseDown}
      >
        <div className="flex items-center space-x-2">
          <EldritchIcon name={MythosIcons.panel} size={16} className="text-mythos-terminal-primary" />
          <span className="text-sm font-bold text-mythos-terminal-primary">{title}</span>
        </div>
        <div className="flex items-center space-x-1">
          {onMinimize && (
            <TerminalButton
              variant="secondary"
              size="sm"
              onClick={handleMinimize}
              className="w-9 h-9 p-0 flex items-center justify-center hover:animate-eldritch-pulse"
            >
              <EldritchIcon name={MythosIcons.minimize} size={12} />
            </TerminalButton>
          )}
          {onMaximize && (
            <TerminalButton
              variant="secondary"
              size="sm"
              onClick={onMaximize}
              className="w-9 h-9 p-0 flex items-center justify-center hover:animate-eldritch-pulse"
            >
              <EldritchIcon name={MythosIcons.maximize} size={12} />
            </TerminalButton>
          )}
          {onClose && (
            <TerminalButton
              variant="danger"
              size="sm"
              onClick={onClose}
              className="w-9 h-9 p-0 flex items-center justify-center hover:animate-eldritch-glow"
            >
              <EldritchIcon name={MythosIcons.close} size={12} />
            </TerminalButton>
          )}
        </div>
      </div>

      {/* Content */}
      {!isMinimized && (
        <div
          ref={contentRef}
          className="p-3 h-full overflow-auto relative bg-mythos-terminal-surface"
          style={{
            height: `calc(100% - ${headerHeight}px)`,
            minHeight: '100px', // Ensure minimum content height
          }}
        >
          {children}
        </div>
      )}

      {/* Resize handles */}
      {!isMinimized && (
        <DraggablePanelResizeHandles onMouseDown={handleMouseDown} onResizeHandleKeyDown={handleResizeHandleKeyDown} />
      )}
    </div>
  );
};
