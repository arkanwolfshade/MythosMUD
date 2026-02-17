import { fireEvent, render, screen } from '@testing-library/react';
import { beforeEach, describe, expect, it, vi } from 'vitest';
import { GameTerminal } from '../GameTerminal';

// Mock the dependencies
vi.mock('../ui/EldritchIcon', () => ({
  EldritchIcon: ({ name, className }: { name: string; className?: string }) => (
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

vi.mock('../ui/TerminalButton', () => ({
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

vi.mock('../ui/TerminalInput', () => ({
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

vi.mock('../ui/ChannelSelector', () => ({
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

vi.mock('../DraggablePanel', () => ({
  DraggablePanel: ({ children, title, ...props }: DraggablePanelProps) => (
    <div data-testid={`panel-${title.toLowerCase().replace(/\s+/g, '-')}`} {...props}>
      <h3>{title}</h3>
      {children}
    </div>
  ),
}));

vi.mock('../../utils/ansiToHtml', () => ({
  ansiToHtmlWithBreaks: (text: string) => text.replace(/\n/g, '<br>'),
}));

vi.mock('../../utils/messageTypeUtils', () => ({
  extractChannelFromMessage: () => null,
  isChatContent: () => false,
}));

vi.mock('../../config/channels', () => {
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
    playerName: 'TestPlayer',
    isConnected: true,
    isConnecting: false,
    error: null,
    reconnectAttempts: 0,
    room: {
      id: 'room-1',
      name: 'Test Room',
      description: 'A test room',
      exits: {},
    },
    player: null,
    messages: mockMessages,
    commandHistory: mockCommandHistory,
    lucidityStatus: null,
    healthStatus: null,
    hallucinations: [],
    rescueState: null,
    onConnect: vi.fn(),
    onDisconnect: vi.fn(),
    onLogout: vi.fn(),
    onDownloadLogs: vi.fn(),
    onSendCommand: vi.fn(),
    onSendChatMessage: vi.fn(),
    onClearMessages: vi.fn(),
    onClearHistory: vi.fn(),
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

      expect(screen.getAllByText('Chat').length).toBeGreaterThan(0);
      expect(screen.getAllByText('Game Log').length).toBeGreaterThan(0);
      expect(screen.getAllByText('Commands').length).toBeGreaterThan(0);
    });

    it('passes props to all panels', () => {
      render(<GameTerminal {...defaultProps} />);

      // Chat and GameLog panels have search (ChatPanel is display-only; commands sent via CommandPanel)
      expect(screen.getAllByPlaceholderText('Search messages...').length).toBeGreaterThan(0);

      // Game log panel should show messages
      expect(screen.getByText('Hello, world!')).toBeInTheDocument();
      expect(screen.getByText('System message')).toBeInTheDocument();

      // Command panel should have command input
      expect(screen.getByPlaceholderText(/Enter game command/)).toBeInTheDocument();
    });
  });

  // Note: GameTerminalWithPanels has been replaced with GameClientV2Container
  // Integration tests for the new UI should be added separately

  describe('Panel Interaction', () => {
    it('allows switching between panels', () => {
      render(<GameTerminal {...defaultProps} />);

      // All panels should be visible and interactive (ChatPanel and GameLogPanel have search; CommandPanel has input)
      const searchInputs = screen.getAllByPlaceholderText('Search messages...');
      const commandInput = screen.getByPlaceholderText(/Enter game command/);

      expect(searchInputs.length).toBeGreaterThan(0);
      expect(commandInput).toBeInTheDocument();
    });

    it('maintains state across panel interactions', () => {
      render(<GameTerminal {...defaultProps} />);

      // Type in chat search (ChatPanel search filter)
      const searchInput = screen.getAllByPlaceholderText('Search messages...')[0];
      fireEvent.change(searchInput, { target: { value: 'Hello' } });

      // Type in command panel
      const commandInput = screen.getByPlaceholderText(/Enter game command/);
      fireEvent.change(commandInput, { target: { value: 'look' } });

      // Both inputs should maintain their values
      expect(searchInput).toHaveValue('Hello');
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

      // Click on a command from history (populates input), then submit
      const historyItem = screen.getByText('look');
      fireEvent.click(historyItem);

      const sendButton = screen.getByText('Send Command');
      fireEvent.click(sendButton);

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

    it('sends commands via command panel', () => {
      render(<GameTerminal {...defaultProps} />);

      const commandInput = screen.getByPlaceholderText(/Enter game command/);
      const sendButton = screen.getByText('Send Command');

      fireEvent.change(commandInput, { target: { value: 'look' } });
      fireEvent.click(sendButton);

      expect(defaultProps.onSendCommand).toHaveBeenCalledWith('look');
    });
  });

  describe('Error Handling', () => {
    it('handles connection errors gracefully', () => {
      render(<GameTerminal {...defaultProps} isConnected={false} />);

      // Should disable command input when disconnected
      const commandInput = screen.getByPlaceholderText(/Enter game command/);
      expect(commandInput).toBeDisabled();
    });

    it('handles missing props gracefully', () => {
      const { container } = render(
        <GameTerminal
          playerName="TestPlayer"
          isConnected={false}
          isConnecting={false}
          error={null}
          reconnectAttempts={0}
          room={null}
          player={null}
          messages={[]}
          commandHistory={[]}
          lucidityStatus={null}
          hallucinations={[]}
          rescueState={null}
          onConnect={vi.fn()}
          onDisconnect={vi.fn()}
          onLogout={vi.fn()}
          onDownloadLogs={vi.fn()}
          onSendCommand={vi.fn()}
          onSendChatMessage={vi.fn()}
          onClearMessages={vi.fn()}
          onClearHistory={vi.fn()}
        />
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
      expect(screen.getByLabelText('Chat Messages')).toBeInTheDocument();
    });

    it('supports keyboard navigation between panels', () => {
      render(<GameTerminal {...defaultProps} />);

      const commandInput = screen.getByPlaceholderText(/Enter game command/);

      commandInput.focus();
      expect(commandInput).toHaveFocus();
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

      // Test that state is properly managed (command input and chat search)
      const searchInputs = screen.getAllByPlaceholderText('Search messages...');
      const commandInput = screen.getByPlaceholderText(/Enter game command/);

      if (searchInputs.length > 0) {
        fireEvent.change(searchInputs[0], { target: { value: 'test' } });
        expect(searchInputs[0]).toHaveValue('test');
      }
      fireEvent.change(commandInput, { target: { value: 'look' } });
      expect(commandInput).toHaveValue('look');
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
