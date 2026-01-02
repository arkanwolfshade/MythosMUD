/**
 * Custom Exit Edge component for React Flow.
 *
 * This component renders an exit connection between rooms, with icon/badge
 * indicators for exit flags (hidden, locked, one-way, self-reference).
 *
 * As documented in the Pnakotic Manuscripts, proper visualization of
 * dimensional gateways is essential for understanding the flow of
 * entities through our eldritch architecture.
 */

import React from 'react';
import { BaseEdge, EdgeLabelRenderer, getStraightPath, type EdgeProps } from 'reactflow';
import type { ExitEdgeData } from '../types';

// Type alias for ExitEdge props - extends EdgeProps for type safety
export type ExitEdgeProps = EdgeProps<ExitEdgeData>;

/**
 * Get icon/badge for exit flags.
 */
const getFlagIcon = (flag: string): { icon: string; color: string; label: string } => {
  switch (flag) {
    case 'hidden':
      return { icon: '👁️', color: 'text-gray-400', label: 'Hidden' };
    case 'locked':
      return { icon: '🔒', color: 'text-yellow-400', label: 'Locked' };
    case 'one_way':
      return { icon: '➡️', color: 'text-blue-400', label: 'One-way' };
    case 'self_reference':
      return { icon: '🔄', color: 'text-purple-400', label: 'Self-reference' };
    default:
      return { icon: '', color: '', label: '' };
  }
};

/**
 * Exit Edge component with flag indicators.
 *
 * Memoized to prevent unnecessary re-renders when props haven't changed.
 */
export const ExitEdge: React.FC<ExitEdgeProps> = React.memo(
  ({ id, sourceX, sourceY, targetX, targetY, style = {}, markerEnd, data }) => {
    const [edgePath, labelX, labelY] = getStraightPath({
      sourceX,
      sourceY,
      targetX,
      targetY,
    });

    const flags = data?.flags || [];
    const direction = data?.direction || '';

    return (
      <>
        <BaseEdge
          id={id}
          path={edgePath}
          markerEnd={markerEnd}
          style={{
            ...style,
            stroke: data?.flags?.includes('hidden') ? '#6b7280' : '#10b981',
            strokeWidth: data?.flags?.includes('locked') ? 3 : 2,
            strokeDasharray: data?.flags?.includes('one_way') ? '5,5' : undefined,
          }}
        />
        {flags.length > 0 && (
          <EdgeLabelRenderer>
            <div
              style={{
                position: 'absolute',
                transform: `translate(-50%, -50%) translate(${labelX}px,${labelY}px)`,
                pointerEvents: 'all',
              }}
              className="flex gap-1 bg-mythos-terminal-background border border-mythos-terminal-border rounded px-1 py-0.5"
            >
              {flags.map((flag, index) => {
                const flagInfo = getFlagIcon(flag);
                if (!flagInfo.icon) return null;

                return (
                  <span key={index} className={`${flagInfo.color} text-xs`} title={`${flagInfo.label} exit`}>
                    {flagInfo.icon}
                  </span>
                );
              })}
              {direction && (
                <span className="text-xs text-mythos-terminal-text ml-1" title="Direction">
                  {direction}
                </span>
              )}
            </div>
          </EdgeLabelRenderer>
        )}
      </>
    );
  },
  (prevProps, nextProps) => {
    // Only re-render if relevant props have changed
    return (
      prevProps.id === nextProps.id &&
      prevProps.sourceX === nextProps.sourceX &&
      prevProps.sourceY === nextProps.sourceY &&
      prevProps.targetX === nextProps.targetX &&
      prevProps.targetY === nextProps.targetY &&
      JSON.stringify(prevProps.data?.flags) === JSON.stringify(nextProps.data?.flags) &&
      prevProps.data?.direction === nextProps.data?.direction
    );
  }
);
