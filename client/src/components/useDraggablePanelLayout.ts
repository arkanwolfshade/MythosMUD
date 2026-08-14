import { useEffect, useLayoutEffect, useRef, useState } from 'react';
import { relativeSizeToAbsolute, relativeToAbsolute } from './draggablePanelUtils';

function getViewportDimensions(): { width: number; height: number } {
  if (typeof window === 'undefined') return { width: 1920, height: 1080 };
  return { width: window.innerWidth, height: window.innerHeight };
}

function clampPanelPosition(
  position: { x: number; y: number },
  size: { width: number; height: number },
  viewport: { width: number; height: number },
  padding = 50
): { x: number; y: number } {
  return {
    x: Math.max(padding, Math.min(position.x, viewport.width - size.width - padding)),
    y: Math.max(padding, Math.min(position.y, viewport.height - size.height - padding)),
  };
}

function computeInitialPanelState(
  defaultPosition: { x: number; y: number },
  defaultSize: { width: number; height: number }
): { position: { x: number; y: number }; size: { width: number; height: number } } {
  const vp = getViewportDimensions();
  const w = Math.max(vp.width || window.innerWidth || 1920, 1920);
  const h = Math.max(vp.height || window.innerHeight || 1080, 1080);
  const absPos = relativeToAbsolute(defaultPosition, w, h);
  const absSize = relativeSizeToAbsolute(defaultSize, w, h);
  return {
    position: clampPanelPosition(absPos, absSize, { width: w, height: h }),
    size: absSize,
  };
}

function computeFallbackPanelState(
  defaultPosition: { x: number; y: number },
  defaultSize: { width: number; height: number }
): { position: { x: number; y: number }; size: { width: number; height: number } } {
  const fallbackPos = relativeToAbsolute(defaultPosition, 1920, 1080);
  const fallbackSize = relativeSizeToAbsolute(defaultSize, 1920, 1080);
  return {
    position: clampPanelPosition(fallbackPos, fallbackSize, { width: 1920, height: 1080 }),
    size: fallbackSize,
  };
}

function computeSafePanelState(
  defaultPosition: { x: number; y: number },
  defaultSize: { width: number; height: number },
  viewport: { width: number; height: number }
): { position: { x: number; y: number }; size: { width: number; height: number } } {
  const absPos = relativeToAbsolute(defaultPosition, viewport.width, viewport.height);
  const absSize = relativeSizeToAbsolute(defaultSize, viewport.width, viewport.height);
  return {
    position: clampPanelPosition(absPos, absSize, viewport),
    size: absSize,
  };
}

export interface DraggablePanelLayoutProps {
  defaultPosition?: { x: number; y: number };
  defaultSize?: { width: number; height: number };
  minSize?: { width: number; height: number };
  maxSize?: { width: number; height: number };
  className?: string;
  autoSize?: boolean;
  onMinimize?: () => void;
}

