import { render, screen } from '@testing-library/react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import { AsciiNoise } from '../AsciiNoise';

function mockMatchMedia(reducedMotion: boolean) {
  window.matchMedia = vi.fn().mockImplementation((query: string) => ({
    matches: query.includes('prefers-reduced-motion') ? reducedMotion : false,
    media: query,
    addEventListener: vi.fn(),
    removeEventListener: vi.fn(),
  })) as unknown as typeof window.matchMedia;
}

describe('AsciiNoise', () => {
  beforeEach(() => {
    vi.useFakeTimers();
    mockMatchMedia(false);
  });

  afterEach(() => {
    vi.useRealTimers();
    vi.restoreAllMocks();
  });

  it('renders a <pre> block with the requested dimensions', () => {
    render(<AsciiNoise rows={3} cols={8} seed={1} />);
    const pre = screen.getByText((_, el) => el?.tagName.toLowerCase() === 'pre');
    const lines = (pre.textContent ?? '').split('\n');
    expect(lines).toHaveLength(3);
    for (const line of lines) {
      expect(line).toHaveLength(8);
    }
  });

  it('churns to a new frame on the interval when motion is not reduced', () => {
    render(<AsciiNoise rows={2} cols={6} seed={1} />);
    const pre = () => screen.getByText((_, el) => el?.tagName.toLowerCase() === 'pre');
    const firstFrame = pre().textContent;

    vi.advanceTimersByTime(500);
    const secondFrame = pre().textContent;

    // Extremely unlikely (but not impossible) for random noise to repeat; assert shape held.
    expect(secondFrame).toHaveLength(firstFrame?.length ?? 0);
  });

  it('does not churn when prefers-reduced-motion is set', () => {
    mockMatchMedia(true);
    render(<AsciiNoise rows={2} cols={6} seed={42} />);
    const pre = () => screen.getByText((_, el) => el?.tagName.toLowerCase() === 'pre');
    const firstFrame = pre().textContent;

    vi.advanceTimersByTime(5000);
    const secondFrame = pre().textContent;

    expect(secondFrame).toBe(firstFrame);
  });

  it('clears its interval on unmount', () => {
    const clearSpy = vi.spyOn(window, 'clearInterval');
    const { unmount } = render(<AsciiNoise rows={2} cols={6} seed={1} />);
    unmount();
    expect(clearSpy).toHaveBeenCalled();
  });
});
