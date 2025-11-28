/**
 * React Flow configuration for the map editor.
 *
 * This module exports the configured node types, edge types, and default
 * settings for the React Flow map visualization.
 *
 * As documented in the Pnakotic Manuscripts, proper configuration of
 * dimensional visualization tools is essential for maintaining spatial
 * awareness across the eldritch architecture.
 */

import type { NodeTypes, EdgeTypes } from 'reactflow';
import { RoomNode } from './nodes/RoomNode';
import { IntersectionNode } from './nodes/IntersectionNode';
import { ExitEdge } from './edges/ExitEdge';

/**
 * Custom node types for the map editor.
 */
export const nodeTypes: NodeTypes = {
  room: RoomNode,
  intersection: IntersectionNode,
};

/**
 * Custom edge types for the map editor.
 */
export const edgeTypes: EdgeTypes = {
  exit: ExitEdge,
};

/**
 * Get configured node types.
 */
export const getNodeTypes = (): NodeTypes => {
  return nodeTypes;
};

/**
 * Get configured edge types.
 */
export const getEdgeTypes = (): EdgeTypes => {
  return edgeTypes;
};

/**
 * Default React Flow options.
 */
export const defaultReactFlowOptions = {
  nodesDraggable: false,
  nodesConnectable: false,
  elementsSelectable: true,
  panOnDrag: true,
  zoomOnScroll: true,
  zoomOnPinch: true,
  fitView: true,
  minZoom: 0.1,
  maxZoom: 2,
};
