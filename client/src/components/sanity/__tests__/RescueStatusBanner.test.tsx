import { render, screen } from '@testing-library/react';
import { describe, it, expect } from 'vitest';
import { RescueStatusBanner } from '../RescueStatusBanner';
import type { RescueState } from '../../../types/sanity';

const buildRescueState = (overrides: Partial<RescueState> = {}): RescueState => ({
  status: 'channeling',
  progress: 42,
  rescuerName: 'Professor Armitage',
  targetName: 'Investigator Keziah',
  timestamp: new Date().toISOString(),
  ...overrides,
});

describe('RescueStatusBanner', () => {
  it('returns null when state is null or idle', () => {
    const { container } = render(<RescueStatusBanner state={null} />);
    expect(container.firstChild).toBeNull();

    const { container: idleContainer } = render(<RescueStatusBanner state={buildRescueState({ status: 'idle' })} />);
    expect(idleContainer.firstChild).toBeNull();
  });

  it('renders progress information for channeling state', () => {
    render(<RescueStatusBanner state={buildRescueState()} />);
    expect(screen.getByText(/Rescue ritual/i)).toBeInTheDocument();
    expect(screen.getByText(/42%/)).toBeInTheDocument();
  });

  it('announces success message', () => {
    render(<RescueStatusBanner state={buildRescueState({ status: 'success', progress: undefined })} />);
    expect(screen.getByText(/Sanity tether restored/i)).toBeInTheDocument();
  });
});
