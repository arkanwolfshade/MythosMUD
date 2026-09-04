/**
 * Tests for useMapEditing hook.
 *
 * Verifies that the hook properly manages edit operations including
 * node repositioning, edge creation/deletion, and undo/redo functionality.
 */

import { act, renderHook } from '@testing-library/react';
import type { Edge, Node } from 'reactflow';
import { beforeEach, describe, expect, it, vi } from 'vitest';
import type { ExitEdgeData, RoomNodeData } from '../../types';
import { useMapEditing } from '../useMapEditing';

describe('useMapEditing', () => {
  const mockNodes: Node<RoomNodeData>[] = [
    {
      id: 'room1',
      type: 'room',
      position: { x: 0, y: 0 },
      data: { id: 'room1', name: 'Room 1', description: '' },
    },
    {
      id: 'room2',
      type: 'room',
      position: { x: 100, y: 100 },
      data: { id: 'room2', name: 'Room 2', description: '' },
    },
  ];

  const mockEdges: Edge<ExitEdgeData>[] = [
    {
      id: 'edge1',
      source: 'room1',
      target: 'room2',
      type: 'exit',
      data: { direction: 'north', sourceRoomId: 'room1', targetRoomId: 'room2' },
    },
  ];

  beforeEach(() => {
    vi.clearAllMocks();
  });

  it('should initialize with nodes and edges', () => {
    const { result } = renderHook(() =>
      useMapEditing({
        nodes: mockNodes,
        edges: mockEdges,
      })
    );

    expect(result.current.nodes).toEqual(mockNodes);
    expect(result.current.edges).toEqual(mockEdges);
    expect(result.current.hasUnsavedChanges).toBe(false);
  });

  it('should update node position', () => {
    const { result } = renderHook(() =>
      useMapEditing({
        nodes: mockNodes,
        edges: mockEdges,
      })
    );

    act(() => {
      result.current.updateNodePosition('room1', { x: 50, y: 50 });
    });

    expect(result.current.nodes[0].position).toEqual({ x: 50, y: 50 });
    expect(result.current.hasUnsavedChanges).toBe(true);
  });

  it('should create a new edge', () => {
    const { result } = renderHook(() =>
      useMapEditing({
        nodes: mockNodes,
        edges: mockEdges,
      })
    );

    act(() => {
      result.current.createEdge({
        sourceRoomId: 'room2',
        targetRoomId: 'room1',
        direction: 'south',
      });
    });

    expect(result.current.edges).toHaveLength(2);
    expect(result.current.edges[1].data?.direction).toBe('south');
    expect(result.current.hasUnsavedChanges).toBe(true);
  });

  it('should delete an edge', () => {
    const { result } = renderHook(() =>
      useMapEditing({
        nodes: mockNodes,
        edges: mockEdges,
      })
    );

    act(() => {
      result.current.deleteEdge('edge1');
    });

    expect(result.current.edges).toHaveLength(0);
    expect(result.current.hasUnsavedChanges).toBe(true);
  });

  it('should update edge properties', () => {
    const { result } = renderHook(() =>
      useMapEditing({
        nodes: mockNodes,
        edges: mockEdges,
      })
    );

    act(() => {
      result.current.updateEdge('edge1', {
        flags: ['hidden', 'locked'],
        description: 'A hidden locked door',
      });
    });

    expect(result.current.edges[0].data?.flags).toEqual(['hidden', 'locked']);
    expect(result.current.edges[0].data?.description).toBe('A hidden locked door');
    expect(result.current.hasUnsavedChanges).toBe(true);
  });

  it('should support undo operation', () => {
    const { result } = renderHook(() =>
      useMapEditing({
        nodes: mockNodes,
        edges: mockEdges,
      })
    );

    act(() => {
      result.current.updateNodePosition('room1', { x: 50, y: 50 });
    });

    expect(result.current.hasUnsavedChanges).toBe(true);

    act(() => {
      result.current.undo();
    });

    expect(result.current.nodes[0].position).toEqual({ x: 0, y: 0 });
    expect(result.current.hasUnsavedChanges).toBe(false);
  });

  it('should support redo operation', () => {
    const { result } = renderHook(() =>
      useMapEditing({
        nodes: mockNodes,
        edges: mockEdges,
      })
    );

    act(() => {
      result.current.updateNodePosition('room1', { x: 50, y: 50 });
    });

    act(() => {
      result.current.undo();
    });

    act(() => {
      result.current.redo();
    });

    expect(result.current.nodes[0].position).toEqual({ x: 50, y: 50 });
    expect(result.current.hasUnsavedChanges).toBe(true);
  });

  it('should validate edge creation', () => {
    const { result } = renderHook(() =>
      useMapEditing({
        nodes: mockNodes,
        edges: mockEdges,
      })
    );

    // Try to create edge with non-existent target
    act(() => {
      const validation = result.current.validateEdgeCreation({
        sourceRoomId: 'room1',
        targetRoomId: 'nonexistent',
        direction: 'north',
      });
      expect(validation.isValid).toBe(false);
      expect(validation.errors).toContain('Target room does not exist');
    });
  });

  it('should clear unsaved changes after save', async () => {
    const onSave = vi.fn().mockResolvedValue(undefined);

    const { result } = renderHook(() =>
      useMapEditing({
        nodes: mockNodes,
        edges: mockEdges,
        onSave,
      })
    );

    act(() => {
      result.current.updateNodePosition('room1', { x: 50, y: 50 });
    });

    expect(result.current.hasUnsavedChanges).toBe(true);

    await act(async () => {
      await result.current.save();
    });

    expect(onSave).toHaveBeenCalled();
    expect(result.current.hasUnsavedChanges).toBe(false);
  });
});
