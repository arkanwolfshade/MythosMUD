import { fireEvent, render, screen, waitFor } from '@testing-library/react';
import { beforeEach, describe, expect, it, vi } from 'vitest';
import { CommandPanelTest } from './CommandPanelTest';

// Mock all child components
vi.mock('./panels/CommandPanel', () => ({
  CommandPanel: ({
    commandHistory,
    onSendCommand,
    onClearHistory,
    placeholder,
  }: {
    commandHistory: string[];
    onSendCommand: (command: string) => void;
    onClearHistory: () => void;
    placeholder?: string;
  }) => (
    <div data-testid="command-panel">
      <div data-testid="command-count">{commandHistory.length} commands</div>
      <button onClick={() => onSendCommand('test command')} data-testid="send-command">
        Send Command
      </button>
      <button onClick={onClearHistory} data-testid="clear-history">
        Clear History
      </button>
      <input placeholder={placeholder} data-testid="command-input" />
    </div>
  ),
}));

vi.mock('./ui/EldritchIcon', () => ({
  EldritchIcon: ({ name, className }: { name: string; _size?: number; className?: string; _variant?: string }) => (
    <div data-testid={`eldritch-icon-${name}`} className={className}>
      {name}
    </div>
  ),
  MythosIcons: {
    move: 'move',
    eldritch: 'eldritch',
    search: 'search',
    clock: 'clock',
    clear: 'clear',
    help: 'help',
    stats: 'stats',
  },
}));

vi.mock('./ui/MythosPanel', () => ({
  MythosPanel: ({
    title,
    children,
    className,
  }: {
    title?: string;
    children: React.ReactNode;
    _variant?: string;
    _size?: string;
    className?: string;
  }) => (
    <div data-testid={`mythos-panel-${title?.toLowerCase().replace(/\s+/g, '-')}`} className={className}>
      {title && <h3 data-testid="panel-title">{title}</h3>}
      {children}
    </div>
  ),
}));

vi.mock('./ui/TerminalButton', () => ({
  TerminalButton: ({
    children,
    onClick,
    disabled,
    className,
  }: {
    children: React.ReactNode;
    onClick?: () => void;
    _variant?: string;
    _size?: string;
    disabled?: boolean;
    className?: string;
  }) => (
    <button onClick={onClick} disabled={disabled} className={className} data-testid="terminal-button">
      {children}
    </button>
  ),
}));

