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

  it('renders no dismiss control (self-clearing only, per #715)', () => {
    render(<IncapacitatedBanner />);
    expect(screen.queryByRole('button')).not.toBeInTheDocument();
  });
});
