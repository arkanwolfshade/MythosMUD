import { useCallback, useEffect, useMemo, useState } from 'react';
import type { PanelPosition } from '../types';
import type { PanelContainerProps } from './PanelContainerShared';
import type { PanelRndViewProps } from './PanelContainerViews';

function getPanelVariantClasses(variant: 'default' | 'eldritch' | 'elevated', opaque: boolean): string {
  const base = 'bg-mythos-terminal-surface border-gray-700';
  if (opaque) {
    return `${base} bg-opacity-100`;
  }
  switch (variant) {
    case 'eldritch':
      return 'bg-mythos-terminal-surface border-mythos-terminal-primary';
    case 'elevated':
      return 'bg-mythos-terminal-surface border-gray-600 shadow-lg';
    default:
      return base;
  }
}

export function usePanelContainerBody(props: PanelContainerProps): {
  isMinimized: boolean;
  rndProps: PanelRndViewProps;
} {
  const {
    id,
    title,
    children,
    position,
    size,
    zIndex,
    isMinimized,
    isMaximized,
    minSize = { width: 200, height: 150 },
    maxSize,
    variant = 'default',
    className = '',
    opaque = false,
    minHeight,
    onPositionChange,
    onSizeChange,
    onMinimize,
    onMaximize,
    onClose,
    onFocus,
  } = props;

  const [windowDimensions, setWindowDimensions] = useState(() => ({
    width: typeof window !== 'undefined' ? window.innerWidth : 1920,
    height: typeof window !== 'undefined' ? window.innerHeight : 1080,
  }));

  useEffect(() => {
    const handleResize = () => {
      setWindowDimensions({ width: window.innerWidth, height: window.innerHeight });
    };
    window.addEventListener('resize', handleResize);
    return () => window.removeEventListener('resize', handleResize);
  }, []);

  const maximizedSize = useMemo(() => {
    if (!isMaximized) return null;
    const headerHeight = 48;
    return { width: windowDimensions.width, height: windowDimensions.height - headerHeight };
  }, [isMaximized, windowDimensions.width, windowDimensions.height]);

  const maximizedPosition = useMemo(() => (isMaximized ? { x: 0, y: 48 } : null), [isMaximized]);

  const handleDragStart = useCallback(() => onFocus(id), [id, onFocus]);
  const handleDragStop = useCallback(
    (_e: unknown, d: { x: number; y: number }) => onPositionChange(id, { x: d.x, y: d.y }),
    [id, onPositionChange]
  );
  const handleResizeStop = useCallback(
    (_e: unknown, _direction: unknown, ref: HTMLElement, _delta: unknown, nextPosition: PanelPosition) => {
      onSizeChange(id, { width: ref.offsetWidth, height: ref.offsetHeight });
      onPositionChange(id, nextPosition);
    },
    [id, onSizeChange, onPositionChange]
  );
  const handleMinimize = useCallback(() => onMinimize(id), [id, onMinimize]);
  const handleMaximize = useCallback(() => onMaximize(id), [id, onMaximize]);
  const handleClose = useCallback(() => onClose?.(id), [id, onClose]);

  const variantClasses = useMemo(() => getPanelVariantClasses(variant, opaque), [variant, opaque]);
  const effectiveSize =
    minHeight != null && size.height < minHeight ? { ...size, height: Math.max(size.height, minHeight) } : size;
  const displaySize = isMaximized && maximizedSize ? maximizedSize : effectiveSize;
  const displayPosition = isMaximized && maximizedPosition ? maximizedPosition : position;

  const rndProps: PanelRndViewProps = {
    id,
    title,
    children,
    displayPosition,
    displaySize,
    zIndex,
    variantClasses,
    className,
    opaque,
    minSize,
    maxSize,
    minHeight,
    isMaximized,
    onFocus,
    onDragStart: handleDragStart,
    onDragStop: handleDragStop,
    onResizeStop: handleResizeStop,
    onMinimize: handleMinimize,
    onMaximize: handleMaximize,
    onClose: onClose ? handleClose : undefined,
  };

  return { isMinimized, rndProps };
}
