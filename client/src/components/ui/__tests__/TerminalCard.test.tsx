/**
 * Tests for TerminalCard component.
 */

import { render, screen } from '@testing-library/react';
import { describe, expect, it } from 'vitest';
import { TerminalCard } from '../TerminalCard';

describe('TerminalCard', () => {
  it('should render card with children', () => {
    render(
      <TerminalCard>
        <div>Card content</div>
      </TerminalCard>
    );

    expect(screen.getByText('Card content')).toBeInTheDocument();
  });

  it('should render card with title', () => {
    render(
      <TerminalCard title="Test Title">
        <div>Card content</div>
      </TerminalCard>
    );

    expect(screen.getByText('Test Title')).toBeInTheDocument();
    expect(screen.getByText('Card content')).toBeInTheDocument();
  });

  it('should render card without title', () => {
    render(
      <TerminalCard>
        <div>Card content</div>
      </TerminalCard>
    );

    expect(screen.queryByText('Test Title')).not.toBeInTheDocument();
    expect(screen.getByText('Card content')).toBeInTheDocument();
  });

  it('should handle default variant', () => {
    const { container } = render(
      <TerminalCard variant="default">
        <div>Content</div>
      </TerminalCard>
    );

    expect(container.firstChild).toBeInTheDocument();
  });

  it('should handle elevated variant', () => {
    const { container } = render(
      <TerminalCard variant="elevated">
        <div>Content</div>
      </TerminalCard>
    );

    expect(container.firstChild).toBeInTheDocument();
  });

  it('should handle outlined variant', () => {
    const { container } = render(
      <TerminalCard variant="outlined">
        <div>Content</div>
      </TerminalCard>
    );

    expect(container.firstChild).toBeInTheDocument();
  });

  it('should handle custom className', () => {
    const { container } = render(
      <TerminalCard className="custom-class">
        <div>Content</div>
      </TerminalCard>
    );

    const card = container.firstChild as HTMLElement;
    expect(card.className).toContain('custom-class');
  });

  it('should render multiple children', () => {
    render(
      <TerminalCard>
        <div>First</div>
        <div>Second</div>
      </TerminalCard>
    );

    expect(screen.getByText('First')).toBeInTheDocument();
    expect(screen.getByText('Second')).toBeInTheDocument();
  });
});
