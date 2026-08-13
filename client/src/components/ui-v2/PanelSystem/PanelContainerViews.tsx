import React from 'react';
import { Rnd } from 'react-rnd';

import { EldritchIcon, MythosIcons } from '../../ui/EldritchIcon';
import { TerminalButton } from '../../ui/TerminalButton';
import type { PanelPosition, PanelSize } from '../types';
import { PanelSolidUnderlay } from './PanelContainerShared';

export interface PanelRndViewProps {
  id: string;
  title: string;
  children: React.ReactNode;
  displayPosition: PanelPosition;
  displaySize: PanelSize;
  zIndex: number;
  variantClasses: string;
  className: string;
  opaque: boolean;
  minSize: PanelSize;
  maxSize?: PanelSize;
  minHeight?: number;
  isMaximized: boolean;
  onFocus: (id: string) => void;
  onDragStart: () => void;
  onDragStop: (_e: unknown, d: { x: number; y: number }) => void;
  onResizeStop: (_e: unknown, _direction: unknown, ref: HTMLElement, _delta: unknown, position: PanelPosition) => void;
  onMinimize: () => void;
  onMaximize: () => void;
  onClose?: () => void;
}

export function MinimizedPanelRnd(props: PanelRndViewProps): React.ReactElement {
  return (
    <Rnd
      position={props.displayPosition}
      size={{ width: 200, height: 40 }}
      minWidth={200}
      minHeight={40}
      maxWidth={400}
      maxHeight={40}
      enableResizing={false}
      onDragStop={props.onDragStop}
      onDragStart={props.onDragStart}
      dragHandleClassName="panel-drag-handle"
      style={{
        zIndex: props.zIndex,
        backgroundColor: 'var(--color-mythos-terminal-background, #0a0a0a)',
        opacity: 1,
      }}
      className={`${props.variantClasses} overflow-hidden border rounded ${props.className}`}
      data-testid={`game-panel-${props.id}`}
      data-panel-minimized="true"
      {...(props.opaque ? { 'data-panel-opaque': 'true' } : {})}
    >
      <PanelSolidUnderlay />
      <div
        className="panel-drag-handle flex items-center justify-between h-full px-3 bg-mythos-terminal-background cursor-move"
        style={{ position: 'relative', zIndex: 1 }}
      >
        <span className="text-sm font-bold text-mythos-terminal-primary">{props.title}</span>
        <div className="flex items-center gap-2">
          <TerminalButton
            variant="secondary"
            size="sm"
            onClick={props.onMinimize}
            className="p-1 h-9 w-9"
            data-testid={`game-panel-${props.id}-restore`}
          >
            <EldritchIcon name={MythosIcons.restore} size={12} variant="primary" />
          </TerminalButton>
          {props.onClose && (
            <TerminalButton variant="secondary" size="sm" onClick={props.onClose} className="p-1 h-9 w-9">
              <EldritchIcon name={MythosIcons.close} size={12} variant="error" />
            </TerminalButton>
          )}
        </div>
      </div>
    </Rnd>
  );
}

export function ExpandedPanelRnd(props: PanelRndViewProps): React.ReactElement {
  return (
    <Rnd
      position={props.displayPosition}
      size={props.displaySize}
      minWidth={props.minSize.width}
      minHeight={props.minSize.height}
      maxWidth={props.maxSize?.width}
      maxHeight={props.maxSize?.height}
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
      onDragStop={props.onDragStop}
      onDragStart={props.onDragStart}
      onResizeStop={props.onResizeStop}
      dragHandleClassName="panel-drag-handle"
      style={{
        zIndex: props.zIndex,
        backgroundColor: 'var(--color-mythos-terminal-background, #0a0a0a)',
        opacity: 1,
      }}
      className={`${props.variantClasses} overflow-hidden border rounded ${props.className}`}
      data-testid={`game-panel-${props.id}`}
      data-panel-minimized="false"
      {...(props.opaque ? { 'data-panel-opaque': 'true' } : {})}
      bounds="window"
    >
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
        {/* eslint-disable-next-line jsx-a11y/no-static-element-interactions -- drag handle uses mousedown; panel controls are separate buttons */}
        <div
          className="panel-drag-handle flex items-center justify-between p-2 border-b border-gray-700 bg-mythos-terminal-surface cursor-move"
          onMouseDown={() => props.onFocus(props.id)}
        >
          <span className="text-sm font-bold text-mythos-terminal-primary">{props.title}</span>
          <div className="flex items-center gap-2">
            <TerminalButton
              variant="secondary"
              size="sm"
              onClick={props.onMinimize}
              className="p-1 h-9 w-9"
              data-testid={`game-panel-${props.id}-minimize`}
            >
              <EldritchIcon name={MythosIcons.minimize} size={12} variant="primary" />
            </TerminalButton>
            <TerminalButton variant="secondary" size="sm" onClick={props.onMaximize} className="p-1 h-9 w-9">
              <EldritchIcon
                name={props.isMaximized ? MythosIcons.restore : MythosIcons.maximize}
                size={12}
                variant="primary"
              />
            </TerminalButton>
            {props.onClose && (
              <TerminalButton variant="secondary" size="sm" onClick={props.onClose} className="p-1 h-9 w-9">
                <EldritchIcon name={MythosIcons.close} size={12} variant="error" />
              </TerminalButton>
            )}
          </div>
        </div>
        <div
          className="flex-1 min-h-0 overflow-auto bg-mythos-terminal-background"
          style={props.minHeight != null ? { minHeight: `${props.minHeight}px` } : undefined}
        >
          {props.children}
        </div>
      </div>
    </Rnd>
  );
}
