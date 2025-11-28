/**
 * Tests for MapView component.
 *
 * Verifies integration with RoomMapViewer, ESC key handling,
 * and proper display of map content.
 */

import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import { describe, it, expect, vi, beforeEach } from 'vitest';
import { MapView } from '../../MapView';

// Mock RoomMapViewer
vi.mock('../RoomMapViewer', () => ({
  RoomMapViewer: ({ plane, zone, currentRoomId }: { plane: string; zone: string; currentRoomId?: string }) => (
    <div data-testid="room-map-viewer">
      <div>Plane: {plane}</div>
      <div>Zone: {zone}</div>
      {currentRoomId && <div>Current Room: {currentRoomId}</div>}
    </div>
  ),
}));

describe('MapView', () => {
  const mockRoom = {
    id: 'earth_arkhamcity_northside_room_test',
    name: 'Test Room',
    description: 'A test room',
    plane: 'earth',
    zone: 'arkhamcity',
    sub_zone: 'northside',
    exits: {},
  };

  const defaultProps = {
    isOpen: true,
    onClose: vi.fn(),
    currentRoom: mockRoom,
    authToken: 'test-token',
  };

  beforeEach(() => {
    vi.clearAllMocks();
  });

  it('should render when isOpen is true', () => {
    render(<MapView {...defaultProps} />);
    expect(screen.getByText('Map')).toBeInTheDocument();
    expect(screen.getByTestId('room-map-viewer')).toBeInTheDocument();
  });

  it('should not render when isOpen is false', () => {
    render(<MapView {...defaultProps} isOpen={false} />);
    expect(screen.queryByText('Map')).not.toBeInTheDocument();
  });

  it('should call onClose when close button is clicked', () => {
    render(<MapView {...defaultProps} />);
    const closeButton = screen.getByLabelText('Close map');
    fireEvent.click(closeButton);
    expect(defaultProps.onClose).toHaveBeenCalledTimes(1);
  });

  it('should call onClose when ESC key is pressed', async () => {
    render(<MapView {...defaultProps} />);
    fireEvent.keyDown(window, { key: 'Escape' });
    await waitFor(() => {
      expect(defaultProps.onClose).toHaveBeenCalledTimes(1);
    });
  });

  it('should pass correct props to RoomMapViewer', () => {
    render(<MapView {...defaultProps} />);
    expect(screen.getByText('Plane: earth')).toBeInTheDocument();
    expect(screen.getByText('Zone: arkhamcity')).toBeInTheDocument();
    expect(screen.getByText('Current Room: earth_arkhamcity_northside_room_test')).toBeInTheDocument();
  });

  it('should show error message when room data is missing (not render RoomMapViewer)', () => {
    render(<MapView {...defaultProps} currentRoom={null} />);
    // When room is null, MapView shows error message instead of RoomMapViewer
    expect(screen.queryByTestId('room-map-viewer')).not.toBeInTheDocument();
    expect(screen.getByText(/Unable to load map: No room data available/)).toBeInTheDocument();
    expect(screen.getByText(/You must be in a room to view the map/)).toBeInTheDocument();
  });

  it('should prevent body scroll when open', () => {
    const { rerender } = render(<MapView {...defaultProps} isOpen={true} />);
    expect(document.body.style.overflow).toBe('hidden');

    rerender(<MapView {...defaultProps} isOpen={false} />);
    expect(document.body.style.overflow).toBe('');
  });
});
