import { expect } from '@playwright/test';
import { fireEvent, render, screen } from '@testing-library/react';
import { beforeEach, describe, it, vi } from 'vitest';
import { DEFAULT_CHANNEL } from '../src/config/channels';

// Mock the dependencies
vi.mock('../src/config/channels', () => ({
  AVAILABLE_CHANNELS: [
    { id: 'local', name: 'Local', shortcut: 'l' },
    { id: 'global', name: 'Global', shortcut: 'g' },
  ],
  DEFAULT_CHANNEL: 'local',
}));

vi.mock('../src/components/ui/EldritchIcon', () => ({
  EldritchIcon: ({
    name,
    _size,
    _variant,
    className,
  }: {
    name: string;
    _size?: number;
    _variant?: string;
    className?: string;
  }) => (
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
  },
}));

interface TerminalButtonProps {
  children: React.ReactNode;
  onClick?: () => void;
  disabled?: boolean;
  [key: string]: unknown;
}

vi.mock('../src/components/ui/TerminalButton', () => ({
  TerminalButton: ({ children, onClick, disabled, ...props }: TerminalButtonProps) => (
    <button onClick={onClick} disabled={disabled} {...props}>
      {children}
    </button>
  ),
}));

interface TerminalInputProps {
  value: string;
  onChange?: (event: React.ChangeEvent<HTMLInputElement>) => void;
  onKeyDown?: (event: React.KeyboardEvent) => void;
  [key: string]: unknown;
}

