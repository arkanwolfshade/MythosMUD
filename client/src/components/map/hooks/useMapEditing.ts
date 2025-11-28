/**
 * React hook for managing map editing operations in admin mode.
 *
 * Handles node repositioning, edge creation/deletion, property editing,
 * validation, and undo/redo functionality.
 *
 * As documented in the Pnakotic Manuscripts, proper management of
 * dimensional modifications is essential for maintaining the integrity
 * of our eldritch architecture.
 */

import { useCallback, useRef, useState, useEffect } from 'react';
import type { Node, Edge } from 'reactflow';
import type { RoomNodeData, ExitEdgeData } from '../types';

export interface UseMapEditingOptions {
  /** Initial nodes */
  nodes: Node<RoomNodeData>[];
  /** Initial edges */
  edges: Edge<ExitEdgeData>[];
  /** Callback when save is requested */
  onSave?: (changes: MapEditingChanges) => Promise<void>;
}

export interface MapEditingChanges {
  /** Node position updates */
  nodePositions: Map<string, { x: number; y: number }>;
  /** New edges to create */
  newEdges: Edge<ExitEdgeData>[];
  /** Edges to delete */
  deletedEdgeIds: string[];
  /** Edge updates */
  edgeUpdates: Map<string, Partial<ExitEdgeData>>;
  /** Room property updates */
  roomUpdates: Map<string, Partial<RoomNodeData>>;
}

export interface EdgeCreationData {
  sourceRoomId: string;
  targetRoomId: string;
  direction: string;
  flags?: string[];
  description?: string;
}

export interface EdgeValidationResult {
  isValid: boolean;
  errors: string[];
  warnings: string[];
}

export interface UseMapEditingResult {
  /** Current nodes with edits applied */
  nodes: Node<RoomNodeData>[];
  /** Current edges with edits applied */
  edges: Edge<ExitEdgeData>[];
  /** Whether there are unsaved changes */
  hasUnsavedChanges: boolean;
  /** Whether undo is available */
  canUndo: boolean;
  /** Whether redo is available */
  canRedo: boolean;
  /** Update a node's position */
  updateNodePosition: (nodeId: string, position: { x: number; y: number }) => void;
  /** Create a new edge */
  createEdge: (edgeData: EdgeCreationData) => void;
  /** Delete an edge */
  deleteEdge: (edgeId: string) => void;
  /** Update edge properties */
  updateEdge: (edgeId: string, updates: Partial<ExitEdgeData>) => void;
  /** Update room properties */
  updateRoom: (roomId: string, updates: Partial<RoomNodeData>) => void;
  /** Validate edge creation */
  validateEdgeCreation: (edgeData: EdgeCreationData) => EdgeValidationResult;
  /** Undo last operation */
  undo: () => void;
  /** Redo last undone operation */
  redo: () => void;
  /** Save all changes */
  save: () => Promise<void>;
  /** Reset to initial state */
  reset: () => void;
}

/**
 * History entry for undo/redo.
 */
interface HistoryEntry {
  nodes: Node<RoomNodeData>[];
  edges: Edge<ExitEdgeData>[];
}

/**
 * Hook for managing map editing operations.
 *
 * @param options - Configuration options for editing
 * @returns Editing state and operations
 */