export function useDraggablePanelLayout(props: DraggablePanelLayoutProps) {
  const {
    defaultPosition = { x: 50, y: 50 },
    defaultSize = { width: 400, height: 300 },
    minSize = { width: 200, height: 150 },
    maxSize = { width: 800, height: 600 },
    className = '',
    autoSize = false,
  } = props;

  const isGridPositioned = Boolean(className && className.includes('panel-'));
  const [position, setPosition] = useState(() =>
    isGridPositioned ? { x: 0, y: 0 } : computeInitialPanelState(defaultPosition, defaultSize).position
  );
  const [size, setSize] = useState(() =>
    isGridPositioned ? { width: 0, height: 0 } : computeInitialPanelState(defaultPosition, defaultSize).size
  );
  const prevDefaultPositionRef = useRef(defaultPosition);
  const prevDefaultSizeRef = useRef(defaultSize);
  const hasInitializedRef = useRef(false);
  const isRelativePositionRef = useRef(defaultPosition.x <= 1 && defaultPosition.y <= 1);
  const isRelativeSizeRef = useRef(defaultSize.width <= 1 && defaultSize.height <= 1);
  const [isMinimized, setIsMinimized] = useState(false);
  const [headerHeight, setHeaderHeight] = useState(40);
  const panelRef = useRef<HTMLDivElement>(null);
  const headerRef = useRef<HTMLDivElement>(null);
  const contentRef = useRef<HTMLDivElement>(null);

  useLayoutEffect(() => {
    if (isGridPositioned) return;
    const positionChanged =
      prevDefaultPositionRef.current.x !== defaultPosition.x || prevDefaultPositionRef.current.y !== defaultPosition.y;
    const sizeChanged =
      prevDefaultSizeRef.current.width !== defaultSize.width ||
      prevDefaultSizeRef.current.height !== defaultSize.height;
    if (!hasInitializedRef.current || positionChanged || sizeChanged) {
      const applyPanelState = (nextPosition: { x: number; y: number }, nextSize: { width: number; height: number }) => {
        setPosition(prev => (prev.x !== nextPosition.x || prev.y !== nextPosition.y ? nextPosition : prev));
        setSize(prev => (prev.width !== nextSize.width || prev.height !== nextSize.height ? nextSize : prev));
      };
      const fixPosition = () => {
        const currentViewport = getViewportDimensions();
        if (currentViewport.width === 0 || currentViewport.height === 0) {
          const fallback = computeFallbackPanelState(defaultPosition, defaultSize);
          applyPanelState(fallback.position, fallback.size);
          setTimeout(fixPosition, 0);
          return;
        }
        const safe = computeSafePanelState(defaultPosition, defaultSize, currentViewport);
        applyPanelState(safe.position, safe.size);
      };
      fixPosition();
      hasInitializedRef.current = true;
      prevDefaultPositionRef.current = defaultPosition;
      prevDefaultSizeRef.current = defaultSize;
    }
  }, [defaultPosition, defaultSize, isGridPositioned]);

  useEffect(() => {
    if (isGridPositioned || (!isRelativePositionRef.current && !isRelativeSizeRef.current)) return;
    const handleResize = () => {
      const viewport = getViewportDimensions();
      if (isRelativePositionRef.current) {
        const newAbsolutePosition = relativeToAbsolute(defaultPosition, viewport.width, viewport.height);
        const padding = 50;
        setPosition({
          x: Math.max(padding, Math.min(newAbsolutePosition.x, viewport.width - size.width - padding)),
          y: Math.max(padding, Math.min(newAbsolutePosition.y, viewport.height - size.height - padding)),
        });
      }
      if (isRelativeSizeRef.current) {
        setSize(relativeSizeToAbsolute(defaultSize, viewport.width, viewport.height));
      }
    };
    window.addEventListener('resize', handleResize);
    return () => window.removeEventListener('resize', handleResize);
  }, [defaultPosition, defaultSize, size.width, size.height, isGridPositioned]);

  useEffect(() => {
    if (headerRef.current) setHeaderHeight(headerRef.current.offsetHeight);
  }, [isMinimized]);

  useEffect(() => {
    if (isGridPositioned || !autoSize || !contentRef.current || isMinimized) return;
    const contentRect = contentRef.current.getBoundingClientRect();
    const optimalWidth = Math.max(minSize.width, Math.min(maxSize.width, contentRect.width + 40));
    const optimalHeight = Math.max(minSize.height, Math.min(maxSize.height, contentRect.height + 80));
    if (Math.abs(size.width - optimalWidth) > 20 || Math.abs(size.height - optimalHeight) > 20) {
      setSize({ width: optimalWidth, height: optimalHeight });
    }
  }, [autoSize, isMinimized, size.width, size.height, minSize, maxSize, isGridPositioned]);

  const handleMinimize = () => {
    setIsMinimized(prev => !prev);
    props.onMinimize?.();
  };

  return {
    isGridPositioned,
    position,
    size,
    minSize,
    maxSize,
    isMinimized,
    headerHeight,
    panelRef,
    headerRef,
    contentRef,
    setPosition,
    setSize,
    handleMinimize,
  };
}
