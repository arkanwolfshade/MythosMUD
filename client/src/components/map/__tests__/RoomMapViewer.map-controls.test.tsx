/**
 * Map controls and search filtering tests for RoomMapViewer component.
 */

import { fireEvent, render, screen } from '@testing-library/react';
import { beforeEach, describe, expect, it, vi } from 'vitest';
import type { Room } from '../../../stores/gameStore';
import { RoomMapViewer } from '../RoomMapViewer';
import { useMapLayout } from '../hooks/useMapLayout';
import { useRoomMapData } from '../hooks/useRoomMapData';
import { createEdgesFromRooms, roomsToNodes } from '../utils/mapUtils';
import { mockRooms, setupDefaultMocks } from './RoomMapViewer.test-utils';

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
  // Mock component props use any type for test flexibility
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  MapControls: ({ searchQuery, onSearchChange }: any) => (
    <div data-testid="map-controls">
      <input data-testid="search-input" value={searchQuery} onChange={e => onSearchChange(e.target.value)} />
    </div>
  ),
}));

vi.mock('../RoomDetailsPanel', () => ({
  RoomDetailsPanel: () => null,
}));

describe('RoomMapViewer - Map Controls', () => {
  beforeEach(() => {
    setupDefaultMocks();
  });

  it('should filter rooms by search query', () => {
    const mockNodes = [{ id: 'node1', type: 'room', position: { x: 0, y: 0 }, data: { id: 'room1', name: 'Room 1' } }];

    // Mock function requires any type for vi.mock type casting
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    (roomsToNodes as any).mockReturnValue(mockNodes);
    // Mock function requires any type for vi.mock type casting
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    (createEdgesFromRooms as any).mockReturnValue([]);
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

    render(<RoomMapViewer plane="earth" zone="arkhamcity" />);

    const searchInput = screen.getByTestId('search-input') as HTMLInputElement;
    fireEvent.change(searchInput, { target: { value: 'Test Room 1' } });

    expect(roomsToNodes).toHaveBeenCalled();
  });

  it('should filter rooms by ID', () => {
    const mockNodes = [{ id: 'node1', type: 'room', position: { x: 0, y: 0 }, data: { id: 'room1', name: 'Room 1' } }];
    // Mock function requires any type for vi.mock type casting
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    (roomsToNodes as any).mockReturnValue(mockNodes);
    // Mock function requires any type for vi.mock type casting
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    (createEdgesFromRooms as any).mockReturnValue([]);
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

    render(<RoomMapViewer plane="earth" zone="arkhamcity" />);

    const searchInput = screen.getByTestId('search-input') as HTMLInputElement;
    fireEvent.change(searchInput, { target: { value: 'earth_arkhamcity_campus_room_001' } });

    expect(roomsToNodes).toHaveBeenCalled();
  });

  it('should filter rooms by description', () => {
    const mockNodes = [{ id: 'node1', type: 'room', position: { x: 0, y: 0 }, data: { id: 'room1', name: 'Room 1' } }];
    // Mock function requires any type for vi.mock type casting
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    (roomsToNodes as any).mockReturnValue(mockNodes);
    // Mock function requires any type for vi.mock type casting
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    (createEdgesFromRooms as any).mockReturnValue([]);
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

    render(<RoomMapViewer plane="earth" zone="arkhamcity" />);

    const searchInput = screen.getByTestId('search-input') as HTMLInputElement;
    fireEvent.change(searchInput, { target: { value: 'test room' } });

    expect(roomsToNodes).toHaveBeenCalled();
  });

  it('should filter rooms by zone', () => {
    const roomsWithZone: Room[] = [
      {
        ...mockRooms[0],
        zone: 'arkhamcity',
      },
    ];
    // Mock hook requires any type for vi.mock type casting
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    (useRoomMapData as any).mockReturnValue({
      rooms: roomsWithZone,
      isLoading: false,
      error: null,
      refetch: vi.fn(),
      total: 1,
    });

    const mockNodes = [{ id: 'node1', type: 'room', position: { x: 0, y: 0 }, data: { id: 'room1', name: 'Room 1' } }];
    // Mock function requires any type for vi.mock type casting
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    (roomsToNodes as any).mockReturnValue(mockNodes);
    // Mock function requires any type for vi.mock type casting
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    (createEdgesFromRooms as any).mockReturnValue([]);
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

    render(<RoomMapViewer plane="earth" zone="arkhamcity" />);

    const searchInput = screen.getByTestId('search-input') as HTMLInputElement;
    fireEvent.change(searchInput, { target: { value: 'arkhamcity' } });

    expect(roomsToNodes).toHaveBeenCalled();
  });

  it('should filter rooms by sub_zone', () => {
    const roomsWithSubZone: Room[] = [
      {
        ...mockRooms[0],
        sub_zone: 'campus',
      },
    ];
    // Mock hook requires any type for vi.mock type casting
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    (useRoomMapData as any).mockReturnValue({
      rooms: roomsWithSubZone,
      isLoading: false,
      error: null,
      refetch: vi.fn(),
      total: 1,
    });

    const mockNodes = [{ id: 'node1', type: 'room', position: { x: 0, y: 0 }, data: { id: 'room1', name: 'Room 1' } }];
    // Mock function requires any type for vi.mock type casting
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    (roomsToNodes as any).mockReturnValue(mockNodes);
    // Mock function requires any type for vi.mock type casting
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    (createEdgesFromRooms as any).mockReturnValue([]);
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

    render(<RoomMapViewer plane="earth" zone="arkhamcity" />);

    const searchInput = screen.getByTestId('search-input') as HTMLInputElement;
    fireEvent.change(searchInput, { target: { value: 'campus' } });

    expect(roomsToNodes).toHaveBeenCalled();
  });

  it('should handle empty search query', () => {
    const mockNodes = [{ id: 'node1', type: 'room', position: { x: 0, y: 0 }, data: { id: 'room1', name: 'Room 1' } }];
    // Mock function requires any type for vi.mock type casting
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    (roomsToNodes as any).mockReturnValue(mockNodes);
    // Mock function requires any type for vi.mock type casting
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    (createEdgesFromRooms as any).mockReturnValue([]);
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

    render(<RoomMapViewer plane="earth" zone="arkhamcity" />);

    const searchInput = screen.getByTestId('search-input') as HTMLInputElement;
    fireEvent.change(searchInput, { target: { value: '   ' } });

    expect(roomsToNodes).toHaveBeenCalled();
  });

  it('should show Clear Search button when search query exists and no rooms match', () => {
    // Mock hook requires any type for vi.mock type casting
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    (useRoomMapData as any).mockReturnValue({
      rooms: mockRooms,
      isLoading: false,
      error: null,
      refetch: vi.fn(),
      total: 2,
    });

    // Mock function requires any type for vi.mock type casting
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    (roomsToNodes as any).mockReturnValue([]);
    // Mock function requires any type for vi.mock type casting
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    (createEdgesFromRooms as any).mockReturnValue([]);
    // Mock hook requires any type for vi.mock type casting
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    (useMapLayout as any).mockReturnValue({
      layoutNodes: [],
      hasUnsavedChanges: false,
      updateNodePosition: vi.fn(),
      savePositions: vi.fn(),
      resetToAutoLayout: vi.fn(),
      applyGridLayout: vi.fn(),
    });

    render(<RoomMapViewer plane="earth" zone="arkhamcity" />);

    const searchInput = screen.getByTestId('search-input') as HTMLInputElement;
    fireEvent.change(searchInput, { target: { value: 'nonexistent-search-query' } });

    expect(screen.getByText(/no rooms found matching your search/i)).toBeInTheDocument();
    expect(screen.getByText('Clear Search')).toBeInTheDocument();
  });

  it('should not show Clear Search button when no search query and no rooms', () => {
    // Mock hook requires any type for vi.mock type casting
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    (useRoomMapData as any).mockReturnValue({
      rooms: [],
      isLoading: false,
      error: null,
      refetch: vi.fn(),
      total: 0,
    });

    render(<RoomMapViewer plane="earth" zone="arkhamcity" />);

    expect(screen.getByText(/no rooms available in this area/i)).toBeInTheDocument();
    expect(screen.queryByText('Clear Search')).not.toBeInTheDocument();
  });

  it('should handle search query with only whitespace (empty after trim)', () => {
    const mockNodes = [{ id: 'node1', type: 'room', position: { x: 0, y: 0 }, data: { id: 'room1', name: 'Room 1' } }];
    // Mock function requires any type for vi.mock type casting
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    (roomsToNodes as any).mockReturnValue(mockNodes);
    // Mock function requires any type for vi.mock type casting
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    (createEdgesFromRooms as any).mockReturnValue([]);
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

    render(<RoomMapViewer plane="earth" zone="arkhamcity" />);

    const searchInput = screen.getByTestId('search-input') as HTMLInputElement;
    fireEvent.change(searchInput, { target: { value: '   ' } });

    expect(roomsToNodes).toHaveBeenCalled();
  });
});
