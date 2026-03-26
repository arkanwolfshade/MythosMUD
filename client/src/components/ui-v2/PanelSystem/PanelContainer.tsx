import React, { useCallback, useEffect, useMemo, useState } from 'react';
import { Rnd } from 'react-rnd';

import { EldritchIcon, MythosIcons } from '../../ui/EldritchIcon';
import { TerminalButton } from '../../ui/TerminalButton';
import type { PanelPosition, PanelSize, PanelVariant } from '../types';

interface PanelContainerProps {
  id: string;
  title: string;
  children: React.ReactNode;
  position: PanelPosition;
  size: PanelSize;
  zIndex: number;
  isMinimized: boolean;
  isMaximized: boolean;
  isVisible: boolean;
  minSize?: PanelSize;
  maxSize?: PanelSize;
  variant?: PanelVariant;
  className?: string;
  /** Opaque background so panel stays readable over others (e.g. minimap popout). */
  opaque?: boolean;
  /** Minimum content height in px to avoid collapsed content. */
  minHeight?: number;
  onPositionChange: (id: string, position: PanelPosition) => void;
  onSizeChange: (id: string, size: PanelSize) => void;
  onMinimize: (id: string) => void;
  onMaximize: (id: string) => void;
  onClose?: (id: string) => void;
  onFocus: (id: string) => void;
}

