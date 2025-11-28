/**
 * Tests for RoomMapViewer component.
 *
 * Verifies that the component properly renders the map, handles data loading,
 * displays errors, and responds to user interactions.
 */

import { render, screen, waitFor } from '@testing-library/react';
import { describe, expect, it, vi, beforeEach } from 'vitest';
import { RoomMapViewer } from '../RoomMapViewer';
import { useRoomMapData } from '../hooks/useRoomMapData';
import { useMapLayout } from '../hooks/useMapLayout';
import { roomsToNodes, createEdgesFromRooms } from '../utils/mapUtils';
import type { Room } from '../../../stores/gameStore';

// Mock the hooks
vi.mock('../hooks/useRoomMapData');
vi.mock('../hooks/useMapLayout');
vi.mock('../utils/mapUtils');

// Mock React Flow
vi.mock('reactflow', () => ({
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  default: ({ children, nodes, edges, onNodeClick }: any) => {
    const handleClick = () => {
      if (onNodeClick) {
        const mockNode = nodes?.[0] || { data: { id: 'test-room', name: 'Test Room' } };
        // eslint-disable-next-line @typescript-eslint/no-explicit-any
        onNodeClick({ target: {} } as any, mockNode as any);
      }
    };

    return (
      <div data-testid="react-flow">
        {children}
        <div data-testid="nodes">{nodes?.length || 0} nodes</div>
        <div data-testid="edges">{edges?.length || 0} edges</div>
        {onNodeClick && <button onClick={handleClick}>Click Node</button>}
      </div>
    );
  },
  Controls: () => <div data-testid="controls">Controls</div>,
  Background: () => <div data-testid="background">Background</div>,
  MiniMap: () => <div data-testid="minimap">MiniMap</div>,
}));

// Mock MapControls and RoomDetailsPanel
vi.mock('../MapControls', () => ({
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  MapControls: ({ searchQuery, onSearchChange }: any) => (
    <div data-testid="map-controls">
      <input data-testid="search-input" value={searchQuery} onChange={e => onSearchChange(e.target.value)} />
    </div>
  ),
}));

vi.mock('../RoomDetailsPanel', () => ({
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  RoomDetailsPanel: ({ room, onClose }: any) => (
    <div data-testid="room-details-panel">
      <div>{room.name}</div>
      <button onClick={onClose}>Close</button>
    </div>
  ),
}));

describe('RoomMapViewer', () => {
  const mockRooms: Room[] = [
    {
      id: 'earth_arkhamcity_campus_room_001',
      name: 'Test Room 1',
      description: 'A test room',
      plane: 'earth',
      zone: 'arkhamcity',
      sub_zone: 'campus',
      exits: { north: 'earth_arkhamcity_campus_room_002' },
    },
    {
      id: 'earth_arkhamcity_campus_room_002',
      name: 'Test Room 2',
      description: 'Another test room',
      plane: 'earth',
      zone: 'arkhamcity',
      sub_zone: 'campus',
      exits: {},
    },
  ];

  beforeEach(() => {
    vi.clearAllMocks();

    // Default mock implementations
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    (useRoomMapData as any).mockReturnValue({
      rooms: mockRooms,
      isLoading: false,
      error: null,
      refetch: vi.fn(),
      total: 2,
    });

    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    (useMapLayout as any).mockReturnValue({
      layoutNodes: [],
      hasUnsavedChanges: false,
      updateNodePosition: vi.fn(),
      savePositions: vi.fn(),
      resetToAutoLayout: vi.fn(),
      applyGridLayout: vi.fn(),
    });

    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    (roomsToNodes as any).mockReturnValue([]);
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    (createEdgesFromRooms as any).mockReturnValue([]);
  });

  it('should render loading state', () => {
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    (useRoomMapData as any).mockReturnValue({
      rooms: [],
      isLoading: true,
      error: null,
      refetch: vi.fn(),
      total: 0,
    });

    render(<RoomMapViewer plane="earth" zone="arkhamcity" />);

    expect(screen.getByText(/loading/i)).toBeInTheDocument();
  });

  it('should render error state', () => {
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    (useRoomMapData as any).mockReturnValue({
      rooms: [],
      isLoading: false,
      error: 'Failed to fetch rooms',
      refetch: vi.fn(),
      total: 0,
    });

    render(<RoomMapViewer plane="earth" zone="arkhamcity" />);

    expect(screen.getByText(/failed to fetch rooms/i)).toBeInTheDocument();
  });

  it('should render map with nodes and edges', () => {
    const mockNodes = [{ id: 'node1', type: 'room', position: { x: 0, y: 0 }, data: { id: 'room1', name: 'Room 1' } }];
    const mockEdges = [{ id: 'edge1', source: 'node1', target: 'node2', data: { direction: 'north' } }];

    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    (roomsToNodes as any).mockReturnValue(mockNodes);
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    (createEdgesFromRooms as any).mockReturnValue(mockEdges);
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    (useMapLayout as any).mockReturnValue({
      layoutNodes: mockNodes,
      hasUnsavedChanges: false,
      updateNodePosition: vi.fn(),
      savePositions: vi.fn(),
      resetToAutoLayout: vi.fn(),
      applyGridLayout: vi.fn(),
    });

    render(<RoomMapViewer plane="earth" zone="arkhamcity" />);

    expect(screen.getByTestId('react-flow')).toBeInTheDocument();
    expect(screen.getByTestId('nodes')).toHaveTextContent('1 nodes');
    expect(screen.getByTestId('edges')).toHaveTextContent('1 edges');
  });

  it('should render controls and minimap', () => {
    render(<RoomMapViewer plane="earth" zone="arkhamcity" />);

    expect(screen.getByTestId('controls')).toBeInTheDocument();
    expect(screen.getByTestId('minimap')).toBeInTheDocument();
    expect(screen.getByTestId('background')).toBeInTheDocument();
  });

  it('should handle node clicks', async () => {
    const mockNodes = [
      {
        id: 'node1',
        type: 'room',
        position: { x: 0, y: 0 },
        data: { id: 'earth_arkhamcity_campus_room_001', name: 'Test Room 1' },
      },
    ];

    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    (roomsToNodes as any).mockReturnValue(mockNodes);
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    (useMapLayout as any).mockReturnValue({
      layoutNodes: mockNodes,
      hasUnsavedChanges: false,
      updateNodePosition: vi.fn(),
      savePositions: vi.fn(),
      resetToAutoLayout: vi.fn(),
      applyGridLayout: vi.fn(),
    });

    render(<RoomMapViewer plane="earth" zone="arkhamcity" />);

    const clickButton = screen.getByText('Click Node');
    clickButton.click();

    // Should show room details panel
    await waitFor(() => {
      expect(screen.getByTestId('room-details-panel')).toBeInTheDocument();
      expect(screen.getByText('Test Room 1')).toBeInTheDocument();
    });
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
});
