import { fireEvent, render, screen } from '@testing-library/react';
import React from 'react';
import { beforeEach, describe, expect, it, vi } from 'vitest';
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
    size?: number;
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
    portal: 'portal',
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
    variant: _variant,
    size: _size,
    ...props
  }: {
    children: React.ReactNode;
    onClick?: () => void;
    disabled?: boolean;
    className?: string;
    title?: string;
    variant?: string;
    size?: string;
    [key: string]: unknown;
  }) => (
    <button onClick={onClick} disabled={disabled} className={className} title={title} {...props}>
      {children}
    </button>
  ),
}));

// Mock the LogoutButton component
vi.mock('../../ui/LogoutButton', () => ({
  LogoutButton: ({
    onLogout,
    disabled,
    isLoggingOut,
  }: {
    onLogout: () => void;
    disabled?: boolean;
    isLoggingOut?: boolean;
  }) => (
    <button
      onClick={onLogout}
      disabled={disabled || isLoggingOut}
      data-testid="logout-button"
      aria-label="Exit the realm and return to login screen"
      title="Exit the realm and return to login screen (Ctrl+Q)"
    >
      <div className="flex items-center justify-center gap-2">
        <div data-testid="icon-portal" data-size="16" data-variant="error">
          portal
        </div>
        <span>{isLoggingOut ? 'Exiting...' : 'Exit the Realm'}</span>
      </div>
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
          className="relative z-20 flex items-center gap-2 px-3 py-2 bg-mythos-terminal-surface border border-gray-700 rounded text-sm font-mono transition-all duration-200 min-w-min-w-button"
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
                onClick={() => {
                  handleChannelSelect(channel.id);
                }}
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

describe('CommandPanel with LogoutButton Integration', () => {
  const defaultProps = {
    commandHistory: ['look', 'n', 'say Hello'],
    onSendCommand: vi.fn(),
    onClearHistory: vi.fn(),
    onLogout: vi.fn(),
    isConnected: true,
  };

  beforeEach(() => {
    vi.clearAllMocks();
  });

  describe('Logout Button Integration', () => {
    it('renders logout button when onLogout prop is provided', () => {
      render(<CommandPanel {...defaultProps} />);

      expect(screen.getByTestId('logout-button')).toBeInTheDocument();
      expect(screen.getByText('Exit the Realm')).toBeInTheDocument();
      expect(screen.getByTestId('icon-portal')).toBeInTheDocument();
    });

    it('does not render logout button when onLogout prop is not provided', () => {
      // Destructuring removes onLogout from props, variable intentionally unused
      // eslint-disable-next-line @typescript-eslint/no-unused-vars
      const { onLogout, ...propsWithoutLogout } = defaultProps;
      render(<CommandPanel {...propsWithoutLogout} />);

      expect(screen.queryByTestId('logout-button')).not.toBeInTheDocument();
    });

    it('calls onLogout when logout button is clicked', () => {
      const onLogout = vi.fn();
      render(<CommandPanel {...defaultProps} onLogout={onLogout} />);

      const logoutButton = screen.getByTestId('logout-button');
      fireEvent.click(logoutButton);

      expect(onLogout).toHaveBeenCalledTimes(1);
    });

    it('positions logout button at the bottom of the panel', () => {
      render(<CommandPanel {...defaultProps} />);

      const logoutButton = screen.getByTestId('logout-button');
      const panel = logoutButton.closest('.command-panel');

      // The logout button should be the last interactive element in the panel
      const allButtons = panel?.querySelectorAll('button');
      const lastButton = allButtons?.[allButtons.length - 1];

      expect(lastButton).toBe(logoutButton);
    });

    it('disables logout button when panel is disabled', () => {
      render(<CommandPanel {...defaultProps} disabled={true} />);

      const logoutButton = screen.getByTestId('logout-button');
      expect(logoutButton).toBeDisabled();
    });

    it('disables logout button when not connected', () => {
      render(<CommandPanel {...defaultProps} isConnected={false} />);

      const logoutButton = screen.getByTestId('logout-button');
      expect(logoutButton).toBeDisabled();
    });

    it('disables logout button when both disabled and not connected', () => {
      render(<CommandPanel {...defaultProps} disabled={true} isConnected={false} />);

      const logoutButton = screen.getByTestId('logout-button');
      expect(logoutButton).toBeDisabled();
    });

    it('shows logout button with proper styling and accessibility attributes', () => {
      render(<CommandPanel {...defaultProps} />);

      const logoutButton = screen.getByTestId('logout-button');
      expect(logoutButton).toHaveAttribute('aria-label', 'Exit the realm and return to login screen');
      expect(logoutButton).toHaveAttribute('title', 'Exit the realm and return to login screen (Ctrl+Q)');
    });
  });

  describe('Panel Layout with Logout Button', () => {
    it('maintains proper panel structure with logout button at bottom', () => {
      render(<CommandPanel {...defaultProps} />);

      // Check that all sections are present in correct order
      expect(screen.getByTestId('command-panel')).toBeInTheDocument(); // Panel container
      expect(screen.getByText('Recent Commands')).toBeInTheDocument(); // Command History
      // Note: Quick Commands section was removed - feature not implemented
      expect(screen.getByTestId('logout-button')).toBeInTheDocument(); // Logout Button
    });

    it('logout button section has proper styling and separation', () => {
      render(<CommandPanel {...defaultProps} />);

      const logoutButton = screen.getByTestId('logout-button');
      const logoutSection = logoutButton.closest('div');

      expect(logoutSection).toHaveClass('p-3');
      expect(logoutSection).toHaveClass('border-t');
      expect(logoutSection).toHaveClass('border-gray-700');
      expect(logoutSection).toHaveClass('bg-mythos-terminal-background');
    });
  });

  describe('Keyboard Shortcut Integration', () => {
    it('logout button responds to Ctrl+Q keyboard shortcut', () => {
      const onLogout = vi.fn();
      render(<CommandPanel {...defaultProps} onLogout={onLogout} />);

      // Simulate Ctrl+Q keypress
      fireEvent.keyDown(document, { key: 'q', code: 'KeyQ', ctrlKey: true });

      expect(onLogout).toHaveBeenCalledTimes(1);
    });

    it('logout button does not respond to Ctrl+Q when disabled', () => {
      const onLogout = vi.fn();
      render(<CommandPanel {...defaultProps} onLogout={onLogout} disabled={true} />);

      // Simulate Ctrl+Q keypress
      fireEvent.keyDown(document, { key: 'q', code: 'KeyQ', ctrlKey: true });

      expect(onLogout).not.toHaveBeenCalled();
    });

    it('logout button does not respond to Ctrl+Q when not connected', () => {
      const onLogout = vi.fn();
      render(<CommandPanel {...defaultProps} onLogout={onLogout} isConnected={false} />);

      // Simulate Ctrl+Q keypress
      fireEvent.keyDown(document, { key: 'q', code: 'KeyQ', ctrlKey: true });

      expect(onLogout).not.toHaveBeenCalled();
    });
  });

  describe('Component Interaction', () => {
    it('logout button works alongside other panel functionality', () => {
      const onSendCommand = vi.fn();
      const onClearHistory = vi.fn();
      const onLogout = vi.fn();

      render(
        <CommandPanel
          {...defaultProps}
          onSendCommand={onSendCommand}
          onClearHistory={onClearHistory}
          onLogout={onLogout}
        />
      );

      // Test command input
      const input = screen.getByPlaceholderText("Enter game command (e.g., 'look', 'inventory', 'go north')...");
      fireEvent.change(input, { target: { value: 'look' } });
      fireEvent.keyDown(input, { key: 'Enter' });
      expect(onSendCommand).toHaveBeenCalledWith('look');

      // Test clear history
      const clearButton = screen.getByText('Clear');
      fireEvent.click(clearButton);
      expect(onClearHistory).toHaveBeenCalled();

      // Test logout
      const logoutButton = screen.getByTestId('logout-button');
      fireEvent.click(logoutButton);
      expect(onLogout).toHaveBeenCalled();
    });

    it('logout button maintains focus management with other panel elements', () => {
      render(<CommandPanel {...defaultProps} />);

      const input = screen.getByPlaceholderText("Enter game command (e.g., 'look', 'inventory', 'go north')...");
      const logoutButton = screen.getByTestId('logout-button');

      // Focus input
      input.focus();
      expect(input).toHaveFocus();

      // Focus logout button
      logoutButton.focus();
      expect(logoutButton).toHaveFocus();
    });
  });
});
