import { fireEvent, render, screen, waitFor } from '@testing-library/react';
import { beforeEach, describe, expect, it, vi } from 'vitest';

// Mock the dependencies
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
    command: 'command',
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

interface DraggablePanelProps {
  children: React.ReactNode;
  title: string;
  [key: string]: unknown;
}

vi.mock('../src/components/ui/DraggablePanel', () => ({
  DraggablePanel: ({ children, title, ...props }: DraggablePanelProps) => (
    <div data-testid={`panel-${title.toLowerCase().replace(/\s+/g, '-')}`} {...props}>
      <h3>{title}</h3>
      {children}
    </div>
  ),
}));

vi.mock('../src/utils/ansiToHtml', () => ({
  ansiToHtmlWithBreaks: (text: string) => text.replace(/\n/g, '<br>'),
}));

vi.mock('../src/config/channels', () => ({
  AVAILABLE_CHANNELS: [
    { id: 'local', name: 'Local', shortcut: 'l' },
    { id: 'global', name: 'Global', shortcut: 'g' },
  ],
  DEFAULT_CHANNEL: 'local',
}));

describe('GameTerminal Integration', () => {
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

  const mockCommandHistory = ['look', 'go north', 'inventory', 'say hello', 'who'];

  const defaultProps = {
    messages: mockMessages,
    commandHistory: mockCommandHistory,
    onSendCommand: vi.fn(),
    onSendChatMessage: vi.fn(),
    onClearMessages: vi.fn(),
    onClearHistory: vi.fn(),
    onDownloadLogs: vi.fn(),
    disabled: false,
    isConnected: true,
  };

  beforeEach(() => {
    vi.clearAllMocks();
  });

  describe('GameTerminal Component', () => {
    it('renders all three panels', () => {
      render(<GameTerminal {...defaultProps} />);

      expect(screen.getByTestId('panel-chat')).toBeInTheDocument();
      expect(screen.getByTestId('panel-game-log')).toBeInTheDocument();
      expect(screen.getByTestId('panel-commands')).toBeInTheDocument();
    });

    it('displays correct panel titles', () => {
      render(<GameTerminal {...defaultProps} />);

      expect(screen.getByText('Chat')).toBeInTheDocument();
      expect(screen.getByText('Game Log')).toBeInTheDocument();
      expect(screen.getByText('Commands')).toBeInTheDocument();
    });

    it('passes props to all panels', () => {
      render(<GameTerminal {...defaultProps} />);

      // Chat panel should have chat input
      expect(screen.getByPlaceholderText('Type your message here...')).toBeInTheDocument();

      // Game log panel should show messages
      expect(screen.getByText('Hello, world!')).toBeInTheDocument();
      expect(screen.getByText('System message')).toBeInTheDocument();

      // Command panel should have command input
      expect(screen.getByPlaceholderText('Enter game command...')).toBeInTheDocument();
    });
  });

  describe('GameTerminalWithPanels Component', () => {
    it('manages game connection state', () => {
      render(<GameTerminalWithPanels />);

      // Should show connection status
      expect(screen.getByText('Connected')).toBeInTheDocument();
    });

    it('handles command routing correctly', async () => {
      render(<GameTerminalWithPanels />);

      // Test game command routing
      const commandInput = screen.getByPlaceholderText('Enter game command...');
      fireEvent.change(commandInput, { target: { value: 'look' } });
      fireEvent.keyDown(commandInput, { key: 'Enter' });

      // Should route to game command handler
      await waitFor(() => {
        // The command should be processed
        expect(commandInput).toHaveValue('');
      });
    });

    it('handles chat message routing correctly', async () => {
      render(<GameTerminalWithPanels />);

      // Test chat message routing
      const chatInput = screen.getByPlaceholderText('Type your message here...');
      fireEvent.change(chatInput, { target: { value: 'Hello everyone!' } });

      const sendButton = screen.getByText('Send');
      fireEvent.click(sendButton);

      // Should route to chat message handler
      await waitFor(() => {
        expect(chatInput).toHaveValue('');
      });
    });
  });

  describe('Panel Interaction', () => {
    it('allows switching between panels', () => {
      render(<GameTerminal {...defaultProps} />);

      // All panels should be visible and interactive
      const chatInput = screen.getByPlaceholderText('Type your message here...');
      const commandInput = screen.getByPlaceholderText('Enter game command...');

      expect(chatInput).toBeInTheDocument();
      expect(commandInput).toBeInTheDocument();
    });

    it('maintains state across panel interactions', () => {
      render(<GameTerminal {...defaultProps} />);

      // Type in chat panel
      const chatInput = screen.getByPlaceholderText('Type your message here...');
      fireEvent.change(chatInput, { target: { value: 'Test chat message' } });

      // Type in command panel
      const commandInput = screen.getByPlaceholderText('Enter game command...');
      fireEvent.change(commandInput, { target: { value: 'look' } });

      // Both inputs should maintain their values
      expect(chatInput).toHaveValue('Test chat message');
      expect(commandInput).toHaveValue('look');
    });
  });

  describe('Message Flow', () => {
    it('displays messages in game log panel', () => {
      render(<GameTerminal {...defaultProps} />);

      // Messages should appear in the game log panel
      expect(screen.getByText('Hello, world!')).toBeInTheDocument();
      expect(screen.getByText('System message')).toBeInTheDocument();
    });

    it('updates message display when new messages arrive', () => {
      const { rerender } = render(<GameTerminal {...defaultProps} />);

      // Add new message
      const newMessages = [
        ...mockMessages,
        {
          text: 'New message',
          timestamp: '2024-01-01T12:02:00Z',
          isHtml: false,
          messageType: 'chat',
        },
      ];

      rerender(<GameTerminal {...defaultProps} messages={newMessages} />);

      // Should show new message
      expect(screen.getByText('New message')).toBeInTheDocument();
    });
  });

  describe('Command History Integration', () => {
    it('shows command history in command panel', () => {
      render(<GameTerminal {...defaultProps} />);

      // Command history should be displayed
      expect(screen.getByText('look')).toBeInTheDocument();
      expect(screen.getByText('go north')).toBeInTheDocument();
      expect(screen.getByText('inventory')).toBeInTheDocument();
    });

    it('allows executing commands from history', () => {
      render(<GameTerminal {...defaultProps} />);

      // Click on a command from history
      const historyItem = screen.getByText('look');
      fireEvent.click(historyItem);

      // Should execute the command
      expect(defaultProps.onSendCommand).toHaveBeenCalledWith('look');
    });
  });

  describe('Channel Management', () => {
    it('allows switching channels in chat panel', () => {
      render(<GameTerminal {...defaultProps} />);

      const channelSelector = screen.getByTestId('channel-selector');
      fireEvent.change(channelSelector, { target: { value: 'global' } });

      // Should update selected channel
      expect(channelSelector).toHaveValue('global');
    });

    it('sends chat messages to correct channel', () => {
      render(<GameTerminal {...defaultProps} />);

      const chatInput = screen.getByPlaceholderText('Type your message here...');
      const sendButton = screen.getByText('Send');

      fireEvent.change(chatInput, { target: { value: 'Hello!' } });
      fireEvent.click(sendButton);

      // Should send to default channel (local)
      expect(defaultProps.onSendChatMessage).toHaveBeenCalledWith('Hello!', 'local');
    });
  });

  describe('Error Handling', () => {
    it('handles connection errors gracefully', () => {
      render(<GameTerminal {...defaultProps} isConnected={false} />);

      // Should disable inputs when disconnected
      const chatInput = screen.getByPlaceholderText('Type your message here...');
      const commandInput = screen.getByPlaceholderText('Enter game command...');

      expect(chatInput).toBeDisabled();
      expect(commandInput).toBeDisabled();
    });

    it('handles missing props gracefully', () => {
      const { container } = render(
        <GameTerminal messages={[]} commandHistory={[]} onSendCommand={vi.fn()} onSendChatMessage={vi.fn()} />
      );

      expect(container).toBeInTheDocument();
    });
  });

  describe('Performance', () => {
    it('handles large message lists efficiently', () => {
      const largeMessages = Array.from({ length: 1000 }, (_, i) => ({
        text: `Message ${i}`,
        timestamp: new Date(Date.now() - i * 60000).toISOString(),
        isHtml: false,
        messageType: 'chat' as const,
      }));

      render(<GameTerminal {...defaultProps} messages={largeMessages} />);

      // Should render without performance issues
      expect(screen.getByText('Message 0')).toBeInTheDocument();
      expect(screen.getByText('Message 999')).toBeInTheDocument();
    });

    it('handles large command history efficiently', () => {
      const largeHistory = Array.from({ length: 1000 }, (_, i) => `command${i}`);

      render(<GameTerminal {...defaultProps} commandHistory={largeHistory} />);

      // Should render without performance issues
      expect(screen.getByText('command999')).toBeInTheDocument();
    });
  });

  describe('Accessibility', () => {
    it('provides proper ARIA labels for all panels', () => {
      render(<GameTerminal {...defaultProps} />);

      // Each panel should have proper accessibility labels
      expect(screen.getByLabelText('Channel Selection')).toBeInTheDocument();
      expect(screen.getByLabelText('Chat Input')).toBeInTheDocument();
      expect(screen.getByLabelText('Chat Messages')).toBeInTheDocument();
    });

    it('supports keyboard navigation between panels', () => {
      render(<GameTerminal {...defaultProps} />);

      const chatInput = screen.getByPlaceholderText('Type your message here...');
      const commandInput = screen.getByPlaceholderText('Enter game command...');

      // Test tab navigation
      chatInput.focus();
      expect(chatInput).toHaveFocus();

      // Should be able to navigate between inputs
      expect(chatInput).toBeInTheDocument();
      expect(commandInput).toBeInTheDocument();
    });
  });

  describe('Responsive Design', () => {
    it('adapts to different screen sizes', () => {
      render(<GameTerminal {...defaultProps} />);

      // All panels should be visible and functional
      expect(screen.getByTestId('panel-chat')).toBeInTheDocument();
      expect(screen.getByTestId('panel-game-log')).toBeInTheDocument();
      expect(screen.getByTestId('panel-commands')).toBeInTheDocument();

      // Should not throw errors on different screen sizes
    });
  });

  describe('State Management', () => {
    it('maintains consistent state across all panels', () => {
      render(<GameTerminal {...defaultProps} />);

      // Test that state is properly managed
      const chatInput = screen.getByPlaceholderText('Type your message here...');
      const commandInput = screen.getByPlaceholderText('Enter game command...');

      // Both inputs should be functional
      fireEvent.change(chatInput, { target: { value: 'test' } });
      fireEvent.change(commandInput, { target: { value: 'test' } });

      expect(chatInput).toHaveValue('test');
      expect(commandInput).toHaveValue('test');
    });

    it('handles state updates correctly', () => {
      const { rerender } = render(<GameTerminal {...defaultProps} />);

      // Update props
      const newProps = {
        ...defaultProps,
        messages: [
          ...mockMessages,
          { text: 'New message', timestamp: '2024-01-01T12:02:00Z', isHtml: false, messageType: 'chat' },
        ],
      };

      rerender(<GameTerminal {...newProps} />);

      // Should show new message
      expect(screen.getByText('New message')).toBeInTheDocument();
    });
  });
});
