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

function createResizeKeyHandlers(
  isGridPositioned: boolean,
  size: Size,
  position: Position,
  minSize: Size,
  maxSize: Size,
  setPosition: React.Dispatch<React.SetStateAction<Position>>,
  setSize: React.Dispatch<React.SetStateAction<Size>>
) {
  const applyResizeDelta = (direction: string, step: number, key: string) => {
    applyKeyboardResizeDelta({
      isGridPositioned,
      direction,
      step,
      key,
      size,
      position,
      minSize,
      maxSize,
      setPosition,
      setSize,
    });
  };

  const handleResizeHandleKeyDown = (direction: string, e: React.KeyboardEvent<HTMLButtonElement>) => {
    const supportedKeys = ['ArrowUp', 'ArrowDown', 'ArrowLeft', 'ArrowRight'];
    if (!supportedKeys.includes(e.key)) return;
    e.preventDefault();
    applyResizeDelta(direction, e.shiftKey ? 24 : 12, e.key);
  };

  return { handleResizeHandleKeyDown };
}

function useDraggablePanelInteractionCore(
  args: UseDraggablePanelInteractionsArgs
): UseDraggablePanelInteractionsResult {
  const { isGridPositioned, position, size, minSize, maxSize, setPosition, setSize, panelRef, headerRef } = args;
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

  const { handleResizeHandleKeyDown } = createResizeKeyHandlers(
    isGridPositioned,
    size,
    position,
    minSize,
    maxSize,
    setPosition,
    setSize
  );

  const handleHeaderMouseDown = (e: React.MouseEvent) => {
    beginHeaderDrag({
      event: e,
      headerRef,
      panelRef,
      dragStartPositionRef,
      hasDraggedRef,
      setDragOffset,
      setIsDragging,
    });
  };

  // Refs are read/written only inside these handlers (event path), not during render.
  const handleMouseMove = useCallback(
    (e: MouseEvent) => {
      handlePanelPointerMove({
        event: e,
        isDragging,
        isResizing,
        dragStartPosition: dragStartPositionRef.current,
        hasDraggedRef,
        dragOffset,
        size,
        position,
        minSize,
        maxSize,
        resizeDirection,
        panelRef,
        setPosition,
        setSize,
      });
    },
    [
      isDragging,
      isResizing,
      dragOffset,
      size,
      position,
      minSize,
      maxSize,
      resizeDirection,
      panelRef,
      setPosition,
      setSize,
    ]
  );

  const handleMouseUp = useCallback(() => {
    setIsDragging(false);
    setIsResizing(false);
    setResizeDirection('');
    dragStartPositionRef.current = null;
    hasDraggedRef.current = false;
  }, []);

  useEffect(
    () => attachDragResizeListeners(isDragging, isResizing, handleMouseMove, handleMouseUp),
    [isDragging, isResizing, handleMouseMove, handleMouseUp]
  );

  return { isDragging, isResizing, handleMouseDown, handleResizeHandleKeyDown, handleHeaderMouseDown };
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

interface ResizeUpdateContext {
  event: MouseEvent;
  rect: DOMRect;
  size: Size;
  position: Position;
  minSize: Size;
  maxSize: Size;
  resizeDirection: string;
  setPosition: React.Dispatch<React.SetStateAction<Position>>;
  setSize: React.Dispatch<React.SetStateAction<Size>>;
}

function applyHorizontalResize(ctx: ResizeUpdateContext): { newWidth: number; newX: number } {
  let newWidth = ctx.size.width;
  let newX = ctx.position.x;
  if (ctx.resizeDirection.includes('e')) {
    newWidth = Math.max(ctx.minSize.width, Math.min(ctx.maxSize.width, ctx.event.clientX - ctx.rect.left));
  }
  if (ctx.resizeDirection.includes('w')) {
    const deltaX = ctx.rect.right - ctx.event.clientX;
    newWidth = Math.max(ctx.minSize.width, Math.min(ctx.maxSize.width, ctx.size.width + deltaX));
    newX = ctx.position.x + (ctx.size.width - newWidth);
  }
  return { newWidth, newX };
}

function applyVerticalResize(ctx: ResizeUpdateContext): { newHeight: number; newY: number } {
  const headerHeight = 60;
  let newHeight = ctx.size.height;
  let newY = ctx.position.y;
  if (ctx.resizeDirection.includes('s')) {
    newHeight = Math.max(ctx.minSize.height, Math.min(ctx.maxSize.height, ctx.event.clientY - ctx.rect.top));
  }
  if (ctx.resizeDirection.includes('n')) {
    const deltaY = ctx.rect.bottom - ctx.event.clientY;
    newHeight = Math.max(ctx.minSize.height, Math.min(ctx.maxSize.height, ctx.size.height + deltaY));
    newY = ctx.position.y + (ctx.size.height - newHeight);
    if (newY < headerHeight) {
      const adjustment = headerHeight - newY;
      newY = headerHeight;
      newHeight = Math.max(ctx.minSize.height, newHeight - adjustment);
    }
  }
  return { newHeight, newY };
}

const updateResizePosition = (ctx: ResizeUpdateContext): void => {
  const { newWidth, newX } = applyHorizontalResize(ctx);
  const { newHeight, newY } = applyVerticalResize(ctx);
  ctx.setSize({ width: newWidth, height: newHeight });
  ctx.setPosition({ x: newX, y: newY });
};

function attachDragResizeListeners(
  isDragging: boolean,
  isResizing: boolean,
  handleMouseMove: (e: MouseEvent) => void,
  handleMouseUp: () => void
): (() => void) | undefined {
  if (!isDragging && !isResizing) return undefined;
  document.addEventListener('mousemove', handleMouseMove);
  document.addEventListener('mouseup', handleMouseUp);
  return () => {
    document.removeEventListener('mousemove', handleMouseMove);
    document.removeEventListener('mouseup', handleMouseUp);
  };
}

function getArrowDelta(key: string, positiveKey: string, negativeKey: string, step: number): number {
  if (key === positiveKey) return step;
  if (key === negativeKey) return -step;
  return 0;
}

type KeyboardResizeInput = {
  direction: string;
  step: number;
  key: string;
  size: Size;
  position: Position;
};

function computeKeyboardResizeDimensions(input: KeyboardResizeInput): {
  width: number;
  height: number;
  x: number;
  y: number;
} {
  let newWidth = input.size.width;
  let newHeight = input.size.height;
  let newX = input.position.x;
  let newY = input.position.y;

  if (input.direction.includes('e')) {
    newWidth += getArrowDelta(input.key, 'ArrowRight', 'ArrowLeft', input.step);
  }
  if (input.direction.includes('s')) {
    newHeight += getArrowDelta(input.key, 'ArrowDown', 'ArrowUp', input.step);
  }
  if (input.direction.includes('w')) {
    const widthDelta = getArrowDelta(input.key, 'ArrowLeft', 'ArrowRight', input.step);
    newWidth += widthDelta;
    newX -= widthDelta;
  }
  if (input.direction.includes('n')) {
    const heightDelta = getArrowDelta(input.key, 'ArrowUp', 'ArrowDown', input.step);
    newHeight += heightDelta;
    newY -= heightDelta;
  }

  return { width: newWidth, height: newHeight, x: newX, y: newY };
}

function clampPanelSizeAndPosition(
  dimensions: { width: number; height: number; x: number; y: number },
  minSize: Size,
  maxSize: Size
): { width: number; height: number; x: number; y: number } {
  const topBoundary = 60;
  const clampedWidth = Math.max(minSize.width, Math.min(maxSize.width, dimensions.width));
  const clampedHeight = Math.max(minSize.height, Math.min(maxSize.height, dimensions.height));
  const maxX = window.innerWidth - clampedWidth;
  const maxY = window.innerHeight - clampedHeight;
  return {
    width: clampedWidth,
    height: clampedHeight,
    x: Math.max(-100, Math.min(dimensions.x, maxX)),
    y: Math.max(topBoundary, Math.min(dimensions.y, maxY)),
  };
}

interface KeyboardResizeDeltaContext extends KeyboardResizeInput {
  isGridPositioned: boolean;
  minSize: Size;
  maxSize: Size;
  setPosition: React.Dispatch<React.SetStateAction<Position>>;
  setSize: React.Dispatch<React.SetStateAction<Size>>;
}

function applyKeyboardResizeDelta(ctx: KeyboardResizeDeltaContext): void {
  if (ctx.isGridPositioned) {
    return;
  }
  const dimensions = computeKeyboardResizeDimensions(ctx);
  const clamped = clampPanelSizeAndPosition(dimensions, ctx.minSize, ctx.maxSize);
  ctx.setSize({ width: clamped.width, height: clamped.height });
  ctx.setPosition({ x: clamped.x, y: clamped.y });
}

interface DragMoveContext {
  event: MouseEvent;
  isDragging: boolean;
  isResizing: boolean;
  dragStartPosition: Position | null;
  hasDraggedRef: React.MutableRefObject<boolean>;
  dragOffset: Position;
  size: Size;
  position: Position;
  minSize: Size;
  maxSize: Size;
  resizeDirection: string;
  panelRef: React.RefObject<HTMLDivElement | null>;
  setPosition: React.Dispatch<React.SetStateAction<Position>>;
  setSize: React.Dispatch<React.SetStateAction<Size>>;
}

const DRAG_THRESHOLD_PX = 3;

function exceedsDragThreshold(event: MouseEvent, start: Position | null): boolean {
  if (!start) {
    return false;
  }
  const deltaX = Math.abs(event.clientX - start.x);
  const deltaY = Math.abs(event.clientY - start.y);
  return deltaX > DRAG_THRESHOLD_PX || deltaY > DRAG_THRESHOLD_PX;
}

function applyDragMove(ctx: DragMoveContext): void {
  if (!ctx.isDragging) {
    return;
  }
  if (exceedsDragThreshold(ctx.event, ctx.dragStartPosition)) {
    ctx.hasDraggedRef.current = true;
  }
  if (!ctx.hasDraggedRef.current) {
    return;
  }
  updateDragPosition({
    event: ctx.event,
    dragOffset: ctx.dragOffset,
    size: ctx.size,
    setPosition: ctx.setPosition,
  });
}

function applyResizeMove(ctx: DragMoveContext): void {
  if (!ctx.isResizing) {
    return;
  }
  const rect = ctx.panelRef.current?.getBoundingClientRect();
  if (!rect) {
    return;
  }
  updateResizePosition({
    event: ctx.event,
    rect,
    size: ctx.size,
    position: ctx.position,
    minSize: ctx.minSize,
    maxSize: ctx.maxSize,
    resizeDirection: ctx.resizeDirection,
    setPosition: ctx.setPosition,
    setSize: ctx.setSize,
  });
}

function handlePanelPointerMove(ctx: DragMoveContext): void {
  applyDragMove(ctx);
  applyResizeMove(ctx);
}

interface HeaderDragContext {
  event: React.MouseEvent;
  headerRef: React.RefObject<HTMLDivElement | null>;
  panelRef: React.RefObject<HTMLDivElement | null>;
  dragStartPositionRef: React.MutableRefObject<Position | null>;
  hasDraggedRef: React.MutableRefObject<boolean>;
  setDragOffset: React.Dispatch<React.SetStateAction<Position>>;
  setIsDragging: React.Dispatch<React.SetStateAction<boolean>>;
}

function canBeginHeaderDrag(event: React.MouseEvent, header: HTMLDivElement | null | undefined): boolean {
  const target = event.target as HTMLElement;
  return !isPanelDragBlockedTarget(target) && isMouseEventOnHeader(event, header ?? null);
}

function beginHeaderDrag(ctx: HeaderDragContext): void {
  if (!canBeginHeaderDrag(ctx.event, ctx.headerRef.current)) {
    return;
  }

  ctx.event.preventDefault();
  ctx.event.stopPropagation();

  const rect = ctx.panelRef.current?.getBoundingClientRect();
  if (!rect) {
    return;
  }

  ctx.dragStartPositionRef.current = { x: ctx.event.clientX, y: ctx.event.clientY };
  ctx.hasDraggedRef.current = false;
  ctx.setDragOffset({
    x: ctx.event.clientX - rect.left,
    y: ctx.event.clientY - rect.top,
  });
  ctx.setIsDragging(true);
}

export const useDraggablePanelInteractions = (
  args: UseDraggablePanelInteractionsArgs
): UseDraggablePanelInteractionsResult => useDraggablePanelInteractionCore(args);
