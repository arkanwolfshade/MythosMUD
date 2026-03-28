/**
 * Main dock: skip rendering when panel manager marks a slot invisible.
 */

import '@testing-library/jest-dom/vitest';
import { render, screen } from '@testing-library/react';
import React from 'react';
import { beforeEach, describe, expect, it, vi } from 'vitest';
import { GameClientV2 } from '../GameClientV2';

const dockTest = vi.hoisted(() => ({
  invisibleIds: new Set<string>(),
  /** How many times dock-mounted panel bodies executed (must stay 0 when slot is invisible). */
  chatHistoryBodyRenders: 0,
  gameInfoBodyRenders: 0,
}));

/** Split panel shape so Lizard parameter-count stays under the file threshold (object keys count toward it). */
function mockPanelRecordCore(id: string) {
  return {
    id,
    title: id,
    position: { x: 0, y: 0 },
    size: { width: 300, height: 200 },
  };
}

function mockPanelRecordFlags(id: string) {
  return {
    zIndex: 1,
    isMinimized: false,
    isMaximized: false,
    isVisible: !dockTest.invisibleIds.has(id),
    minSize: { width: 100, height: 100 },
  };
}

function mockPanelRecord(id: string) {
  return { ...mockPanelRecordCore(id), ...mockPanelRecordFlags(id) };
}

function mockUsePanelManagerNoops() {
  return {
    updatePosition: vi.fn(),
    updateSize: vi.fn(),
    toggleMinimize: vi.fn(),
    toggleMaximize: vi.fn(),
    focusPanel: vi.fn(),
    scalePanelsToViewport: vi.fn(),
  };
}

function mockUsePanelManagerValue() {
  return {
    getPanel: (id: string) => mockPanelRecord(id),
    ...mockUsePanelManagerNoops(),
  };
}

const chatHistoryLayoutIdentity = {
  id: 'chatHistory' as const,
  title: 'Chat History',
  position: { x: 0, y: 0 },
  size: { width: 300, height: 200 },
};

const chatHistoryLayoutState = {
  isMinimized: false,
  isMaximized: false,
  isVisible: true,
  zIndex: 1000,
  minSize: { width: 200, height: 100 },
};

const defaultChatHistoryLayoutKey = { ...chatHistoryLayoutIdentity, ...chatHistoryLayoutState };

function mockDefaultPanelLayout() {
  return {
    chatHistory: { ...defaultChatHistoryLayoutKey },
  };
}

vi.mock('../HeaderBar', () => ({
  HeaderBar: ({ playerName }: { playerName: string }) => <div data-testid="header-bar">{playerName}</div>,
}));

vi.mock('../TentacleBackdrop', () => ({
  TentacleBackdrop: () => null,
}));

vi.mock('../GameClientV2AuxiliaryPanels', () => ({
  GameClientV2AuxiliaryPanels: () => null,
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
  usePanelManager: () => mockUsePanelManagerValue(),
}));

vi.mock('../panels/ChatHistoryPanel', () => ({
  ChatHistoryPanel: () => {
    dockTest.chatHistoryBodyRenders += 1;
    return <div data-testid="chat-history-panel">Chat History</div>;
  },
}));

vi.mock('../panels/GameInfoPanel', () => ({
  GameInfoPanel: () => {
    dockTest.gameInfoBodyRenders += 1;
    return <div data-testid="game-info-panel">Game Info</div>;
  },
}));

vi.mock('../panels/LocationPanel', () => ({
  LocationPanel: () => <div data-testid="location-panel">Location</div>,
}));

vi.mock('../panels/OccupantsPanel', () => ({
  OccupantsPanel: () => <div data-testid="occupants-panel">Occupants</div>,
}));

vi.mock('../panels/QuestLogPanel', () => ({
  QuestLogPanel: () => <div data-testid="quest-log-panel">Quest Log</div>,
}));

vi.mock('../panels/RoomDescriptionPanel', () => ({
  RoomDescriptionPanel: () => <div data-testid="room-description-panel">Room Description</div>,
}));

vi.mock('../utils/panelLayout', () => ({
  createDefaultPanelLayout: () => mockDefaultPanelLayout(),
}));

describe('GameClientV2 main dock visibility', () => {
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
    dockTest.invisibleIds.clear();
    dockTest.chatHistoryBodyRenders = 0;
    dockTest.gameInfoBodyRenders = 0;
    vi.clearAllMocks();
    Object.defineProperty(window, 'innerWidth', { writable: true, configurable: true, value: 1920 });
    Object.defineProperty(window, 'innerHeight', { writable: true, configurable: true, value: 1080 });
  });

  it('does not render a dock slot when that panel is invisible', () => {
    dockTest.invisibleIds.add('chatHistory');
    render(<GameClientV2 {...defaultProps} />);
    expect(screen.queryByTestId('panel-chatHistory')).not.toBeInTheDocument();
    expect(screen.queryByTestId('chat-history-panel')).not.toBeInTheDocument();
    expect(dockTest.chatHistoryBodyRenders).toBe(0);
  });

  it('still renders other dock slots when one main dock panel is invisible', () => {
    dockTest.invisibleIds.add('gameInfo');
    render(<GameClientV2 {...defaultProps} />);
    expect(screen.queryByTestId('panel-gameInfo')).not.toBeInTheDocument();
    expect(screen.getByTestId('panel-location')).toBeInTheDocument();
    expect(screen.getByTestId('panel-questLog')).toBeInTheDocument();
    expect(dockTest.gameInfoBodyRenders).toBe(0);
    expect(dockTest.chatHistoryBodyRenders).toBeGreaterThan(0);
  });

  it('runs dock panel bodies when the slot is visible', () => {
    render(<GameClientV2 {...defaultProps} />);
    expect(dockTest.chatHistoryBodyRenders).toBeGreaterThan(0);
    expect(dockTest.gameInfoBodyRenders).toBeGreaterThan(0);
  });
});
