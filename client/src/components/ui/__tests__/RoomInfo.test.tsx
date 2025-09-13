import { render, screen } from '@testing-library/react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import {
  CompleteRoomInfo,
  DebugInfo,
  RoomDescription,
  RoomEntities,
  RoomExits,
  RoomInfo,
  RoomLocation,
  RoomName,
  RoomOccupants,
} from '../RoomInfo';

describe('RoomInfo Compound Component', () => {
  const defaultRoom = {
    id: 'room-1',
    name: 'Test Room',
    description: 'A test room for testing purposes',
    plane: 'Material',
    zone: 'Arkham',
    sub_zone: 'Downtown',
    environment: 'Urban',
    exits: {
      north: 'room-2',
      south: 'room-3',
      east: 'room-4',
    },
    occupants: ['player-1', 'player-2'],
    occupant_count: 2,
    entities: [
      { name: 'Test NPC', type: 'npc' },
      { name: 'Test Item', type: 'item' },
      { name: 'Another NPC', type: 'npc' },
    ],
  };

  const defaultDebugInfo = {
    hasRoom: true,
    roomType: 'object',
    roomKeys: ['id', 'name', 'description', 'exits'],
    timestamp: '2024-01-01T12:00:00Z',
  };

  beforeEach(() => {
    vi.clearAllMocks();
  });

  afterEach(() => {
    vi.restoreAllMocks();
  });

  describe('RoomInfo Provider', () => {
    it('should provide context to child components', () => {
      render(
        <RoomInfo room={defaultRoom} debugInfo={defaultDebugInfo}>
          <RoomName />
        </RoomInfo>
      );

      expect(screen.getByText('Test Room')).toBeInTheDocument();
    });

    it('should throw error when child components are used outside provider', () => {
      // Suppress console.error for this test
      const consoleSpy = vi.spyOn(console, 'error').mockImplementation(() => {});

      expect(() => {
        render(<RoomName />);
      }).toThrow('useRoomInfo must be used within a RoomInfo');

      consoleSpy.mockRestore();
    });
  });

  describe('RoomName', () => {
    it('should display room name when room exists', () => {
      render(
        <RoomInfo room={defaultRoom}>
          <RoomName />
        </RoomInfo>
      );

      expect(screen.getByText('Test Room')).toBeInTheDocument();
    });

    it('should display no room message when room is null', () => {
      render(
        <RoomInfo room={null}>
          <RoomName />
        </RoomInfo>
      );

      expect(screen.getByText('No room information available')).toBeInTheDocument();
    });
  });

  describe('RoomDescription', () => {
    it('should display room description when room exists', () => {
      render(
        <RoomInfo room={defaultRoom}>
          <RoomDescription />
        </RoomInfo>
      );

      expect(screen.getByText('A test room for testing purposes')).toBeInTheDocument();
    });

    it('should not display when room is null', () => {
      render(
        <RoomInfo room={null}>
          <RoomDescription />
        </RoomInfo>
      );

      expect(screen.queryByText('A test room for testing purposes')).not.toBeInTheDocument();
    });
  });

  describe('RoomLocation', () => {
    it('should display all location information when available', () => {
      render(
        <RoomInfo room={defaultRoom}>
          <RoomLocation />
        </RoomInfo>
      );

      expect(screen.getByText('Location')).toBeInTheDocument();
      expect(screen.getByText('Plane:')).toBeInTheDocument();
      expect(screen.getByText('Material')).toBeInTheDocument();
      expect(screen.getByText('Zone:')).toBeInTheDocument();
      expect(screen.getByText('Arkham')).toBeInTheDocument();
      expect(screen.getByText('Sub-zone:')).toBeInTheDocument();
      expect(screen.getByText('Downtown')).toBeInTheDocument();
      expect(screen.getByText('Environment:')).toBeInTheDocument();
      expect(screen.getByText('Urban')).toBeInTheDocument();
    });

    it('should not display when room is null', () => {
      render(
        <RoomInfo room={null}>
          <RoomLocation />
        </RoomInfo>
      );

      expect(screen.queryByText('Location')).not.toBeInTheDocument();
    });

    it('should only display available location fields', () => {
      const roomWithLimitedLocation = {
        ...defaultRoom,
        plane: undefined,
        environment: undefined,
      };

      render(
        <RoomInfo room={roomWithLimitedLocation}>
          <RoomLocation />
        </RoomInfo>
      );

      expect(screen.getByText('Zone:')).toBeInTheDocument();
      expect(screen.getByText('Sub-zone:')).toBeInTheDocument();
      expect(screen.queryByText('Plane:')).not.toBeInTheDocument();
      expect(screen.queryByText('Environment:')).not.toBeInTheDocument();
    });
  });

  describe('RoomExits', () => {
    it('should display all exits when available', () => {
      render(
        <RoomInfo room={defaultRoom}>
          <RoomExits />
        </RoomInfo>
      );

      expect(screen.getByText('Exits')).toBeInTheDocument();
      expect(screen.getByText('North')).toBeInTheDocument();
      expect(screen.getByText('South')).toBeInTheDocument();
      expect(screen.getByText('East')).toBeInTheDocument();
    });

    it('should display no exits message when no exits', () => {
      const roomWithoutExits = { ...defaultRoom, exits: {} };

      render(
        <RoomInfo room={roomWithoutExits}>
          <RoomExits />
        </RoomInfo>
      );

      expect(screen.getByText('No exits available')).toBeInTheDocument();
    });

    it('should display no exits message when room is null', () => {
      render(
        <RoomInfo room={null}>
          <RoomExits />
        </RoomInfo>
      );

      expect(screen.getByText('No exits available')).toBeInTheDocument();
    });

    it('should handle unknown exit directions', () => {
      const roomWithUnknownExits = {
        ...defaultRoom,
        exits: {
          north: 'room-2',
          unknown: 'room-3',
          another_unknown: 'room-4',
        },
      };

      render(
        <RoomInfo room={roomWithUnknownExits}>
          <RoomExits />
        </RoomInfo>
      );

      expect(screen.getByText('North')).toBeInTheDocument();
      expect(screen.getByText('unknown')).toBeInTheDocument();
      expect(screen.getByText('another_unknown')).toBeInTheDocument();
    });
  });

  describe('RoomOccupants', () => {
    it('should display all occupants when available', () => {
      render(
        <RoomInfo room={defaultRoom}>
          <RoomOccupants />
        </RoomInfo>
      );

      expect(screen.getByText('Occupants (2)')).toBeInTheDocument();
      expect(screen.getByText('• player-1')).toBeInTheDocument();
      expect(screen.getByText('• player-2')).toBeInTheDocument();
    });

    it('should display no occupants message when no occupants', () => {
      const roomWithoutOccupants = { ...defaultRoom, occupants: [], occupant_count: 0 };

      render(
        <RoomInfo room={roomWithoutOccupants}>
          <RoomOccupants />
        </RoomInfo>
      );

      expect(screen.getByText('No one else is here')).toBeInTheDocument();
    });

    it('should display no occupants message when room is null', () => {
      render(
        <RoomInfo room={null}>
          <RoomOccupants />
        </RoomInfo>
      );

      expect(screen.getByText('No one else is here')).toBeInTheDocument();
    });

    it('should use occupant_count when available', () => {
      const roomWithCount = { ...defaultRoom, occupant_count: 5 };

      render(
        <RoomInfo room={roomWithCount}>
          <RoomOccupants />
        </RoomInfo>
      );

      expect(screen.getByText('Occupants (5)')).toBeInTheDocument();
    });
  });

  describe('RoomEntities', () => {
    it('should display all entities grouped by type', () => {
      render(
        <RoomInfo room={defaultRoom}>
          <RoomEntities />
        </RoomInfo>
      );

      expect(screen.getByText('Entities')).toBeInTheDocument();
      expect(screen.getByText('npc')).toBeInTheDocument();
      expect(screen.getByText('• Test NPC')).toBeInTheDocument();
      expect(screen.getByText('• Another NPC')).toBeInTheDocument();
      expect(screen.getByText('item')).toBeInTheDocument();
      expect(screen.getByText('• Test Item')).toBeInTheDocument();
    });

    it('should display no entities message when no entities', () => {
      const roomWithoutEntities = { ...defaultRoom, entities: [] };

      render(
        <RoomInfo room={roomWithoutEntities}>
          <RoomEntities />
        </RoomInfo>
      );

      expect(screen.getByText('No entities present')).toBeInTheDocument();
    });

    it('should display no entities message when room is null', () => {
      render(
        <RoomInfo room={null}>
          <RoomEntities />
        </RoomInfo>
      );

      expect(screen.getByText('No entities present')).toBeInTheDocument();
    });
  });

  describe('DebugInfo', () => {
    it('should display debug information when available', () => {
      render(
        <RoomInfo room={defaultRoom} debugInfo={defaultDebugInfo}>
          <DebugInfo />
        </RoomInfo>
      );

      expect(screen.getByText('Debug Info')).toBeInTheDocument();
      expect(screen.getByText('Has Room:')).toBeInTheDocument();
      expect(screen.getByText('Yes')).toBeInTheDocument();
      expect(screen.getByText('Room Type:')).toBeInTheDocument();
      expect(screen.getByText('object')).toBeInTheDocument();
      expect(screen.getByText('Room Keys:')).toBeInTheDocument();
      expect(screen.getByText('id, name, description, exits')).toBeInTheDocument();
      expect(screen.getByText('Timestamp:')).toBeInTheDocument();
      expect(screen.getByText('2024-01-01T12:00:00Z')).toBeInTheDocument();
    });

    it('should not display when debug info is not provided', () => {
      render(
        <RoomInfo room={defaultRoom}>
          <DebugInfo />
        </RoomInfo>
      );

      expect(screen.queryByText('Debug Info')).not.toBeInTheDocument();
    });
  });

  describe('CompleteRoomInfo', () => {
    it('should display all room information', () => {
      render(
        <RoomInfo room={defaultRoom} debugInfo={defaultDebugInfo}>
          <CompleteRoomInfo />
        </RoomInfo>
      );

      // Check that all components are rendered
      expect(screen.getByText('Test Room')).toBeInTheDocument();
      expect(screen.getByText('A test room for testing purposes')).toBeInTheDocument();
      expect(screen.getByText('Location')).toBeInTheDocument();
      expect(screen.getByText('Exits')).toBeInTheDocument();
      expect(screen.getByText('Occupants (2)')).toBeInTheDocument();
      expect(screen.getByText('Entities')).toBeInTheDocument();
      expect(screen.getByText('Debug Info')).toBeInTheDocument();
    });

    it('should handle null room gracefully', () => {
      render(
        <RoomInfo room={null}>
          <CompleteRoomInfo />
        </RoomInfo>
      );

      expect(screen.getByText('No room information available')).toBeInTheDocument();
    });
  });

  describe('Custom Composition', () => {
    it('should allow custom composition of components', () => {
      render(
        <RoomInfo room={defaultRoom}>
          <RoomName />
          <RoomDescription />
          <RoomExits />
        </RoomInfo>
      );

      expect(screen.getByText('Test Room')).toBeInTheDocument();
      expect(screen.getByText('A test room for testing purposes')).toBeInTheDocument();
      expect(screen.getByText('Exits')).toBeInTheDocument();
      // Should not display components not included
      expect(screen.queryByText('Location')).not.toBeInTheDocument();
      expect(screen.queryByText('Occupants')).not.toBeInTheDocument();
      expect(screen.queryByText('Entities')).not.toBeInTheDocument();
    });
  });
});