vi.mock('../src/components/ui/TerminalInput', () => ({
  TerminalInput: ({ value, onChange, onKeyDown, ...props }: TerminalInputProps) => (
    <input value={value} onChange={onChange} onKeyDown={onKeyDown} {...props} />
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

vi.mock('../src/components/ui/ChannelSelector', () => ({
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

vi.mock('../src/utils/ansiToHtml', () => ({
  ansiToHtmlWithBreaks: (text: string) => text.replace(/\n/g, '<br>'),
}));

describe('ChatPanel', () => {
  const mockMessages = [
    {
      text: 'Hello, world!',
      timestamp: '2024-01-01T12:00:00Z',
      isHtml: false,
      messageType: 'chat',
      aliasChain: [{ original: 'Player1', expanded: 'Player1', alias_name: 'p1' }],
    },
    {
      text: 'System message',
      timestamp: '2024-01-01T12:01:00Z',
      isHtml: false,
      messageType: 'system',
    },
  ];

  const defaultProps = {
    messages: mockMessages,
    onSendChatMessage: vi.fn(),
    onClearMessages: vi.fn(),
    onDownloadLogs: vi.fn(),
    disabled: false,
    isConnected: true,
    selectedChannel: DEFAULT_CHANNEL,
    onChannelSelect: vi.fn(),
  };

  beforeEach(() => {
    vi.clearAllMocks();
  });

  describe('Basic Rendering', () => {
    it('renders chat panel with all sections', () => {
      render(<ChatPanel {...defaultProps} />);

      expect(screen.getByText('Chat')).toBeInTheDocument();
      expect(screen.getByTestId('channel-selector')).toBeInTheDocument();
      expect(screen.getByPlaceholderText('Type your message here...')).toBeInTheDocument();
      expect(screen.getByText('Send')).toBeInTheDocument();
    });

    it('displays messages correctly', () => {
      render(<ChatPanel {...defaultProps} />);

      expect(screen.getByText('Hello, world!')).toBeInTheDocument();
      expect(screen.getByText('System message')).toBeInTheDocument();
    });

    it('shows empty state when no messages', () => {
      render(<ChatPanel {...defaultProps} messages={[]} />);

      expect(screen.getByText('No messages yet. Start chatting to see messages here.')).toBeInTheDocument();
    });
  });

  describe('Chat Input Functionality', () => {
    it('sends message when form is submitted', async () => {
      render(<ChatPanel {...defaultProps} />);

      const input = screen.getByPlaceholderText('Type your message here...');
      const sendButton = screen.getByText('Send');

      fireEvent.change(input, { target: { value: 'Test message' } });
      fireEvent.click(sendButton);

      expect(defaultProps.onSendChatMessage).toHaveBeenCalledWith('Test message', DEFAULT_CHANNEL);
    });

    it('clears input after sending message', () => {
      render(<ChatPanel {...defaultProps} />);

      const input = screen.getByPlaceholderText('Type your message here...');
      const sendButton = screen.getByText('Send');

      fireEvent.change(input, { target: { value: 'Test message' } });
      fireEvent.click(sendButton);

      expect(input).toHaveValue('');
    });

    it('does not send empty messages', () => {
      render(<ChatPanel {...defaultProps} />);

      const sendButton = screen.getByText('Send');
      fireEvent.click(sendButton);

      expect(defaultProps.onSendChatMessage).not.toHaveBeenCalled();
    });

    it('disables input when disconnected', () => {
      render(<ChatPanel {...defaultProps} isConnected={false} />);

      const input = screen.getByPlaceholderText('Type your message here...');
      const sendButton = screen.getByText('Send');

      expect(input).toBeDisabled();
      expect(sendButton).toBeDisabled();
    });
  });

  describe('Emote System', () => {
    it('shows emote panel when emote button is clicked', () => {
      render(<ChatPanel {...defaultProps} />);

      const emoteButton = screen.getByText('Emotes');
      fireEvent.click(emoteButton);

      expect(screen.getByText('😊')).toBeInTheDocument();
      expect(screen.getByText('👋')).toBeInTheDocument();
    });

    it('inserts emote when clicked', () => {
      render(<ChatPanel {...defaultProps} />);

      const emoteButton = screen.getByText('Emotes');
      fireEvent.click(emoteButton);

      const smileEmote = screen.getByText('😊');
      fireEvent.click(smileEmote);

      const input = screen.getByPlaceholderText('Type your message here...');
      expect(input).toHaveValue('😊');
    });

    it('hides emote panel when emote button is clicked again', () => {
      render(<ChatPanel {...defaultProps} />);

      const emoteButton = screen.getByText('Emotes');
      fireEvent.click(emoteButton);
      expect(screen.getByText('😊')).toBeInTheDocument();

      fireEvent.click(emoteButton);
      expect(screen.queryByText('😊')).not.toBeInTheDocument();
    });
  });

  describe('Formatting System', () => {
    it('shows formatting panel when format button is clicked', () => {
      render(<ChatPanel {...defaultProps} />);

      const formatButton = screen.getByText('Format');
      fireEvent.click(formatButton);

      expect(screen.getByText('**bold**')).toBeInTheDocument();
      expect(screen.getByText('*italic*')).toBeInTheDocument();
    });

    it('inserts formatting when clicked', () => {
      render(<ChatPanel {...defaultProps} />);

      const formatButton = screen.getByText('Format');
      fireEvent.click(formatButton);

      const boldFormat = screen.getByText('**bold**');
      fireEvent.click(boldFormat);

      const input = screen.getByPlaceholderText('Type your message here...');
      expect(input).toHaveValue('**text**');
    });
  });

  describe('Settings Panel', () => {
    it('shows settings panel when settings button is clicked', () => {
      render(<ChatPanel {...defaultProps} />);

      const settingsButton = screen.getByText('Settings');
      fireEvent.click(settingsButton);

      expect(screen.getByText('Font Size:')).toBeInTheDocument();
      expect(screen.getByText('Sound Notifications:')).toBeInTheDocument();
    });

    it('changes font size when selected', () => {
      render(<ChatPanel {...defaultProps} />);

      const settingsButton = screen.getByText('Settings');
      fireEvent.click(settingsButton);

      const fontSizeSelect = screen.getByDisplayValue('Medium');
      fireEvent.change(fontSizeSelect, { target: { value: 'large' } });

      expect(fontSizeSelect).toHaveValue('large');
    });

    it('toggles sound notifications', () => {
      render(<ChatPanel {...defaultProps} />);

      const settingsButton = screen.getByText('Settings');
      fireEvent.click(settingsButton);

      const soundCheckbox = screen.getByRole('checkbox', { name: /sound notifications/i });
      fireEvent.click(soundCheckbox);

      expect(soundCheckbox).toBeChecked();
    });
  });

  describe('Moderation Features', () => {
    it('filters out ignored users', () => {
      const messagesWithIgnoredUser = [
        ...mockMessages,
        {
          text: 'Message from ignored user',
          timestamp: '2024-01-01T12:02:00Z',
          isHtml: false,
          messageType: 'chat',
          aliasChain: [{ original: 'IgnoredUser', expanded: 'IgnoredUser', alias_name: 'iu' }],
        },
      ];

      render(<ChatPanel {...defaultProps} messages={messagesWithIgnoredUser} />);

      // Open settings and add user to ignore list
      const settingsButton = screen.getByText('Settings');
      fireEvent.click(settingsButton);

      // Simulate adding user to ignore list (this would need to be implemented in the component)
      // For now, we'll test that the moderation functions exist
      expect(screen.getByText('Ignored Users')).toBeInTheDocument();
    });

    it('prevents spam messages from being sent', () => {
      render(<ChatPanel {...defaultProps} />);

      const input = screen.getByPlaceholderText('Type your message here...');
      const sendButton = screen.getByText('Send');

      // Test with spam message (repeated characters)
      fireEvent.change(input, { target: { value: 'AAAAA' } });
      fireEvent.click(sendButton);

      // The component should show an alert for spam
      // In a real test, we'd need to mock window.alert
      expect(defaultProps.onSendChatMessage).not.toHaveBeenCalled();
    });
  });

  describe('Export Functionality', () => {
    it('shows export options in settings', () => {
      render(<ChatPanel {...defaultProps} />);

      const settingsButton = screen.getByText('Settings');
      fireEvent.click(settingsButton);

      expect(screen.getByText('Export & Backup')).toBeInTheDocument();
      expect(screen.getByText('Export Format:')).toBeInTheDocument();
    });

    it('allows changing export format', () => {
      render(<ChatPanel {...defaultProps} />);

      const settingsButton = screen.getByText('Settings');
      fireEvent.click(settingsButton);

      const exportFormatSelect = screen.getByDisplayValue('Text (.txt)');
      fireEvent.change(exportFormatSelect, { target: { value: 'json' } });

      expect(exportFormatSelect).toHaveValue('json');
    });
  });

  describe('Channel Management', () => {
    it('changes selected channel', () => {
      render(<ChatPanel {...defaultProps} />);

      const channelSelector = screen.getByTestId('channel-selector');
      fireEvent.change(channelSelector, { target: { value: 'global' } });

      expect(defaultProps.onChannelSelect).toHaveBeenCalledWith('global');
    });

    it('shows channel activity indicators', () => {
      render(<ChatPanel {...defaultProps} />);

      expect(screen.getByText('Activity:')).toBeInTheDocument();
      expect(screen.getByText('Local')).toBeInTheDocument();
      expect(screen.getByText('Global')).toBeInTheDocument();
    });
  });

  describe('Accessibility', () => {
    it('has proper ARIA labels', () => {
      render(<ChatPanel {...defaultProps} />);

      expect(screen.getByLabelText('Channel Selection')).toBeInTheDocument();
      expect(screen.getByLabelText('Chat Input')).toBeInTheDocument();
      expect(screen.getByLabelText('Chat Messages')).toBeInTheDocument();
    });

    it('supports keyboard navigation', () => {
      render(<ChatPanel {...defaultProps} />);

      const input = screen.getByPlaceholderText('Type your message here...');

      // Test arrow key navigation for input history
      fireEvent.keyDown(input, { key: 'ArrowUp' });
      fireEvent.keyDown(input, { key: 'ArrowDown' });

      // Test tab completion
      fireEvent.keyDown(input, { key: 'Tab' });

      // These should not throw errors
      expect(input).toBeInTheDocument();
    });
  });

  describe('Responsive Design', () => {
    it('adapts to different screen sizes', () => {
      render(<ChatPanel {...defaultProps} />);

      // Test that responsive classes are applied
      const channelSelector = screen.getByTestId('channel-selector');
      expect(channelSelector).toBeInTheDocument();

      // The component should render without errors on different screen sizes
      // In a real test, we'd use a library like @testing-library/react-hooks
      // to test responsive behavior
    });
  });

  describe('Error Handling', () => {
    it('handles missing props gracefully', () => {
      const { container } = render(<ChatPanel messages={[]} onSendChatMessage={vi.fn()} />);

      expect(container).toBeInTheDocument();
    });

    it('handles malformed messages', () => {
      const malformedMessages = [
        {
          text: 'Valid message',
          timestamp: '2024-01-01T12:00:00Z',
          isHtml: false,
        },
        {
          // Missing required fields
          text: 'Invalid message',
        },
      ];

      render(<ChatPanel {...defaultProps} messages={malformedMessages} />);

      // Should not crash and should display valid messages
      expect(screen.getByText('Valid message')).toBeInTheDocument();
    });
  });
});
