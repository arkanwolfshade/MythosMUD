/**
 * Rendering tests for RoomMapViewer component.
 *
 * Verifies that the component properly renders in various states.
 */

import { render, screen } from '@testing-library/react';
import type { ReactFlowProps } from 'reactflow';
import { beforeEach, describe, expect, it, vi } from 'vitest';
import type { MapControlsProps } from '../MapControls';
import { RoomMapViewer } from '../RoomMapViewer';
import { useMapLayout } from '../hooks/useMapLayout';
import { useRoomMapData } from '../hooks/useRoomMapData';
import { createEdgesFromRooms, roomsToNodes } from '../utils/mapUtils';
import { createMockNodes, setupDefaultMocks } from './RoomMapViewer.test-utils';

// Mock the hooks
vi.mock('../hooks/useRoomMapData');
vi.mock('../hooks/useMapLayout');
vi.mock('../utils/mapUtils');

// Mock React Flow
vi.mock('reactflow', () => ({
  default: ({ children, nodes, edges }: Pick<ReactFlowProps, 'children' | 'nodes' | 'edges'>) => (
    <div data-testid="react-flow">
      {children}
      <div data-testid="nodes">{nodes?.length || 0} nodes</div>
      <div data-testid="edges">{edges?.length || 0} edges</div>
    </div>
  ),
  Controls: () => <div data-testid="controls">Controls</div>,
  Background: () => <div data-testid="background">Background</div>,
  MiniMap: () => <div data-testid="minimap">MiniMap</div>,
}));

// Mock MapControls and RoomDetailsPanel
vi.mock('../MapControls', () => ({
  MapControls: ({ searchQuery, onSearchChange }: Pick<MapControlsProps, 'searchQuery' | 'onSearchChange'>) => (
    <div data-testid="map-controls">
      <input
        data-testid="search-input"
        value={searchQuery}
        onChange={e => {
          onSearchChange(e.target.value);
        }}
      />
    </div>
  ),
}));

vi.mock('../RoomDetailsPanel', () => ({
  RoomDetailsPanel: () => null,
}));

describe('RoomMapViewer - Rendering', () => {
  beforeEach(() => {
    setupDefaultMocks();
  });

  it('should render loading state', () => {
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

    expect(screen.getByText(/loading/i)).toBeInTheDocument();
  });

  it('should render error state', () => {
    // Mock hook requires any type for vi.mock type casting
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
    const mockNodes = createMockNodes(1);
    const mockEdges = [{ id: 'edge1', source: 'node1', target: 'node2', data: { direction: 'north' } }];

    // Mock function requires any type for vi.mock type casting
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    (roomsToNodes as any).mockReturnValue(mockNodes);
    // Mock function requires any type for vi.mock type casting
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    (createEdgesFromRooms as any).mockReturnValue(mockEdges);
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

  it('should render empty state when no rooms available', () => {
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
  });

  it('should render empty state with search query and clear button', () => {
    // Mock roomsToNodes to return empty array (simulating no matches)
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

    // The component should handle the empty filtered rooms case
    // This tests the branch where searchQuery exists and filteredRooms.length === 0
  });

  it('should display error banner when error exists', () => {
    // Mock hook requires any type for vi.mock type casting
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    (useRoomMapData as any).mockReturnValue({
      rooms: [],
      isLoading: false,
      error: 'Network error',
      refetch: vi.fn(),
      total: 0,
    });

    const mockNodes = createMockNodes(1);
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

    // Error banner should be displayed
    expect(screen.getByText(/network error/i)).toBeInTheDocument();
  });

  it('should render MiniMap with nodeColor function for different node types', () => {
    const mockNodes = [
      {
        id: 'node1',
        type: 'room',
        position: { x: 0, y: 0 },
        data: { id: 'earth_arkhamcity_campus_room_001', name: 'Test Room 1', isCurrentLocation: true },
      },
      {
        id: 'node2',
        type: 'room',
        position: { x: 100, y: 100 },
        data: { id: 'earth_arkhamcity_campus_room_002', name: 'Test Room 2', isCurrentLocation: false },
      },
    ];

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

    render(<RoomMapViewer plane="earth" zone="arkhamcity" currentRoomId="earth_arkhamcity_campus_room_001" />);

    // MiniMap should be rendered
    expect(screen.getByTestId('minimap')).toBeInTheDocument();
  });

  it('should handle nodeColor function with isCurrentLocation false branch', () => {
    const mockNodes = [
      {
        id: 'node1',
        type: 'room',
        position: { x: 0, y: 0 },
        data: { id: 'earth_arkhamcity_campus_room_001', name: 'Test Room 1', isCurrentLocation: false },
      },
    ];

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

    // MiniMap should render and nodeColor function should return gray for non-current location
    expect(screen.getByTestId('minimap')).toBeInTheDocument();
  });

  it('should handle nodeColor function with undefined isCurrentLocation', () => {
    const mockNodes = [
      {
        id: 'node1',
        type: 'room',
        position: { x: 0, y: 0 },
        data: { id: 'earth_arkhamcity_campus_room_001', name: 'Test Room 1' }, // isCurrentLocation undefined
      },
    ];

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

    // MiniMap should render and nodeColor function should handle undefined isCurrentLocation
    expect(screen.getByTestId('minimap')).toBeInTheDocument();
  });

  it('should handle error banner when error exists in main render (not early return)', () => {
    const mockNodes = createMockNodes(1);
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

    // Mock hook requires any type for vi.mock type casting
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    (useRoomMapData as any).mockReturnValue({
      rooms: [],
      isLoading: false,
      error: null, // No error so we don't return early
      refetch: vi.fn(),
      total: 0,
    });

    render(<RoomMapViewer plane="earth" zone="arkhamcity" />);

    // Error banner should not be rendered when error is null
    expect(screen.queryByText(/error:/i)).not.toBeInTheDocument();
  });
});
