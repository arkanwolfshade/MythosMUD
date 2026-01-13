/**
 * Interaction tests for RoomMapViewer component.
 *
 * Verifies user interactions like clicking nodes, closing panels, and selecting rooms.
 */

import { render, screen, waitFor } from '@testing-library/react';
import { beforeEach, describe, expect, it, vi } from 'vitest';
import { RoomMapViewer } from '../RoomMapViewer';
import { useMapLayout } from '../hooks/useMapLayout';
import { createEdgesFromRooms, roomsToNodes } from '../utils/mapUtils';
import { createMockNodes, setupDefaultMocks } from './RoomMapViewer.test-utils';

// Mock the hooks
vi.mock('../hooks/useRoomMapData');
vi.mock('../hooks/useMapLayout');
vi.mock('../utils/mapUtils');

// Mock React Flow
vi.mock('reactflow', () => ({
  // Mock component props use any type for test flexibility
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  default: ({ children, nodes, edges, onNodeClick }: any) => {
    const handleClick = () => {
      if (onNodeClick) {
        const mockNode = nodes?.[0] || { data: { id: 'test-room', name: 'Test Room' } };
        // Mock event handler requires any type for test event simulation
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
  MapControls: () => <div data-testid="map-controls" />,
}));

vi.mock('../RoomDetailsPanel', () => ({
  // Mock component props use any type for test flexibility
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  RoomDetailsPanel: ({ room, onClose }: any) => (
    <div data-testid="room-details-panel">
      <div>{room.name}</div>
      <button onClick={onClose}>Close</button>
    </div>
  ),
}));

describe('RoomMapViewer - Interactions', () => {
  beforeEach(() => {
    setupDefaultMocks();
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

    render(<RoomMapViewer plane="earth" zone="arkhamcity" />);

    const clickButton = screen.getByText('Click Node');
    clickButton.click();

    await waitFor(() => {
      expect(screen.getByTestId('room-details-panel')).toBeInTheDocument();
      expect(screen.getByText('Test Room 1')).toBeInTheDocument();
    });
  });

  it('should call onRoomSelect when room is selected', async () => {
    const onRoomSelect = vi.fn();
    const mockNodes = [
      {
        id: 'node1',
        type: 'room',
        position: { x: 0, y: 0 },
        data: { id: 'earth_arkhamcity_campus_room_001', name: 'Test Room 1' },
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

    render(<RoomMapViewer plane="earth" zone="arkhamcity" onRoomSelect={onRoomSelect} />);

    const clickButton = screen.getByText('Click Node');
    clickButton.click();

    await waitFor(() => {
      expect(onRoomSelect).toHaveBeenCalledWith('earth_arkhamcity_campus_room_001');
    });
  });

  it('should close room details panel', async () => {
    const mockNodes = [
      {
        id: 'node1',
        type: 'room',
        position: { x: 0, y: 0 },
        data: { id: 'earth_arkhamcity_campus_room_001', name: 'Test Room 1' },
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

    render(<RoomMapViewer plane="earth" zone="arkhamcity" />);

    const clickButton = screen.getByText('Click Node');
    clickButton.click();

    await waitFor(() => {
      expect(screen.getByTestId('room-details-panel')).toBeInTheDocument();
    });

    const closeButton = screen.getByText('Close');
    closeButton.click();

    await waitFor(() => {
      expect(screen.queryByTestId('room-details-panel')).not.toBeInTheDocument();
    });
  });

  it('should handle node click without onRoomSelect callback', async () => {
    const mockNodes = [
      {
        id: 'node1',
        type: 'room',
        position: { x: 0, y: 0 },
        data: { id: 'earth_arkhamcity_campus_room_001', name: 'Test Room 1' },
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

    render(<RoomMapViewer plane="earth" zone="arkhamcity" />);

    const clickButton = screen.getByText('Click Node');
    clickButton.click();

    await waitFor(() => {
      expect(screen.getByTestId('room-details-panel')).toBeInTheDocument();
    });
  });

  it('should handle selectedRoom not found in rooms array', async () => {
    const mockNodes = [
      {
        id: 'node1',
        type: 'room',
        position: { x: 0, y: 0 },
        data: { id: 'nonexistent-room', name: 'Non-existent Room' },
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

    render(<RoomMapViewer plane="earth" zone="arkhamcity" />);

    const clickButton = screen.getByText('Click Node');
    clickButton.click();

    await waitFor(() => {
      expect(screen.queryByTestId('room-details-panel')).not.toBeInTheDocument();
    });
  });

  it('should handle onRoomSelect optional callback (undefined)', async () => {
    const mockNodes = [
      {
        id: 'node1',
        type: 'room',
        position: { x: 0, y: 0 },
        data: { id: 'earth_arkhamcity_campus_room_001', name: 'Test Room 1' },
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

    render(<RoomMapViewer plane="earth" zone="arkhamcity" />);

    const clickButton = screen.getByText('Click Node');
    clickButton.click();

    await waitFor(() => {
      expect(screen.getByTestId('room-details-panel')).toBeInTheDocument();
    });
  });

  it('should handle selectedRoom null when selectedRoomId is null', () => {
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

    expect(screen.queryByTestId('room-details-panel')).not.toBeInTheDocument();
  });

  it('should handle rooms.find returning undefined (room not found)', async () => {
    const mockNodes = [
      {
        id: 'node1',
        type: 'room',
        position: { x: 0, y: 0 },
        data: { id: 'nonexistent-room-id', name: 'Non-existent Room' },
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

    const clickButton = screen.getByText('Click Node');
    clickButton.click();

    await waitFor(() => {
      expect(screen.queryByTestId('room-details-panel')).not.toBeInTheDocument();
    });
  });
});
