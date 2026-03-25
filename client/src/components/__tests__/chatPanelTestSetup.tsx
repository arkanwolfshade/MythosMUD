import React from 'react';
import { vi } from 'vitest';

vi.mock('../../config/channels', () => {
  const baseChannels = [
    { id: 'say', name: 'Say', shortcut: 'say' },
    { id: 'local', name: 'Local', shortcut: 'local' },
    { id: 'whisper', name: 'Whisper', shortcut: 'whisper' },
    { id: 'shout', name: 'Shout', shortcut: 'shout' },
  ];
  const allChannel = { id: 'all', name: 'All Messages' };

  return {
    AVAILABLE_CHANNELS: baseChannels,
    ALL_MESSAGES_CHANNEL: allChannel,
    CHAT_CHANNEL_OPTIONS: [allChannel, ...baseChannels],
    DEFAULT_CHANNEL: 'all',
    getChannelById: (channelId: string) =>
      channelId === allChannel.id ? allChannel : baseChannels.find(channel => channel.id === channelId),
  };
});

vi.mock('../../utils/ansiToHtml', () => ({
  ansiToHtmlWithBreaks: (text: string) => text.replace(/\n/g, '<br/>'),
}));

vi.mock('../../utils/messageTypeUtils', () => ({
  extractChannelFromMessage: (text: string) => {
    if (text.includes('[local]')) return 'local';
    if (text.includes('[whisper]')) return 'whisper';
    if (text.includes('[shout]')) return 'shout';
    return 'say';
  },
  isChatContent: (text: string) => {
    return text.includes('[local]') || text.includes('[whisper]') || text.includes('[shout]') || text.includes('says:');
  },
}));

vi.mock('../ui/ChannelSelector', () => ({
  ChannelSelector: ({
    selectedChannel,
    onChannelSelect,
    disabled,
    channels,
    className,
  }: {
    selectedChannel: string;
    onChannelSelect?: (channel: string) => void;
    disabled?: boolean;
    channels: Array<{ id: string; name: string }>;
    className?: string;
  }) => (
    <select
      data-testid="channel-selector"
      value={selectedChannel}
      onChange={e => onChannelSelect?.(e.target.value)}
      disabled={disabled}
      className={className}
      aria-label="Channel Selector"
    >
      {channels.map((channel: { id: string; name: string }) => (
        <option key={channel.id} value={channel.id}>
          {channel.name}
        </option>
      ))}
    </select>
  ),
}));

vi.mock('../ui/EldritchIcon', () => ({
  EldritchIcon: ({
    name,
    size,
    className,
    variant,
  }: {
    name: string;
    size?: string;
    className?: string;
    variant?: string;
  }) => (
    <span data-testid={`eldritch-icon-${name}`} className={className} style={{ fontSize: size }} data-variant={variant}>
      {name}
    </span>
  ),
  MythosIcons: {
    chat: 'chat-icon',
    clear: 'clear-icon',
    download: 'download-icon',
    clock: 'clock-icon',
    move: 'move-icon',
    exit: 'exit-icon',
    connection: 'connection-icon',
  },
}));

vi.mock('../ui/TerminalButton', () => ({
  TerminalButton: ({
    children,
    onClick,
    disabled,
    variant,
    size,
    className,
    'data-testid': dataTestId,
    ...rest
  }: {
    children: React.ReactNode;
    onClick?: () => void;
    disabled?: boolean;
    variant?: string;
    size?: string;
    className?: string;
    'data-testid'?: string;
    [key: string]: unknown;
  }) => (
    <button
      {...rest}
      data-testid={dataTestId ?? 'terminal-button'}
      onClick={onClick}
      disabled={disabled}
      className={`terminal-button ${variant || ''} ${size || ''} ${className || ''}`}
    >
      {children}
    </button>
  ),
}));

export const mockConsoleLog = vi.spyOn(console, 'log').mockImplementation(() => {});
