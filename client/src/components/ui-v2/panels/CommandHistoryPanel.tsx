import React from 'react';
import { EldritchIcon, MythosIcons } from '../../ui/EldritchIcon';
import { TerminalButton } from '../../ui/TerminalButton';

interface CommandHistoryPanelProps {
  commandHistory: string[];
  onClearHistory?: () => void;
  onSelectCommand?: (command: string) => void;
}

// Display command history
// Based on findings from "Command Interface Patterns" - Dr. Armitage, 1928
export const CommandHistoryPanel: React.FC<CommandHistoryPanelProps> = ({
  commandHistory,
  onClearHistory,
  onSelectCommand,
}) => {
  return (
    <div className="h-full flex flex-col">
      <div className="flex items-center justify-between p-3 border-b border-gray-700 bg-mythos-terminal-surface">
        <div className="flex items-center gap-2">
          <EldritchIcon name={MythosIcons.command} size={20} variant="primary" />
          <h3 className="text-sm font-bold text-mythos-terminal-primary">Command History</h3>
        </div>
        {onClearHistory && commandHistory.length > 0 && (
          <TerminalButton variant="secondary" size="sm" onClick={onClearHistory} className="px-2 py-1 text-xs">
            Clear
          </TerminalButton>
        )}
      </div>

      <div className="flex-1 overflow-y-auto p-3 space-y-1 min-h-[150px]">
        {commandHistory.length === 0 ? (
          <div className="text-center text-mythos-terminal-text-secondary py-4">
            <EldritchIcon name={MythosIcons.command} size={24} className="mx-auto mb-2 opacity-50" />
            <p className="text-xs">No commands yet</p>
          </div>
        ) : (
          <div className="space-y-1">
            {commandHistory
              .slice(-10)
              .reverse()
              .map((command, index) => (
                <div
                  key={index}
                  className="text-xs text-mythos-terminal-text-secondary cursor-pointer hover:text-mythos-terminal-text p-1 rounded hover:bg-mythos-terminal-background"
                  onClick={() => onSelectCommand?.(command)}
                >
                  {command}
                </div>
              ))}
          </div>
        )}
      </div>
    </div>
  );
};
