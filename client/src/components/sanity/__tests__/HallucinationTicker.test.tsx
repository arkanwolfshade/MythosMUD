import { render, screen, fireEvent } from '@testing-library/react';
import { describe, it, expect, vi } from 'vitest';
import { HallucinationTicker } from '../HallucinationTicker';
import type { HallucinationMessage } from '../../../types/sanity';

const buildHallucination = (overrides: Partial<HallucinationMessage> = {}): HallucinationMessage => ({
  id: 'hallucination-1',
  title: 'Walls ripple like water',
  severity: 'moderate',
  timestamp: new Date().toISOString(),
  ...overrides,
});

describe('HallucinationTicker', () => {
  it('returns null when there are no hallucinations', () => {
    const { container } = render(<HallucinationTicker hallucinations={[]} />);
    expect(container.firstChild).toBeNull();
  });

  it('renders hallucination title and description', () => {
    const entry = buildHallucination({ description: 'A phantom choir hums in dissonant intervals.' });
    render(<HallucinationTicker hallucinations={[entry]} />);

    expect(screen.getByText(entry.title)).toBeInTheDocument();
    expect(screen.getByText(entry.description!)).toBeInTheDocument();
  });

  it('invokes dismiss callback when dismiss button clicked', () => {
    const onDismiss = vi.fn();
    const entry = buildHallucination();
    render(<HallucinationTicker hallucinations={[entry]} onDismiss={onDismiss} />);

    fireEvent.click(screen.getByRole('button', { name: /dismiss/i }));
    expect(onDismiss).toHaveBeenCalledWith(entry.id);
  });
});
