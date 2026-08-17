import React from 'react';

import { ExpandedPanelHeader } from './ExpandedPanelHeader';
import { PanelSolidUnderlay } from './PanelSolidUnderlay';
import type { PanelLayoutHandlers } from './panelLayoutTypes';

interface ExpandedPanelBodyProps {
  id: string;
  title: string;
  children: React.ReactNode;
  isMaximized: boolean;
  minHeight?: number;
  onClose?: (id: string) => void;
  onFocus: (id: string) => void;
  layout: PanelLayoutHandlers;
}

/** Underlay + header + scrollable content inside an expanded panel shell. */
export function ExpandedPanelBody(props: ExpandedPanelBodyProps) {
  const { id, title, children, isMaximized, minHeight, onClose, onFocus, layout } = props;
  return (
    <>
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
        <ExpandedPanelHeader
          id={id}
          title={title}
          isMaximized={isMaximized}
          onClose={onClose}
          onFocus={onFocus}
          layout={layout}
        />
        {/* Panel Content: min-h-0 lets flex item shrink; minHeight prop avoids collapsed content */}
        <div
          className="flex-1 min-h-0 overflow-auto bg-mythos-terminal-background"
          style={minHeight != null ? { minHeight: `${minHeight}px` } : undefined}
        >
          {children}
        </div>
      </div>
    </>
  );
}
