import React from 'react';
import { Rnd } from 'react-rnd';

import { EldritchIcon, MythosIcons } from '../../ui/EldritchIcon';
import { TerminalButton } from '../../ui/TerminalButton';
import type { PanelPosition, PanelSize, PanelVariant } from '../types';
import { usePanelContainerLayout } from './usePanelContainerLayout';

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

/** Opaque fill behind panel chrome so backdrop art does not show through the face. */
function PanelSolidUnderlay() {
  return (
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
  );
}

// Implementing panel container with react-rnd for drag/resize functionality
// Based on findings from "Non-Euclidean UI Architecture" - Dr. Armitage, 1928
export const PanelContainer: React.FC<PanelContainerProps> = React.memo(props => {
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

  const layout = usePanelContainerLayout({
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
  });

  const displaySize = isMaximized && layout.maximizedSize ? layout.maximizedSize : layout.effectiveSize;
  const displayPosition = isMaximized && layout.maximizedPosition ? layout.maximizedPosition : position;

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
        onDragStop={layout.handleDragStop}
        onDragStart={layout.handleDragStart}
        dragHandleClassName="panel-drag-handle"
        style={{
          zIndex,
          backgroundColor: 'var(--color-mythos-terminal-background, #0a0a0a)',
          opacity: 1,
        }}
        className={`${layout.variantClasses} overflow-hidden border rounded ${className}`}
        data-testid={`game-panel-${id}`}
        data-panel-minimized="true"
        {...(opaque ? { 'data-panel-opaque': 'true' } : {})}
      >
        <PanelSolidUnderlay />
        <div
          className="panel-drag-handle flex items-center justify-between h-full px-3 bg-mythos-terminal-background cursor-move"
          style={{ position: 'relative', zIndex: 1 }}
        >
          <span className="text-sm font-bold text-mythos-terminal-primary">{title}</span>
          <div className="flex items-center gap-2">
            <TerminalButton
              variant="secondary"
              size="sm"
              onClick={layout.handleMinimize}
              className="p-1 h-9 w-9"
              data-testid={`game-panel-${id}-restore`}
            >
              <EldritchIcon name={MythosIcons.restore} size={12} variant="primary" />
            </TerminalButton>
            {onClose && (
              <TerminalButton variant="secondary" size="sm" onClick={layout.handleClose} className="p-1 h-9 w-9">
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
      onDragStop={layout.handleDragStop}
      onDragStart={layout.handleDragStart}
      onResizeStop={layout.handleResizeStop}
      dragHandleClassName="panel-drag-handle"
      style={{
        zIndex,
        backgroundColor: 'var(--color-mythos-terminal-background, #0a0a0a)',
        opacity: 1,
      }}
      className={`${layout.variantClasses} overflow-hidden border rounded ${className}`}
      data-testid={`game-panel-${id}`}
      data-panel-minimized="false"
      {...(opaque ? { 'data-panel-opaque': 'true' } : {})}
      bounds="window"
    >
      {/* Solid underlay on every panel so backdrop art (e.g. tentacles) never reads through the face */}
      <PanelSolidUnderlay />
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
            <TerminalButton
              variant="secondary"
              size="sm"
              onClick={layout.handleMinimize}
              className="p-1 h-9 w-9"
              data-testid={`game-panel-${id}-minimize`}
            >
              <EldritchIcon name={MythosIcons.minimize} size={12} variant="primary" />
            </TerminalButton>
            <TerminalButton variant="secondary" size="sm" onClick={layout.handleMaximize} className="p-1 h-9 w-9">
              <EldritchIcon
                name={isMaximized ? MythosIcons.restore : MythosIcons.maximize}
                size={12}
                variant="primary"
              />
            </TerminalButton>
            {onClose && (
              <TerminalButton variant="secondary" size="sm" onClick={layout.handleClose} className="p-1 h-9 w-9">
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
});

PanelContainer.displayName = 'PanelContainer';
