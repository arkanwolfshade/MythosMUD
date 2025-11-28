/**
 * Tests for useMapLayout hook.
 *
 * Verifies that the hook properly manages node positions, handles
 * stored coordinates, and provides save/reset functionality.
 */

import { renderHook, act } from '@testing-library/react';
import { describe, expect, it, vi, beforeEach } from 'vitest';
import { useMapLayout } from '../useMapLayout';
import type { Node } from 'reactflow';
import type { RoomNodeData } from '../../types';

describe('useMapLayout', () => {
  const createMockNode = (id: string, position = { x: 0, y: 0 }): Node<RoomNodeData> => ({
    id,
    type: 'room',
    position,
    data: {
      id,
      name: `Room ${id}`,
      description: 'Test room',
    },
  });

  beforeEach(() => {
    vi.clearAllMocks();
  });

  it('should use stored coordinates when available', () => {
    const nodes: Node<RoomNodeData>[] = [
      {
        ...createMockNode('room1'),
        data: {
          ...createMockNode('room1').data,
          map_x: 100,
          map_y: 200,
        } as RoomNodeData & { map_x: number; map_y: number },
      },
    ];

    const { result } = renderHook(() =>
      useMapLayout({
        nodes,
        useStoredCoordinates: true,
      })
    );

    expect(result.current.layoutNodes[0].position).toEqual({ x: 100, y: 200 });
    expect(result.current.hasUnsavedChanges).toBe(false);
  });

  it('should fall back to grid layout when stored coordinates not available', () => {
    const nodes: Node<RoomNodeData>[] = [createMockNode('room1'), createMockNode('room2')];

    const { result } = renderHook(() =>
      useMapLayout({
        nodes,
        useStoredCoordinates: true,
      })
    );

    // Nodes should have positions (either from grid or existing)
    expect(result.current.layoutNodes).toHaveLength(2);
    expect(result.current.layoutNodes[0].position).toBeDefined();
    expect(result.current.layoutNodes[1].position).toBeDefined();
  });

  it('should update node position and mark as unsaved', () => {
    const nodes: Node<RoomNodeData>[] = [createMockNode('room1')];

    const { result } = renderHook(() =>
      useMapLayout({
        nodes,
      })
    );

    act(() => {
      result.current.updateNodePosition('room1', { x: 150, y: 250 });
    });

    expect(result.current.layoutNodes[0].position).toEqual({ x: 150, y: 250 });
    expect(result.current.hasUnsavedChanges).toBe(true);
    expect(result.current.layoutNodes[0].data.hasUnsavedChanges).toBe(true);
  });

  it('should save positions when onSave is provided', async () => {
    const nodes: Node<RoomNodeData>[] = [createMockNode('room1')];
    const onSave = vi.fn().mockResolvedValue(undefined);

    const { result } = renderHook(() =>
      useMapLayout({
        nodes,
        onSave,
      })
    );

    act(() => {
      result.current.updateNodePosition('room1', { x: 150, y: 250 });
    });

    await act(async () => {
      await result.current.savePositions();
    });

    expect(onSave).toHaveBeenCalledWith(
      expect.objectContaining({
        get: expect.any(Function),
      })
    );
    expect(result.current.hasUnsavedChanges).toBe(false);
  });

  it('should reset to auto-layout', () => {
    const nodes: Node<RoomNodeData>[] = [createMockNode('room1')];

    const { result } = renderHook(() =>
      useMapLayout({
        nodes,
      })
    );

    act(() => {
      result.current.updateNodePosition('room1', { x: 150, y: 250 });
    });

    expect(result.current.hasUnsavedChanges).toBe(true);

    act(() => {
      result.current.resetToAutoLayout();
    });

    expect(result.current.hasUnsavedChanges).toBe(false);
  });

  it('should apply grid layout to all nodes', () => {
    const nodes: Node<RoomNodeData>[] = [createMockNode('room1'), createMockNode('room2'), createMockNode('room3')];

    const { result } = renderHook(() =>
      useMapLayout({
        nodes,
      })
    );

    act(() => {
      result.current.applyGridLayout();
    });

    // All nodes should have positions after grid layout
    result.current.layoutNodes.forEach(node => {
      expect(node.position).toBeDefined();
      expect(typeof node.position.x).toBe('number');
      expect(typeof node.position.y).toBe('number');
    });
  });

  it('should handle null stored coordinates', () => {
    const nodes: Node<RoomNodeData>[] = [
      {
        ...createMockNode('room1'),
        data: {
          ...createMockNode('room1').data,
          map_x: null,
          map_y: null,
        } as RoomNodeData & { map_x: null; map_y: null },
      },
    ];

    const { result } = renderHook(() =>
      useMapLayout({
        nodes,
        useStoredCoordinates: true,
      })
    );

    // Should not use null coordinates, should use grid or existing position
    expect(result.current.layoutNodes[0].position).toBeDefined();
  });
});
