import { render, screen } from '@testing-library/react';

import { HealthMeter } from '../HealthMeter';
import type { HealthStatus } from '../../../types/health';

const buildStatus = (overrides: Partial<HealthStatus> = {}): HealthStatus => ({
  current: 70,
  max: 100,
  tier: 'steady',
  ...overrides,
});

describe('HealthMeter', () => {
  it('renders nothing when no status is provided', () => {
    const { container } = render(<HealthMeter status={null} />);
    expect(container.firstChild).toBeNull();
  });

  it('shows current and max health', () => {
    render(<HealthMeter status={buildStatus({ current: 55 })} />);
    expect(screen.getByText('55')).toBeInTheDocument();
    expect(screen.getByText(/\/\s*100/)).toBeInTheDocument();
  });

  it('formats recent change when provided', () => {
    render(
      <HealthMeter
        status={buildStatus({
          lastChange: { delta: -12, reason: 'combat', timestamp: new Date().toISOString() },
        })}
      />
    );
    expect(screen.getByText('-12 (combat)')).toBeInTheDocument();
  });

  it('displays posture information when supplied', () => {
    render(<HealthMeter status={buildStatus({ posture: 'kneeling' })} />);
    expect(screen.getByText('kneeling')).toBeInTheDocument();
  });
});
