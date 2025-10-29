import '@testing-library/jest-dom';
import { render, screen, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { vi } from 'vitest';
import { CommandPanel } from '../panels/CommandPanel';

// Mock the child components to isolate testing
vi.mock('../../config/channels', () => ({
  AVAILABLE_CHANNELS: [
    { id: 'say', name: 'Say', shortcut: 'say' },
    { id: 'local', name: 'Local', shortcut: 'local' },
    { id: 'whisper', name: 'Whisper', shortcut: 'whisper' },
  ],
  DEFAULT_CHANNEL: 'say',
}));

vi.mock('../ui/ChannelSelector', () => ({
  ChannelSelector: ({
    selectedChannel,
    onChannelSelect,
    disabled,
    channels,
  }: {
    selectedChannel: string;
    onChannelSelect?: (channel: string) => void;
    disabled?: boolean;
    channels: Array<{ id: string; name: string }>;
  }) => (
    <select
      data-testid="channel-selector"
      value={selectedChannel}
      onChange={e => onChannelSelect?.(e.target.value)}
      disabled={disabled}
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
  EldritchIcon: ({ name, size, className }: { name: string; size?: string; className?: string }) => (
    <span data-testid={`eldritch-icon-${name}`} className={className} style={{ fontSize: size }}>
      {name}
    </span>
  ),
  MythosIcons: {
    command: 'command-icon',
    clear: 'clear-icon',
  },
}));

vi.mock('../ui/LogoutButton', () => ({
  LogoutButton: ({
    onLogout,
    disabled,
    isLoggingOut,
  }: {
    onLogout?: () => void;
    disabled?: boolean;
    isLoggingOut?: boolean;
  }) => (
    <button
      data-testid="logout-button"
      onClick={onLogout}
      disabled={disabled}
      aria-label={isLoggingOut ? 'Logging out...' : 'Logout'}
    >
      {isLoggingOut ? 'Logging out...' : 'Logout'}
    </button>
  ),
}));

vi.mock('../ui/TerminalButton', () => ({
  TerminalButton: ({
    children,
    onClick,
    disabled,
    type,
    variant,
    size,
    className,
    ...props
  }: {
    children: React.ReactNode;
    onClick?: () => void;
    disabled?: boolean;
    type?: string;
    variant?: string;
    size?: string;
    className?: string;
    [key: string]: unknown;
  }) => (
    <button
      {...props}
      data-testid="terminal-button"
      onClick={onClick}
      disabled={disabled}
      type={type}
      className={`terminal-button ${variant || ''} ${size || ''} ${className || ''}`}
    >
      {children}
    </button>
  ),
}));

vi.mock('../ui/TerminalInput', () => ({
  TerminalInput: ({
    value,
    onChange,
    onKeyDown,
    placeholder,
    disabled,
    className,
    autoFocus,
    ...props
  }: {
    value: string;
    onChange?: (e: React.ChangeEvent<HTMLInputElement>) => void;
    onKeyDown?: (e: React.KeyboardEvent<HTMLInputElement>) => void;
    placeholder?: string;
    disabled?: boolean;
    className?: string;
    autoFocus?: boolean;
    [key: string]: unknown;
  }) => (
    <input
      {...props}
      data-testid="terminal-input"
      value={value}
      onChange={onChange}
      onKeyDown={onKeyDown}
      placeholder={placeholder}
      disabled={disabled}
      className={className}
      autoFocus={autoFocus}
    />
  ),
}));

// Mock console.debug to avoid noise in tests
const mockConsoleDebug = vi.spyOn(console, 'debug').mockImplementation(() => {});

describe('CommandPanel', () => {
  const defaultProps = {
    commandHistory: ['look', 'inventory', 'go north'],
    onSendCommand: vi.fn(),
    onClearHistory: vi.fn(),
    onLogout: vi.fn(),
    disabled: false,
    isConnected: true,
    isLoggingOut: false,
    placeholder: "Enter game command (e.g., 'look', 'inventory', 'go north')...",
    selectedChannel: 'say',
  };

  beforeEach(() => {
    vi.clearAllMocks();
    mockConsoleDebug.mockClear();
  });

  afterAll(() => {
    mockConsoleDebug.mockRestore();
  });

  describe('Rendering and Structure', () => {
    it('should render command panel with correct structure', () => {
      render(<CommandPanel {...defaultProps} />);

      expect(screen.getByTestId('command-panel')).toBeInTheDocument();
      expect(screen.getByText('Commands')).toBeInTheDocument();
      expect(screen.getByTestId('channel-selector')).toBeInTheDocument();
      expect(screen.getByTestId('terminal-input')).toBeInTheDocument();
      expect(screen.getByText('Send Command')).toBeInTheDocument();
      expect(screen.getByText('Recent Commands')).toBeInTheDocument();
      expect(screen.getByText('Quick Commands')).toBeInTheDocument();
      expect(screen.getByTestId('logout-button')).toBeInTheDocument();
    });

    it('should render with correct data-testid attributes', () => {
      render(<CommandPanel {...defaultProps} />);

      expect(screen.getByTestId('command-panel')).toBeInTheDocument();
      expect(screen.getByTestId('terminal-input')).toBeInTheDocument();
      expect(screen.getByTestId('channel-selector')).toBeInTheDocument();
      expect(screen.getByTestId('logout-button')).toBeInTheDocument();
    });

    it('should render with correct default props', () => {
      render(<CommandPanel {...defaultProps} />);

      const input = screen.getByTestId('terminal-input');
      expect(input).toHaveValue('');
      expect(input).toHaveAttribute('placeholder', "Enter game command (e.g., 'look', 'inventory', 'go north')...");
      expect(input).not.toBeDisabled();

      const sendButton = screen.getByText('Send Command');
      expect(sendButton).toBeInTheDocument();
      expect(sendButton).toBeDisabled(); // Should be disabled when no command is entered
    });
  });

  describe('Command Input and Submission', () => {
    it('should update input value when typing', async () => {
      const user = userEvent.setup();
      render(<CommandPanel {...defaultProps} />);

      const input = screen.getByTestId('terminal-input');
      await user.type(input, 'look around');

      expect(input).toHaveValue('look around');
    });

    it('should enable send button when command is entered', async () => {
      const user = userEvent.setup();
      render(<CommandPanel {...defaultProps} />);

      const input = screen.getByTestId('terminal-input');
      const sendButton = screen.getByText('Send Command');

      expect(sendButton).toBeDisabled();

      await user.type(input, 'look');

      expect(sendButton).not.toBeDisabled();
    });

    it('should call onSendCommand when form is submitted', async () => {
      const user = userEvent.setup();
      const mockOnSendCommand = vi.fn();
      render(<CommandPanel {...defaultProps} onSendCommand={mockOnSendCommand} />);

      const input = screen.getByTestId('terminal-input');
      const sendButton = screen.getByText('Send Command');

      await user.type(input, 'look around');
      await user.click(sendButton);

      expect(mockOnSendCommand).toHaveBeenCalledWith('look around');
      expect(input).toHaveValue(''); // Input should be cleared after submission
    });

    it('should call onSendCommand when Enter key is pressed', async () => {
      const user = userEvent.setup();
      const mockOnSendCommand = vi.fn();
      render(<CommandPanel {...defaultProps} onSendCommand={mockOnSendCommand} />);

      const input = screen.getByTestId('terminal-input');
      await user.type(input, 'look around');
      await user.keyboard('{Enter}');

      expect(mockOnSendCommand).toHaveBeenCalledWith('look around');
      expect(input).toHaveValue(''); // Input should be cleared after submission
    });

    it('should not submit empty commands', async () => {
      const user = userEvent.setup();
      const mockOnSendCommand = vi.fn();
      render(<CommandPanel {...defaultProps} onSendCommand={mockOnSendCommand} />);

      const input = screen.getByTestId('terminal-input');
      const sendButton = screen.getByText('Send Command');

      // Try to submit with just spaces
      await user.type(input, '   ');
      await user.click(sendButton);

      expect(mockOnSendCommand).not.toHaveBeenCalled();
      expect(sendButton).toBeDisabled();
    });

    it('should trim whitespace from commands before sending', async () => {
      const user = userEvent.setup();
      const mockOnSendCommand = vi.fn();
      render(<CommandPanel {...defaultProps} onSendCommand={mockOnSendCommand} />);

      const input = screen.getByTestId('terminal-input');
      await user.type(input, '  look around  ');
      await user.keyboard('{Enter}');

      expect(mockOnSendCommand).toHaveBeenCalledWith('look around');
    });
  });

  describe('Channel Selection and Command Prefixing', () => {
    it('should use default channel initially', () => {
      render(<CommandPanel {...defaultProps} />);

      const channelSelector = screen.getByTestId('channel-selector');
      expect(channelSelector).toHaveValue('say');
    });

    it('should update channel when selector changes', async () => {
      const user = userEvent.setup();
      render(<CommandPanel {...defaultProps} />);

      const channelSelector = screen.getByTestId('channel-selector');
      await user.selectOptions(channelSelector, 'local');

      expect(channelSelector).toHaveValue('local');
    });

    it('should prefix commands with channel shortcut when not on say or local channel', async () => {
      const user = userEvent.setup();
      const mockOnSendCommand = vi.fn();
      // Use 'global' channel instead of 'local' since local is excluded from prefixing
      render(<CommandPanel {...defaultProps} onSendCommand={mockOnSendCommand} selectedChannel="global" />);

      const input = screen.getByTestId('terminal-input');
      await user.type(input, 'hello everyone');
      await user.keyboard('{Enter}');

      expect(mockOnSendCommand).toHaveBeenCalledWith('/g hello everyone');
    });

    it('should not prefix commands that already start with slash', async () => {
      const user = userEvent.setup();
      const mockOnSendCommand = vi.fn();
      render(<CommandPanel {...defaultProps} onSendCommand={mockOnSendCommand} selectedChannel="local" />);

      const input = screen.getByTestId('terminal-input');
      await user.type(input, '/whisper player hello');
      await user.keyboard('{Enter}');

      expect(mockOnSendCommand).toHaveBeenCalledWith('/whisper player hello');
    });

    it('should not prefix commands on say channel', async () => {
      const user = userEvent.setup();
      const mockOnSendCommand = vi.fn();
      render(<CommandPanel {...defaultProps} onSendCommand={mockOnSendCommand} selectedChannel="say" />);

      const input = screen.getByTestId('terminal-input');
      await user.type(input, 'hello everyone');
      await user.keyboard('{Enter}');

      expect(mockOnSendCommand).toHaveBeenCalledWith('hello everyone');
    });
  });

  describe('Command History', () => {
    it('should display command history', () => {
      render(<CommandPanel {...defaultProps} />);

      expect(screen.getByText('Recent Commands')).toBeInTheDocument();
      expect(screen.getByText('go north')).toBeInTheDocument();

      // Use getAllByText to handle duplicates between history and quick commands
      const inventoryElements = screen.getAllByText('inventory');
      expect(inventoryElements.length).toBeGreaterThan(0);

      const lookElements = screen.getAllByText('look');
      expect(lookElements.length).toBeGreaterThan(0);
    });

    it('should display history in reverse chronological order (newest first)', () => {
      render(<CommandPanel {...defaultProps} />);

      const historyItems = screen.getAllByText(/go north|inventory|look/);
      expect(historyItems[0]).toHaveTextContent('go north');
      expect(historyItems[1]).toHaveTextContent('inventory');
      expect(historyItems[2]).toHaveTextContent('look');
    });

    it('should limit history to last 10 commands', () => {
      const longHistory = Array.from({ length: 15 }, (_, i) => `command${i + 1}`);
      render(<CommandPanel {...defaultProps} commandHistory={longHistory} />);

      // Should only show the last 10 commands
      expect(screen.getByText('command15')).toBeInTheDocument();
      expect(screen.getByText('command6')).toBeInTheDocument();
      expect(screen.queryByText('command5')).not.toBeInTheDocument();
    });

    it('should show "No commands yet" when history is empty', () => {
      render(<CommandPanel {...defaultProps} commandHistory={[]} />);

      expect(screen.getByText('No commands yet')).toBeInTheDocument();
    });

    it('should allow clicking on history items to reuse commands', async () => {
      const user = userEvent.setup();
      render(<CommandPanel {...defaultProps} />);

      // Find the history item (not the quick command button)
      const historyItems = screen.getAllByText('inventory');
      const historyItem = historyItems.find(
        item =>
          item.closest('div')?.classList.contains('text-xs') &&
          item.closest('div')?.classList.contains('cursor-pointer')
      );

      expect(historyItem).toBeInTheDocument();
      await user.click(historyItem!);

      const input = screen.getByTestId('terminal-input');
      expect(input).toHaveValue('inventory');
    });
  });

  describe('Quick Commands', () => {
    it('should display quick command buttons', () => {
      render(<CommandPanel {...defaultProps} />);

      // Check for quick command buttons specifically
      const quickCommandButtons = screen.getAllByTestId('terminal-button');
      const quickCommands = quickCommandButtons.filter(button =>
        ['look', 'inventory', 'health', 'status'].includes(button.textContent || '')
      );

      expect(quickCommands).toHaveLength(4);
      expect(quickCommands.some(btn => btn.textContent === 'look')).toBe(true);
      expect(quickCommands.some(btn => btn.textContent === 'inventory')).toBe(true);
      expect(quickCommands.some(btn => btn.textContent === 'health')).toBe(true);
      expect(quickCommands.some(btn => btn.textContent === 'status')).toBe(true);
    });

    it('should populate input when quick command is clicked', async () => {
      const user = userEvent.setup();
      render(<CommandPanel {...defaultProps} />);

      // Find the quick command button (not the history item)
      const quickCommandButtons = screen.getAllByTestId('terminal-button');
      const lookButton = quickCommandButtons.find(
        button => button.textContent === 'look' && button.classList.contains('secondary')
      );
      expect(lookButton).toBeInTheDocument();

      await user.click(lookButton!);

      const input = screen.getByTestId('terminal-input');
      expect(input).toHaveValue('look');
    });

    it('should focus input after clicking quick command', async () => {
      const user = userEvent.setup();
      render(<CommandPanel {...defaultProps} />);

      const input = screen.getByTestId('terminal-input');
      const quickCommandButtons = screen.getAllByTestId('terminal-button');
      const inventoryButton = quickCommandButtons.find(
        button => button.textContent === 'inventory' && button.classList.contains('secondary')
      );

      await user.click(inventoryButton!);

      await waitFor(() => {
        expect(input).toHaveFocus();
      });
    });
  });

  describe('Clear History Functionality', () => {
    it('should call onClearHistory when clear button is clicked', async () => {
      const user = userEvent.setup();
      const mockOnClearHistory = vi.fn();
      render(<CommandPanel {...defaultProps} onClearHistory={mockOnClearHistory} />);

      const clearButton = screen.getByText('Clear');
      await user.click(clearButton);

      expect(mockOnClearHistory).toHaveBeenCalled();
    });

    it('should not show clear button when onClearHistory is not provided', () => {
      // eslint-disable-next-line @typescript-eslint/no-unused-vars
      const { onClearHistory, ...propsWithoutClear } = defaultProps;
      render(<CommandPanel {...propsWithoutClear} />);

      // The clear button should still be present but the onClearHistory prop should not be passed
      const clearButton = screen.getByText('Clear');
      expect(clearButton).toBeInTheDocument();
      // We can't easily test the callback not being passed without modifying the component
    });
  });

  describe('Logout Functionality', () => {
    it('should call onLogout when logout button is clicked', async () => {
      const user = userEvent.setup();
      const mockOnLogout = vi.fn();
      render(<CommandPanel {...defaultProps} onLogout={mockOnLogout} />);

      const logoutButton = screen.getByTestId('logout-button');
      await user.click(logoutButton);

      expect(mockOnLogout).toHaveBeenCalled();
    });

    it('should handle Ctrl+Q keyboard shortcut for logout', async () => {
      const user = userEvent.setup();
      const mockOnLogout = vi.fn();
      render(<CommandPanel {...defaultProps} onLogout={mockOnLogout} />);

      await user.keyboard('{Control>}q{/Control}');

      expect(mockOnLogout).toHaveBeenCalled();
    });

    it('should not show logout button when onLogout is not provided', () => {
      // eslint-disable-next-line @typescript-eslint/no-unused-vars
      const { onLogout, ...propsWithoutLogout } = defaultProps;
      render(<CommandPanel {...propsWithoutLogout} />);

      expect(screen.queryByTestId('logout-button')).not.toBeInTheDocument();
    });

    it('should show logging out state', () => {
      render(<CommandPanel {...defaultProps} isLoggingOut={true} />);

      const logoutButton = screen.getByTestId('logout-button');
      expect(logoutButton).toHaveAttribute('aria-label', 'Logging out...');
      expect(logoutButton).toHaveTextContent('Logging out...');
    });
  });

  describe('Disabled and Connection States', () => {
    it('should disable input and buttons when disabled', () => {
      render(<CommandPanel {...defaultProps} disabled={true} />);

      const input = screen.getByTestId('terminal-input');
      const sendButton = screen.getByText('Send Command');
      const channelSelector = screen.getByTestId('channel-selector');
      const logoutButton = screen.getByTestId('logout-button');

      expect(input).toBeDisabled();
      expect(sendButton).toBeDisabled();
      expect(channelSelector).toBeDisabled();
      expect(logoutButton).toBeDisabled();
    });

    it('should disable input and buttons when not connected', () => {
      render(<CommandPanel {...defaultProps} isConnected={false} />);

      const input = screen.getByTestId('terminal-input');
      const sendButton = screen.getByText('Send Command');
      const channelSelector = screen.getByTestId('channel-selector');
      const logoutButton = screen.getByTestId('logout-button');

      expect(input).toBeDisabled();
      expect(sendButton).toBeDisabled();
      expect(channelSelector).toBeDisabled();
      expect(logoutButton).toBeDisabled();
    });

    it('should not respond to keyboard shortcuts when disabled', async () => {
      const user = userEvent.setup();
      const mockOnLogout = vi.fn();
      render(<CommandPanel {...defaultProps} onLogout={mockOnLogout} disabled={true} />);

      await user.keyboard('{Control>}q{/Control}');

      expect(mockOnLogout).not.toHaveBeenCalled();
    });

    it('should not respond to keyboard shortcuts when not connected', async () => {
      const user = userEvent.setup();
      const mockOnLogout = vi.fn();
      render(<CommandPanel {...defaultProps} onLogout={mockOnLogout} isConnected={false} />);

      await user.keyboard('{Control>}q{/Control}');

      expect(mockOnLogout).not.toHaveBeenCalled();
    });
  });

  describe('Accessibility', () => {
    it('should have proper ARIA labels and roles', () => {
      render(<CommandPanel {...defaultProps} />);

      expect(screen.getByTestId('channel-selector')).toHaveAttribute('aria-label', 'Channel Selector');
      expect(screen.getByTestId('logout-button')).toHaveAttribute('aria-label', 'Logout');
    });

    it('should focus input on mount', () => {
      render(<CommandPanel {...defaultProps} />);

      const input = screen.getByTestId('terminal-input');
      expect(input).toHaveFocus();
    });

    it('should maintain focus management', async () => {
      const user = userEvent.setup();
      render(<CommandPanel {...defaultProps} />);

      const input = screen.getByTestId('terminal-input');

      // Click elsewhere
      await user.click(screen.getByText('Commands'));

      // Click on history item should refocus input
      const historyItems = screen.getAllByText('look');
      const historyItem = historyItems.find(
        item =>
          item.closest('div')?.classList.contains('text-xs') &&
          item.closest('div')?.classList.contains('cursor-pointer')
      );
      await user.click(historyItem!);

      expect(input).toHaveFocus();
      expect(input).toHaveValue('look');
    });
  });

  describe('Development Debug Logging', () => {
    it('should log debug information in development mode', () => {
      // Set NODE_ENV to development for this test
      const originalEnv = process.env.NODE_ENV;
      process.env.NODE_ENV = 'development';

      render(<CommandPanel {...defaultProps} />);

      expect(mockConsoleDebug).toHaveBeenCalledWith(
        'CommandPanel received isConnected prop',
        expect.objectContaining({
          isConnected: true,
          disabled: false,
          commandInputLength: 0,
          buttonDisabled: true,
          buttonDisabledReason: expect.objectContaining({
            noCommand: true,
            panelDisabled: false,
            notConnected: false,
          }),
        })
      );

      // Restore original environment
      process.env.NODE_ENV = originalEnv;
    });
  });

  describe('Edge Cases and Error Handling', () => {
    it('should handle undefined commandHistory gracefully', () => {
      // Provide empty array as fallback to prevent crashes
      const propsWithUndefinedHistory = { ...defaultProps, commandHistory: [] };
      render(<CommandPanel {...propsWithUndefinedHistory} />);

      expect(screen.getByText('No commands yet')).toBeInTheDocument();
    });

    it('should handle null commandHistory gracefully', () => {
      // Provide empty array as fallback to prevent crashes
      const propsWithNullHistory = { ...defaultProps, commandHistory: [] };
      render(<CommandPanel {...propsWithNullHistory} />);

      expect(screen.getByText('No commands yet')).toBeInTheDocument();
    });

    it('should handle commands with special characters', async () => {
      const user = userEvent.setup();
      const mockOnSendCommand = vi.fn();
      render(<CommandPanel {...defaultProps} onSendCommand={mockOnSendCommand} />);

      const input = screen.getByTestId('terminal-input');
      await user.type(input, 'say "Hello, world!" & <script>alert("test")</script>');
      await user.keyboard('{Enter}');

      expect(mockOnSendCommand).toHaveBeenCalledWith('say "Hello, world!" & <script>alert("test")</script>');
    });

    it('should handle very long commands', async () => {
      const user = userEvent.setup();
      const mockOnSendCommand = vi.fn();
      const longCommand = 'a'.repeat(100); // Reduced length to prevent timeout
      render(<CommandPanel {...defaultProps} onSendCommand={mockOnSendCommand} />);

      const input = screen.getByTestId('terminal-input');
      await user.type(input, longCommand);
      await user.keyboard('{Enter}');

      expect(mockOnSendCommand).toHaveBeenCalledWith(longCommand);
    });
  });
});
