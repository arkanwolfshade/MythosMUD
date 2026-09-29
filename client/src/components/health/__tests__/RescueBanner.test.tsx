import { act, render, screen } from '@testing-library/react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import { RESCUE_TERMINAL_DISPLAY_MS, type RescueStatus } from '../../../types/rescue';
import { RescueBanner } from '../RescueBanner';

const status = (overrides: Partial<RescueStatus> = {}): RescueStatus => ({
  status: 'channeling',
  role: 'target',
  rescuerName: 'Armitage',
  targetName: 'Wilmarth',
  message: 'Armitage kneels beside you and begins the grounding ritual.',
  etaSeconds: 10,
  seq: 1,
  ...overrides,
});

describe('RescueBanner', () => {
  beforeEach(() => {
    vi.useFakeTimers();
  });
  afterEach(() => {
    vi.useRealTimers();
  });

  it('renders nothing when there is no rescue phase and the player is not catatonic', () => {
    const { container } = render(<RescueBanner rescueStatus={null} isCatatonic={false} />);
    expect(container).toBeEmptyDOMElement();
  });

  it('words the headline for each side but shows the server line as the body', () => {
    const { rerender } = render(<RescueBanner rescueStatus={status()} isCatatonic />);
    expect(screen.getByText('Being Grounded')).toBeInTheDocument();
    expect(screen.getByText(/kneels beside you/i)).toBeInTheDocument();

    rerender(
      <RescueBanner
        rescueStatus={status({ role: 'rescuer', seq: 2, message: 'You steady Wilmarth and begin channeling focus.' })}
        isCatatonic={false}
      />
    );
    expect(screen.getByText('Grounding')).toBeInTheDocument();
    expect(screen.getByText(/you steady wilmarth/i)).toBeInTheDocument();
  });

  it('animates the ETA bar over the server-provided eta_seconds while channeling', () => {
    render(<RescueBanner rescueStatus={status({ etaSeconds: 7 })} isCatatonic />);
    expect(screen.getByTestId('rescue-banner-progress')).toHaveStyle({ animationDuration: '7s' });
  });

  it('shows no ETA bar for a terminal phase', () => {
    render(<RescueBanner rescueStatus={status({ status: 'success', etaSeconds: undefined })} isCatatonic={false} />);
    expect(screen.queryByTestId('rescue-banner-progress')).not.toBeInTheDocument();
    expect(screen.getByText('Mind Steadied')).toBeInTheDocument();
  });

  it('shows the catatonic state, derived from the tier, when no rescue phase is active', () => {
    render(<RescueBanner rescueStatus={null} isCatatonic />);
    expect(screen.getByText('Catatonic')).toBeInTheDocument();
    expect(screen.getByText(/only allies can reach you/i)).toBeInTheDocument();
  });

  it('clears a terminal phase after the display window and falls back to catatonic if the tier says so', () => {
    render(<RescueBanner rescueStatus={status({ status: 'failed', etaSeconds: undefined })} isCatatonic />);
    expect(screen.getByText('Grounding Failed')).toBeInTheDocument();

    act(() => {
      vi.advanceTimersByTime(RESCUE_TERMINAL_DISPLAY_MS);
    });

    expect(screen.queryByText('Grounding Failed')).not.toBeInTheDocument();
    expect(screen.getByText('Catatonic')).toBeInTheDocument();
  });

  it('clears a terminal phase entirely when the player is no longer catatonic', () => {
    const { container } = render(
      <RescueBanner rescueStatus={status({ status: 'success', etaSeconds: undefined })} isCatatonic={false} />
    );
    act(() => {
      vi.advanceTimersByTime(RESCUE_TERMINAL_DISPLAY_MS);
    });
    expect(container).toBeEmptyDOMElement();
  });

  it('expires a channeling phase only after its ETA plus the grace window, in case the terminal event is lost', () => {
    render(<RescueBanner rescueStatus={status({ etaSeconds: 10 })} isCatatonic={false} />);

    act(() => {
      vi.advanceTimersByTime(10_000 + RESCUE_TERMINAL_DISPLAY_MS - 1);
    });
    expect(screen.getByText('Being Grounded')).toBeInTheDocument();

    act(() => {
      vi.advanceTimersByTime(1);
    });
    expect(screen.queryByText('Being Grounded')).not.toBeInTheDocument();
  });

  it('restarts the expiry window when a new phase arrives', () => {
    const { rerender } = render(
      <RescueBanner rescueStatus={status({ status: 'failed', seq: 1 })} isCatatonic={false} />
    );
    act(() => {
      vi.advanceTimersByTime(RESCUE_TERMINAL_DISPLAY_MS - 1000);
    });

    rerender(<RescueBanner rescueStatus={status({ status: 'interrupted', seq: 2 })} isCatatonic={false} />);
    act(() => {
      vi.advanceTimersByTime(RESCUE_TERMINAL_DISPLAY_MS - 1000);
    });

    expect(screen.getByText('Grounding Interrupted')).toBeInTheDocument();
  });

  it('is a polite live region', () => {
    render(<RescueBanner rescueStatus={status()} isCatatonic />);
    const banner = screen.getByTestId('rescue-banner');
    expect(banner).toHaveAttribute('role', 'status');
    expect(banner).toHaveAttribute('aria-live', 'polite');
  });
});
