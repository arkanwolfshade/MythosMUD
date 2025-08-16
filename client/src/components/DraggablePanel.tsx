import { Close, DragIndicator, Minimize, OpenInFull } from '@mui/icons-material';
import { Box, IconButton, Paper, Tooltip, Typography } from '@mui/material';
import { styled } from '@mui/material/styles';
import React, { useCallback, useEffect, useRef, useState } from 'react';

// Styled components for the draggable panel
const DraggablePaper = styled(Paper)(({ theme }) => ({
  position: 'absolute',
  cursor: 'move',
  userSelect: 'none',
  zIndex: 1000,
  minWidth: 200,
  minHeight: 150,
  transition: 'box-shadow 0.2s ease-in-out',
  '&:hover': {
    boxShadow: theme.shadows[8],
  },
  '&.dragging': {
    boxShadow: theme.shadows[12],
    opacity: 0.9,
  },
  '&.snapping': {
    transition: 'transform 0.1s ease-out',
  },
}));

const PanelHeader = styled(Box)(({ theme }) => ({
  display: 'flex',
  alignItems: 'center',
  justifyContent: 'space-between',
  padding: theme.spacing(1, 2),
  backgroundColor: theme.palette.primary.main,
  color: theme.palette.primary.contrastText,
  cursor: 'move',
  borderTopLeftRadius: theme.shape.borderRadius,
  borderTopRightRadius: theme.shape.borderRadius,
  '&:hover': {
    backgroundColor: theme.palette.primary.dark,
  },
}));

const PanelContent = styled(Box)(({ theme }) => ({
  padding: theme.spacing(2),
  height: 'calc(100% - 48px)', // Subtract header height
  overflow: 'auto',
}));

const HeaderControls = styled(Box)({
  display: 'flex',
  alignItems: 'center',
  gap: '4px',
});

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
  className,
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

  // Resize handles
  const ResizeHandle = styled(Box)<{ handlePosition: string }>(({ handlePosition }) => ({
    position: 'absolute',
    backgroundColor: 'transparent',
    '&:hover': {
      backgroundColor: 'rgba(0, 0, 0, 0.1)',
    },
    ...(handlePosition.includes('n') && { top: 0, height: 4, cursor: 'n-resize' }),
    ...(handlePosition.includes('s') && { bottom: 0, height: 4, cursor: 's-resize' }),
    ...(handlePosition.includes('e') && { right: 0, width: 4, cursor: 'e-resize' }),
    ...(handlePosition.includes('w') && { left: 0, width: 4, cursor: 'w-resize' }),
    ...(handlePosition === 'nw' && { cursor: 'nw-resize' }),
    ...(handlePosition === 'ne' && { cursor: 'ne-resize' }),
    ...(handlePosition === 'sw' && { cursor: 'sw-resize' }),
    ...(handlePosition === 'se' && { cursor: 'se-resize' }),
  }));

  if (isMinimized) {
    return (
      <DraggablePaper
        ref={panelRef}
        style={{
          left: position.x,
          top: position.y,
          width: 200,
          height: 48,
        }}
        className={`${className || ''} ${isDragging ? 'dragging' : ''}`}
        elevation={isDragging ? 12 : 4}
      >
        <PanelHeader onMouseDown={handleMouseDown}>
          <Typography variant="subtitle2" noWrap>
            {title}
          </Typography>
          <HeaderControls>
            {onMaximize && (
              <Tooltip title="Restore">
                <IconButton size="small" onClick={onMaximize}>
                  <OpenInFull fontSize="small" />
                </IconButton>
              </Tooltip>
            )}
            {onClose && (
              <Tooltip title="Close">
                <IconButton size="small" onClick={onClose}>
                  <Close fontSize="small" />
                </IconButton>
              </Tooltip>
            )}
          </HeaderControls>
        </PanelHeader>
      </DraggablePaper>
    );
  }

  return (
    <DraggablePaper
      ref={panelRef}
      style={{
        left: position.x,
        top: position.y,
        width: size.width,
        height: size.height,
      }}
      className={`${className || ''} ${isDragging ? 'dragging' : ''} ${isResizing ? 'snapping' : ''}`}
      elevation={isDragging || isResizing ? 12 : 4}
    >
      <PanelHeader onMouseDown={handleMouseDown}>
        <Box display="flex" alignItems="center" gap={1}>
          <DragIndicator fontSize="small" />
          <Typography variant="subtitle2" noWrap>
            {title}
          </Typography>
        </Box>
        <HeaderControls>
          {onMinimize && (
            <Tooltip title="Minimize">
              <IconButton size="small" onClick={onMinimize}>
                <Minimize fontSize="small" />
              </IconButton>
            </Tooltip>
          )}
          {onMaximize && (
            <Tooltip title={isMaximized ? 'Restore' : 'Maximize'}>
              <IconButton size="small" onClick={onMaximize}>
                <OpenInFull fontSize="small" />
              </IconButton>
            </Tooltip>
          )}
          {onClose && (
            <Tooltip title="Close">
              <IconButton size="small" onClick={onClose}>
                <Close fontSize="small" />
              </IconButton>
            </Tooltip>
          )}
        </HeaderControls>
      </PanelHeader>

      <PanelContent>{children}</PanelContent>

      {/* Resize handles */}
      <ResizeHandle handlePosition="n" onMouseDown={e => handleResizeMouseDown(e, 'n')} />
      <ResizeHandle handlePosition="s" onMouseDown={e => handleResizeMouseDown(e, 's')} />
      <ResizeHandle handlePosition="e" onMouseDown={e => handleResizeMouseDown(e, 'e')} />
      <ResizeHandle handlePosition="w" onMouseDown={e => handleResizeMouseDown(e, 'w')} />
      <ResizeHandle handlePosition="nw" onMouseDown={e => handleResizeMouseDown(e, 'nw')} />
      <ResizeHandle handlePosition="ne" onMouseDown={e => handleResizeMouseDown(e, 'ne')} />
      <ResizeHandle handlePosition="sw" onMouseDown={e => handleResizeMouseDown(e, 'sw')} />
      <ResizeHandle handlePosition="se" onMouseDown={e => handleResizeMouseDown(e, 'se')} />
    </DraggablePaper>
  );
};
