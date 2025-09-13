import { fireEvent, render, screen, waitFor } from '@testing-library/react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import { ChatMessage } from '../../stores/gameStore';
import { GameTerminal } from '../GameTerminal';

// Mock the debug logger
vi.mock('../../utils/debugLogger', () => ({
  debugLogger: vi.fn(() => ({
    debug: vi.fn(),
    info: vi.fn(),
    warn: vi.fn(),
    error: vi.fn(),
  })),
}));

// Mock the panel components
vi.mock('../panels/ChatPanel', () => ({
  ChatPanel: ({
    messages,
    onSendChatMessage,
    onClearMessages,
    onDownloadLogs,
    isConnected,
  }: {
    messages: ChatMessage[];
    onSendChatMessage: (message: string, channel: string) => void;
    onClearMessages?: () => void;
    onDownloadLogs?: () => void;
    isConnected?: boolean;
  }) => (
    <div data-testid="chat-panel">
      <div data-testid="chat-messages-count">{messages.length}</div>
      <button data-testid="send-chat" onClick={() => onSendChatMessage('test message', 'local')}>
        Send Chat
      </button>
      <button data-testid="clear-messages" onClick={onClearMessages}>
        Clear Messages
      </button>
      <button data-testid="download-logs" onClick={onDownloadLogs}>
        Download Logs
      </button>
      <div data-testid="chat-connected">{isConnected ? 'connected' : 'disconnected'}</div>
    </div>
  ),
}));

vi.mock('../panels/CommandPanel', () => ({
  CommandPanel: ({
    commandHistory,
    onSendCommand,
    onClearHistory,
    isConnected,
  }: {
    commandHistory: string[];
    onSendCommand: (command: string) => void;
    onClearHistory?: () => void;
    isConnected?: boolean;
  }) => (
    <div data-testid="command-panel">
      <div data-testid="command-history-count">{commandHistory.length}</div>
      <button data-testid="send-command" onClick={() => onSendCommand('look')}>
        Send Command
      </button>
      <button data-testid="clear-history" onClick={onClearHistory}>
        Clear History
      </button>
      <div data-testid="command-connected">{isConnected ? 'connected' : 'disconnected'}</div>
    </div>
  ),
}));

vi.mock('../panels/GameLogPanel', () => ({
  GameLogPanel: ({
    messages,
    onClearMessages,
    onDownloadLogs,
  }: {
    messages: ChatMessage[];
    onClearMessages?: () => void;
    onDownloadLogs?: () => void;
  }) => (
    <div data-testid="game-log-panel">
      <div data-testid="game-log-messages-count">{messages.length}</div>
      <button data-testid="game-log-clear" onClick={onClearMessages}>
        Clear Game Log
      </button>
      <button data-testid="game-log-download" onClick={onDownloadLogs}>
        Download Game Log
      </button>
    </div>
  ),
}));

vi.mock('../DraggablePanel', () => ({
  DraggablePanel: ({
    children,
    title,
    onClose,
    onMinimize,
    onMaximize,
  }: {
    children: React.ReactNode;
    title?: string;
    onClose?: () => void;
    onMinimize?: () => void;
    onMaximize?: () => void;
  }) => (
    <div data-testid={`draggable-panel-${title.toLowerCase().replace(' ', '-')}`}>
      <div data-testid="panel-title">{title}</div>
      <button data-testid="panel-close" onClick={onClose}>
        Close
      </button>
      <button data-testid="panel-minimize" onClick={onMinimize}>
        Minimize
      </button>
      <button data-testid="panel-maximize" onClick={onMaximize}>
        Maximize
      </button>
      {children}
    </div>
  ),
}));

vi.mock('../MotdContent', () => ({
  MotdContent: () => <div data-testid="motd-content">MOTD Content</div>,
}));

vi.mock('../RoomInfoPanel', () => ({
  RoomInfoPanel: ({ room, debugInfo }: { room?: { name?: string; description?: string }; debugInfo?: unknown }) => (
    <div data-testid="room-info-panel">
      <div data-testid="room-name">{room?.name || 'No Room'}</div>
      <div data-testid="room-description">{room?.description || 'No Description'}</div>
      <div data-testid="debug-info">{JSON.stringify(debugInfo)}</div>
    </div>
  ),
}));