export function useMapEditing(options: UseMapEditingOptions): UseMapEditingResult {
  const { nodes: initialNodes, edges: initialEdges, onSave } = options;

  const [nodes, setNodes] = useState<Node<RoomNodeData>[]>(initialNodes);
  const [edges, setEdges] = useState<Edge<ExitEdgeData>[]>(initialEdges);
  const [hasUnsavedChanges, setHasUnsavedChanges] = useState(false);
  const [canUndo, setCanUndo] = useState(false);
  const [canRedo, setCanRedo] = useState(false);

  // Undo/redo history - initialize with initial state
  const historyRef = useRef<HistoryEntry[]>([
    {
      nodes: JSON.parse(JSON.stringify(initialNodes)),
      edges: JSON.parse(JSON.stringify(initialEdges)),
    },
  ]);
  const historyIndexRef = useRef<number>(0);
  const maxHistorySize = 50;

  // Track changes
  const nodePositionChangesRef = useRef<Map<string, { x: number; y: number }>>(new Map());
  const newEdgesRef = useRef<Edge<ExitEdgeData>[]>([]);
  const deletedEdgeIdsRef = useRef<Set<string>>(new Set());
  const edgeUpdatesRef = useRef<Map<string, Partial<ExitEdgeData>>>(new Map());
  const roomUpdatesRef = useRef<Map<string, Partial<RoomNodeData>>>(new Map());

  // Save current state to history
  const saveToHistory = useCallback((currentNodes: Node<RoomNodeData>[], currentEdges: Edge<ExitEdgeData>[]) => {
    const entry: HistoryEntry = {
      nodes: JSON.parse(JSON.stringify(currentNodes)),
      edges: JSON.parse(JSON.stringify(currentEdges)),
    };

    // Remove any history after current index (when undoing and then making new changes)
    if (historyIndexRef.current < historyRef.current.length - 1) {
      historyRef.current = historyRef.current.slice(0, historyIndexRef.current + 1);
    }

    historyRef.current.push(entry);
    historyIndexRef.current = historyRef.current.length - 1;

    // Limit history size
    if (historyRef.current.length > maxHistorySize) {
      historyRef.current.shift();
      historyIndexRef.current--;
    }

    // Update undo/redo state
    setCanUndo(historyIndexRef.current > 0);
    setCanRedo(historyIndexRef.current < historyRef.current.length - 1);
  }, []);

  // Update node position
  const updateNodePosition = useCallback(
    (nodeId: string, position: { x: number; y: number }) => {
      setNodes(currentNodes => {
        const updated = currentNodes.map(node => {
          if (node.id === nodeId) {
            nodePositionChangesRef.current.set(nodeId, position);
            return {
              ...node,
              position,
              data: {
                ...node.data,
                hasUnsavedChanges: true,
              },
            };
          }
          return node;
        });
        saveToHistory(updated, edges);
        return updated;
      });
      setHasUnsavedChanges(true);
    },
    [edges, saveToHistory]
  );

  // Validate edge creation
  const validateEdgeCreation = useCallback(
    (edgeData: EdgeCreationData): EdgeValidationResult => {
      const errors: string[] = [];
      const warnings: string[] = [];

      // Check if target room exists
      const targetExists = nodes.some(node => node.id === edgeData.targetRoomId);
      if (!targetExists) {
        errors.push('Target room does not exist');
      }

      // Check if source room exists
      const sourceExists = nodes.some(node => node.id === edgeData.sourceRoomId);
      if (!sourceExists) {
        errors.push('Source room does not exist');
      }

      // Check for duplicate edge
      const duplicateExists = edges.some(
        edge =>
          edge.source === edgeData.sourceRoomId &&
          edge.target === edgeData.targetRoomId &&
          edge.data?.direction === edgeData.direction
      );
      if (duplicateExists) {
        errors.push('An edge with this direction already exists');
      }

      // Check for bidirectional pairing
      const reverseEdge = edges.find(
        edge => edge.source === edgeData.targetRoomId && edge.target === edgeData.sourceRoomId
      );
      if (!reverseEdge && !edgeData.flags?.includes('one_way')) {
        warnings.push('No reverse edge found. Consider creating a bidirectional connection.');
      }

      return {
        isValid: errors.length === 0,
        errors,
        warnings,
      };
    },
    [nodes, edges]
  );

  // Create a new edge
  const createEdge = useCallback(
    (edgeData: EdgeCreationData) => {
      const validation = validateEdgeCreation(edgeData);
      if (!validation.isValid) {
        throw new Error(`Invalid edge: ${validation.errors.join(', ')}`);
      }

      const newEdge: Edge<ExitEdgeData> = {
        id: `${edgeData.sourceRoomId}-${edgeData.direction}-${edgeData.targetRoomId}`,
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
      };

      setEdges(currentEdges => {
        const updated = [...currentEdges, newEdge];
        newEdgesRef.current.push(newEdge);
        saveToHistory(nodes, updated);
        return updated;
      });
      setHasUnsavedChanges(true);
    },
    [nodes, validateEdgeCreation, saveToHistory]
  );

  // Delete an edge
  const deleteEdge = useCallback(
    (edgeId: string) => {
      setEdges(currentEdges => {
        const updated = currentEdges.filter(edge => edge.id !== edgeId);
        deletedEdgeIdsRef.current.add(edgeId);
        saveToHistory(nodes, updated);
        return updated;
      });
      setHasUnsavedChanges(true);
    },
    [nodes, saveToHistory]
  );

  // Update edge properties
  const updateEdge = useCallback(
    (edgeId: string, updates: Partial<ExitEdgeData>) => {
      setEdges(currentEdges => {
        const updated = currentEdges.map(edge => {
          if (edge.id === edgeId) {
            const currentUpdates = edgeUpdatesRef.current.get(edgeId) || {};
            edgeUpdatesRef.current.set(edgeId, { ...currentUpdates, ...updates });
            return {
              ...edge,
              data: {
                ...edge.data,
                ...updates,
              } as ExitEdgeData,
            };
          }
          return edge;
        });
        saveToHistory(nodes, updated);
        return updated;
      });
      setHasUnsavedChanges(true);
    },
    [nodes, saveToHistory]
  );

  // Update room properties
  const updateRoom = useCallback(
    (roomId: string, updates: Partial<RoomNodeData>) => {
      setNodes(currentNodes => {
        const updated = currentNodes.map(node => {
          if (node.id === roomId) {
            const currentUpdates = roomUpdatesRef.current.get(roomId) || {};
            roomUpdatesRef.current.set(roomId, { ...currentUpdates, ...updates });
            return {
              ...node,
              data: {
                ...node.data,
                ...updates,
                hasUnsavedChanges: true,
              },
            };
          }
          return node;
        });
        saveToHistory(updated, edges);
        return updated;
      });
      setHasUnsavedChanges(true);
    },
    [edges, saveToHistory]
  );

  // Undo
  const undo = useCallback(() => {
    if (historyIndexRef.current > 0) {
      historyIndexRef.current--;
      const entry = historyRef.current[historyIndexRef.current];
      setNodes(entry.nodes);
      setEdges(entry.edges);
      setHasUnsavedChanges(historyIndexRef.current !== 0);
      setCanUndo(historyIndexRef.current > 0);
      setCanRedo(historyIndexRef.current < historyRef.current.length - 1);
    }
  }, []);

  // Redo
  const redo = useCallback(() => {
    if (historyIndexRef.current < historyRef.current.length - 1) {
      historyIndexRef.current++;
      const entry = historyRef.current[historyIndexRef.current];
      setNodes(entry.nodes);
      setEdges(entry.edges);
      setHasUnsavedChanges(historyIndexRef.current !== 0);
      setCanUndo(historyIndexRef.current > 0);
      setCanRedo(historyIndexRef.current < historyRef.current.length - 1);
    }
  }, []);

  // Save changes
  const save = useCallback(async () => {
    if (!onSave) {
      return;
    }

    const changes: MapEditingChanges = {
      nodePositions: nodePositionChangesRef.current,
      newEdges: newEdgesRef.current,
      deletedEdgeIds: Array.from(deletedEdgeIdsRef.current),
      edgeUpdates: edgeUpdatesRef.current,
      roomUpdates: roomUpdatesRef.current,
    };

    await onSave(changes);

    // Clear change tracking after successful save
    nodePositionChangesRef.current.clear();
    newEdgesRef.current = [];
    deletedEdgeIdsRef.current.clear();
    edgeUpdatesRef.current.clear();
    roomUpdatesRef.current.clear();
    setHasUnsavedChanges(false);
  }, [onSave]);

  // Reset to initial state
  const reset = useCallback(() => {
    setNodes(initialNodes);
    setEdges(initialEdges);
    nodePositionChangesRef.current.clear();
    newEdgesRef.current = [];
    deletedEdgeIdsRef.current.clear();
    edgeUpdatesRef.current.clear();
    roomUpdatesRef.current.clear();
    historyRef.current = [
      {
        nodes: JSON.parse(JSON.stringify(initialNodes)),
        edges: JSON.parse(JSON.stringify(initialEdges)),
      },
    ];
    historyIndexRef.current = 0;
    setCanUndo(false);
    setCanRedo(false);
    setHasUnsavedChanges(false);
  }, [initialNodes, initialEdges]);

  // Initialize undo/redo state
  useEffect(() => {
    setCanUndo(historyIndexRef.current > 0);
    setCanRedo(historyIndexRef.current < historyRef.current.length - 1);
  }, []);

  return {
    nodes,
    edges,
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
  };
}
