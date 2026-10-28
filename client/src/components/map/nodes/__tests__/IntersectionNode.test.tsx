/**
 * Tests for IntersectionNode component.
 */

import { render, screen } from '@testing-library/react';
import { describe, expect, it, vi } from 'vitest';
import type { RoomNodeData } from '../../types';
import { IntersectionNode } from '../IntersectionNode';

// Mock reactflow
vi.mock('reactflow', () => ({
  Handle: ({ position, type }: { position: string; type: string }) => (
    <div data-testid={`handle-${type}-${position}`} />
  ),
  Position: {
    Top: 'top',
    Right: 'right',
    Bottom: 'bottom',
    Left: 'left',
  },
}));

describe('IntersectionNode', () => {
  const defaultData: RoomNodeData = {
    id: 'intersection1',
    name: 'Intersection',
    description: 'A crossroads intersection',
    isCurrentLocation: false,
    hasUnsavedChanges: false,
  };

  const defaultProps = {
    id: 'node1',
    type: 'intersection',
    position: { x: 0, y: 0 },
    data: defaultData,
    selected: false,
    dragging: false,
    zIndex: 0,
    isConnectable: false,
    xPos: 0,
    yPos: 0,
  };

  it('should render intersection node', () => {
    render(<IntersectionNode {...defaultProps} />);
    expect(screen.getByText('Intersection')).toBeInTheDocument();
  });

  it('should render all handles', () => {
    render(<IntersectionNode {...defaultProps} />);
    expect(screen.getByTestId('handle-target-top')).toBeInTheDocument();
    expect(screen.getByTestId('handle-target-right')).toBeInTheDocument();
    expect(screen.getByTestId('handle-target-bottom')).toBeInTheDocument();
    expect(screen.getByTestId('handle-target-left')).toBeInTheDocument();
    expect(screen.getByTestId('handle-source-top')).toBeInTheDocument();
    expect(screen.getByTestId('handle-source-right')).toBeInTheDocument();
    expect(screen.getByTestId('handle-source-bottom')).toBeInTheDocument();
    expect(screen.getByTestId('handle-source-left')).toBeInTheDocument();
  });

  it('should render node with current location', () => {
    const props = {
      ...defaultProps,
      data: {
        ...defaultData,
        isCurrentLocation: true,
      },
    };
    render(<IntersectionNode {...props} />);
    expect(screen.getByText('Intersection')).toBeInTheDocument();
  });

  it('should render node with unsaved changes', () => {
    const props = {
      ...defaultProps,
      data: {
        ...defaultData,
        hasUnsavedChanges: true,
      },
    };
    render(<IntersectionNode {...props} />);
    expect(screen.getByText('Intersection')).toBeInTheDocument();
  });

  it('should render node with different environment', () => {
    const props = {
      ...defaultProps,
      data: {
        ...defaultData,
        environment: 'indoors',
      },
    };
    render(<IntersectionNode {...props} />);
    expect(screen.getByText('Intersection')).toBeInTheDocument();
  });

  it('should render node with subzone', () => {
    const props = {
      ...defaultProps,
      data: {
        ...defaultData,
        subZone: 'campus',
      },
    };
    render(<IntersectionNode {...props} />);
    expect(screen.getByText('Intersection')).toBeInTheDocument();
  });

  it('should memoize component and prevent unnecessary re-renders', () => {
    const props1 = {
      ...defaultProps,
      data: {
        ...defaultData,
        id: 'intersection1',
        name: 'Intersection',
        isCurrentLocation: false,
        hasUnsavedChanges: false,
        environment: undefined,
        subZone: undefined,
      },
    };

    const props2 = {
      ...props1,
      // Same props - should not re-render
    };

    const { rerender } = render(<IntersectionNode {...props1} />);
    const initialRender = screen.getByText('Intersection');

    rerender(<IntersectionNode {...props2} />);
    const afterRerender = screen.getByText('Intersection');

    expect(initialRender).toBe(afterRerender);
  });

  it('should re-render when data changes', () => {
    const props1 = {
      ...defaultProps,
      data: {
        ...defaultData,
        isCurrentLocation: false,
      },
    };

    const props2 = {
      ...defaultProps,
      data: {
        ...defaultData,
        isCurrentLocation: true,
      },
    };

    const { rerender } = render(<IntersectionNode {...props1} />);
    rerender(<IntersectionNode {...props2} />);
    // Component should re-render when isCurrentLocation changes
  });

  it('should re-render when name changes', () => {
    const props1 = {
      ...defaultProps,
      data: {
        ...defaultData,
        name: 'Intersection 1',
      },
    };

    const props2 = {
      ...defaultProps,
      data: {
        ...defaultData,
        name: 'Intersection 2',
      },
    };

    const { rerender } = render(<IntersectionNode {...props1} />);
    expect(screen.getByText('Intersection 1')).toBeInTheDocument();
    rerender(<IntersectionNode {...props2} />);
    expect(screen.getByText('Intersection 2')).toBeInTheDocument();
  });

  it('should re-render when hasUnsavedChanges changes', () => {
    const props1 = {
      ...defaultProps,
      data: {
        ...defaultData,
        hasUnsavedChanges: false,
      },
    };

    const props2 = {
      ...defaultProps,
      data: {
        ...defaultData,
        hasUnsavedChanges: true,
      },
    };

    const { rerender } = render(<IntersectionNode {...props1} />);
    rerender(<IntersectionNode {...props2} />);
    // Component should re-render when hasUnsavedChanges changes
  });

  it('should re-render when environment changes', () => {
    const props1 = {
      ...defaultProps,
      data: {
        ...defaultData,
        environment: 'outdoors',
      },
    };

    const props2 = {
      ...defaultProps,
      data: {
        ...defaultData,
        environment: 'indoors',
      },
    };

    const { rerender } = render(<IntersectionNode {...props1} />);
    rerender(<IntersectionNode {...props2} />);
    // Component should re-render when environment changes
  });

  it('should re-render when subZone changes', () => {
    const props1 = {
      ...defaultProps,
      data: {
        ...defaultData,
        subZone: 'campus',
      },
    };

    const props2 = {
      ...defaultProps,
      data: {
        ...defaultData,
        subZone: 'downtown',
      },
    };

    const { rerender } = render(<IntersectionNode {...props1} />);
    rerender(<IntersectionNode {...props2} />);
    // Component should re-render when subZone changes
  });

  it('should handle long intersection names with truncation', () => {
    const props = {
      ...defaultProps,
      data: {
        ...defaultData,
        name: 'A Very Long Intersection Name That Should Be Truncated',
      },
    };
    const { container } = render(<IntersectionNode {...props} />);
    expect(container).toBeTruthy();
    // Name should be truncated
  });

  describe('departure marker (#829)', () => {
    // A map request covers one sub-zone, so an exit into another sub-zone has no node to
    // connect to and no edge is drawn. Without a marker on the room itself, the only way
    // into a building like the Sanitarium is invisible and the corner reads as a dead end.
    it('shows a marker when the room has an exit leaving the area', () => {
      render(<IntersectionNode {...defaultProps} data={{ ...defaultData, departures: ['north'] }} />);
      expect(screen.getByLabelText('Exits to another area: north')).toBeInTheDocument();
    });

    it('names every departing direction in the label', () => {
      render(<IntersectionNode {...defaultProps} data={{ ...defaultData, departures: ['north', 'down'] }} />);
      // One marker per direction, each carrying the full list in its label.
      expect(screen.getAllByLabelText('Exits to another area: north, down')).toHaveLength(2);
    });

    it('anchors the marker to the node itself', () => {
      // The marker is absolutely positioned. Without `relative` on the node it resolves
      // against some ancestor further up and renders somewhere else on the canvas
      // entirely - present in the DOM, invisible on the map. Querying by label passes
      // either way, so the positioning context has to be asserted directly.
      const { container } = render(
        <IntersectionNode {...defaultProps} data={{ ...defaultData, departures: ['north'] }} />
      );
      const marker = screen.getByLabelText('Exits to another area: north');
      const anchor = marker.closest('.relative');
      expect(anchor).not.toBeNull();
      expect(container.contains(anchor)).toBe(true);
    });

    it('places the marker on the edge facing the way out', () => {
      render(<IntersectionNode {...defaultProps} data={{ ...defaultData, departures: ['north', 'east'] }} />);
      expect(screen.getByTestId('departure-north')).toBeInTheDocument();
      expect(screen.getByTestId('departure-east')).toBeInTheDocument();
    });

    it('does not intercept clicks meant for the node', () => {
      render(<IntersectionNode {...defaultProps} data={{ ...defaultData, departures: ['north'] }} />);
      expect(screen.getByTestId('departure-north').className).toContain('pointer-events-none');
    });

    it('shows no marker when every exit stays inside the area', () => {
      render(<IntersectionNode {...defaultProps} data={{ ...defaultData, departures: [] }} />);
      expect(screen.queryByLabelText(/Exits to another area/)).not.toBeInTheDocument();
    });

    it('shows no marker when departures are absent entirely', () => {
      render(<IntersectionNode {...defaultProps} data={defaultData} />);
      expect(screen.queryByLabelText(/Exits to another area/)).not.toBeInTheDocument();
    });
  });
});
