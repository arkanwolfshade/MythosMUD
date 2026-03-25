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
  Background,
  Controls,
  MiniMap,
  type Edge,
  type EdgeChange,
  type Node,
  type NodeChange,
} from 'reactflow';
import 'reactflow/dist/style.css';
import { getVersionedApiBaseUrl } from '../../utils/config';
import { EdgeCreationModal } from './EdgeCreationModal';
import { EdgeDetailsPanel } from './EdgeDetailsPanel';
import { MapControls } from './MapControls';
import { MapEditToolbar } from './MapEditToolbar';
import { RoomDetailsPanel } from './RoomDetailsPanel';
import { RoomEditModal } from './RoomEditModal';
import { edgeTypes, nodeTypes } from './config';
import type { EdgeCreationData, EdgeValidationResult } from './hooks/useMapEditing';
import { useMapEditing } from './hooks/useMapEditing';
import { useMapLayout } from './hooks/useMapLayout';
import { useRoomMapData } from './hooks/useRoomMapData';
import type { ExitEdgeData, RoomNodeData } from './types';
import { createEdgesFromRooms, roomsToNodes } from './utils/mapUtils';
import { saveMapChanges } from './utils/saveMapChanges';

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
  const [isRoomEditOpen, setIsRoomEditOpen] = useState(false);
  const [editingRoomId, setEditingRoomId] = useState<string | null>(null);
  const [previewEdge, setPreviewEdge] = useState<Edge<ExitEdgeData> | null>(null);
  const [edgeValidation, setEdgeValidation] = useState<EdgeValidationResult | null>(null);

  const { rooms, isLoading, error, refetch } = useRoomMapData({
    plane: selectedPlane,
    zone: selectedZone,
    subZone: selectedSubZone,
    includeExits: true,
    baseUrl,
    authToken,
  });

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

  const { nodes: rawNodes, edges: rawEdges } = useMemo(() => {
    if (filteredRooms.length === 0) {
      return { nodes: [], edges: [] };
    }
    return {
      nodes: roomsToNodes(filteredRooms, currentRoomId),
      edges: createEdgesFromRooms(filteredRooms),
    };
  }, [filteredRooms, currentRoomId]);

  const { layoutNodes: initialLayoutNodes } = useMapLayout({
    nodes: rawNodes,
    useStoredCoordinates: true,
  });

  const availableDirections = useMemo(
    () => [
      'north',
      'south',
      'east',
      'west',
      'northeast',
      'northwest',
      'southeast',
      'southwest',
      'up',
      'down',
      'in',
      'out',
    ],
    []
  );

  const {
    nodes: editedNodes,
    edges: editedEdges,
    hasUnsavedChanges,
    canUndo,
    canRedo,
    updateNodePosition,
    createEdge,
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
      await saveMapChanges(changes, {
        authToken,
        baseUrl: baseUrl || getVersionedApiBaseUrl(),
      });
    },
  });

  const onNodesChange = useCallback(
    (changes: NodeChange[]) => {
      for (const change of changes) {
        if (change.type === 'position' && change.position) {
          updateNodePosition(change.id, change.position);
        }
      }
    },
    [updateNodePosition]
  );

  const onEdgesChange = useCallback(
    (changes: EdgeChange[]) => {
      for (const change of changes) {
        if (change.type === 'remove') {
          deleteEdge(change.id);
        }
      }
    },
    [deleteEdge]
  );

  const handleNodeClick = useCallback(
    (_event: React.MouseEvent, node: Node<RoomNodeData>) => {
      setSelectedRoomId(node.data.id);
      onRoomSelect?.(node.data.id);
    },
    [onRoomSelect]
  );

  const handleEdgeClick = useCallback((_event: React.MouseEvent, edge: Edge<ExitEdgeData>) => {
    setSelectedEdgeId(edge.id);
  }, []);

  const selectedRoom = useMemo(
    () => (selectedRoomId ? rooms.find(room => room.id === selectedRoomId) || null : null),
    [selectedRoomId, rooms]
  );
  const selectedEdge = useMemo(
    () => (selectedEdgeId ? editedEdges.find(edge => edge.id === selectedEdgeId) || null : null),
    [selectedEdgeId, editedEdges]
  );

  const edgeSourceRoomName = useMemo(() => {
    if (!selectedEdge) return undefined;
    return editedNodes.find(node => node.id === selectedEdge.source)?.data.name;
  }, [selectedEdge, editedNodes]);
  const edgeTargetRoomName = useMemo(() => {
    if (!selectedEdge) return undefined;
    return editedNodes.find(node => node.id === selectedEdge.target)?.data.name;
  }, [selectedEdge, editedNodes]);

  const handleClosePanel = useCallback(() => {
    setSelectedRoomId(null);
  }, []);
  const handleCloseEdgePanel = useCallback(() => {
    setSelectedEdgeId(null);
  }, []);
  const handleDeleteEdge = useCallback(
    (edgeId: string) => {
      deleteEdge(edgeId);
      setSelectedEdgeId(null);
    },
    [deleteEdge]
  );

  const [editingEdgeDataState, setEditingEdgeDataState] = useState<string | null>(null);
  const handleEditEdge = useCallback((edgeId: string) => {
    setEditingEdgeDataState(edgeId);
    setIsEdgeEditOpen(true);
  }, []);
  const handleEditRoom = useCallback((roomId: string) => {
    setEditingRoomId(roomId);
    setIsRoomEditOpen(true);
  }, []);

  const editingRoom = useMemo(
    () => (editingRoomId ? rooms.find(room => room.id === editingRoomId) || null : null),
    [editingRoomId, rooms]
  );

  const handleUpdateRoom = useCallback(
    (roomId: string, updates: Partial<RoomNodeData>) => {
      updateRoom(roomId, updates);
      setIsRoomEditOpen(false);
      setEditingRoomId(null);
    },
    [updateRoom]
  );

  const editingEdgeData = useMemo(() => {
    if (!editingEdgeDataState) return undefined;
    const edge = editedEdges.find(e => e.id === editingEdgeDataState);
    if (!edge || !edge.data) return undefined;
    return {
      edgeId: edge.id,
      sourceRoomId: edge.source,
      targetRoomId: edge.target,
      direction: edge.data.direction || '',
      flags: edge.data.flags,
      description: edge.data.description,
    };
  }, [editingEdgeDataState, editedEdges]);

  const handleCreateEdge = useCallback(
    (edgeData: EdgeCreationData) => {
      createEdge(edgeData);
      setIsEdgeCreationOpen(false);
      setSelectedRoomId(null);
      setPreviewEdge(null);
      setEdgeValidation(null);
    },
    [createEdge]
  );

  const handleUpdateEdge = useCallback(
    (edgeId: string, edgeData: EdgeCreationData) => {
      updateEdge(edgeId, {
        direction: edgeData.direction,
        flags: edgeData.flags,
        description: edgeData.description,
      });
      setIsEdgeEditOpen(false);
      setEditingEdgeDataState(null);
      setPreviewEdge(null);
      setEdgeValidation(null);
    },
    [updateEdge]
  );

  const handlePreviewChange = useCallback(
    (edgeData: EdgeCreationData | null) => {
      if (!edgeData) {
        setPreviewEdge(null);
        setEdgeValidation(null);
        return;
      }
      const validation = validateEdgeCreation(edgeData);
      setEdgeValidation(validation);
      if (validation.isValid && edgeData.targetRoomId) {
        setPreviewEdge({
          id: `preview-${edgeData.sourceRoomId}-${edgeData.direction}-${edgeData.targetRoomId}`,
          source: edgeData.sourceRoomId,
          target: edgeData.targetRoomId,
          type: 'exit',
          data: {
            direction: edgeData.direction,
            sourceRoomId: edgeData.sourceRoomId,
            targetRoomId: edgeData.targetRoomId,
            flags: edgeData.flags,
            description: edgeData.description,
          },
          style: { strokeDasharray: '5,5', opacity: 0.5 },
        });
      } else {
        setPreviewEdge(null);
      }
    },
    [validateEdgeCreation]
  );

  if (isLoading) {
    return (
      <div className="flex items-center justify-center h-full w-full bg-mythos-terminal-background">
        <div className="text-mythos-terminal-text">Loading map...</div>
      </div>
    );
  }
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
      {error && (
        <div className="absolute top-0 left-0 right-0 bg-mythos-terminal-error text-white p-2 text-center z-50">
          {error}
        </div>
      )}
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
          availablePlanes={[plane]}
          availableZones={[zone]}
          availableSubZones={Array.from(
            new Set(
              rooms.map(r => r.sub_zone).filter((sub): sub is string => typeof sub === 'string' && sub.length > 0)
            )
          )}
        />
      </div>
      <div
        className="relative h-full w-full"
        style={{ backgroundColor: 'var(--color-mythos-terminal-background, #0a0a0a)' }}
      >
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
          <Background style={{ backgroundColor: 'var(--color-mythos-terminal-background, #0a0a0a)', opacity: 1 }} />
          <MiniMap
            className="bg-mythos-terminal-background border border-mythos-terminal-border"
            nodeColor={node => {
              if (node.data?.isCurrentLocation) return '#10b981';
              if (node.data?.hasUnsavedChanges) return '#fbbf24';
              return '#6b7280';
            }}
          />
        </ReactFlow>
      </div>
      {selectedRoom && (
        <RoomDetailsPanel
          room={selectedRoom}
          onClose={handleClosePanel}
          onEditRoom={handleEditRoom}
          onCreateExit={() => {
            if (selectedRoomId) setIsEdgeCreationOpen(true);
          }}
          isAdmin={true}
        />
      )}
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
      {editingEdgeData && (
        <EdgeCreationModal
          isOpen={isEdgeEditOpen}
          onClose={() => {
            setIsEdgeEditOpen(false);
            setEditingEdgeDataState(null);
            setPreviewEdge(null);
            setEdgeValidation(null);
          }}
          sourceRoomId={editingEdgeData.sourceRoomId}
          availableNodes={editedNodes}
          availableDirections={availableDirections}
          validation={edgeValidation}
          onCreate={handleCreateEdge}
          onValidate={validateEdgeCreation}
          onPreviewChange={handlePreviewChange}
          existingEdge={editingEdgeData}
          onUpdate={handleUpdateEdge}
        />
      )}
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
