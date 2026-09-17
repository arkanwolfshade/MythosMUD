import React, { useEffect, useState } from 'react';
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

function ChannelDropdownMenu({
  channels,
  selectedChannel,
  onChannelSelect,
}: {
  channels: Channel[];
  selectedChannel: string;
  onChannelSelect: (channelId: string) => void;
}) {
  return (
    <div
      className="absolute top-full left-0 right-0 mt-1 bg-mythos-terminal-surface border border-mythos-terminal-border rounded shadow-lg z-30 max-h-60 overflow-y-auto"
      data-testid="channel-dropdown"
    >
      {channels.map(channel => (
        <button
          key={channel.id}
          onClick={() => onChannelSelect(channel.id)}
          disabled={channel.disabled}
          className={`
            w-full flex items-center gap-3 px-3 py-2 text-left text-sm font-mono
            transition-colors duration-200 border-b border-mythos-terminal-border last:border-b-0
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
          {selectedChannel === channel.id && <EldritchIcon name={MythosIcons.connection} size={12} variant="success" />}
        </button>
      ))}
    </div>
  );
}

function ChannelSelectorUi({
  ui,
}: {
  ui: {
    channels: Channel[];
    selectedChannel: string;
    disabled: boolean;
    className: string;
    isOpen: boolean;
    selectedChannelData: Channel | undefined;
    onChannelSelect: (channelId: string) => void;
    onToggleDropdown: () => void;
    onBackdropClick: (e: React.MouseEvent) => void;
    onBackdropKeyDown: (e: React.KeyboardEvent) => void;
  };
}) {
  const {
    channels,
    selectedChannel,
    disabled,
    className,
    isOpen,
    selectedChannelData,
    onChannelSelect,
    onToggleDropdown,
    onBackdropClick,
    onBackdropKeyDown,
  } = ui;
  return (
    <div className={`relative ${className}`}>
      <select
        data-testid="channel-selector"
        value={selectedChannel}
        onChange={e => onChannelSelect(e.target.value)}
        disabled={disabled}
        className="sr-only"
      >
        {channels.map(channel => (
          <option key={channel.id} value={channel.id} disabled={channel.disabled}>
            {channel.name}
          </option>
        ))}
      </select>

      {isOpen && (
        <div
          className="fixed inset-0 z-10"
          onClick={onBackdropClick}
          onKeyDown={onBackdropKeyDown}
          role="button"
          aria-label="Close dropdown"
          tabIndex={0}
          data-testid="dropdown-backdrop"
        />
      )}

      <button
        onClick={onToggleDropdown}
        disabled={disabled}
        className={`
          relative z-20 flex items-center gap-2 px-3 py-2 bg-mythos-terminal-surface border border-mythos-terminal-border rounded
          text-sm font-mono transition-all duration-200 min-w-button
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

      {isOpen && !disabled && (
        <ChannelDropdownMenu channels={channels} selectedChannel={selectedChannel} onChannelSelect={onChannelSelect} />
      )}
    </div>
  );
}

function useChannelSelectorState(onChannelSelect: (channelId: string) => void, disabled: boolean) {
  const [isOpen, setIsOpen] = useState(false);

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
    e.stopPropagation();
    setIsOpen(false);
  };

  const handleBackdropKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'Escape') {
      e.stopPropagation();
      setIsOpen(false);
    }
  };

  useEffect(() => {
    if (!isOpen) return;

    const handleEscape = (e: KeyboardEvent) => {
      if (e.key === 'Escape') {
        setIsOpen(false);
      }
    };

    document.addEventListener('keydown', handleEscape);
    return () => {
      document.removeEventListener('keydown', handleEscape);
    };
  }, [isOpen]);

  return { isOpen, handleChannelSelect, toggleDropdown, handleBackdropClick, handleBackdropKeyDown };
}

export const ChannelSelector: React.FC<ChannelSelectorProps> = props => {
  const { channels, selectedChannel, onChannelSelect, disabled = false, className = '' } = props;
  const selectedChannelData = channels.find(channel => channel.id === selectedChannel);
  const { isOpen, handleChannelSelect, toggleDropdown, handleBackdropClick, handleBackdropKeyDown } =
    useChannelSelectorState(onChannelSelect, disabled);

  return (
    <ChannelSelectorUi
      ui={{
        channels,
        selectedChannel,
        disabled,
        className,
        isOpen,
        selectedChannelData,
        onChannelSelect: handleChannelSelect,
        onToggleDropdown: toggleDropdown,
        onBackdropClick: handleBackdropClick,
        onBackdropKeyDown: handleBackdropKeyDown,
      }}
    />
  );
};
