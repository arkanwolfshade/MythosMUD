/**
 * Room Map Editor component (Admin Edit Mode).
 *
 * This component provides admin editing capabilities for the map, including
 * node repositioning, edge creation/deletion, and property editing.
 *
 * As documented in the Pnakotic Manuscripts, proper management of dimensional
 * modifications is essential for maintaining the integrity of our eldritch architecture.
 */

import React, { useCallback, useMemo, useState } from 'react';
import ReactFlow, {
  Controls,
  Background,
  MiniMap,
  type Node,
  type Edge,
  type NodeChange,
  type EdgeChange,
} from 'reactflow';
import 'reactflow/dist/style.css';
import { useRoomMapData } from './hooks/useRoomMapData';
import { useMapLayout } from './hooks/useMapLayout';
import { useMapEditing } from './hooks/useMapEditing';
import { roomsToNodes, createEdgesFromRooms } from './utils/mapUtils';
import { nodeTypes, edgeTypes } from './config';
import type { RoomNodeData, ExitEdgeData } from './types';
import type { EdgeCreationData, EdgeValidationResult } from './hooks/useMapEditing';
import { MapControls } from './MapControls';
import { RoomDetailsPanel } from './RoomDetailsPanel';
import { MapEditToolbar } from './MapEditToolbar';
import { EdgeCreationModal } from './EdgeCreationModal';
import { EdgeDetailsPanel } from './EdgeDetailsPanel';
import { RoomEditModal } from './RoomEditModal';
import { saveMapChanges } from './utils/saveMapChanges';
import { getApiBaseUrl } from '../../utils/config';

export interface RoomMapEditorProps {
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
 * Room Map Editor component (Admin Edit Mode).
 */
export const RoomMapEditor: React.FC<RoomMapEditorProps> = ({
  plane,
  zone,
  subZone,
  currentRoomId,
  baseUrl,
  authToken,
  onRoomSelect,
}) => {
  const [selectedRoomId, setSelectedRoomId] = useState<string | null>(null);
  const [selectedEdgeId, setSelectedEdgeId] = useState<string | null>(null);
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedPlane, setSelectedPlane] = useState(plane);
  const [selectedZone, setSelectedZone] = useState(zone);
  const [selectedSubZone, setSelectedSubZone] = useState<string | undefined>(subZone);
  const [isEdgeCreationOpen, setIsEdgeCreationOpen] = useState(false);
  const [isEdgeEditOpen, setIsEdgeEditOpen] = useState(false);
  const [editingEdgeId, setEditingEdgeId] = useState<string | null>(null);
  const [isRoomEditOpen, setIsRoomEditOpen] = useState(false);
  const [editingRoomId, setEditingRoomId] = useState<string | null>(null);
  const [previewEdge, setPreviewEdge] = useState<Edge<ExitEdgeData> | null>(null);
  const [edgeValidation, setEdgeValidation] = useState<EdgeValidationResult | null>(null);

