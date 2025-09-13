import React from 'react';
import { AVAILABLE_CHANNELS } from '../../../config/channels';

interface ChannelActivityIndicatorsProps {
  selectedChannel: string;
  unreadCounts: Record<string, number>;
  onChannelSelect: (channelId: string) => void;
}

// Function to get activity color classes based on activity level
const getActivityColor = (activityLevel: string): string => {
  switch (activityLevel) {
    case 'high':
      return 'bg-red-500';
    case 'medium':
      return 'bg-yellow-500';
    case 'low':
      return 'bg-green-500';
    case 'none':
    default:
      return 'bg-gray-500';
  }
};

export const ChannelActivityIndicators: React.FC<ChannelActivityIndicatorsProps> = ({
  selectedChannel,
  unreadCounts,
  onChannelSelect,
}) => {
  return (
    <div
      className="flex flex-col sm:flex-row items-start sm:items-center gap-2 sm:gap-4 mt-2"
      role="region"
      aria-label="Channel Activity Indicators"
    >
      <span className="text-xs text-mythos-terminal-text-secondary">Activity:</span>
      <div className="flex flex-wrap items-center gap-2">
        {AVAILABLE_CHANNELS.map(channel => {
          const activityLevel = 'none';
          const unreadCount = unreadCounts[channel.id] || 0;

          return (
            <div
              key={channel.id}
              className="flex items-center gap-1 group cursor-pointer hover:bg-mythos-terminal-background/50 rounded px-1 transition-all duration-200"
              role="button"
              tabIndex={0}
              aria-label={`${channel.name} channel - ${activityLevel} activity${unreadCount > 0 ? `, ${unreadCount} unread messages` : ''}`}
              onKeyDown={e => {
                if (e.key === 'Enter' || e.key === ' ') {
                  e.preventDefault();
                  onChannelSelect(channel.id);
                }
              }}
            >
              <div
                className={`w-2 h-2 rounded-full ${getActivityColor(activityLevel)} transition-all duration-300 ${activityLevel === 'high' ? 'animate-pulse' : ''}`}
              ></div>
              <span className="text-xs text-mythos-terminal-text-secondary group-hover:text-mythos-terminal-primary transition-colors duration-200">
                {channel.name}
              </span>
              {unreadCount > 0 && (
                <div className="bg-mythos-terminal-error text-white text-xs rounded-full px-1 min-w-[16px] h-4 flex items-center justify-center animate-bounce">
                  {unreadCount > 99 ? '99+' : unreadCount}
                </div>
              )}
            </div>
          );
        })}
      </div>
    </div>
  );
};
