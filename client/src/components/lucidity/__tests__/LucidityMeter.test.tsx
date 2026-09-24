import { render, screen } from '@testing-library/react';
import { describe, it, expect } from 'vitest';
import { LucidityMeter } from '../LucidityMeter';
import type { LucidityStatus } from '../../../types/lucidity';

const buildStatus = (overrides: Partial<LucidityStatus> = {}): LucidityStatus => ({
  current: 82,
  max: 100,
  tier: 'uneasy',
  liabilities: [],
  ...overrides,
});

describe('LucidityMeter', () => {
  it('renders current lucidity and tier label', () => {
    const status = buildStatus();
    render(<LucidityMeter status={status} />);

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

    render(<LucidityMeter status={status} />);

    expect(screen.getByText('−6 (disturbing encounter)')).toBeInTheDocument();
    expect(screen.getByText(/disturbing encounter/i)).toBeInTheDocument();
  });

  it('renders liabilities when provided', () => {
    const status = buildStatus({
      liabilities: ['night_frayed_reflexes'],
    });

    render(<LucidityMeter status={status} />);

    expect(screen.getByText(/night frayed reflexes/i)).toBeInTheDocument();
  });

  it('returns null when status is null', () => {
    const { container } = render(<LucidityMeter status={null} />);
    expect(container.firstChild).toBeNull();
  });

  it('renders a neutral placeholder when no server tier has arrived yet', () => {
    // tier is optional: the server is authoritative for it (game_state/lucidity_change), and the
    // client must not invent one (see server-authority.mdc / CLIENT_SERVER_AUTHORITY_REGISTER_2026-09).
    const status = buildStatus({ tier: undefined });
    render(<LucidityMeter status={status} />);

    expect(screen.getByText(/82/)).toBeInTheDocument();
    expect(screen.getByText('—')).toBeInTheDocument();
    expect(screen.queryByText(/^(Uneasy|Lucid|Fractured|Deranged|Catatonic)$/i)).not.toBeInTheDocument();
  });
});
