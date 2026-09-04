/**
 * Tests for calculateGridPosition function.
 */

import type { Node } from 'reactflow';
import { describe, expect, it } from 'vitest';
import type { RoomNodeData } from '../../types';
import { calculateGridPosition, defaultGridLayoutConfig, type GridLayoutConfig } from '../layout';

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

    expect(position.x).toBeGreaterThanOrEqual(0);
    expect(position.y).toBeGreaterThanOrEqual(0);
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
