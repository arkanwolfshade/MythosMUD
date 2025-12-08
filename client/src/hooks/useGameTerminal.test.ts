/* eslint-disable @typescript-eslint/no-explicit-any */
import { renderHook } from '@testing-library/react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import { useCommandStore, useConnectionStore, useGameStore, useSessionStore } from '../stores';
import { useGameTerminal } from './useGameTerminal';

// Mock the stores
vi.mock('../stores', () => ({
  useConnectionStore: vi.fn(() => ({
    isFullyConnected: vi.fn().mockReturnValue(true),
    isConnecting: false,
    error: null,
    reconnectAttempts: 0,
    sessionId: 'test-session',
    websocketConnected: true,
    connectionHealth: 'connected' as const,
    hasAnyConnection: vi.fn().mockReturnValue(true),
    getConnectionInfo: vi.fn().mockReturnValue({
      sessionId: 'test-session',
      websocketConnected: true,
      connectionHealth: 'connected' as const,
    }),
  })),
  useGameStore: vi.fn(() => ({
    player: {
      id: 'player-1',
      name: 'TestPlayer',
      stats: { current_health: 100, lucidity: 80 },
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
    chatMessages: [
      {
        text: 'Welcome to the test room',
        timestamp: '2024-01-01T12:00:00Z',
        isHtml: false,
        type: 'system',
        channel: 'game',
        sender: 'System',
      },
    ],
    gameLog: [],
  })),
  useSessionStore: vi.fn(() => ({
    playerName: 'TestPlayer',
    characterName: 'TestCharacter',
    isAuthenticated: true,
    hasCharacter: true,
  })),
  useCommandStore: vi.fn(() => ({
    commandHistory: [
      { command: 'look', timestamp: Date.now(), success: true },
      { command: 'inventory', timestamp: Date.now(), success: true },
      { command: 'status', timestamp: Date.now(), success: true },
    ],
    currentCommand: '',
    isExecuting: false,
  })),
}));

describe('useGameTerminal', () => {
  beforeEach(() => {
    vi.clearAllMocks();
  });

  afterEach(() => {
    vi.restoreAllMocks();
  });

  describe('Initial State', () => {
    it('should return initial state with all required properties', () => {
      const { result } = renderHook(() => useGameTerminal());

      expect(result.current).toHaveProperty('playerName');
      expect(result.current).toHaveProperty('isConnected');
      expect(result.current).toHaveProperty('isConnecting');
      expect(result.current).toHaveProperty('error');
      expect(result.current).toHaveProperty('reconnectAttempts');
      expect(result.current).toHaveProperty('room');
      expect(result.current).toHaveProperty('player');
      expect(result.current).toHaveProperty('messages');
      expect(result.current).toHaveProperty('commandHistory');
      expect(result.current).toHaveProperty('onSendCommand');
      expect(result.current).toHaveProperty('onSendChatMessage');
      expect(result.current).toHaveProperty('onClearMessages');
      expect(result.current).toHaveProperty('onClearHistory');
      expect(result.current).toHaveProperty('onDownloadLogs');
    });

    it('should return correct initial values', () => {
      const { result } = renderHook(() => useGameTerminal());

      expect(result.current.playerName).toBe('TestPlayer');
      expect(result.current.isConnected).toBe(true);
      expect(result.current.isConnecting).toBe(false);
      expect(result.current.error).toBe(null);
      expect(result.current.reconnectAttempts).toBe(0);
      expect(result.current.room).toEqual({
        id: 'room-1',
        name: 'Test Room',
        description: 'A test room',
        exits: { north: 'room-2' },
        occupants: ['player-1'],
        occupant_count: 1,
        entities: [{ name: 'Test NPC', type: 'npc' }],
      });
      expect(result.current.player).toEqual({
        id: 'player-1',
        name: 'TestPlayer',
        stats: { current_health: 100, lucidity: 80 },
        level: 5,
      });
      expect(result.current.messages).toHaveLength(1);
      expect(result.current.commandHistory).toHaveLength(3);
    });
  });

  describe('Event Handlers', () => {
    it('should provide onSendCommand handler', () => {
      const { result } = renderHook(() => useGameTerminal());

      expect(typeof result.current.onSendCommand).toBe('function');
    });

    it('should provide onSendChatMessage handler', () => {
      const { result } = renderHook(() => useGameTerminal());

      expect(typeof result.current.onSendChatMessage).toBe('function');
    });

    it('should provide onClearMessages handler', () => {
      const { result } = renderHook(() => useGameTerminal());

      expect(typeof result.current.onClearMessages).toBe('function');
    });

    it('should provide onClearHistory handler', () => {
      const { result } = renderHook(() => useGameTerminal());

      expect(typeof result.current.onClearHistory).toBe('function');
    });

    it('should provide onDownloadLogs handler', () => {
      const { result } = renderHook(() => useGameTerminal());

      expect(typeof result.current.onDownloadLogs).toBe('function');
    });
  });

  describe('State Updates', () => {
    it('should update when connection state changes', () => {
      const { result, rerender } = renderHook(() => useGameTerminal());

      expect(result.current.isConnected).toBe(true);

      // Mock updated connection state
      vi.mocked(useConnectionStore).mockReturnValue({
        isFullyConnected: vi.fn().mockReturnValue(false),
        isConnecting: true,
        error: 'Connection failed',
        reconnectAttempts: 3,
        sessionId: null,
        websocketConnected: false,
        connectionHealth: 'disconnected' as const,
        hasAnyConnection: vi.fn().mockReturnValue(false),
        getConnectionInfo: vi.fn().mockReturnValue({
          sessionId: null,
          websocketConnected: false,
          connectionHealth: 'disconnected' as const,
        }),
      });

      rerender();

      expect(result.current.isConnected).toBe(false);
      expect(result.current.isConnecting).toBe(true);
      expect(result.current.error).toBe('Connection failed');
      expect(result.current.reconnectAttempts).toBe(3);
    });

    it('should update when game state changes', () => {
      const { result, rerender } = renderHook(() => useGameTerminal());

      expect(result.current.player?.stats.current_health).toBe(100);

      // Mock updated game state
      vi.mocked(useGameStore).mockReturnValue({
        player: {
          id: 'player-1',
          name: 'TestPlayer',
          stats: { current_health: 80, lucidity: 60 },
          level: 5,
        },
        room: result.current.room,
        chatMessages: result.current.messages,
        gameLog: [],
      });

      rerender();

      expect(result.current.player?.stats.current_health).toBe(80);
      expect(result.current.player?.stats.lucidity).toBe(60);
    });

    it('should update when session state changes', () => {
      const { result, rerender } = renderHook(() => useGameTerminal());

      expect(result.current.playerName).toBe('TestPlayer');

      // Mock updated session state
      vi.mocked(useSessionStore).mockReturnValue({
        playerName: 'NewPlayer',
        characterName: 'NewCharacter',
        isAuthenticated: true,
        hasCharacter: true,
      });

      rerender();

      expect(result.current.playerName).toBe('NewPlayer');
    });

    it('should update when command state changes', () => {
      const { result, rerender } = renderHook(() => useGameTerminal());

      expect(result.current.commandHistory).toHaveLength(3);

      // Mock updated command state
      vi.mocked(useCommandStore).mockReturnValue({
        commandHistory: [
          { command: 'look', timestamp: Date.now(), success: true },
          { command: 'inventory', timestamp: Date.now(), success: true },
          { command: 'status', timestamp: Date.now(), success: true },
          { command: 'go north', timestamp: Date.now(), success: true },
        ],
        currentCommand: 'go north',
        isExecuting: true,
      });

      rerender();

      expect(result.current.commandHistory).toHaveLength(4);
    });
  });

  describe('Data Transformation', () => {
    it('should transform chat messages correctly', () => {
      const { result } = renderHook(() => useGameTerminal());

      expect(result.current.messages).toHaveLength(1);
      expect(result.current.messages[0]).toEqual({
        text: 'Welcome to the test room',
        timestamp: '2024-01-01T12:00:00Z',
        isHtml: false,
        messageType: 'system',
      });
    });

    it('should transform command history correctly', () => {
      const { result } = renderHook(() => useGameTerminal());

      expect(result.current.commandHistory).toHaveLength(3);
      expect(result.current.commandHistory[0]).toBe('look');
      expect(result.current.commandHistory[1]).toBe('inventory');
      expect(result.current.commandHistory[2]).toBe('status');
    });

    it('should handle empty data gracefully', () => {
      // Mock empty states
      vi.mocked(useGameStore).mockReturnValue({
        player: null,
        room: null,
        chatMessages: [],
        gameLog: [],
      });

      vi.mocked(useCommandStore).mockReturnValue({
        commandHistory: [],
        currentCommand: '',
        isExecuting: false,
      });

      const { result } = renderHook(() => useGameTerminal());

      expect(result.current.player).toBe(null);
      expect(result.current.room).toBe(null);
      expect(result.current.messages).toEqual([]);
      expect(result.current.commandHistory).toEqual([]);
    });
  });

  describe('Error Handling', () => {
    it('should handle store errors gracefully', () => {
      // Mock store throwing error
      vi.mocked(useConnectionStore).mockImplementation(() => {
        throw new Error('Store error');
      });

      expect(() => {
        renderHook(() => useGameTerminal());
      }).toThrow('Store error');

      // Restore default mock implementation
      vi.mocked(useConnectionStore).mockImplementation(() => ({
        isFullyConnected: vi.fn().mockReturnValue(true),
        isConnecting: false,
        error: null,
        reconnectAttempts: 0,
        sessionId: 'test-session',
        websocketConnected: true,
        connectionHealth: 'connected' as const,
        hasAnyConnection: vi.fn().mockReturnValue(true),
        getConnectionInfo: vi.fn().mockReturnValue({
          sessionId: 'test-session',
          websocketConnected: true,
          connectionHealth: 'connected' as const,
        }),
      }));
    });

    it('should handle missing store data gracefully', () => {
      // Mock undefined store return
      vi.mocked(useGameStore).mockReturnValue(undefined);

      expect(() => {
        renderHook(() => useGameTerminal());
      }).toThrow();

      // Restore default mock implementation
      vi.mocked(useGameStore).mockImplementation(() => ({
        player: {
          id: 'player-1',
          name: 'TestPlayer',
          stats: { current_health: 100, lucidity: 80 },
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
        chatMessages: [
          {
            text: 'Welcome to the test room',
            timestamp: '2024-01-01T12:00:00Z',
            isHtml: false,
            type: 'system',
            channel: 'game',
            sender: 'System',
          },
        ],
        gameLog: [],
      }));
    });
  });

  describe('Callback Execution', () => {
    it('should execute onSendCommand callback', () => {
      const mockExecuteCommand = vi.fn();
      vi.mocked(useConnectionStore).mockReturnValue({
        isFullyConnected: vi.fn().mockReturnValue(true),
        isConnecting: false,
        error: null,
        reconnectAttempts: 0,
        sessionId: 'test-session',
        websocketConnected: true,
        connectionHealth: 'connected' as const,
        hasAnyConnection: vi.fn().mockReturnValue(true),
        getConnectionInfo: vi.fn().mockReturnValue({
          sessionId: 'test-session',
          websocketConnected: true,
          connectionHealth: 'connected' as const,
        }),
      } as any);
      vi.mocked(useGameStore).mockReturnValue({
        player: null,
        room: null,
        chatMessages: [],
        gameLog: [],
      } as any);
      vi.mocked(useSessionStore).mockReturnValue({
        playerName: 'TestPlayer',
        characterName: 'TestCharacter',
        isAuthenticated: true,
        hasCharacter: true,
      } as any);
      vi.mocked(useCommandStore).mockReturnValue({
        commandHistory: [],
        currentCommand: '',
        isExecuting: false,
        executeCommand: mockExecuteCommand,
        clearHistory: vi.fn(),
      } as any);

      const { result } = renderHook(() => useGameTerminal());

      result.current.onSendCommand('look around');

      expect(mockExecuteCommand).toHaveBeenCalledWith('look around');
    });

    it('should execute onSendChatMessage callback', () => {
      const mockAddGameLogEntry = vi.fn();
      vi.mocked(useConnectionStore).mockReturnValue({
        isFullyConnected: vi.fn().mockReturnValue(true),
        isConnecting: false,
        error: null,
        reconnectAttempts: 0,
        sessionId: 'test-session',
        websocketConnected: true,
        connectionHealth: 'connected' as const,
        hasAnyConnection: vi.fn().mockReturnValue(true),
        getConnectionInfo: vi.fn().mockReturnValue({
          sessionId: 'test-session',
          websocketConnected: true,
          connectionHealth: 'connected' as const,
        }),
      } as any);
      vi.mocked(useGameStore).mockReturnValue({
        player: null,
        room: null,
        chatMessages: [],
        gameLog: [],
        addGameLogEntry: mockAddGameLogEntry,
        clearChatMessages: vi.fn(),
      } as any);

      vi.mocked(useSessionStore).mockReturnValue({
        playerName: 'TestPlayer',
        characterName: 'TestCharacter',
        isAuthenticated: true,
        hasCharacter: true,
      } as any);

      const { result } = renderHook(() => useGameTerminal());

      result.current.onSendChatMessage('Hello everyone', 'local');

      expect(mockAddGameLogEntry).toHaveBeenCalledWith(
        expect.objectContaining({
          text: 'Hello everyone',
          channel: 'local',
          sender: 'TestCharacter',
        })
      );
    });

    it('should use playerName when characterName is not available', () => {
      const mockAddGameLogEntry = vi.fn();
      vi.mocked(useConnectionStore).mockReturnValue({
        isFullyConnected: vi.fn().mockReturnValue(true),
        isConnecting: false,
        error: null,
        reconnectAttempts: 0,
        sessionId: 'test-session',
        websocketConnected: true,
        connectionHealth: 'connected' as const,
        hasAnyConnection: vi.fn().mockReturnValue(true),
        getConnectionInfo: vi.fn().mockReturnValue({
          sessionId: 'test-session',
          websocketConnected: true,
          connectionHealth: 'connected' as const,
        }),
      } as any);
      vi.mocked(useGameStore).mockReturnValue({
        player: null,
        room: null,
        chatMessages: [],
        gameLog: [],
        addGameLogEntry: mockAddGameLogEntry,
        clearChatMessages: vi.fn(),
      } as any);

      vi.mocked(useSessionStore).mockReturnValue({
        playerName: 'TestPlayer',
        characterName: '',
        isAuthenticated: true,
        hasCharacter: false,
      } as any);

      const { result } = renderHook(() => useGameTerminal());

      result.current.onSendChatMessage('Hello', 'local');

      expect(mockAddGameLogEntry).toHaveBeenCalledWith(
        expect.objectContaining({
          sender: 'TestPlayer',
        })
      );
    });

    it('should execute onClearMessages callback', () => {
      const mockClearChatMessages = vi.fn();
      vi.mocked(useConnectionStore).mockReturnValue({
        isFullyConnected: vi.fn().mockReturnValue(true),
        isConnecting: false,
        error: null,
        reconnectAttempts: 0,
        sessionId: 'test-session',
        websocketConnected: true,
        connectionHealth: 'connected' as const,
        hasAnyConnection: vi.fn().mockReturnValue(true),
        getConnectionInfo: vi.fn().mockReturnValue({
          sessionId: 'test-session',
          websocketConnected: true,
          connectionHealth: 'connected' as const,
        }),
      } as any);
      vi.mocked(useGameStore).mockReturnValue({
        player: null,
        room: null,
        chatMessages: [],
        gameLog: [],
        addGameLogEntry: vi.fn(),
        clearChatMessages: mockClearChatMessages,
      } as any);
      vi.mocked(useSessionStore).mockReturnValue({
        playerName: 'TestPlayer',
        characterName: 'TestCharacter',
        isAuthenticated: true,
        hasCharacter: true,
      } as any);
      vi.mocked(useCommandStore).mockReturnValue({
        commandHistory: [],
        currentCommand: '',
        isExecuting: false,
        executeCommand: vi.fn(),
        clearHistory: vi.fn(),
      } as any);

      const { result } = renderHook(() => useGameTerminal());

      result.current.onClearMessages();

      expect(mockClearChatMessages).toHaveBeenCalled();
    });

    it('should execute onClearHistory callback', () => {
      const mockClearHistory = vi.fn();
      vi.mocked(useConnectionStore).mockReturnValue({
        isFullyConnected: vi.fn().mockReturnValue(true),
        isConnecting: false,
        error: null,
        reconnectAttempts: 0,
        sessionId: 'test-session',
        websocketConnected: true,
        connectionHealth: 'connected' as const,
        hasAnyConnection: vi.fn().mockReturnValue(true),
        getConnectionInfo: vi.fn().mockReturnValue({
          sessionId: 'test-session',
          websocketConnected: true,
          connectionHealth: 'connected' as const,
        }),
      } as any);
      vi.mocked(useGameStore).mockReturnValue({
        player: null,
        room: null,
        chatMessages: [],
        gameLog: [],
      } as any);
      vi.mocked(useSessionStore).mockReturnValue({
        playerName: 'TestPlayer',
        characterName: 'TestCharacter',
        isAuthenticated: true,
        hasCharacter: true,
      } as any);
      vi.mocked(useCommandStore).mockReturnValue({
        commandHistory: [],
        currentCommand: '',
        isExecuting: false,
        executeCommand: vi.fn(),
        clearHistory: mockClearHistory,
      } as any);

      const { result } = renderHook(() => useGameTerminal());

      result.current.onClearHistory();

      expect(mockClearHistory).toHaveBeenCalled();
    });

    it('should execute onDownloadLogs callback', () => {
      const consoleSpy = vi.spyOn(console, 'log').mockImplementation(() => {});
      const mockGameLog = [{ text: 'log entry', timestamp: '2024-01-01T12:00:00Z', type: 'system' }];
      const mockCommandHistory = [{ command: 'look', timestamp: Date.now(), success: true }];

      vi.mocked(useConnectionStore).mockReturnValue({
        isFullyConnected: vi.fn().mockReturnValue(true),
        isConnecting: false,
        error: null,
        reconnectAttempts: 0,
        sessionId: 'test-session',
        websocketConnected: true,
        connectionHealth: 'connected' as const,
        hasAnyConnection: vi.fn().mockReturnValue(true),
        getConnectionInfo: vi.fn().mockReturnValue({
          sessionId: 'test-session',
          websocketConnected: true,
          connectionHealth: 'connected' as const,
        }),
      } as any);
      vi.mocked(useGameStore).mockReturnValue({
        player: null,
        room: null,
        chatMessages: [],
        gameLog: mockGameLog,
        addGameLogEntry: vi.fn(),
        clearChatMessages: vi.fn(),
      } as any);

      vi.mocked(useSessionStore).mockReturnValue({
        playerName: 'TestPlayer',
        characterName: 'TestCharacter',
        isAuthenticated: true,
        hasCharacter: true,
      } as any);
      vi.mocked(useCommandStore).mockReturnValue({
        commandHistory: mockCommandHistory,
        currentCommand: '',
        isExecuting: false,
        executeCommand: vi.fn(),
        clearHistory: vi.fn(),
      } as any);

      const { result } = renderHook(() => useGameTerminal());

      result.current.onDownloadLogs();

      expect(consoleSpy).toHaveBeenCalledWith(
        'Downloading logs...',
        expect.objectContaining({
          chatMessages: expect.any(Array),
          gameLog: mockGameLog,
          commandHistory: mockCommandHistory,
        })
      );

      consoleSpy.mockRestore();
    });
  });

  describe('Message Transformation', () => {
    it('should transform messages with isCompleteHtml field', () => {
      vi.mocked(useConnectionStore).mockReturnValue({
        isFullyConnected: vi.fn().mockReturnValue(true),
        isConnecting: false,
        error: null,
        reconnectAttempts: 0,
        sessionId: 'test-session',
        websocketConnected: true,
        connectionHealth: 'connected' as const,
        hasAnyConnection: vi.fn().mockReturnValue(true),
        getConnectionInfo: vi.fn().mockReturnValue({
          sessionId: 'test-session',
          websocketConnected: true,
          connectionHealth: 'connected' as const,
        }),
      } as any);
      vi.mocked(useGameStore).mockReturnValue({
        player: null,
        room: null,
        chatMessages: [
          {
            text: '<div>HTML content</div>',
            timestamp: '2024-01-01T12:00:00Z',
            isHtml: true,
            isCompleteHtml: true,
            type: 'system',
          },
        ],
        gameLog: [],
      } as any);
      vi.mocked(useSessionStore).mockReturnValue({
        playerName: 'TestPlayer',
        characterName: 'TestCharacter',
        isAuthenticated: true,
        hasCharacter: true,
      } as any);
      vi.mocked(useCommandStore).mockReturnValue({
        commandHistory: [],
        currentCommand: '',
        isExecuting: false,
        executeCommand: vi.fn(),
        clearHistory: vi.fn(),
      } as any);

      const { result } = renderHook(() => useGameTerminal());

      const message = result.current.messages[0];
      expect(message.text).toBe('<div>HTML content</div>');
      expect(Object.getOwnPropertyDescriptor(message, 'isCompleteHtml')?.value).toBe(true);
    });

    it('should transform messages with channel field', () => {
      vi.mocked(useConnectionStore).mockReturnValue({
        isFullyConnected: vi.fn().mockReturnValue(true),
        isConnecting: false,
        error: null,
        reconnectAttempts: 0,
        sessionId: 'test-session',
        websocketConnected: true,
        connectionHealth: 'connected' as const,
        hasAnyConnection: vi.fn().mockReturnValue(true),
        getConnectionInfo: vi.fn().mockReturnValue({
          sessionId: 'test-session',
          websocketConnected: true,
          connectionHealth: 'connected' as const,
        }),
      } as any);
      vi.mocked(useGameStore).mockReturnValue({
        player: null,
        room: null,
        chatMessages: [
          {
            text: 'Hello world',
            timestamp: '2024-01-01T12:00:00Z',
            isHtml: false,
            channel: 'local',
            type: 'chat',
          },
        ],
        gameLog: [],
      } as any);
      vi.mocked(useSessionStore).mockReturnValue({
        playerName: 'TestPlayer',
        characterName: 'TestCharacter',
        isAuthenticated: true,
        hasCharacter: true,
      } as any);
      vi.mocked(useCommandStore).mockReturnValue({
        commandHistory: [],
        currentCommand: '',
        isExecuting: false,
        executeCommand: vi.fn(),
        clearHistory: vi.fn(),
      } as any);

      const { result } = renderHook(() => useGameTerminal());

      const message = result.current.messages[0];
      expect(Object.getOwnPropertyDescriptor(message, 'channel')?.value).toBe('local');
    });

    it('should transform messages with rawText field', () => {
      vi.mocked(useConnectionStore).mockReturnValue({
        isFullyConnected: vi.fn().mockReturnValue(true),
        isConnecting: false,
        error: null,
        reconnectAttempts: 0,
        sessionId: 'test-session',
        websocketConnected: true,
        connectionHealth: 'connected' as const,
        hasAnyConnection: vi.fn().mockReturnValue(true),
        getConnectionInfo: vi.fn().mockReturnValue({
          sessionId: 'test-session',
          websocketConnected: true,
          connectionHealth: 'connected' as const,
        }),
      } as any);
      vi.mocked(useGameStore).mockReturnValue({
        player: null,
        room: null,
        chatMessages: [
          {
            text: 'Formatted text',
            timestamp: '2024-01-01T12:00:00Z',
            isHtml: false,
            rawText: 'raw unformatted text',
            type: 'system',
          },
        ],
        gameLog: [],
      } as any);
      vi.mocked(useSessionStore).mockReturnValue({
        playerName: 'TestPlayer',
        characterName: 'TestCharacter',
        isAuthenticated: true,
        hasCharacter: true,
      } as any);
      vi.mocked(useCommandStore).mockReturnValue({
        commandHistory: [],
        currentCommand: '',
        isExecuting: false,
        executeCommand: vi.fn(),
        clearHistory: vi.fn(),
      } as any);

      const { result } = renderHook(() => useGameTerminal());

      const message = result.current.messages[0];
      expect(Object.getOwnPropertyDescriptor(message, 'rawText')?.value).toBe('raw unformatted text');
    });

    it('should transform messages with aliasChain field', () => {
      const aliasChain = [
        { original: 'l', expanded: 'look', alias_name: 'look' },
        { original: 'around', expanded: 'around', alias_name: '' },
      ];

      vi.mocked(useConnectionStore).mockReturnValue({
        isFullyConnected: vi.fn().mockReturnValue(true),
        isConnecting: false,
        error: null,
        reconnectAttempts: 0,
        sessionId: 'test-session',
        websocketConnected: true,
        connectionHealth: 'connected' as const,
        hasAnyConnection: vi.fn().mockReturnValue(true),
        getConnectionInfo: vi.fn().mockReturnValue({
          sessionId: 'test-session',
          websocketConnected: true,
          connectionHealth: 'connected' as const,
        }),
      } as any);
      vi.mocked(useGameStore).mockReturnValue({
        player: null,
        room: null,
        chatMessages: [
          {
            text: 'You look around',
            timestamp: '2024-01-01T12:00:00Z',
            isHtml: false,
            aliasChain,
            type: 'command',
          },
        ],
        gameLog: [],
      } as any);
      vi.mocked(useSessionStore).mockReturnValue({
        playerName: 'TestPlayer',
        characterName: 'TestCharacter',
        isAuthenticated: true,
        hasCharacter: true,
      } as any);
      vi.mocked(useCommandStore).mockReturnValue({
        commandHistory: [],
        currentCommand: '',
        isExecuting: false,
        executeCommand: vi.fn(),
        clearHistory: vi.fn(),
      } as any);

      const { result } = renderHook(() => useGameTerminal());

      const message = result.current.messages[0];
      expect(Object.getOwnPropertyDescriptor(message, 'aliasChain')?.value).toEqual(aliasChain);
    });

    it('should use messageType from message if available', () => {
      vi.mocked(useConnectionStore).mockReturnValue({
        isFullyConnected: vi.fn().mockReturnValue(true),
        isConnecting: false,
        error: null,
        reconnectAttempts: 0,
        sessionId: 'test-session',
        websocketConnected: true,
        connectionHealth: 'connected' as const,
        hasAnyConnection: vi.fn().mockReturnValue(true),
        getConnectionInfo: vi.fn().mockReturnValue({
          sessionId: 'test-session',
          websocketConnected: true,
          connectionHealth: 'connected' as const,
        }),
      } as any);
      vi.mocked(useGameStore).mockReturnValue({
        player: null,
        room: null,
        chatMessages: [
          {
            text: 'Test message',
            timestamp: '2024-01-01T12:00:00Z',
            isHtml: false,
            type: 'system',
            messageType: 'custom_type',
          },
        ],
        gameLog: [],
      } as any);

      const { result } = renderHook(() => useGameTerminal());

      expect(result.current.messages[0].messageType).toBe('custom_type');
    });

    it('should fallback to type if messageType is not available', () => {
      vi.mocked(useConnectionStore).mockReturnValue({
        isFullyConnected: vi.fn().mockReturnValue(true),
        isConnecting: false,
        error: null,
        reconnectAttempts: 0,
        sessionId: 'test-session',
        websocketConnected: true,
        connectionHealth: 'connected' as const,
        hasAnyConnection: vi.fn().mockReturnValue(true),
        getConnectionInfo: vi.fn().mockReturnValue({
          sessionId: 'test-session',
          websocketConnected: true,
          connectionHealth: 'connected' as const,
        }),
      } as any);
      vi.mocked(useGameStore).mockReturnValue({
        player: null,
        room: null,
        chatMessages: [
          {
            text: 'Test message',
            timestamp: '2024-01-01T12:00:00Z',
            isHtml: false,
            type: 'system',
          },
        ],
        gameLog: [],
      } as any);

      const { result } = renderHook(() => useGameTerminal());

      expect(result.current.messages[0].messageType).toBe('system');
    });
  });

  describe('Test-Specific Command History Logic', () => {
    it('should handle command history transformation in test mode', () => {
      const initialHistory = [
        { command: 'look', timestamp: Date.now(), success: true },
        { command: 'inventory', timestamp: Date.now(), success: true },
      ];

      vi.mocked(useConnectionStore).mockReturnValue({
        isFullyConnected: vi.fn().mockReturnValue(true),
        isConnecting: false,
        error: null,
        reconnectAttempts: 0,
        sessionId: 'test-session',
        websocketConnected: true,
        connectionHealth: 'connected' as const,
        hasAnyConnection: vi.fn().mockReturnValue(true),
        getConnectionInfo: vi.fn().mockReturnValue({
          sessionId: 'test-session',
          websocketConnected: true,
          connectionHealth: 'connected' as const,
        }),
      } as any);
      vi.mocked(useSessionStore).mockReturnValue({
        playerName: 'TestPlayer',
        characterName: 'TestCharacter',
        isAuthenticated: true,
        hasCharacter: true,
      } as any);
      vi.mocked(useCommandStore).mockReturnValue({
        commandHistory: initialHistory,
        currentCommand: '',
        isExecuting: false,
        executeCommand: vi.fn(),
        clearHistory: vi.fn(),
      } as any);

      const { result } = renderHook(() => useGameTerminal());

      // Should transform command history to array of strings
      expect(result.current.commandHistory).toHaveLength(2);
      expect(result.current.commandHistory[0]).toBe('look');
      expect(result.current.commandHistory[1]).toBe('inventory');
    });
  });
});
