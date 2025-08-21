import { render, screen } from '@testing-library/react';
import { beforeEach, describe, expect, it, vi } from 'vitest';
import { RoomInfoPanel } from './RoomInfoPanel';

// Mock console.log to avoid noise in tests
const mockConsoleLog = vi.fn();
console.log = mockConsoleLog;

describe('RoomInfoPanel', () => {
  beforeEach(() => {
    vi.clearAllMocks();
  });

  describe('No Room State', () => {
    it('should display no room message when room is null', () => {
      render(<RoomInfoPanel room={null} />);

      expect(screen.getByText('No room information available')).toBeInTheDocument();
    });
  });

  describe('Room Display', () => {
    const mockRoom = {
      id: 'test-room-1',
      name: 'Test Room',
      description: 'A mysterious test room with eldritch properties.',
      plane: 'earth',
      zone: 'arkham',
      sub_zone: 'university',
      environment: 'indoor',
      exits: {
        north: 'test-room-2',
        south: null,
        east: 'test-room-3',
        west: null,
      },
      occupants: ['player1', 'player2'],
      occupant_count: 2,
    };

    it('should display room name', () => {
      render(<RoomInfoPanel room={mockRoom} />);

      expect(screen.getByText('Test Room')).toBeInTheDocument();
    });

    it('should format and display zone information', () => {
      render(<RoomInfoPanel room={mockRoom} />);

      expect(screen.getByText('Zone:')).toBeInTheDocument();
      expect(screen.getByText('Arkham')).toBeInTheDocument();
    });

    it('should format and display subzone information', () => {
      render(<RoomInfoPanel room={mockRoom} />);

      expect(screen.getByText('Subzone:')).toBeInTheDocument();
      expect(screen.getByText('University')).toBeInTheDocument();
    });

    it('should display room description', () => {
      render(<RoomInfoPanel room={mockRoom} />);

      expect(screen.getByText('Description:')).toBeInTheDocument();
      expect(screen.getByText('A mysterious test room with eldritch properties.')).toBeInTheDocument();
    });

    it('should display available exits', () => {
      render(<RoomInfoPanel room={mockRoom} />);

      expect(screen.getByText('Exits:')).toBeInTheDocument();
      expect(screen.getByText('North, East')).toBeInTheDocument();
    });

    it('should display occupants with count', () => {
      render(<RoomInfoPanel room={mockRoom} />);

      expect(screen.getByText('Occupants')).toBeInTheDocument();
      expect(screen.getByText('(2)')).toBeInTheDocument();
      expect(screen.getByText('Player1')).toBeInTheDocument();
      expect(screen.getByText('Player2')).toBeInTheDocument();
    });
  });

  describe('Formatting Functions', () => {
    it('should handle room with unknown zone and subzone', () => {
      const roomWithUnknown = {
        id: 'test-room-2',
        name: 'Unknown Room',
        description: 'A room with unknown location.',
        exits: {},
        occupants: [],
      };

      render(<RoomInfoPanel room={roomWithUnknown} />);

      expect(screen.getByText('Zone:')).toBeInTheDocument();
      expect(screen.getByText('Subzone:')).toBeInTheDocument();
      // Check that both zone and subzone show "Unknown" by using getAllByText
      const unknownElements = screen.getAllByText('Unknown');
      expect(unknownElements).toHaveLength(2);
    });

    it('should handle room with no description', () => {
      const roomWithoutDescription = {
        id: 'test-room-3',
        name: 'Empty Room',
        description: '',
        exits: {},
        occupants: [],
      };

      render(<RoomInfoPanel room={roomWithoutDescription} />);

      expect(screen.getByText('No description available')).toBeInTheDocument();
    });

    it('should handle room with no exits', () => {
      const roomWithoutExits = {
        id: 'test-room-4',
        name: 'Dead End Room',
        description: 'A room with no exits.',
        exits: {},
        occupants: [],
      };

      render(<RoomInfoPanel room={roomWithoutExits} />);

      expect(screen.getByText('None')).toBeInTheDocument();
    });

    it('should handle room with no occupants', () => {
      const roomWithoutOccupants = {
        id: 'test-room-5',
        name: 'Empty Room',
        description: 'A room with no occupants.',
        exits: { north: 'test-room-6' },
        occupants: [],
      };

      render(<RoomInfoPanel room={roomWithoutOccupants} />);

      expect(screen.getByText('No other players present')).toBeInTheDocument();
    });

    it('should format location names with underscores', () => {
      const roomWithUnderscores = {
        id: 'test-room-6',
        name: 'Underscore Room',
        description: 'A room with underscore formatting.',
        zone: 'arkham_city',
        sub_zone: 'university_library',
        exits: {},
        occupants: [],
      };

      render(<RoomInfoPanel room={roomWithUnderscores} />);

      expect(screen.getByText('Arkham City')).toBeInTheDocument();
      expect(screen.getByText('University Library')).toBeInTheDocument();
    });

    it('should handle room without occupant count', () => {
      const roomWithoutCount = {
        id: 'test-room-7',
        name: 'Countless Room',
        description: 'A room without occupant count.',
        exits: {},
        occupants: ['player1'],
      };

      render(<RoomInfoPanel room={roomWithoutCount} />);

      expect(screen.getByText('Occupants')).toBeInTheDocument();
      expect(screen.queryByText(/\(\d+\)/)).not.toBeInTheDocument();
      expect(screen.getByText('Player1')).toBeInTheDocument();
    });
  });

  describe('Edge Cases', () => {
    it('should handle room with null exits', () => {
      const roomWithNullExits = {
        id: 'test-room-8',
        name: 'Null Exits Room',
        description: 'A room with null exits.',
        exits: undefined,
        occupants: [],
      };

      render(<RoomInfoPanel room={roomWithNullExits} />);

      expect(screen.getByText('None')).toBeInTheDocument();
    });

    it('should handle room with null occupants', () => {
      const roomWithNullOccupants = {
        id: 'test-room-9',
        name: 'Null Occupants Room',
        description: 'A room with null occupants.',
        exits: {},
        occupants: undefined,
      };

      render(<RoomInfoPanel room={roomWithNullOccupants} />);

      expect(screen.getByText('No other players present')).toBeInTheDocument();
    });

    it('should handle room with all null exits', () => {
      const roomWithAllNullExits = {
        id: 'test-room-10',
        name: 'All Null Exits Room',
        description: 'A room with all null exits.',
        exits: {
          north: null,
          south: null,
          east: null,
          west: null,
        },
        occupants: [],
      };

      render(<RoomInfoPanel room={roomWithAllNullExits} />);

      expect(screen.getByText('None')).toBeInTheDocument();
    });
  });
});
