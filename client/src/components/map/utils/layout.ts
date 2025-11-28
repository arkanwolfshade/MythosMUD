/**
 * Grid-based layout utilities for the map editor.
 *
 * This module provides utilities for arranging room nodes in a grid
 * layout, with support for zone/subzone grouping.
 *
 * As noted in the Cultes des Goules, proper spatial organization is
 * essential for understanding the dimensional relationships in our
 * eldritch architecture.
 */

import type { Node } from 'reactflow';
import type { RoomNodeData } from '../types';

/**
 * Grid layout configuration.
 */
export interface GridLayoutConfig {
  /** Grid cell width in pixels */
  cellWidth: number;
  /** Grid cell height in pixels */
  cellHeight: number;
  /** Horizontal spacing between cells */
  horizontalSpacing: number;
  /** Vertical spacing between cells */
  verticalSpacing: number;
  /** Whether to group by zone */
  groupByZone: boolean;
  /** Whether to group by subzone */
  groupBySubZone: boolean;
}

/**
 * Default grid layout configuration.
 */
export const defaultGridLayoutConfig: GridLayoutConfig = {
  cellWidth: 120,
  cellHeight: 120,
  horizontalSpacing: 50,
  verticalSpacing: 50,
  groupByZone: false,
  groupBySubZone: true,
};

/**
 * Calculate grid position for a node based on zone/subzone grouping.
 */
export const calculateGridPosition = (
  node: Node<RoomNodeData>,
  index: number,
  nodes: Node<RoomNodeData>[],
  config: GridLayoutConfig = defaultGridLayoutConfig
): { x: number; y: number } => {
  // If node has stored position, use it
  if (node.data && 'map_x' in node.data && 'map_y' in node.data) {
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    const mapX = (node.data as any).map_x;
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    const mapY = (node.data as any).map_y;
    if (mapX !== null && mapY !== null && mapX !== undefined && mapY !== undefined) {
      return { x: mapX, y: mapY };
    }
  }

  // Otherwise, calculate grid position
  const { cellWidth, cellHeight, horizontalSpacing, verticalSpacing, groupByZone, groupBySubZone } = config;

  if (groupBySubZone && node.data?.subZone) {
    // Group by subzone
    const subZoneNodes = nodes.filter(n => n.data?.subZone === node.data?.subZone);
    const subZoneIndex = subZoneNodes.findIndex(n => n.id === node.id);
    const subZoneCount = subZoneNodes.length;

    // Arrange in rows
    const colsPerRow = Math.ceil(Math.sqrt(subZoneCount));
    const row = Math.floor(subZoneIndex / colsPerRow);
    const col = subZoneIndex % colsPerRow;

    return {
      x: col * (cellWidth + horizontalSpacing),
      y: row * (cellHeight + verticalSpacing),
    };
  } else if (groupByZone && node.data?.zone) {
    // Group by zone
    const zoneNodes = nodes.filter(n => n.data?.zone === node.data?.zone);
    const zoneIndex = zoneNodes.findIndex(n => n.id === node.id);
    const zoneCount = zoneNodes.length;

    // Arrange in rows
    const colsPerRow = Math.ceil(Math.sqrt(zoneCount));
    const row = Math.floor(zoneIndex / colsPerRow);
    const col = zoneIndex % colsPerRow;

    return {
      x: col * (cellWidth + horizontalSpacing),
      y: row * (cellHeight + verticalSpacing),
    };
  } else {
    // Simple grid layout
    const colsPerRow = Math.ceil(Math.sqrt(nodes.length));
    const row = Math.floor(index / colsPerRow);
    const col = index % colsPerRow;

    return {
      x: col * (cellWidth + horizontalSpacing),
      y: row * (cellHeight + verticalSpacing),
    };
  }
};

/**
 * Apply grid layout to a set of nodes.
 */
export const applyGridLayout = (
  nodes: Node<RoomNodeData>[],
  config: GridLayoutConfig = defaultGridLayoutConfig
): Node<RoomNodeData>[] => {
  return nodes.map((node, index) => {
    const position = calculateGridPosition(node, index, nodes, config);
    return {
      ...node,
      position,
    };
  });
};
