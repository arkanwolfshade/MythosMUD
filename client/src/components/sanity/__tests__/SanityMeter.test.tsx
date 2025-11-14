import { render, screen } from '@testing-library/react';
import { describe, it, expect } from 'vitest';
import { SanityMeter } from '../SanityMeter';
import type { SanityStatus } from '../../../types/sanity';

const buildStatus = (overrides: Partial<SanityStatus> = {}): SanityStatus => ({
  current: 82,
  max: 100,
  tier: 'uneasy',
  liabilities: [],
  ...overrides,
});

describe('SanityMeter', () => {
  it('renders current sanity and tier label', () => {
    const status = buildStatus();
    render(<SanityMeter status={status} />);

    expect(screen.getByText(/82/)).toBeInTheDocument();
    expect(screen.getByText(/Uneasy/i)).toBeInTheDocument();
  });

  it('announces recent change with reason', () => {
    const status = buildStatus({
      lastChange: {
        delta: -6,
        reason: 'disturbing_encounter',
        timestamp: new Date().toISOString(),
      },
    });

    render(<SanityMeter status={status} />);

    expect(screen.getByText('−6 (disturbing encounter)')).toBeInTheDocument();
    expect(screen.getByText(/disturbing encounter/i)).toBeInTheDocument();
  });

  it('renders liabilities when provided', () => {
    const status = buildStatus({
      liabilities: ['night_frayed_reflexes'],
    });

    render(<SanityMeter status={status} />);

    expect(screen.getByText(/night frayed reflexes/i)).toBeInTheDocument();
  });

  it('returns null when status is null', () => {
    const { container } = render(<SanityMeter status={null} />);
    expect(container.firstChild).toBeNull();
  });
});
