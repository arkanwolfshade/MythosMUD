/**
 * React hook for managing map layout and positioning.
 *
 * Handles grid-based layout calculation, manual positioning persistence,
 * and performance optimizations for the map editor.
 *
 * As documented in the Pnakotic Manuscripts, proper layout management is
 * essential for maintaining the integrity of our dimensional mappings.
 */

import { useCallback, useMemo, useRef, useState } from 'react';
import type { Node } from 'reactflow';
import type { RoomNodeData } from '../types';
import { applyGridLayout, type GridLayoutConfig, defaultGridLayoutConfig } from '../utils/layout';
import { debounce } from '../utils/performance';

export interface UseMapLayoutOptions {
  /** Initial nodes to layout */
  nodes: Node<RoomNodeData>[];
  /** Grid layout configuration */
  config?: Partial<GridLayoutConfig>;
  /** Whether to use stored coordinates from database */
  useStoredCoordinates?: boolean;
  /** Callback when positions are saved */
  onSave?: (positions: Map<string, { x: number; y: number }>) => Promise<void>;
  /** Debounce delay for layout recalculations (ms) */
  debounceDelay?: number;
}

export interface UseMapLayoutResult {
  /** Nodes with calculated positions */
  layoutNodes: Node<RoomNodeData>[];
  /** Whether there are unsaved position changes */
  hasUnsavedChanges: boolean;
  /** Function to update a node's position */
  updateNodePosition: (nodeId: string, position: { x: number; y: number }) => void;
  /** Function to save positions to database */
  savePositions: () => Promise<void>;
  /** Function to reset positions to auto-layout */
  resetToAutoLayout: () => void;
  /** Function to apply grid layout to all nodes */
  applyGridLayout: () => void;
}

/**
 * Hook for managing map layout and positioning.
 *
 * @param options - Configuration options for layout management
 * @returns Layout nodes, position management functions, and save/reset functions
 */
export function useMapLayout(options: UseMapLayoutOptions): UseMapLayoutResult {
  const { nodes: initialNodes, config = {}, useStoredCoordinates = true, onSave, debounceDelay = 300 } = options;

  // Memoize layout config to prevent unnecessary re-renders
  const layoutConfig: GridLayoutConfig = useMemo(
    () => ({
      ...defaultGridLayoutConfig,
      ...config,
    }),
    [config]
  );

  // Track nodes with their positions
  const [nodes, setNodes] = useState<Node<RoomNodeData>[]>(initialNodes);
  const [hasUnsavedChanges, setHasUnsavedChanges] = useState(false);

  // Track manual position changes
  const manualPositionsRef = useRef<Map<string, { x: number; y: number }>>(new Map());

  // Debounced layout recalculation function
  const debouncedLayoutRecalc = useMemo(
    () =>
      debounce(() => {
        // Layout recalculation can happen here if needed
        // This is a placeholder for future optimizations
      }, debounceDelay),
    [debounceDelay]
  );

  // Update nodes when initialNodes change
  useMemo(() => {
    if (initialNodes.length !== nodes.length || initialNodes.some((n, i) => n.id !== nodes[i]?.id)) {
      setNodes(initialNodes);
      manualPositionsRef.current.clear();
      setHasUnsavedChanges(false);
    }
  }, [initialNodes, nodes]);

  // Calculate layout nodes with stored coordinates or grid layout
  const layoutNodes = useMemo(() => {
    // First, apply grid layout to nodes that don't have stored coordinates
    const nodesWithLayout = applyGridLayout(nodes, layoutConfig);

    return nodesWithLayout.map(node => {
      // Check if node has stored coordinates and we should use them
      if (useStoredCoordinates && node.data) {
        const roomData = node.data as RoomNodeData & { map_x?: number | null; map_y?: number | null };
        if (
          roomData.map_x !== null &&
          roomData.map_x !== undefined &&
          roomData.map_y !== null &&
          roomData.map_y !== undefined &&
          !manualPositionsRef.current.has(node.id)
        ) {
          return {
            ...node,
            position: { x: roomData.map_x, y: roomData.map_y },
            data: {
              ...node.data,
              hasUnsavedChanges: false,
            },
          };
        }
      }

      // Check if node has manual position override (takes precedence)
      if (manualPositionsRef.current.has(node.id)) {
        const manualPos = manualPositionsRef.current.get(node.id)!;
        return {
          ...node,
          position: manualPos,
          data: {
            ...node.data,
            hasUnsavedChanges: true,
          },
        };
      }

      // Use grid layout position
      return node;
    });
  }, [nodes, useStoredCoordinates, layoutConfig]);

  // Apply grid layout to all nodes
  const applyGridLayoutToNodes = useCallback(() => {
    setNodes(currentNodes => {
      const layoutedNodes = applyGridLayout(currentNodes, layoutConfig);
      // Clear manual positions when applying grid layout
      manualPositionsRef.current.clear();
      setHasUnsavedChanges(false);
      return layoutedNodes;
    });
  }, [layoutConfig]);

  // Update a single node's position
  const updateNodePosition = useCallback(
    (nodeId: string, position: { x: number; y: number }) => {
      // Store manual position
      manualPositionsRef.current.set(nodeId, position);

      // Update node position
      setNodes(currentNodes =>
        currentNodes.map(node => {
          if (node.id === nodeId) {
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
        })
      );

      setHasUnsavedChanges(true);

      // Trigger debounced layout recalculation
      debouncedLayoutRecalc();
    },
    [debouncedLayoutRecalc]
  );

  // Save positions to database
  const savePositions = useCallback(async () => {
    if (!onSave || manualPositionsRef.current.size === 0) {
      return;
    }

    setIsSaving(true);
    try {
      await onSave(manualPositionsRef.current);
      // Clear unsaved changes flag after successful save
      setHasUnsavedChanges(false);
      // Update nodes to mark positions as saved
      setNodes(currentNodes =>
        currentNodes.map(node => {
          if (manualPositionsRef.current.has(node.id)) {
            return {
              ...node,
              data: {
                ...node.data,
                hasUnsavedChanges: false,
              },
            };
          }
          return node;
        })
      );
    } catch (error) {
      console.error('Failed to save positions:', error);
      throw error;
    } finally {
      setIsSaving(false);
    }
  }, [onSave]);

  // Reset to auto-layout
  const resetToAutoLayout = useCallback(() => {
    manualPositionsRef.current.clear();
    setHasUnsavedChanges(false);
    applyGridLayoutToNodes();
  }, [applyGridLayoutToNodes]);

  return {
    layoutNodes,
    hasUnsavedChanges,
    updateNodePosition,
    savePositions,
    resetToAutoLayout,
    applyGridLayout: applyGridLayoutToNodes,
  };
}
