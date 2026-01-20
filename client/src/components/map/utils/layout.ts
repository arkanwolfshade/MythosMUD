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
import type { ExitEdgeData, RoomNodeData } from '../types';

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
  iterations: 800, // Increased to 800 to allow more time for crossing minimization to converge
  damping: 0.9, // Increased from 0.85 to 0.9 to reduce velocity loss and allow more movement
  minDistance: 120, // Node size (80px) + padding (40px) - increased to ensure no visual overlap
  nodeRadius: 50, // Half of typical node size
  collisionStrength: 8.0, // Increased from 2.0 to 8.0 - much stronger force to prevent overlap
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
    // Node data structure varies by node type, runtime check ensures map_x/map_y exist but
    // TypeScript cannot infer type
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    const mapX = (node.data as any).map_x;
    // Node data structure varies by node type, runtime check ensures map_x/map_y exist but
    // TypeScript cannot infer type
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

    const position = {
      x: col * (cellWidth + horizontalSpacing),
      y: row * (cellHeight + verticalSpacing),
    };
    return position;
  }
};

/**
 * Node state for force simulation.
 */
interface NodeState {
  id: string;
  x: number;
  y: number;
  vx: number;
  vy: number;
}

/**
 * Initialize node positions in a spiral pattern to avoid initial overlaps.
 */
