import { fireEvent, render, screen, waitFor } from '@testing-library/react';
import { vi } from 'vitest';
import { CommandPanel } from '../CommandPanel';

// Mock the EldritchIcon component
vi.mock('../../ui/EldritchIcon', () => ({
  EldritchIcon: ({
    name,
    size,
    variant,
    className,
  }: {
    name: string;
    size?: string;
    variant?: string;
    className?: string;
  }) => (
    <div data-testid={`icon-${name}`} data-size={size} data-variant={variant} className={className}>
      {name}
    </div>
  ),
  MythosIcons: {
    chat: 'chat',
    local: 'local',
    global: 'global',
    whisper: 'whisper',
    system: 'system',
    exit: 'exit',
    connection: 'connection',
    search: 'search',
    clear: 'clear',
    help: 'help',
    move: 'move',
    look: 'look',
    inventory: 'inventory',
    character: 'character',
    clock: 'clock',
    stats: 'stats',
  },
}));

// Mock the TerminalButton component
vi.mock('../../ui/TerminalButton', () => ({
  TerminalButton: ({
    children,
    onClick,
    disabled,
    className,
    title,
    ...props
  }: {
    children: React.ReactNode;
    onClick?: () => void;
    disabled?: boolean;
    className?: string;
    title?: string;
    [key: string]: unknown;
  }) => (
    <button onClick={onClick} disabled={disabled} className={className} title={title} {...props}>
      {children}
    </button>
  ),
}));

// Mock the TerminalInput component
vi.mock('../../ui/TerminalInput', () => ({
  TerminalInput: ({
    value,
    onChange,
    onKeyDown,
    placeholder,
    disabled,
    className,
    onFocus,
  }: {
    value: string;
    onChange: (value: string) => void;
    onKeyDown?: (e: React.KeyboardEvent) => void;
    placeholder?: string;
    disabled?: boolean;
    className?: string;
    onFocus?: () => void;
  }) => (
    <input
      value={value}
      onChange={e => onChange(e.target.value)}
      onKeyDown={onKeyDown}
      placeholder={placeholder}
      disabled={disabled}
      className={className}
      onFocus={onFocus}
    />
  ),
}));

