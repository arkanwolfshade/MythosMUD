/**
 * Main Room Map Viewer component.
 *
 * This component provides the view-only mode for players to explore the world map.
 * It displays rooms as nodes connected by exits, with support for filtering,
 * searching, and room details.
 *
 * As documented in the Pnakotic Manuscripts, proper visualization of spatial
 * relationships is essential for understanding the eldritch architecture of our world.
 */

import React, { useCallback, useMemo, useState } from 'react';
import ReactFlow, { Background, Controls, MiniMap, type Edge, type Node } from 'reactflow';
import 'reactflow/dist/style.css';
import { MapControls } from './MapControls';
import { RoomDetailsPanel } from './RoomDetailsPanel';
import { edgeTypes, nodeTypes } from './config';
import { useMapLayout } from './hooks/useMapLayout';
import { useRoomMapData } from './hooks/useRoomMapData';
import type { ExitEdgeData, RoomNodeData } from './types';
import { createEdgesFromRooms, roomsToNodes } from './utils/mapUtils';

export interface RoomMapViewerProps {
  /** Plane name (required) */
  plane: string;
  /** Zone name (required) */
  zone: string;
  /** Optional sub-zone name for filtering */
  subZone?: string;
  /** Current player's room ID for highlighting */
  currentRoomId?: string;
  /** API base URL */
  baseUrl?: string;
  /** Auth token for authenticated requests */
  authToken?: string;
  /** Callback when room is selected */
  onRoomSelect?: (roomId: string) => void;
}

/**
 * Room Map Viewer component.
 */
export const RoomMapViewer: React.FC<RoomMapViewerProps> = ({
  plane,
  zone,
  subZone,
  currentRoomId,
  baseUrl,
  authToken,
  onRoomSelect,
}) => {
  const [selectedRoomId, setSelectedRoomId] = useState<string | null>(null);
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedPlane, setSelectedPlane] = useState(plane);
  const [selectedZone, setSelectedZone] = useState(zone);
  const [selectedSubZone, setSelectedSubZone] = useState<string | undefined>(subZone);

  // Fetch room data
  // For players (with authToken), filter to only show explored rooms
  // For admins or unauthenticated users, show all rooms
  const { rooms, isLoading, error, refetch } = useRoomMapData({
    plane: selectedPlane,
    zone: selectedZone,
    subZone: selectedSubZone,
    includeExits: true,
    filterExplored: !!authToken, // Filter to explored rooms if authenticated (player view)
    baseUrl,
    authToken,
  });

  // Filter rooms by search query
  const filteredRooms = useMemo(() => {
    if (!searchQuery.trim()) {
      return rooms;
    }

    const query = searchQuery.toLowerCase();
    return rooms.filter(room => {
      return (
        room.name.toLowerCase().includes(query) ||
        room.id.toLowerCase().includes(query) ||
        room.description.toLowerCase().includes(query) ||
        room.zone?.toLowerCase().includes(query) ||
        room.sub_zone?.toLowerCase().includes(query)
      );
    });
  }, [rooms, searchQuery]);

  // Convert rooms to nodes and edges
  const { nodes: rawNodes, edges: rawEdges } = useMemo(() => {
    if (filteredRooms.length === 0) {
      return { nodes: [], edges: [] };
    }

    const nodes = roomsToNodes(filteredRooms, currentRoomId);
    const edges = createEdgesFromRooms(filteredRooms);

    return { nodes, edges };
  }, [filteredRooms, currentRoomId]);

  // Apply layout to nodes (force-directed by default to minimize edge crossings)
  const { layoutNodes } = useMapLayout({
    nodes: rawNodes,
    edges: rawEdges,
    layoutAlgorithm: 'force',
    useStoredCoordinates: true,
  });

  // Handle node click
  const handleNodeClick = useCallback(
    (_event: React.MouseEvent, node: Node<RoomNodeData>) => {
      setSelectedRoomId(node.data.id);
      onRoomSelect?.(node.data.id);
    },
    [onRoomSelect]
  );

  // Get selected room data
  const selectedRoom = useMemo(() => {
    if (!selectedRoomId) {
      return null;
    }
    return rooms.find(room => room.id === selectedRoomId) || null;
  }, [selectedRoomId, rooms]);

  // Close room details panel
  const handleClosePanel = useCallback(() => {
    setSelectedRoomId(null);
  }, []);

  // Loading state
  if (isLoading) {
    return (
      <div className="flex items-center justify-center h-full w-full bg-mythos-terminal-background">
        <div className="text-mythos-terminal-text">Loading map...</div>
      </div>
    );
  }

  // Error state
  if (error) {
    return (
      <div className="flex flex-col items-center justify-center h-full w-full bg-mythos-terminal-background p-4">
        <div className="text-mythos-terminal-error mb-4">Error: {error}</div>
        <button
          onClick={() => refetch()}
          className="px-4 py-2 bg-mythos-terminal-primary text-white rounded hover:bg-mythos-terminal-primary/80"
        >
          Retry
        </button>
      </div>
    );
  }

  // Empty state
  if (filteredRooms.length === 0) {
    return (
      <div className="flex flex-col items-center justify-center h-full w-full bg-mythos-terminal-background p-4">
        <div className="text-mythos-terminal-text mb-4">
          {searchQuery ? 'No rooms found matching your search.' : 'No rooms available in this area.'}
        </div>
        {searchQuery && (
          <button
            onClick={() => {
              setSearchQuery('');
            }}
            className="px-4 py-2 bg-mythos-terminal-primary text-white rounded hover:bg-mythos-terminal-primary/80"
          >
            Clear Search
          </button>
        )}
      </div>
    );
  }

  return (
    <div className="relative h-full w-full bg-mythos-terminal-background">
      {/* Error banner */}
      {error && (
        <div className="absolute top-0 left-0 right-0 bg-mythos-terminal-error text-white p-2 text-center z-50">
          {error}
        </div>
      )}

      {/* Map controls */}
      <div className="absolute top-4 left-4 z-10">
        <MapControls
          searchQuery={searchQuery}
          onSearchChange={setSearchQuery}
          plane={selectedPlane}
          zone={selectedZone}
          subZone={selectedSubZone}
          onPlaneChange={setSelectedPlane}
          onZoneChange={setSelectedZone}
          onSubZoneChange={setSelectedSubZone}
          availablePlanes={[plane]} // TODO: Get from API
          availableZones={[zone]} // TODO: Get from API
          availableSubZones={Array.from(
            new Set(rooms.map(r => r.sub_zone).filter((zone): zone is string => Boolean(zone)))
          )} // Extract from rooms
        />
      </div>

      {/* React Flow map */}
      <ReactFlow
        nodes={layoutNodes}
        edges={rawEdges as Edge<ExitEdgeData>[]}
        nodeTypes={nodeTypes}
        edgeTypes={edgeTypes}
        onNodeClick={handleNodeClick}
        fitView
        className="bg-mythos-terminal-background"
        onlyRenderVisibleElements={true}
        proOptions={{ hideAttribution: true }}
      >
        <Controls className="bg-mythos-terminal-background border border-mythos-terminal-border" />
        <Background />
        <MiniMap
          className="bg-mythos-terminal-background border border-mythos-terminal-border"
          nodeColor={node => {
            if (node.data?.isCurrentLocation) {
              return '#10b981'; // Green for current location
            }
            return '#6b7280'; // Gray for other rooms
          }}
        />
      </ReactFlow>

      {/* Room details panel */}
      {selectedRoom && <RoomDetailsPanel room={selectedRoom} onClose={handleClosePanel} />}
    </div>
  );
};
