/**
 * Tests for RoomDetailsPanel component.
 */

import { fireEvent, render, screen } from '@testing-library/react';
import { describe, expect, it, vi } from 'vitest';
import type { Room } from '../../../stores/gameStore';
import { RoomDetailsPanel } from '../RoomDetailsPanel';

describe('RoomDetailsPanel', () => {
  const mockRoom: Room = {
    id: 'earth_arkhamcity_campus_room_001',
    name: 'Test Room',
    description: 'A test room description',
    plane: 'earth',
    zone: 'arkhamcity',
    sub_zone: 'campus',
    environment: 'indoor',
    exits: {
      north: 'earth_arkhamcity_campus_room_002',
      south: 'earth_arkhamcity_campus_room_003',
    },
    occupants: ['player1', 'player2'],
    occupant_count: 2,
  };

  it('should render room details', () => {
    const onClose = vi.fn();
    render(<RoomDetailsPanel room={mockRoom} onClose={onClose} />);

    expect(screen.getByText('Test Room')).toBeInTheDocument();
    expect(screen.getByText('earth_arkhamcity_campus_room_001')).toBeInTheDocument();
    expect(screen.getByText('A test room description')).toBeInTheDocument();
    expect(screen.getByText('earth')).toBeInTheDocument();
    expect(screen.getByText('arkhamcity')).toBeInTheDocument();
    expect(screen.getByText('campus')).toBeInTheDocument();
    expect(screen.getByText('indoor')).toBeInTheDocument();
  });

  it('should call onClose when close button is clicked', () => {
    const onClose = vi.fn();
    render(<RoomDetailsPanel room={mockRoom} onClose={onClose} />);

    const closeButton = screen.getByLabelText('Close panel');
    fireEvent.click(closeButton);

    expect(onClose).toHaveBeenCalledTimes(1);
  });

  it('should render admin buttons when isAdmin is true', () => {
    const onClose = vi.fn();
    const onEditRoom = vi.fn();
    const onCreateExit = vi.fn();

    render(
      <RoomDetailsPanel
        room={mockRoom}
        onClose={onClose}
        isAdmin={true}
        onEditRoom={onEditRoom}
        onCreateExit={onCreateExit}
      />
    );

    expect(screen.getByText('Edit Room')).toBeInTheDocument();
    expect(screen.getByText('Create Exit')).toBeInTheDocument();
  });

  it('should not render admin buttons when isAdmin is false', () => {
    const onClose = vi.fn();
    render(<RoomDetailsPanel room={mockRoom} onClose={onClose} isAdmin={false} />);

    expect(screen.queryByText('Edit Room')).not.toBeInTheDocument();
    expect(screen.queryByText('Create Exit')).not.toBeInTheDocument();
  });

  it('should call onEditRoom when edit button is clicked', () => {
    const onClose = vi.fn();
    const onEditRoom = vi.fn();

    render(<RoomDetailsPanel room={mockRoom} onClose={onClose} isAdmin={true} onEditRoom={onEditRoom} />);

    const editButton = screen.getByText('Edit Room');
    fireEvent.click(editButton);

    expect(onEditRoom).toHaveBeenCalledWith('earth_arkhamcity_campus_room_001');
  });

  it('should call onCreateExit when create exit button is clicked', () => {
    const onClose = vi.fn();
    const onCreateExit = vi.fn();

    render(<RoomDetailsPanel room={mockRoom} onClose={onClose} isAdmin={true} onCreateExit={onCreateExit} />);

    const createExitButton = screen.getByText('Create Exit');
    fireEvent.click(createExitButton);

    expect(onCreateExit).toHaveBeenCalledTimes(1);
  });

  it('should not render edit button when onEditRoom is not provided', () => {
    const onClose = vi.fn();
    const onCreateExit = vi.fn();

    render(<RoomDetailsPanel room={mockRoom} onClose={onClose} isAdmin={true} onCreateExit={onCreateExit} />);

    expect(screen.queryByText('Edit Room')).not.toBeInTheDocument();
    expect(screen.getByText('Create Exit')).toBeInTheDocument();
  });

  it('should not render create exit button when onCreateExit is not provided', () => {
    const onClose = vi.fn();
    const onEditRoom = vi.fn();

    render(<RoomDetailsPanel room={mockRoom} onClose={onClose} isAdmin={true} onEditRoom={onEditRoom} />);

    expect(screen.getByText('Edit Room')).toBeInTheDocument();
    expect(screen.queryByText('Create Exit')).not.toBeInTheDocument();
  });

  it('should handle room without description', () => {
    const roomWithoutDescription: Omit<Room, 'description'> & { description?: string } = {
      ...mockRoom,
      description: undefined,
    };
    const onClose = vi.fn();

    render(<RoomDetailsPanel room={roomWithoutDescription as Room} onClose={onClose} />);

    expect(screen.queryByText('Description:')).not.toBeInTheDocument();
  });

  it('should handle room without optional location fields', () => {
    const minimalRoom: Room = {
      id: 'room_001',
      name: 'Minimal Room',
      description: '',
      exits: {},
    };
    const onClose = vi.fn();

    render(<RoomDetailsPanel room={minimalRoom} onClose={onClose} />);

    expect(screen.getByText('Minimal Room')).toBeInTheDocument();
    expect(screen.queryByText('Plane:')).not.toBeInTheDocument();
    expect(screen.queryByText('Zone:')).not.toBeInTheDocument();
    expect(screen.queryByText('Sub-zone:')).not.toBeInTheDocument();
    expect(screen.queryByText('Environment:')).not.toBeInTheDocument();
  });

  it('should render occupants when present', () => {
    const onClose = vi.fn();
    render(<RoomDetailsPanel room={mockRoom} onClose={onClose} />);

    expect(screen.getByText(/Occupants \(2\):/)).toBeInTheDocument();
    expect(screen.getByText('player1, player2')).toBeInTheDocument();
  });

  it('should handle occupants with occupant_count', () => {
    const roomWithCount: Room = {
      ...mockRoom,
      occupants: ['player1'],
      occupant_count: 5,
    };
    const onClose = vi.fn();

    render(<RoomDetailsPanel room={roomWithCount} onClose={onClose} />);

    expect(screen.getByText(/Occupants \(5\):/)).toBeInTheDocument();
  });

  it('should not render occupants section when empty', () => {
    const roomWithoutOccupants: Room = {
      ...mockRoom,
      occupants: [],
    };
    const onClose = vi.fn();

    render(<RoomDetailsPanel room={roomWithoutOccupants} onClose={onClose} />);

    expect(screen.queryByText(/Occupants/)).not.toBeInTheDocument();
  });

  it('should render exits when present', () => {
    const onClose = vi.fn();
    render(<RoomDetailsPanel room={mockRoom} onClose={onClose} />);

    expect(screen.getByText('Exits:')).toBeInTheDocument();
    expect(screen.getByText('north:')).toBeInTheDocument();
    expect(screen.getByText('earth_arkhamcity_campus_room_002')).toBeInTheDocument();
    expect(screen.getByText('south:')).toBeInTheDocument();
    expect(screen.getByText('earth_arkhamcity_campus_room_003')).toBeInTheDocument();
  });

  it('should not render exits section when empty', () => {
    const roomWithoutExits: Room = {
      ...mockRoom,
      exits: {},
    };
    const onClose = vi.fn();

    render(<RoomDetailsPanel room={roomWithoutExits} onClose={onClose} />);

    expect(screen.queryByText('Exits:')).not.toBeInTheDocument();
  });

  it('should handle room with only plane', () => {
    const roomWithPlaneOnly: Room = {
      id: 'room_001',
      name: 'Room',
      description: '',
      plane: 'earth',
      exits: {},
    };
    const onClose = vi.fn();

    render(<RoomDetailsPanel room={roomWithPlaneOnly} onClose={onClose} />);

    expect(screen.getByText('Plane:')).toBeInTheDocument();
    expect(screen.getByText('earth')).toBeInTheDocument();
    expect(screen.queryByText('Zone:')).not.toBeInTheDocument();
  });

  it('should handle room with only zone', () => {
    const roomWithZoneOnly: Room = {
      id: 'room_001',
      name: 'Room',
      description: '',
      zone: 'arkhamcity',
      exits: {},
    };
    const onClose = vi.fn();

    render(<RoomDetailsPanel room={roomWithZoneOnly} onClose={onClose} />);

    expect(screen.getByText('Zone:')).toBeInTheDocument();
    expect(screen.getByText('arkhamcity')).toBeInTheDocument();
  });

  it('should handle room with only sub_zone', () => {
    const roomWithSubZoneOnly: Room = {
      id: 'room_001',
      name: 'Room',
      description: '',
      sub_zone: 'campus',
      exits: {},
    };
    const onClose = vi.fn();

    render(<RoomDetailsPanel room={roomWithSubZoneOnly} onClose={onClose} />);

    expect(screen.getByText('Sub-zone:')).toBeInTheDocument();
    expect(screen.getByText('campus')).toBeInTheDocument();
  });

  it('should handle room with only environment', () => {
    const roomWithEnvironmentOnly: Room = {
      id: 'room_001',
      name: 'Room',
      description: '',
      environment: 'outdoor',
      exits: {},
    };
    const onClose = vi.fn();

    render(<RoomDetailsPanel room={roomWithEnvironmentOnly} onClose={onClose} />);

    expect(screen.getByText('Environment:')).toBeInTheDocument();
    expect(screen.getByText('outdoor')).toBeInTheDocument();
  });

  it('should handle occupants with null/undefined occupant_count', () => {
    const roomWithOccupantsOnly: Room = {
      ...mockRoom,
      occupants: ['player1', 'player2'],
      occupant_count: undefined,
    };
    const onClose = vi.fn();

    render(<RoomDetailsPanel room={roomWithOccupantsOnly} onClose={onClose} />);

    // Should use occupants.length when occupant_count is undefined (line 119 branch)
    expect(screen.getByText(/Occupants \(2\):/)).toBeInTheDocument();
  });

  it('should handle occupants with empty array', () => {
    const roomWithEmptyOccupants: Room = {
      ...mockRoom,
      occupants: [],
      occupant_count: 0,
    };
    const onClose = vi.fn();

    render(<RoomDetailsPanel room={roomWithEmptyOccupants} onClose={onClose} />);

    // Should not render occupants section when array is empty (line 116 branch)
    expect(screen.queryByText(/Occupants/)).not.toBeInTheDocument();
  });

  it('should handle occupants with null occupants array', () => {
    const roomWithNullOccupants: Room = {
      ...mockRoom,
      occupants: null as unknown as string[],
    };
    const onClose = vi.fn();

    render(<RoomDetailsPanel room={roomWithNullOccupants} onClose={onClose} />);

    // Should not render occupants section when occupants is null (line 116 branch)
    expect(screen.queryByText(/Occupants/)).not.toBeInTheDocument();
  });

  it('should handle exits with empty object', () => {
    const roomWithEmptyExits: Room = {
      ...mockRoom,
      exits: {},
    };
    const onClose = vi.fn();

    render(<RoomDetailsPanel room={roomWithEmptyExits} onClose={onClose} />);

    // Should not render exits section when exits object is empty (line 126 branch)
    expect(screen.queryByText('Exits:')).not.toBeInTheDocument();
  });

  it('should handle exits with null exits', () => {
    const roomWithNullExits: Room = {
      ...mockRoom,
      exits: null as unknown as Record<string, string>,
    };
    const onClose = vi.fn();

    render(<RoomDetailsPanel room={roomWithNullExits} onClose={onClose} />);

    // Should not render exits section when exits is null (line 126 branch)
    expect(screen.queryByText('Exits:')).not.toBeInTheDocument();
  });

  it('should handle admin buttons when isAdmin is true but callbacks not provided', () => {
    const onClose = vi.fn();

    render(<RoomDetailsPanel room={mockRoom} onClose={onClose} isAdmin={true} />);

    // Should not render admin buttons when callbacks are not provided (lines 54, 62 branches)
    expect(screen.queryByText('Edit Room')).not.toBeInTheDocument();
    expect(screen.queryByText('Create Exit')).not.toBeInTheDocument();
  });

  it('should handle room with all optional fields missing', () => {
    const minimalRoom: Room = {
      id: 'room_001',
      name: 'Minimal Room',
      description: '',
      exits: {},
    };
    const onClose = vi.fn();

    render(<RoomDetailsPanel room={minimalRoom} onClose={onClose} />);

    // Should only show name and ID
    expect(screen.getByText('Minimal Room')).toBeInTheDocument();
    expect(screen.getByText('room_001')).toBeInTheDocument();
    // Should not show any optional sections
    expect(screen.queryByText('Description:')).not.toBeInTheDocument();
    expect(screen.queryByText('Plane:')).not.toBeInTheDocument();
    expect(screen.queryByText('Zone:')).not.toBeInTheDocument();
    expect(screen.queryByText('Sub-zone:')).not.toBeInTheDocument();
    expect(screen.queryByText('Environment:')).not.toBeInTheDocument();
    expect(screen.queryByText(/Occupants/)).not.toBeInTheDocument();
    expect(screen.queryByText('Exits:')).not.toBeInTheDocument();
  });

  it('should handle occupants with occupant_count 0', () => {
    const roomWithZeroCount: Room = {
      ...mockRoom,
      occupants: ['player1'],
      occupant_count: 0,
    };
    const onClose = vi.fn();

    render(<RoomDetailsPanel room={roomWithZeroCount} onClose={onClose} />);

    // Should use occupants.length when occupant_count is 0 (line 119: 0 || length)
    expect(screen.getByText(/Occupants \(1\):/)).toBeInTheDocument();
  });
});
