import { render, screen } from '@testing-library/react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import { GameTerminalContainer } from '../GameTerminalContainer';

// Mock the useGameTerminal hook
vi.mock('../../hooks/useGameTerminal', () => ({
  useGameTerminal: vi.fn(() => ({
    // Connection state
    isConnected: true,
    isConnecting: false,
    error: null,
    reconnectAttempts: 0,

    // Session state
    playerName: 'TestPlayer',
    characterName: 'TestCharacter',
    isAuthenticated: true,
    hasCharacter: true,

    // Game state
    player: {
      id: 'player-1',
      name: 'TestPlayer',
      stats: { current_health: 100, sanity: 80 },
      level: 5,
    },
    room: {
      id: 'room-1',
      name: 'Test Room',
      description: 'A test room',
      exits: { north: 'room-2' },
      occupants: ['player-1'],
      occupant_count: 1,
      entities: [{ name: 'Test NPC', type: 'npc' }],
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

    // Event handlers
    onSendCommand: vi.fn(),
    onSendChatMessage: vi.fn(),
    onClearMessages: vi.fn(),
    onClearHistory: vi.fn(),
    onDownloadLogs: vi.fn(),
  })),
}));

// Mock the presentation component
vi.mock('../GameTerminalPresentation', () => ({
  GameTerminalPresentation: ({ playerName, isConnected, messages, commandHistory, ...props }: any) => (
    <div data-testid="game-terminal-presentation">
      <div data-testid="player-name">{playerName}</div>
      <div data-testid="connection-status">{isConnected ? 'connected' : 'disconnected'}</div>
      <div data-testid="messages-count">{messages.length}</div>
      <div data-testid="command-history-count">{commandHistory.length}</div>
      <button data-testid="send-command" onClick={() => props.onSendCommand('look')}>
        Send Command
      </button>
      <button data-testid="send-chat" onClick={() => props.onSendChatMessage('hello', 'local')}>
        Send Chat
      </button>
      <button data-testid="clear-messages" onClick={props.onClearMessages}>
        Clear Messages
      </button>
      <button data-testid="clear-history" onClick={props.onClearHistory}>
        Clear History
      </button>
      <button data-testid="download-logs" onClick={props.onDownloadLogs}>
        Download Logs
      </button>
    </div>
  ),
}));

describe('GameTerminalContainer', () => {
  const mockUseGameTerminal = vi.mocked(require('../../hooks/useGameTerminal').useGameTerminal);

  beforeEach(() => {
    vi.clearAllMocks();
  });

  afterEach(() => {
    vi.restoreAllMocks();
  });

  describe('Rendering', () => {
    it('should render the presentation component', () => {
      render(<GameTerminalContainer />);

      expect(screen.getByTestId('game-terminal-presentation')).toBeInTheDocument();
    });

    it('should pass all state from useGameTerminal to presentation', () => {
      render(<GameTerminalContainer />);

      expect(screen.getByTestId('player-name')).toHaveTextContent('TestPlayer');
      expect(screen.getByTestId('connection-status')).toHaveTextContent('connected');
      expect(screen.getByTestId('messages-count')).toHaveTextContent('1');
      expect(screen.getByTestId('command-history-count')).toHaveTextContent('3');
    });

    it('should call useGameTerminal hook', () => {
      render(<GameTerminalContainer />);

      expect(mockUseGameTerminal).toHaveBeenCalledTimes(1);
    });
  });

  describe('State Updates', () => {
    it('should re-render when useGameTerminal returns new state', () => {
      const { rerender } = render(<GameTerminalContainer />);

      expect(screen.getByTestId('player-name')).toHaveTextContent('TestPlayer');

      // Mock updated state
      mockUseGameTerminal.mockReturnValue({
        // Connection state
        isConnected: false,
        isConnecting: true,
        error: 'Connection failed',
        reconnectAttempts: 3,

        // Session state
        playerName: 'NewPlayer',
        characterName: 'NewCharacter',
        isAuthenticated: true,
        hasCharacter: true,

        // Game state
        player: null,
        room: null,
        messages: [],
        commandHistory: [],

        // Event handlers
        onSendCommand: vi.fn(),
        onSendChatMessage: vi.fn(),
        onClearMessages: vi.fn(),
        onClearHistory: vi.fn(),
        onDownloadLogs: vi.fn(),
      });

      rerender(<GameTerminalContainer />);

      expect(screen.getByTestId('player-name')).toHaveTextContent('NewPlayer');
      expect(screen.getByTestId('connection-status')).toHaveTextContent('disconnected');
      expect(screen.getByTestId('messages-count')).toHaveTextContent('0');
      expect(screen.getByTestId('command-history-count')).toHaveTextContent('0');
    });
  });

  describe('Event Handling', () => {
    it('should pass event handlers from useGameTerminal to presentation', () => {
      const mockOnSendCommand = vi.fn();
      const mockOnSendChatMessage = vi.fn();
      const mockOnClearMessages = vi.fn();
      const mockOnClearHistory = vi.fn();
      const mockOnDownloadLogs = vi.fn();

      mockUseGameTerminal.mockReturnValue({
        // Connection state
        isConnected: true,
        isConnecting: false,
        error: null,
        reconnectAttempts: 0,

        // Session state
        playerName: 'TestPlayer',
        characterName: 'TestCharacter',
        isAuthenticated: true,
        hasCharacter: true,

        // Game state
        player: {
          id: 'player-1',
          name: 'TestPlayer',
          stats: { current_health: 100, sanity: 80 },
          level: 5,
        },
        room: {
          id: 'room-1',
          name: 'Test Room',
          description: 'A test room',
          exits: { north: 'room-2' },
          occupants: ['player-1'],
          occupant_count: 1,
          entities: [{ name: 'Test NPC', type: 'npc' }],
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

        // Event handlers
        onSendCommand: mockOnSendCommand,
        onSendChatMessage: mockOnSendChatMessage,
        onClearMessages: mockOnClearMessages,
        onClearHistory: mockOnClearHistory,
        onDownloadLogs: mockOnDownloadLogs,
      });

      render(<GameTerminalContainer />);

      // Test event handlers
      screen.getByTestId('send-command').click();
      expect(mockOnSendCommand).toHaveBeenCalledWith('look');

      screen.getByTestId('send-chat').click();
      expect(mockOnSendChatMessage).toHaveBeenCalledWith('hello', 'local');

      screen.getByTestId('clear-messages').click();
      expect(mockOnClearMessages).toHaveBeenCalled();

      screen.getByTestId('clear-history').click();
      expect(mockOnClearHistory).toHaveBeenCalled();

      screen.getByTestId('download-logs').click();
      expect(mockOnDownloadLogs).toHaveBeenCalled();
    });
  });

  describe('Error Handling', () => {
    it('should handle useGameTerminal throwing an error', () => {
      mockUseGameTerminal.mockImplementation(() => {
        throw new Error('Hook error');
      });

      expect(() => {
        render(<GameTerminalContainer />);
      }).toThrow('Hook error');
    });

    it('should handle useGameTerminal returning undefined', () => {
      mockUseGameTerminal.mockReturnValue(undefined);

      expect(() => {
        render(<GameTerminalContainer />);
      }).toThrow();
    });
  });

  describe('Performance', () => {
    it('should not re-render unnecessarily', () => {
      const { rerender } = render(<GameTerminalContainer />);

      const initialCallCount = mockUseGameTerminal.mock.calls.length;

      // Re-render with same props
      rerender(<GameTerminalContainer />);

      // Hook should only be called once (on mount)
      expect(mockUseGameTerminal).toHaveBeenCalledTimes(initialCallCount);
    });
  });
});