describe('GameTerminal', () => {
  const defaultProps = {
    playerName: 'TestPlayer',
    isConnected: true,
    isConnecting: false,
    error: null,
    reconnectAttempts: 0,
    room: {
      id: 'room-1',
      name: 'Test Room',
      description: 'A test room for testing',
      exits: { north: 'room-2' },
      occupants: ['player-1'],
      occupant_count: 1,
      entities: [{ name: 'Test NPC', type: 'npc' }],
    },
    player: {
      name: 'TestPlayer',
      stats: {
        current_health: 100,
        sanity: 80,
        strength: 10,
        dexterity: 12,
        constitution: 14,
        intelligence: 16,
        wisdom: 13,
        charisma: 15,
      },
      level: 5,
    },
    messages: [
      {
        text: 'Welcome to the test room',
        timestamp: '2024-01-01T12:00:00Z',
        isHtml: false,
        messageType: 'system',
      },
    ],
    commandHistory: ['look', 'inventory', 'status'],
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

  afterEach(() => {
    vi.restoreAllMocks();
  });

  describe('Rendering', () => {
    it('should render all main components', () => {
      render(<GameTerminal {...defaultProps} />);

      expect(screen.getByTestId('chat-panel')).toBeInTheDocument();
      expect(screen.getByTestId('command-panel')).toBeInTheDocument();
      expect(screen.getByTestId('game-log-panel')).toBeInTheDocument();
      expect(screen.getByTestId('room-info-panel')).toBeInTheDocument();
    });

    it('should display connection status in header', () => {
      render(<GameTerminal {...defaultProps} />);

      expect(screen.getByText('Connected')).toBeInTheDocument();
      expect(screen.getByText('Player: TestPlayer')).toBeInTheDocument();
    });

    it('should display disconnected status when not connected', () => {
      render(<GameTerminal {...defaultProps} isConnected={false} isConnecting={false} />);

      expect(screen.getByText('Disconnected')).toBeInTheDocument();
    });

    it('should display connecting status when connecting', () => {
      render(<GameTerminal {...defaultProps} isConnected={false} isConnecting={true} />);

      expect(screen.getByText('Connecting...')).toBeInTheDocument();
    });

    it('should display error message when error exists', () => {
      const errorMessage = 'Connection failed';
      render(<GameTerminal {...defaultProps} error={errorMessage} />);

      expect(screen.getByText(errorMessage)).toBeInTheDocument();
    });

    it('should display reconnect attempts when greater than 0', () => {
      render(<GameTerminal {...defaultProps} reconnectAttempts={3} />);

      expect(screen.getByText('Reconnect: 3')).toBeInTheDocument();
    });

    it('should display player stats in status panel', () => {
      render(<GameTerminal {...defaultProps} />);

      expect(screen.getByText('Health:')).toBeInTheDocument();
      expect(screen.getByText('100')).toBeInTheDocument();
      expect(screen.getByText('Sanity:')).toBeInTheDocument();
      expect(screen.getByText('80')).toBeInTheDocument();
      expect(screen.getByText('STR:')).toBeInTheDocument();
      expect(screen.getByText('10')).toBeInTheDocument();
    });

    it('should display message and command counts in status panel', () => {
      render(<GameTerminal {...defaultProps} />);

      expect(screen.getByText('Messages:')).toBeInTheDocument();
      expect(screen.getByText('1')).toBeInTheDocument();
      expect(screen.getByText('Commands:')).toBeInTheDocument();
      expect(screen.getByText('3')).toBeInTheDocument();
    });
  });

  describe('MOTD Overlay', () => {
    it('should show MOTD overlay by default', () => {
      render(<GameTerminal {...defaultProps} />);

      expect(screen.getByTestId('motd-content')).toBeInTheDocument();
    });

    it('should hide MOTD overlay when continue button is clicked', async () => {
      render(<GameTerminal {...defaultProps} />);

      const continueButton = screen.getByText('Continue');
      fireEvent.click(continueButton);

      await waitFor(() => {
        expect(screen.queryByTestId('motd-content')).not.toBeInTheDocument();
      });
    });
  });

  describe('Panel Interactions', () => {
    it('should pass correct props to ChatPanel', () => {
      render(<GameTerminal {...defaultProps} />);

      const chatPanel = screen.getByTestId('chat-panel');
      expect(chatPanel).toBeInTheDocument();
      expect(screen.getByTestId('chat-messages-count')).toHaveTextContent('1');
      expect(screen.getByTestId('chat-connected')).toHaveTextContent('connected');
    });

    it('should pass correct props to CommandPanel', () => {
      render(<GameTerminal {...defaultProps} />);

      const commandPanel = screen.getByTestId('command-panel');
      expect(commandPanel).toBeInTheDocument();
      expect(screen.getByTestId('command-history-count')).toHaveTextContent('3');
      expect(screen.getByTestId('command-connected')).toHaveTextContent('connected');
    });

    it('should pass correct props to GameLogPanel', () => {
      render(<GameTerminal {...defaultProps} />);

      const gameLogPanel = screen.getByTestId('game-log-panel');
      expect(gameLogPanel).toBeInTheDocument();
      expect(screen.getByTestId('game-log-messages-count')).toHaveTextContent('1');
    });

    it('should pass correct props to RoomInfoPanel', () => {
      render(<GameTerminal {...defaultProps} />);

      expect(screen.getByTestId('room-name')).toHaveTextContent('Test Room');
      expect(screen.getByTestId('room-description')).toHaveTextContent('A test room for testing');
    });
  });

  describe('Event Handlers', () => {
    it('should call onSendChatMessage when chat message is sent', () => {
      render(<GameTerminal {...defaultProps} />);

      const sendChatButton = screen.getByTestId('send-chat');
      fireEvent.click(sendChatButton);

      expect(defaultProps.onSendChatMessage).toHaveBeenCalledWith('test message', 'local');
    });

    it('should call onSendCommand when command is sent', () => {
      render(<GameTerminal {...defaultProps} />);

      const sendCommandButton = screen.getByTestId('send-command');
      fireEvent.click(sendCommandButton);

      expect(defaultProps.onSendCommand).toHaveBeenCalledWith('look');
    });

    it('should call onClearMessages when clear messages is clicked', () => {
      render(<GameTerminal {...defaultProps} />);

      const clearMessagesButton = screen.getByTestId('clear-messages');
      fireEvent.click(clearMessagesButton);

      expect(defaultProps.onClearMessages).toHaveBeenCalled();
    });

    it('should call onClearHistory when clear history is clicked', () => {
      render(<GameTerminal {...defaultProps} />);

      const clearHistoryButton = screen.getByTestId('clear-history');
      fireEvent.click(clearHistoryButton);

      expect(defaultProps.onClearHistory).toHaveBeenCalled();
    });

    it('should call onDownloadLogs when download logs is clicked', () => {
      render(<GameTerminal {...defaultProps} />);

      const downloadLogsButton = screen.getByTestId('download-logs');
      fireEvent.click(downloadLogsButton);

      expect(defaultProps.onDownloadLogs).toHaveBeenCalled();
    });
  });

  describe('Responsive Layout', () => {
    it('should handle window resize events', () => {
      const { container } = render(<GameTerminal {...defaultProps} />);

      // Simulate window resize
      const resizeEvent = new Event('resize');
      window.dispatchEvent(resizeEvent);

      // Component should still be rendered
      expect(container.firstChild).toBeInTheDocument();
    });
  });

  describe('Edge Cases', () => {
    it('should handle null room gracefully', () => {
      render(<GameTerminal {...defaultProps} room={null} />);

      expect(screen.getByTestId('room-name')).toHaveTextContent('No Room');
      expect(screen.getByTestId('room-description')).toHaveTextContent('No Description');
    });

    it('should handle null player gracefully', () => {
      render(<GameTerminal {...defaultProps} player={null} />);

      // Should not display player stats
      expect(screen.queryByText('Health:')).not.toBeInTheDocument();
      expect(screen.queryByText('Sanity:')).not.toBeInTheDocument();
    });

    it('should handle empty messages array', () => {
      render(<GameTerminal {...defaultProps} messages={[]} />);

      expect(screen.getByTestId('chat-messages-count')).toHaveTextContent('0');
      expect(screen.getByTestId('game-log-messages-count')).toHaveTextContent('0');
    });

    it('should handle empty command history', () => {
      render(<GameTerminal {...defaultProps} commandHistory={[]} />);

      expect(screen.getByTestId('command-history-count')).toHaveTextContent('0');
    });

    it('should handle player without stats', () => {
      const playerWithoutStats = { name: 'TestPlayer', level: 5 };
      render(<GameTerminal {...defaultProps} player={playerWithoutStats} />);

      // Should not display stats section
      expect(screen.queryByText('Health:')).not.toBeInTheDocument();
      expect(screen.queryByText('Sanity:')).not.toBeInTheDocument();
    });
  });

  describe('DraggablePanel Integration', () => {
    it('should render all draggable panels with correct titles', () => {
      render(<GameTerminal {...defaultProps} />);

      expect(screen.getByTestId('draggable-panel-chat')).toBeInTheDocument();
      expect(screen.getByTestId('draggable-panel-game-log')).toBeInTheDocument();
      expect(screen.getByTestId('draggable-panel-commands')).toBeInTheDocument();
      expect(screen.getByTestId('draggable-panel-room-info')).toBeInTheDocument();
      expect(screen.getByTestId('draggable-panel-status')).toBeInTheDocument();
    });

    it('should handle panel close events', () => {
      render(<GameTerminal {...defaultProps} />);

      const closeButton = screen.getByTestId('panel-close');
      fireEvent.click(closeButton);

      // Should not throw error
      expect(closeButton).toBeInTheDocument();
    });

    it('should handle panel minimize events', () => {
      render(<GameTerminal {...defaultProps} />);

      const minimizeButton = screen.getByTestId('panel-minimize');
      fireEvent.click(minimizeButton);

      // Should not throw error
      expect(minimizeButton).toBeInTheDocument();
    });

    it('should handle panel maximize events', () => {
      render(<GameTerminal {...defaultProps} />);

      const maximizeButton = screen.getByTestId('panel-maximize');
      fireEvent.click(maximizeButton);

      // Should not throw error
      expect(maximizeButton).toBeInTheDocument();
    });
  });
});
