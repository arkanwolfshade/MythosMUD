/**
 * Custom Room Node component for React Flow.
 *
 * This component renders a room as a node on the map, with different
 * shapes based on subzone/environment and visual indicators for the
 * player's current location.
 *
 * As documented in the Pnakotic Manuscripts, proper visualization of
 * spatial relationships is essential for understanding the eldritch
 * architecture of our world.
 */

import React from 'react';
import { Handle, Position, type NodeProps } from 'reactflow';
import type { RoomNodeData } from '../types';

// Type alias for RoomNode props - extends NodeProps for type safety
export type RoomNodeProps = NodeProps<RoomNodeData>;

/**
 * Get the shape component based on environment/subzone.
 */
const getNodeShape = (environment?: string, subZone?: string): 'circle' | 'square' | 'diamond' => {
  // Default to circle for outdoors
  if (!environment || environment === 'outdoors') {
    return 'circle';
  }

  // Square for indoors
  if (environment === 'indoors') {
    return 'square';
  }

  // Diamond for intersections or special locations
  if (environment === 'intersection' || subZone?.includes('intersection')) {
    return 'diamond';
  }

  // Default to circle
  return 'circle';
};

/**
 * Get CSS classes for the node based on its state.
 */
const getNodeClasses = (data: RoomNodeData): string => {
  const baseClasses = 'flex items-center justify-center border-2 font-mono text-xs';
  const shapeClasses = {
    circle: 'rounded-full',
    square: 'rounded',
    diamond: 'rotate-45',
  };

  const shape = getNodeShape(data.environment, data.subZone);
  const shapeClass = shapeClasses[shape];

  // Color based on state
  let colorClasses = 'bg-mythos-terminal-background border-mythos-terminal-border text-mythos-terminal-text';

  if (data.isCurrentLocation) {
    // Pulsing animation for current location
    colorClasses = 'bg-mythos-terminal-primary border-mythos-terminal-primary text-white animate-pulse';
  } else if (data.hasUnsavedChanges) {
    colorClasses = 'bg-yellow-900 border-yellow-600 text-yellow-200';
  }

  return `${baseClasses} ${shapeClass} ${colorClasses}`;
};

/**
 * Room Node component.
 *
 * Memoized to prevent unnecessary re-renders when props haven't changed.
 */
export const RoomNode: React.FC<RoomNodeProps> = React.memo(
  ({ data }) => {
    const nodeClasses = getNodeClasses(data);
    const shape = getNodeShape(data.environment, data.subZone);

    // For diamond shape, we need to rotate the content back
    const contentClasses = shape === 'diamond' ? 'rotate-[-45deg]' : '';

    return (
      <div className={nodeClasses} style={{ width: '80px', height: '80px' }}>
        {/* Handles for connections */}
        <Handle type="target" position={Position.Top} className="w-2 h-2 bg-mythos-terminal-primary" />
        <Handle type="target" position={Position.Right} className="w-2 h-2 bg-mythos-terminal-primary" />
        <Handle type="target" position={Position.Bottom} className="w-2 h-2 bg-mythos-terminal-primary" />
        <Handle type="target" position={Position.Left} className="w-2 h-2 bg-mythos-terminal-primary" />

        <Handle type="source" position={Position.Top} className="w-2 h-2 bg-mythos-terminal-success" />
        <Handle type="source" position={Position.Right} className="w-2 h-2 bg-mythos-terminal-success" />
        <Handle type="source" position={Position.Bottom} className="w-2 h-2 bg-mythos-terminal-success" />
        <Handle type="source" position={Position.Left} className="w-2 h-2 bg-mythos-terminal-success" />

        {/* Node content */}
        <div className={contentClasses}>
          <div className="text-center px-1 truncate max-w-full" title={data.name}>
            {data.name}
          </div>
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
