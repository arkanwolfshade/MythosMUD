/**
 * Hooks and helpers for RoomMapEditorRuntime.
 */

import { useCallback, useMemo, useState } from 'react';
import type { Edge, EdgeChange, Node, NodeChange } from 'reactflow';
import type { Room } from '../../stores/gameStore';
import { getVersionedApiBaseUrl } from '../../utils/config';
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

export const MAP_EDITOR_DIRECTIONS = [
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
];

function filterEditorRooms(rooms: Room[], searchQuery: string): Room[] {
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
}

function buildPreviewEdge(
  edgeData: EdgeCreationData,
  validateEdgeCreation: (edgeData: EdgeCreationData) => EdgeValidationResult
): { preview: Edge<ExitEdgeData> | null; validation: EdgeValidationResult } {
  const validation = validateEdgeCreation(edgeData);
  if (!validation.isValid || !edgeData.targetRoomId) {
    return { preview: null, validation };
  }
  return {
    validation,
    preview: {
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
    },
  };
}

function useRoomMapEditorData(props: RoomMapEditorProps) {
  const { plane, zone, subZone, currentRoomId, baseUrl, authToken } = props;
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedPlane, setSelectedPlane] = useState(plane);
  const [selectedZone, setSelectedZone] = useState(zone);
  const [selectedSubZone, setSelectedSubZone] = useState<string | undefined>(subZone);

  const { rooms, isLoading, error, refetch } = useRoomMapData({
    plane: selectedPlane,
    zone: selectedZone,
    subZone: selectedSubZone,
    includeExits: true,
    baseUrl,
    authToken,
  });

  const filteredRooms = useMemo(() => filterEditorRooms(rooms, searchQuery), [rooms, searchQuery]);
  const { nodes: rawNodes, edges: rawEdges } = useMemo(() => {
    if (filteredRooms.length === 0) {
      return { nodes: [], edges: [] };
    }
    return {
      nodes: roomsToNodes(filteredRooms, currentRoomId),
      edges: createEdgesFromRooms(filteredRooms),
    };
  }, [filteredRooms, currentRoomId]);
  const { layoutNodes: initialLayoutNodes } = useMapLayout({ nodes: rawNodes, useStoredCoordinates: true });

  return {
    plane,
    zone,
    rooms,
    isLoading,
    error,
    refetch,
    filteredRooms,
    rawEdges,
    initialLayoutNodes,
    searchQuery,
    setSearchQuery,
    selectedPlane,
    setSelectedPlane,
    selectedZone,
    setSelectedZone,
    selectedSubZone,
    setSelectedSubZone,
  };
}

function useRoomMapEditorEditing(
  initialLayoutNodes: Node<RoomNodeData>[],
  rawEdges: Edge<ExitEdgeData>[],
  authToken?: string,
  baseUrl?: string
) {
  const editing = useMapEditing({
    nodes: initialLayoutNodes,
    edges: rawEdges,
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
          editing.updateNodePosition(change.id, change.position);
        }
      }
    },
    [editing]
  );

  const onEdgesChange = useCallback(
    (changes: EdgeChange[]) => {
      for (const change of changes) {
        if (change.type === 'remove') {
          editing.deleteEdge(change.id);
        }
      }
    },
    [editing]
  );

  return { ...editing, onNodesChange, onEdgesChange };
}

export interface RoomMapEditorEditingApi {
  createEdge: ReturnType<typeof useMapEditing>['createEdge'];
  deleteEdge: ReturnType<typeof useMapEditing>['deleteEdge'];
  updateEdge: ReturnType<typeof useMapEditing>['updateEdge'];
  updateRoom: ReturnType<typeof useMapEditing>['updateRoom'];
  validateEdgeCreation: ReturnType<typeof useMapEditing>['validateEdgeCreation'];
}

function useRoomMapEditorSelection(
  rooms: Room[],
  editedEdges: Edge<ExitEdgeData>[],
  onRoomSelect: RoomMapEditorProps['onRoomSelect']
) {
  const [selectedRoomId, setSelectedRoomId] = useState<string | null>(null);
  const [selectedEdgeId, setSelectedEdgeId] = useState<string | null>(null);

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

  return {
    selectedRoomId,
    selectedEdgeId,
    selectedRoom,
    selectedEdge,
    handleNodeClick,
    handleEdgeClick,
    setSelectedRoomId,
    setSelectedEdgeId,
  };
}

function resolveEditingEdgeData(editedEdges: Edge<ExitEdgeData>[], editingEdgeDataState: string | null) {
  if (!editingEdgeDataState) return undefined;
  const edge = editedEdges.find(e => e.id === editingEdgeDataState);
  if (!edge?.data) return undefined;
  return {
    edgeId: edge.id,
    sourceRoomId: edge.source,
    targetRoomId: edge.target,
    direction: edge.data.direction || '',
    flags: edge.data.flags,
    description: edge.data.description,
  };
}

