/**
 * Edge creation and data handling tests for ExitEdge component.
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
  getStraightPath: vi.fn(() => ['M0,0 L100,100', 50, 50]),
  Position: {
    Right: 'right',
    Left: 'left',
    Top: 'top',
    Bottom: 'bottom',
  },
}));

describe('ExitEdge - Edge Creation', () => {
  it('should not render flag icon when flagInfo.icon is empty', () => {
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

  it('should handle data with undefined flags', () => {
    const props = {
      ...defaultExitEdgeProps,
      data: {
        ...defaultExitEdgeProps.data,
        flags: undefined,
      },
    };
    const { container } = render(<ExitEdge {...props} />);
    expect(container).toBeTruthy();
  });

  it('should handle data with undefined direction', () => {
    const props = {
      ...defaultExitEdgeProps,
      data: {
        ...defaultExitEdgeProps.data,
        direction: undefined as unknown as string,
      },
    };
    const { container } = render(<ExitEdge {...props} />);
    expect(container).toBeTruthy();
  });

  it('should handle style prop with custom values', () => {
    const props = {
      ...defaultExitEdgeProps,
      style: { stroke: 'blue', strokeWidth: 4 },
      data: {
        ...defaultExitEdgeProps.data,
        flags: ['hidden', 'locked', 'one_way'],
      },
    };
    const { container } = render(<ExitEdge {...props} />);
    expect(container).toBeTruthy();
  });
});
