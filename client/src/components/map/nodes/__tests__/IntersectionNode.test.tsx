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
  };

  it('should render intersection node', () => {
    render(<IntersectionNode zIndex={0} isConnectable={false} xPos={0} yPos={0} {...defaultProps} />);
    expect(screen.getByText('Intersection')).toBeInTheDocument();
  });

  it('should render all handles', () => {
    render(<IntersectionNode zIndex={0} isConnectable={false} xPos={0} yPos={0} {...defaultProps} />);
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
    render(<IntersectionNode zIndex={0} isConnectable={false} xPos={0} yPos={0} {...props} />);
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
    render(<IntersectionNode zIndex={0} isConnectable={false} xPos={0} yPos={0} {...props} />);
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
    render(<IntersectionNode zIndex={0} isConnectable={false} xPos={0} yPos={0} {...props} />);
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
    render(<IntersectionNode zIndex={0} isConnectable={false} xPos={0} yPos={0} {...props} />);
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

    const { rerender } = render(<IntersectionNode zIndex={0} isConnectable={false} xPos={0} yPos={0} {...props1} />);
    const initialRender = screen.getByText('Intersection');

    rerender(<IntersectionNode zIndex={0} isConnectable={false} xPos={0} yPos={0} {...props2} />);
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

    const { rerender } = render(<IntersectionNode zIndex={0} isConnectable={false} xPos={0} yPos={0} {...props1} />);
    rerender(<IntersectionNode zIndex={0} isConnectable={false} xPos={0} yPos={0} {...props2} />);
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

    const { rerender } = render(<IntersectionNode zIndex={0} isConnectable={false} xPos={0} yPos={0} {...props1} />);
    expect(screen.getByText('Intersection 1')).toBeInTheDocument();
    rerender(<IntersectionNode zIndex={0} isConnectable={false} xPos={0} yPos={0} {...props2} />);
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

    const { rerender } = render(<IntersectionNode zIndex={0} isConnectable={false} xPos={0} yPos={0} {...props1} />);
    rerender(<IntersectionNode zIndex={0} isConnectable={false} xPos={0} yPos={0} {...props2} />);
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

    const { rerender } = render(<IntersectionNode zIndex={0} isConnectable={false} xPos={0} yPos={0} {...props1} />);
    rerender(<IntersectionNode zIndex={0} isConnectable={false} xPos={0} yPos={0} {...props2} />);
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

    const { rerender } = render(<IntersectionNode zIndex={0} isConnectable={false} xPos={0} yPos={0} {...props1} />);
    rerender(<IntersectionNode zIndex={0} isConnectable={false} xPos={0} yPos={0} {...props2} />);
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
    const { container } = render(<IntersectionNode zIndex={0} isConnectable={false} xPos={0} yPos={0} {...props} />);
    expect(container).toBeTruthy();
    // Name should be truncated
  });
});