function useRoomMapEditorModalState(rooms: Room[], editedEdges: Edge<ExitEdgeData>[]) {
  const [isEdgeCreationOpen, setIsEdgeCreationOpen] = useState(false);
  const [isEdgeEditOpen, setIsEdgeEditOpen] = useState(false);
  const [isRoomEditOpen, setIsRoomEditOpen] = useState(false);
  const [editingRoomId, setEditingRoomId] = useState<string | null>(null);
  const [editingEdgeDataState, setEditingEdgeDataState] = useState<string | null>(null);
  const [previewEdge, setPreviewEdge] = useState<Edge<ExitEdgeData> | null>(null);
  const [edgeValidation, setEdgeValidation] = useState<EdgeValidationResult | null>(null);

  const editingRoom = useMemo(
    () => (editingRoomId ? rooms.find(room => room.id === editingRoomId) || null : null),
    [editingRoomId, rooms]
  );
  const editingEdgeData = useMemo(
    () => resolveEditingEdgeData(editedEdges, editingEdgeDataState),
    [editedEdges, editingEdgeDataState]
  );

  const clearPreview = useCallback(() => {
    setPreviewEdge(null);
    setEdgeValidation(null);
  }, []);

  return {
    isEdgeCreationOpen,
    setIsEdgeCreationOpen,
    isEdgeEditOpen,
    setIsEdgeEditOpen,
    isRoomEditOpen,
    setIsRoomEditOpen,
    editingRoomId,
    setEditingRoomId,
    editingEdgeDataState,
    setEditingEdgeDataState,
    previewEdge,
    setPreviewEdge,
    edgeValidation,
    setEdgeValidation,
    editingRoom,
    editingEdgeData,
    clearPreview,
  };
}

function createRoomMapEditorModalActions(
  editing: RoomMapEditorEditingApi,
  selection: ReturnType<typeof useRoomMapEditorSelection>,
  modalState: ReturnType<typeof useRoomMapEditorModalState>
) {
  return {
    handleEditEdge: (edgeId: string) => {
      modalState.setEditingEdgeDataState(edgeId);
      modalState.setIsEdgeEditOpen(true);
    },
    handleEditRoom: (roomId: string) => {
      modalState.setEditingRoomId(roomId);
      modalState.setIsRoomEditOpen(true);
    },
    handleDeleteEdge: (edgeId: string) => {
      editing.deleteEdge(edgeId);
      selection.setSelectedEdgeId(null);
    },
    handleClosePanel: () => selection.setSelectedRoomId(null),
    handleCloseEdgePanel: () => selection.setSelectedEdgeId(null),
  };
}

function buildModalPreviewHandler(
  editing: RoomMapEditorEditingApi,
  modalState: ReturnType<typeof useRoomMapEditorModalState>
) {
  return (edgeData: EdgeCreationData | null) => {
    if (!edgeData) {
      modalState.clearPreview();
      return;
    }
    const { preview, validation } = buildPreviewEdge(edgeData, editing.validateEdgeCreation);
    modalState.setEdgeValidation(validation);
    modalState.setPreviewEdge(preview);
  };
}

function buildModalCreateEdgeHandler(
  editing: RoomMapEditorEditingApi,
  selection: ReturnType<typeof useRoomMapEditorSelection>,
  modalState: ReturnType<typeof useRoomMapEditorModalState>
) {
  return (edgeData: EdgeCreationData) => {
    editing.createEdge(edgeData);
    modalState.setIsEdgeCreationOpen(false);
    selection.setSelectedRoomId(null);
    modalState.clearPreview();
  };
}

function buildModalUpdateEdgeHandler(
  editing: RoomMapEditorEditingApi,
  modalState: ReturnType<typeof useRoomMapEditorModalState>
) {
  return (edgeId: string, edgeData: EdgeCreationData) => {
    editing.updateEdge(edgeId, {
      direction: edgeData.direction,
      flags: edgeData.flags,
      description: edgeData.description,
    });
    modalState.setIsEdgeEditOpen(false);
    modalState.setEditingEdgeDataState(null);
    modalState.clearPreview();
  };
}

function buildModalUpdateRoomHandler(
  editing: RoomMapEditorEditingApi,
  modalState: ReturnType<typeof useRoomMapEditorModalState>
) {
  return (roomId: string, updates: Partial<RoomNodeData>) => {
    editing.updateRoom(roomId, updates);
    modalState.setIsRoomEditOpen(false);
    modalState.setEditingRoomId(null);
  };
}

function useRoomMapEditorModalHandlers(
  editing: RoomMapEditorEditingApi,
  selection: ReturnType<typeof useRoomMapEditorSelection>,
  modalState: ReturnType<typeof useRoomMapEditorModalState>
) {
  const handlePreviewChange = useCallback(
    (edgeData: EdgeCreationData | null) => {
      buildModalPreviewHandler(editing, modalState)(edgeData);
    },
    [editing, modalState]
  );
  const handleCreateEdge = useCallback(
    (edgeData: EdgeCreationData) => {
      buildModalCreateEdgeHandler(editing, selection, modalState)(edgeData);
    },
    [editing, modalState, selection]
  );
  const handleUpdateEdge = useCallback(
    (edgeId: string, edgeData: EdgeCreationData) => {
      buildModalUpdateEdgeHandler(editing, modalState)(edgeId, edgeData);
    },
    [editing, modalState]
  );
  const handleUpdateRoom = useCallback(
    (roomId: string, updates: Partial<RoomNodeData>) => {
      buildModalUpdateRoomHandler(editing, modalState)(roomId, updates);
    },
    [editing, modalState]
  );

  return {
    handlePreviewChange,
    handleCreateEdge,
    handleUpdateEdge,
    handleUpdateRoom,
    ...createRoomMapEditorModalActions(editing, selection, modalState),
  };
}

function useRoomMapEditorModals(
  rooms: Room[],
  editedEdges: Edge<ExitEdgeData>[],
  editing: RoomMapEditorEditingApi,
  selection: ReturnType<typeof useRoomMapEditorSelection>
) {
  const modalState = useRoomMapEditorModalState(rooms, editedEdges);
  const handlers = useRoomMapEditorModalHandlers(editing, selection, modalState);
  return { ...modalState, ...handlers };
}

export { useRoomMapEditorData, useRoomMapEditorEditing, useRoomMapEditorModals, useRoomMapEditorSelection };