describe('CommandPanelTest', () => {
  beforeEach(() => {
    vi.clearAllMocks();
  });

  describe('Initial Rendering', () => {
    it('should render the main title and description', () => {
      render(<CommandPanelTest />);

      expect(screen.getByText('Enhanced Command Panel')).toBeInTheDocument();
      expect(screen.getByText(/Mythos-themed command interface/)).toBeInTheDocument();
    });

    it('should render panel sections', () => {
      render(<CommandPanelTest />);

      expect(screen.getByTestId('mythos-panel-command-interface')).toBeInTheDocument();
      expect(screen.getByTestId('mythos-panel-command-controls')).toBeInTheDocument();
      expect(screen.getByTestId('mythos-panel-command-statistics')).toBeInTheDocument();
      expect(screen.getByTestId('mythos-panel-command-categories')).toBeInTheDocument();
    });

    it('should render initial command history', () => {
      render(<CommandPanelTest />);

      // Check that the command panel shows the initial command count
      expect(screen.getByTestId('command-count')).toHaveTextContent('20 commands');
    });

    it('should show initial last command state', () => {
      render(<CommandPanelTest />);

      expect(screen.getByText('No command sent yet')).toBeInTheDocument();
    });

    it('should show initial command results state', () => {
      render(<CommandPanelTest />);

      expect(screen.getByText('No results yet')).toBeInTheDocument();
    });
  });

  describe('Command Functions', () => {
    it('should send command when send button is clicked', async () => {
      render(<CommandPanelTest />);

      const sendButton = screen.getByTestId('send-command');
      fireEvent.click(sendButton);

      await waitFor(() => {
        expect(screen.getByText('test command')).toBeInTheDocument();
      });

      // Command count should increase
      expect(screen.getByTestId('command-count')).toHaveTextContent('21 commands');
    });

    it('should clear history when clear button is clicked', async () => {
      render(<CommandPanelTest />);

      const clearButton = screen.getByTestId('clear-history');
      fireEvent.click(clearButton);

      await waitFor(() => {
        expect(screen.getByTestId('command-count')).toHaveTextContent('0 commands');
      });
    });

    it('should add sample commands when Add Sample button is clicked', async () => {
      render(<CommandPanelTest />);

      const addSampleButton = screen.getByText('Add Sample');
      fireEvent.click(addSampleButton);

      await waitFor(() => {
        expect(screen.getByTestId('command-count')).toHaveTextContent('28 commands');
      });
    });

    it('should add mythos commands when Add Mythos button is clicked', async () => {
      render(<CommandPanelTest />);

      const addMythosButton = screen.getByText('Add Mythos');
      fireEvent.click(addMythosButton);

      await waitFor(() => {
        expect(screen.getByTestId('command-count')).toHaveTextContent('28 commands');
      });
    });
  });

  describe('Statistics Display', () => {
    it('should display command statistics', () => {
      render(<CommandPanelTest />);

      expect(screen.getByText('Total Commands:')).toBeInTheDocument();
      expect(screen.getByText('20')).toBeInTheDocument(); // Total commands
      expect(screen.getByText('Look Commands:')).toBeInTheDocument();
      expect(screen.getByText('Movement Commands:')).toBeInTheDocument();
      expect(screen.getByText('Cast Commands:')).toBeInTheDocument();
      expect(screen.getByText('Communication:')).toBeInTheDocument();
      expect(screen.getByText('Eldritch Commands:')).toBeInTheDocument();
    });

    it('should calculate look commands correctly', () => {
      render(<CommandPanelTest />);

      // Should find 3 look commands in the initial history
      const lookCommandsElement = screen.getByText('Look Commands:').closest('div');
      expect(lookCommandsElement).toHaveTextContent('3');
    });

    it('should calculate movement commands correctly', () => {
      render(<CommandPanelTest />);

      // Should find 2 movement commands in the initial history (n, s)
      const movementCommandsElement = screen.getByText('Movement Commands:').closest('div');
      expect(movementCommandsElement).toHaveTextContent('2');
    });

    it('should calculate cast commands correctly', () => {
      render(<CommandPanelTest />);

      // Should find 2 cast commands in the initial history
      const castCommandsElement = screen.getByText('Cast Commands:').closest('div');
      expect(castCommandsElement).toHaveTextContent('2');
    });

    it('should calculate communication commands correctly', () => {
      render(<CommandPanelTest />);

      // Should find 3 communication commands in the initial history
      const communicationCommandsElement = screen.getByText('Communication:').closest('div');
      expect(communicationCommandsElement).toHaveTextContent('3');
    });
  });

  describe('Command Categories', () => {
    it('should display movement command categories', () => {
      render(<CommandPanelTest />);

      // Use getAllByText to get all Movement elements and check the first one
      const movementElements = screen.getAllByText('Movement');
      expect(movementElements[0]).toBeInTheDocument();
      expect(screen.getByText('n')).toBeInTheDocument();
      expect(screen.getByText('s')).toBeInTheDocument();
      expect(screen.getByText('e')).toBeInTheDocument();
      expect(screen.getByText('w')).toBeInTheDocument();
    });

    it('should display combat command categories', () => {
      render(<CommandPanelTest />);

      expect(screen.getByText('Combat')).toBeInTheDocument();
      expect(screen.getByText('attack')).toBeInTheDocument();
      expect(screen.getByText('defend')).toBeInTheDocument();
      expect(screen.getByText('flee')).toBeInTheDocument();
      expect(screen.getByText('cast')).toBeInTheDocument();
    });

    it('should display communication command categories', () => {
      render(<CommandPanelTest />);

      expect(screen.getByText('Communication')).toBeInTheDocument();
      expect(screen.getByText('say')).toBeInTheDocument();
      expect(screen.getByText('whisper')).toBeInTheDocument();
      expect(screen.getByText('shout')).toBeInTheDocument();
      expect(screen.getByText('tell')).toBeInTheDocument();
    });
  });

  describe('Features Showcase', () => {
    it('should display command features', () => {
      render(<CommandPanelTest />);

      expect(screen.getByText('Command Features')).toBeInTheDocument();
      expect(screen.getByText(/Auto-suggestions/)).toBeInTheDocument();
      expect(screen.getByText(/History Navigation/)).toBeInTheDocument();
      expect(screen.getByText(/Quick Commands/)).toBeInTheDocument();
      expect(screen.getByText(/History Management/)).toBeInTheDocument();
      expect(screen.getByText(/Help Integration/)).toBeInTheDocument();
      // Use a more specific selector for Command Statistics
      const commandStatsElement = screen.getByText('Command Statistics:');
      expect(commandStatsElement).toBeInTheDocument();
    });

    it('should display keyboard shortcuts', () => {
      render(<CommandPanelTest />);

      expect(screen.getByText('Keyboard Shortcuts')).toBeInTheDocument();
      expect(screen.getByText(/Navigate up in command history/)).toBeInTheDocument();
      expect(screen.getByText(/Navigate down in command history/)).toBeInTheDocument();
      expect(screen.getByText(/Auto-complete command/)).toBeInTheDocument();
      expect(screen.getByText(/Send command/)).toBeInTheDocument();
    });
  });

  describe('Command Examples', () => {
    it('should display basic command examples', () => {
      render(<CommandPanelTest />);

      expect(screen.getByText('Basic Commands')).toBeInTheDocument();
      expect(screen.getByText('> look')).toBeInTheDocument();
      expect(screen.getByText('Examine your surroundings')).toBeInTheDocument();
      expect(screen.getByText('> inventory')).toBeInTheDocument();
      expect(screen.getByText('Check your possessions')).toBeInTheDocument();
    });

    it('should display movement command examples', () => {
      render(<CommandPanelTest />);

      // Use getAllByText to get all Movement elements and check the second one (in examples section)
      const movementElements = screen.getAllByText('Movement');
      expect(movementElements[1]).toBeInTheDocument();
      expect(screen.getByText('> n')).toBeInTheDocument();
      expect(screen.getByText('Move north')).toBeInTheDocument();
      expect(screen.getByText('> s')).toBeInTheDocument();
      expect(screen.getByText('Move south')).toBeInTheDocument();
    });

    it('should display eldritch command examples', () => {
      render(<CommandPanelTest />);

      expect(screen.getByText('Eldritch Commands')).toBeInTheDocument();
      expect(screen.getByText('> cast eldritch sight')).toBeInTheDocument();
      expect(screen.getByText('See the unseen')).toBeInTheDocument();
      expect(screen.getByText('> read Necronomicon')).toBeInTheDocument();
      expect(screen.getByText('Study forbidden lore')).toBeInTheDocument();
    });
  });

  describe('State Management', () => {
    it('should update last command when command is sent', async () => {
      render(<CommandPanelTest />);

      const sendButton = screen.getByTestId('send-command');
      fireEvent.click(sendButton);

      await waitFor(() => {
        expect(screen.getByText('test command')).toBeInTheDocument();
      });
    });

    it('should update command results when command is sent', async () => {
      render(<CommandPanelTest />);

      const sendButton = screen.getByTestId('send-command');
      fireEvent.click(sendButton);

      await waitFor(() => {
        expect(screen.getByText('Command executed: test command')).toBeInTheDocument();
        expect(screen.getByText('Processing eldritch knowledge...')).toBeInTheDocument();
        expect(screen.getByText('The forbidden knowledge courses through your mind.')).toBeInTheDocument();
      });
    });

    it('should clear both history and results when clear is clicked', async () => {
      render(<CommandPanelTest />);

      // First send a command to have some history and results
      const sendButton = screen.getByTestId('send-command');
      fireEvent.click(sendButton);

      await waitFor(() => {
        expect(screen.getByTestId('command-count')).toHaveTextContent('21 commands');
      });

      // Then clear everything
      const clearButton = screen.getByTestId('clear-history');
      fireEvent.click(clearButton);

      await waitFor(() => {
        expect(screen.getByTestId('command-count')).toHaveTextContent('0 commands');
      });

      // Should show no results
      expect(screen.getByText('No results yet')).toBeInTheDocument();
    });
  });
});
