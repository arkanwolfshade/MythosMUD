import { fireEvent, render, screen } from '@testing-library/react';
import React from 'react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import { useGameTerminal } from '../../hooks/useGameTerminal';
import {
  GameTerminalProvider,
  useConnectionState,
  useGameActions,
  useGameState,
  useGameTerminalContext,
  useSessionState,
} from '../GameTerminalContext';

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

// Test component that uses the context
const TestComponent: React.FC = () => {
  const context = useGameTerminalContext();

  return (
    <div>
      <div data-testid="player-name">{context.playerName}</div>
      <div data-testid="is-connected">{context.isConnected ? 'connected' : 'disconnected'}</div>
      <div data-testid="messages-count">{context.messages.length}</div>
      <button data-testid="send-command" onClick={() => context.onSendCommand('look')}>
        Send Command
      </button>
    </div>
  );
};

// Test component for connection state
const ConnectionTestComponent: React.FC = () => {
  const connectionState = useConnectionState();

  return (
    <div>
      <div data-testid="connection-status">{connectionState.isConnected ? 'connected' : 'disconnected'}</div>
      <div data-testid="connection-error">{connectionState.error || 'no error'}</div>
    </div>
  );
};

// Test component for session state
const SessionTestComponent: React.FC = () => {
  const sessionState = useSessionState();

  return (
    <div>
      <div data-testid="session-player-name">{sessionState.playerName}</div>
      <div data-testid="session-character-name">{sessionState.characterName}</div>
      <div data-testid="session-authenticated">
        {sessionState.isAuthenticated ? 'authenticated' : 'not authenticated'}
      </div>
    </div>
  );
};

// Test component for game state
const GameStateTestComponent: React.FC = () => {
  const gameState = useGameState();

  return (
    <div>
      <div data-testid="game-player-name">{gameState.player?.name || 'no player'}</div>
      <div data-testid="game-room-name">{gameState.room?.name || 'no room'}</div>
      <div data-testid="game-messages-count">{gameState.messages.length}</div>
      <div data-testid="game-commands-count">{gameState.commandHistory.length}</div>
    </div>
  );
};

// Test component for game actions
const GameActionsTestComponent: React.FC = () => {
  const gameActions = useGameActions();

  return (
    <div>
      <button data-testid="action-send-command" onClick={() => gameActions.onSendCommand('look')}>
        Send Command
      </button>
      <button data-testid="action-send-chat" onClick={() => gameActions.onSendChatMessage('hello', 'local')}>
        Send Chat
      </button>
      <button data-testid="action-clear-messages" onClick={gameActions.onClearMessages}>
        Clear Messages
      </button>
      <button data-testid="action-clear-history" onClick={gameActions.onClearHistory}>
        Clear History
      </button>
      <button data-testid="action-download-logs" onClick={gameActions.onDownloadLogs}>
        Download Logs
      </button>
    </div>
  );
};

// Error boundary component
const ErrorBoundary: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  try {
    return <>{children}</>;
  } catch (error) {
    return <div data-testid="error-boundary">{(error as Error).message}</div>;
  }
};

