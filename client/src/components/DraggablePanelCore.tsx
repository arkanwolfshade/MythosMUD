import React from 'react';
import { DraggablePanelView } from './DraggablePanelView';
import { useDraggablePanelInteractions } from './useDraggablePanelInteractions';
import { useDraggablePanelLayout } from './useDraggablePanelLayout';

export interface DraggablePanelProps {
  children: React.ReactNode;
  title: string;
  panelId?: string;
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
  autoSize?: boolean;
}

export const DraggablePanel: React.FC<DraggablePanelProps> = props => {
  const {
    children,
    title,
    onClose,
    onMinimize,
    onMaximize,
    className = '',
    variant = 'default',
    zIndex = 1000,
  } = props;

  const layout = useDraggablePanelLayout(props);
  const { handleMouseDown, handleResizeHandleKeyDown, handleHeaderMouseDown } = useDraggablePanelInteractions({
    isGridPositioned: layout.isGridPositioned,
    position: layout.position,
    size: layout.size,
    minSize: layout.minSize,
    maxSize: layout.maxSize,
    setPosition: layout.setPosition,
    setSize: layout.setSize,
    panelRef: layout.panelRef,
    headerRef: layout.headerRef,
  });

  return (
    <DraggablePanelView
      children={children}
      title={title}
      className={className}
      variant={variant}
      zIndex={zIndex}
      onClose={onClose}
      onMinimize={onMinimize}
      onMaximize={onMaximize}
      isGridPositioned={layout.isGridPositioned}
      position={layout.position}
      size={layout.size}
      isMinimized={layout.isMinimized}
      headerHeight={layout.headerHeight}
      panelRef={layout.panelRef}
      headerRef={layout.headerRef}
      contentRef={layout.contentRef}
      handleMinimize={layout.handleMinimize}
      handleMouseDown={handleMouseDown}
      handleResizeHandleKeyDown={handleResizeHandleKeyDown}
      handleHeaderMouseDown={handleHeaderMouseDown}
    />
  );
};