  // Fetch room data
  const { rooms, isLoading, error, refetch } = useRoomMapData({
    plane: selectedPlane,
    zone: selectedZone,
    subZone: selectedSubZone,
    includeExits: true,
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
        room.name?.toLowerCase().includes(query) ||
        room.id?.toLowerCase().includes(query) ||
        room.description?.toLowerCase().includes(query) ||
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

  // Apply layout to nodes
  const { layoutNodes: initialLayoutNodes } = useMapLayout({
    nodes: rawNodes,
    useStoredCoordinates: true,
  });

  // Use editing hook for admin operations
  const {
    nodes: editedNodes,
    edges: editedEdges,
    hasUnsavedChanges,
    canUndo,
    canRedo,
    updateNodePosition,
    deleteEdge,
    updateEdge,
    updateRoom,
    validateEdgeCreation,
    undo,
    redo,
    save,
    reset,
  } = useMapEditing({
    nodes: initialLayoutNodes,
    edges: rawEdges as Edge<ExitEdgeData>[],
    onSave: async changes => {
      try {
        await saveMapChanges(changes, {
          authToken,
          baseUrl: baseUrl || getApiBaseUrl(),
        });
      } catch (error) {
        console.error('Failed to save map changes:', error);
        throw error; // Re-throw so MapEditToolbar can handle it
      }
    },
  });

  // Handle React Flow node changes (drag, position updates)
  const onNodesChange = useCallback(
    (changes: NodeChange[]) => {
      // Track position changes in our editing system
      for (const change of changes) {
        if (change.type === 'position' && change.position) {
          updateNodePosition(change.id, change.position);
        }
      }
    },
    [updateNodePosition]
  );

  // Handle React Flow edge changes
  const onEdgesChange = useCallback(
    (changes: EdgeChange[]) => {
      // Track deletions in our editing system
      for (const change of changes) {
        if (change.type === 'remove') {
          deleteEdge(change.id);
        }
      }
    },
    [deleteEdge]
  );

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

  // Get selected edge data
  const selectedEdge = useMemo(() => {
    if (!selectedEdgeId) {
      return null;
    }
    return editedEdges.find(edge => edge.id === selectedEdgeId) || null;
  }, [selectedEdgeId, editedEdges]);

  // Get room names for selected edge
  const edgeSourceRoomName = useMemo(() => {
    if (!selectedEdge) return undefined;
    const sourceNode = editedNodes.find(node => node.id === selectedEdge.source);
    return sourceNode?.data.name;
  }, [selectedEdge, editedNodes]);

  const edgeTargetRoomName = useMemo(() => {
    if (!selectedEdge) return undefined;
    const targetNode = editedNodes.find(node => node.id === selectedEdge.target);
    return targetNode?.data.name;
  }, [selectedEdge, editedNodes]);

  // Close room details panel
  const handleClosePanel = useCallback(() => {
    setSelectedRoomId(null);
  }, []);

  // Close edge details panel
  const handleCloseEdgePanel = useCallback(() => {
    setSelectedEdgeId(null);
  }, []);

  // Handle edge deletion
  const handleDeleteEdge = useCallback(
    (edgeId: string) => {
      deleteEdge(edgeId);
      setSelectedEdgeId(null);
    },
    [deleteEdge]
  );

  // Handle edge editing
  const handleEditEdge = useCallback((edgeId: string) => {
    setEditingEdgeId(edgeId);
    setIsEdgeEditOpen(true);
  }, []);

  // Handle room editing
  const handleEditRoom = useCallback((roomId: string) => {
    setEditingRoomId(roomId);
    setIsRoomEditOpen(true);
  }, []);

  // Get room data for editing
  const editingRoom = useMemo(() => {
    if (!editingRoomId) return null;
    return rooms.find(room => room.id === editingRoomId) || null;
  }, [editingRoomId, rooms]);

  // Handle room update
  const handleUpdateRoom = useCallback(
    (roomId: string, updates: Partial<RoomNodeData>) => {
      updateRoom(roomId, updates);
      setIsRoomEditOpen(false);
      setEditingRoomId(null);
    },
    [updateRoom]
  );

  // Get edge data for editing
  const editingEdgeData = useMemo(() => {
    if (!editingEdgeId) return undefined;
    const edge = editedEdges.find(e => e.id === editingEdgeId);
    if (!edge || !edge.data) return undefined;

    return {
      edgeId: edge.id,
      sourceRoomId: edge.source,
      targetRoomId: edge.target,
      direction: edge.data.direction || '',
      flags: edge.data.flags,
      description: edge.data.description,
    };
  }, [editingEdgeId, editedEdges]);

  // Handle edge update
  const handleUpdateEdge = useCallback(
    (edgeId: string, edgeData: EdgeCreationData) => {
      // Update edge properties (direction, flags, description)
      // Note: target room cannot be changed in edit mode
      updateEdge(edgeId, {
        direction: edgeData.direction,
        flags: edgeData.flags,
        description: edgeData.description,
      });
      setIsEdgeEditOpen(false);
      setEditingEdgeId(null);
      setPreviewEdge(null);
      setEdgeValidation(null);
    },
    [updateEdge]
  );

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
            onClick={() => setSearchQuery('')}
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

      {/* Edit toolbar */}
      <div className="absolute top-4 right-4 z-10">
        <MapEditToolbar
          hasUnsavedChanges={hasUnsavedChanges}
          canUndo={canUndo}
          canRedo={canRedo}
          onUndo={undo}
          onRedo={redo}
          onSave={save}
          onReset={reset}
        />
      </div>

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
          availableSubZones={Array.from(new Set(rooms.map(r => r.sub_zone).filter(Boolean)))} // Extract from rooms
        />
      </div>

      {/* React Flow map (editable) */}
      <ReactFlow
        nodes={editedNodes}
        edges={[...editedEdges, ...(previewEdge ? [previewEdge] : [])]}
        nodeTypes={nodeTypes}
        edgeTypes={edgeTypes}
        onNodesChange={onNodesChange}
        onEdgesChange={onEdgesChange}
        onNodeClick={handleNodeClick}
        onEdgeClick={handleEdgeClick}
        nodesDraggable={true}
        nodesConnectable={false}
        elementsSelectable={true}
        edgesFocusable={true}
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
            if (node.data?.hasUnsavedChanges) {
              return '#fbbf24'; // Yellow for unsaved changes
            }
            return '#6b7280'; // Gray for other rooms
          }}
        />
      </ReactFlow>

