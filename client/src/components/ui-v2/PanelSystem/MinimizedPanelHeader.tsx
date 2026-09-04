import React from 'react';

import { EldritchIcon, MythosIcons } from '../../ui/EldritchIcon';
import { TerminalButton } from '../../ui/TerminalButton';
import type { PanelLayoutHandlers } from './panelLayoutTypes';

interface MinimizedPanelHeaderProps {
  id: string;
  title: string;
  onClose?: (id: string) => void;
  layout: PanelLayoutHandlers;
}

export function MinimizedPanelHeader({ id, title, onClose, layout }: MinimizedPanelHeaderProps) {
  return (
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
  );
}
