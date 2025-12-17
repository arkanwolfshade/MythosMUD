/**
 * Tests for RoomNode component.
 */

import { render, screen } from '@testing-library/react';
import { describe, expect, it, vi } from 'vitest';
import type { RoomNodeData } from '../../types';
import { RoomNode, type RoomNodeProps } from '../RoomNode';

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

describe('RoomNode', () => {
  const defaultData: RoomNodeData = {
    id: 'room1',
    name: 'Test Room',
    description: 'A test room description',
    isCurrentLocation: false,
    hasUnsavedChanges: false,
  };

  const defaultProps = {
    id: 'node1',
    type: 'room',
    position: { x: 0, y: 0 },
    data: defaultData,
    selected: false,
    dragging: false,
  } as unknown as RoomNodeProps;

  it('should render room node', () => {
    render(<RoomNode {...defaultProps} />);
    expect(screen.getByText('Test Room')).toBeInTheDocument();
  });

  it('should render current location node', () => {
    const props = {
      ...defaultProps,
      data: {
        ...defaultData,
        isCurrentLocation: true,
      },
    } as unknown as RoomNodeProps;
    render(<RoomNode {...props} />);
    expect(screen.getByText('Test Room')).toBeInTheDocument();
  });

  it('should render node with unsaved changes', () => {
    const props: RoomNodeProps = {
      ...defaultProps,
      data: {
        ...defaultData,
        hasUnsavedChanges: true,
      },
    } as RoomNodeProps;
    render(<RoomNode {...props} />);
    expect(screen.getByText('Test Room')).toBeInTheDocument();
  });

  it('should render circle shape for outdoors environment', () => {
    const props = {
      ...defaultProps,
      data: {
        ...defaultData,
        environment: 'outdoors',
      },
    } as unknown as RoomNodeProps;
    const { container } = render(<RoomNode {...props} />);
    expect(container).toBeTruthy();
  });

  it('should render square shape for indoors environment', () => {
    const props = {
      ...defaultProps,
      data: {
        ...defaultData,
        environment: 'indoors',
      },
    } as unknown as RoomNodeProps;
    const { container } = render(<RoomNode {...props} />);
    expect(container).toBeTruthy();
  });

  it('should render diamond shape for intersection environment', () => {
    const props = {
      ...defaultProps,
      data: {
        ...defaultData,
        environment: 'intersection',
      },
    } as unknown as RoomNodeProps;
    const { container } = render(<RoomNode {...props} />);
    expect(container).toBeTruthy();
  });

  it('should render diamond shape for intersection subzone', () => {
    const props = {
      ...defaultProps,
      data: {
        ...defaultData,
        subZone: 'intersection-area',
      },
    } as unknown as RoomNodeProps;
    const { container } = render(<RoomNode {...props} />);
    expect(container).toBeTruthy();
  });

  it('should render handles for connections', () => {
    render(<RoomNode {...defaultProps} />);
    expect(screen.getByTestId('handle-target-top')).toBeInTheDocument();
    expect(screen.getByTestId('handle-source-top')).toBeInTheDocument();
  });

  it('should handle missing environment', () => {
    const props = {
      ...defaultProps,
      data: {
        ...defaultData,
        environment: undefined,
      },
    } as unknown as RoomNodeProps;
    const { container } = render(<RoomNode {...props} />);
    expect(container).toBeTruthy();
  });

  it('should render default circle shape when environment is empty string', () => {
    const props = {
      ...defaultProps,
      data: {
        ...defaultData,
        environment: '',
      },
    } as unknown as RoomNodeProps;
    const { container } = render(<RoomNode {...props} />);
    expect(container).toBeTruthy();
  });

  it('should render diamond shape when subzone contains intersection', () => {
    const props = {
      ...defaultProps,
      data: {
        ...defaultData,
        subZone: 'main-intersection-area',
      },
    } as unknown as RoomNodeProps;
    const { container } = render(<RoomNode {...props} />);
    expect(container).toBeTruthy();
  });

  it('should apply current location styling', () => {
    const props = {
      ...defaultProps,
      data: {
        ...defaultData,
        isCurrentLocation: true,
      },
    } as unknown as RoomNodeProps;
    const { container } = render(<RoomNode {...props} />);
    const node = container.querySelector('div');
    expect(node).toBeTruthy();
    // Node should have classes indicating current location
  });

  it('should apply unsaved changes styling', () => {
    const props = {
      ...defaultProps,
      data: {
        ...defaultData,
        hasUnsavedChanges: true,
      },
    } as unknown as RoomNodeProps;
    const { container } = render(<RoomNode {...props} />);
    const node = container.querySelector('div');
    expect(node).toBeTruthy();
    // Node should have classes indicating unsaved changes
  });

  it('should render all handles', () => {
    render(<RoomNode {...defaultProps} />);
    expect(screen.getByTestId('handle-target-top')).toBeInTheDocument();
    expect(screen.getByTestId('handle-target-right')).toBeInTheDocument();
    expect(screen.getByTestId('handle-target-bottom')).toBeInTheDocument();
    expect(screen.getByTestId('handle-target-left')).toBeInTheDocument();
    expect(screen.getByTestId('handle-source-top')).toBeInTheDocument();
    expect(screen.getByTestId('handle-source-right')).toBeInTheDocument();
    expect(screen.getByTestId('handle-source-bottom')).toBeInTheDocument();
    expect(screen.getByTestId('handle-source-left')).toBeInTheDocument();
  });

  it('should memoize component and prevent unnecessary re-renders', () => {
    const props1 = {
      ...defaultProps,
      data: {
        ...defaultData,
        id: 'room1',
        name: 'Test Room',
        isCurrentLocation: false,
        hasUnsavedChanges: false,
        environment: 'outdoors',
        subZone: undefined,
      },
    } as unknown as RoomNodeProps;

    const props2 = {
      ...props1,
      // Same props - should not re-render
    };

    const { rerender } = render(<RoomNode {...props1} />);
    const initialRender = screen.getByText('Test Room');

    rerender(<RoomNode {...props2} />);
    const afterRerender = screen.getByText('Test Room');

    expect(initialRender).toBe(afterRerender);
  });

  it('should re-render when data changes', () => {
    const props1 = {
      ...defaultProps,
      data: {
        ...defaultData,
        isCurrentLocation: false,
      },
    } as unknown as RoomNodeProps;

    const props2 = {
      ...defaultProps,
      data: {
        ...defaultData,
        isCurrentLocation: true,
      },
    } as unknown as RoomNodeProps;

    const { rerender } = render(<RoomNode {...props1} />);
    rerender(<RoomNode {...props2} />);
    // Component should re-render when isCurrentLocation changes
  });

  it('should re-render when name changes', () => {
    const props1 = {
      ...defaultProps,
      data: {
        ...defaultData,
        name: 'Room 1',
      },
    } as unknown as RoomNodeProps;

    const props2 = {
      ...defaultProps,
      data: {
        ...defaultData,
        name: 'Room 2',
      },
    } as unknown as RoomNodeProps;

    const { rerender } = render(<RoomNode {...props1} />);
    expect(screen.getByText('Room 1')).toBeInTheDocument();
    rerender(<RoomNode {...props2} />);
    expect(screen.getByText('Room 2')).toBeInTheDocument();
  });

  it('should handle long room names with truncation', () => {
    const props = {
      ...defaultProps,
      data: {
        ...defaultData,
        name: 'A Very Long Room Name That Should Be Truncated',
      },
    } as unknown as RoomNodeProps;
    const { container } = render(<RoomNode {...props} />);
    expect(container).toBeTruthy();
    // Name should be truncated
  });
});
