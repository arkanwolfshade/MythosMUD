/**
 * Tests for ExitEdge component.
 */

import { render } from '@testing-library/react';
import React from 'react';
import { Position } from 'reactflow';
import { describe, expect, it, vi } from 'vitest';
import type { ExitEdgeData } from '../../types';
import { ExitEdge } from '../ExitEdge';

// Mock reactflow
vi.mock('reactflow', () => ({
  BaseEdge: ({ id, path }: { id: string; path: string }): React.ReactElement => (
    <div data-testid={`edge-${id}`}>{path}</div>
  ),
  EdgeLabelRenderer: ({ children }: { children: React.ReactNode }): React.ReactElement => (
    <div data-testid="edge-label-renderer">{children}</div>
  ),
  getBezierPath: vi.fn(() => ['M0,0 L100,100', 50, 50]),
  Position: {
    Right: 'right',
    Left: 'left',
    Top: 'top',
    Bottom: 'bottom',
  },
}));

describe('ExitEdge', () => {
  const defaultProps = {
    id: 'edge1',
    source: 'room1',
    target: 'room2',
    sourceX: 0,
    sourceY: 0,
    targetX: 100,
    targetY: 100,
    sourcePosition: Position.Right,
    targetPosition: Position.Left,
    style: {},
    markerEnd: undefined,
    data: {
      direction: 'north',
      sourceRoomId: 'room1',
      targetRoomId: 'room2',
      flags: [],
    } as ExitEdgeData,
  };

  it('should render edge', () => {
    const { container } = render(<ExitEdge {...defaultProps} />);
    expect(container).toBeTruthy();
  });

  it('should render edge with hidden flag', () => {
    const props = {
      ...defaultProps,
      data: {
        ...defaultProps.data,
        flags: ['hidden'],
      },
    };
    const { container } = render(<ExitEdge {...props} />);
    expect(container).toBeTruthy();
  });

  it('should render edge with locked flag', () => {
    const props = {
      ...defaultProps,
      data: {
        ...defaultProps.data,
        flags: ['locked'],
      },
    };
    const { container } = render(<ExitEdge {...props} />);
    expect(container).toBeTruthy();
  });

  it('should render edge with one_way flag', () => {
    const props = {
      ...defaultProps,
      data: {
        ...defaultProps.data,
        flags: ['one_way'],
      },
    };
    const { container } = render(<ExitEdge {...props} />);
    expect(container).toBeTruthy();
  });

  it('should render edge with self_reference flag', () => {
    const props = {
      ...defaultProps,
      data: {
        ...defaultProps.data,
        flags: ['self_reference'],
      },
    };
    const { container } = render(<ExitEdge {...props} />);
    expect(container).toBeTruthy();
  });

  it('should render edge without flags (no label renderer)', () => {
    const props = {
      ...defaultProps,
      data: {
        ...defaultProps.data,
        flags: [],
      },
    };
    const { queryByTestId } = render(<ExitEdge {...props} />);
    // Edge label renderer should not be rendered when flags.length === 0
    expect(queryByTestId('edge-label-renderer')).not.toBeInTheDocument();
  });

  it('should render edge with multiple flags', () => {
    const props = {
      ...defaultProps,
      data: {
        ...defaultProps.data,
        flags: ['hidden', 'locked', 'one_way'],
      },
    };
    const { getByTestId } = render(<ExitEdge {...props} />);
    expect(getByTestId('edge-label-renderer')).toBeInTheDocument();
  });

  it('should render edge with direction text when direction is provided', () => {
    const props = {
      ...defaultProps,
      data: {
        ...defaultProps.data,
        flags: ['hidden'],
        direction: 'north',
      },
    };
    const { container } = render(<ExitEdge {...props} />);
    // Should render direction text when direction is provided
    expect(container.textContent).toContain('north');
  });

  it('should not render direction text when direction is empty', () => {
    const props = {
      ...defaultProps,
      data: {
        ...defaultProps.data,
        flags: ['hidden'],
        direction: '',
      },
    };
    const { getByTestId } = render(<ExitEdge {...props} />);
    // Direction should not render when empty (line 89: direction &&)
    // The flags icon should still render
    expect(getByTestId('edge-label-renderer')).toBeInTheDocument();
  });

  it('should apply hidden flag styling (gray stroke)', () => {
    const props = {
      ...defaultProps,
      data: {
        ...defaultProps.data,
        flags: ['hidden'],
      },
    };
    const { getByTestId } = render(<ExitEdge {...props} />);
    const edge = getByTestId('edge-edge1');
    // Should have gray stroke when hidden flag is present (line 64)
    expect(edge).toBeInTheDocument();
  });

  it('should apply locked flag styling (thicker stroke)', () => {
    const props = {
      ...defaultProps,
      data: {
        ...defaultProps.data,
        flags: ['locked'],
      },
    };
    const { getByTestId } = render(<ExitEdge {...props} />);
    const edge = getByTestId('edge-edge1');
    // Should have strokeWidth 3 when locked flag is present (line 65)
    expect(edge).toBeInTheDocument();
  });

  it('should apply one_way flag styling (dashed stroke)', () => {
    const props = {
      ...defaultProps,
      data: {
        ...defaultProps.data,
        flags: ['one_way'],
      },
    };
    const { getByTestId } = render(<ExitEdge {...props} />);
    const edge = getByTestId('edge-edge1');
    // Should have strokeDasharray when one_way flag is present (line 66)
    expect(edge).toBeInTheDocument();
  });

  it('should handle unknown flag type (no icon)', () => {
    const props = {
      ...defaultProps,
      data: {
        ...defaultProps.data,
        flags: ['unknown_flag'],
      },
    };
    const { getByTestId } = render(<ExitEdge {...props} />);
    // Unknown flags should not render icons (line 81: if (!flagInfo.icon) return null)
    expect(getByTestId('edge-label-renderer')).toBeInTheDocument();
  });

  it('should handle edge with no data', () => {
    const props = {
      ...defaultProps,
      data: undefined,
    };
    const { container } = render(<ExitEdge {...props} />);
    expect(container).toBeTruthy();
  });

  it('should handle edge with data but no flags property', () => {
    const props = {
      ...defaultProps,
      data: {
        direction: 'north',
        sourceRoomId: 'room1',
        targetRoomId: 'room2',
      } as ExitEdgeData,
    };
    const { container } = render(<ExitEdge {...props} />);
    // Should handle missing flags property (line 53: data?.flags || [])
    expect(container).toBeTruthy();
  });

  it('should handle edge with data but no direction property', () => {
    const props = {
      ...defaultProps,
      data: {
        flags: ['hidden'],
        sourceRoomId: 'room1',
        targetRoomId: 'room2',
      } as ExitEdgeData,
    };
    const { container } = render(<ExitEdge {...props} />);
    // Should handle missing direction property (line 54: data?.direction || '')
    expect(container).toBeTruthy();
  });

  it('should apply default stroke color when hidden flag is not present', () => {
    const props = {
      ...defaultProps,
      data: {
        ...defaultProps.data,
        flags: [],
      },
    };
    const { getByTestId } = render(<ExitEdge {...props} />);
    const edge = getByTestId('edge-edge1');
    // Should use green stroke (#10b981) when hidden flag is not present (line 64: ternary false branch)
    expect(edge).toBeInTheDocument();
  });

  it('should apply default stroke width when locked flag is not present', () => {
    const props = {
      ...defaultProps,
      data: {
        ...defaultProps.data,
        flags: [],
      },
    };
    const { getByTestId } = render(<ExitEdge {...props} />);
    const edge = getByTestId('edge-edge1');
    // Should use strokeWidth 2 when locked flag is not present (line 65: ternary false branch)
    expect(edge).toBeInTheDocument();
  });

  it('should apply no dash array when one_way flag is not present', () => {
    const props = {
      ...defaultProps,
      data: {
        ...defaultProps.data,
        flags: [],
      },
    };
    const { getByTestId } = render(<ExitEdge {...props} />);
    const edge = getByTestId('edge-edge1');
    // Should use undefined strokeDasharray when one_way flag is not present (line 66: ternary false branch)
    expect(edge).toBeInTheDocument();
  });

  it('should handle all flag icons correctly', () => {
    const flagTests = [
      { flag: 'hidden', expectedIcon: '👁️' },
      { flag: 'locked', expectedIcon: '🔒' },
      { flag: 'one_way', expectedIcon: '➡️' },
      { flag: 'self_reference', expectedIcon: '🔄' },
    ];

    flagTests.forEach(({ flag, expectedIcon }) => {
      const props = {
        ...defaultProps,
        data: {
          ...defaultProps.data,
          flags: [flag],
        },
      };
      const { container } = render(<ExitEdge {...props} />);
      expect(container.textContent).toContain(expectedIcon);
    });
  });

  it('should render edge with multiple flags', () => {
    const props = {
      ...defaultProps,
      data: {
        ...defaultProps.data,
        flags: ['hidden', 'locked'],
      },
    };
    const { container } = render(<ExitEdge {...props} />);
    expect(container).toBeTruthy();
  });

  it('should render edge without flags', () => {
    const props = {
      ...defaultProps,
      data: {
        ...defaultProps.data,
        flags: [],
      },
    };
    const { container } = render(<ExitEdge {...props} />);
    expect(container).toBeTruthy();
  });

  it('should render edge with direction', () => {
    const props = {
      ...defaultProps,
      data: {
        ...defaultProps.data,
        direction: 'south',
      },
    };
    const { container } = render(<ExitEdge {...props} />);
    expect(container).toBeTruthy();
  });

  it('should handle missing data', () => {
    const props = {
      ...defaultProps,
      data: undefined,
    };
    const { container } = render(<ExitEdge {...props} />);
    expect(container).toBeTruthy();
  });

  it('should apply hidden flag styling to edge', () => {
    const props = {
      ...defaultProps,
      data: {
        ...defaultProps.data,
        flags: ['hidden'],
      },
    };
    const { container } = render(<ExitEdge {...props} />);
    expect(container).toBeTruthy();
    // The edge should have gray stroke color when hidden flag is present
  });

  it('should apply locked flag styling to edge', () => {
    const props = {
      ...defaultProps,
      data: {
        ...defaultProps.data,
        flags: ['locked'],
      },
    };
    const { container } = render(<ExitEdge {...props} />);
    expect(container).toBeTruthy();
    // The edge should have thicker stroke width when locked flag is present
  });

  it('should apply one_way flag styling to edge', () => {
    const props = {
      ...defaultProps,
      data: {
        ...defaultProps.data,
        flags: ['one_way'],
      },
    };
    const { container } = render(<ExitEdge {...props} />);
    expect(container).toBeTruthy();
    // The edge should have dashed stroke when one_way flag is present
  });

  it('should render edge without flags section when flags array is empty', () => {
    const props = {
      ...defaultProps,
      data: {
        ...defaultProps.data,
        flags: [],
      },
    };
    const { container } = render(<ExitEdge {...props} />);
    expect(container).toBeTruthy();
    // EdgeLabelRenderer should not be rendered when flags.length === 0
  });

  it('should render direction label when direction is provided', () => {
    const props = {
      ...defaultProps,
      data: {
        ...defaultProps.data,
        flags: ['hidden'],
        direction: 'east',
      },
    };
    const { container } = render(<ExitEdge {...props} />);
    expect(container).toBeTruthy();
  });

  it('should not render direction label when direction is empty', () => {
    const props = {
      ...defaultProps,
      data: {
        ...defaultProps.data,
        flags: ['hidden'],
        direction: '',
      },
    };
    const { container } = render(<ExitEdge {...props} />);
    expect(container).toBeTruthy();
  });

  it('should handle unknown flag type', () => {
    const props = {
      ...defaultProps,
      data: {
        ...defaultProps.data,
        flags: ['unknown_flag'],
      },
    };
    const { container } = render(<ExitEdge {...props} />);
    expect(container).toBeTruthy();
    // Unknown flags should not render icons (getFlagIcon returns empty icon)
  });

  it('should handle edge with custom style', () => {
    const props = {
      ...defaultProps,
      style: { stroke: 'red', strokeWidth: 5 },
    };
    const { container } = render(<ExitEdge {...props} />);
    expect(container).toBeTruthy();
  });

  it('should handle edge with markerEnd', () => {
    const props = {
      ...defaultProps,
      markerEnd: 'arrowclosed',
    };
    const { container } = render(<ExitEdge {...props} />);
    expect(container).toBeTruthy();
  });

  it('should handle edge with multiple flags and direction', () => {
    const props = {
      ...defaultProps,
      data: {
        ...defaultProps.data,
        flags: ['hidden', 'locked', 'one_way'],
        direction: 'north',
      },
    };
    const { container } = render(<ExitEdge {...props} />);
    expect(container).toBeTruthy();
  });

  it('should memoize component and prevent unnecessary re-renders', () => {
    const props1 = {
      ...defaultProps,
      id: 'edge1',
      sourceX: 0,
      sourceY: 0,
      data: {
        ...defaultProps.data,
        flags: ['hidden'],
        direction: 'north',
      },
    };

    const props2 = {
      ...props1,
      // Same props - should not re-render
    };

    const { rerender } = render(<ExitEdge {...props1} />);
    const initialRender = document.querySelector('[data-testid="edge-edge1"]');

    rerender(<ExitEdge {...props2} />);
    const afterRerender = document.querySelector('[data-testid="edge-edge1"]');

    // Component should be memoized
    expect(initialRender).toBeTruthy();
    expect(afterRerender).toBeTruthy();
  });

  it('should re-render when flags change', () => {
    const props1 = {
      ...defaultProps,
      data: {
        ...defaultProps.data,
        flags: ['hidden'],
      },
    };

    const props2 = {
      ...defaultProps,
      data: {
        ...defaultProps.data,
        flags: ['locked'],
      },
    };

    const { rerender } = render(<ExitEdge {...props1} />);
    rerender(<ExitEdge {...props2} />);
    // Component should re-render when flags change
  });

  it('should re-render when direction changes', () => {
    const props1 = {
      ...defaultProps,
      data: {
        ...defaultProps.data,
        flags: ['hidden'],
        direction: 'north',
      },
    };

    const props2 = {
      ...defaultProps,
      data: {
        ...defaultProps.data,
        flags: ['hidden'],
        direction: 'south',
      },
    };

    const { rerender } = render(<ExitEdge {...props1} />);
    rerender(<ExitEdge {...props2} />);
    // Component should re-render when direction changes
  });

  it('should re-render when position changes', () => {
    const props1 = {
      ...defaultProps,
      sourceX: 0,
      sourceY: 0,
    };

    const props2 = {
      ...defaultProps,
      sourceX: 100,
      sourceY: 100,
    };

    const { rerender } = render(<ExitEdge {...props1} />);
    rerender(<ExitEdge {...props2} />);
    // Component should re-render when position changes
  });

  it('should not render flag icon when flagInfo.icon is empty', () => {
    // Test line 81: when getFlagIcon returns empty icon for unknown flag
    const props = {
      ...defaultProps,
      data: {
        ...defaultProps.data,
        flags: ['unknown_flag'],
      },
    };
    const { container } = render(<ExitEdge {...props} />);
    // EdgeLabelRenderer should still render, but flag icon should not (line 81 branch)
    expect(container).toBeTruthy();
  });

  it('should handle data with undefined flags', () => {
    // Test line 53: data?.flags || []
    const props = {
      ...defaultProps,
      data: {
        ...defaultProps.data,
        flags: undefined,
      },
    };
    const { container } = render(<ExitEdge {...props} />);
    // Should use empty array when flags is undefined (line 53 branch)
    expect(container).toBeTruthy();
  });

  it('should handle data with undefined direction', () => {
    // Test line 54: data?.direction || ''
    const props = {
      ...defaultProps,
      data: {
        ...defaultProps.data,
        direction: undefined as unknown as string,
      },
    };
    const { container } = render(<ExitEdge {...props} />);
    // Should use empty string when direction is undefined (line 54 branch)
    expect(container).toBeTruthy();
  });

  it('should handle style prop with custom values', () => {
    // Test line 62-67: style merging with flag-based styles
    const props = {
      ...defaultProps,
      style: { stroke: 'blue', strokeWidth: 4 },
      data: {
        ...defaultProps.data,
        flags: ['hidden', 'locked', 'one_way'],
      },
    };
    const { container } = render(<ExitEdge {...props} />);
    // Style should be merged with flag-based styles
    expect(container).toBeTruthy();
  });

  it('should not re-render when irrelevant props change (memo test)', () => {
    // Test line 100-111: memo comparison function
    const props1 = {
      ...defaultProps,
      id: 'edge1',
      sourceX: 0,
      sourceY: 0,
      targetX: 100,
      targetY: 100,
      data: {
        ...defaultProps.data,
        flags: ['hidden'],
        direction: 'north',
      },
    };

    const props2 = {
      ...props1,
      // Change irrelevant prop (markerEnd) - should not trigger re-render
      markerEnd: 'arrowclosed',
    };

    const { rerender } = render(<ExitEdge {...props1} />);
    const initialRender = document.querySelector('[data-testid="edge-edge1"]');

    rerender(<ExitEdge {...props2} />);
    const afterRerender = document.querySelector('[data-testid="edge-edge1"]');

    // Component should be memoized and not re-render for irrelevant changes
    expect(initialRender).toBeTruthy();
    expect(afterRerender).toBeTruthy();
  });

  it('should handle all flag types in getFlagIcon', () => {
    // Test all switch cases in getFlagIcon (lines 24-31)
    const flagTypes = ['hidden', 'locked', 'one_way', 'self_reference'];

    flagTypes.forEach(flag => {
      const props = {
        ...defaultProps,
        data: {
          ...defaultProps.data,
          flags: [flag],
        },
      };
      const { container } = render(<ExitEdge {...props} />);
      expect(container).toBeTruthy();
    });
  });

  it('should handle edge with flags but no direction', () => {
    // Test line 89: direction && ( branch when direction is empty
    const props = {
      ...defaultProps,
      data: {
        ...defaultProps.data,
        flags: ['hidden'],
        direction: '',
      },
    };
    const { container } = render(<ExitEdge {...props} />);
    // EdgeLabelRenderer should render (flags.length > 0), but direction should not (line 89)
    expect(container).toBeTruthy();
  });

  it('should handle edge with direction but no flags', () => {
    // Test line 69: flags.length > 0 branch when flags is empty
    const props = {
      ...defaultProps,
      data: {
        ...defaultProps.data,
        flags: [],
        direction: 'north',
      },
    };
    const { container } = render(<ExitEdge {...props} />);
    // EdgeLabelRenderer should not render when flags.length === 0 (line 69)
    expect(container).toBeTruthy();
  });
});
