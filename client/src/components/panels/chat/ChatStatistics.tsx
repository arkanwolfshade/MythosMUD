import React from 'react';
import { AVAILABLE_CHANNELS } from '../../../config/channels';
import { EldritchIcon, MythosIcons } from '../../ui/EldritchIcon';

interface ChatStatisticsProps {
  selectedChannel: string;
  currentChannelMessages: number;
  unreadCounts: Record<string, number>;
}

export const ChatStatistics: React.FC<ChatStatisticsProps> = ({
  selectedChannel,
  currentChannelMessages,
  unreadCounts,
}) => {
  const totalUnread = Object.values(unreadCounts).reduce((sum, count) => sum + count, 0);

  return (
    <div className="p-2 border-t border-gray-700 bg-mythos-terminal-surface" role="status" aria-label="Chat Statistics">
      <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between text-xs text-mythos-terminal-text-secondary gap-2 sm:gap-0">
        <div className="flex flex-wrap items-center gap-2 sm:gap-4">
          <div className="flex items-center gap-1">
            <div className="w-2 h-2 bg-mythos-terminal-success rounded-full"></div>
            <span>Connected</span>
          </div>
          <div className="flex items-center gap-1">
            <EldritchIcon name={MythosIcons.chat} size={12} variant="secondary" />
            <span>{currentChannelMessages} messages</span>
          </div>
          <div className="flex items-center gap-1">
            <EldritchIcon name={MythosIcons.connection} size={12} variant="secondary" />
            <span>Channel: {AVAILABLE_CHANNELS.find(c => c.id === selectedChannel)?.name}</span>
          </div>
          <div className="flex items-center gap-1">
            <EldritchIcon name={MythosIcons.clock} size={12} variant="secondary" />
            <span>0 sent</span>
          </div>
          <div className="flex items-center gap-1">
            <div className="w-2 h-2 rounded-full bg-gray-600"></div>
            <span>Activity: none</span>
          </div>
          {totalUnread > 0 && (
            <div className="flex items-center gap-1">
              <EldritchIcon name={MythosIcons.chat} size={12} variant="error" />
              <span>{totalUnread} unread</span>
            </div>
          )}
        </div>
        <div className="text-xs opacity-75">MythosMUD Terminal</div>
      </div>
    </div>
  );
};