// Implementing panel container with react-rnd for drag/resize functionality
// Based on findings from "Non-Euclidean UI Architecture" - Dr. Armitage, 1928
export const PanelContainer: React.FC<PanelContainerProps> = React.memo(
  ({
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
  }) => {
    // Track window dimensions for responsive maximized size calculation
    // As noted in "Viewport-Aware Panel Sizing" - Dr. Armitage, 1928
    const [windowDimensions, setWindowDimensions] = useState(() => ({
      width: typeof window !== 'undefined' ? window.innerWidth : 1920,
      height: typeof window !== 'undefined' ? window.innerHeight : 1080,
    }));

    // Update window dimensions on resize
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

    // Calculate maximized size to fill viewport completely
    // Now recalculates when window dimensions change
    const maximizedSize = useMemo(() => {
      if (!isMaximized) return null;
      const headerHeight = 48; // Header bar height
      // No padding for maximized panels - fill entire viewport
      return {
        width: windowDimensions.width,
        height: windowDimensions.height - headerHeight,
      };
    }, [isMaximized, windowDimensions.width, windowDimensions.height]);

    // Calculate maximized position to fill viewport from top-left
    const maximizedPosition = useMemo(() => {
      if (!isMaximized) return null;
      const headerHeight = 48;
      return { x: 0, y: headerHeight };
    }, [isMaximized]);

    // Handle drag start
    const handleDragStart = useCallback(() => {
      onFocus(id);
    }, [id, onFocus]);

    // Handle drag stop
    const handleDragStop = useCallback(
      (_e: unknown, d: { x: number; y: number }) => {
        onPositionChange(id, { x: d.x, y: d.y });
      },
      [id, onPositionChange]
    );

    // Handle resize stop
    const handleResizeStop = useCallback(
      (_e: unknown, _direction: unknown, ref: HTMLElement, _delta: unknown, position: PanelPosition) => {
        const newSize: PanelSize = {
          width: ref.offsetWidth,
          height: ref.offsetHeight,
        };
        onSizeChange(id, newSize);
        onPositionChange(id, position);
      },
      [id, onSizeChange, onPositionChange]
    );

    // Handle minimize
    const handleMinimize = useCallback(() => {
      onMinimize(id);
    }, [id, onMinimize]);

    // Handle maximize
    const handleMaximize = useCallback(() => {
      onMaximize(id);
    }, [id, onMaximize]);

    // Handle close
    const handleClose = useCallback(() => {
      if (onClose) {
        onClose(id);
      }
    }, [id, onClose]);

    // Get variant classes; opaque panels use full opacity so they stay readable over other panels
    const variantClasses = useMemo(() => {
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
    }, [variant, opaque]);

    // Calculate current display size (maximized or normal)
    // When minHeight is set, ensure at least that height so content (e.g. inline map) is visible
    const effectiveSize =
      minHeight != null && size.height < minHeight ? { ...size, height: Math.max(size.height, minHeight) } : size;
    const displaySize = isMaximized && maximizedSize ? maximizedSize : effectiveSize;
    const displayPosition = isMaximized && maximizedPosition ? maximizedPosition : position;

    if (isMinimized) {
      // Render minimized panel as a small bar
      return (
        <Rnd
          position={displayPosition}
          size={{ width: 200, height: 40 }}
          minWidth={200}
          minHeight={40}
          maxWidth={400}
          maxHeight={40}
          enableResizing={false}
          onDragStop={handleDragStop}
          onDragStart={handleDragStart}
          dragHandleClassName="panel-drag-handle"
          style={{
            zIndex,
            backgroundColor: 'var(--color-mythos-terminal-background, #0a0a0a)',
            opacity: 1,
          }}
          className={`${variantClasses} overflow-hidden border rounded ${className}`}
          {...(opaque ? { 'data-panel-opaque': 'true' } : {})}
        >
          <div
            style={{
              position: 'absolute',
              inset: 0,
              backgroundColor: 'var(--color-mythos-terminal-background, #0a0a0a)',
              zIndex: 0,
              pointerEvents: 'none',
              borderRadius: 'inherit',
            }}
            aria-hidden
          />
          <div
            className="panel-drag-handle flex items-center justify-between h-full px-3 bg-mythos-terminal-background cursor-move"
            style={{ position: 'relative', zIndex: 1 }}
          >
            <span className="text-sm font-bold text-mythos-terminal-primary">{title}</span>
            <div className="flex items-center gap-2">
              <TerminalButton variant="secondary" size="sm" onClick={handleMaximize} className="p-1 h-9 w-9">
                <EldritchIcon
                  name={isMaximized ? MythosIcons.restore : MythosIcons.maximize}
                  size={12}
                  variant="primary"
                />
              </TerminalButton>
              {onClose && (
                <TerminalButton variant="secondary" size="sm" onClick={handleClose} className="p-1 h-9 w-9">
                  <EldritchIcon name={MythosIcons.close} size={12} variant="error" />
                </TerminalButton>
              )}
            </div>
          </div>
        </Rnd>
      );
    }

    return (
      <Rnd
        position={displayPosition}
        size={displaySize}
        minWidth={minSize.width}
        minHeight={minSize.height}
        maxWidth={maxSize?.width}
        maxHeight={maxSize?.height}
        enableResizing={{
          top: true,
          right: true,
          bottom: true,
          left: true,
          topRight: true,
          bottomRight: true,
          bottomLeft: true,
          topLeft: true,
        }}
        onDragStop={handleDragStop}
        onDragStart={handleDragStart}
        onResizeStop={handleResizeStop}
        dragHandleClassName="panel-drag-handle"
        style={{
          zIndex,
          backgroundColor: 'var(--color-mythos-terminal-background, #0a0a0a)',
          opacity: 1,
        }}
        className={`${variantClasses} overflow-hidden border rounded ${className}`}
        {...(opaque ? { 'data-panel-opaque': 'true' } : {})}
        bounds="window"
      >
        {/* Solid underlay on every panel so backdrop art (e.g. tentacles) never reads through the face */}
        <div
          style={{
            position: 'absolute',
            inset: 0,
            backgroundColor: 'var(--color-mythos-terminal-background, #0a0a0a)',
            zIndex: 0,
            pointerEvents: 'none',
            borderRadius: 'inherit',
          }}
          aria-hidden
        />
        <div
          className="h-full flex flex-col bg-mythos-terminal-background"
          style={{
            position: 'relative',
            zIndex: 1,
            backgroundColor: 'var(--color-mythos-terminal-background, #0a0a0a)',
            opacity: 1,
          }}
        >
          {/* Panel Header: only this area triggers drag; scrolling content no longer moves the panel */}
          {/* eslint-disable-next-line jsx-a11y/no-static-element-interactions -- drag handle uses mousedown; panel controls are separate buttons */}
          <div
            className="panel-drag-handle flex items-center justify-between p-2 border-b border-gray-700 bg-mythos-terminal-surface cursor-move"
            onMouseDown={() => onFocus(id)}
          >
            <span className="text-sm font-bold text-mythos-terminal-primary">{title}</span>
            <div className="flex items-center gap-2">
              <TerminalButton variant="secondary" size="sm" onClick={handleMinimize} className="p-1 h-9 w-9">
                <EldritchIcon name={MythosIcons.minimize} size={12} variant="primary" />
              </TerminalButton>
              <TerminalButton variant="secondary" size="sm" onClick={handleMaximize} className="p-1 h-9 w-9">
                <EldritchIcon
                  name={isMaximized ? MythosIcons.restore : MythosIcons.maximize}
                  size={12}
                  variant="primary"
                />
              </TerminalButton>
              {onClose && (
                <TerminalButton variant="secondary" size="sm" onClick={handleClose} className="p-1 h-9 w-9">
                  <EldritchIcon name={MythosIcons.close} size={12} variant="error" />
                </TerminalButton>
              )}
            </div>
          </div>

          {/* Panel Content: min-h-0 lets flex item shrink; minHeight prop avoids collapsed content */}
          <div
            className="flex-1 min-h-0 overflow-auto bg-mythos-terminal-background"
            style={minHeight != null ? { minHeight: `${minHeight}px` } : undefined}
          >
            {children}
          </div>
        </div>
      </Rnd>
    );
  }
);

PanelContainer.displayName = 'PanelContainer';
