/**
 * Tests for GameClientV2 component.
 */

import { render, screen } from '@testing-library/react';
import { beforeEach, describe, expect, it, vi } from 'vitest';
import { GameClientV2 } from '../GameClientV2';
import type { Player, Room } from '../types';

// Mock all dependencies
vi.mock('../HeaderBar', () => ({
  HeaderBar: ({ playerName }: { playerName: string }) => <div data-testid="header-bar">{playerName}</div>,
}));

vi.mock('../PanelSystem/PanelContainer', () => ({
  PanelContainer: ({ children, title }: { children: React.ReactNode; title: string }) => (
    <div data-testid={`panel-${title}`}>{children}</div>
  ),
}));

vi.mock('../PanelSystem/PanelManager', () => ({
  PanelManagerProvider: ({ children }: { children: React.ReactNode }) => <div>{children}</div>,
}));

vi.mock('../PanelSystem/usePanelManager', () => ({
  usePanelManager: () => ({
    getPanel: (id: string) => ({
      id,
      title: id,
      position: { x: 0, y: 0 },
      size: { width: 300, height: 200 },
      zIndex: 1,
      isMinimized: false,
      isMaximized: false,
      isVisible: true,
      minSize: { width: 100, height: 100 },
    }),
    updatePosition: vi.fn(),
    updateSize: vi.fn(),
    toggleMinimize: vi.fn(),
    toggleMaximize: vi.fn(),
    focusPanel: vi.fn(),
    scalePanelsToViewport: vi.fn(),
  }),
}));

vi.mock('../panels/CharacterInfoPanel', () => ({
  CharacterInfoPanel: () => <div data-testid="character-info-panel">Character Info</div>,
}));

vi.mock('../panels/ChatHistoryPanel', () => ({
  ChatHistoryPanel: () => <div data-testid="chat-history-panel">Chat History</div>,
}));

vi.mock('../panels/CommandHistoryPanel', () => ({
  CommandHistoryPanel: () => <div data-testid="command-history-panel">Command History</div>,
}));

vi.mock('../panels/CommandInputPanel', () => ({
  CommandInputPanel: () => <div data-testid="command-input-panel">Command Input</div>,
}));

vi.mock('../panels/GameInfoPanel', () => ({
  GameInfoPanel: () => <div data-testid="game-info-panel">Game Info</div>,
}));

vi.mock('../panels/LocationPanel', () => ({
  LocationPanel: () => <div data-testid="location-panel">Location</div>,
}));

vi.mock('../panels/OccupantsPanel', () => ({
  OccupantsPanel: () => <div data-testid="occupants-panel">Occupants</div>,
}));

vi.mock('../panels/RoomDescriptionPanel', () => ({
  RoomDescriptionPanel: () => <div data-testid="room-description-panel">Room Description</div>,
}));

vi.mock('../utils/panelLayout', () => ({
  createDefaultPanelLayout: () => [
    { id: 'chatHistory', title: 'Chat History', position: { x: 0, y: 0 }, size: { width: 300, height: 200 } },
    { id: 'location', title: 'Location', position: { x: 300, y: 0 }, size: { width: 300, height: 200 } },
    { id: 'roomDescription', title: 'Room Description', position: { x: 0, y: 200 }, size: { width: 300, height: 200 } },
    { id: 'occupants', title: 'Occupants', position: { x: 300, y: 200 }, size: { width: 300, height: 200 } },
    { id: 'gameInfo', title: 'Game Info', position: { x: 600, y: 0 }, size: { width: 300, height: 200 } },
    { id: 'characterInfo', title: 'Character Info', position: { x: 600, y: 200 }, size: { width: 300, height: 200 } },
    { id: 'commandHistory', title: 'Command History', position: { x: 0, y: 400 }, size: { width: 300, height: 200 } },
    { id: 'commandInput', title: 'Command Input', position: { x: 300, y: 400 }, size: { width: 300, height: 200 } },
  ],
}));

