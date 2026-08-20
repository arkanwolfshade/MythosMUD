/**
 * AsciiNoise: replaces an ASCII map surface with churning noise for deranged-tier players (#626).
 *
 * Renders as plain text in a <pre> -- deliberately bypasses SafeHtml/DOMPurify since the content
 * is generated locally, never from the server or another user.
 */

import React, { useEffect, useMemo, useState } from 'react';
import { generateAsciiNoise, mulberry32 } from '../../utils/directionHallucination';

const CHURN_INTERVAL_MS = 500;

interface AsciiNoiseProps {
  /** Number of noise lines to render. */
  rows: number;
  /** Characters per noise line. */
  cols: number;
  /** Seeds the static frame shown when reduced motion is preferred, and the very first frame. */
  seed: number;
  className?: string;
}

function prefersReducedMotion(): boolean {
  return typeof window !== 'undefined' && window.matchMedia?.('(prefers-reduced-motion: reduce)').matches === true;
}

export const AsciiNoise: React.FC<AsciiNoiseProps> = ({ rows, cols, seed, className }) => {
  // Static frame: recomputed only when dimensions/seed change, used as-is when motion is reduced
  // and as the first paint before churn kicks in otherwise.
  const staticFrame = useMemo(() => generateAsciiNoise(rows, cols, mulberry32(seed)), [rows, cols, seed]);
  const [frame, setFrame] = useState(staticFrame);

  // "Adjusting state when a prop changes" pattern (react.dev) -- setState during render, not in an
  // effect, so a room/seed change resets the displayed frame without an extra render-then-flicker.
  const [renderedStaticFrame, setRenderedStaticFrame] = useState(staticFrame);
  if (staticFrame !== renderedStaticFrame) {
    setRenderedStaticFrame(staticFrame);
    setFrame(staticFrame);
  }

  useEffect(() => {
    if (prefersReducedMotion()) {
      return;
    }
    const interval = window.setInterval(() => {
      setFrame(generateAsciiNoise(rows, cols, Math.random));
    }, CHURN_INTERVAL_MS);
    return () => window.clearInterval(interval);
  }, [rows, cols]);

  return <pre className={className}>{frame}</pre>;
};
