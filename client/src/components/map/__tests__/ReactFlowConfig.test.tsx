/**
 * Tests for React Flow installation and configuration.
 *
 * These tests verify that React Flow is properly installed and can be
 * configured with custom node and edge types for the map editor.
 *
 * As documented in the Pnakotic Manuscripts, proper configuration of
 * dimensional visualization tools is essential for maintaining spatial
 * awareness across the eldritch architecture.
 */

import { render } from '@testing-library/react';
import { Handle, MarkerType, Position, ReactFlow, ReactFlowProvider } from 'reactflow';
import { describe, expect, it } from 'vitest';
import { getEdgeTypes, getNodeTypes } from '../config';
import { ExitEdge } from '../edges/ExitEdge';
import { IntersectionNode } from '../nodes/IntersectionNode';
import { RoomNode } from '../nodes/RoomNode';

describe('React Flow Installation and Configuration', () => {
  it('should be able to import ReactFlow', () => {
    expect(ReactFlow).toBeDefined();
    // ReactFlow is exported as a component (object in some contexts)
    expect(ReactFlow).toBeTruthy();
  });

  it('should be able to import ReactFlowProvider', () => {
    expect(ReactFlowProvider).toBeDefined();
    expect(typeof ReactFlowProvider).toBe('function');
  });

  it('should be able to import node components (Handle, Position)', () => {
    expect(Handle).toBeDefined();
    // Handle is a React component (object in some contexts)
    expect(Handle).toBeTruthy();
    expect(Position).toBeDefined();
    expect(Position.Top).toBe('top');
    expect(Position.Bottom).toBe('bottom');
    expect(Position.Left).toBe('left');
    expect(Position.Right).toBe('right');
  });

  it('should be able to import edge types', () => {
    expect(MarkerType).toBeDefined();
    expect(MarkerType.ArrowClosed).toBe('arrowclosed');
  });

  it('should export custom node types', () => {
    expect(RoomNode).toBeDefined();
    expect(IntersectionNode).toBeDefined();
  });

  it('should export custom edge types', () => {
    expect(ExitEdge).toBeDefined();
  });

  it('should provide node types configuration', () => {
    const nodeTypes = getNodeTypes();
    expect(nodeTypes).toBeDefined();
    expect(nodeTypes.room).toBeDefined();
    expect(nodeTypes.intersection).toBeDefined();
    expect(nodeTypes.room).toBe(RoomNode);
    expect(nodeTypes.intersection).toBe(IntersectionNode);
  });

  it('should provide edge types configuration', () => {
    const edgeTypes = getEdgeTypes();
    expect(edgeTypes).toBeDefined();
    expect(edgeTypes.exit).toBeDefined();
    expect(edgeTypes.exit).toBe(ExitEdge);
  });

  it('should render ReactFlowProvider without errors', () => {
    const { container } = render(
      <ReactFlowProvider>
        <div>Test</div>
      </ReactFlowProvider>
    );
    expect(container).toBeDefined();
  });
});
