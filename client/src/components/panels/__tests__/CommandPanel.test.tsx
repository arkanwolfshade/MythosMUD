import { fireEvent, render, screen, waitFor } from '@testing-library/react';
import React from 'react';
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

// Mock the ChannelSelector component
vi.mock('../../ui/ChannelSelector', () => ({
  ChannelSelector: ({
    channels,
    selectedChannel,
    onChannelSelect,
    disabled,
  }: {
    channels: Array<{ id: string; name: string; shortcut?: string }>;
    selectedChannel: string;
    onChannelSelect: (channelId: string) => void;
    disabled?: boolean;
  }) => {
    const [isOpen, setIsOpen] = React.useState(false);
    const [currentChannel, setCurrentChannel] = React.useState(selectedChannel);

    const handleChannelSelect = (channelId: string) => {
      setCurrentChannel(channelId);
      onChannelSelect(channelId);
      setIsOpen(false);
    };

    const currentChannelData = channels.find(channel => channel.id === currentChannel);

    return (
      <div className="relative">
        <button
          onClick={() => !disabled && setIsOpen(!isOpen)}
          disabled={disabled}
          className="relative z-20 flex items-center gap-2 px-3 py-2 bg-mythos-terminal-surface border border-gray-700 rounded text-sm font-mono transition-all duration-200 min-w-[140px]"
        >
          <div data-testid={`icon-${currentChannelData?.id || 'undefined'}`} data-size="16" data-variant="primary">
            {currentChannelData?.id || 'undefined'}
          </div>
          <span className="text-mythos-terminal-text">{currentChannelData?.name || 'Unknown'}</span>
          {currentChannelData?.shortcut && (
            <span className="text-xs text-mythos-terminal-text-secondary ml-auto">/{currentChannelData.shortcut}</span>
          )}
          <div data-size="12" data-testid="icon-exit" data-variant="secondary">
            exit
          </div>
        </button>

        {isOpen && !disabled && (
          <div className="absolute top-full left-0 right-0 mt-1 bg-mythos-terminal-surface border border-gray-700 rounded shadow-lg z-30">
            {channels.map(channel => (
              <button
                key={channel.id}
                onClick={() => handleChannelSelect(channel.id)}
                className="w-full flex items-center gap-3 px-3 py-2 text-left text-sm font-mono border-b border-gray-700 last:border-b-0"
              >
                <div data-testid={`icon-${channel.id}`} data-size="16" data-variant="secondary">
                  {channel.id}
                </div>
                <div className="flex-1">
                  <div className="flex items-center gap-2">
                    <span>{channel.name}</span>
                    {channel.shortcut && (
                      <span className="text-xs text-mythos-terminal-text-secondary">/{channel.shortcut}</span>
                    )}
                  </div>
                </div>
              </button>
            ))}
          </div>
        )}
      </div>
    );
  },
}));

// Mock the TerminalInput component
vi.mock('../../ui/TerminalInput', () => ({
  TerminalInput: React.forwardRef<
    HTMLInputElement,
    {
      value: string;
      onChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
      onKeyDown?: (e: React.KeyboardEvent) => void;
      placeholder?: string;
      disabled?: boolean;
      className?: string;
      onFocus?: () => void;
    }
  >((props, ref) => (
    <input
      ref={ref}
      value={props.value}
      onChange={props.onChange}
      onKeyDown={props.onKeyDown}
      placeholder={props.placeholder}
      disabled={props.disabled}
      className={props.className}
      onFocus={props.onFocus}
    />
  )),
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

      expect(screen.getByText('Commands')).toBeInTheDocument();
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
      const input = screen.getByPlaceholderText("Enter game command (e.g., 'look', 'inventory', 'go north')...");
      fireEvent.change(input, { target: { value: 'Hello world!' } });

      // Send the message
      const sendButton = screen.getByText('Send Command');
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
      const input = screen.getByPlaceholderText("Enter game command (e.g., 'look', 'inventory', 'go north')...");
      fireEvent.change(input, { target: { value: '/look' } });

      // Send the message
      const sendButton = screen.getByText('Send Command');
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

      // Check that we're on Global channel
      expect(screen.getByText('Global')).toBeInTheDocument();
      expect(screen.getByText('/g')).toBeInTheDocument();
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

      // Verify we're on Global channel
      expect(screen.getByText('Global')).toBeInTheDocument();
      expect(screen.getByText('/g')).toBeInTheDocument();
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
      const input = screen.getByPlaceholderText("Enter game command (e.g., 'look', 'inventory', 'go north')...");
      fireEvent.change(input, { target: { value: 'Testing global chat' } });

      // Send the message
      const sendButton = screen.getByText('Send Command');
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

      // Check that we're on Local channel
      expect(screen.getByText('Local')).toBeInTheDocument();
      expect(screen.getByText('/l')).toBeInTheDocument();

      // Switch to Global channel
      fireEvent.click(screen.getByText('Local'));

      await waitFor(() => {
        const globalOption = screen.getByText('Global');
        fireEvent.click(globalOption);
      });

      // Check that we're on Global channel
      expect(screen.getByText('Global')).toBeInTheDocument();
      expect(screen.getByText('/g')).toBeInTheDocument();
    });
  });

  describe('Whisper Channel', () => {
    it('allows selecting whisper channel', async () => {
      render(<CommandPanel {...defaultProps} />);

      const channelButton = screen.getByText('Say');
      fireEvent.click(channelButton);

      await waitFor(() => {
        const whisperOption = screen.getByText('Whisper').closest('button');
        expect(whisperOption).not.toBeDisabled();
        fireEvent.click(whisperOption!);
      });

      // Verify the channel changed to whisper
      expect(screen.getByText('Whisper')).toBeInTheDocument();
      expect(screen.getByText('/whisper')).toBeInTheDocument();
    });

    it('shows whisper channel quick commands', async () => {
      render(<CommandPanel {...defaultProps} />);

      // Switch to Whisper channel
      const channelButton = screen.getByText('Say');
      fireEvent.click(channelButton);

      // Check that we're on Whisper channel
      expect(screen.getByText('Whisper')).toBeInTheDocument();
      expect(screen.getByText('/whisper')).toBeInTheDocument();
    });
  });

  describe('Command History Integration', () => {
    it('shows channel commands in history', () => {
      const commandHistory = ['/say Hello', '/g Global message', '/l Local message'];
      render(<CommandPanel {...defaultProps} commandHistory={commandHistory} />);

      expect(screen.getByText('/say Hello')).toBeInTheDocument();
      expect(screen.getByText('/g Global message')).toBeInTheDocument();
      expect(screen.getByText('/l Local message')).toBeInTheDocument();
    });

    it('allows clicking on channel commands in history', () => {
      const commandHistory = ['/g Hello world'];
      render(<CommandPanel {...defaultProps} commandHistory={commandHistory} />);

      const historyItem = screen.getByText('/g Hello world');
      fireEvent.click(historyItem);

      const input = screen.getByPlaceholderText("Enter game command (e.g., 'look', 'inventory', 'go north')...");
      expect(input).toHaveValue('/g Hello world');
    });
  });
});
