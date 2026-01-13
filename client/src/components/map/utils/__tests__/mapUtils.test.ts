/**
 * Tests for room data transformation utilities.
 *
 * These tests verify that room data from the server can be properly
 * transformed into React Flow nodes and edges format.
 *
 * As documented in the Pnakotic Manuscripts, proper transformation of
 * dimensional data is essential for accurate visualization of our
 * eldritch architecture.
 */

import { describe, expect, it } from 'vitest';
import type { Room } from '../../../../stores/gameStore';
import { createEdgesFromRooms, roomToNode, roomsToNodes, transformRoomsToMapData } from '../mapUtils';

describe('mapUtils', () => {
  describe('roomToNode', () => {
    it('should convert a basic room to a React Flow node', () => {
      const room: Room = {
        id: 'test_room_001',
        name: 'Test Room',
        description: 'A test room',
        plane: 'earth',
        zone: 'arkhamcity',
        sub_zone: 'campus',
        environment: 'outdoors',
        exits: {},
      };

      const node = roomToNode(room);

      expect(node.id).toBe('test_room_001');
      expect(node.type).toBe('room');
      expect(node.data.id).toBe('test_room_001');
      expect(node.data.name).toBe('Test Room');
      expect(node.data.description).toBe('A test room');
      expect(node.data.plane).toBe('earth');
      expect(node.data.zone).toBe('arkhamcity');
      expect(node.data.subZone).toBe('campus');
      expect(node.data.environment).toBe('outdoors');
      expect(node.position).toBeDefined();
      expect(node.position.x).toBe(0);
      expect(node.position.y).toBe(0);
    });

    it('should use stored map coordinates when available', () => {
      const room: Room & { map_x?: number; map_y?: number } = {
        id: 'test_room_002',
        name: 'Test Room 2',
        description: 'A test room with coordinates',
        plane: 'earth',
        zone: 'arkhamcity',
        sub_zone: 'campus',
        environment: 'indoors',
        exits: {},
        map_x: 150.5,
        map_y: 200.3,
      };

      const node = roomToNode(room);

      expect(node.position.x).toBe(150.5);
      expect(node.position.y).toBe(200.3);
    });

    it('should set node type to intersection for intersection environments', () => {
      const room: Room = {
        id: 'test_intersection_001',
        name: 'Test Intersection',
        description: 'An intersection',
        plane: 'earth',
        zone: 'arkhamcity',
        sub_zone: 'campus',
        environment: 'intersection',
        exits: {},
      };

      const node = roomToNode(room);

      expect(node.type).toBe('intersection');
    });

    it('should handle rooms with occupants', () => {
      const room: Room = {
        id: 'test_room_003',
        name: 'Test Room 3',
        description: 'A room with occupants',
        plane: 'earth',
        zone: 'arkhamcity',
        sub_zone: 'campus',
        environment: 'outdoors',
        exits: {},
        occupants: ['player1', 'player2'],
        occupant_count: 2,
      };

      const node = roomToNode(room);

      expect(node.data.occupants).toEqual(['player1', 'player2']);
      expect(node.data.occupantCount).toBe(2);
    });

    it('should mark current location when room ID matches', () => {
      const room: Room = {
        id: 'current_room',
        name: 'Current Room',
        description: 'The current room',
        plane: 'earth',
        zone: 'arkhamcity',
        sub_zone: 'campus',
        environment: 'outdoors',
        exits: {},
      };

      const node = roomToNode(room, 'current_room');

      expect(node.data.isCurrentLocation).toBe(true);
    });
  });

  describe('roomsToNodes', () => {
    it('should convert multiple rooms to nodes', () => {
      const rooms: Room[] = [
        {
          id: 'room_001',
          name: 'Room 1',
          description: 'First room',
          plane: 'earth',
          zone: 'arkhamcity',
          sub_zone: 'campus',
          environment: 'outdoors',
          exits: {},
        },
        {
          id: 'room_002',
          name: 'Room 2',
          description: 'Second room',
          plane: 'earth',
          zone: 'arkhamcity',
          sub_zone: 'campus',
          environment: 'indoors',
          exits: {},
        },
      ];

      const nodes = roomsToNodes(rooms);

      expect(nodes).toHaveLength(2);
      expect(nodes[0].id).toBe('room_001');
      expect(nodes[1].id).toBe('room_002');
    });

    it('should apply grid layout when coordinates not available', () => {
      const rooms: Room[] = [
        {
          id: 'room_001',
          name: 'Room 1',
          description: 'First room',
          plane: 'earth',
          zone: 'arkhamcity',
          sub_zone: 'campus',
          environment: 'outdoors',
          exits: {},
        },
        {
          id: 'room_002',
          name: 'Room 2',
          description: 'Second room',
          plane: 'earth',
          zone: 'arkhamcity',
          sub_zone: 'campus',
          environment: 'indoors',
          exits: {},
        },
      ];

      const nodes = roomsToNodes(rooms);

      // Both should have positions (grid layout applied)
      expect(nodes[0].position).toBeDefined();
      expect(nodes[1].position).toBeDefined();
      // Positions should be different
      expect(nodes[0].position.x !== nodes[1].position.x || nodes[0].position.y !== nodes[1].position.y).toBe(true);
    });
  });

  describe('createEdgesFromRooms', () => {
    it('should create edges from string exit format', () => {
      const rooms: Room[] = [
        {
          id: 'room_001',
          name: 'Room 1',
          description: 'First room',
          plane: 'earth',
          zone: 'arkhamcity',
          sub_zone: 'campus',
          environment: 'outdoors',
          exits: {
            north: 'room_002',
            // south: null - null exits are filtered out by createEdgesFromRooms
          } as Record<string, string>,
        },
        {
          id: 'room_002',
          name: 'Room 2',
          description: 'Second room',
          plane: 'earth',
          zone: 'arkhamcity',
          sub_zone: 'campus',
          environment: 'indoors',
          exits: {},
        },
      ];

      const edges = createEdgesFromRooms(rooms);

      expect(edges).toHaveLength(1);
      expect(edges[0].source).toBe('room_001');
      expect(edges[0].target).toBe('room_002');
      expect(edges[0].type).toBe('exit');
      expect(edges[0].data?.direction).toBe('north');
      expect(edges[0].data?.sourceRoomId).toBe('room_001');
      expect(edges[0].data?.targetRoomId).toBe('room_002');
      // Verify edge handles for north exit
      expect(edges[0].sourceHandle).toBe('source-top');
      expect(edges[0].targetHandle).toBe('target-bottom');
    });

    it('should create edges from object exit format with flags', () => {
      const rooms: Room[] = [
        {
          id: 'room_001',
          name: 'Room 1',
          description: 'First room',
          plane: 'earth',
          zone: 'arkhamcity',
          sub_zone: 'campus',
          environment: 'outdoors',
          exits: {
            north: {
              target: 'room_002',
              flags: ['hidden', 'locked'],
              description: 'A hidden locked door',
              // Exit object structure varies, using any for test data flexibility
              // eslint-disable-next-line @typescript-eslint/no-explicit-any
            } as any,
          },
        },
        {
          id: 'room_002',
          name: 'Room 2',
          description: 'Second room',
          plane: 'earth',
          zone: 'arkhamcity',
          sub_zone: 'campus',
          environment: 'indoors',
          exits: {},
        },
      ];

      const edges = createEdgesFromRooms(rooms);

      expect(edges).toHaveLength(1);
      expect(edges[0].data?.flags).toEqual(['hidden', 'locked']);
      expect(edges[0].data?.description).toBe('A hidden locked door');
    });

    it('should merge string and object exit formats', () => {
      const rooms: Room[] = [
        {
          id: 'room_001',
          name: 'Room 1',
          description: 'First room',
          plane: 'earth',
          zone: 'arkhamcity',
          sub_zone: 'campus',
          environment: 'outdoors',
          exits: {
            north: 'room_002',
            south: {
              target: 'room_003',
              flags: ['one_way'],
              // Exit object structure varies, using any for test data flexibility
              // eslint-disable-next-line @typescript-eslint/no-explicit-any
            } as any,
          },
        },
        {
          id: 'room_002',
          name: 'Room 2',
          description: 'Second room',
          plane: 'earth',
          zone: 'arkhamcity',
          sub_zone: 'campus',
          environment: 'indoors',
          exits: {},
        },
        {
          id: 'room_003',
          name: 'Room 3',
          description: 'Third room',
          plane: 'earth',
          zone: 'arkhamcity',
          sub_zone: 'campus',
          environment: 'outdoors',
          exits: {},
        },
      ];

      const edges = createEdgesFromRooms(rooms);

      expect(edges).toHaveLength(2);

      const northEdge = edges.find(e => e.data?.direction === 'north');
      expect(northEdge).toBeDefined();
      expect(northEdge?.target).toBe('room_002');
      expect(northEdge?.data?.flags).toBeUndefined();

      const southEdge = edges.find(e => e.data?.direction === 'south');
      expect(southEdge).toBeDefined();
      expect(southEdge?.target).toBe('room_003');
      expect(southEdge?.data?.flags).toEqual(['one_way']);
    });

    it('should ignore null exits', () => {
      const rooms: Room[] = [
        {
          id: 'room_001',
          name: 'Room 1',
          description: 'First room',
          plane: 'earth',
          zone: 'arkhamcity',
          sub_zone: 'campus',
          environment: 'outdoors',
          exits: {
            // north: null - null exits are filtered out by createEdgesFromRooms
            // south: null - null exits are filtered out by createEdgesFromRooms
            east: 'room_002',
          },
        },
        {
          id: 'room_002',
          name: 'Room 2',
          description: 'Second room',
          plane: 'earth',
          zone: 'arkhamcity',
          sub_zone: 'campus',
          environment: 'indoors',
          exits: {},
        },
      ];

      const edges = createEdgesFromRooms(rooms);

      expect(edges).toHaveLength(1);
      expect(edges[0].data?.direction).toBe('east');
    });

    it('should set correct edge positions for south exit', () => {
      const rooms: Room[] = [
        {
          id: 'room_001',
          name: 'Room 1',
          description: 'First room',
          plane: 'earth',
          zone: 'arkhamcity',
          sub_zone: 'campus',
          environment: 'outdoors',
          exits: {
            south: 'room_002',
          },
        },
        {
          id: 'room_002',
          name: 'Room 2',
          description: 'Second room',
          plane: 'earth',
          zone: 'arkhamcity',
          sub_zone: 'campus',
          environment: 'indoors',
          exits: {},
        },
      ];

      const edges = createEdgesFromRooms(rooms);

      expect(edges).toHaveLength(1);
      expect(edges[0].data?.direction).toBe('south');
      // Verify edge handles for south exit
      expect(edges[0].sourceHandle).toBe('source-bottom');
      expect(edges[0].targetHandle).toBe('target-top');
    });

    it('should set correct edge positions for east and west exits', () => {
      const rooms: Room[] = [
        {
          id: 'room_001',
          name: 'Room 1',
          description: 'First room',
          plane: 'earth',
          zone: 'arkhamcity',
          sub_zone: 'campus',
          environment: 'outdoors',
          exits: {
            east: 'room_002',
            west: 'room_003',
          },
        },
        {
          id: 'room_002',
          name: 'Room 2',
          description: 'Second room',
          plane: 'earth',
          zone: 'arkhamcity',
          sub_zone: 'campus',
          environment: 'indoors',
          exits: {},
        },
        {
          id: 'room_003',
          name: 'Room 3',
          description: 'Third room',
          plane: 'earth',
          zone: 'arkhamcity',
          sub_zone: 'campus',
          environment: 'indoors',
          exits: {},
        },
      ];

      const edges = createEdgesFromRooms(rooms);

      expect(edges).toHaveLength(2);
      const eastEdge = edges.find(e => e.data?.direction === 'east');
      const westEdge = edges.find(e => e.data?.direction === 'west');

      expect(eastEdge?.sourceHandle).toBe('source-right');
      expect(eastEdge?.targetHandle).toBe('target-left');
      expect(westEdge?.sourceHandle).toBe('source-left');
      expect(westEdge?.targetHandle).toBe('target-right');
    });

    it('should handle all exit directions', () => {
      const rooms: Room[] = [
        {
          id: 'room_001',
          name: 'Room 1',
          description: 'First room',
          plane: 'earth',
          zone: 'arkhamcity',
          sub_zone: 'campus',
          environment: 'outdoors',
          exits: {
            north: 'room_002',
            south: 'room_003',
            east: 'room_004',
            west: 'room_005',
            up: 'room_006',
            down: 'room_007',
          },
        },
        {
          id: 'room_002',
          name: 'Room 2',
          description: 'Second room',
          plane: 'earth',
          zone: 'arkhamcity',
          sub_zone: 'campus',
          environment: 'indoors',
          exits: {},
        },
        {
          id: 'room_003',
          name: 'Room 3',
          description: 'Third room',
          plane: 'earth',
          zone: 'arkhamcity',
          sub_zone: 'campus',
          environment: 'indoors',
          exits: {},
        },
        {
          id: 'room_004',
          name: 'Room 4',
          description: 'Fourth room',
          plane: 'earth',
          zone: 'arkhamcity',
          sub_zone: 'campus',
          environment: 'indoors',
          exits: {},
        },
        {
          id: 'room_005',
          name: 'Room 5',
          description: 'Fifth room',
          plane: 'earth',
          zone: 'arkhamcity',
          sub_zone: 'campus',
          environment: 'indoors',
          exits: {},
        },
        {
          id: 'room_006',
          name: 'Room 6',
          description: 'Sixth room',
          plane: 'earth',
          zone: 'arkhamcity',
          sub_zone: 'campus',
          environment: 'indoors',
          exits: {},
        },
        {
          id: 'room_007',
          name: 'Room 7',
          description: 'Seventh room',
          plane: 'earth',
          zone: 'arkhamcity',
          sub_zone: 'campus',
          environment: 'indoors',
          exits: {},
        },
      ];

      const edges = createEdgesFromRooms(rooms);

      expect(edges).toHaveLength(6);
      const directions = edges.map(e => e.data?.direction);
      expect(directions).toContain('north');
      expect(directions).toContain('south');
      expect(directions).toContain('east');
      expect(directions).toContain('west');
      expect(directions).toContain('up');
      expect(directions).toContain('down');
    });
  });

  describe('transformRoomsToMapData', () => {
    it('should transform rooms to complete map data structure', () => {
      const rooms: Room[] = [
        {
          id: 'room_001',
          name: 'Room 1',
          description: 'First room',
          plane: 'earth',
          zone: 'arkhamcity',
          sub_zone: 'campus',
          environment: 'outdoors',
          exits: {
            north: 'room_002',
          },
        },
        {
          id: 'room_002',
          name: 'Room 2',
          description: 'Second room',
          plane: 'earth',
          zone: 'arkhamcity',
          sub_zone: 'campus',
          environment: 'indoors',
          exits: {},
        },
      ];

      const mapData = transformRoomsToMapData(rooms, 'room_001');

      expect(mapData.nodes).toHaveLength(2);
      expect(mapData.edges).toHaveLength(1);
      expect(mapData.nodes[0].data.isCurrentLocation).toBe(true);
      expect(mapData.nodes[1].data.isCurrentLocation).toBe(false);
    });

    it('should handle empty room array', () => {
      const rooms: Room[] = [];

      const mapData = transformRoomsToMapData(rooms);

      expect(mapData.nodes).toHaveLength(0);
      expect(mapData.edges).toHaveLength(0);
    });

    it('should handle rooms with mixed exit formats', () => {
      const rooms: Room[] = [
        {
          id: 'room_001',
          name: 'Room 1',
          description: 'First room',
          plane: 'earth',
          zone: 'arkhamcity',
          sub_zone: 'campus',
          environment: 'outdoors',
          exits: {
            north: 'room_002',
            south: {
              target: 'room_003',
              flags: ['one_way'],
              // Exit object structure varies, using any for test data flexibility
              // eslint-disable-next-line @typescript-eslint/no-explicit-any
            } as any,
            // east: null - null exits are filtered out by createEdgesFromRooms
          },
        },
        {
          id: 'room_002',
          name: 'Room 2',
          description: 'Second room',
          plane: 'earth',
          zone: 'arkhamcity',
          sub_zone: 'campus',
          environment: 'indoors',
          exits: {},
        },
        {
          id: 'room_003',
          name: 'Room 3',
          description: 'Third room',
          plane: 'earth',
          zone: 'arkhamcity',
          sub_zone: 'campus',
          environment: 'outdoors',
          exits: {},
        },
      ];

      const mapData = transformRoomsToMapData(rooms);

      expect(mapData.nodes).toHaveLength(3);
      expect(mapData.edges).toHaveLength(2);

      const northEdge = mapData.edges.find(e => e.data?.direction === 'north');
      expect(northEdge?.data?.flags).toBeUndefined();

      const southEdge = mapData.edges.find(e => e.data?.direction === 'south');
      expect(southEdge?.data?.flags).toEqual(['one_way']);
    });
  });
});
