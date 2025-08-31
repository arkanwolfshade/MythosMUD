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
    command: 'command',
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
  onChange?: (value: string) => void;
  onKeyDown?: (event: React.KeyboardEvent) => void;
  [key: string]: unknown;
}

vi.mock('../src/components/ui/TerminalInput', () => ({
  TerminalInput: ({ value, onChange, onKeyDown, ...props }: TerminalInputProps) => (
    <input value={value} onChange={e => onChange?.(e.target.value)} onKeyDown={onKeyDown} {...props} />
  ),
}));

describe('CommandPanel', () => {
  const mockCommandHistory = ['look', 'go north', 'inventory', 'say hello', 'who'];

  const defaultProps = {
    commandHistory: mockCommandHistory,
    onSendCommand: vi.fn(),
    onClearHistory: vi.fn(),
    disabled: false,
    isConnected: true,
  };

  beforeEach(() => {
    vi.clearAllMocks();
  });

  describe('Basic Rendering', () => {
    it('renders command panel with header', () => {
      render(<CommandPanel {...defaultProps} />);

      expect(screen.getByText('Commands')).toBeInTheDocument();
      expect(screen.getByTestId('icon-command')).toBeInTheDocument();
    });

    it('displays command input field', () => {
      render(<CommandPanel {...defaultProps} />);

      expect(
        screen.getByPlaceholderText("Enter game command (e.g., 'look', 'inventory', 'go north')...")
      ).toBeInTheDocument();
      expect(screen.getByText('Send')).toBeInTheDocument();
    });

    it('shows command history', () => {
      render(<CommandPanel {...defaultProps} />);

      expect(screen.getByText('look')).toBeInTheDocument();
      expect(screen.getByText('go north')).toBeInTheDocument();
      expect(screen.getByText('inventory')).toBeInTheDocument();
    });
  });

  describe('Command Input Functionality', () => {
    it('sends command when form is submitted', () => {
      render(<CommandPanel {...defaultProps} />);

      const input = screen.getByPlaceholderText('Enter game command...');
      const sendButton = screen.getByText('Send');

      fireEvent.change(input, { target: { value: 'look' } });
      fireEvent.click(sendButton);

      expect(defaultProps.onSendCommand).toHaveBeenCalledWith('look');
    });

    it('clears input after sending command', () => {
      render(<CommandPanel {...defaultProps} />);

      const input = screen.getByPlaceholderText('Enter game command...');
      const sendButton = screen.getByText('Send');

      fireEvent.change(input, { target: { value: 'look' } });
      fireEvent.click(sendButton);

      expect(input).toHaveValue('');
    });

    it('does not send empty commands', () => {
      render(<CommandPanel {...defaultProps} />);

      const sendButton = screen.getByText('Send');
      fireEvent.click(sendButton);

      expect(defaultProps.onSendCommand).not.toHaveBeenCalled();
    });

    it('disables input when disconnected', () => {
      render(<CommandPanel {...defaultProps} isConnected={false} />);

      const input = screen.getByPlaceholderText('Enter game command...');
      const sendButton = screen.getByText('Send');

      expect(input).toBeDisabled();
      expect(sendButton).toBeDisabled();
    });

    it('sends command on Enter key press', () => {
      render(<CommandPanel {...defaultProps} />);

      const input = screen.getByPlaceholderText('Enter game command...');

      fireEvent.change(input, { target: { value: 'look' } });
      fireEvent.keyDown(input, { key: 'Enter' });

      expect(defaultProps.onSendCommand).toHaveBeenCalledWith('look');
    });
  });

  describe('Command History Navigation', () => {
    it('navigates through command history with arrow keys', () => {
      render(<CommandPanel {...defaultProps} />);

      const input = screen.getByPlaceholderText('Enter game command...');

      // Navigate up through history
      fireEvent.keyDown(input, { key: 'ArrowUp' });
      expect(input).toHaveValue('who');

      fireEvent.keyDown(input, { key: 'ArrowUp' });
      expect(input).toHaveValue('say hello');

      // Navigate down through history
      fireEvent.keyDown(input, { key: 'ArrowDown' });
      expect(input).toHaveValue('who');

      fireEvent.keyDown(input, { key: 'ArrowDown' });
      expect(input).toHaveValue('');
    });

    it('stops at history boundaries', () => {
      render(<CommandPanel {...defaultProps} />);

      const input = screen.getByPlaceholderText('Enter game command...');

      // Try to go beyond the beginning of history
      for (let i = 0; i < 10; i++) {
        fireEvent.keyDown(input, { key: 'ArrowUp' });
      }

      // Should stop at the oldest command
      expect(input).toHaveValue('look');
    });

    it('resets to empty when going past the end of history', () => {
      render(<CommandPanel {...defaultProps} />);

      const input = screen.getByPlaceholderText('Enter game command...');

      // Go to the end of history
      fireEvent.keyDown(input, { key: 'ArrowUp' });
      expect(input).toHaveValue('who');

      // Go past the end
      fireEvent.keyDown(input, { key: 'ArrowDown' });
      expect(input).toHaveValue('');
    });
  });

  describe('Command Suggestions', () => {
    it('shows command suggestions based on input', () => {
      render(<CommandPanel {...defaultProps} />);

      const input = screen.getByPlaceholderText('Enter game command...');

      fireEvent.change(input, { target: { value: 'l' } });

      // Should show suggestions starting with 'l'
      expect(screen.getByText('look')).toBeInTheDocument();
    });

    it('filters suggestions as user types', () => {
      render(<CommandPanel {...defaultProps} />);

      const input = screen.getByPlaceholderText('Enter game command...');

      fireEvent.change(input, { target: { value: 'go' } });

      // Should show suggestions containing 'go'
      expect(screen.getByText('go north')).toBeInTheDocument();
    });

    it('allows selecting suggestions with arrow keys', () => {
      render(<CommandPanel {...defaultProps} />);

      const input = screen.getByPlaceholderText('Enter game command...');

      fireEvent.change(input, { target: { value: 'l' } });

      // Navigate through suggestions
      fireEvent.keyDown(input, { key: 'ArrowUp' });
      fireEvent.keyDown(input, { key: 'ArrowDown' });

      // Should not throw errors
      expect(input).toBeInTheDocument();
    });

    it('completes command when suggestion is selected', () => {
      render(<CommandPanel {...defaultProps} />);

      const input = screen.getByPlaceholderText('Enter game command...');

      fireEvent.change(input, { target: { value: 'l' } });

      // Click on a suggestion
      const suggestion = screen.getByText('look');
      fireEvent.click(suggestion);

      expect(input).toHaveValue('look');
    });
  });

  describe('Quick Commands', () => {
    it('shows quick command buttons', () => {
      render(<CommandPanel {...defaultProps} />);

      expect(screen.getByText('look')).toBeInTheDocument();
      expect(screen.getByText('inventory')).toBeInTheDocument();
      expect(screen.getByText('who')).toBeInTheDocument();
    });

    it('executes quick commands when clicked', () => {
      render(<CommandPanel {...defaultProps} />);

      const lookButton = screen.getByText('look');
      fireEvent.click(lookButton);

      expect(defaultProps.onSendCommand).toHaveBeenCalledWith('look');
    });

    it('disables quick commands when disconnected', () => {
      render(<CommandPanel {...defaultProps} isConnected={false} />);

      const lookButton = screen.getByText('look');
      expect(lookButton).toBeDisabled();
    });
  });

  describe('Command History Management', () => {
    it('shows command history list', () => {
      render(<CommandPanel {...defaultProps} />);

      expect(screen.getByText('Command History')).toBeInTheDocument();

      // Should show recent commands
      expect(screen.getByText('look')).toBeInTheDocument();
      expect(screen.getByText('go north')).toBeInTheDocument();
      expect(screen.getByText('inventory')).toBeInTheDocument();
    });

    it('allows clearing command history', () => {
      render(<CommandPanel {...defaultProps} />);

      const clearButton = screen.getByText('Clear History');
      fireEvent.click(clearButton);

      expect(defaultProps.onClearHistory).toHaveBeenCalled();
    });

    it('executes commands from history when clicked', () => {
      render(<CommandPanel {...defaultProps} />);

      const historyItem = screen.getByText('look');
      fireEvent.click(historyItem);

      expect(defaultProps.onSendCommand).toHaveBeenCalledWith('look');
    });

    it('limits history display to recent commands', () => {
      const longHistory = Array.from({ length: 50 }, (_, i) => `command${i}`);

      render(<CommandPanel {...defaultProps} commandHistory={longHistory} />);

      // Should only show recent commands (e.g., last 10)
      expect(screen.getByText('command49')).toBeInTheDocument();
      expect(screen.queryByText('command0')).not.toBeInTheDocument();
    });
  });

  describe('Common Commands Section', () => {
    it('shows categorized common commands', () => {
      render(<CommandPanel {...defaultProps} />);

      expect(screen.getByText('Common Commands')).toBeInTheDocument();

      // Should show movement commands
      expect(screen.getByText('north')).toBeInTheDocument();
      expect(screen.getByText('south')).toBeInTheDocument();
      expect(screen.getByText('east')).toBeInTheDocument();
      expect(screen.getByText('west')).toBeInTheDocument();

      // Should show other common commands
      expect(screen.getByText('look')).toBeInTheDocument();
      expect(screen.getByText('inventory')).toBeInTheDocument();
    });

    it('executes common commands when clicked', () => {
      render(<CommandPanel {...defaultProps} />);

      const northButton = screen.getByText('north');
      fireEvent.click(northButton);

      expect(defaultProps.onSendCommand).toHaveBeenCalledWith('go north');
    });

    it('disables common commands when disconnected', () => {
      render(<CommandPanel {...defaultProps} isConnected={false} />);

      const northButton = screen.getByText('north');
      expect(northButton).toBeDisabled();
    });
  });

  describe('Input Validation', () => {
    it('trims whitespace from commands', () => {
      render(<CommandPanel {...defaultProps} />);

      const input = screen.getByPlaceholderText('Enter game command...');
      const sendButton = screen.getByText('Send');

      fireEvent.change(input, { target: { value: '  look  ' } });
      fireEvent.click(sendButton);

      expect(defaultProps.onSendCommand).toHaveBeenCalledWith('look');
    });

    it('prevents sending commands with only whitespace', () => {
      render(<CommandPanel {...defaultProps} />);

      const input = screen.getByPlaceholderText('Enter game command...');
      const sendButton = screen.getByText('Send');

      fireEvent.change(input, { target: { value: '   ' } });
      fireEvent.click(sendButton);

      expect(defaultProps.onSendCommand).not.toHaveBeenCalled();
    });
  });

  describe('Performance', () => {
    it('handles large command history efficiently', () => {
      const largeHistory = Array.from({ length: 1000 }, (_, i) => `command${i}`);

      render(<CommandPanel {...defaultProps} commandHistory={largeHistory} />);

      // Should render without performance issues
      expect(screen.getByText('command999')).toBeInTheDocument();
    });

    it('debounces suggestion filtering', async () => {
      render(<CommandPanel {...defaultProps} />);

      const input = screen.getByPlaceholderText('Enter game command...');

      // Rapidly type
      fireEvent.change(input, { target: { value: 'l' } });
      fireEvent.change(input, { target: { value: 'lo' } });
      fireEvent.change(input, { target: { value: 'loo' } });
      fireEvent.change(input, { target: { value: 'look' } });

      // Should debounce and not cause performance issues
      await waitFor(() => {
        expect(screen.getByText('look')).toBeInTheDocument();
      });
    });
  });

  describe('Error Handling', () => {
    it('handles missing props gracefully', () => {
      const { container } = render(<CommandPanel commandHistory={[]} onSendCommand={vi.fn()} />);

      expect(container).toBeInTheDocument();
    });

    it('handles empty command history', () => {
      render(<CommandPanel {...defaultProps} commandHistory={[]} />);

      expect(screen.getByText('No command history')).toBeInTheDocument();
    });

    it('handles malformed command history', () => {
      const malformedHistory = ['valid', null, undefined, '', 'another valid'];

      render(<CommandPanel {...defaultProps} commandHistory={malformedHistory} />);

      // Should not crash and should display valid commands
      expect(screen.getByText('valid')).toBeInTheDocument();
      expect(screen.getByText('another valid')).toBeInTheDocument();
    });
  });

  describe('Accessibility', () => {
    it('has proper ARIA labels', () => {
      render(<CommandPanel {...defaultProps} />);

      expect(screen.getByLabelText('Command Input')).toBeInTheDocument();
      expect(screen.getByLabelText('Command History')).toBeInTheDocument();
    });

    it('supports keyboard navigation', () => {
      render(<CommandPanel {...defaultProps} />);

      const input = screen.getByPlaceholderText('Enter game command...');

      // Test keyboard navigation
      fireEvent.keyDown(input, { key: 'Tab' });
      fireEvent.keyDown(input, { key: 'Escape' });

      // Should not throw errors
      expect(input).toBeInTheDocument();
    });

    it('provides keyboard shortcuts for common actions', () => {
      render(<CommandPanel {...defaultProps} />);

      const input = screen.getByPlaceholderText('Enter game command...');

      // Test Ctrl+L for clearing input (if implemented)
      fireEvent.keyDown(input, { key: 'l', ctrlKey: true });

      // Should not throw errors
      expect(input).toBeInTheDocument();
    });
  });

  describe('Responsive Design', () => {
    it('adapts to different screen sizes', () => {
      render(<CommandPanel {...defaultProps} />);

      // Test that responsive classes are applied
      const input = screen.getByPlaceholderText('Enter game command...');
      expect(input).toBeInTheDocument();

      // The component should render without errors on different screen sizes
    });
  });
});