describe('GameClientV2', () => {
  const defaultProps = {
    playerName: 'TestPlayer',
    authToken: 'test-token',
    player: null,
    room: null,
    messages: [],
    commandHistory: [],
    isConnected: true,
    isConnecting: false,
    error: null,
    reconnectAttempts: 0,
    mythosTime: null,
    healthStatus: null,
    lucidityStatus: null,
    onSendCommand: vi.fn(),
    onSendChatMessage: vi.fn(),
    onClearMessages: vi.fn(),
    onClearHistory: vi.fn(),
    onDownloadLogs: vi.fn(),
  };

  beforeEach(() => {
    vi.clearAllMocks();
    // Mock window.innerWidth and innerHeight
    Object.defineProperty(window, 'innerWidth', { writable: true, configurable: true, value: 1920 });
    Object.defineProperty(window, 'innerHeight', { writable: true, configurable: true, value: 1080 });
  });

  it('should render component', () => {
    render(<GameClientV2 {...defaultProps} />);
    expect(screen.getByTestId('header-bar')).toBeInTheDocument();
  });

  it('should render HeaderBar with playerName', () => {
    render(<GameClientV2 {...defaultProps} playerName="MyPlayer" />);
    expect(screen.getByText('MyPlayer')).toBeInTheDocument();
  });

  it('should render panels when visible', () => {
    render(<GameClientV2 {...defaultProps} />);
    expect(screen.getByTestId('chat-history-panel')).toBeInTheDocument();
    expect(screen.getByTestId('location-panel')).toBeInTheDocument();
    expect(screen.getByTestId('room-description-panel')).toBeInTheDocument();
    expect(screen.getByTestId('occupants-panel')).toBeInTheDocument();
    expect(screen.getByTestId('game-info-panel')).toBeInTheDocument();
    expect(screen.getByTestId('character-info-panel')).toBeInTheDocument();
    expect(screen.getByTestId('command-history-panel')).toBeInTheDocument();
    expect(screen.getByTestId('command-input-panel')).toBeInTheDocument();
  });

  it('should handle player with stats', () => {
    const playerWithStats = {
      id: 'player1',
      name: 'TestPlayer',
      stats: {
        current_dp: 75,
        max_dp: 100,
        lucidity: 50,
        max_lucidity: 100,
        position: 'standing',
      },
      in_combat: false,
    };
    render(<GameClientV2 {...defaultProps} player={playerWithStats as Player} />);
    expect(screen.getByTestId('character-info-panel')).toBeInTheDocument();
  });

  it('should handle room with occupant_count', () => {
    const roomWithOccupants: Room = {
      id: 'room1',
      name: 'Test Room',
      description: '',
      exits: {},
      occupant_count: 5,
    };
    render(<GameClientV2 {...defaultProps} room={roomWithOccupants} />);
    expect(screen.getByTestId('occupants-panel')).toBeInTheDocument();
  });

  it('should handle room with players array', () => {
    const roomWithPlayers: Room = {
      id: 'room1',
      name: 'Test Room',
      description: '',
      exits: {},
      players: ['Player1'],
      npcs: [],
    };
    render(<GameClientV2 {...defaultProps} room={roomWithPlayers} />);
    expect(screen.getByTestId('occupants-panel')).toBeInTheDocument();
  });

  it('should handle healthStatus prop', () => {
    const healthStatus = {
      current: 50,
      max: 100,
      tier: 'wounded' as const,
      posture: 'standing',
      inCombat: false,
    };
    render(<GameClientV2 {...defaultProps} healthStatus={healthStatus} />);
    expect(screen.getByTestId('character-info-panel')).toBeInTheDocument();
  });

  it('should handle lucidityStatus prop', () => {
    const lucidityStatus = {
      current: 75,
      max: 100,
      tier: 'lucid' as const,
      liabilities: [],
    };
    render(<GameClientV2 {...defaultProps} lucidityStatus={lucidityStatus} />);
    expect(screen.getByTestId('character-info-panel')).toBeInTheDocument();
  });

  it('should handle isConnected prop', () => {
    render(<GameClientV2 {...defaultProps} isConnected={false} />);
    expect(screen.getByTestId('command-input-panel')).toBeInTheDocument();
  });

  it('should handle isConnecting prop', () => {
    render(<GameClientV2 {...defaultProps} isConnecting={true} />);
    expect(screen.getByTestId('header-bar')).toBeInTheDocument();
  });

  it('should handle error prop', () => {
    render(<GameClientV2 {...defaultProps} error="Connection failed" />);
    expect(screen.getByTestId('header-bar')).toBeInTheDocument();
  });

  it('should handle onLogout callback', () => {
    const onLogout = vi.fn();
    render(<GameClientV2 {...defaultProps} onLogout={onLogout} />);
    expect(screen.getByTestId('header-bar')).toBeInTheDocument();
  });

  it('should handle isLoggingOut prop', () => {
    render(<GameClientV2 {...defaultProps} isLoggingOut={true} />);
    expect(screen.getByTestId('header-bar')).toBeInTheDocument();
  });

  it('should handle empty room (null)', () => {
    render(<GameClientV2 {...defaultProps} room={null} />);
    expect(screen.getByTestId('occupants-panel')).toBeInTheDocument();
  });

  it('should handle empty player (null)', () => {
    render(<GameClientV2 {...defaultProps} player={null} />);
    expect(screen.getByTestId('character-info-panel')).toBeInTheDocument();
  });
});
