/**
 * Tests for applyForceLayout function.
 */

import type { Edge, Node } from 'reactflow';
import { describe, expect, it } from 'vitest';
import type { RoomNodeData } from '../../types';
import { applyForceLayout, defaultForceLayoutConfig, type ForceLayoutConfig } from '../layout';

describe('applyForceLayout', () => {
  it('should return empty array for empty nodes', () => {
    const nodes: Node<RoomNodeData>[] = [];
    const edges: Edge[] = [];
    const result = applyForceLayout(nodes, edges);

    expect(result).toEqual([]);
  });

  it('should apply force layout to nodes', () => {
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
      position: { x: 100, y: 100 },
      data: {
        id: 'room2',
        name: 'Room 2',
        description: '',
      },
    };

    const nodes = [node1, node2];
    const edges: Edge[] = [
      {
        id: 'edge1',
        source: 'node1',
        target: 'node2',
      },
    ];

    const result = applyForceLayout(nodes, edges, {
      ...defaultForceLayoutConfig,
      iterations: 10,
    });

    expect(result).toHaveLength(2);
    expect(result[0].position).toBeDefined();
    expect(result[1].position).toBeDefined();
  });

  it('should handle nodes with existing positions', () => {
    const node1: Node<RoomNodeData> = {
      id: 'node1',
      type: 'room',
      position: { x: 50, y: 50 },
      data: {
        id: 'room1',
        name: 'Room 1',
        description: '',
      },
    };

    const nodes = [node1];
    const edges: Edge[] = [];

    const result = applyForceLayout(nodes, edges, {
      ...defaultForceLayoutConfig,
      iterations: 10,
    });

    expect(result).toHaveLength(1);
    expect(result[0].position.x).toBeDefined();
    expect(result[0].position.y).toBeDefined();
  });

  it('should handle nodes without positions', () => {
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
    const edges: Edge[] = [];

    const result = applyForceLayout(nodes, edges, {
      ...defaultForceLayoutConfig,
      iterations: 10,
    });

    expect(result).toHaveLength(2);
    expect(result[0].position).toBeDefined();
    expect(result[1].position).toBeDefined();
  });

  it('should handle edge with missing source node', () => {
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

    const nodes = [node1];
    const edges: Edge[] = [
      {
        id: 'edge1',
        source: 'missing-node',
        target: 'node1',
      },
    ];

    const result = applyForceLayout(nodes, edges, {
      ...defaultForceLayoutConfig,
      iterations: 10,
    });

    expect(result).toHaveLength(1);
  });

  it('should handle edge with missing target node', () => {
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

    const nodes = [node1];
    const edges: Edge[] = [
      {
        id: 'edge1',
        source: 'node1',
        target: 'missing-node',
      },
    ];

    const result = applyForceLayout(nodes, edges, {
      ...defaultForceLayoutConfig,
      iterations: 10,
    });

    expect(result).toHaveLength(1);
  });

  it('should handle nodes at same position (zero distance)', () => {
    const node1: Node<RoomNodeData> = {
      id: 'node1',
      type: 'room',
      position: { x: 100, y: 100 },
      data: {
        id: 'room1',
        name: 'Room 1',
        description: '',
      },
    };

    const node2: Node<RoomNodeData> = {
      id: 'node2',
      type: 'room',
      position: { x: 100, y: 100 },
      data: {
        id: 'room2',
        name: 'Room 2',
        description: '',
      },
    };

    const nodes = [node1, node2];
    const edges: Edge[] = [];

    const result = applyForceLayout(nodes, edges, {
      ...defaultForceLayoutConfig,
      iterations: 50,
      minDistance: 120,
    });

    expect(result).toHaveLength(2);
    expect(
      result[0].position.x !== 100 ||
        result[0].position.y !== 100 ||
        result[1].position.x !== 100 ||
        result[1].position.y !== 100
    ).toBe(true);
  });

  it('should handle custom force layout config', () => {
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
      position: { x: 100, y: 100 },
      data: {
        id: 'room2',
        name: 'Room 2',
        description: '',
      },
    };

    const nodes = [node1, node2];
    const edges: Edge[] = [
      {
        id: 'edge1',
        source: 'node1',
        target: 'node2',
      },
    ];

    const customConfig: ForceLayoutConfig = {
      linkDistance: 300,
      chargeStrength: -2000,
      centerStrength: 0.1,
      iterations: 5,
      damping: 0.9,
      minDistance: 150,
      nodeRadius: 60,
      collisionStrength: 3.0,
      minimizeCrossings: false,
    };

    const result = applyForceLayout(nodes, edges, customConfig);

    expect(result).toHaveLength(2);
    expect(result[0].position).toBeDefined();
    expect(result[1].position).toBeDefined();
  });

  it('should handle single node', () => {
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

    const nodes = [node];
    const edges: Edge[] = [];

    const result = applyForceLayout(nodes, edges, {
      ...defaultForceLayoutConfig,
      iterations: 10,
    });

    expect(result).toHaveLength(1);
    expect(result[0].position).toBeDefined();
  });

  it('should handle node at index 0 with position 0,0 (should keep position)', () => {
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

    const nodes = [node];
    const edges: Edge[] = [];

    const result = applyForceLayout(nodes, edges, {
      ...defaultForceLayoutConfig,
      iterations: 10,
    });

    expect(result).toHaveLength(1);
    expect(result[0].position.x).toBe(0);
    expect(result[0].position.y).toBe(0);
  });

  it('should handle edge with zero distance (division by zero protection)', () => {
    const node1: Node<RoomNodeData> = {
      id: 'node1',
      type: 'room',
      position: { x: 100, y: 100 },
      data: {
        id: 'room1',
        name: 'Room 1',
        description: '',
      },
    };

    const node2: Node<RoomNodeData> = {
      id: 'node2',
      type: 'room',
      position: { x: 100, y: 100 },
      data: {
        id: 'room2',
        name: 'Room 2',
        description: '',
      },
    };

    const nodes = [node1, node2];
    const edges: Edge[] = [
      {
        id: 'edge1',
        source: 'node1',
        target: 'node2',
      },
    ];

    const result = applyForceLayout(nodes, edges, {
      ...defaultForceLayoutConfig,
      iterations: 10,
    });

    expect(result).toHaveLength(2);
  });

  it('should handle collision detection branch (distance < minDistance)', () => {
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
      position: { x: 50, y: 50 },
      data: {
        id: 'room2',
        name: 'Room 2',
        description: '',
      },
    };

    const nodes = [node1, node2];
    const edges: Edge[] = [];

    const result = applyForceLayout(nodes, edges, {
      ...defaultForceLayoutConfig,
      iterations: 20,
      minDistance: 120,
      collisionStrength: 2.0,
    });

    expect(result).toHaveLength(2);
    const dx = result[1].position.x - result[0].position.x;
    const dy = result[1].position.y - result[0].position.y;
    const distance = Math.sqrt(dx * dx + dy * dy);
    expect(distance).toBeGreaterThan(0);
  });

  it('should handle repulsive force branch (distance >= minDistance)', () => {
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
      position: { x: 200, y: 200 },
      data: {
        id: 'room2',
        name: 'Room 2',
        description: '',
      },
    };

    const nodes = [node1, node2];
    const edges: Edge[] = [];

    const result = applyForceLayout(nodes, edges, {
      ...defaultForceLayoutConfig,
      iterations: 10,
      minDistance: 120,
    });

    expect(result).toHaveLength(2);
    expect(result[0].position).toBeDefined();
    expect(result[1].position).toBeDefined();
  });

  it('should handle node not found in nodeMap after layout', () => {
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

    const nodes = [node1];
    const edges: Edge[] = [];

    const result = applyForceLayout(nodes, edges, {
      ...defaultForceLayoutConfig,
      iterations: 1,
    });

    expect(result).toHaveLength(1);
    expect(result[0].id).toBe('node1');
  });
});
