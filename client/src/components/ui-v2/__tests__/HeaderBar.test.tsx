import { fireEvent, render, screen } from '@testing-library/react';
import { beforeEach, describe, expect, it, vi } from 'vitest';
import type { MythosTimeState } from '../../../types/mythosTime';
import { HeaderBar } from '../HeaderBar';

// Mock the dependencies
vi.mock('../ui/EldritchIcon', () => ({
  EldritchIcon: ({ name }: { name: string; size?: number }) => <div data-testid="eldritch-icon">{name}</div>,
  MythosIcons: {
    minimize: 'minimize',
    maximize: 'maximize',
  },
}));

// Note: We're not mocking LogoutButton here since we want to test the actual component behavior

vi.mock('../../utils/mythosTime', () => ({
  formatMythosTime12Hour: (_time: string) => `12:00 PM`,
}));

describe('HeaderBar', () => {
  const defaultProps = {
    playerName: 'TestPlayer',
    isConnected: true,
    isConnecting: false,
    error: null,
    reconnectAttempts: 0,
    mythosTime: null,
    onLogout: vi.fn(),
    isLoggingOut: false,
  };

  const mockMythosTime: MythosTimeState = {
    mythos_datetime: '1928-01-01T12:00:00Z',
    mythos_clock: '12:00:00',
    month_name: 'January',
    day_of_month: 1,
    day_name: 'Sunday',
    week_of_month: 1,
    season: 'Winter',
    daypart: 'midday',
    is_daytime: true,
    is_witching_hour: false,
    server_timestamp: '2025-01-01T12:00:00Z',
    active_holidays: [],
    upcoming_holidays: [],
    formatted_date: 'January 1, 1928',
  };

  beforeEach(() => {
    localStorage.clear();
    vi.clearAllMocks();
  });

  describe('rendering', () => {
    it('should render player name', () => {
      render(<HeaderBar {...defaultProps} />);
      expect(screen.getByText(/Player: TestPlayer/)).toBeInTheDocument();
    });

    it('should render connection status when connected', () => {
      render(<HeaderBar {...defaultProps} isConnected={true} />);
      expect(screen.getByText('Connected')).toBeInTheDocument();
    });

    it('should render connection status when connecting', () => {
      render(<HeaderBar {...defaultProps} isConnected={false} isConnecting={true} />);
      expect(screen.getByText('Connecting...')).toBeInTheDocument();
    });

    it('should render connection status when disconnected', () => {
      render(<HeaderBar {...defaultProps} isConnected={false} isConnecting={false} />);
      expect(screen.getByText('Disconnected')).toBeInTheDocument();
    });

    it('should render Reconnecting... when isConnecting and reconnectAttempts > 0', () => {
      render(<HeaderBar {...defaultProps} isConnected={false} isConnecting={true} reconnectAttempts={2} />);
      expect(screen.getByText('Reconnecting...')).toBeInTheDocument();
    });

    it('should render error message when error is present', () => {
      render(<HeaderBar {...defaultProps} error="Connection failed" />);
      expect(screen.getByText('Connection failed')).toBeInTheDocument();
    });

    it('should render reconnect attempts when greater than 0', () => {
      render(<HeaderBar {...defaultProps} reconnectAttempts={3} />);
      expect(screen.getByText(/Reconnect: 3/)).toBeInTheDocument();
    });

    it('should not render reconnect attempts when 0', () => {
      render(<HeaderBar {...defaultProps} reconnectAttempts={0} />);
      expect(screen.queryByText(/Reconnect:/)).not.toBeInTheDocument();
    });

    it('should render active effects when provided', () => {
      render(
        <HeaderBar
          {...defaultProps}
          activeEffects={[{ effect_type: 'login_warded', label: 'Warded', remaining_seconds: 8 }]}
        />
      );
      expect(screen.getByText(/Warded/)).toBeInTheDocument();
      expect(screen.getByText(/0:08/)).toBeInTheDocument();
    });

    it('should not render effects section when activeEffects is empty', () => {
      render(<HeaderBar {...defaultProps} activeEffects={[]} />);
      expect(screen.queryByText(/Warded/)).not.toBeInTheDocument();
    });

    it('should render mythos time when provided', () => {
      render(<HeaderBar {...defaultProps} mythosTime={mockMythosTime} />);
      expect(screen.getByText(/Mythos Time/)).toBeInTheDocument();
      expect(screen.getByText(/12:00 PM - January 1, 1928/)).toBeInTheDocument();
    });

    it('should render "Calibrating chronicle..." when mythos time is null', () => {
      render(<HeaderBar {...defaultProps} mythosTime={null} />);
      expect(screen.getByText(/Calibrating chronicle.../)).toBeInTheDocument();
    });

    it('should render logout button', () => {
      render(<HeaderBar {...defaultProps} />);
      expect(screen.getByTestId('logout-button')).toBeInTheDocument();
    });
  });

  describe('collapse/expand functionality', () => {
    it('should render expanded by default', () => {
      render(<HeaderBar {...defaultProps} />);
      expect(screen.getByText(/Player: TestPlayer/)).toBeInTheDocument();
      expect(screen.getByLabelText('Collapse header')).toBeInTheDocument();
    });

    it('should render collapsed when localStorage has collapsed state', () => {
      localStorage.setItem('mythosmud-ui-v2-header-collapsed', 'true');
      render(<HeaderBar {...defaultProps} />);
      expect(screen.getByLabelText('Expand header')).toBeInTheDocument();
      expect(screen.queryByText(/Player: TestPlayer/)).not.toBeInTheDocument();
    });

    it('should toggle collapse state when collapse button is clicked', () => {
      render(<HeaderBar {...defaultProps} />);
      const collapseButton = screen.getByLabelText('Collapse header');

      fireEvent.click(collapseButton);

      expect(screen.getByLabelText('Expand header')).toBeInTheDocument();
      expect(localStorage.getItem('mythosmud-ui-v2-header-collapsed')).toBe('true');
    });

    it('should toggle expand state when expand button is clicked', () => {
      localStorage.setItem('mythosmud-ui-v2-header-collapsed', 'true');
      render(<HeaderBar {...defaultProps} />);
      const expandButton = screen.getByLabelText('Expand header');

      fireEvent.click(expandButton);

      expect(screen.getByLabelText('Collapse header')).toBeInTheDocument();
      expect(localStorage.getItem('mythosmud-ui-v2-header-collapsed')).toBe('false');
    });

    it('should show player name in collapsed state', () => {
      localStorage.setItem('mythosmud-ui-v2-header-collapsed', 'true');
      render(<HeaderBar {...defaultProps} />);
      expect(screen.getByText('TestPlayer')).toBeInTheDocument();
    });
  });

  describe('logout functionality', () => {
    it('should call onLogout when logout button is clicked', () => {
      const onLogout = vi.fn();
      render(<HeaderBar {...defaultProps} onLogout={onLogout} />);

      const logoutButton = screen.getByTestId('logout-button');
      fireEvent.click(logoutButton);

      expect(onLogout).toHaveBeenCalledTimes(1);
    });

    it('should disable logout button when not connected', () => {
      render(<HeaderBar {...defaultProps} isConnected={false} />);
      const logoutButton = screen.getByTestId('logout-button');
      expect(logoutButton).toBeDisabled();
    });

    it('should disable logout button when logging out', () => {
      render(<HeaderBar {...defaultProps} isLoggingOut={true} />);
      const logoutButton = screen.getByTestId('logout-button');
      expect(logoutButton).toBeDisabled();
    });

    it('should enable logout button when connected and not logging out', () => {
      render(<HeaderBar {...defaultProps} isConnected={true} isLoggingOut={false} />);
      const logoutButton = screen.getByTestId('logout-button');
      expect(logoutButton).not.toBeDisabled();
    });

    it('should show "Exiting..." when isLoggingOut is true', () => {
      render(<HeaderBar {...defaultProps} isLoggingOut={true} />);
      expect(screen.getByText('Exiting...')).toBeInTheDocument();
    });
  });

  describe('connection status styling', () => {
    it('should apply success color when connected', () => {
      render(<HeaderBar {...defaultProps} isConnected={true} />);
      const statusElement = screen.getByText('Connected');
      expect(statusElement.className).toContain('bg-mythos-terminal-success');
    });

    it('should apply error color when disconnected', () => {
      render(<HeaderBar {...defaultProps} isConnected={false} isConnecting={false} />);
      const statusElement = screen.getByText('Disconnected');
      expect(statusElement.className).toContain('bg-mythos-terminal-error');
    });
  });
});
