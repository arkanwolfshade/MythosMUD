import React from 'react';
import { EldritchIcon, MythosIcons } from '../../ui/EldritchIcon';
import { TerminalButton } from '../../ui/TerminalButton';

interface ChatHeaderProps {
  onClearMessages?: () => void;
  onDownloadLogs?: () => void;
}

export const ChatHeader: React.FC<ChatHeaderProps> = ({ onClearMessages, onDownloadLogs }) => {
  return (
    <div className="flex items-center justify-between p-3 border-b border-gray-700 bg-mythos-terminal-surface">
      <div className="flex items-center gap-2">
        <EldritchIcon name={MythosIcons.chat} size={20} variant="primary" />
        <h3 className="text-mythos-terminal-primary font-bold">Chat</h3>
      </div>
      <div className="flex items-center gap-2">
        {onClearMessages && (
          <TerminalButton variant="secondary" size="sm" onClick={onClearMessages} className="p-2 h-8 w-8">
            <EldritchIcon name={MythosIcons.clear} size={14} variant="error" />
          </TerminalButton>
        )}
        {onDownloadLogs && (
          <TerminalButton variant="secondary" size="sm" onClick={onDownloadLogs} className="p-2 h-8 w-8">
            <EldritchIcon name={MythosIcons.download} size={14} variant="primary" />
          </TerminalButton>
        )}
      </div>
    </div>
  );
};
