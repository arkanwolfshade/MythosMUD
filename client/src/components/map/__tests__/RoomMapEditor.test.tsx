import { beforeEach, describe, expect, it, vi } from 'vitest';

const useRoomMapDataMock = vi.hoisted(() =>
  vi.fn((_options?: unknown) => ({
    rooms: [
      {
        id: 'room1',
        name: 'Room 1',
        description: 'Test room',
        zone: 'test-zone',
        sub_zone: 'test-subzone',
        exits: { north: 'room2' },
      },
    ],
    isLoading: false,
    error: null,
    refetch: vi.fn(),
  }))
);

vi.mock('../hooks/useRoomMapData', () => ({
  useRoomMapData: (options: unknown) => useRoomMapDataMock(options),
}));

import '@testing-library/jest-dom';
import { fireEvent, render, screen } from '@testing-library/react';
import React from 'react';
import { RoomMapEditor } from '../RoomMapEditor';
import type { UseRoomMapDataOptions } from '../hooks/useRoomMapData';
import './roomMapEditorTestSetup';

describe('RoomMapEditor', () => {
  const defaultProps = {
    plane: 'test-plane',
    zone: 'test-zone',
    authToken: 'test-token',
  };

  beforeEach(() => {
    vi.clearAllMocks();
    useRoomMapDataMock.mockImplementation(() => ({
      rooms: [
        {
          id: 'room1',
          name: 'Room 1',
          description: 'Test room',
          zone: 'test-zone',
          sub_zone: 'test-subzone',
          exits: { north: 'room2' },
        },
      ],
      isLoading: false,
      error: null,
      refetch: vi.fn(),
    }));
  });

  describe('Basic Rendering', () => {
    it('should render ReactFlow component', () => {
      render(<RoomMapEditor {...defaultProps} />);

      expect(screen.getByTestId('react-flow')).toBeInTheDocument();
    });

    it('should render map controls', () => {
      render(<RoomMapEditor {...defaultProps} />);

      expect(screen.getByTestId('map-controls')).toBeInTheDocument();
    });

    it('should render map edit toolbar', () => {
      render(<RoomMapEditor {...defaultProps} />);

      expect(screen.getByTestId('map-edit-toolbar')).toBeInTheDocument();
    });

    it('should render background, controls, and minimap', () => {
      render(<RoomMapEditor {...defaultProps} />);

      expect(screen.getByTestId('background')).toBeInTheDocument();
      expect(screen.getByTestId('controls')).toBeInTheDocument();
      expect(screen.getByTestId('minimap')).toBeInTheDocument();
    });
  });

  describe('Search Functionality', () => {
    it('should filter rooms by search query', async () => {
      render(<RoomMapEditor {...defaultProps} />);

      const searchInput = screen.getByTestId('search-input');
      expect(searchInput).toBeInTheDocument();
    });
  });

  describe('Node Interactions', () => {
    it('should handle node click', () => {
      const onRoomSelect = vi.fn();
      render(<RoomMapEditor {...defaultProps} onRoomSelect={onRoomSelect} />);

      const nodeClickButton = screen.getByTestId('trigger-node-click');
      expect(nodeClickButton).toBeInTheDocument();
    });

    it('should handle node position changes', () => {
      render(<RoomMapEditor {...defaultProps} />);

      const nodeChangeButton = screen.getByTestId('trigger-node-change');
      expect(nodeChangeButton).toBeInTheDocument();
    });
  });

  describe('Edge Interactions', () => {
    it('should handle edge click', () => {
      render(<RoomMapEditor {...defaultProps} />);

      const edgeClickButton = screen.getByTestId('trigger-edge-click');
      expect(edgeClickButton).toBeInTheDocument();
    });

    it('should handle edge deletion', () => {
      render(<RoomMapEditor {...defaultProps} />);

      const edgeChangeButton = screen.getByTestId('trigger-edge-change');
      expect(edgeChangeButton).toBeInTheDocument();
    });
  });

  describe('Props Handling', () => {
    it('should accept plane and zone props', () => {
      render(<RoomMapEditor plane="plane1" zone="zone1" />);

      expect(screen.getByTestId('react-flow')).toBeInTheDocument();
    });

    it('should accept optional subZone prop', () => {
      render(<RoomMapEditor {...defaultProps} subZone="subzone1" />);

      expect(screen.getByTestId('react-flow')).toBeInTheDocument();
    });

    it('should accept optional currentRoomId prop', () => {
      render(<RoomMapEditor {...defaultProps} currentRoomId="room1" />);

      expect(screen.getByTestId('react-flow')).toBeInTheDocument();
    });

    it('should accept optional baseUrl prop', () => {
      render(<RoomMapEditor {...defaultProps} baseUrl="http://custom-url.com" />);

      expect(screen.getByTestId('react-flow')).toBeInTheDocument();
    });

    it('should accept optional authToken prop', () => {
      render(<RoomMapEditor {...defaultProps} authToken="custom-token" />);

      expect(screen.getByTestId('react-flow')).toBeInTheDocument();
    });

    it('should accept optional onRoomSelect callback', () => {
      const onRoomSelect = vi.fn();
      render(<RoomMapEditor {...defaultProps} onRoomSelect={onRoomSelect} />);

      expect(screen.getByTestId('react-flow')).toBeInTheDocument();
    });
  });

  describe('Loading and Error States', () => {
    it('should handle loading state', () => {
      render(<RoomMapEditor {...defaultProps} />);

      expect(screen.getByTestId('react-flow')).toBeInTheDocument();
    });

    it('should handle error state', () => {
      render(<RoomMapEditor {...defaultProps} />);

      expect(screen.getByTestId('react-flow')).toBeInTheDocument();
    });
  });

  describe('Scene data loading transitions', () => {
    it('requests map data with updated plane after MapControls plane change', () => {
      render(<RoomMapEditor {...defaultProps} />);
      const planeInput = screen.getByTestId('plane-input');
      fireEvent.change(planeInput, { target: { value: 'other-plane' } });

      const lastArgs = useRoomMapDataMock.mock.calls.at(-1);
      expect(lastArgs).toBeDefined();
      const opts = lastArgs![0] as UseRoomMapDataOptions;
      expect(opts.plane).toBe('other-plane');
    });

    it('requests map data with updated zone and subZone', () => {
      render(<RoomMapEditor {...defaultProps} />);
      fireEvent.change(screen.getByTestId('zone-input'), { target: { value: 'new-zone' } });
      fireEvent.change(screen.getByTestId('subzone-input'), { target: { value: 'new-sub' } });

      const lastArgs = useRoomMapDataMock.mock.calls.at(-1);
      expect(lastArgs).toBeDefined();
      const opts = lastArgs![0] as UseRoomMapDataOptions;
      expect(opts.zone).toBe('new-zone');
      expect(opts.subZone).toBe('new-sub');
    });
  });

  describe('Edge Cases', () => {
    it('should handle empty rooms array', () => {
      useRoomMapDataMock.mockReturnValueOnce({
        rooms: [],
        isLoading: false,
        error: null,
        refetch: vi.fn(),
      });

      render(<RoomMapEditor {...defaultProps} />);

      expect(screen.getByText(/No rooms available/i)).toBeInTheDocument();
    });

    it('should handle search query changes', () => {
      render(<RoomMapEditor {...defaultProps} />);

      const searchInput = screen.getByTestId('search-input');
      expect(searchInput).toBeInTheDocument();
    });

    it('should handle plane changes', () => {
      render(<RoomMapEditor {...defaultProps} />);

      const planeInput = screen.getByTestId('plane-input');
      expect(planeInput).toBeInTheDocument();
    });

    it('should handle zone changes', () => {
      render(<RoomMapEditor {...defaultProps} />);

      const zoneInput = screen.getByTestId('zone-input');
      expect(zoneInput).toBeInTheDocument();
    });

    it('should handle subZone changes', () => {
      render(<RoomMapEditor {...defaultProps} />);

      const subzoneInput = screen.getByTestId('subzone-input');
      expect(subzoneInput).toBeInTheDocument();
    });
  });
});
