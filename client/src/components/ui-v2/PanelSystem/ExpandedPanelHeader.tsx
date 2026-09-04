import React from 'react';

import { EldritchIcon, MythosIcons } from '../../ui/EldritchIcon';
import { TerminalButton } from '../../ui/TerminalButton';
import type { PanelLayoutHandlers } from './panelLayoutTypes';

interface ExpandedPanelHeaderProps {
  id: string;
  title: string;
  isMaximized: boolean;
  onClose?: (id: string) => void;
  onFocus: (id: string) => void;
  layout: PanelLayoutHandlers;
}

export function ExpandedPanelHeader({ id, title, isMaximized, onClose, onFocus, layout }: ExpandedPanelHeaderProps) {
  return (
    // eslint-disable-next-line jsx-a11y/no-static-element-interactions -- drag handle uses mousedown; panel controls are separate buttons
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
          <EldritchIcon name={isMaximized ? MythosIcons.restore : MythosIcons.maximize} size={12} variant="primary" />
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
