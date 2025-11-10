import React, { useState } from 'react';
import { EldritchIcon, MythosIcons } from './EldritchIcon';

export interface Channel {
  id: string;
  name: string;
  description: string;
  icon: keyof typeof MythosIcons;
  color: string;
  shortcut?: string;
  disabled?: boolean;
}

interface ChannelSelectorProps {
  channels: Channel[];
  selectedChannel: string;
  onChannelSelect: (channelId: string) => void;
  disabled?: boolean;
  className?: string;
}

export const ChannelSelector: React.FC<ChannelSelectorProps> = ({
  channels,
  selectedChannel,
  onChannelSelect,
  disabled = false,
  className = '',
}) => {
  const [isOpen, setIsOpen] = useState(false);

  const selectedChannelData = channels.find(channel => channel.id === selectedChannel);

  const handleChannelSelect = (channelId: string) => {
    onChannelSelect(channelId);
    setIsOpen(false);
  };

  const toggleDropdown = () => {
    if (!disabled) {
      setIsOpen(!isOpen);
    }
  };

  const handleBackdropClick = (e: React.MouseEvent) => {
    // Prevent event bubbling to avoid triggering other click handlers
    e.stopPropagation();
    setIsOpen(false);
  };

  return (
    <div className={`relative ${className}`}>
      <select
        data-testid="channel-selector"
        value={selectedChannel}
        onChange={e => handleChannelSelect(e.target.value)}
        disabled={disabled}
        className="sr-only"
      >
        {channels.map(channel => (
          <option key={channel.id} value={channel.id} disabled={channel.disabled}>
            {channel.name}
          </option>
        ))}
      </select>

      {/* Backdrop to close dropdown when clicking outside - positioned BEFORE dropdown */}
      {isOpen && <div className="fixed inset-0 z-10" onClick={handleBackdropClick} data-testid="dropdown-backdrop" />}

      {/* Channel Selector Button */}
      <button
        onClick={toggleDropdown}
        disabled={disabled}
        className={`
          relative z-20 flex items-center gap-2 px-3 py-2 bg-mythos-terminal-surface border border-gray-700 rounded
          text-sm font-mono transition-all duration-200 min-w-[140px]
          ${
            disabled
              ? 'opacity-50 cursor-not-allowed'
              : 'hover:border-mythos-terminal-primary/50 hover:bg-mythos-terminal-background cursor-pointer'
          }
          ${isOpen ? 'border-mythos-terminal-primary bg-mythos-terminal-background' : ''}
        `}
      >
        {selectedChannelData && (
          <>
            <EldritchIcon name={selectedChannelData.icon} size={16} variant="primary" />
            <span className="text-mythos-terminal-text">{selectedChannelData.name}</span>
            {selectedChannelData.shortcut && (
              <span className="text-xs text-mythos-terminal-text-secondary ml-auto">
                /{selectedChannelData.shortcut}
              </span>
            )}
          </>
        )}
        <EldritchIcon
          name={MythosIcons.exit}
          size={12}
          variant="secondary"
          className={`transition-transform duration-200 ${isOpen ? 'rotate-90' : ''}`}
        />
      </button>

      {/* Dropdown Menu - positioned AFTER backdrop but with higher z-index */}
      {isOpen && !disabled && (
        <div className="absolute top-full left-0 right-0 mt-1 bg-mythos-terminal-surface border border-gray-700 rounded shadow-lg z-30 max-h-60 overflow-y-auto">
          {channels.map(channel => (
            <button
              key={channel.id}
              onClick={() => handleChannelSelect(channel.id)}
              disabled={channel.disabled}
              className={`
                w-full flex items-center gap-3 px-3 py-2 text-left text-sm font-mono
                transition-colors duration-200 border-b border-gray-700 last:border-b-0
                ${
                  channel.disabled
                    ? 'opacity-50 cursor-not-allowed text-mythos-terminal-text-secondary'
                    : 'hover:bg-mythos-terminal-background cursor-pointer'
                }
                ${
                  selectedChannel === channel.id
                    ? 'bg-mythos-terminal-primary/20 border-mythos-terminal-primary/50'
                    : 'text-mythos-terminal-text'
                }
              `}
            >
              <EldritchIcon
                name={channel.icon}
                size={16}
                variant={selectedChannel === channel.id ? 'primary' : 'secondary'}
              />
              <div className="flex-1">
                <div className="flex items-center gap-2">
                  <span className={selectedChannel === channel.id ? 'text-mythos-terminal-primary font-bold' : ''}>
                    {channel.name}
                  </span>
                  {channel.shortcut && (
                    <span className="text-xs text-mythos-terminal-text-secondary">/{channel.shortcut}</span>
                  )}
                </div>
                <div className="text-xs text-mythos-terminal-text-secondary mt-1">{channel.description}</div>
              </div>
              {selectedChannel === channel.id && (
                <EldritchIcon name={MythosIcons.connection} size={12} variant="success" />
              )}
            </button>
          ))}
        </div>
      )}
    </div>
  );
};
