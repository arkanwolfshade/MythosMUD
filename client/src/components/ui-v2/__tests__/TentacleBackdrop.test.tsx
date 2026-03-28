/**
 * TentacleBackdrop: decorative layer behind panels (pointer-events none, aria-hidden).
 */

import { render, screen } from '@testing-library/react';
import { describe, expect, it } from 'vitest';
import { TentacleBackdrop } from '../TentacleBackdrop';

describe('TentacleBackdrop', () => {
  it('renders inside a relative container', () => {
    const { container } = render(
      <div className="relative h-40 w-full">
        <TentacleBackdrop />
      </div>
    );
    expect(container.querySelector('.relative')).toBeInTheDocument();
    expect(screen.getByTestId('tentacle-backdrop')).toBeInTheDocument();
  });

  it('is decorative and non-interactive', () => {
    render(
      <div className="relative">
        <TentacleBackdrop />
      </div>
    );
    const root = screen.getByTestId('tentacle-backdrop');
    expect(root).toHaveAttribute('aria-hidden', 'true');
    expect(root.className).toMatch(/pointer-events-none/);
    expect(root.className).toMatch(/absolute\s+inset-0/);
  });

  it('includes svg tentacle strokes', () => {
    const { container } = render(
      <div className="relative">
        <TentacleBackdrop />
      </div>
    );
    const svg = container.querySelector('svg.mythos-tentacle-svg');
    expect(svg).toBeInTheDocument();
    expect(container.querySelectorAll('path.mythos-tentacle-stroke').length).toBeGreaterThanOrEqual(3);
  });
});
