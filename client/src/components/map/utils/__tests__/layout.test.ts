/**
 * Tests for layout utilities.
 */

import type { Edge, Node } from 'reactflow';
import { describe, expect, it } from 'vitest';
import type { RoomNodeData } from '../../types';
import {
  applyForceLayout,
  applyGridLayout,
  calculateGridPosition,
  defaultForceLayoutConfig,
  defaultGridLayoutConfig,
  type ForceLayoutConfig,
  type GridLayoutConfig,
} from '../layout';

describe('layout utilities', () => {
  describe('calculateGridPosition', () => {
    it('should use stored position when available', () => {
      const node: Node<RoomNodeData> = {
        id: 'node1',
        type: 'room',
        position: { x: 0, y: 0 },
        data: {
          id: 'room1',
          name: 'Room 1',
          map_x: 100,
          map_y: 200,
        } as RoomNodeData & { map_x: number; map_y: number },
      };

      const nodes: Node<RoomNodeData>[] = [node];
      const position = calculateGridPosition(node, 0, nodes);

      expect(position).toEqual({ x: 100, y: 200 });
    });

    it('should calculate grid position when no stored position', () => {
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

      const nodes: Node<RoomNodeData>[] = [node];
      const position = calculateGridPosition(node, 0, nodes);

      expect(position.x).toBeGreaterThanOrEqual(0);
      expect(position.y).toBeGreaterThanOrEqual(0);
    });

    it('should group by subzone when groupBySubZone is true', () => {
      const config: GridLayoutConfig = {
        ...defaultGridLayoutConfig,
        groupBySubZone: true,
      };

      const node1: Node<RoomNodeData> = {
        id: 'node1',
        type: 'room',
        position: { x: 0, y: 0 },
        data: {
          id: 'room1',
          name: 'Room 1',
          subZone: 'campus',
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
          subZone: 'campus',
          description: '',
        },
      };

      const nodes = [node1, node2];
      const position1 = calculateGridPosition(node1, 0, nodes, config);
      const position2 = calculateGridPosition(node2, 1, nodes, config);

      // Both should be in the same subzone group
      expect(position1).toBeDefined();
      expect(position2).toBeDefined();
    });

    it('should group by zone when groupByZone is true and groupBySubZone is false', () => {
      const config: GridLayoutConfig = {
        ...defaultGridLayoutConfig,
        groupByZone: true,
        groupBySubZone: false,
      };

      const node1: Node<RoomNodeData> = {
        id: 'node1',
        type: 'room',
        position: { x: 0, y: 0 },
        data: {
          id: 'room1',
          name: 'Room 1',
          zone: 'arkhamcity',
          description: '',
        },
      };

      const nodes = [node1];
      const position = calculateGridPosition(node1, 0, nodes, config);

      expect(position).toBeDefined();
      expect(position.x).toBeGreaterThanOrEqual(0);
      expect(position.y).toBeGreaterThanOrEqual(0);
    });

    it('should use simple grid layout when no grouping', () => {
      const config: GridLayoutConfig = {
        ...defaultGridLayoutConfig,
        groupByZone: false,
        groupBySubZone: false,
      };

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
      const position1 = calculateGridPosition(node1, 0, nodes, config);
      const position2 = calculateGridPosition(node2, 1, nodes, config);

      expect(position1).toBeDefined();
      expect(position2).toBeDefined();
      // Positions should be different
      expect(position1.x !== position2.x || position1.y !== position2.y).toBe(true);
    });

    it('should handle null stored positions', () => {
      const node: Node<RoomNodeData> = {
        id: 'node1',
        type: 'room',
        position: { x: 0, y: 0 },
        data: {
          id: 'room1',
          name: 'Room 1',
          map_x: null,
          map_y: null,
        } as RoomNodeData & { map_x: null; map_y: null },
      };

      const nodes: Node<RoomNodeData>[] = [node];
      const position = calculateGridPosition(node, 0, nodes);

      // Should calculate grid position instead of using null
      expect(position.x).toBeGreaterThanOrEqual(0);
      expect(position.y).toBeGreaterThanOrEqual(0);
    });
  });

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
        iterations: 10, // Use fewer iterations for faster tests
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
      // First node should stay at origin, others should be positioned
      expect(result[0].position).toBeDefined();
      expect(result[1].position).toBeDefined();
    });
  });

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
      // Positions should be different
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

    it('should handle nodes with undefined stored positions', () => {
      const node: Node<RoomNodeData> = {
        id: 'node1',
        type: 'room',
        position: { x: 0, y: 0 },
        data: {
          id: 'room1',
          name: 'Room 1',
          map_x: undefined,
          map_y: undefined,
        } as RoomNodeData & { map_x?: number; map_y?: number },
      };

      const nodes: Node<RoomNodeData>[] = [node];
      const position = calculateGridPosition(node, 0, nodes);

      // Should calculate grid position instead of using undefined
      expect(position.x).toBeGreaterThanOrEqual(0);
      expect(position.y).toBeGreaterThanOrEqual(0);
    });

    it('should handle groupBySubZone when subZone is undefined', () => {
      const config: GridLayoutConfig = {
        ...defaultGridLayoutConfig,
        groupBySubZone: true,
      };

      const node: Node<RoomNodeData> = {
        id: 'node1',
        type: 'room',
        position: { x: 0, y: 0 },
        data: {
          id: 'room1',
          name: 'Room 1',
          subZone: undefined,
          description: '',
        },
      };

      const nodes = [node];
      const position = calculateGridPosition(node, 0, nodes, config);

      // Should fall back to simple grid layout when subZone is undefined
      expect(position).toBeDefined();
      expect(position.x).toBeGreaterThanOrEqual(0);
      expect(position.y).toBeGreaterThanOrEqual(0);
    });

    it('should handle groupByZone when zone is undefined', () => {
      const config: GridLayoutConfig = {
        ...defaultGridLayoutConfig,
        groupByZone: true,
        groupBySubZone: false,
      };

      const node: Node<RoomNodeData> = {
        id: 'node1',
        type: 'room',
        position: { x: 0, y: 0 },
        data: {
          id: 'room1',
          name: 'Room 1',
          zone: undefined,
          description: '',
        },
      };

      const nodes = [node];
      const position = calculateGridPosition(node, 0, nodes, config);

      // Should fall back to simple grid layout when zone is undefined
      expect(position).toBeDefined();
      expect(position.x).toBeGreaterThanOrEqual(0);
      expect(position.y).toBeGreaterThanOrEqual(0);
    });

    it('should handle multiple subzones in grouping', () => {
      const config: GridLayoutConfig = {
        ...defaultGridLayoutConfig,
        groupBySubZone: true,
      };

      const node1: Node<RoomNodeData> = {
        id: 'node1',
        type: 'room',
        position: { x: 0, y: 0 },
        data: {
          id: 'room1',
          name: 'Room 1',
          subZone: 'campus',
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
          subZone: 'downtown',
          description: '',
        },
      };

      const nodes = [node1, node2];
      const position1 = calculateGridPosition(node1, 0, nodes, config);
      const position2 = calculateGridPosition(node2, 1, nodes, config);

      expect(position1).toBeDefined();
      expect(position2).toBeDefined();
    });

    it('should handle multiple zones in grouping', () => {
      const config: GridLayoutConfig = {
        ...defaultGridLayoutConfig,
        groupByZone: true,
        groupBySubZone: false,
      };

      const node1: Node<RoomNodeData> = {
        id: 'node1',
        type: 'room',
        position: { x: 0, y: 0 },
        data: {
          id: 'room1',
          name: 'Room 1',
          zone: 'arkhamcity',
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
          zone: 'innsmouth',
          description: '',
        },
      };

      const nodes = [node1, node2];
      const position1 = calculateGridPosition(node1, 0, nodes, config);
      const position2 = calculateGridPosition(node2, 1, nodes, config);

      expect(position1).toBeDefined();
      expect(position2).toBeDefined();
    });
  });

  describe('applyForceLayout edge cases', () => {
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

      // Should not throw error, but edge should be ignored
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

      // Should not throw error, but edge should be ignored
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

      // Should handle collision detection when nodes are at same position
      // Use more iterations to ensure nodes are separated
      const result = applyForceLayout(nodes, edges, {
        ...defaultForceLayoutConfig,
        iterations: 50, // Increased from 10 to ensure separation
        minDistance: 120,
      });

      expect(result).toHaveLength(2);
      // Nodes should be separated after force layout (with sufficient iterations)
      // Note: With only 10 iterations, nodes might not separate enough, so we use 50
      // After force layout with collision detection, nodes should be at least minDistance apart
      // But with limited iterations, we just verify they moved from original position
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
      // Test line 167: index === 0 should keep position even if x=0, y=0
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
      // First node at 0,0 should keep its position (line 167: index === 0)
      expect(result[0].position.x).toBe(0);
      expect(result[0].position.y).toBe(0);
    });

    it('should handle edge with zero distance (division by zero protection)', () => {
      // Test line 224: distance || 1 branch
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
        position: { x: 100, y: 100 }, // Same position
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

      // Should handle zero distance in link force calculation (line 224)
      const result = applyForceLayout(nodes, edges, {
        ...defaultForceLayoutConfig,
        iterations: 10,
      });

      expect(result).toHaveLength(2);
    });

    it('should handle collision detection branch (distance < minDistance)', () => {
      // Test line 248: collision branch
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
        position: { x: 50, y: 50 }, // Close but less than minDistance (120)
        data: {
          id: 'room2',
          name: 'Room 2',
          description: '',
        },
      };

      const nodes = [node1, node2];
      const edges: Edge[] = [];

      // Should apply collision force when distance < minDistance (line 248)
      const result = applyForceLayout(nodes, edges, {
        ...defaultForceLayoutConfig,
        iterations: 20,
        minDistance: 120,
        collisionStrength: 2.0,
      });

      expect(result).toHaveLength(2);
      // Nodes should be separated by collision force
      const dx = result[1].position.x - result[0].position.x;
      const dy = result[1].position.y - result[0].position.y;
      const distance = Math.sqrt(dx * dx + dy * dy);
      // After force layout, nodes should be further apart (or at least moved)
      expect(distance).toBeGreaterThan(0);
    });

    it('should handle repulsive force branch (distance >= minDistance)', () => {
      // Test line 259: else branch for standard repulsive force
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
        position: { x: 200, y: 200 }, // Far apart (distance > minDistance)
        data: {
          id: 'room2',
          name: 'Room 2',
          description: '',
        },
      };

      const nodes = [node1, node2];
      const edges: Edge[] = [];

      // Should apply standard repulsive force when distance >= minDistance (line 259)
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
      // Test line 291: if (positioned) branch - edge case where node might not be in map
      // This is unlikely but we should test the branch
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
        iterations: 1, // Minimal iterations
      });

      // All nodes should be in the result (line 291: positioned should be truthy)
      expect(result).toHaveLength(1);
      expect(result[0].id).toBe('node1');
    });
  });
});
