/**
 * Custom Intersection Node component for React Flow.
 *
 * This component renders an intersection (room where multiple paths meet)
 * as a node on the map, using a square shape (all nodes are now squares).
 *
 * As noted in the Cultes des Goules, intersections represent critical
 * dimensional convergence points in our eldritch architecture.
 */

import React from 'react';
import { Handle, Position, type NodeProps } from 'reactflow';
import type { RoomNodeData } from '../types';
import { DepartureMarkers } from './DepartureMarkers';

// Type alias for IntersectionNode props - extends NodeProps for type safety
export type IntersectionNodeProps = NodeProps<RoomNodeData>;

// Scalar fields compared by strict equality; `departures` (an array) is compared separately below.
const MEMO_COMPARE_FIELDS = [
  'id',
  'name',
  'isCurrentLocation',
  'hasUnsavedChanges',
  'environment',
  'subZone',
] as const satisfies readonly (keyof RoomNodeData)[];

function arePropsEqual(prevProps: IntersectionNodeProps, nextProps: IntersectionNodeProps): boolean {
  // Only re-render if data has changed
  const scalarFieldsEqual = MEMO_COMPARE_FIELDS.every(field => prevProps.data[field] === nextProps.data[field]);
  const departuresEqual = (prevProps.data.departures?.join() ?? '') === (nextProps.data.departures?.join() ?? '');
  return scalarFieldsEqual && departuresEqual;
}

/**
 * Intersection Node component.
 *
 * Memoized to prevent unnecessary re-renders when props haven't changed.
 */
export const IntersectionNode: React.FC<IntersectionNodeProps> = React.memo(({ data }) => {
  return (
    <div className="relative flex items-center justify-center border-2 border-mythos-terminal-primary bg-mythos-terminal-background text-mythos-terminal-text font-mono text-xs w-20 h-20">
      {/* Handles for connections - each handle has a unique ID based on position */}
      <Handle type="target" id="target-top" position={Position.Top} className="w-2 h-2 bg-mythos-terminal-primary" />
      <Handle
        type="target"
        id="target-right"
        position={Position.Right}
        className="w-2 h-2 bg-mythos-terminal-primary"
      />
      <Handle
        type="target"
        id="target-bottom"
        position={Position.Bottom}
        className="w-2 h-2 bg-mythos-terminal-primary"
      />
      <Handle type="target" id="target-left" position={Position.Left} className="w-2 h-2 bg-mythos-terminal-primary" />

      <Handle type="source" id="source-top" position={Position.Top} className="w-2 h-2 bg-mythos-terminal-success" />
      <Handle
        type="source"
        id="source-right"
        position={Position.Right}
        className="w-2 h-2 bg-mythos-terminal-success"
      />
      <Handle
        type="source"
        id="source-bottom"
        position={Position.Bottom}
        className="w-2 h-2 bg-mythos-terminal-success"
      />
      <Handle type="source" id="source-left" position={Position.Left} className="w-2 h-2 bg-mythos-terminal-success" />
      {/* Ways out of the loaded area; see DepartureMarkers. */}
      <DepartureMarkers departures={data.departures} />

      {/* Node content */}
      <div className="text-center px-1 truncate max-w-full" title={data.name}>
        {data.name}
      </div>
    </div>
  );
}, arePropsEqual);
