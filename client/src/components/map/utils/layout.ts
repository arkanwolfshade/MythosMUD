/**
 * Layout utilities for the map editor.
 *
 * This module provides utilities for arranging room nodes using various
 * layout algorithms, with support for minimizing edge crossings.
 *
 * As noted in the Cultes des Goules, proper spatial organization is
 * essential for understanding the dimensional relationships in our
 * eldritch architecture. The force-directed layout minimizes edge crossings
 * as documented in the Pnakotic Manuscripts' section on graph visualization.
 */

import type { Edge, Node } from 'reactflow';
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
 * Force-directed layout configuration optimized for minimizing edge crossings.
 */
export interface ForceLayoutConfig {
  /** Ideal distance between connected nodes */
  linkDistance: number;
  /** Strength of repulsive force between nodes */
  chargeStrength: number;
  /** Strength of centering force */
  centerStrength: number;
  /** Number of iterations to run the simulation */
  iterations: number;
  /** Damping factor for the simulation */
  damping: number;
  /** Minimum distance between nodes (node radius * 2 + padding) */
  minDistance: number;
  /** Node radius for collision detection */
  nodeRadius: number;
  /** Strength of collision force when nodes overlap */
  collisionStrength: number;
  /** Whether to use edge-crossing minimization */
  minimizeCrossings: boolean;
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
 * Default force-directed layout configuration optimized for minimizing crossings.
 */
export const defaultForceLayoutConfig: ForceLayoutConfig = {
  linkDistance: 200,
  chargeStrength: -1200,
  centerStrength: 0.05,
  iterations: 400,
  damping: 0.85,
  minDistance: 120, // Node width/height (100px) + padding (20px)
  nodeRadius: 50, // Half of typical node size
  collisionStrength: 2.0, // Strong collision force to prevent overlap
  minimizeCrossings: true,
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
 * Apply force-directed layout to minimize edge crossings.
 * This uses a physics simulation to position nodes optimally.
 */
export const applyForceLayout = (
  nodes: Node<RoomNodeData>[],
  edges: Edge[],
  config: ForceLayoutConfig = defaultForceLayoutConfig
): Node<RoomNodeData>[] => {
  if (nodes.length === 0) {
    return nodes;
  }

  // Initialize positions if not set - spread nodes in a wider pattern to avoid initial overlaps
  const positionedNodes = nodes.map((node, index) => {
    // Check if node has a meaningful position (not just at origin)
    const hasPosition = !(node.position.x === 0 && node.position.y === 0) || index === 0;

    if (!hasPosition) {
      // Spread initial positions in a wider circle/spiral pattern
      // Use a spiral to ensure nodes are well-separated initially
      const angle = (index * 2.4 * Math.PI) / Math.sqrt(nodes.length); // Golden angle approximation
      const radius = Math.sqrt(index) * (config.minDistance * 1.5); // Spiral outward
      return {
        ...node,
        position: {
          x: Math.cos(angle) * radius,
          y: Math.sin(angle) * radius,
        },
      };
    }
    return node;
  });

  // Create node map for quick lookup
  const nodeMap = new Map(
    positionedNodes.map(n => [
      n.id,
      {
        id: n.id,
        x: n.position.x,
        y: n.position.y,
        vx: 0,
        vy: 0,
      },
    ])
  );

  // Create edge list with node references, filtering out edges with missing nodes
  const edgeList = edges
    .filter(edge => {
      const source = nodeMap.get(edge.source);
      const target = nodeMap.get(edge.target);
      return source && target;
    })
    .map(edge => {
      const source = nodeMap.get(edge.source)!;
      const target = nodeMap.get(edge.target)!;
      return { source, target };
    });

  // Run force simulation
  for (let iteration = 0; iteration < config.iterations; iteration++) {
    // Reset forces
    for (const node of nodeMap.values()) {
      node.vx = 0;
      node.vy = 0;
    }

    // Apply link forces (attraction between connected nodes)
    for (const edge of edgeList) {
      const dx = edge.target.x - edge.source.x;
      const dy = edge.target.y - edge.source.y;
      const distance = Math.sqrt(dx * dx + dy * dy) || 1;
      const force = (distance - config.linkDistance) * 0.1;

      const fx = (dx / distance) * force;
      const fy = (dy / distance) * force;

      edge.source.vx += fx;
      edge.source.vy += fy;
      edge.target.vx -= fx;
      edge.target.vy -= fy;
    }

    // Apply charge forces and collision avoidance (repulsion between all nodes)
    const nodesArray = Array.from(nodeMap.values());
    for (let i = 0; i < nodesArray.length; i++) {
      for (let j = i + 1; j < nodesArray.length; j++) {
        const node1 = nodesArray[i];
        const node2 = nodesArray[j];

        const dx = node2.x - node1.x;
        const dy = node2.y - node1.y;
        const distance = Math.sqrt(dx * dx + dy * dy) || 0.1; // Avoid division by zero

        // Strong collision force when nodes are too close (prevents overlap)
        if (distance < config.minDistance) {
          // Calculate overlap amount
          const overlap = config.minDistance - distance;
          // Apply strong repulsive force proportional to overlap
          const force = overlap * config.collisionStrength;
          const fx = (dx / distance) * force;
          const fy = (dy / distance) * force;
          node1.vx -= fx;
          node1.vy -= fy;
          node2.vx += fx;
          node2.vy += fy;
        } else {
          // Standard repulsive force (inverse square law)
          // Use a smoother falloff to prevent sudden jumps
          const force = config.chargeStrength / (distance * distance + 1);
          const fx = (dx / distance) * force;
          const fy = (dy / distance) * force;
          node1.vx -= fx;
          node1.vy -= fy;
          node2.vx += fx;
          node2.vy += fy;
        }
      }
    }

    // Apply center force
    const centerX = 0;
    const centerY = 0;
    for (const node of nodeMap.values()) {
      node.vx += (centerX - node.x) * config.centerStrength;
      node.vy += (centerY - node.y) * config.centerStrength;
    }

    // Update positions with damping
    for (const node of nodeMap.values()) {
      node.x += node.vx * config.damping;
      node.y += node.vy * config.damping;
    }
  }

  // Convert back to React Flow nodes
  return positionedNodes.map(node => {
    const positioned = nodeMap.get(node.id);
    if (positioned) {
      return {
        ...node,
        position: {
          x: positioned.x,
          y: positioned.y,
        },
      };
    }
    return node;
  });
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
