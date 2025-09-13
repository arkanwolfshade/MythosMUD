import React from 'react';
import { AVAILABLE_CHANNELS } from '../../../config/channels';
import { ChannelSelector } from '../../ui/ChannelSelector';

interface ChannelSelectorSectionProps {
  selectedChannel: string;
  onChannelSelect: (channelId: string) => void;
  disabled?: boolean;
  isConnected?: boolean;
}

export const ChannelSelectorSection: React.FC<ChannelSelectorSectionProps> = ({
  selectedChannel,
  onChannelSelect,
  disabled = false,
  isConnected = true,
}) => {
  return (
    <div
      className="p-3 border-b border-gray-700 bg-mythos-terminal-surface"
      role="region"
      aria-label="Channel Selection"
    >
      <div className="flex flex-col sm:flex-row items-start sm:items-center gap-2">
        <span className="text-sm text-mythos-terminal-text-secondary font-mono">Channel:</span>
        <ChannelSelector
          channels={AVAILABLE_CHANNELS}
          selectedChannel={selectedChannel}
          onChannelSelect={onChannelSelect}
          disabled={disabled || !isConnected}
          className="flex-1 w-full sm:w-auto"
        />
      </div>
    </div>
  );
};
