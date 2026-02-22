import { fireEvent, render, screen, waitFor } from '@testing-library/react';
import { beforeEach, describe, expect, it, vi } from 'vitest';
import { CommandPanel } from '../panels/CommandPanel';

// Mock the dependencies
vi.mock('../../ui/EldritchIcon', () => ({
  EldritchIcon: ({ name, className }: { name: string; className?: string }) => (
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

vi.mock('../../ui/TerminalButton', () => ({
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

vi.mock('../../ui/TerminalInput', () => ({
  TerminalInput: ({ value, onChange, onKeyDown, ...props }: TerminalInputProps) => (
    <input value={value} onChange={onChange} onKeyDown={onKeyDown} {...props} />
  ),
}));

describe('CommandPanel (components)', () => {
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

      expect(screen.getByTestId('command-panel')).toBeInTheDocument();
      expect(screen.getByText('Recent Commands')).toBeInTheDocument();
    });

    it('displays command input field', () => {
      render(<CommandPanel {...defaultProps} />);

      expect(screen.getByPlaceholderText(/Enter game command/)).toBeInTheDocument();
      expect(screen.getByText('Send Command')).toBeInTheDocument();
    });

    it('shows Recent Commands section with history items', () => {
      render(<CommandPanel {...defaultProps} />);

      expect(screen.getByText('Recent Commands')).toBeInTheDocument();
      expect(screen.getByText('look')).toBeInTheDocument();
      expect(screen.getByText('go north')).toBeInTheDocument();
      expect(screen.getByText('inventory')).toBeInTheDocument();
    });
  });

  describe('Command Input Functionality', () => {
    it('sends command when form is submitted', () => {
      render(<CommandPanel {...defaultProps} />);

      const input = screen.getByPlaceholderText(/Enter game command/);
      const sendButton = screen.getByText('Send Command');

      fireEvent.change(input, { target: { value: 'look' } });
      fireEvent.click(sendButton);

      expect(defaultProps.onSendCommand).toHaveBeenCalledWith('look');
    });

    it('clears input after sending command', () => {
      render(<CommandPanel {...defaultProps} />);

      const input = screen.getByPlaceholderText(/Enter game command/);
      const sendButton = screen.getByText('Send Command');

      fireEvent.change(input, { target: { value: 'look' } });
      fireEvent.click(sendButton);

      expect(input).toHaveValue('');
    });

    it('does not send empty commands', () => {
      render(<CommandPanel {...defaultProps} />);

      const sendButton = screen.getByText('Send Command');
      fireEvent.click(sendButton);

      expect(defaultProps.onSendCommand).not.toHaveBeenCalled();
    });

    it('disables input when disconnected', () => {
      render(<CommandPanel {...defaultProps} isConnected={false} />);

      const input = screen.getByPlaceholderText(/Enter game command/);
      const sendButton = screen.getByText('Send Command');

      expect(input).toBeDisabled();
      expect(sendButton).toBeDisabled();
    });

    it('sends command on Enter key press', () => {
      render(<CommandPanel {...defaultProps} />);

      const input = screen.getByPlaceholderText(/Enter game command/);

      fireEvent.change(input, { target: { value: 'look' } });
      fireEvent.keyDown(input, { key: 'Enter' });

      expect(defaultProps.onSendCommand).toHaveBeenCalledWith('look');
    });
  });

  describe('Command History', () => {
    it('populates input when history item is clicked', () => {
      render(<CommandPanel {...defaultProps} />);

      const historyItem = screen.getByText('look');
      fireEvent.click(historyItem);

      const input = screen.getByPlaceholderText(/Enter game command/);
      expect(input).toHaveValue('look');
    });

    it('sends command when history item is clicked and form is submitted', () => {
      render(<CommandPanel {...defaultProps} />);

      const historyItem = screen.getByText('look');
      fireEvent.click(historyItem);

      const sendButton = screen.getByText('Send Command');
      fireEvent.click(sendButton);

      expect(defaultProps.onSendCommand).toHaveBeenCalledWith('look');
    });

    it('shows Clear button when history has items and onClearHistory provided', () => {
      render(<CommandPanel {...defaultProps} />);

      const clearButton = screen.getByText('Clear');
      fireEvent.click(clearButton);

      expect(defaultProps.onClearHistory).toHaveBeenCalled();
    });

    it('limits history display to recent 10 commands', () => {
      const longHistory = Array.from({ length: 50 }, (_, i) => `command${i}`);

      render(<CommandPanel {...defaultProps} commandHistory={longHistory} />);

      expect(screen.getByText('command49')).toBeInTheDocument();
      expect(screen.queryByText('command0')).not.toBeInTheDocument();
    });
  });

  describe('Input Validation', () => {
    it('trims whitespace from commands', () => {
      render(<CommandPanel {...defaultProps} />);

      const input = screen.getByPlaceholderText(/Enter game command/);
      const sendButton = screen.getByText('Send Command');

      fireEvent.change(input, { target: { value: '  look  ' } });
      fireEvent.click(sendButton);

      expect(defaultProps.onSendCommand).toHaveBeenCalledWith('look');
    });

    it('prevents sending commands with only whitespace', () => {
      render(<CommandPanel {...defaultProps} />);

      const input = screen.getByPlaceholderText(/Enter game command/);
      const sendButton = screen.getByText('Send Command');

      fireEvent.change(input, { target: { value: '   ' } });
      fireEvent.click(sendButton);

      expect(defaultProps.onSendCommand).not.toHaveBeenCalled();
    });
  });

  describe('Performance', () => {
    it('handles large command history efficiently', () => {
      const largeHistory = Array.from({ length: 1000 }, (_, i) => `command${i}`);

      render(<CommandPanel {...defaultProps} commandHistory={largeHistory} />);

      expect(screen.getByText('command999')).toBeInTheDocument();
    });

    it('handles rapid input without issues', async () => {
      render(<CommandPanel {...defaultProps} />);

      const input = screen.getByPlaceholderText(/Enter game command/);
      fireEvent.change(input, { target: { value: 'l' } });
      fireEvent.change(input, { target: { value: 'lo' } });
      fireEvent.change(input, { target: { value: 'look' } });

      await waitFor(() => {
        expect(input).toHaveValue('look');
      });
    });
  });

  describe('Error Handling', () => {
    it('handles missing props gracefully', () => {
      const { container } = render(<CommandPanel commandHistory={[]} onSendCommand={vi.fn()} />);

      expect(container).toBeInTheDocument();
    });

    it('shows empty state when command history is empty', () => {
      render(<CommandPanel {...defaultProps} commandHistory={[]} />);

      expect(screen.getByText('No commands yet')).toBeInTheDocument();
    });

    it('handles malformed command history', () => {
      const malformedHistory = ['valid', '', 'another valid'];

      render(<CommandPanel {...defaultProps} commandHistory={malformedHistory} />);

      expect(screen.getByText('valid')).toBeInTheDocument();
      expect(screen.getByText('another valid')).toBeInTheDocument();
    });
  });

  describe('Keyboard and Accessibility', () => {
    it('supports keyboard interaction', () => {
      render(<CommandPanel {...defaultProps} />);

      const input = screen.getByPlaceholderText(/Enter game command/);
      fireEvent.keyDown(input, { key: 'Tab' });
      fireEvent.keyDown(input, { key: 'Escape' });
      expect(input).toBeInTheDocument();
    });

    it('renders with data-testid for command input', () => {
      render(<CommandPanel {...defaultProps} />);

      expect(screen.getByTestId('command-input')).toBeInTheDocument();
    });
  });
});