const initializeNodePositions = (nodes: Node<RoomNodeData>[], minDistance: number): Node<RoomNodeData>[] => {
  return nodes.map((node, index) => {
    // Check if node has a meaningful position (not just at origin)
    // Fixed: removed `|| index === 0` which was preventing first node from being initialized
    const hasPosition = !(node.position.x === 0 && node.position.y === 0);

    if (!hasPosition) {
      // Spread initial positions in a wider circle/spiral pattern
      // Use a spiral to ensure nodes are well-separated initially
      const angle = (index * 2.4 * Math.PI) / Math.sqrt(nodes.length); // Golden angle approximation
      const radius = Math.sqrt(index) * (minDistance * 2.0); // Increased from 1.5 to 2.0 for better initial separation
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
};

/**
 * Apply link forces with directional constraints based on exit directions.
 *
 * Positioning rules based on canvas orientation (top=north, bottom=south, right=east, left=west):
 * - If source has a southern exit to target, source should be NORTH of target (source.y < target.y)
 * - If source has a northern exit to target, source should be SOUTH of target (source.y > target.y)
 * - If source has an eastern exit to target, source should be WEST of target (source.x < target.x)
 * - If source has a western exit to target, source should be EAST of target (source.x > target.x)
 */
const applyLinkForces = (
  edgeList: Array<{ source: NodeState; target: NodeState; direction?: string }>,
  linkDistance: number
): void => {
  for (const edge of edgeList) {
    const dx = edge.target.x - edge.source.x;
    const dy = edge.target.y - edge.source.y;
    const distance = Math.sqrt(dx * dx + dy * dy) || 1;

    let fx: number;
    let fy: number;

    // Apply directional forces based on exit direction if available
    if (edge.direction) {
      const direction = edge.direction.toLowerCase();
      let desiredDx = 0;
      let desiredDy = 0;

      // Calculate desired relative position based on direction
      // Canvas orientation: top=north, bottom=south, right=east, left=west
      switch (direction) {
        case 'north':
          // Source exits NORTH to target, so source should be SOUTH of target
          // source.y > target.y (south = larger y), so dy < 0, desiredDy = -linkDistance
          desiredDy = -linkDistance;
          break;
        case 'south':
          // Source exits SOUTH to target, so source should be NORTH of target
          // source.y < target.y (north = smaller y), so dy > 0, desiredDy = linkDistance
          desiredDy = linkDistance;
          break;
        case 'east':
          // Source exits EAST to target, so source should be WEST of target
          // source.x < target.x (west = smaller x), so dx > 0, desiredDx = linkDistance
          desiredDx = linkDistance;
          break;
        case 'west':
          // Source exits WEST to target, so source should be EAST of target
          // source.x > target.x (east = larger x), so dx < 0, desiredDx = -linkDistance
          desiredDx = -linkDistance;
          break;
        default: {
          // For other directions (up, down, diagonals), use standard attraction
          const force = (distance - linkDistance) * 0.1;
          fx = (dx / distance) * force;
          fy = (dy / distance) * force;
          edge.source.vx += fx;
          edge.source.vy += fy;
          edge.target.vx -= fx;
          edge.target.vy -= fy;
          continue;
        }
      }

      // Apply gentle directional nudge instead of strong error-based force
      // This prevents force explosion when nodes are far apart
      // Normalize desired direction to unit vector
      const desiredLength = Math.sqrt(desiredDx * desiredDx + desiredDy * desiredDy);
      if (desiredLength > 0) {
        const desiredUnitX = desiredDx / desiredLength;
        const desiredUnitY = desiredDy / desiredLength;

        // Apply a gentle force in the desired direction, scaled by linkDistance
        // This gives a gentle nudge without exploding when nodes are far apart
        const directionalStrength = 0.02; // Much weaker to prevent instability
        fx = desiredUnitX * linkDistance * directionalStrength;
        fy = desiredUnitY * linkDistance * directionalStrength;
      } else {
        fx = 0;
        fy = 0;
      }

      // Also apply standard distance maintenance force (this is stable)
      // But reduce link force strength when nodes are too close to prevent overlap
      const distanceError = distance - linkDistance;
      const baseDistanceForce = distanceError * 0.05;
      // Reduce link force when nodes are closer than minDistance to allow collision forces to work
      const minDistanceForLink = 120; // Match minDistance from config
      const linkForceReduction = distance < minDistanceForLink ? Math.max(0.1, distance / minDistanceForLink) : 1.0;
      const distanceForce = baseDistanceForce * linkForceReduction;
      fx += (dx / distance) * distanceForce;
      fy += (dy / distance) * distanceForce;
    } else {
      // No direction specified - use standard attraction
      // But reduce link force when nodes are too close to prevent overlap
      const baseForce = (distance - linkDistance) * 0.1;
      const minDistanceForLink = 120; // Match minDistance from config
      const linkForceReduction = distance < minDistanceForLink ? Math.max(0.1, distance / minDistanceForLink) : 1.0;
      const force = baseForce * linkForceReduction;
      fx = (dx / distance) * force;
      fy = (dy / distance) * force;
    }

    edge.source.vx += fx;
    edge.source.vy += fy;
    edge.target.vx -= fx;
    edge.target.vy -= fy;
  }
};

/**
 * Apply collision forces when nodes are too close.
 */
const applyCollisionForces = (
  node1: NodeState,
  node2: NodeState,
  minDistance: number,
  collisionStrength: number
): void => {
  const dx = node2.x - node1.x;
  const dy = node2.y - node1.y;
  let distance = Math.sqrt(dx * dx + dy * dy);

  // If nodes are exactly on top of each other (distance = 0 or very small), add a small random offset
  // to break the symmetry and allow separation. Use a larger threshold to catch more cases.
  if (distance < 1.0) {
    const angle = Math.random() * Math.PI * 2;
    const offset = minDistance * 0.2; // Increased from 0.1 to 0.2 for stronger initial separation
    node1.x -= Math.cos(angle) * offset;
    node1.y -= Math.sin(angle) * offset;
    node2.x += Math.cos(angle) * offset;
    node2.y += Math.sin(angle) * offset;
    // Recalculate distance after offset
    const newDx = node2.x - node1.x;
    const newDy = node2.y - node1.y;
    distance = Math.sqrt(newDx * newDx + newDy * newDy);
  }

  if (distance < minDistance) {
    // Calculate overlap amount
    const overlap = minDistance - distance;
    // Apply strong repulsive force - use quadratic scaling for severe overlaps
    // This makes the force much stronger when nodes are very close
    const forceMultiplier = overlap > 20 ? overlap * 1.5 : overlap; // Extra boost for severe overlaps
    const force = forceMultiplier * collisionStrength;
    // Use the current dx/dy (or recalculated if we applied offset)
    const currentDx = node2.x - node1.x;
    const currentDy = node2.y - node1.y;
    const currentDistance = Math.sqrt(currentDx * currentDx + currentDy * currentDy) || 0.1;
    const fx = (currentDx / currentDistance) * force;
    const fy = (currentDy / currentDistance) * force;
    node1.vx -= fx;
    node1.vy -= fy;
    node2.vx += fx;
    node2.vy += fy;
  }
};

/**
 * Apply charge forces (repulsion between all nodes).
 */
const applyChargeForces = (nodesArray: NodeState[], config: ForceLayoutConfig): void => {
  for (let i = 0; i < nodesArray.length; i++) {
    for (let j = i + 1; j < nodesArray.length; j++) {
      const node1 = nodesArray[i];
      const node2 = nodesArray[j];

      const dx = node2.x - node1.x;
      const dy = node2.y - node1.y;
      const distance = Math.sqrt(dx * dx + dy * dy) || 0.1; // Avoid division by zero

      // Strong collision force when nodes are too close (prevents overlap)
      if (distance < config.minDistance) {
        applyCollisionForces(node1, node2, config.minDistance, config.collisionStrength);
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
};

/**
 * Check if two line segments intersect.
 * Uses parametric line intersection formula.
 */
const doLineSegmentsIntersect = (
  p1x: number,
  p1y: number,
  p2x: number,
  p2y: number,
  p3x: number,
  p3y: number,
  p4x: number,
  p4y: number
): boolean => {
  // Calculate direction vectors
  const d1x = p2x - p1x;
  const d1y = p2y - p1y;
  const d2x = p4x - p3x;
  const d2y = p4y - p3y;

  // Calculate denominator
  const denom = d1x * d2y - d1y * d2x;

  // Lines are parallel
  if (Math.abs(denom) < 1e-10) {
    return false;
  }

  // Calculate parameters
  const t1 = ((p3x - p1x) * d2y - (p3y - p1y) * d2x) / denom;
  const t2 = ((p3x - p1x) * d1y - (p3y - p1y) * d1x) / denom;

  // Check if intersection is within both segments
  return t1 >= 0 && t1 <= 1 && t2 >= 0 && t2 <= 1;
};

/**
 * Check if a line segment passes through a node (rectangle).
 * Node is 80x80px, so we check if the line segment intersects the node's bounding box.
 */
const doesEdgeCrossNode = (
  edgeStartX: number,
  edgeStartY: number,
  edgeEndX: number,
  edgeEndY: number,
  nodeX: number,
  nodeY: number,
  nodeSize: number = 80
): boolean => {
  // Node bounding box
  const nodeLeft = nodeX - nodeSize / 2;
  const nodeRight = nodeX + nodeSize / 2;
  const nodeTop = nodeY - nodeSize / 2;
  const nodeBottom = nodeY + nodeSize / 2;

  // Check if edge endpoints are both outside the node (if both inside, it's not crossing)
  const startInside =
    edgeStartX >= nodeLeft && edgeStartX <= nodeRight && edgeStartY >= nodeTop && edgeStartY <= nodeBottom;
  const endInside = edgeEndX >= nodeLeft && edgeEndX <= nodeRight && edgeEndY >= nodeTop && edgeEndY <= nodeBottom;

  // If both endpoints are inside, it's not crossing (it's connected)
  if (startInside && endInside) {
    return false;
  }

  // Check if line segment intersects any of the four sides of the node rectangle
  const corners = [
    [nodeLeft, nodeTop],
    [nodeRight, nodeTop],
    [nodeRight, nodeBottom],
    [nodeLeft, nodeBottom],
  ];

  for (let i = 0; i < 4; i++) {
    const [x1, y1] = corners[i];
    const [x2, y2] = corners[(i + 1) % 4];
    if (doLineSegmentsIntersect(edgeStartX, edgeStartY, edgeEndX, edgeEndY, x1, y1, x2, y2)) {
      return true;
    }
  }

  return false;
};

/**
 * Apply forces to minimize edge crossings.
 * This detects edge-to-edge and edge-to-node crossings and applies repulsive forces.
 */
const applyCrossingMinimizationForces = (
  edgeList: Array<{ source: NodeState; target: NodeState }>,
  nodesArray: NodeState[],
  crossingStrength: number = 50
): void => {
  // Check all pairs of edges for crossings
  for (let i = 0; i < edgeList.length; i++) {
    const edge1 = edgeList[i];
    const x1 = edge1.source.x;
    const y1 = edge1.source.y;
    const x2 = edge1.target.x;
    const y2 = edge1.target.y;

    // Check against all other edges
    for (let j = i + 1; j < edgeList.length; j++) {
      const edge2 = edgeList[j];
      const x3 = edge2.source.x;
      const y3 = edge2.source.y;
      const x4 = edge2.target.x;
      const y4 = edge2.target.y;

      // Skip if edges share a node (they're allowed to meet at nodes)
      if (
        edge1.source === edge2.source ||
        edge1.source === edge2.target ||
        edge1.target === edge2.source ||
        edge1.target === edge2.target
      ) {
        continue;
      }

      // Check if edges cross
      if (doLineSegmentsIntersect(x1, y1, x2, y2, x3, y3, x4, y4)) {
        // Calculate midpoint of each edge
        const mid1x = (x1 + x2) / 2;
        const mid1y = (y1 + y2) / 2;
        const mid2x = (x3 + x4) / 2;
        const mid2y = (y3 + y4) / 2;

        // Calculate direction to push edges apart
        const dx = mid2x - mid1x;
        const dy = mid2y - mid1y;
        const distance = Math.sqrt(dx * dx + dy * dy) || 1;

        // Apply repulsive force to push edges apart
        const force = crossingStrength / distance;
        const fx = (dx / distance) * force;
        const fy = (dy / distance) * force;

        // Apply forces to all four nodes
        edge1.source.vx -= fx * 0.25;
        edge1.source.vy -= fy * 0.25;
        edge1.target.vx -= fx * 0.25;
        edge1.target.vy -= fy * 0.25;
        edge2.source.vx += fx * 0.25;
        edge2.source.vy += fy * 0.25;
        edge2.target.vx += fx * 0.25;
        edge2.target.vy += fy * 0.25;
      }
    }

    // Check if edge passes through any node (excluding its own endpoints)
    for (const node of nodesArray) {
      if (node === edge1.source || node === edge1.target) {
        continue;
      }

      if (doesEdgeCrossNode(x1, y1, x2, y2, node.x, node.y)) {
        // Calculate closest point on edge to node center
        const edgeDx = x2 - x1;
        const edgeDy = y2 - y1;
        const edgeLengthSq = edgeDx * edgeDx + edgeDy * edgeDy;
        if (edgeLengthSq < 1e-10) continue;

        const t = Math.max(0, Math.min(1, ((node.x - x1) * edgeDx + (node.y - y1) * edgeDy) / edgeLengthSq));
        const closestX = x1 + t * edgeDx;
        const closestY = y1 + t * edgeDy;

        // Push node away from edge
        const dx = node.x - closestX;
        const dy = node.y - closestY;
        const distance = Math.sqrt(dx * dx + dy * dy) || 1;
        const force = (crossingStrength * 2) / distance; // Stronger force for node-edge crossings
        node.vx += (dx / distance) * force;
        node.vy += (dy / distance) * force;

        // Also push edge endpoints slightly
        const edgeForce = force * 0.1;
        edge1.source.vx -= (dx / distance) * edgeForce;
        edge1.source.vy -= (dy / distance) * edgeForce;
        edge1.target.vx -= (dx / distance) * edgeForce;
        edge1.target.vy -= (dy / distance) * edgeForce;
      }
    }
  }
};

/**
 * Apply center force to keep nodes centered.
 */
const applyCenterForce = (nodeMap: Map<string, NodeState>, centerStrength: number): void => {
  const centerX = 0;
  const centerY = 0;
  for (const node of nodeMap.values()) {
    node.vx += (centerX - node.x) * centerStrength;
    node.vy += (centerY - node.y) * centerStrength;
  }
};

/**
 * Update node positions with damping.
 */
const updateNodePositions = (nodeMap: Map<string, NodeState>, damping: number): void => {
  for (const node of nodeMap.values()) {
    node.x += node.vx * damping;
    node.y += node.vy * damping;
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
  const positionedNodes = initializeNodePositions(nodes, config.minDistance);

  // Create node map for quick lookup
  const nodeMap = new Map<string, NodeState>(
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

  // Create edge list with node references and direction data, filtering out edges with missing nodes
  const edgeList = edges
    .filter(edge => {
      const source = nodeMap.get(edge.source);
      const target = nodeMap.get(edge.target);
      return source && target;
    })
    .map(edge => {
      const source = nodeMap.get(edge.source)!;
      const target = nodeMap.get(edge.target)!;
      const direction = (edge.data as ExitEdgeData | undefined)?.direction;
      return { source, target, direction };
    });

  // Run force simulation
  for (let iteration = 0; iteration < config.iterations; iteration++) {
    // Reset forces
    for (const node of nodeMap.values()) {
      node.vx = 0;
      node.vy = 0;
    }

    // Apply link forces (attraction between connected nodes)
    applyLinkForces(edgeList, config.linkDistance);

    // Apply charge forces and collision avoidance (repulsion between all nodes)
    const nodesArray = Array.from(nodeMap.values());
    applyChargeForces(nodesArray, config);

    // Apply edge crossing minimization if enabled
    if (config.minimizeCrossings) {
      applyCrossingMinimizationForces(edgeList, nodesArray, 50);
    }

    // Apply center force
    applyCenterForce(nodeMap, config.centerStrength);

    // Update positions with damping
    updateNodePositions(nodeMap, config.damping);
  }

  // Convert back to React Flow nodes
  const result = positionedNodes.map(node => {
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

  return result;
};

/**
 * Apply grid layout to a set of nodes.
 */
export const applyGridLayout = (
  nodes: Node<RoomNodeData>[],
  config: GridLayoutConfig = defaultGridLayoutConfig
): Node<RoomNodeData>[] => {
  const result = nodes.map((node, index) => {
    const position = calculateGridPosition(node, index, nodes, config);
    return {
      ...node,
      position,
    };
  });
  return result;
};
