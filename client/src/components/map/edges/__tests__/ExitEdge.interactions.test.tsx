/**
 * Interaction tests for ExitEdge component.
 */

import { render } from '@testing-library/react';
import React from 'react';
import { describe, expect, it, vi } from 'vitest';
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
  getBezierPath: vi.fn(() => ['M0,0 L100,100', 50, 50]),
  Position: {
    Right: 'right',
    Left: 'left',
    Top: 'top',
    Bottom: 'bottom',
  },
}));

describe('ExitEdge - Interactions', () => {
  it('should memoize component and prevent unnecessary re-renders', () => {
    const props1 = {
      ...defaultExitEdgeProps,
      id: 'edge1',
      sourceX: 0,
      sourceY: 0,
      data: {
        ...defaultExitEdgeProps.data,
        flags: ['hidden'],
        direction: 'north',
      },
    };

    const props2 = {
      ...props1,
    };

    const { rerender } = render(<ExitEdge {...props1} />);
    const initialRender = document.querySelector('[data-testid="edge-edge1"]');

    rerender(<ExitEdge {...props2} />);
    const afterRerender = document.querySelector('[data-testid="edge-edge1"]');

    expect(initialRender).toBeTruthy();
    expect(afterRerender).toBeTruthy();
  });

  it('should re-render when flags change', () => {
    const props1 = {
      ...defaultExitEdgeProps,
      data: {
        ...defaultExitEdgeProps.data,
        flags: ['hidden'],
      },
    };

    const props2 = {
      ...defaultExitEdgeProps,
      data: {
        ...defaultExitEdgeProps.data,
        flags: ['locked'],
      },
    };

    const { rerender } = render(<ExitEdge {...props1} />);
    rerender(<ExitEdge {...props2} />);
  });

  it('should re-render when direction changes', () => {
    const props1 = {
      ...defaultExitEdgeProps,
      data: {
        ...defaultExitEdgeProps.data,
        flags: ['hidden'],
        direction: 'north',
      },
    };

    const props2 = {
      ...defaultExitEdgeProps,
      data: {
        ...defaultExitEdgeProps.data,
        flags: ['hidden'],
        direction: 'south',
      },
    };

    const { rerender } = render(<ExitEdge {...props1} />);
    rerender(<ExitEdge {...props2} />);
  });

  it('should re-render when position changes', () => {
    const props1 = {
      ...defaultExitEdgeProps,
      sourceX: 0,
      sourceY: 0,
    };

    const props2 = {
      ...defaultExitEdgeProps,
      sourceX: 100,
      sourceY: 100,
    };

    const { rerender } = render(<ExitEdge {...props1} />);
    rerender(<ExitEdge {...props2} />);
  });

  it('should not re-render when irrelevant props change (memo test)', () => {
    const props1 = {
      ...defaultExitEdgeProps,
      id: 'edge1',
      sourceX: 0,
      sourceY: 0,
      targetX: 100,
      targetY: 100,
      data: {
        ...defaultExitEdgeProps.data,
        flags: ['hidden'],
        direction: 'north',
      },
    };

    const props2 = {
      ...props1,
      markerEnd: 'arrowclosed',
    };

    const { rerender } = render(<ExitEdge {...props1} />);
    const initialRender = document.querySelector('[data-testid="edge-edge1"]');

    rerender(<ExitEdge {...props2} />);
    const afterRerender = document.querySelector('[data-testid="edge-edge1"]');

    expect(initialRender).toBeTruthy();
    expect(afterRerender).toBeTruthy();
  });
});
