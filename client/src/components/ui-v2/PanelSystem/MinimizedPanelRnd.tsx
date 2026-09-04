import React from 'react';
import { Rnd } from 'react-rnd';

import type { PanelPosition } from '../types';
import { MinimizedPanelHeader } from './MinimizedPanelHeader';
import { PanelSolidUnderlay } from './PanelSolidUnderlay';
import type { PanelLayoutHandlers } from './panelLayoutTypes';

export interface MinimizedPanelRndProps {
  id: string;
  title: string;
  children: React.ReactNode;
  displayPosition: PanelPosition;
  zIndex: number;
  opaque: boolean;
  className: string;
  onClose?: (id: string) => void;
  layout: PanelLayoutHandlers;
}

export function MinimizedPanelRnd(props: MinimizedPanelRndProps) {
  const { id, title, children, displayPosition, zIndex, opaque, className, onClose, layout } = props;
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
      <MinimizedPanelHeader id={id} title={title} onClose={onClose} layout={layout} />
      {/* Content stays mounted while minimized so panel state and its DOM survive a collapse.
          The hidden attribute keeps it out of layout and the accessibility tree. */}
      <div hidden>{children}</div>
    </Rnd>
  );
}
