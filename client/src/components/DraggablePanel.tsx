import React, { useCallback, useEffect, useRef, useState } from 'react';
import { EldritchIcon, MythosIcons } from './ui/EldritchIcon';
import { TerminalButton } from './ui/TerminalButton';

interface PanelPosition {
  x: number;
  y: number;
}

interface PanelSize {
  width: number;
  height: number;
}

interface DraggablePanelProps {
  id: string;
  title: string;
  children: React.ReactNode;
  initialPosition?: PanelPosition;
  initialSize?: PanelSize;
  minSize?: PanelSize;
  maxSize?: PanelSize;
  onPositionChange?: (position: PanelPosition) => void;
  onSizeChange?: (size: PanelSize) => void;
  onClose?: () => void;
  onMinimize?: () => void;
  onMaximize?: () => void;
  isMinimized?: boolean;
  isMaximized?: boolean;
  snapToGrid?: boolean;
  gridSize?: number;
  className?: string;
  style?: React.CSSProperties;
  variant?: 'default' | 'elevated' | 'eldritch';
}

export const DraggablePanel: React.FC<DraggablePanelProps> = ({
  title,
  children,
  initialPosition = { x: 50, y: 50 },
  initialSize = { width: 300, height: 400 },
  minSize = { width: 200, height: 150 },
  maxSize = { width: 800, height: 600 },
  onPositionChange,
  onSizeChange,
  onClose,
  onMinimize,
  onMaximize,
  isMinimized = false,
  isMaximized = false,
  snapToGrid = true,
  gridSize = 20,
  className = '',
  variant = 'default',
}) => {
  const [position, setPosition] = useState<PanelPosition>(initialPosition);
  const [size, setSize] = useState<PanelSize>(initialSize);
  const [isDragging, setIsDragging] = useState(false);
  const [isResizing, setIsResizing] = useState(false);
  const [dragOffset, setDragOffset] = useState<PanelPosition>({ x: 0, y: 0 });
  const [resizeHandle, setResizeHandle] = useState<string | null>(null);
  const [resizeStart, setResizeStart] = useState<{ size: PanelSize; mouse: PanelPosition } | null>(null);

  const panelRef = useRef<HTMLDivElement>(null);

  // Snap position to grid
  const snapToGridPosition = useCallback(
    (pos: PanelPosition): PanelPosition => {
      if (!snapToGrid) return pos;
      return {
        x: Math.round(pos.x / gridSize) * gridSize,
        y: Math.round(pos.y / gridSize) * gridSize,
      };
    },
    [snapToGrid, gridSize]
  );

  // Snap size to grid
  const snapToGridSize = useCallback(
    (s: PanelSize): PanelSize => {
      if (!snapToGrid) return s;
      return {
        width: Math.round(s.width / gridSize) * gridSize,
        height: Math.round(s.height / gridSize) * gridSize,
      };
    },
    [snapToGrid, gridSize]
  );

  // Handle mouse down for dragging
  const handleMouseDown = useCallback((e: React.MouseEvent) => {
    if (e.target !== e.currentTarget) return; // Only drag from header

    e.preventDefault();
    setIsDragging(true);

    const rect = panelRef.current?.getBoundingClientRect();
    if (rect) {
      setDragOffset({
        x: e.clientX - rect.left,
        y: e.clientY - rect.top,
      });
    }
  }, []);

  // Handle mouse down for resizing
  const handleResizeMouseDown = useCallback(
    (e: React.MouseEvent, handle: string) => {
      e.preventDefault();
      e.stopPropagation();

      setIsResizing(true);
      setResizeHandle(handle);

      const rect = panelRef.current?.getBoundingClientRect();
      if (rect) {
        setResizeStart({
          size: { ...size },
          mouse: { x: e.clientX, y: e.clientY },
        });
      }
    },
    [size]
  );

  // Handle mouse move
  const handleMouseMove = useCallback(
    (e: MouseEvent) => {
      if (isDragging) {
        const newPosition = snapToGridPosition({
          x: e.clientX - dragOffset.x,
          y: e.clientY - dragOffset.y,
        });

        setPosition(newPosition);
        onPositionChange?.(newPosition);
      }

      if (isResizing && resizeStart) {
        const deltaX = e.clientX - resizeStart.mouse.x;
        const deltaY = e.clientY - resizeStart.mouse.y;

        const newSize = { ...resizeStart.size };

        switch (resizeHandle) {
          case 'nw':
            newSize.width = Math.max(minSize.width, resizeStart.size.width - deltaX);
            newSize.height = Math.max(minSize.height, resizeStart.size.height - deltaY);
            break;
          case 'ne':
            newSize.width = Math.max(minSize.width, resizeStart.size.width + deltaX);
            newSize.height = Math.max(minSize.height, resizeStart.size.height - deltaY);
            break;
          case 'sw':
            newSize.width = Math.max(minSize.width, resizeStart.size.width - deltaX);
            newSize.height = Math.max(minSize.height, resizeStart.size.height + deltaY);
            break;
          case 'se':
            newSize.width = Math.max(minSize.width, resizeStart.size.width + deltaX);
            newSize.height = Math.max(minSize.height, resizeStart.size.height + deltaY);
            break;
          case 'n':
            newSize.height = Math.max(minSize.height, resizeStart.size.height - deltaY);
            break;
          case 's':
            newSize.height = Math.max(minSize.height, resizeStart.size.height + deltaY);
            break;
          case 'e':
            newSize.width = Math.max(minSize.width, resizeStart.size.width + deltaX);
            break;
          case 'w':
            newSize.width = Math.max(minSize.width, resizeStart.size.width - deltaX);
            break;
        }

        // Apply max size constraints
        newSize.width = Math.min(maxSize.width, newSize.width);
        newSize.height = Math.min(maxSize.height, newSize.height);

        const snappedSize = snapToGridSize(newSize);
        setSize(snappedSize);
        onSizeChange?.(snappedSize);
      }
    },
    [
      isDragging,
      isResizing,
      dragOffset,
      resizeStart,
      resizeHandle,
      minSize,
      maxSize,
      snapToGridPosition,
      snapToGridSize,
      onPositionChange,
      onSizeChange,
    ]
  );

  // Handle mouse up
  const handleMouseUp = useCallback(() => {
    setIsDragging(false);
    setIsResizing(false);
    setResizeHandle(null);
    setResizeStart(null);
  }, []);

  // Add/remove event listeners
  useEffect(() => {
    if (isDragging || isResizing) {
      document.addEventListener('mousemove', handleMouseMove);
      document.addEventListener('mouseup', handleMouseUp);

      return () => {
        document.removeEventListener('mousemove', handleMouseMove);
        document.removeEventListener('mouseup', handleMouseUp);
      };
    }
  }, [isDragging, isResizing, handleMouseMove, handleMouseUp]);

  // Base panel classes
  const baseClasses = 'font-mono border rounded relative overflow-hidden transition-all duration-200';

  const variantClasses = {
    default: 'bg-mythos-terminal-surface border-gray-700 text-mythos-terminal-text shadow-lg',
    elevated:
      'bg-mythos-terminal-surface border-mythos-terminal-primary text-mythos-terminal-text shadow-xl shadow-green-900/20',
    eldritch:
      'bg-mythos-terminal-surface border-mythos-terminal-primary text-mythos-terminal-text shadow-xl shadow-green-900/30',
  };

  const stateClasses = isDragging || isResizing ? 'shadow-2xl opacity-90' : '';

  const panelClasses = `${baseClasses} ${variantClasses[variant]} ${stateClasses} ${className}`;

  // Resize handle component
  const ResizeHandle: React.FC<{ handlePosition: string }> = ({ handlePosition }) => {
    const handleClasses = 'absolute bg-transparent hover:bg-mythos-terminal-primary/20 transition-colors duration-200';

    const positionClasses = {
      n: 'top-0 left-0 right-0 h-1 cursor-n-resize',
      s: 'bottom-0 left-0 right-0 h-1 cursor-s-resize',
      e: 'top-0 right-0 bottom-0 w-1 cursor-e-resize',
      w: 'top-0 left-0 bottom-0 w-1 cursor-w-resize',
      nw: 'top-0 left-0 w-2 h-2 cursor-nw-resize',
      ne: 'top-0 right-0 w-2 h-2 cursor-ne-resize',
      sw: 'bottom-0 left-0 w-2 h-2 cursor-sw-resize',
      se: 'bottom-0 right-0 w-2 h-2 cursor-se-resize',
    };

    return (
      <div
        className={`${handleClasses} ${positionClasses[handlePosition as keyof typeof positionClasses]}`}
        onMouseDown={e => handleResizeMouseDown(e, handlePosition)}
      />
    );
  };

  if (isMinimized) {
    return (
      <div
        ref={panelRef}
        style={{
          position: 'absolute',
          left: position.x,
          top: position.y,
          width: 200,
          height: 48,
          zIndex: 1000,
        }}
        className={panelClasses}
      >
        <div
          className="flex items-center justify-between px-3 py-2 bg-mythos-terminal-primary text-black cursor-move border-b border-gray-700"
          onMouseDown={handleMouseDown}
        >
          <span className="text-sm font-bold truncate">{title}</span>
          <div className="flex items-center gap-1">
            {onMaximize && (
              <TerminalButton variant="secondary" size="sm" onClick={onMaximize} className="p-1 h-6 w-6">
                <EldritchIcon name={MythosIcons.maximize} size={12} variant="primary" />
              </TerminalButton>
            )}
            {onClose && (
              <TerminalButton variant="danger" size="sm" onClick={onClose} className="p-1 h-6 w-6">
                <EldritchIcon name={MythosIcons.close} size={12} variant="error" />
              </TerminalButton>
            )}
          </div>
        </div>
      </div>
    );
  }

  return (
    <div
      ref={panelRef}
      style={{
        position: 'absolute',
        left: position.x,
        top: position.y,
        width: size.width,
        height: size.height,
        zIndex: 1000,
      }}
      className={panelClasses}
    >
      {/* Header */}
      <div
        className="flex items-center justify-between px-3 py-2 bg-mythos-terminal-primary text-black cursor-move border-b border-gray-700"
        onMouseDown={handleMouseDown}
      >
        <div className="flex items-center gap-2">
          <EldritchIcon name={MythosIcons.move} size={16} variant="primary" />
          <span className="text-sm font-bold truncate">{title}</span>
        </div>
        <div className="flex items-center gap-1">
          {onMinimize && (
            <TerminalButton variant="secondary" size="sm" onClick={onMinimize} className="p-1 h-6 w-6">
              <EldritchIcon name={MythosIcons.minimize} size={12} variant="primary" />
            </TerminalButton>
          )}
          {onMaximize && (
            <TerminalButton variant="secondary" size="sm" onClick={onMaximize} className="p-1 h-6 w-6">
              <EldritchIcon
                name={isMaximized ? MythosIcons.maximize : MythosIcons.maximize}
                size={12}
                variant="primary"
              />
            </TerminalButton>
          )}
          {onClose && (
            <TerminalButton variant="danger" size="sm" onClick={onClose} className="p-1 h-6 w-6">
              <EldritchIcon name={MythosIcons.close} size={12} variant="error" />
            </TerminalButton>
          )}
        </div>
      </div>

      {/* Content */}
      <div className="p-3 h-[calc(100%-48px)] overflow-auto">{children}</div>

      {/* Resize handles */}
      <ResizeHandle handlePosition="n" />
      <ResizeHandle handlePosition="s" />
      <ResizeHandle handlePosition="e" />
      <ResizeHandle handlePosition="w" />
      <ResizeHandle handlePosition="nw" />
      <ResizeHandle handlePosition="ne" />
      <ResizeHandle handlePosition="sw" />
      <ResizeHandle handlePosition="se" />
    </div>
  );
};
