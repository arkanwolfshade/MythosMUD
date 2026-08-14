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

interface Point2D {
  x: number;
  y: number;
}

interface Segment2D {
  start: Point2D;
  end: Point2D;
}

function getStoredMapPosition(node: Node<RoomNodeData>): Point2D | null {
  if (!node.data || !('map_x' in node.data) || !('map_y' in node.data)) {
    return null;
  }
  const mapX = node.data.map_x;
  const mapY = node.data.map_y;
  if (mapX == null || mapY == null) {
    return null;
  }
  return { x: mapX, y: mapY };
}

function gridPositionForIndex(
  index: number,
  count: number,
  cellWidth: number,
  cellHeight: number,
  horizontalSpacing: number,
  verticalSpacing: number
): Point2D {
  const colsPerRow = Math.ceil(Math.sqrt(count));
  const row = Math.floor(index / colsPerRow);
  const col = index % colsPerRow;
  return {
    x: col * (cellWidth + horizontalSpacing),
    y: row * (cellHeight + verticalSpacing),
  };
}

function groupedGridPosition(
  node: Node<RoomNodeData>,
  nodes: Node<RoomNodeData>[],
  groupKey: 'subZone' | 'zone',
  config: GridLayoutConfig
): Point2D | null {
  const groupValue = groupKey === 'subZone' ? node.data?.subZone : node.data?.zone;
  if (!groupValue) return null;

  const groupNodes = nodes.filter(n => (groupKey === 'subZone' ? n.data?.subZone : n.data?.zone) === groupValue);
  const groupIndex = groupNodes.findIndex(n => n.id === node.id);
  return gridPositionForIndex(
    groupIndex,
    groupNodes.length,
    config.cellWidth,
    config.cellHeight,
    config.horizontalSpacing,
    config.verticalSpacing
  );
}

/**
 * Calculate grid position for a node based on zone/subzone grouping.
 */
