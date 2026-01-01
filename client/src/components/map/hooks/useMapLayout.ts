/**
 * React hook for managing map layout and positioning.
 *
 * Handles grid-based layout calculation, manual positioning persistence,
 * and performance optimizations for the map editor.
 *
 * As documented in the Pnakotic Manuscripts, proper layout management is
 * essential for maintaining the integrity of our dimensional mappings.
 */

import { useCallback, useEffect, useMemo, useRef, useState } from 'react';
import type { Edge, Node } from 'reactflow';
import type { RoomNodeData } from '../types';
import {
  applyForceLayout,
  applyGridLayout,
  defaultForceLayoutConfig,
  defaultGridLayoutConfig,
  type ForceLayoutConfig,
  type GridLayoutConfig,
} from '../utils/layout';
import { debounce } from '../utils/performance';

export interface UseMapLayoutOptions {
  /** Initial nodes to layout */
  nodes: Node<RoomNodeData>[];
  /** Edges for force-directed layout (required for crossing minimization) */
  edges?: Edge[];
  /** Grid layout configuration */
  config?: Partial<GridLayoutConfig>;
  /** Force layout configuration */
  forceConfig?: Partial<ForceLayoutConfig>;
  /** Layout algorithm to use */
  layoutAlgorithm?: 'grid' | 'force';
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
  const {
    nodes: initialNodes,
    edges = [],
    config = {},
    forceConfig = {},
    layoutAlgorithm = 'force',
    useStoredCoordinates = true,
    onSave,
    debounceDelay = 300,
  } = options;

  // Memoize layout configs to prevent unnecessary re-renders
  const layoutConfig: GridLayoutConfig = useMemo(
    () => ({
      ...defaultGridLayoutConfig,
      ...config,
    }),
    [config]
  );

  const forceLayoutConfig: ForceLayoutConfig = useMemo(
    () => ({
      ...defaultForceLayoutConfig,
      ...forceConfig,
    }),
    [forceConfig]
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
  useEffect(() => {
    if (initialNodes.length !== nodes.length || initialNodes.some((n, i) => n.id !== nodes[i]?.id)) {
      setNodes(initialNodes);
      manualPositionsRef.current.clear();
      setHasUnsavedChanges(false);
    }
  }, [initialNodes, nodes]);

  // Calculate layout nodes with stored coordinates or auto layout
  // Accessing refs in useMemo is safe; refs don't cause re-renders and this is intentional for performance
  /* eslint-disable react-hooks/refs */
  const layoutNodes = useMemo(() => {
    // Determine which nodes need auto-layout (don't have stored or manual positions)
    const nodesNeedingLayout = nodes.filter(node => {
      // Skip if has manual position
      if (manualPositionsRef.current.has(node.id)) {
        return false;
      }

      // Skip if has stored coordinates and we should use them
      if (useStoredCoordinates && node.data) {
        const roomData = node.data as RoomNodeData & { map_x?: number | null; map_y?: number | null };
        if (
          roomData.map_x !== null &&
          roomData.map_x !== undefined &&
          roomData.map_y !== null &&
          roomData.map_y !== undefined
        ) {
          return false;
        }
      }

      return true;
    });

    // Apply appropriate layout algorithm to nodes that need it
    let nodesWithLayout: Node<RoomNodeData>[];
    if (layoutAlgorithm === 'force' && edges.length > 0 && nodesNeedingLayout.length > 0) {
      // Use force-directed layout for crossing minimization
      nodesWithLayout = applyForceLayout(nodesNeedingLayout, edges, forceLayoutConfig);
    } else {
      // Fall back to grid layout
      nodesWithLayout = applyGridLayout(nodesNeedingLayout, layoutConfig);
    }

    // Create a map of auto-laid-out positions
    const autoLayoutMap = new Map(nodesWithLayout.map(n => [n.id, n.position]));

    // Combine all nodes with their appropriate positions
    const result = nodes.map(node => {
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

      // Use auto-layout position
      const autoPos = autoLayoutMap.get(node.id);
      if (autoPos) {
        return {
          ...node,
          position: autoPos,
        };
      }

      // Fallback: use existing position
      return node;
    });

    return result;
  }, [nodes, edges, useStoredCoordinates, layoutConfig, forceLayoutConfig, layoutAlgorithm]);
  /* eslint-enable react-hooks/refs */

  // Apply auto layout to all nodes
  const applyGridLayoutToNodes = useCallback(() => {
    setNodes(currentNodes => {
      let layoutedNodes: Node<RoomNodeData>[];
      if (layoutAlgorithm === 'force' && edges.length > 0) {
        layoutedNodes = applyForceLayout(currentNodes, edges, forceLayoutConfig);
      } else {
        layoutedNodes = applyGridLayout(currentNodes, layoutConfig);
      }
      // Clear manual positions when applying auto layout
      manualPositionsRef.current.clear();
      setHasUnsavedChanges(false);
      return layoutedNodes;
    });
  }, [layoutConfig, forceLayoutConfig, layoutAlgorithm, edges]);

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
