import React from 'react';

/**
 * Decorative full-viewport tentacle line-art behind all panels. Keep panels opaque; this only fills gaps.
 * Tiled SVG pattern for dense, fine line-art; swap pattern defs or embed an image later.
 */
export const TentacleBackdrop: React.FC = () => (
  <div
    className="pointer-events-none absolute inset-0 z-0 select-none overflow-hidden"
    aria-hidden="true"
    data-testid="tentacle-backdrop"
  >
    <svg
      className="mythos-tentacle-svg h-full w-full"
      xmlns="http://www.w3.org/2000/svg"
      preserveAspectRatio="xMidYMid slice"
      viewBox="0 0 1200 800"
    >
      <defs>
        <pattern
          id="mythos-tentacle-tile"
          width="88"
          height="88"
          patternUnits="userSpaceOnUse"
          patternContentUnits="userSpaceOnUse"
        >
          <path className="mythos-tentacle-stroke mythos-tentacle-stroke--tile-a" d="M -6 72 Q 22 38 48 44 T 94 18" />
          <path className="mythos-tentacle-stroke mythos-tentacle-stroke--tile-b" d="M 72 96 Q 52 58 28 42 T 8 6" />
          <path className="mythos-tentacle-stroke mythos-tentacle-stroke--tile-c" d="M 0 24 Q 30 8 58 22 T 86 4" />
          <path className="mythos-tentacle-stroke mythos-tentacle-stroke--tile-d" d="M 44 80 Q 62 52 38 28 T 18 -4" />
          <path
            className="mythos-tentacle-stroke mythos-tentacle-stroke--tile-e mythos-tentacle-dash-path"
            d="M 10 50 Q 36 62 54 40 T 78 22"
          />
        </pattern>
      </defs>
      <g className="mythos-tentacle-drift">
        <rect width="1200" height="800" fill="url(#mythos-tentacle-tile)" />
      </g>
    </svg>
  </div>
);

TentacleBackdrop.displayName = 'TentacleBackdrop';