export const calculateGridPosition = (
  node: Node<RoomNodeData>,
  index: number,
  nodes: Node<RoomNodeData>[],
  config: GridLayoutConfig = defaultGridLayoutConfig
): Point2D => {
  const stored = getStoredMapPosition(node);
  if (stored) return stored;

  if (config.groupBySubZone && node.data?.subZone) {
    const grouped = groupedGridPosition(node, nodes, 'subZone', config);
    if (grouped) return grouped;
  }

  if (config.groupByZone && node.data?.zone) {
    const grouped = groupedGridPosition(node, nodes, 'zone', config);
    if (grouped) return grouped;
  }

  return gridPositionForIndex(
    index,
    nodes.length,
    config.cellWidth,
    config.cellHeight,
    config.horizontalSpacing,
    config.verticalSpacing
  );
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

const CARDINAL_DESIRED_OFFSET: Record<string, { dx: number; dy: number }> = {
  north: { dx: 0, dy: -1 },
  south: { dx: 0, dy: 1 },
  east: { dx: 1, dy: 0 },
  west: { dx: -1, dy: 0 },
};

// Arrow consts (not function decls): Lizard merges consecutive `function` bodies into one function.
const linkForceReduction = (distance: number, minDistanceForLink: number): number =>
  distance < minDistanceForLink ? Math.max(0.1, distance / minDistanceForLink) : 1.0;

const applyMutualForce = (
  source: NodeState,
  target: NodeState,
  fx: number,
  fy: number,
  sourceScale = 1,
  targetScale = 1
): void => {
  source.vx += fx * sourceScale;
  source.vy += fy * sourceScale;
  target.vx -= fx * targetScale;
  target.vy -= fy * targetScale;
};

const applyStandardLinkAttraction = (
  edge: { source: NodeState; target: NodeState },
  dx: number,
  dy: number,
  distance: number,
  linkDistance: number
): void => {
  const minDistanceForLink = 120;
  const baseForce = (distance - linkDistance) * 0.1;
  const force = baseForce * linkForceReduction(distance, minDistanceForLink);
  applyMutualForce(edge.source, edge.target, (dx / distance) * force, (dy / distance) * force);
};

const applyCardinalLinkForce = (
  edge: { source: NodeState; target: NodeState },
  direction: string,
  dx: number,
  dy: number,
  distance: number,
  linkDistance: number
): void => {
  const offset = CARDINAL_DESIRED_OFFSET[direction.toLowerCase()];
  if (!offset) {
    applyStandardLinkAttraction(edge, dx, dy, distance, linkDistance);
    return;
  }

  const desiredDx = offset.dx * linkDistance;
  const desiredDy = offset.dy * linkDistance;
  const desiredLength = Math.sqrt(desiredDx * desiredDx + desiredDy * desiredDy);
  const directionalStrength = 0.02;
  let fx = (desiredDx / desiredLength) * linkDistance * directionalStrength;
  let fy = (desiredDy / desiredLength) * linkDistance * directionalStrength;

  const minDistanceForLink = 120;
  const distanceForce = (distance - linkDistance) * 0.05 * linkForceReduction(distance, minDistanceForLink);
  fx += (dx / distance) * distanceForce;
  fy += (dy / distance) * distanceForce;
  applyMutualForce(edge.source, edge.target, fx, fy);
};

const applyLinkForces = (
  edgeList: Array<{ source: NodeState; target: NodeState; direction?: string }>,
  linkDistance: number
): void => {
  for (const edge of edgeList) {
    const dx = edge.target.x - edge.source.x;
    const dy = edge.target.y - edge.source.y;
    const distance = Math.sqrt(dx * dx + dy * dy) || 1;

    if (edge.direction && CARDINAL_DESIRED_OFFSET[edge.direction.toLowerCase()]) {
      applyCardinalLinkForce(edge, edge.direction, dx, dy, distance, linkDistance);
    } else if (edge.direction) {
      applyStandardLinkAttraction(edge, dx, dy, distance, linkDistance);
    } else {
      applyStandardLinkAttraction(edge, dx, dy, distance, linkDistance);
    }
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
 */
const doLineSegmentsIntersect = (segmentA: Segment2D, segmentB: Segment2D): boolean => {
  const { start: p1, end: p2 } = segmentA;
  const { start: p3, end: p4 } = segmentB;
  const d1x = p2.x - p1.x;
  const d1y = p2.y - p1.y;
  const d2x = p4.x - p3.x;
  const d2y = p4.y - p3.y;
  const denom = d1x * d2y - d1y * d2x;

  if (Math.abs(denom) < 1e-10) {
    return false;
  }

  const t1 = ((p3.x - p1.x) * d2y - (p3.y - p1.y) * d2x) / denom;
  const t2 = ((p3.x - p1.x) * d1y - (p3.y - p1.y) * d1x) / denom;
  return t1 >= 0 && t1 <= 1 && t2 >= 0 && t2 <= 1;
};

/** Axis-aligned bounds check for a point vs node rectangle. */
const isPointInNodeBounds = (x: number, y: number, left: number, right: number, top: number, bottom: number): boolean =>
  x >= left && x <= right && y >= top && y <= bottom;

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
  const nodeLeft = nodeX - nodeSize / 2;
  const nodeRight = nodeX + nodeSize / 2;
  const nodeTop = nodeY - nodeSize / 2;
  const nodeBottom = nodeY + nodeSize / 2;

  // Endpoints both inside means the edge is a room-to-self stub; not a crossing.
  if (
    isPointInNodeBounds(edgeStartX, edgeStartY, nodeLeft, nodeRight, nodeTop, nodeBottom) &&
    isPointInNodeBounds(edgeEndX, edgeEndY, nodeLeft, nodeRight, nodeTop, nodeBottom)
  ) {
    return false;
  }

  const edgeSegment: Segment2D = {
    start: { x: edgeStartX, y: edgeStartY },
    end: { x: edgeEndX, y: edgeEndY },
  };
  const corners: Point2D[] = [
    { x: nodeLeft, y: nodeTop },
    { x: nodeRight, y: nodeTop },
    { x: nodeRight, y: nodeBottom },
    { x: nodeLeft, y: nodeBottom },
  ];

  for (let i = 0; i < 4; i++) {
    const side: Segment2D = { start: corners[i], end: corners[(i + 1) % 4] };
    if (doLineSegmentsIntersect(edgeSegment, side)) {
      return true;
    }
  }

  return false;
};

const edgesShareNode = (
  edge1: { source: NodeState; target: NodeState },
  edge2: { source: NodeState; target: NodeState }
): boolean =>
  edge1.source === edge2.source ||
  edge1.source === edge2.target ||
  edge1.target === edge2.source ||
  edge1.target === edge2.target;

function edgeEndpointsSegment(edge: { source: NodeState; target: NodeState }): Segment2D {
  return {
    start: { x: edge.source.x, y: edge.source.y },
    end: { x: edge.target.x, y: edge.target.y },
  };
}

/** Midpoint-to-midpoint repulsion when two edge segments cross. */
function crossingEdgeForce(
  edge1: { source: NodeState; target: NodeState },
  edge2: { source: NodeState; target: NodeState },
  crossingStrength: number
): Point2D | null {
  if (!doLineSegmentsIntersect(edgeEndpointsSegment(edge1), edgeEndpointsSegment(edge2))) {
    return null;
  }
  const mid1x = (edge1.source.x + edge1.target.x) / 2;
  const mid1y = (edge1.source.y + edge1.target.y) / 2;
  const mid2x = (edge2.source.x + edge2.target.x) / 2;
  const mid2y = (edge2.source.y + edge2.target.y) / 2;
  const dx = mid2x - mid1x;
  const dy = mid2y - mid1y;
  const distance = Math.sqrt(dx * dx + dy * dy) || 1;
  const force = (crossingStrength / distance) * 0.25;
  return { x: (dx / distance) * force, y: (dy / distance) * force };
}

function nudgeEdgeVelocity(edge: { source: NodeState; target: NodeState }, fx: number, fy: number): void {
  edge.source.vx += fx;
  edge.source.vy += fy;
  edge.target.vx += fx;
  edge.target.vy += fy;
}

function repelCrossingEdgePair(
  edge1: { source: NodeState; target: NodeState },
  edge2: { source: NodeState; target: NodeState },
  crossingStrength: number
): void {
  const f = crossingEdgeForce(edge1, edge2, crossingStrength);
  if (!f) return;
  nudgeEdgeVelocity(edge1, -f.x, -f.y);
  nudgeEdgeVelocity(edge2, f.x, f.y);
}

function repelEdgeFromBlockingNode(
  edge1: { source: NodeState; target: NodeState },
  node: NodeState,
  crossingStrength: number
): void {
  const x1 = edge1.source.x;
  const y1 = edge1.source.y;
  const x2 = edge1.target.x;
  const y2 = edge1.target.y;

  if (!doesEdgeCrossNode(x1, y1, x2, y2, node.x, node.y)) {
    return;
  }

  const edgeDx = x2 - x1;
  const edgeDy = y2 - y1;
  const edgeLengthSq = edgeDx * edgeDx + edgeDy * edgeDy;
  if (edgeLengthSq < 1e-10) return;

  const t = Math.max(0, Math.min(1, ((node.x - x1) * edgeDx + (node.y - y1) * edgeDy) / edgeLengthSq));
  const closestX = x1 + t * edgeDx;
  const closestY = y1 + t * edgeDy;
  const dx = node.x - closestX;
  const dy = node.y - closestY;
  const distance = Math.sqrt(dx * dx + dy * dy) || 1;
  const force = (crossingStrength * 2) / distance;
  node.vx += (dx / distance) * force;
  node.vy += (dy / distance) * force;

  const edgeForce = force * 0.1;
  edge1.source.vx -= (dx / distance) * edgeForce;
  edge1.source.vy -= (dy / distance) * edgeForce;
  edge1.target.vx -= (dx / distance) * edgeForce;
  edge1.target.vy -= (dy / distance) * edgeForce;
}

const applyCrossingMinimizationForces = (
  edgeList: Array<{ source: NodeState; target: NodeState }>,
  nodesArray: NodeState[],
  crossingStrength: number = 50
): void => {
  for (let i = 0; i < edgeList.length; i++) {
    const edge1 = edgeList[i];
    for (let j = i + 1; j < edgeList.length; j++) {
      const edge2 = edgeList[j];
      if (edgesShareNode(edge1, edge2)) continue;
      repelCrossingEdgePair(edge1, edge2, crossingStrength);
    }

    for (const node of nodesArray) {
      if (node === edge1.source || node === edge1.target) continue;
      repelEdgeFromBlockingNode(edge1, node, crossingStrength);
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

function buildSimulationEdgeList(
  edges: Edge[],
  nodeMap: Map<string, NodeState>
): Array<{ source: NodeState; target: NodeState; direction?: string }> {
  return edges
    .filter(edge => nodeMap.has(edge.source) && nodeMap.has(edge.target))
    .map(edge => ({
      source: nodeMap.get(edge.source)!,
      target: nodeMap.get(edge.target)!,
      direction: (edge.data as ExitEdgeData | undefined)?.direction,
    }));
}

function runForceSimulationStep(
  nodeMap: Map<string, NodeState>,
  edgeList: Array<{ source: NodeState; target: NodeState; direction?: string }>,
  config: ForceLayoutConfig
): void {
  for (const node of nodeMap.values()) {
    node.vx = 0;
    node.vy = 0;
  }

  applyLinkForces(edgeList, config.linkDistance);
  const nodesArray = Array.from(nodeMap.values());
  applyChargeForces(nodesArray, config);

  if (config.minimizeCrossings) {
    applyCrossingMinimizationForces(edgeList, nodesArray, 50);
  }

  applyCenterForce(nodeMap, config.centerStrength);
  updateNodePositions(nodeMap, config.damping);
}

/**
 * Apply force-directed layout to minimize edge crossings.
 */
export const applyForceLayout = (
  nodes: Node<RoomNodeData>[],
  edges: Edge[],
  config: ForceLayoutConfig = defaultForceLayoutConfig
): Node<RoomNodeData>[] => {
  if (nodes.length === 0) {
    return nodes;
  }

  const positionedNodes = initializeNodePositions(nodes, config.minDistance);
  const nodeMap = new Map<string, NodeState>(
    positionedNodes.map(n => [n.id, { id: n.id, x: n.position.x, y: n.position.y, vx: 0, vy: 0 }])
  );
  const edgeList = buildSimulationEdgeList(edges, nodeMap);

  for (let iteration = 0; iteration < config.iterations; iteration++) {
    runForceSimulationStep(nodeMap, edgeList, config);
  }

  return positionedNodes.map(node => {
    const positioned = nodeMap.get(node.id);
    if (!positioned) return node;
    return { ...node, position: { x: positioned.x, y: positioned.y } };
  });
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
