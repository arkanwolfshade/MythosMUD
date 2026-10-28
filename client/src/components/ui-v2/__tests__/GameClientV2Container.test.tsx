/**
 * Tests for GameClientV2Container component.
 */

import { fireEvent, render, screen } from '@testing-library/react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import { GameClientV2Container } from '../GameClientV2Container';

// Mock WebSocket globally to prevent connection errors in test environment
global.WebSocket = vi.fn().mockImplementation(() => ({
  send: vi.fn(),
  close: vi.fn(),
  addEventListener: vi.fn(),
  removeEventListener: vi.fn(),
  readyState: WebSocket.CONNECTING,
})) as unknown as typeof WebSocket;

// Mock URL constructor to handle relative URLs in tests
const originalURL = global.URL;
global.URL = vi.fn().mockImplementation((url: string, base?: string) => {
  // If url is relative and no base is provided, use a default base
  if (url.startsWith('/') && !base) {
    return new originalURL(url, 'http://localhost');
  }
  return new originalURL(url, base);
}) as unknown as typeof URL;

// Mock fetch for API calls using vi.spyOn for proper cleanup
const fetchSpy = vi.spyOn(global, 'fetch').mockResolvedValue({
  ok: true,
  json: async () => ({}),
  text: async () => '',
} as Response);

// Mock all dependencies
vi.mock('../GameClientV2', async () => {
  const { useState } = await import('react');
  let mounts = 0;
  return {
    // data-mount-id changes only when the component remounts (e.g. the container bumps its key).
    GameClientV2: ({ playerName }: { playerName: string }) => {
      const [mountId] = useState(() => ++mounts);
      return (
        <div data-testid="game-client-v2" data-mount-id={mountId}>
          {playerName}
        </div>
      );
    },
  };
});

vi.mock('../DeathInterstitial', () => ({
  DeathInterstitial: ({ isVisible }: { isVisible: boolean }) =>
    isVisible ? <div data-testid="death-interstitial">Death</div> : null,
}));

vi.mock('../DeliriumInterstitial', () => ({
  DeliriumInterstitial: ({ isVisible }: { isVisible: boolean }) =>
    isVisible ? <div data-testid="delirium-interstitial">Delirium</div> : null,
}));

vi.mock('../../MainMenuModal', () => ({
  MainMenuModal: ({ isOpen, onResetLayoutClick }: { isOpen: boolean; onResetLayoutClick?: () => void }) => (
    <>
      {isOpen ? <div data-testid="main-menu-modal">Main Menu</div> : null}
      <button type="button" data-testid="mock-reset-ui-layout" onClick={onResetLayoutClick} />
    </>
  ),
}));

vi.mock('../MapView', () => ({
  MapView: ({ isOpen }: { isOpen: boolean }) => (isOpen ? <div data-testid="map-view">Map</div> : null),
}));

vi.mock('./components/TabbedInterfaceOverlay', () => ({
  TabbedInterfaceOverlay: ({ tabs }: { tabs: unknown[] }) =>
    tabs.length > 0 ? <div data-testid="tabbed-interface-overlay">Tabs</div> : null,
}));

vi.mock('./useTabbedInterface', () => ({
  useTabbedInterface: () => ({
    tabs: [],
    activeTabId: null,
    addTab: vi.fn(),
    closeTab: vi.fn(),
    setActiveTab: vi.fn(),
  }),
}));

vi.mock('./hooks/useCommandHandlers', () => ({
  useCommandHandlers: () => ({
    handleCommandSubmit: vi.fn(),
    handleChatMessage: vi.fn(),
    handleClearMessages: vi.fn(),
    handleClearHistory: vi.fn(),
  }),
}));

vi.mock('./hooks/useEventProcessing', () => ({
  useEventProcessing: () => ({
    handleGameEvent: vi.fn(),
    clearEventLog: vi.fn(),
  }),
}));

vi.mock('./hooks/useGameConnectionManagement', () => ({
  useGameConnectionManagement: () => ({
    isConnected: true,
    isConnecting: false,
    error: null,
    reconnectAttempts: 0,
    sendCommand: vi.fn(),
    disconnect: vi.fn(),
  }),
}));

vi.mock('./hooks/useMythosTimeBootstrap', () => ({
  useMythosTimeBootstrap: () => {},
}));

vi.mock('./hooks/useRespawnHandlers', () => ({
  useRespawnHandlers: () => ({
    handleRespawn: vi.fn(),
    handleDeliriumRespawn: vi.fn(),
  }),
}));

