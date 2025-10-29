import React, { useCallback, useEffect, useRef, useState } from 'react';
import { EldritchIcon, MythosIcons } from './ui/EldritchIcon';
import { TerminalButton } from './ui/TerminalButton';

interface DraggablePanelProps {
  children: React.ReactNode;
  title: string;
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

export const DraggablePanel: React.FC<DraggablePanelProps> = ({
  children,
  title,
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
  const [position, setPosition] = useState(defaultPosition);
  const [size, setSize] = useState(defaultSize);
  const [isDragging, setIsDragging] = useState(false);
  const [isResizing, setIsResizing] = useState(false);
  const [isMinimized, setIsMinimized] = useState(false);
  // isMaximized state removed - maximize state managed by parent component
  const [dragOffset, setDragOffset] = useState({ x: 0, y: 0 });
  const [resizeDirection, setResizeDirection] = useState<string>('');
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
  useEffect(() => {
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
  ]);

  // Use CSS Grid positioning if className is provided, otherwise use absolute positioning
  const isGridPositioned = className && className.includes('panel-');
  const baseClasses = isGridPositioned
    ? 'font-mono bg-mythos-terminal-surface border border-gray-700 rounded shadow-lg overflow-hidden transition-eldritch duration-eldritch ease-eldritch'
    : 'font-mono bg-mythos-terminal-surface border border-gray-700 rounded shadow-lg absolute overflow-hidden transition-eldritch duration-eldritch ease-eldritch';

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
    if (e.target === headerRef.current || headerRef.current?.contains(e.target as Node)) {
      e.preventDefault();
      setIsDragging(true);
      const rect = panelRef.current?.getBoundingClientRect();
      if (rect) {
        setDragOffset({
          x: e.clientX - rect.left,
          y: e.clientY - rect.top,
        });
      }
    }
  };

  const handleMouseMove = useCallback(
    (e: MouseEvent) => {
      if (isDragging) {
        const newX = e.clientX - dragOffset.x;
        const newY = e.clientY - dragOffset.y;
        setPosition({ x: Math.max(0, newX), y: Math.max(0, newY) });
      }

      if (isResizing) {
        const rect = panelRef.current?.getBoundingClientRect();
        if (rect) {
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
          }

          setSize({ width: newWidth, height: newHeight });
          setPosition({ x: newX, y: newY });
        }
      }
    },
    [isDragging, isResizing, dragOffset, resizeDirection, position, size, minSize, maxSize]
  );

  const handleMouseUp = () => {
    setIsDragging(false);
    setIsResizing(false);
    setResizeDirection('');
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
        // CSS Grid positioning - no absolute positioning needed
        width: '100%',
        height: '100%',
        zIndex,
      }
    : {
        // Absolute positioning for draggable panels
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
          className="p-3 h-full overflow-auto"
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
          <div
            className="absolute top-0 right-0 w-2 h-2 cursor-se-resize hover:bg-mythos-terminal-primary/20"
            onMouseDown={e => handleMouseDown(e, 'se')}
          />
          <div
            className="absolute bottom-0 left-0 w-2 h-2 cursor-sw-resize hover:bg-mythos-terminal-primary/20"
            onMouseDown={e => handleMouseDown(e, 'sw')}
          />
          <div
            className="absolute bottom-0 right-0 w-2 h-2 cursor-se-resize hover:bg-mythos-terminal-primary/20"
            onMouseDown={e => handleMouseDown(e, 'se')}
          />
          <div
            className="absolute top-0 left-0 w-2 h-2 cursor-nw-resize hover:bg-mythos-terminal-primary/20"
            onMouseDown={e => handleMouseDown(e, 'nw')}
          />
          <div
            className="absolute top-1/2 left-0 w-1 h-4 -translate-y-1/2 cursor-w-resize hover:bg-mythos-terminal-primary/20"
            onMouseDown={e => handleMouseDown(e, 'w')}
          />
          <div
            className="absolute top-1/2 right-0 w-1 h-4 -translate-y-1/2 cursor-e-resize hover:bg-mythos-terminal-primary/20"
            onMouseDown={e => handleMouseDown(e, 'e')}
          />
          <div
            className="absolute left-1/2 top-0 w-4 h-1 -translate-x-1/2 cursor-n-resize hover:bg-mythos-terminal-primary/20"
            onMouseDown={e => handleMouseDown(e, 'n')}
          />
          <div
            className="absolute left-1/2 bottom-0 w-4 h-1 -translate-x-1/2 cursor-s-resize hover:bg-mythos-terminal-primary/20"
            onMouseDown={e => handleMouseDown(e, 's')}
          />
        </>
      )}
    </div>
  );
};