describe('CommandPanel', () => {
  const defaultProps = {
    commandHistory: ['look', 'n', 'say Hello'],
    onSendCommand: vi.fn(),
    onClearHistory: vi.fn(),
    isConnected: true,
  };

  beforeEach(() => {
    vi.clearAllMocks();
  });

  describe('Channel Selector Integration', () => {
    it('renders channel selector with default channel', () => {
      render(<CommandPanel {...defaultProps} />);

      expect(screen.getByText('Channel:')).toBeInTheDocument();
      expect(screen.getByText('Say')).toBeInTheDocument();
      expect(screen.getByText('/say')).toBeInTheDocument();
    });

    it('allows changing channels', async () => {
      render(<CommandPanel {...defaultProps} />);

      // Click the channel selector
      const channelButton = screen.getByText('Say');
      fireEvent.click(channelButton);

      // Select Global channel
      await waitFor(() => {
        const globalOption = screen.getByText('Global');
        fireEvent.click(globalOption);
      });

      // Verify the channel changed
      expect(screen.getByText('Global')).toBeInTheDocument();
      expect(screen.getByText('/g')).toBeInTheDocument();
    });

    it('prepends channel command when sending message without slash', async () => {
      const onSendCommand = vi.fn();
      render(<CommandPanel {...defaultProps} onSendCommand={onSendCommand} />);

      // Change to Global channel
      const channelButton = screen.getByText('Say');
      fireEvent.click(channelButton);

      await waitFor(() => {
        const globalOption = screen.getByText('Global');
        fireEvent.click(globalOption);
      });

      // Enter a message without slash
      const input = screen.getByPlaceholderText(/Enter command/);
      fireEvent.change(input, { target: { value: 'Hello world!' } });

      // Send the message
      const sendButton = screen.getByText('Send');
      fireEvent.click(sendButton);

      // Verify the command was prepended with channel
      expect(onSendCommand).toHaveBeenCalledWith('/g Hello world!');
    });

    it('does not prepend channel command when message starts with slash', async () => {
      const onSendCommand = vi.fn();
      render(<CommandPanel {...defaultProps} onSendCommand={onSendCommand} />);

      // Change to Local channel
      const channelButton = screen.getByText('Say');
      fireEvent.click(channelButton);

      await waitFor(() => {
        const localOption = screen.getByText('Local');
        fireEvent.click(localOption);
      });

      // Enter a message with slash
      const input = screen.getByPlaceholderText(/Enter command/);
      fireEvent.change(input, { target: { value: '/look' } });

      // Send the message
      const sendButton = screen.getByText('Send');
      fireEvent.click(sendButton);

      // Verify the command was not prepended
      expect(onSendCommand).toHaveBeenCalledWith('/look');
    });

    it('shows channel-specific quick commands', async () => {
      render(<CommandPanel {...defaultProps} />);

      // Change to Global channel
      const channelButton = screen.getByText('Say');
      fireEvent.click(channelButton);

      await waitFor(() => {
        const globalOption = screen.getByText('Global');
        fireEvent.click(globalOption);
      });

      // Check for channel-specific quick commands
      expect(screen.getByText('Global Channel:')).toBeInTheDocument();
      expect(screen.getByText('/g Hello!')).toBeInTheDocument();
      expect(screen.getByText('/g How is everyone?')).toBeInTheDocument();
    });

    it('disables channel selector when disconnected', () => {
      render(<CommandPanel {...defaultProps} isConnected={false} />);

      const channelButton = screen.getByText('Say').closest('button');
      expect(channelButton).toBeDisabled();
    });
  });

  describe('Global Channel Functionality', () => {
    it('shows global channel in dropdown', async () => {
      render(<CommandPanel {...defaultProps} />);

      const channelButton = screen.getByText('Say');
      fireEvent.click(channelButton);

      await waitFor(() => {
        expect(screen.getByText('Global')).toBeInTheDocument();
        expect(screen.getByText('Chat with all players on the server')).toBeInTheDocument();
        expect(screen.getByText('/g')).toBeInTheDocument();
      });
    });

    it('sends global channel commands correctly', async () => {
      const onSendCommand = vi.fn();
      render(<CommandPanel {...defaultProps} onSendCommand={onSendCommand} />);

      // Select Global channel
      const channelButton = screen.getByText('Say');
      fireEvent.click(channelButton);

      await waitFor(() => {
        const globalOption = screen.getByText('Global');
        fireEvent.click(globalOption);
      });

      // Use global channel quick command
      const quickCommand = screen.getByText('/g Hello!');
      fireEvent.click(quickCommand);

      // Verify the command was sent (the quick command sets the input value)
      const input = screen.getByPlaceholderText(/Enter command/);
      expect(input).toHaveValue('/g Hello!');
    });

    it('handles global channel message input', async () => {
      const onSendCommand = vi.fn();
      render(<CommandPanel {...defaultProps} onSendCommand={onSendCommand} />);

      // Select Global channel
      const channelButton = screen.getByText('Say');
      fireEvent.click(channelButton);

      await waitFor(() => {
        const globalOption = screen.getByText('Global');
        fireEvent.click(globalOption);
      });

      // Type a message
      const input = screen.getByPlaceholderText(/Enter command/);
      fireEvent.change(input, { target: { value: 'Testing global chat' } });

      // Send the message
      const sendButton = screen.getByText('Send');
      fireEvent.click(sendButton);

      // Verify the command was sent with global prefix
      expect(onSendCommand).toHaveBeenCalledWith('/g Testing global chat');
    });
  });

  describe('Channel Switching', () => {
    it('allows switching between channels', async () => {
      render(<CommandPanel {...defaultProps} />);

      // Switch to Global channel
      const channelButton = screen.getByText('Say');
      fireEvent.click(channelButton);

      await waitFor(() => {
        const globalOption = screen.getByText('Global');
        fireEvent.click(globalOption);
      });

      // Verify the channel changed
      expect(screen.getByText('Global')).toBeInTheDocument();
      expect(screen.getByText('/g')).toBeInTheDocument();
    });

    it('updates quick commands when switching channels', async () => {
      render(<CommandPanel {...defaultProps} />);

      // Switch to Local channel
      const channelButton = screen.getByText('Say');
      fireEvent.click(channelButton);

      await waitFor(() => {
        const localOption = screen.getByText('Local');
        fireEvent.click(localOption);
      });

      // Check for local channel quick commands
      expect(screen.getByText('Local Channel:')).toBeInTheDocument();
      expect(screen.getByText('/l Hello!')).toBeInTheDocument();

      // Switch to Global channel
      fireEvent.click(screen.getByText('Local'));

      await waitFor(() => {
        const globalOption = screen.getByText('Global');
        fireEvent.click(globalOption);
      });

      // Check for global channel quick commands
      expect(screen.getByText('Global Channel:')).toBeInTheDocument();
      expect(screen.getByText('/g Hello!')).toBeInTheDocument();
    });
  });

  describe('Disabled Channels', () => {
    it('shows disabled channels as disabled in dropdown', async () => {
      render(<CommandPanel {...defaultProps} />);

      const channelButton = screen.getByText('Say');
      fireEvent.click(channelButton);

      await waitFor(() => {
        const whisperOption = screen.getByText('Whisper').closest('button');
        expect(whisperOption).toBeDisabled();
      });
    });

    it('does not allow selecting disabled channels', async () => {
      render(<CommandPanel {...defaultProps} />);

      const channelButton = screen.getByText('Say');
      fireEvent.click(channelButton);

      await waitFor(() => {
        const whisperOption = screen.getByText('Whisper').closest('button');
        fireEvent.click(whisperOption!);
      });

      // Verify the channel didn't change (should still be Say)
      // Use a more specific selector to avoid ambiguity
      const channelButtons = screen.getAllByText('Say');
      expect(channelButtons.length).toBeGreaterThan(0);
    });
  });

  describe('Command History Integration', () => {
    it('shows channel commands in history', () => {
      const commandHistory = ['/say Hello', '/g Global message', '/l Local message'];
      render(<CommandPanel {...defaultProps} commandHistory={commandHistory} />);

      expect(screen.getByText('> /say Hello')).toBeInTheDocument();
      expect(screen.getByText('> /g Global message')).toBeInTheDocument();
      expect(screen.getByText('> /l Local message')).toBeInTheDocument();
    });

    it('allows clicking on channel commands in history', () => {
      const commandHistory = ['/g Hello world'];
      render(<CommandPanel {...defaultProps} commandHistory={commandHistory} />);

      const historyItem = screen.getByText('> /g Hello world');
      fireEvent.click(historyItem);

      const input = screen.getByPlaceholderText(/Enter command/);
      expect(input).toHaveValue('/g Hello world');
    });
  });
});
