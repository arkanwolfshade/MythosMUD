import { render, screen } from '@testing-library/react';
import { describe, expect, it } from 'vitest';
import { IncapacitatedBanner } from '../IncapacitatedBanner';

describe('IncapacitatedBanner', () => {
  it('renders the flavor headline and the mechanics line', () => {
    render(<IncapacitatedBanner />);
    expect(screen.getByText(/darkness closes in on your vision/i)).toBeInTheDocument();
    expect(screen.getByText(/cannot attack or cast spells/i)).toBeInTheDocument();
  });

  it('has status/live-region semantics for a self-clearing state announcement', () => {
    render(<IncapacitatedBanner />);
    const banner = screen.getByTestId('incapacitated-banner');
    expect(banner).toHaveAttribute('role', 'status');
    expect(banner).toHaveAttribute('aria-live', 'assertive');
  });

  it.each([
    [0, '10 seconds'],
    [-3, '7 seconds'],
    [-9, '1 second'],
    [-10, '0 seconds'],
  ])('counts down from server DP: %i DP leaves %s (#1059)', (currentDp, expected) => {
    render(<IncapacitatedBanner currentDp={currentDp} />);
    expect(screen.getByTestId('bleed-out-countdown')).toHaveTextContent(`bleeding out: ${expected} remain`);
  });

  it('shows no countdown when DP is unknown', () => {
    render(<IncapacitatedBanner />);
    expect(screen.queryByTestId('bleed-out-countdown')).not.toBeInTheDocument();
  });

  it('renders no dismiss control (self-clearing only, per #715)', () => {
    render(<IncapacitatedBanner />);
    expect(screen.queryByRole('button')).not.toBeInTheDocument();
  });
});
