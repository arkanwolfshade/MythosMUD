import type React from 'react';
import { useCallback, useEffect, useRef, useState } from 'react';
import { isMouseEventOnHeader, isPanelDragBlockedTarget } from './draggablePanelUtils';

interface Size {
  width: number;
  height: number;
}

interface Position {
  x: number;
  y: number;
}

interface UseDraggablePanelInteractionsArgs {
  isGridPositioned: boolean;
  position: Position;
  size: Size;
  minSize: Size;
  maxSize: Size;
  setPosition: React.Dispatch<React.SetStateAction<Position>>;
  setSize: React.Dispatch<React.SetStateAction<Size>>;
  panelRef: React.RefObject<HTMLDivElement | null>;
  headerRef: React.RefObject<HTMLDivElement | null>;
}

interface UseDraggablePanelInteractionsResult {
  isDragging: boolean;
  isResizing: boolean;
  handleMouseDown: (e: React.MouseEvent, direction: string) => void;
  handleResizeHandleKeyDown: (direction: string, e: React.KeyboardEvent<HTMLButtonElement>) => void;
  handleHeaderMouseDown: (e: React.MouseEvent) => void;
}

const updateDragPosition = ({
  event,
  dragOffset,
  size,
  setPosition,
}: {
  event: MouseEvent;
  dragOffset: { x: number; y: number };
  size: Size;
  setPosition: React.Dispatch<React.SetStateAction<Position>>;
}) => {
  const newX = event.clientX - dragOffset.x;
  const newY = event.clientY - dragOffset.y;
  const viewportWidth = window.innerWidth;
  const viewportHeight = window.innerHeight;
  const headerHeight = 60;
  let constrainedX = Math.round(newX);
  let constrainedY = Math.round(newY);
  const maxX = viewportWidth - size.width;
  const maxY = viewportHeight - size.height;
  const minX = -100;
  const minY = headerHeight - 10;

  if (event.clientX <= 20 && constrainedX >= -20 && constrainedX <= 20) {
    constrainedX = 0;
  }
  if (event.clientY <= headerHeight + 20 && constrainedY >= headerHeight - 20 && constrainedY <= headerHeight + 20) {
    constrainedY = headerHeight;
  }

  setPosition({
    x: Math.max(minX, Math.min(constrainedX, maxX)),
    y: Math.max(minY, Math.min(constrainedY, maxY)),
  });
};

const updateResizePosition = ({
  event,
  rect,
  size,
  position,
  minSize,
  maxSize,
  resizeDirection,
  setPosition,
  setSize,
}: {
  event: MouseEvent;
  rect: DOMRect;
  size: Size;
  position: Position;
  minSize: Size;
  maxSize: Size;
  resizeDirection: string;
  setPosition: React.Dispatch<React.SetStateAction<Position>>;
  setSize: React.Dispatch<React.SetStateAction<Size>>;
}) => {
  const headerHeight = 60;
  let newWidth = size.width;
  let newHeight = size.height;
  let newX = position.x;
  let newY = position.y;

  if (resizeDirection.includes('e')) {
    newWidth = Math.max(minSize.width, Math.min(maxSize.width, event.clientX - rect.left));
  }
  if (resizeDirection.includes('w')) {
    const deltaX = rect.right - event.clientX;
    newWidth = Math.max(minSize.width, Math.min(maxSize.width, size.width + deltaX));
    newX = position.x + (size.width - newWidth);
  }
  if (resizeDirection.includes('s')) {
    newHeight = Math.max(minSize.height, Math.min(maxSize.height, event.clientY - rect.top));
  }
  if (resizeDirection.includes('n')) {
    const deltaY = rect.bottom - event.clientY;
    newHeight = Math.max(minSize.height, Math.min(maxSize.height, size.height + deltaY));
    newY = position.y + (size.height - newHeight);
    if (newY < headerHeight) {
      const adjustment = headerHeight - newY;
      newY = headerHeight;
      newHeight = Math.max(minSize.height, newHeight - adjustment);
    }
  }

  setSize({ width: newWidth, height: newHeight });
  setPosition({ x: newX, y: newY });
};