      {/* Room details panel */}
      {selectedRoom && (
        <RoomDetailsPanel
          room={selectedRoom}
          onClose={handleClosePanel}
          onEditRoom={handleEditRoom}
          onCreateExit={() => {
            if (selectedRoomId) {
              setIsEdgeCreationOpen(true);
            }
          }}
          isAdmin={true}
        />
      )}

      {/* Edge details panel */}
      {selectedEdge && (
        <EdgeDetailsPanel
          edge={selectedEdge}
          sourceRoomName={edgeSourceRoomName}
          targetRoomName={edgeTargetRoomName}
          onClose={handleCloseEdgePanel}
          onDelete={handleDeleteEdge}
          onEdit={handleEditEdge}
          isAdmin={true}
        />
      )}

      {/* Edge creation modal */}
      {selectedRoomId && (
        <EdgeCreationModal
          isOpen={isEdgeCreationOpen}
          onClose={() => {
            setIsEdgeCreationOpen(false);
            setPreviewEdge(null);
            setEdgeValidation(null);
          }}
          sourceRoomId={selectedRoomId}
          availableNodes={editedNodes}
          availableDirections={availableDirections}
          validation={edgeValidation}
          onCreate={handleCreateEdge}
          onValidate={validateEdgeCreation}
          onPreviewChange={handlePreviewChange}
        />
      )}

      {/* Edge edit modal */}
      {editingEdgeData && (
        <EdgeCreationModal
          isOpen={isEdgeEditOpen}
          onClose={() => {
            setIsEdgeEditOpen(false);
            setEditingEdgeId(null);
            setPreviewEdge(null);
            setEdgeValidation(null);
          }}
          sourceRoomId={editingEdgeData.sourceRoomId}
          availableNodes={editedNodes}
          availableDirections={availableDirections}
          validation={edgeValidation}
          onCreate={handleCreateEdge} // Not used in edit mode
          onValidate={validateEdgeCreation}
          onPreviewChange={handlePreviewChange}
          existingEdge={editingEdgeData}
          onUpdate={handleUpdateEdge}
        />
      )}

      {/* Room edit modal */}
      {editingRoom && (
        <RoomEditModal
          isOpen={isRoomEditOpen}
          onClose={() => {
            setIsRoomEditOpen(false);
            setEditingRoomId(null);
          }}
          room={editingRoom}
          onUpdate={handleUpdateRoom}
        />
      )}
    </div>
  );
};
