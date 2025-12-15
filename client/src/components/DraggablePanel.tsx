import React, { useCallback, useEffect, useLayoutEffect, useRef, useState } from 'react';
import { EldritchIcon, MythosIcons } from './ui/EldritchIcon';
import { TerminalButton } from './ui/TerminalButton';

interface DraggablePanelProps {
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

// Helper function to convert relative position (0-1) to absolute pixels
const relativeToAbsolute = (
  relative: { x: number; y: number },
  viewportWidth: number,
  viewportHeight: number
): { x: number; y: number } => {
  // If values are > 1, treat as absolute pixels; otherwise treat as percentage (0-1)
  const x = relative.x > 1 ? relative.x : relative.x * viewportWidth;
  const y = relative.y > 1 ? relative.y : relative.y * viewportHeight;
  return { x: Math.round(x), y: Math.round(y) };
};

// Helper function to convert relative size (0-1) to absolute pixels
const relativeSizeToAbsolute = (
  relative: { width: number; height: number },
  viewportWidth: number,
  viewportHeight: number
): { width: number; height: number } => {
  // If values are > 1, treat as absolute pixels; otherwise treat as percentage (0-1)
  const width = relative.width > 1 ? relative.width : relative.width * viewportWidth;
  const height = relative.height > 1 ? relative.height : relative.height * viewportHeight;
  return { width: Math.round(width), height: Math.round(height) };
};

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
  const isGridPositioned = className && className.includes('panel-');

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
  useLayoutEffect(() => {
    // Skip position fixing for grid-positioned panels - CSS Grid handles it
    if (isGridPositioned) return;

    const fixPosition = () => {
      const currentViewport = getViewportDimensions();
      if (currentViewport.width === 0 || currentViewport.height === 0) {
        // If viewport not ready, use fallback and schedule retry
        const fallbackPos = relativeToAbsolute(defaultPosition, 1920, 1080);
        const fallbackSize = relativeSizeToAbsolute(defaultSize, 1920, 1080);
        const padding = 50;
        setPosition({
          x: Math.max(padding, Math.min(fallbackPos.x, 1920 - fallbackSize.width - padding)),
          y: Math.max(padding, Math.min(fallbackPos.y, 1080 - fallbackSize.height - padding)),
        });
        setSize(fallbackSize);
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

      // Always use safe default position - no localStorage persistence
      setPosition(safePos);
      setSize(currentAbsoluteSize);
    };

    // Run immediately - useLayoutEffect runs synchronously before paint
    fixPosition();
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
  const [isDragging, setIsDragging] = useState(false);
  const [isResizing, setIsResizing] = useState(false);
  const [isMinimized, setIsMinimized] = useState(false);
  // isMaximized state removed - maximize state managed by parent component
  const [dragOffset, setDragOffset] = useState({ x: 0, y: 0 });
  const [resizeDirection, setResizeDirection] = useState<string>('');
  const [headerHeight, setHeaderHeight] = useState(40); // Track header height to avoid ref access during render
  const dragStartPositionRef = useRef<{ x: number; y: number } | null>(null); // Track where drag started
  const hasDraggedRef = useRef(false); // Track if actual dragging occurred (not just a click)

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
    ? 'font-mono bg-mythos-terminal-surface border border-gray-700 rounded shadow-lg overflow-hidden transition-eldritch duration-eldritch ease-eldritch'
    : 'font-mono bg-mythos-terminal-surface border border-gray-700 rounded shadow-lg absolute overflow-hidden transition-eldritch duration-eldritch ease-eldritch relative';

  const variantClasses = {
    default: 'text-mythos-terminal-text',
    eldritch:
      'text-mythos-terminal-text border-mythos-terminal-primary shadow-green-900/30 hover:shadow-green-900/50 hover:animate-eldritch-shadow',
    elevated:
      'text-mythos-terminal-text border-mythos-terminal-primary shadow-xl shadow-green-900/20 hover:shadow-2xl hover:shadow-green-900/30',
  };

  const headerClasses = {
    default: 'bg-mythos-terminal-background border-b border-gray-700 cursor-move select-none',
    eldritch:
      'bg-mythos-terminal-background border-b border-mythos-terminal-primary cursor-move select-none animate-eldritch-glow',
    elevated: 'bg-mythos-terminal-background border-b border-mythos-terminal-primary cursor-move select-none',
  };

  const classes = `draggable-panel ${baseClasses} ${variantClasses[variant]} ${className}`;

  const handleMouseDown = (e: React.MouseEvent, direction: string) => {
    e.preventDefault();
    setIsResizing(true);
    setResizeDirection(direction);
  };

  const handleHeaderMouseDown = (e: React.MouseEvent) => {
    // Only allow dragging from the header, not buttons or other interactive elements
    const target = e.target as HTMLElement;
    if (
      target.closest('button') ||
      target.closest('[role="button"]') ||
      target.closest('.terminal-button') ||
      target.closest('input') ||
      target.closest('select')
    ) {
      // Don't start dragging if clicking on interactive elements
      return;
    }

    if (e.target === headerRef.current || headerRef.current?.contains(e.target as Node)) {
      e.preventDefault();
      e.stopPropagation();

      const rect = panelRef.current?.getBoundingClientRect();
      if (rect) {
        // Store the starting position and mouse position
        dragStartPositionRef.current = { x: e.clientX, y: e.clientY };
        hasDraggedRef.current = false;

        // Calculate drag offset correctly: mouse position relative to panel's current screen position
        setDragOffset({
          x: e.clientX - rect.left,
          y: e.clientY - rect.top,
        });

        setIsDragging(true);
      }
    }
  };

  const handleMouseMove = useCallback(
    (e: MouseEvent) => {
      if (isDragging) {
        // Check if this is actual dragging (mouse moved) or just a click
        if (dragStartPositionRef.current) {
          const deltaX = Math.abs(e.clientX - dragStartPositionRef.current.x);
          const deltaY = Math.abs(e.clientY - dragStartPositionRef.current.y);
          const dragThreshold = 3; // Minimum pixels to move before considering it a drag

          if (deltaX > dragThreshold || deltaY > dragThreshold) {
            hasDraggedRef.current = true;
          }
        }

        // Only update position if we've actually dragged (not just clicked)
        if (hasDraggedRef.current) {
          const newX = e.clientX - dragOffset.x;
          const newY = e.clientY - dragOffset.y;

          // Get viewport dimensions to constrain panels within screen bounds
          const viewportWidth = window.innerWidth;
          const viewportHeight = window.innerHeight;

          // Header height - panels should not drag above the header
          const headerHeight = 60; // Approximate header height

          // Round to nearest pixel for smooth dragging
          let constrainedX = Math.round(newX);
          let constrainedY = Math.round(newY);

          // Allow dragging with minimal constraints
          // Allow panels to reach exactly x: 0 (screen left edge)
          // Allow reasonable overflow so panels can be dragged back if needed

          // Calculate maximum allowed positions
          const maxX = viewportWidth - size.width; // Right edge of screen
          const maxY = viewportHeight - size.height; // Bottom edge of screen

          // Allow panels to reach exactly x: 0
          // Allow up to 100px off-screen horizontally so panels can be dragged back if needed
          const minX = -100; // Allow 100px off left edge

          // Constrain vertical position to be below header
          // Allow slight overflow (10px) for recovery, but prevent going above header
          const minY = headerHeight - 10; // Allow panels to be just below header

          // Snap to edges when very close - make it easier to reach x: 0
          // If mouse is very close to left edge (within 20px), snap panel to x: 0
          if (e.clientX <= 20 && constrainedX >= -20 && constrainedX <= 20) {
            constrainedX = 0;
          }
          // If mouse is very close to header bottom (within 20px), snap panel to just below header
          if (
            e.clientY <= headerHeight + 20 &&
            constrainedY >= headerHeight - 20 &&
            constrainedY <= headerHeight + 20
          ) {
            constrainedY = headerHeight;
          }

          // Apply constraints - allow reaching exactly x: 0, constrain to below header
          const newPosition = {
            x: Math.max(minX, Math.min(constrainedX, maxX)),
            y: Math.max(minY, Math.min(constrainedY, maxY)),
          };
          setPosition(newPosition);
        }
      }

      if (isResizing) {
        const rect = panelRef.current?.getBoundingClientRect();
        if (rect) {
          const headerHeight = 60; // Header height - panels should not resize above header

          let newWidth = size.width;
          let newHeight = size.height;
          let newX = position.x;
          let newY = position.y;

          if (resizeDirection.includes('e')) {
            newWidth = Math.max(minSize.width, Math.min(maxSize.width, e.clientX - rect.left));
          }
          if (resizeDirection.includes('w')) {
            const deltaX = rect.right - e.clientX;
            newWidth = Math.max(minSize.width, Math.min(maxSize.width, size.width + deltaX));
            newX = position.x + (size.width - newWidth);
          }
          if (resizeDirection.includes('s')) {
            newHeight = Math.max(minSize.height, Math.min(maxSize.height, e.clientY - rect.top));
          }
          if (resizeDirection.includes('n')) {
            const deltaY = rect.bottom - e.clientY;
            newHeight = Math.max(minSize.height, Math.min(maxSize.height, size.height + deltaY));
            newY = position.y + (size.height - newHeight);

            // Ensure panel doesn't resize above header
            if (newY < headerHeight) {
              const adjustment = headerHeight - newY;
              newY = headerHeight;
              newHeight = Math.max(minSize.height, newHeight - adjustment);
            }
          }

          const newSize = { width: newWidth, height: newHeight };
          const newPosition = { x: newX, y: newY };
          setSize(newSize);
          setPosition(newPosition);
        }
      }
    },
    [isDragging, isResizing, dragOffset, resizeDirection, position, size, minSize, maxSize]
  );

  const handleMouseUp = () => {
    // Reset drag state
    setIsDragging(false);
    setIsResizing(false);
    setResizeDirection('');
    dragStartPositionRef.current = null;
    hasDraggedRef.current = false;
  };

  const handleMinimize = () => {
    setIsMinimized(!isMinimized);
    onMinimize?.();
  };

  // handleMaximize function removed - maximize button calls onMaximize directly

  useEffect(() => {
    if (isDragging || isResizing) {
      document.addEventListener('mousemove', handleMouseMove);
      document.addEventListener('mouseup', handleMouseUp);
      return () => {
        document.removeEventListener('mousemove', handleMouseMove);
        document.removeEventListener('mouseup', handleMouseUp);
      };
    }
  }, [isDragging, isResizing, dragOffset, resizeDirection, position, size, handleMouseMove]);

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
              className="w-6 h-6 p-0 flex items-center justify-center hover:animate-eldritch-pulse"
            >
              <EldritchIcon name={MythosIcons.minimize} size={12} />
            </TerminalButton>
          )}
          {onMaximize && (
            <TerminalButton
              variant="secondary"
              size="sm"
              onClick={onMaximize}
              className="w-6 h-6 p-0 flex items-center justify-center hover:animate-eldritch-pulse"
            >
              <EldritchIcon name={MythosIcons.maximize} size={12} />
            </TerminalButton>
          )}
          {onClose && (
            <TerminalButton
              variant="danger"
              size="sm"
              onClick={onClose}
              className="w-6 h-6 p-0 flex items-center justify-center hover:animate-eldritch-glow"
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
        <>
          {/* Corner resize handles */}
          <div
            className="absolute top-0 right-0 w-3 h-3 cursor-se-resize hover:bg-mythos-terminal-primary/30 z-10"
            onMouseDown={e => {
              handleMouseDown(e, 'se');
            }}
            title="Resize"
          />
          <div
            className="absolute bottom-0 left-0 w-3 h-3 cursor-sw-resize hover:bg-mythos-terminal-primary/30 z-10"
            onMouseDown={e => {
              handleMouseDown(e, 'sw');
            }}
            title="Resize"
          />
          <div
            className="absolute bottom-0 right-0 w-3 h-3 cursor-se-resize hover:bg-mythos-terminal-primary/30 z-10"
            onMouseDown={e => {
              handleMouseDown(e, 'se');
            }}
            title="Resize"
          />
          <div
            className="absolute top-0 left-0 w-3 h-3 cursor-nw-resize hover:bg-mythos-terminal-primary/30 z-10"
            onMouseDown={e => {
              handleMouseDown(e, 'nw');
            }}
            title="Resize"
          />
          {/* Edge resize handles */}
          <div
            className="absolute top-1/2 left-0 w-2 h-8 -translate-y-1/2 cursor-w-resize hover:bg-mythos-terminal-primary/30 z-10"
            onMouseDown={e => {
              handleMouseDown(e, 'w');
            }}
            title="Resize width"
          />
          <div
            className="absolute top-1/2 right-0 w-2 h-8 -translate-y-1/2 cursor-e-resize hover:bg-mythos-terminal-primary/30 z-10"
            onMouseDown={e => {
              handleMouseDown(e, 'e');
            }}
            title="Resize width"
          />
          <div
            className="absolute left-1/2 top-0 w-8 h-2 -translate-x-1/2 cursor-n-resize hover:bg-mythos-terminal-primary/30 z-10"
            onMouseDown={e => {
              handleMouseDown(e, 'n');
            }}
            title="Resize height"
          />
          <div
            className="absolute left-1/2 bottom-0 w-8 h-2 -translate-x-1/2 cursor-s-resize hover:bg-mythos-terminal-primary/30 z-10"
            onMouseDown={e => {
              handleMouseDown(e, 's');
            }}
            title="Resize height"
          />
        </>
      )}
    </div>
  );
};
