import { render, screen } from '@testing-library/react';
import React from 'react';
import { vi } from 'vitest';

// Mock all components before importing GameTerminal
vi.mock('./DraggablePanel', () => ({
  DraggablePanel: ({
    children,
    title,
    defaultSize,
    defaultPosition,
    autoSize,
  }: {
    children: React.ReactNode;
    title: string;
    defaultSize: { width: number; height: number };
    defaultPosition: { x: number; y: number };
    autoSize?: boolean;
  }) => (
    <div
      data-testid={`panel-${title}`}
      data-size={JSON.stringify(defaultSize)}
      data-position={JSON.stringify(defaultPosition)}
      data-auto-size={autoSize}
      className="draggable-panel"
    >
      <h3>{title}</h3>
      {children}
    </div>
  ),
}));

vi.mock('./panels/ChatPanel', () => ({
  ChatPanel: () => <div data-testid="chat-panel">Chat Panel</div>,
}));

vi.mock('./panels/GameLogPanel', () => ({
  GameLogPanel: () => <div data-testid="game-log-panel">Game Log Panel</div>,
}));

vi.mock('./panels/CommandPanel', () => ({
  CommandPanel: () => <div data-testid="command-panel">Command Panel</div>,
}));

vi.mock('./MotdContent', () => ({
  MotdContent: () => <div data-testid="motd-content">MOTD Content</div>,
}));

vi.mock('./ui/EldritchIcon', () => ({
  EldritchIcon: () => <div data-testid="eldritch-icon">Icon</div>,
  MythosIcons: { connection: 'connection' },
}));

// Now import the component
import { GameTerminal } from './GameTerminal';

describe('GameTerminal Panel Sizing', () => {
  const defaultProps = {
    playerName: 'TestPlayer',
    isConnected: true,
    isConnecting: false,
    error: null,
    reconnectAttempts: 0,
    room: {
      id: 'test-room',
      name: 'Test Room',
      description: 'A test room',
      exits: { north: 'north-room' },
    },
    player: {
      name: 'TestPlayer',
      stats: {
        current_health: 100,
        sanity: 80,
        position: 'standing',
      },
    },
    messages: [{ text: 'Welcome to MythosMUD', timestamp: '2024-01-01T00:00:00Z', isHtml: false }],
    commandHistory: ['look', 'inventory'],
    hallucinations: [],
    sanityStatus: null,
    healthStatus: null,
    rescueState: null,
    isLoggingOut: false,
    isMortallyWounded: false,
    isDead: false,
    mythosTime: null,
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
    // Mock window dimensions for testing
    Object.defineProperty(window, 'innerWidth', {
      writable: true,
      configurable: true,
      value: 1200,
    });
    Object.defineProperty(window, 'innerHeight', {
      writable: true,
      configurable: true,
      value: 800,
    });
  });

  test('renders all panels with proper sizing', () => {
    render(<GameTerminal {...defaultProps} />);

    // Check that all panels are rendered
    expect(screen.getByTestId('panel-Chat')).toBeInTheDocument();
    expect(screen.getByTestId('panel-Game Log')).toBeInTheDocument();
    expect(screen.getByTestId('panel-Commands')).toBeInTheDocument();
    expect(screen.getByTestId('panel-Room Info')).toBeInTheDocument();
    expect(screen.getByTestId('panel-Status')).toBeInTheDocument();
  });

  test('game log panel has auto-sizing enabled', () => {
    render(<GameTerminal {...defaultProps} />);

    const gameLogPanel = screen.getByTestId('panel-Game Log');
    const autoSize = gameLogPanel.getAttribute('data-auto-size');

    expect(autoSize).toBe('true');
  });

  test('panels have appropriate default sizes', () => {
    render(<GameTerminal {...defaultProps} />);

    const chatPanel = screen.getByTestId('panel-Chat');
    const chatSize = JSON.parse(chatPanel.getAttribute('data-size') || '{}');

    // Verify panel has reasonable dimensions
    expect(chatSize.width).toBeGreaterThan(400);
    expect(chatSize.height).toBeGreaterThan(300);
    expect(chatSize.width).toBeLessThan(600);
    expect(chatSize.height).toBeLessThan(500);
  });

  test('panels are positioned to avoid overlap', () => {
    render(<GameTerminal {...defaultProps} />);

    const chatPanel = screen.getByTestId('panel-Chat');
    const gameLogPanel = screen.getByTestId('panel-Game Log');

    const chatPosition = JSON.parse(chatPanel.getAttribute('data-position') || '{}');
    const gameLogPosition = JSON.parse(gameLogPanel.getAttribute('data-position') || '{}');

    // Chat panel should be on the left
    expect(chatPosition.x).toBe(50);

    // Game log should be to the right of chat
    expect(gameLogPosition.x).toBeGreaterThan(chatPosition.x);
  });

  test('status panel displays current position', () => {
    render(<GameTerminal {...defaultProps} />);

    expect(screen.getByText('Position:')).toBeInTheDocument();
    expect(screen.getByText('Standing')).toBeInTheDocument();
  });
});
