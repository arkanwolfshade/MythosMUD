/**
 * Custom Exit Edge component for React Flow.
 */

import React from 'react';
import { BaseEdge, EdgeLabelRenderer, getStraightPath, type EdgeProps } from 'reactflow';
import type { ExitEdgeData } from '../types';

export type ExitEdgeProps = EdgeProps<ExitEdgeData>;

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

function exitFlags(data: ExitEdgeData | undefined): string[] {
  return data?.flags ?? [];
}

function getEdgeStrokeStyle(data: ExitEdgeData | undefined, style: React.CSSProperties): React.CSSProperties {
  const flags = exitFlags(data);
  return {
    ...style,
    stroke: flags.includes('hidden') ? '#6b7280' : '#10b981',
    strokeWidth: flags.includes('locked') ? 3 : 2,
    strokeDasharray: flags.includes('one_way') ? '5,5' : undefined,
  };
}

function ExitEdgeLabels(props: {
  flags: string[];
  direction: string;
  labelX: number;
  labelY: number;
}): React.ReactElement {
  return (
    <EdgeLabelRenderer>
      <div
        style={{
          position: 'absolute',
          transform: `translate(-50%, -50%) translate(${props.labelX}px,${props.labelY}px)`,
          pointerEvents: 'all',
        }}
        className="flex gap-1 bg-mythos-terminal-background border border-mythos-terminal-border rounded px-1 py-0.5"
      >
        {props.flags.map((flag, index) => {
          const flagInfo = getFlagIcon(flag);
          if (!flagInfo.icon) return null;
          return (
            <span key={index} className={`${flagInfo.color} text-xs`} title={`${flagInfo.label} exit`}>
              {flagInfo.icon}
            </span>
          );
        })}
        {props.direction && (
          <span className="text-xs text-mythos-terminal-text ml-1" title="Direction">
            {props.direction}
          </span>
        )}
      </div>
    </EdgeLabelRenderer>
  );
}

const ExitEdgeBody = (props: ExitEdgeProps) => {
  const { id, sourceX, sourceY, targetX, targetY, style = {}, markerEnd, data } = props;
  const [edgePath, labelX, labelY] = getStraightPath({ sourceX, sourceY, targetX, targetY });
  const flags = data?.flags || [];
  const direction = data?.direction || '';

  return (
    <>
      <BaseEdge id={id} path={edgePath} markerEnd={markerEnd} style={getEdgeStrokeStyle(data, style)} />
      {flags.length > 0 && <ExitEdgeLabels flags={flags} direction={direction} labelX={labelX} labelY={labelY} />}
    </>
  );
};

export const ExitEdge: React.FC<ExitEdgeProps> = React.memo(ExitEdgeBody);
