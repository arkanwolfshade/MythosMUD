import { fireEvent, render, screen } from '@testing-library/react';
import { beforeEach, describe, expect, it, vi } from 'vitest';
import type { MythosTimeState } from '../../../types/mythosTime';
import { HeaderBar } from '../HeaderBar';

// Mock the dependencies
vi.mock('../primitives/EldritchIcon', () => ({
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
    isCollapsed: false,
    onToggleCollapse: vi.fn(),
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

  const witchingMythosTime: MythosTimeState = {
    ...mockMythosTime,
    daypart: 'witching',
    is_daytime: false,
    is_witching_hour: true,
  };

  const holidayMythosTime: MythosTimeState = {
    ...mockMythosTime,
    active_holidays: [
      {
        id: 'hol_hallowmas',
        name: 'Hallowmas',
        tradition: 'mythos',
        season: 'autumn',
        duration_hours: 24,
        bonus_tags: ['harvest_bonus'],
        notes: 'The veil is thin.',
      },
    ],
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

  describe('flavor row (daypart/season/witching/holidays)', () => {
    it('should not render a flavor row on an ordinary day', () => {
      render(<HeaderBar {...defaultProps} mythosTime={mockMythosTime} />);
      expect(screen.queryByText('midday')).not.toBeInTheDocument();
      expect(screen.queryByText('Winter')).not.toBeInTheDocument();
    });

    it('should render daypart and season during witching hour', () => {
      render(<HeaderBar {...defaultProps} mythosTime={witchingMythosTime} />);
      expect(screen.getByText('witching')).toBeInTheDocument();
      expect(screen.getByText('Winter')).toBeInTheDocument();
    });

    it('should use the purple witching accent for daypart text', () => {
      render(<HeaderBar {...defaultProps} mythosTime={witchingMythosTime} />);
      expect(screen.getByText('witching').className).toContain('text-purple-300');
    });

    it('should show "The Veil Thins" only during witching hour', () => {
      render(<HeaderBar {...defaultProps} mythosTime={witchingMythosTime} />);
      expect(screen.getByText('The Veil Thins')).toBeInTheDocument();
    });

    it('should not show "The Veil Thins" outside witching hour', () => {
      render(<HeaderBar {...defaultProps} mythosTime={holidayMythosTime} />);
      expect(screen.queryByText('The Veil Thins')).not.toBeInTheDocument();
    });

    it('should render a holiday chip with name, bonus tags, and notes as title', () => {
      render(<HeaderBar {...defaultProps} mythosTime={holidayMythosTime} />);
      const chip = screen.getByText(/Hallowmas/);
      expect(chip).toBeInTheDocument();
      expect(chip.textContent).toContain('harvest bonus');
      expect(chip.closest('span')).toHaveAttribute('title', 'The veil is thin.');
    });

    it('should apply the tradition color palette to a holiday chip', () => {
      render(<HeaderBar {...defaultProps} mythosTime={holidayMythosTime} />);
      const chip = screen.getByText(/Hallowmas/).closest('span');
      expect(chip?.className).toContain('from-violet-400/30');
    });

    it('should render the flavor row for an active holiday even without witching hour', () => {
      render(<HeaderBar {...defaultProps} mythosTime={holidayMythosTime} />);
      expect(screen.getByText('midday')).toBeInTheDocument();
    });
  });

  describe('witching-hour border tint', () => {
    it('should tint the expanded header border during witching hour', () => {
      const { container } = render(<HeaderBar {...defaultProps} mythosTime={witchingMythosTime} />);
      expect(container.firstElementChild?.className).toContain('border-purple-400/60');
    });

    it('should tint the collapsed header border during witching hour', () => {
      const { container } = render(<HeaderBar {...defaultProps} isCollapsed={true} mythosTime={witchingMythosTime} />);
      expect(container.firstElementChild?.className).toContain('border-purple-400/60');
    });

    it('should not tint the border outside witching hour', () => {
      const { container } = render(<HeaderBar {...defaultProps} mythosTime={mockMythosTime} />);
      expect(container.firstElementChild?.className).not.toContain('border-purple-400/60');
    });
  });

  describe('collapse/expand functionality (controlled by GameClientV2)', () => {
    it('should render expanded when isCollapsed is false', () => {
      render(<HeaderBar {...defaultProps} isCollapsed={false} />);
      expect(screen.getByText(/Player: TestPlayer/)).toBeInTheDocument();
      expect(screen.getByLabelText('Collapse header')).toBeInTheDocument();
    });

    it('should render collapsed when isCollapsed is true', () => {
      render(<HeaderBar {...defaultProps} isCollapsed={true} />);
      expect(screen.getByLabelText('Expand header')).toBeInTheDocument();
      expect(screen.queryByText(/Player: TestPlayer/)).not.toBeInTheDocument();
    });

    it('should call onToggleCollapse when the collapse button is clicked', () => {
      const onToggleCollapse = vi.fn();
      render(<HeaderBar {...defaultProps} isCollapsed={false} onToggleCollapse={onToggleCollapse} />);
      fireEvent.click(screen.getByLabelText('Collapse header'));
      expect(onToggleCollapse).toHaveBeenCalledTimes(1);
    });

    it('should call onToggleCollapse when the expand button is clicked', () => {
      const onToggleCollapse = vi.fn();
      render(<HeaderBar {...defaultProps} isCollapsed={true} onToggleCollapse={onToggleCollapse} />);
      fireEvent.click(screen.getByLabelText('Expand header'));
      expect(onToggleCollapse).toHaveBeenCalledTimes(1);
    });

    it('should show player name in collapsed state', () => {
      render(<HeaderBar {...defaultProps} isCollapsed={true} />);
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
