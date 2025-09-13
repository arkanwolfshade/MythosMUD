import React from 'react';
import { EldritchIcon, MythosIcons } from '../../ui/EldritchIcon';
import { TerminalButton } from '../../ui/TerminalButton';

interface ChatHistoryToggleProps {
  showChatHistory: boolean;
  onToggleHistory: () => void;
  chatFilter: string;
  onFilterChange: (filter: string) => void;
  currentChannelMessages: number;
}

export const ChatHistoryToggle: React.FC<ChatHistoryToggleProps> = ({
  showChatHistory,
  onToggleHistory,
  chatFilter,
  onFilterChange,
  currentChannelMessages,
}) => {
  return (
    <div className="p-2 border-b border-gray-700 bg-mythos-terminal-background">
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-2">
          <TerminalButton
            variant="secondary"
            size="sm"
            onClick={onToggleHistory}
            className="flex items-center gap-2 text-xs"
          >
            <EldritchIcon name={MythosIcons.clock} size={12} variant="primary" />
            <span>Chat History</span>
          </TerminalButton>
          <select
            value={chatFilter}
            onChange={e => onFilterChange(e.target.value)}
            className="bg-mythos-terminal-surface border border-gray-700 rounded px-2 py-1 text-xs text-mythos-terminal-text"
          >
            <option value="all">All Messages</option>
            <option value="current">Current Channel</option>
          </select>
        </div>
        <div className="text-xs text-mythos-terminal-text-secondary">{currentChannelMessages} messages</div>
      </div>
    </div>
  );
};
