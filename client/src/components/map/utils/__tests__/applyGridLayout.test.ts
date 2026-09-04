/**
 * Tests for applyGridLayout function.
 */

import type { Node } from 'reactflow';
import { describe, expect, it } from 'vitest';
import type { RoomNodeData } from '../../types';
import { applyGridLayout, defaultGridLayoutConfig, type GridLayoutConfig } from '../layout';

describe('applyGridLayout', () => {
  it('should apply grid layout to nodes', () => {
    const node1: Node<RoomNodeData> = {
      id: 'node1',
      type: 'room',
      position: { x: 0, y: 0 },
      data: {
        id: 'room1',
        name: 'Room 1',
        description: '',
      },
    };

    const node2: Node<RoomNodeData> = {
      id: 'node2',
      type: 'room',
      position: { x: 0, y: 0 },
      data: {
        id: 'room2',
        name: 'Room 2',
        description: '',
      },
    };

    const nodes = [node1, node2];
    const result = applyGridLayout(nodes);

    expect(result).toHaveLength(2);
    expect(result[0].position).toBeDefined();
    expect(result[1].position).toBeDefined();
    expect(result[0].position.x !== result[1].position.x || result[0].position.y !== result[1].position.y).toBe(true);
  });

  it('should use custom config', () => {
    const node: Node<RoomNodeData> = {
      id: 'node1',
      type: 'room',
      position: { x: 0, y: 0 },
      data: {
        id: 'room1',
        name: 'Room 1',
        description: '',
      },
    };

    const config: GridLayoutConfig = {
      ...defaultGridLayoutConfig,
      cellWidth: 200,
      cellHeight: 200,
    };

    const nodes = [node];
    const result = applyGridLayout(nodes, config);

    expect(result).toHaveLength(1);
    expect(result[0].position).toBeDefined();
  });

  it('should handle empty nodes array', () => {
    const nodes: Node<RoomNodeData>[] = [];
    const result = applyGridLayout(nodes);

    expect(result).toEqual([]);
  });
});
