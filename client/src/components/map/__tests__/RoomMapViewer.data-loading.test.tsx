/**
 * Data loading and error handling tests for RoomMapViewer component.
 */

import { render, screen } from '@testing-library/react';
import { beforeEach, describe, expect, it, vi } from 'vitest';
import { RoomMapViewer } from '../RoomMapViewer';
import { useMapLayout } from '../hooks/useMapLayout';
import { useRoomMapData } from '../hooks/useRoomMapData';
import { roomsToNodes } from '../utils/mapUtils';
import { setupDefaultMocks } from './RoomMapViewer.test-utils';

// Mock the hooks
vi.mock('../hooks/useRoomMapData');
vi.mock('../hooks/useMapLayout');
vi.mock('../utils/mapUtils');

// Mock React Flow
vi.mock('reactflow', () => ({
  default: () => <div data-testid="react-flow" />,
  Controls: () => <div data-testid="controls">Controls</div>,
  Background: () => <div data-testid="background">Background</div>,
  MiniMap: () => <div data-testid="minimap">MiniMap</div>,
}));

// Mock MapControls and RoomDetailsPanel
vi.mock('../MapControls', () => ({
  MapControls: () => <div data-testid="map-controls" />,
}));

vi.mock('../RoomDetailsPanel', () => ({
  RoomDetailsPanel: () => null,
}));

describe('RoomMapViewer - Data Loading', () => {
  beforeEach(() => {
    setupDefaultMocks();
  });

  it('should pass plane and zone to useRoomMapData', () => {
    render(<RoomMapViewer plane="earth" zone="arkhamcity" subZone="campus" />);

    expect(useRoomMapData).toHaveBeenCalledWith(
      expect.objectContaining({
        plane: 'earth',
        zone: 'arkhamcity',
        subZone: 'campus',
      })
    );
  });

  it('should handle filterExplored when authToken is provided', () => {
    render(<RoomMapViewer plane="earth" zone="arkhamcity" authToken="test-token" />);

    expect(useRoomMapData).toHaveBeenCalledWith(
      expect.objectContaining({
        filterExplored: true,
        authToken: 'test-token',
      })
    );
  });

  it('should handle filterExplored when authToken is not provided', () => {
    render(<RoomMapViewer plane="earth" zone="arkhamcity" />);

    expect(useRoomMapData).toHaveBeenCalledWith(
      expect.objectContaining({
        filterExplored: false,
        authToken: undefined,
      })
    );
  });

  it('should handle currentRoomId for highlighting', () => {
    const mockNodes = [
      {
        id: 'node1',
        type: 'room',
        position: { x: 0, y: 0 },
        data: { id: 'earth_arkhamcity_campus_room_001', name: 'Test Room 1', isCurrentLocation: true },
      },
    ];

    // Mock function requires any type for vi.mock type casting
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    (roomsToNodes as any).mockReturnValue(mockNodes);
    // Mock hook requires any type for vi.mock type casting
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    (useMapLayout as any).mockReturnValue({
      layoutNodes: mockNodes,
      hasUnsavedChanges: false,
      updateNodePosition: vi.fn(),
      savePositions: vi.fn(),
      resetToAutoLayout: vi.fn(),
      applyGridLayout: vi.fn(),
    });

    render(<RoomMapViewer plane="earth" zone="arkhamcity" currentRoomId="earth_arkhamcity_campus_room_001" />);

    expect(roomsToNodes).toHaveBeenCalledWith(
      expect.arrayContaining([expect.objectContaining({ id: 'earth_arkhamcity_campus_room_001' })]),
      'earth_arkhamcity_campus_room_001'
    );
  });

  it('should handle retry on error', () => {
    const refetch = vi.fn();
    // Mock hook requires any type for vi.mock type casting
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    (useRoomMapData as any).mockReturnValue({
      rooms: [],
      isLoading: false,
      error: 'Failed to fetch rooms',
      refetch,
      total: 0,
    });

    render(<RoomMapViewer plane="earth" zone="arkhamcity" />);

    const retryButton = screen.getByText('Retry');
    retryButton.click();

    expect(refetch).toHaveBeenCalled();
  });

  it('should handle empty rooms array', () => {
    // Mock hook requires any type for vi.mock type casting
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    (useRoomMapData as any).mockReturnValue({
      rooms: [],
      isLoading: false,
      error: null,
      refetch: vi.fn(),
      total: 0,
    });

    // Mock function requires any type for vi.mock type casting
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    (roomsToNodes as any).mockReturnValue([]);
    // Mock hook requires any type for vi.mock type casting
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    (useMapLayout as any).mockReturnValue({
      layoutNodes: [],
    });

    render(<RoomMapViewer plane="earth" zone="arkhamcity" />);

    // When rooms array is empty, component shows "No rooms available" message
    expect(screen.getByText(/No rooms available/i)).toBeInTheDocument();
  });

  it('should handle loading state', () => {
    // Mock hook requires any type for vi.mock type casting
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    (useRoomMapData as any).mockReturnValue({
      rooms: [],
      isLoading: true,
      error: null,
      refetch: vi.fn(),
      total: 0,
    });

    render(<RoomMapViewer plane="earth" zone="arkhamcity" />);

    expect(screen.getByText('Loading map...')).toBeInTheDocument();
  });

  it('should handle error state with retry button', () => {
    const refetch = vi.fn();
    // Mock hook requires any type for vi.mock type casting
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    (useRoomMapData as any).mockReturnValue({
      rooms: [],
      isLoading: false,
      error: 'Network error',
      refetch,
      total: 0,
    });

    render(<RoomMapViewer plane="earth" zone="arkhamcity" />);

    expect(screen.getByText(/Error:/)).toBeInTheDocument();
    expect(screen.getByText('Retry')).toBeInTheDocument();
  });

  it('should handle baseUrl prop', () => {
    render(<RoomMapViewer plane="earth" zone="arkhamcity" baseUrl="http://custom-url.com" />);

    expect(useRoomMapData).toHaveBeenCalledWith(
      expect.objectContaining({
        baseUrl: 'http://custom-url.com',
      })
    );
  });

  it('should handle subZone changes', () => {
    render(<RoomMapViewer plane="earth" zone="arkhamcity" subZone="campus" />);

    expect(useRoomMapData).toHaveBeenCalledWith(
      expect.objectContaining({
        subZone: 'campus',
      })
    );
  });
});
