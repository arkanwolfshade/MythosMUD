import '@testing-library/jest-dom';
import { render, screen } from '@testing-library/react';
import { vi } from 'vitest';
import { RoomInfoPanel } from '../RoomInfoPanel';

interface Room {
  id: string;
  name: string;
  description: string;
  plane?: string;
  zone?: string;
  sub_zone?: string;
  environment?: string;
  exits?: Record<string, string | null>;
  occupants?: string[];
  occupant_count?: number;
}

// Mock console.log to avoid noise in tests
const mockConsoleLog = vi.spyOn(console, 'log').mockImplementation(() => {});

describe('RoomInfoPanel', () => {
  afterEach(() => {
    mockConsoleLog.mockClear();
  });

  afterAll(() => {
    mockConsoleLog.mockRestore();
  });

  const mockRoom = {
    id: 'test-room-1',
    name: 'Test Room',
    description: 'A test room for testing purposes.',
    zone: 'arkham',
    sub_zone: 'university',
    plane: 'material',
    environment: 'indoor',
    exits: {
      north: 'room-2',
      south: null,
      east: 'room-3',
      west: 'room-4',
    },
    occupants: ['Player1', 'Player2'],
    occupant_count: 2,
  };

  const mockDebugInfo = {
    hasRoom: true,
    roomType: 'object',
    roomKeys: ['id', 'name', 'description'],
    timestamp: new Date().toISOString(),
  };

  describe('Rendering with valid room data', () => {
    it('should render room information correctly', () => {
      render(<RoomInfoPanel room={mockRoom} debugInfo={mockDebugInfo} />);

      expect(screen.getByText('Test Room')).toBeInTheDocument();
      expect(screen.getByText('A test room for testing purposes.')).toBeInTheDocument();
      expect(screen.getByText('Zone:')).toBeInTheDocument();
      expect(screen.getByText('Arkham')).toBeInTheDocument();
      expect(screen.getByText('Subzone:')).toBeInTheDocument();
      expect(screen.getByText('University')).toBeInTheDocument();
    });

    it('should display exits correctly', () => {
      render(<RoomInfoPanel room={mockRoom} debugInfo={mockDebugInfo} />);

      expect(screen.getByText('Exits:')).toBeInTheDocument();
      expect(screen.getByText('North, East, West')).toBeInTheDocument();
    });

    it('should display occupants correctly', () => {
      render(<RoomInfoPanel room={mockRoom} debugInfo={mockDebugInfo} />);

      expect(screen.getByText('Occupants')).toBeInTheDocument();
      expect(screen.getByText('(2)')).toBeInTheDocument();
      expect(screen.getByText('Player1')).toBeInTheDocument();
      expect(screen.getByText('Player2')).toBeInTheDocument();
    });
  });

  describe('Rendering with null room data', () => {
    it('should show no-room message when room is null and no debug info', () => {
      render(<RoomInfoPanel room={null} />);

      expect(screen.getByText('No room information available')).toBeInTheDocument();
    });

    it('should show development mock data when room is null but debug info exists', () => {
      render(<RoomInfoPanel room={null} debugInfo={mockDebugInfo} />);

      expect(screen.getByText('Miskatonic University Library')).toBeInTheDocument();
      expect(screen.getByText(/A vast repository of forbidden knowledge/)).toBeInTheDocument();
    });
  });

  describe('Data validation and consistency checks', () => {
    it('should handle missing zone and sub_zone gracefully', () => {
      const roomWithoutLocation = {
        ...mockRoom,
        zone: undefined,
        sub_zone: undefined,
      };

      render(<RoomInfoPanel room={roomWithoutLocation} debugInfo={mockDebugInfo} />);

      expect(screen.getByText('Zone:')).toBeInTheDocument();
      expect(screen.getAllByText('Unknown')).toHaveLength(2);
      expect(screen.getByText('Subzone:')).toBeInTheDocument();
    });

    it('should handle missing description gracefully', () => {
      const roomWithoutDescription = {
        ...mockRoom,
        description: '',
      };

      render(<RoomInfoPanel room={roomWithoutDescription} debugInfo={mockDebugInfo} />);

      expect(screen.getByText('No description available')).toBeInTheDocument();
    });

    it('should handle missing exits gracefully', () => {
      const roomWithoutExits = {
        ...mockRoom,
        exits: undefined,
      };

      render(<RoomInfoPanel room={roomWithoutExits} debugInfo={mockDebugInfo} />);

      expect(screen.getByText('Exits:')).toBeInTheDocument();
      expect(screen.getByText('None')).toBeInTheDocument();
    });

    it('should handle empty exits object gracefully', () => {
      const roomWithEmptyExits = {
        ...mockRoom,
        exits: {},
      };

      render(<RoomInfoPanel room={roomWithEmptyExits} debugInfo={mockDebugInfo} />);

      expect(screen.getByText('Exits:')).toBeInTheDocument();
      expect(screen.getByText('None')).toBeInTheDocument();
    });

    it('should handle null exits gracefully', () => {
      const roomWithNullExits = {
        ...mockRoom,
        exits: {
          north: null,
          south: null,
          east: null,
          west: null,
        },
      };

      render(<RoomInfoPanel room={roomWithNullExits} debugInfo={mockDebugInfo} />);

      expect(screen.getByText('Exits:')).toBeInTheDocument();
      expect(screen.getByText('None')).toBeInTheDocument();
    });
  });

  describe('Occupant count consistency validation', () => {
    it('should display occupant count when available', () => {
      render(<RoomInfoPanel room={mockRoom} debugInfo={mockDebugInfo} />);

      expect(screen.getByText('(2)')).toBeInTheDocument();
    });

    it('should handle missing occupant_count gracefully', () => {
      const roomWithoutCount = {
        ...mockRoom,
        occupant_count: undefined,
      };

      render(<RoomInfoPanel room={roomWithoutCount} debugInfo={mockDebugInfo} />);

      expect(screen.getByText('Occupants')).toBeInTheDocument();
      expect(screen.queryByText(/\(\d+\)/)).not.toBeInTheDocument();
    });

    it('should handle zero occupants correctly', () => {
      const emptyRoom = {
        ...mockRoom,
        occupants: [],
        occupant_count: 0,
      };

      render(<RoomInfoPanel room={emptyRoom} debugInfo={mockDebugInfo} />);

      expect(screen.getByText('Occupants')).toBeInTheDocument();
      expect(screen.getByText('(0)')).toBeInTheDocument();
      expect(screen.getByText('No other players present')).toBeInTheDocument();
    });

    it('should handle missing occupants array gracefully', () => {
      const roomWithoutOccupants = {
        ...mockRoom,
        occupants: undefined,
        occupant_count: 0,
      };

      render(<RoomInfoPanel room={roomWithoutOccupants} debugInfo={mockDebugInfo} />);

      expect(screen.getByText('Occupants')).toBeInTheDocument();
      expect(screen.getByText('(0)')).toBeInTheDocument();
      expect(screen.getByText('No other players present')).toBeInTheDocument();
    });

    it('should detect and handle occupant count mismatch', () => {
      const inconsistentRoom = {
        ...mockRoom,
        occupants: ['Player1', 'Player2', 'Player3'],
        occupant_count: 2, // Mismatch!
      };

      render(<RoomInfoPanel room={inconsistentRoom} debugInfo={mockDebugInfo} />);

      // Should display the corrected occupant count (validation fixes the mismatch)
      expect(screen.getByText('(3)')).toBeInTheDocument();
      // Should display all occupants from the array
      expect(screen.getByText('Player1')).toBeInTheDocument();
      expect(screen.getByText('Player2')).toBeInTheDocument();
      expect(screen.getByText('Player3')).toBeInTheDocument();
    });
  });

  describe('Text formatting and display', () => {
    it('should format location names correctly', () => {
      const roomWithUnderscoreNames = {
        ...mockRoom,
        zone: 'new_york_city',
        sub_zone: 'manhattan_downtown',
      };

      render(<RoomInfoPanel room={roomWithUnderscoreNames} debugInfo={mockDebugInfo} />);

      expect(screen.getByText('New York City')).toBeInTheDocument();
      expect(screen.getByText('Manhattan Downtown')).toBeInTheDocument();
    });

    it('should format occupant names correctly', () => {
      const roomWithLowercaseOccupants = {
        ...mockRoom,
        occupants: ['player1', 'PLAYER2', 'Player3'],
      };

      render(<RoomInfoPanel room={roomWithLowercaseOccupants} debugInfo={mockDebugInfo} />);

      expect(screen.getByText('Player1')).toBeInTheDocument();
      expect(screen.getByText('Player2')).toBeInTheDocument();
      expect(screen.getByText('Player3')).toBeInTheDocument();
    });

    it('should clean up description formatting', () => {
      const roomWithMessyDescription = {
        ...mockRoom,
        description: '  A   room    with    multiple    spaces.  ',
      };

      render(<RoomInfoPanel room={roomWithMessyDescription} debugInfo={mockDebugInfo} />);

      expect(screen.getByText('A room with multiple spaces.')).toBeInTheDocument();
    });
  });

  describe('Fallback logic and error handling', () => {
    it('should use fallback data when room is null but debug info exists', () => {
      render(<RoomInfoPanel room={null} debugInfo={mockDebugInfo} />);

      // Should show the development mock data
      expect(screen.getByText('Miskatonic University Library')).toBeInTheDocument();
      expect(screen.getByText('Zone:')).toBeInTheDocument();
      expect(screen.getByText('Arkham')).toBeInTheDocument();
    });

    it('should handle completely invalid room data gracefully', () => {
      const invalidRoom = {
        id: null,
        name: null,
        description: null,
      } as unknown as Room;

      render(<RoomInfoPanel room={invalidRoom} debugInfo={mockDebugInfo} />);

      // Should not crash and should show some fallback content
      expect(screen.getByText('Zone:')).toBeInTheDocument();
    });

    it('should handle room with only partial data', () => {
      const partialRoom = {
        id: 'partial-room',
        name: 'Partial Room',
        // Missing description, zone, sub_zone, exits, occupants
      } as unknown as Room;

      render(<RoomInfoPanel room={partialRoom} debugInfo={mockDebugInfo} />);

      expect(screen.getByText('Partial Room')).toBeInTheDocument();
      expect(screen.getByText('Zone:')).toBeInTheDocument();
      expect(screen.getAllByText('Unknown')).toHaveLength(2);
      expect(screen.getByText('No description available')).toBeInTheDocument();
      expect(screen.getByText('Exits:')).toBeInTheDocument();
      expect(screen.getByText('None')).toBeInTheDocument();
      expect(screen.getByText('No other players present')).toBeInTheDocument();
    });
  });

  describe('Debug logging and development features', () => {
    it('should log debug information in development mode', () => {
      render(<RoomInfoPanel room={mockRoom} debugInfo={mockDebugInfo} />);

      // Verify that console.log was called for debug information
      expect(mockConsoleLog).toHaveBeenCalledWith('🔍 RoomInfoPanel render called with room:', mockRoom);
      expect(mockConsoleLog).toHaveBeenCalledWith('🔍 RoomInfoPanel room type:', 'object');
    });

    it('should log room data details for debugging', () => {
      render(<RoomInfoPanel room={mockRoom} debugInfo={mockDebugInfo} />);

      expect(mockConsoleLog).toHaveBeenCalledWith(
        '🔍 RoomInfoPanel: Rendering room data:',
        expect.objectContaining({
          name: 'Test Room',
          description: 'A test room for testing purposes.',
          zone: 'arkham',
          sub_zone: 'university',
        })
      );
    });

    it('should log occupant count debugging information', () => {
      render(<RoomInfoPanel room={mockRoom} debugInfo={mockDebugInfo} />);

      expect(mockConsoleLog).toHaveBeenCalledWith('🔍 DEBUG: occupant_count value:', 2, 'type:', 'number');
      expect(mockConsoleLog).toHaveBeenCalledWith('🔍 DEBUG: occupants array:', ['Player1', 'Player2'], 'length:', 2);
    });
  });

  describe('Edge cases and boundary conditions', () => {
    it('should handle very long room names', () => {
      const roomWithLongName = {
        ...mockRoom,
        name: 'A'.repeat(1000),
      };

      render(<RoomInfoPanel room={roomWithLongName} debugInfo={mockDebugInfo} />);

      expect(screen.getByText('A'.repeat(1000))).toBeInTheDocument();
    });

    it('should handle very long descriptions', () => {
      const roomWithLongDescription = {
        ...mockRoom,
        description: 'A'.repeat(5000),
      };

      render(<RoomInfoPanel room={roomWithLongDescription} debugInfo={mockDebugInfo} />);

      expect(screen.getByText('A'.repeat(5000))).toBeInTheDocument();
    });

    it('should handle many occupants', () => {
      const roomWithManyOccupants = {
        ...mockRoom,
        occupants: Array.from({ length: 100 }, (_, i) => `Player${i + 1}`),
        occupant_count: 100,
      };

      render(<RoomInfoPanel room={roomWithManyOccupants} debugInfo={mockDebugInfo} />);

      expect(screen.getByText('(100)')).toBeInTheDocument();
      expect(screen.getByText('Player1')).toBeInTheDocument();
      expect(screen.getByText('Player100')).toBeInTheDocument();
    });

    it('should handle special characters in room data', () => {
      const roomWithSpecialChars = {
        ...mockRoom,
        name: 'Room with "quotes" & <html> tags',
        description: 'Description with \n newlines and \t tabs',
        zone: 'zone-with-dashes_and_underscores',
      };

      render(<RoomInfoPanel room={roomWithSpecialChars} debugInfo={mockDebugInfo} />);

      expect(screen.getByText('Room with "quotes" & <html> tags')).toBeInTheDocument();
      expect(screen.getByText('Description with newlines and tabs')).toBeInTheDocument();
      expect(screen.getByText('Zone-with-dashes And Underscores')).toBeInTheDocument();
    });
  });
});
