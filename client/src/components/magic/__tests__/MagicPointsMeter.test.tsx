/**
 * Tests for MagicPointsMeter component.
 */

import { render, screen } from '@testing-library/react';
import { describe, expect, it } from 'vitest';
import { MagicPointsMeter, type MagicPointsStatus } from '../MagicPointsMeter';

describe('MagicPointsMeter', () => {
  const mockStatus: MagicPointsStatus = {
    current: 75,
    max: 100,
  };

  it('should render magic points status', () => {
    render(<MagicPointsMeter status={mockStatus} />);
    expect(screen.getByText('Magic Points')).toBeInTheDocument();
    expect(screen.getByText('75')).toBeInTheDocument();
    expect(screen.getByText('/ 100')).toBeInTheDocument();
  });

  it('should render null when status is null', () => {
    const { container } = render(<MagicPointsMeter status={null} />);
    expect(container.firstChild).toBeNull();
  });

  it('should display correct percentage in progress bar', () => {
    const { container } = render(<MagicPointsMeter status={mockStatus} />);
    const progressBar = container.querySelector('[role="meter"]');
    expect(progressBar).toBeInTheDocument();
    expect(progressBar).toHaveAttribute('aria-valuenow', '75');
    expect(progressBar).toHaveAttribute('aria-valuemax', '100');
    expect(progressBar).toHaveAttribute('aria-valuetext', '75%');
  });

  it('should display change delta when provided', () => {
    const statusWithChange: MagicPointsStatus = {
      current: 80,
      max: 100,
      lastChange: {
        delta: 5,
      },
    };
    render(<MagicPointsMeter status={statusWithChange} />);
    expect(screen.getByText('Recent change')).toBeInTheDocument();
    expect(screen.getByText('+5')).toBeInTheDocument();
  });

  it('should display negative delta correctly', () => {
    const statusWithChange: MagicPointsStatus = {
      current: 70,
      max: 100,
      lastChange: {
        delta: -5,
      },
    };
    render(<MagicPointsMeter status={statusWithChange} />);
    expect(screen.getByText('−5')).toBeInTheDocument();
  });

  it('should display change reason when provided', () => {
    const statusWithChange: MagicPointsStatus = {
      current: 80,
      max: 100,
      lastChange: {
        delta: 5,
        reason: 'rested',
      },
    };
    render(<MagicPointsMeter status={statusWithChange} />);
    // The reason appears in the same span as the change text: "+5 (rested)"
    // Check for the reason text (it's appended with parentheses)
    expect(screen.getByText(/rested/)).toBeInTheDocument();
  });

  it('should not display change text when delta is 0', () => {
    const statusWithZeroChange: MagicPointsStatus = {
      current: 75,
      max: 100,
      lastChange: {
        delta: 0,
      },
    };
    render(<MagicPointsMeter status={statusWithZeroChange} />);
    expect(screen.queryByText('Recent change')).not.toBeInTheDocument();
  });

  it('should not display change text when lastChange is undefined', () => {
    const statusWithoutChange: MagicPointsStatus = {
      current: 75,
      max: 100,
    };
    render(<MagicPointsMeter status={statusWithoutChange} />);
    expect(screen.queryByText('Recent change')).not.toBeInTheDocument();
  });

  it('should clamp percentage to 0-100', () => {
    const overMaxStatus: MagicPointsStatus = {
      current: 150,
      max: 100,
    };
    const { container } = render(<MagicPointsMeter status={overMaxStatus} />);
    const progressBar = container.querySelector('[role="meter"]');
    expect(progressBar).toHaveAttribute('aria-valuetext', '100%');

    const underMinStatus: MagicPointsStatus = {
      current: -10,
      max: 100,
    };
    const { container: container2 } = render(<MagicPointsMeter status={underMinStatus} />);
    const progressBar2 = container2.querySelector('[role="meter"]');
    expect(progressBar2).toHaveAttribute('aria-valuetext', '0%');
  });

  it('should apply custom className', () => {
    const { container } = render(<MagicPointsMeter status={mockStatus} className="custom-class" />);
    const meter = container.querySelector('[data-testid="magic-points-meter"]');
    expect(meter).toHaveClass('custom-class');
  });

  it('should have correct accessibility attributes', () => {
    render(<MagicPointsMeter status={mockStatus} />);
    const meter = screen.getByRole('group', { name: 'Magic Points status' });
    expect(meter).toBeInTheDocument();

    const progressMeter = screen.getByRole('meter');
    expect(progressMeter).toHaveAttribute('aria-valuemin', '0');
    expect(progressMeter).toHaveAttribute('aria-valuemax', '100');
    expect(progressMeter).toHaveAttribute('aria-valuenow', '75');
  });

  it('should round percentage correctly', () => {
    const statusWithDecimal: MagicPointsStatus = {
      current: 33,
      max: 100,
    };
    const { container } = render(<MagicPointsMeter status={statusWithDecimal} />);
    const progressBar = container.querySelector('[role="meter"]');
    expect(progressBar).toHaveAttribute('aria-valuetext', '33%');
  });

  it('should handle edge case of max being 0', () => {
    const statusWithZeroMax: MagicPointsStatus = {
      current: 0,
      max: 0,
    };
    const { container } = render(<MagicPointsMeter status={statusWithZeroMax} />);
    const progressBar = container.querySelector('[role="meter"]');
    // Should handle division by zero gracefully
    expect(progressBar).toBeInTheDocument();
  });

  it('should format delta with absolute value', () => {
    const statusWithLargeDelta: MagicPointsStatus = {
      current: 50,
      max: 100,
      lastChange: {
        delta: -25,
      },
    };
    render(<MagicPointsMeter status={statusWithLargeDelta} />);
    expect(screen.getByText('−25')).toBeInTheDocument();
  });
});
