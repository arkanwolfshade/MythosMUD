import { useCallback, useEffect, useMemo, useState } from 'react';

import type { PanelPosition, PanelSize, PanelVariant } from '../types';

const HEADER_HEIGHT = 48;

export interface PanelContainerLayoutInput {
  id: string;
  size: PanelSize;
  isMaximized: boolean;
  minHeight?: number;
  variant: PanelVariant;
  opaque: boolean;
  onPositionChange: (id: string, position: PanelPosition) => void;
  onSizeChange: (id: string, size: PanelSize) => void;
  onMinimize: (id: string) => void;
  onMaximize: (id: string) => void;
  onClose?: (id: string) => void;
  onFocus: (id: string) => void;
}

export function usePanelContainerLayout(input: PanelContainerLayoutInput) {
  const {
    id,
    size,
    isMaximized,
    minHeight,
    variant,
    opaque,
    onPositionChange,
    onSizeChange,
    onMinimize,
    onMaximize,
    onClose,
    onFocus,
  } = input;

  const [windowDimensions, setWindowDimensions] = useState(() => ({
    width: typeof window !== 'undefined' ? window.innerWidth : 1920,
    height: typeof window !== 'undefined' ? window.innerHeight : 1080,
  }));

  useEffect(() => {
    const handleResize = () => {
      setWindowDimensions({
        width: window.innerWidth,
        height: window.innerHeight,
      });
    };
    window.addEventListener('resize', handleResize);
    return () => {
      window.removeEventListener('resize', handleResize);
    };
  }, []);

  const maximizedSize = useMemo(() => {
    if (!isMaximized) return null;
    return {
      width: windowDimensions.width,
      height: windowDimensions.height - HEADER_HEIGHT,
    };
  }, [isMaximized, windowDimensions.width, windowDimensions.height]);

  const maximizedPosition = useMemo(() => {
    if (!isMaximized) return null;
    return { x: 0, y: HEADER_HEIGHT };
  }, [isMaximized]);

  const handleDragStart = useCallback(() => {
    onFocus(id);
  }, [id, onFocus]);

  const handleDragStop = useCallback(
    (_e: unknown, d: { x: number; y: number }) => {
      onPositionChange(id, { x: d.x, y: d.y });
    },
    [id, onPositionChange]
  );

  const handleResizeStop = useCallback(
    (_e: unknown, _direction: unknown, ref: HTMLElement, _delta: unknown, position: PanelPosition) => {
      onSizeChange(id, { width: ref.offsetWidth, height: ref.offsetHeight });
      onPositionChange(id, position);
    },
    [id, onSizeChange, onPositionChange]
  );

  const handleMinimize = useCallback(() => {
    onMinimize(id);
  }, [id, onMinimize]);

  const handleMaximize = useCallback(() => {
    onMaximize(id);
  }, [id, onMaximize]);

  const handleClose = useCallback(() => {
    if (onClose) {
      onClose(id);
    }
  }, [id, onClose]);

  const variantClasses = useMemo(() => {
    const base = 'bg-mythos-terminal-surface border-mythos-terminal-border';
    if (opaque) {
      return `${base} bg-opacity-100`;
    }
    switch (variant) {
      case 'eldritch':
        return 'bg-mythos-terminal-surface border-mythos-terminal-primary';
      case 'elevated':
        return 'bg-mythos-terminal-surface border-mythos-terminal-border shadow-lg';
      case 'default':
        return base;
      default: {
        const _exhaustive: never = variant;
        return _exhaustive;
      }
    }
  }, [variant, opaque]);

  const effectiveSize =
    minHeight != null && size.height < minHeight ? { ...size, height: Math.max(size.height, minHeight) } : size;

  return {
    maximizedSize,
    maximizedPosition,
    handleDragStart,
    handleDragStop,
    handleResizeStop,
    handleMinimize,
    handleMaximize,
    handleClose,
    variantClasses,
    effectiveSize,
  };
}
