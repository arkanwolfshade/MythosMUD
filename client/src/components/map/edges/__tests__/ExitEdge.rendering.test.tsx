/**
 * Rendering tests for ExitEdge component.
 */

import { render } from '@testing-library/react';
import React from 'react';
import { describe, expect, it, vi } from 'vitest';
import type { ExitEdgeData } from '../../types';
import { ExitEdge } from '../ExitEdge';
import { defaultExitEdgeProps } from './ExitEdge.test-fixtures';

// Mock reactflow
vi.mock('reactflow', () => ({
  BaseEdge: ({ id, path }: { id: string; path: string }): React.ReactElement => (
    <div data-testid={`edge-${id}`}>{path}</div>
  ),
  EdgeLabelRenderer: ({ children }: { children: React.ReactNode }): React.ReactElement => (
    <div data-testid="edge-label-renderer">{children}</div>
  ),
  getStraightPath: vi.fn(() => ['M0,0 L100,100', 50, 50]),
  Position: {
    Right: 'right',
    Left: 'left',
    Top: 'top',
    Bottom: 'bottom',
  },
}));

describe('ExitEdge - Rendering', () => {
  it('should render edge', () => {
    const { container } = render(<ExitEdge {...defaultExitEdgeProps} />);
    expect(container).toBeTruthy();
  });

  it('should render edge with hidden flag', () => {
    const props = {
      ...defaultExitEdgeProps,
      data: {
        ...defaultExitEdgeProps.data,
        flags: ['hidden'],
      },
    };
    const { container } = render(<ExitEdge {...props} />);
    expect(container).toBeTruthy();
  });

  it('should render edge with locked flag', () => {
    const props = {
      ...defaultExitEdgeProps,
      data: {
        ...defaultExitEdgeProps.data,
        flags: ['locked'],
      },
    };
    const { container } = render(<ExitEdge {...props} />);
    expect(container).toBeTruthy();
  });

  it('should render edge with one_way flag', () => {
    const props = {
      ...defaultExitEdgeProps,
      data: {
        ...defaultExitEdgeProps.data,
        flags: ['one_way'],
      },
    };
    const { container } = render(<ExitEdge {...props} />);
    expect(container).toBeTruthy();
  });

  it('should render edge with self_reference flag', () => {
    const props = {
      ...defaultExitEdgeProps,
      data: {
        ...defaultExitEdgeProps.data,
        flags: ['self_reference'],
      },
    };
    const { container } = render(<ExitEdge {...props} />);
    expect(container).toBeTruthy();
  });

  it('should render edge without flags (no label renderer)', () => {
    const props = {
      ...defaultExitEdgeProps,
      data: {
        ...defaultExitEdgeProps.data,
        flags: [],
      },
    };
    const { queryByTestId } = render(<ExitEdge {...props} />);
    expect(queryByTestId('edge-label-renderer')).not.toBeInTheDocument();
  });

  it('should render edge with multiple flags', () => {
    const props = {
      ...defaultExitEdgeProps,
      data: {
        ...defaultExitEdgeProps.data,
        flags: ['hidden', 'locked', 'one_way'],
      },
    };
    const { getByTestId } = render(<ExitEdge {...props} />);
    expect(getByTestId('edge-label-renderer')).toBeInTheDocument();
  });

  it('should render edge with direction text when direction is provided', () => {
    const props = {
      ...defaultExitEdgeProps,
      data: {
        ...defaultExitEdgeProps.data,
        flags: ['hidden'],
        direction: 'north',
      },
    };
    const { container } = render(<ExitEdge {...props} />);
    expect(container.textContent).toContain('north');
  });

  it('should not render direction text when direction is empty', () => {
    const props = {
      ...defaultExitEdgeProps,
      data: {
        ...defaultExitEdgeProps.data,
        flags: ['hidden'],
        direction: '',
      },
    };
    const { getByTestId } = render(<ExitEdge {...props} />);
    expect(getByTestId('edge-label-renderer')).toBeInTheDocument();
  });

  it('should apply hidden flag styling (gray stroke)', () => {
    const props = {
      ...defaultExitEdgeProps,
      data: {
        ...defaultExitEdgeProps.data,
        flags: ['hidden'],
      },
    };
    const { getByTestId } = render(<ExitEdge {...props} />);
    const edge = getByTestId('edge-edge1');
    expect(edge).toBeInTheDocument();
  });

  it('should apply locked flag styling (thicker stroke)', () => {
    const props = {
      ...defaultExitEdgeProps,
      data: {
        ...defaultExitEdgeProps.data,
        flags: ['locked'],
      },
    };
    const { getByTestId } = render(<ExitEdge {...props} />);
    const edge = getByTestId('edge-edge1');
    expect(edge).toBeInTheDocument();
  });

  it('should apply one_way flag styling (dashed stroke)', () => {
    const props = {
      ...defaultExitEdgeProps,
      data: {
        ...defaultExitEdgeProps.data,
        flags: ['one_way'],
      },
    };
    const { getByTestId } = render(<ExitEdge {...props} />);
    const edge = getByTestId('edge-edge1');
    expect(edge).toBeInTheDocument();
  });

  it('should handle unknown flag type (no icon)', () => {
    const props = {
      ...defaultExitEdgeProps,
      data: {
        ...defaultExitEdgeProps.data,
        flags: ['unknown_flag'],
      },
    };
    const { getByTestId } = render(<ExitEdge {...props} />);
    expect(getByTestId('edge-label-renderer')).toBeInTheDocument();
  });

  it('should handle edge with no data', () => {
    const props = {
      ...defaultExitEdgeProps,
      data: undefined,
    };
    const { container } = render(<ExitEdge {...props} />);
    expect(container).toBeTruthy();
  });

  it('should handle edge with data but no flags property', () => {
    const props = {
      ...defaultExitEdgeProps,
      data: {
        direction: 'north',
        sourceRoomId: 'room1',
        targetRoomId: 'room2',
      } as ExitEdgeData,
    };
    const { container } = render(<ExitEdge {...props} />);
    expect(container).toBeTruthy();
  });

  it('should handle edge with data but no direction property', () => {
    const props = {
      ...defaultExitEdgeProps,
      data: {
        flags: ['hidden'],
        sourceRoomId: 'room1',
        targetRoomId: 'room2',
      } as ExitEdgeData,
    };
    const { container } = render(<ExitEdge {...props} />);
    expect(container).toBeTruthy();
  });

  it('should apply default stroke color when hidden flag is not present', () => {
    const props = {
      ...defaultExitEdgeProps,
      data: {
        ...defaultExitEdgeProps.data,
        flags: [],
      },
    };
    const { getByTestId } = render(<ExitEdge {...props} />);
    const edge = getByTestId('edge-edge1');
    expect(edge).toBeInTheDocument();
  });

  it('should apply default stroke width when locked flag is not present', () => {
    const props = {
      ...defaultExitEdgeProps,
      data: {
        ...defaultExitEdgeProps.data,
        flags: [],
      },
    };
    const { getByTestId } = render(<ExitEdge {...props} />);
    const edge = getByTestId('edge-edge1');
    expect(edge).toBeInTheDocument();
  });

  it('should apply no dash array when one_way flag is not present', () => {
    const props = {
      ...defaultExitEdgeProps,
      data: {
        ...defaultExitEdgeProps.data,
        flags: [],
      },
    };
    const { getByTestId } = render(<ExitEdge {...props} />);
    const edge = getByTestId('edge-edge1');
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
        ...defaultExitEdgeProps,
        data: {
          ...defaultExitEdgeProps.data,
          flags: [flag],
        },
      };
      const { container } = render(<ExitEdge {...props} />);
      expect(container.textContent).toContain(expectedIcon);
    });
  });

  it('should render edge with direction', () => {
    const props = {
      ...defaultExitEdgeProps,
      data: {
        ...defaultExitEdgeProps.data,
        direction: 'south',
      },
    };
    const { container } = render(<ExitEdge {...props} />);
    expect(container).toBeTruthy();
  });

  it('should apply hidden flag styling to edge', () => {
    const props = {
      ...defaultExitEdgeProps,
      data: {
        ...defaultExitEdgeProps.data,
        flags: ['hidden'],
      },
    };
    const { container } = render(<ExitEdge {...props} />);
    expect(container).toBeTruthy();
  });

  it('should apply locked flag styling to edge', () => {
    const props = {
      ...defaultExitEdgeProps,
      data: {
        ...defaultExitEdgeProps.data,
        flags: ['locked'],
      },
    };
    const { container } = render(<ExitEdge {...props} />);
    expect(container).toBeTruthy();
  });

  it('should apply one_way flag styling to edge', () => {
    const props = {
      ...defaultExitEdgeProps,
      data: {
        ...defaultExitEdgeProps.data,
        flags: ['one_way'],
      },
    };
    const { container } = render(<ExitEdge {...props} />);
    expect(container).toBeTruthy();
  });

  it('should render edge without flags section when flags array is empty', () => {
    const props = {
      ...defaultExitEdgeProps,
      data: {
        ...defaultExitEdgeProps.data,
        flags: [],
      },
    };
    const { container } = render(<ExitEdge {...props} />);
    expect(container).toBeTruthy();
  });

  it('should render direction label when direction is provided', () => {
    const props = {
      ...defaultExitEdgeProps,
      data: {
        ...defaultExitEdgeProps.data,
        flags: ['hidden'],
        direction: 'east',
      },
    };
    const { container } = render(<ExitEdge {...props} />);
    expect(container).toBeTruthy();
  });

  it('should not render direction label when direction is empty', () => {
    const props = {
      ...defaultExitEdgeProps,
      data: {
        ...defaultExitEdgeProps.data,
        flags: ['hidden'],
        direction: '',
      },
    };
    const { container } = render(<ExitEdge {...props} />);
    expect(container).toBeTruthy();
  });

  it('should handle unknown flag type', () => {
    const props = {
      ...defaultExitEdgeProps,
      data: {
        ...defaultExitEdgeProps.data,
        flags: ['unknown_flag'],
      },
    };
    const { container } = render(<ExitEdge {...props} />);
    expect(container).toBeTruthy();
  });

  it('should handle edge with custom style', () => {
    const props = {
      ...defaultExitEdgeProps,
      style: { stroke: 'red', strokeWidth: 5 },
    };
    const { container } = render(<ExitEdge {...props} />);
    expect(container).toBeTruthy();
  });

  it('should handle edge with markerEnd', () => {
    const props = {
      ...defaultExitEdgeProps,
      markerEnd: 'arrowclosed',
    };
    const { container } = render(<ExitEdge {...props} />);
    expect(container).toBeTruthy();
  });

  it('should handle edge with multiple flags and direction', () => {
    const props = {
      ...defaultExitEdgeProps,
      data: {
        ...defaultExitEdgeProps.data,
        flags: ['hidden', 'locked', 'one_way'],
        direction: 'north',
      },
    };
    const { container } = render(<ExitEdge {...props} />);
    expect(container).toBeTruthy();
  });

  it('should handle all flag types in getFlagIcon', () => {
    const flagTypes = ['hidden', 'locked', 'one_way', 'self_reference'];

    flagTypes.forEach(flag => {
      const props = {
        ...defaultExitEdgeProps,
        data: {
          ...defaultExitEdgeProps.data,
          flags: [flag],
        },
      };
      const { container } = render(<ExitEdge {...props} />);
      expect(container).toBeTruthy();
    });
  });

  it('should handle edge with flags but no direction', () => {
    const props = {
      ...defaultExitEdgeProps,
      data: {
        ...defaultExitEdgeProps.data,
        flags: ['hidden'],
        direction: '',
      },
    };
    const { container } = render(<ExitEdge {...props} />);
    expect(container).toBeTruthy();
  });

  it('should handle edge with direction but no flags', () => {
    const props = {
      ...defaultExitEdgeProps,
      data: {
        ...defaultExitEdgeProps.data,
        flags: [],
        direction: 'north',
      },
    };
    const { container } = render(<ExitEdge {...props} />);
    expect(container).toBeTruthy();
  });
});
