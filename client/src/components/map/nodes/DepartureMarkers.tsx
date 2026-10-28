/**
 * Markers for exits that leave the area currently drawn.
 *
 * The map is fetched one sub-zone at a time, so an exit into another sub-zone or zone has
 * no node to connect to and no edge is drawn — the Sanitarium door off Derby Street was
 * simply invisible, and the corner read as a dead end.
 *
 * The marker sits on the edge of the node facing the way out, so it reads as a direction
 * rather than a decoration. Vertical exits have no edge to sit on and go in the corner.
 */

import type React from 'react';

/** Where on the node each direction's marker sits, and what it points with. */
const EDGE_POSITION: Record<string, { className: string; glyph: string }> = {
  north: { className: 'top-0 left-1/2 -translate-x-1/2', glyph: '▲' },
  south: { className: 'bottom-0 left-1/2 -translate-x-1/2', glyph: '▼' },
  east: { className: 'right-0 top-1/2 -translate-y-1/2', glyph: '▶' },
  west: { className: 'left-0 top-1/2 -translate-y-1/2', glyph: '◀' },
  up: { className: 'top-0 right-0', glyph: '↑' },
  down: { className: 'bottom-0 right-0', glyph: '↓' },
};

const FALLBACK = { className: 'top-0 right-0', glyph: '✦' };

export interface DepartureMarkersProps {
  /** Directions whose exit leaves the loaded area. */
  departures?: string[];
}

export const DepartureMarkers: React.FC<DepartureMarkersProps> = ({ departures }) => {
  if (!departures || departures.length === 0) {
    return null;
  }

  const label = `Exits to another area: ${departures.join(', ')}`;

  return (
    <>
      {departures.map(direction => {
        const { className, glyph } = EDGE_POSITION[direction.toLowerCase()] ?? FALLBACK;
        return (
          <div
            key={direction}
            // `pointer-events-none` so the marker never swallows a click meant for the node.
            className={`absolute ${className} pointer-events-none px-0.5 text-[10px] font-bold leading-none text-mythos-terminal-warning`}
            title={label}
            aria-label={label}
            data-testid={`departure-${direction.toLowerCase()}`}
          >
            {glyph}
          </div>
        );
      })}
    </>
  );
};
