/**
 * Tests for DepartureMarkers.
 *
 * These mark exits that leave the area currently drawn. The map is fetched one sub-zone
 * at a time, so an exit into another sub-zone has no node to connect to and no edge is
 * drawn — the Sanitarium door off Derby Street was invisible and the corner read as a
 * dead end.
 *
 * The placement assertions check classes rather than geometry on purpose: jsdom has no
 * layout engine, so "is in the document" says nothing about where a user would see it.
 * An earlier version of this marker rendered correctly into the DOM and landed off the
 * node entirely, because its container had no positioning context.
 */

import { render, screen } from '@testing-library/react';
import { describe, expect, it } from 'vitest';
import { DepartureMarkers } from '../DepartureMarkers';

describe('DepartureMarkers', () => {
  it('renders nothing when there are no departures', () => {
    const { container } = render(<DepartureMarkers departures={[]} />);
    expect(container).toBeEmptyDOMElement();
  });

  it('renders nothing when departures are absent entirely', () => {
    const { container } = render(<DepartureMarkers />);
    expect(container).toBeEmptyDOMElement();
  });

  it('renders one marker per departing direction', () => {
    render(<DepartureMarkers departures={['north', 'east', 'down']} />);
    expect(screen.getByTestId('departure-north')).toBeInTheDocument();
    expect(screen.getByTestId('departure-east')).toBeInTheDocument();
    expect(screen.getByTestId('departure-down')).toBeInTheDocument();
  });

  it.each([
    ['north', 'top-0'],
    ['south', 'bottom-0'],
    ['east', 'right-0'],
    ['west', 'left-0'],
  ])('places the %s marker on the matching edge', (direction, edgeClass) => {
    render(<DepartureMarkers departures={[direction]} />);
    const marker = screen.getByTestId(`departure-${direction}`);
    expect(marker.className).toContain('absolute');
    expect(marker.className).toContain(edgeClass);
  });

  it('falls back to a corner for a direction with no edge of its own', () => {
    // The engine accepts diagonals; they have no single edge to sit on, but they must
    // still be visible rather than silently dropped.
    render(<DepartureMarkers departures={['northeast']} />);
    const marker = screen.getByTestId('departure-northeast');
    expect(marker).toBeInTheDocument();
    expect(marker.className).toContain('absolute');
  });

  it('matches directions case-insensitively', () => {
    render(<DepartureMarkers departures={['NORTH']} />);
    expect(screen.getByTestId('departure-north').className).toContain('top-0');
  });

  it('labels every marker with the full set of directions', () => {
    render(<DepartureMarkers departures={['north', 'west']} />);
    expect(screen.getAllByLabelText('Exits to another area: north, west')).toHaveLength(2);
  });

  it('never intercepts a click meant for the node beneath it', () => {
    render(<DepartureMarkers departures={['north', 'south']} />);
    for (const direction of ['north', 'south']) {
      expect(screen.getByTestId(`departure-${direction}`).className).toContain('pointer-events-none');
    }
  });
});
