/**
 * Custom Intersection Node component for React Flow.
 *
 * This component renders an intersection (room where multiple paths meet)
 * as a node on the map, using a diamond shape to distinguish it from
 * regular rooms.
 *
 * As noted in the Cultes des Goules, intersections represent critical
 * dimensional convergence points in our eldritch architecture.
 */

import React from 'react';
import { Handle, Position, type NodeProps } from 'reactflow';
import type { RoomNodeData } from '../types';

// Type alias for IntersectionNode props - extends NodeProps for type safety
export type IntersectionNodeProps = NodeProps<RoomNodeData>;

/**
 * Intersection Node component.
 *
 * Memoized to prevent unnecessary re-renders when props haven't changed.
 */
export const IntersectionNode: React.FC<IntersectionNodeProps> = React.memo(
  ({ data }) => {
    return (
      <div
        className="flex items-center justify-center border-2 border-mythos-terminal-primary bg-mythos-terminal-background text-mythos-terminal-text font-mono text-xs rounded-full w-20 h-20"
        style={{ transform: 'rotate(45deg)' }}
      >
        {/* Handles for connections */}
        <Handle type="target" position={Position.Top} className="w-2 h-2 bg-mythos-terminal-primary" />
        <Handle type="target" position={Position.Right} className="w-2 h-2 bg-mythos-terminal-primary" />
        <Handle type="target" position={Position.Bottom} className="w-2 h-2 bg-mythos-terminal-primary" />
        <Handle type="target" position={Position.Left} className="w-2 h-2 bg-mythos-terminal-primary" />

        <Handle type="source" position={Position.Top} className="w-2 h-2 bg-mythos-terminal-success" />
        <Handle type="source" position={Position.Right} className="w-2 h-2 bg-mythos-terminal-success" />
        <Handle type="source" position={Position.Bottom} className="w-2 h-2 bg-mythos-terminal-success" />
        <Handle type="source" position={Position.Left} className="w-2 h-2 bg-mythos-terminal-success" />

        {/* Node content (rotated back) */}
        <div style={{ transform: 'rotate(-45deg)' }} className="text-center px-1 truncate max-w-full" title={data.name}>
          {data.name}
        </div>
      </div>
    );
  },
  (prevProps, nextProps) => {
    // Only re-render if data has changed
    return (
      prevProps.data.id === nextProps.data.id &&
      prevProps.data.name === nextProps.data.name &&
      prevProps.data.isCurrentLocation === nextProps.data.isCurrentLocation &&
      prevProps.data.hasUnsavedChanges === nextProps.data.hasUnsavedChanges &&
      prevProps.data.environment === nextProps.data.environment &&
      prevProps.data.subZone === nextProps.data.subZone
    );
  }
);
