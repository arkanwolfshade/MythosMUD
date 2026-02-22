import { fireEvent, render, screen } from '@testing-library/react';
import { beforeEach, describe, expect, it, vi } from 'vitest';
import type { ChatMessage } from '../../../stores/gameStore';
import { ChatPanel } from '../ChatPanel';

// Mock the dependencies - ChatPanel uses config/channels
vi.mock('../../../config/channels', () => {
  const baseChannels = [
    { id: 'local', name: 'Local', shortcut: 'l' },
    { id: 'global', name: 'Global', shortcut: 'g' },
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

vi.mock('../../ui/EldritchIcon', () => ({
  EldritchIcon: ({ name, className }: { name: string; className?: string }) => (
    <span data-testid={`icon-${name}`} className={className}>
      {name}
    </span>
  ),
  MythosIcons: {
    chat: 'chat',
    system: 'system',
    move: 'move',
    exit: 'exit',
    connection: 'connection',
    clock: 'clock',
    clear: 'clear',
    download: 'download',
    search: 'search',
  },
}));

interface TerminalButtonProps {
  children: React.ReactNode;
  onClick?: () => void;
  disabled?: boolean;
  [key: string]: unknown;
}

vi.mock('../../ui/TerminalButton', () => ({
  TerminalButton: ({ children, onClick, disabled, ...props }: TerminalButtonProps) => (
    <button onClick={onClick} disabled={disabled} {...props}>
      {children}
    </button>
  ),
}));

interface Channel {
  id: string;
  name: string;
}

interface ChannelSelectorProps {
  channels: Channel[];
  selectedChannel: string;
  onChannelSelect?: (channelId: string) => void;
  disabled?: boolean;
}

vi.mock('../../ui/ChannelSelector', () => ({
  ChannelSelector: ({ channels, selectedChannel, onChannelSelect, disabled }: ChannelSelectorProps) => (
    <select
      value={selectedChannel}
      onChange={e => onChannelSelect?.(e.target.value)}
      disabled={disabled}
      data-testid="channel-selector"
    >
      {channels.map((channel: Channel) => (
        <option key={channel.id} value={channel.id}>
          {channel.name}
        </option>
      ))}
    </select>
  ),
}));

vi.mock('../../../utils/ansiToHtml', () => ({
  ansiToHtmlWithBreaks: (text: string) => text.replace(/\n/g, '<br>'),
}));

vi.mock('../../../utils/messageTypeUtils', () => ({
  extractChannelFromMessage: () => null,
  isChatContent: () => false,
}));

describe('ChatPanel', () => {
  // ChatPanel filters out system/combat messages - use chat messages only for display tests
  const mockMessages: ChatMessage[] = [
    {
      text: 'Hello, world!',
      timestamp: '2024-01-01T12:00:00Z',
      isHtml: false,
      type: 'say',
      messageType: 'chat',
      channel: 'local',
      aliasChain: [{ original: 'Player1', expanded: 'Player1', alias_name: 'p1' }],
    },
    {
      text: 'Another chat message',
      timestamp: '2024-01-01T12:01:00Z',
      isHtml: false,
      type: 'say',
      messageType: 'chat',
      channel: 'local',
    },
  ];

  const defaultProps = {
    messages: mockMessages,
    onSendChatMessage: vi.fn(),
    onClearMessages: vi.fn(),
    onDownloadLogs: vi.fn(),
    disabled: false,
    isConnected: true,
  };

  beforeEach(() => {
    vi.clearAllMocks();
  });

  describe('Basic Rendering', () => {
    it('renders chat panel with header', () => {
      render(<ChatPanel {...defaultProps} />);

      expect(screen.getByTestId('icon-chat')).toBeInTheDocument();
      expect(screen.getByLabelText('Channel Selection')).toBeInTheDocument();
    });

    it('renders channel selector', () => {
      render(<ChatPanel {...defaultProps} />);

      expect(screen.getByTestId('channel-selector')).toBeInTheDocument();
    });

    it('displays messages when provided', () => {
      render(<ChatPanel {...defaultProps} />);

      expect(screen.getByText('Hello, world!')).toBeInTheDocument();
      expect(screen.getByText('Another chat message')).toBeInTheDocument();
      const chatMessages = screen.getAllByTestId('chat-message');
      expect(chatMessages.length).toBe(2);
    });

    it('shows empty state when no messages', () => {
      render(<ChatPanel {...defaultProps} messages={[]} />);

      expect(screen.getByText('No messages yet. Start chatting to see messages here.')).toBeInTheDocument();
    });
  });

  describe('Channel Selection', () => {
    it('changes selected channel', () => {
      const onChannelSelect = vi.fn();
      render(<ChatPanel {...defaultProps} onChannelSelect={onChannelSelect} />);

      const selector = screen.getByTestId('channel-selector');
      fireEvent.change(selector, { target: { value: 'local' } });

      expect(onChannelSelect).toHaveBeenCalledWith('local');
    });
  });

  describe('Search and Filter', () => {
    it('has search input', () => {
      render(<ChatPanel {...defaultProps} />);

      expect(screen.getByPlaceholderText('Search messages...')).toBeInTheDocument();
    });

    it('toggles chat history view', () => {
      render(<ChatPanel {...defaultProps} />);

      const historyButton = screen.getByText('Chat History');
      fireEvent.click(historyButton);
      expect(historyButton).toBeInTheDocument();
    });
  });

  describe('Accessibility', () => {
    it('has aria-label for chat messages', () => {
      render(<ChatPanel {...defaultProps} />);

      expect(screen.getByLabelText('Chat Messages')).toBeInTheDocument();
    });

    it('has Channel Selection region', () => {
      render(<ChatPanel {...defaultProps} />);

      expect(screen.getByLabelText('Channel Selection')).toBeInTheDocument();
    });
  });

  describe('Error Handling', () => {
    it('handles missing props gracefully', () => {
      const { container } = render(<ChatPanel messages={[]} onSendChatMessage={vi.fn()} />);
      expect(container).toBeInTheDocument();
    });

    it('handles malformed messages', () => {
      const malformed: ChatMessage[] = [
        {
          text: 'Valid',
          timestamp: '2024-01-01T12:00:00Z',
          isHtml: false,
          type: 'say',
          messageType: 'chat',
          channel: 'local',
        },
        { text: 'Invalid', messageType: 'chat' } as unknown as ChatMessage,
      ];
      render(<ChatPanel {...defaultProps} messages={malformed} />);
      expect(screen.getByText('Valid')).toBeInTheDocument();
    });
  });
});
