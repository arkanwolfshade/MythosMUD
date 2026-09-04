import React from 'react';
import { Rnd } from 'react-rnd';

import type { PanelPosition, PanelSize } from '../types';
import type { PanelLayoutHandlers } from './panelLayoutTypes';
import { ExpandedPanelBody } from './ExpandedPanelBody';

const EXPANDED_RESIZE_EDGES = {
  top: true,
  right: true,
  bottom: true,
  left: true,
  topRight: true,
  bottomRight: true,
  bottomLeft: true,
  topLeft: true,
} as const;

function panelShellStyle(zIndex: number) {
  return {
    zIndex,
    backgroundColor: 'var(--color-mythos-terminal-background, #0a0a0a)',
    opacity: 1,
  };
}

export interface ExpandedPanelRndProps {
  id: string;
  title: string;
  children: React.ReactNode;
  displayPosition: PanelPosition;
  displaySize: PanelSize;
  zIndex: number;
  isMaximized: boolean;
  opaque: boolean;
  className: string;
  minSize: PanelSize;
  maxSize?: PanelSize;
  minHeight?: number;
  onClose?: (id: string) => void;
  onFocus: (id: string) => void;
  layout: PanelLayoutHandlers;
}

export function ExpandedPanelRnd(props: ExpandedPanelRndProps) {
  const { id, displayPosition, displaySize, zIndex, opaque, className, minSize, maxSize, layout } = props;
  return (
    <Rnd
      position={displayPosition}
      size={displaySize}
      minWidth={minSize.width}
      minHeight={minSize.height}
      maxWidth={maxSize?.width}
      maxHeight={maxSize?.height}
      enableResizing={EXPANDED_RESIZE_EDGES}
      onDragStop={layout.handleDragStop}
      onDragStart={layout.handleDragStart}
      onResizeStop={layout.handleResizeStop}
      dragHandleClassName="panel-drag-handle"
      style={panelShellStyle(zIndex)}
      className={`${layout.variantClasses} overflow-hidden border rounded ${className}`}
      data-testid={`game-panel-${id}`}
      data-panel-minimized="false"
      {...(opaque ? { 'data-panel-opaque': 'true' } : {})}
      bounds="window"
    >
      <ExpandedPanelBody
        id={id}
        title={props.title}
        isMaximized={props.isMaximized}
        minHeight={props.minHeight}
        onClose={props.onClose}
        onFocus={props.onFocus}
        layout={layout}
      >
        {props.children}
      </ExpandedPanelBody>
    </Rnd>
  );
}