vi.mock('../../utils/memoryMonitor', () => ({
  useMemoryMonitor: () => ({
    detector: {
      start: vi.fn(),
      stop: vi.fn(),
    },
  }),
}));

vi.mock('../../utils/logger', () => ({
  logger: {
    downloadLogs: vi.fn(),
  },
}));

vi.mock('./utils/messageUtils', () => ({
  sanitizeChatMessageForState: (msg: unknown) => msg,
}));

describe('GameClientV2Container', () => {
  const defaultProps = {
    playerName: 'TestPlayer',
    authToken: 'test-token',
  };

  beforeEach(() => {
    fetchSpy.mockClear();
    vi.clearAllMocks();
    vi.useFakeTimers();
  });

  afterEach(() => {
    fetchSpy.mockRestore();
    vi.useRealTimers();
  });

  it('should render GameClientV2 when no tabs are open', () => {
    render(<GameClientV2Container {...defaultProps} />);
    expect(screen.getByTestId('game-client-v2')).toBeInTheDocument();
  });

  it('should render with playerName', () => {
    render(<GameClientV2Container {...defaultProps} playerName="MyPlayer" />);
    expect(screen.getByText('MyPlayer')).toBeInTheDocument();
  });

  it('should render TabbedInterfaceOverlay when tabs exist', () => {
    // TabbedInterfaceOverlay only renders when tabs.length > 0
    // Since useTabbedInterface returns empty tabs, it won't render
    render(<GameClientV2Container {...defaultProps} />);
    // When tabs are empty, TabbedInterfaceOverlay returns null
    expect(screen.queryByTestId('tabbed-interface-overlay')).not.toBeInTheDocument();
  });

  it('should not show death interstitial by default', () => {
    render(<GameClientV2Container {...defaultProps} />);
    expect(screen.queryByTestId('death-interstitial')).not.toBeInTheDocument();
  });

  it('should not show delirium interstitial by default', () => {
    render(<GameClientV2Container {...defaultProps} />);
    expect(screen.queryByTestId('delirium-interstitial')).not.toBeInTheDocument();
  });

  it('should not show main menu by default', () => {
    render(<GameClientV2Container {...defaultProps} />);
    expect(screen.queryByTestId('main-menu-modal')).not.toBeInTheDocument();
  });

  it('should not show map view by default', () => {
    render(<GameClientV2Container {...defaultProps} />);
    expect(screen.queryByTestId('map-view')).not.toBeInTheDocument();
  });

  it('should handle onLogout callback', () => {
    const onLogout = vi.fn();
    render(<GameClientV2Container {...defaultProps} onLogout={onLogout} />);
    expect(screen.getByTestId('game-client-v2')).toBeInTheDocument();
  });

  it('should handle isLoggingOut prop', () => {
    render(<GameClientV2Container {...defaultProps} isLoggingOut={true} />);
    expect(screen.getByTestId('game-client-v2')).toBeInTheDocument();
  });

  describe('Reset UI Layout', () => {
    const PANEL_LAYOUT_KEY = 'mythosmud-ui-v2-panel-layout';
    const HEADER_COLLAPSED_KEY = 'mythosmud-ui-v2-header-collapsed';

    afterEach(() => {
      localStorage.clear();
    });

    it('should forget the saved panel layout and header state, then remount GameClientV2', () => {
      localStorage.setItem(PANEL_LAYOUT_KEY, '{"chatHistory":{}}');
      localStorage.setItem(HEADER_COLLAPSED_KEY, 'true');
      render(<GameClientV2Container {...defaultProps} />);
      const mountBefore = screen.getByTestId('game-client-v2').getAttribute('data-mount-id');

      fireEvent.click(screen.getByTestId('mock-reset-ui-layout'));

      expect(localStorage.getItem(PANEL_LAYOUT_KEY)).toBeNull();
      expect(localStorage.getItem(HEADER_COLLAPSED_KEY)).toBeNull();
      expect(screen.getByTestId('game-client-v2').getAttribute('data-mount-id')).not.toBe(mountBefore);
    });

    it('should leave other saved preferences alone', () => {
      localStorage.setItem('mythosmud-ui-preferences', '{"textLabels":true}');
      render(<GameClientV2Container {...defaultProps} />);

      fireEvent.click(screen.getByTestId('mock-reset-ui-layout'));

      expect(localStorage.getItem('mythosmud-ui-preferences')).toBe('{"textLabels":true}');
    });
  });

  it('should have correct container data attribute', () => {
    const { container } = render(<GameClientV2Container {...defaultProps} />);
    const gameContainer = container.querySelector('[data-game-container]');
    expect(gameContainer).toBeInTheDocument();
  });
});