export const useDraggablePanelInteractions = ({
  isGridPositioned,
  position,
  size,
  minSize,
  maxSize,
  setPosition,
  setSize,
  panelRef,
  headerRef,
}: UseDraggablePanelInteractionsArgs): UseDraggablePanelInteractionsResult => {
  const [isDragging, setIsDragging] = useState(false);
  const [isResizing, setIsResizing] = useState(false);
  const [dragOffset, setDragOffset] = useState({ x: 0, y: 0 });
  const [resizeDirection, setResizeDirection] = useState<string>('');
  const dragStartPositionRef = useRef<{ x: number; y: number } | null>(null);
  const hasDraggedRef = useRef(false);

  const handleMouseDown = (e: React.MouseEvent, direction: string) => {
    e.preventDefault();
    setIsResizing(true);
    setResizeDirection(direction);
  };

  const getArrowDelta = useCallback((key: string, positiveKey: string, negativeKey: string, step: number): number => {
    if (key === positiveKey) return step;
    if (key === negativeKey) return -step;
    return 0;
  }, []);

  const applyResizeDelta = useCallback(
    (direction: string, step: number, key: string) => {
      if (isGridPositioned) {
        return;
      }

      let newWidth = size.width;
      let newHeight = size.height;
      let newX = position.x;
      let newY = position.y;

      if (direction.includes('e')) {
        newWidth += getArrowDelta(key, 'ArrowRight', 'ArrowLeft', step);
      }
      if (direction.includes('s')) {
        newHeight += getArrowDelta(key, 'ArrowDown', 'ArrowUp', step);
      }
      if (direction.includes('w')) {
        const widthDelta = getArrowDelta(key, 'ArrowLeft', 'ArrowRight', step);
        newWidth += widthDelta;
        newX -= widthDelta;
      }
      if (direction.includes('n')) {
        const heightDelta = getArrowDelta(key, 'ArrowUp', 'ArrowDown', step);
        newHeight += heightDelta;
        newY -= heightDelta;
      }

      const viewportWidth = window.innerWidth;
      const viewportHeight = window.innerHeight;
      const topBoundary = 60;

      const clampedWidth = Math.max(minSize.width, Math.min(maxSize.width, newWidth));
      const clampedHeight = Math.max(minSize.height, Math.min(maxSize.height, newHeight));
      const maxX = viewportWidth - clampedWidth;
      const maxY = viewportHeight - clampedHeight;
      const clampedX = Math.max(-100, Math.min(newX, maxX));
      const clampedY = Math.max(topBoundary, Math.min(newY, maxY));

      setSize({ width: clampedWidth, height: clampedHeight });
      setPosition({ x: clampedX, y: clampedY });
    },
    [
      isGridPositioned,
      maxSize.height,
      maxSize.width,
      minSize.height,
      minSize.width,
      position.x,
      position.y,
      size.height,
      size.width,
      getArrowDelta,
      setPosition,
      setSize,
    ]
  );

  const handleResizeHandleKeyDown = useCallback(
    (direction: string, e: React.KeyboardEvent<HTMLButtonElement>) => {
      const supportedKeys = ['ArrowUp', 'ArrowDown', 'ArrowLeft', 'ArrowRight'];
      if (!supportedKeys.includes(e.key)) {
        return;
      }
      e.preventDefault();
      const step = e.shiftKey ? 24 : 12;
      applyResizeDelta(direction, step, e.key);
    },
    [applyResizeDelta]
  );

  const handleHeaderMouseDown = (e: React.MouseEvent) => {
    const target = e.target as HTMLElement;
    if (isPanelDragBlockedTarget(target)) {
      return;
    }

    if (!isMouseEventOnHeader(e, headerRef.current)) {
      return;
    }

    e.preventDefault();
    e.stopPropagation();

    const rect = panelRef.current?.getBoundingClientRect();
    if (!rect) {
      return;
    }

    dragStartPositionRef.current = { x: e.clientX, y: e.clientY };
    hasDraggedRef.current = false;
    setDragOffset({
      x: e.clientX - rect.left,
      y: e.clientY - rect.top,
    });
    setIsDragging(true);
  };

  const handleMouseMove = useCallback(
    (e: MouseEvent) => {
      if (isDragging) {
        if (dragStartPositionRef.current) {
          const deltaX = Math.abs(e.clientX - dragStartPositionRef.current.x);
          const deltaY = Math.abs(e.clientY - dragStartPositionRef.current.y);
          const dragThreshold = 3;
          if (deltaX > dragThreshold || deltaY > dragThreshold) {
            hasDraggedRef.current = true;
          }
        }

        if (hasDraggedRef.current) {
          updateDragPosition({ event: e, dragOffset, size, setPosition });
        }
      }

      if (isResizing) {
        const rect = panelRef.current?.getBoundingClientRect();
        if (rect) {
          updateResizePosition({
            event: e,
            rect,
            size,
            position,
            minSize,
            maxSize,
            resizeDirection,
            setPosition,
            setSize,
          });
        }
      }
    },
    [
      dragOffset,
      isDragging,
      isResizing,
      maxSize,
      minSize,
      panelRef,
      position,
      resizeDirection,
      setPosition,
      setSize,
      size,
    ]
  );

  const handleMouseUp = useCallback(() => {
    setIsDragging(false);
    setIsResizing(false);
    setResizeDirection('');
    dragStartPositionRef.current = null;
    hasDraggedRef.current = false;
  }, []);

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

  return { isDragging, isResizing, handleMouseDown, handleResizeHandleKeyDown, handleHeaderMouseDown };
};
