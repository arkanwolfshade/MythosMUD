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
      <div className="flex items-center justify-center border-2 border-mythos-terminal-primary bg-mythos-terminal-background text-mythos-terminal-text font-mono text-xs w-20 h-20">
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
        <Handle
          type="target"
          id="target-left"
          position={Position.Left}
          className="w-2 h-2 bg-mythos-terminal-primary"
        />

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
        <Handle
          type="source"
          id="source-left"
          position={Position.Left}
          className="w-2 h-2 bg-mythos-terminal-success"
        />

        {/* Node content */}
        <div className="text-center px-1 truncate max-w-full" title={data.name}>
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