describe('GameTerminalContext', () => {
  let mockUseGameTerminal: ReturnType<typeof vi.mocked<typeof useGameTerminal>>;

  beforeEach(() => {
    vi.clearAllMocks();
    mockUseGameTerminal = vi.mocked(useGameTerminal);
  });

  afterEach(() => {
    vi.restoreAllMocks();
  });

  describe('GameTerminalProvider', () => {
    it('should provide context to child components', () => {
      render(
        <GameTerminalProvider>
          <TestComponent />
        </GameTerminalProvider>
      );

      expect(screen.getByTestId('player-name')).toHaveTextContent('TestPlayer');
      expect(screen.getByTestId('is-connected')).toHaveTextContent('connected');
      expect(screen.getByTestId('messages-count')).toHaveTextContent('1');
    });

    it('should call useGameTerminal hook', () => {
      render(
        <GameTerminalProvider>
          <TestComponent />
        </GameTerminalProvider>
      );

      expect(mockUseGameTerminal).toHaveBeenCalledTimes(1);
    });

    it('should handle context updates', () => {
      const { rerender } = render(
        <GameTerminalProvider>
          <TestComponent />
        </GameTerminalProvider>
      );

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

      rerender(
        <GameTerminalProvider>
          <TestComponent />
        </GameTerminalProvider>
      );

      expect(screen.getByTestId('player-name')).toHaveTextContent('NewPlayer');
      expect(screen.getByTestId('is-connected')).toHaveTextContent('disconnected');
      expect(screen.getByTestId('messages-count')).toHaveTextContent('0');
    });
  });

  describe('useGameTerminalContext', () => {
    it('should return the full context', () => {
      render(
        <GameTerminalProvider>
          <TestComponent />
        </GameTerminalProvider>
      );

      expect(screen.getByTestId('player-name')).toHaveTextContent('TestPlayer');
      expect(screen.getByTestId('is-connected')).toHaveTextContent('connected');
    });

    it('should throw error when used outside provider', () => {
      expect(() => {
        render(
          <ErrorBoundary>
            <TestComponent />
          </ErrorBoundary>
        );
      }).toThrow('useGameTerminalContext must be used within a GameTerminalProvider');
    });
  });

  describe('useConnectionState', () => {
    it('should return connection state', () => {
      render(
        <GameTerminalProvider>
          <ConnectionTestComponent />
        </GameTerminalProvider>
      );

      expect(screen.getByTestId('connection-status')).toHaveTextContent('connected');
      expect(screen.getByTestId('connection-error')).toHaveTextContent('no error');
    });

    it('should throw error when used outside provider', () => {
      expect(() => {
        render(
          <ErrorBoundary>
            <ConnectionTestComponent />
          </ErrorBoundary>
        );
      }).toThrow('useGameTerminalContext must be used within a GameTerminalProvider');
    });
  });

  describe('useSessionState', () => {
    it('should return session state', () => {
      render(
        <GameTerminalProvider>
          <SessionTestComponent />
        </GameTerminalProvider>
      );

      expect(screen.getByTestId('session-player-name')).toHaveTextContent('TestPlayer');
      expect(screen.getByTestId('session-character-name')).toHaveTextContent('TestCharacter');
      expect(screen.getByTestId('session-authenticated')).toHaveTextContent('authenticated');
    });

    it('should throw error when used outside provider', () => {
      expect(() => {
        render(
          <ErrorBoundary>
            <SessionTestComponent />
          </ErrorBoundary>
        );
      }).toThrow('useGameTerminalContext must be used within a GameTerminalProvider');
    });
  });

  describe('useGameState', () => {
    it('should return game state', () => {
      render(
        <GameTerminalProvider>
          <GameStateTestComponent />
        </GameTerminalProvider>
      );

      expect(screen.getByTestId('game-player-name')).toHaveTextContent('TestPlayer');
      expect(screen.getByTestId('game-room-name')).toHaveTextContent('Test Room');
      expect(screen.getByTestId('game-messages-count')).toHaveTextContent('1');
      expect(screen.getByTestId('game-commands-count')).toHaveTextContent('3');
    });

    it('should throw error when used outside provider', () => {
      expect(() => {
        render(
          <ErrorBoundary>
            <GameStateTestComponent />
          </ErrorBoundary>
        );
      }).toThrow('useGameTerminalContext must be used within a GameTerminalProvider');
    });
  });

  describe('useGameActions', () => {
    it('should return game actions', () => {
      render(
        <GameTerminalProvider>
          <GameActionsTestComponent />
        </GameTerminalProvider>
      );

      expect(screen.getByTestId('action-send-command')).toBeInTheDocument();
      expect(screen.getByTestId('action-send-chat')).toBeInTheDocument();
      expect(screen.getByTestId('action-clear-messages')).toBeInTheDocument();
      expect(screen.getByTestId('action-clear-history')).toBeInTheDocument();
      expect(screen.getByTestId('action-download-logs')).toBeInTheDocument();
    });

    it('should call action handlers when buttons are clicked', () => {
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

      render(
        <GameTerminalProvider>
          <GameActionsTestComponent />
        </GameTerminalProvider>
      );

      // Test action handlers
      fireEvent.click(screen.getByTestId('action-send-command'));
      expect(mockOnSendCommand).toHaveBeenCalledWith('look');

      fireEvent.click(screen.getByTestId('action-send-chat'));
      expect(mockOnSendChatMessage).toHaveBeenCalledWith('hello', 'local');

      fireEvent.click(screen.getByTestId('action-clear-messages'));
      expect(mockOnClearMessages).toHaveBeenCalled();

      fireEvent.click(screen.getByTestId('action-clear-history'));
      expect(mockOnClearHistory).toHaveBeenCalled();

      fireEvent.click(screen.getByTestId('action-download-logs'));
      expect(mockOnDownloadLogs).toHaveBeenCalled();
    });

    it('should throw error when used outside provider', () => {
      expect(() => {
        render(
          <ErrorBoundary>
            <GameActionsTestComponent />
          </ErrorBoundary>
        );
      }).toThrow('useGameTerminalContext must be used within a GameTerminalProvider');
    });
  });

  describe('Error Handling', () => {
    it('should handle useGameTerminal throwing an error', () => {
      mockUseGameTerminal.mockImplementation(() => {
        throw new Error('Hook error');
      });

      expect(() => {
        render(
          <GameTerminalProvider>
            <TestComponent />
          </GameTerminalProvider>
        );
      }).toThrow('Hook error');
    });
  });
});
