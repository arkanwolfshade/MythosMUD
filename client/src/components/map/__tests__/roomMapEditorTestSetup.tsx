import React from 'react';
import { vi } from 'vitest';

function buildUseMapEditingMockReturn() {
  return {
    nodes: [
      {
        id: 'room1',
        type: 'room',
        position: { x: 0, y: 0 },
        data: { id: 'room1', name: 'Room 1' },
      },
    ],
    edges: [
      {
        id: 'edge1',
        source: 'room1',
        target: 'room2',
        data: { direction: 'north' },
      },
    ],
    hasUnsavedChanges: false,
    canUndo: false,
    canRedo: false,
    updateNodePosition: vi.fn(),
    createEdge: vi.fn(),
    deleteEdge: vi.fn(),
    updateEdge: vi.fn(),
    updateRoom: vi.fn(),
    validateEdgeCreation: vi.fn(() => ({ isValid: true })),
    undo: vi.fn(),
    redo: vi.fn(),
    save: vi.fn(),
    reset: vi.fn(),
  };
}

vi.mock('reactflow', () => ({
  default: ({
    children,
    onNodesChange,
    onEdgesChange,
    onNodeClick,
    onEdgeClick,
  }: {
    children?: React.ReactNode;
    onNodesChange?: (changes: unknown[]) => void;
    onEdgesChange?: (changes: unknown[]) => void;
    onNodeClick?: (event: unknown, node: unknown) => void;
    onEdgeClick?: (event: unknown, edge: unknown) => void;
  }) => (
    <div data-testid="react-flow">
      {children}
      <button
        data-testid="trigger-node-change"
        onClick={() => {
          onNodesChange?.([{ type: 'position', id: 'node1', position: { x: 100, y: 100 } }]);
        }}
      >
        Trigger Node Change
      </button>
      <button
        data-testid="trigger-edge-change"
        onClick={() => {
          onEdgesChange?.([{ type: 'remove', id: 'edge1' }]);
        }}
      >
        Trigger Edge Change
      </button>
      <button
        data-testid="trigger-node-click"
        onClick={() => {
          onNodeClick?.({}, { id: 'node1', data: { id: 'room1', name: 'Room 1' } });
        }}
      >
        Trigger Node Click
      </button>
      <button
        data-testid="trigger-edge-click"
        onClick={() => {
          onEdgeClick?.({}, { id: 'edge1', source: 'room1', target: 'room2', data: {} });
        }}
      >
        Trigger Edge Click
      </button>
    </div>
  ),
  Background: () => <div data-testid="background" />,
  Controls: () => <div data-testid="controls" />,
  MiniMap: () => <div data-testid="minimap" />,
}));

vi.mock('../hooks/useMapLayout', () => ({
  useMapLayout: () => ({
    layoutNodes: [
      {
        id: 'room1',
        type: 'room',
        position: { x: 0, y: 0 },
        data: { id: 'room1', name: 'Room 1' },
      },
    ],
  }),
}));

vi.mock('../hooks/useMapEditing', () => ({
  useMapEditing: () => buildUseMapEditingMockReturn(),
}));

vi.mock('../MapControls', () => ({
  MapControls: ({
    onSearchChange,
    onPlaneChange,
    onZoneChange,
    onSubZoneChange,
  }: {
    onSearchChange?: (value: string) => void;
    onPlaneChange?: (value: string) => void;
    onZoneChange?: (value: string) => void;
    onSubZoneChange?: (value: string) => void;
  }) => (
    <div data-testid="map-controls">
      <input data-testid="search-input" onChange={e => onSearchChange?.(e.target.value)} placeholder="Search" />
      <input data-testid="plane-input" onChange={e => onPlaneChange?.(e.target.value)} placeholder="Plane" />
      <input data-testid="zone-input" onChange={e => onZoneChange?.(e.target.value)} placeholder="Zone" />
      <input data-testid="subzone-input" onChange={e => onSubZoneChange?.(e.target.value)} placeholder="Sub Zone" />
    </div>
  ),
}));

vi.mock('../MapEditToolbar', () => ({
  MapEditToolbar: ({
    onSave,
    onReset,
    hasUnsavedChanges,
    canUndo,
    canRedo,
    onUndo,
    onRedo,
  }: {
    onSave?: () => void;
    onReset?: () => void;
    hasUnsavedChanges?: boolean;
    canUndo?: boolean;
    canRedo?: boolean;
    onUndo?: () => void;
    onRedo?: () => void;
  }) => (
    <div data-testid="map-edit-toolbar">
      <button data-testid="save-button" onClick={onSave} disabled={!hasUnsavedChanges}>
        Save
      </button>
      <button data-testid="reset-button" onClick={onReset}>
        Reset
      </button>
      <button data-testid="undo-button" onClick={onUndo} disabled={!canUndo}>
        Undo
      </button>
      <button data-testid="redo-button" onClick={onRedo} disabled={!canRedo}>
        Redo
      </button>
    </div>
  ),
}));

vi.mock('../EdgeCreationModal', () => ({
  EdgeCreationModal: ({
    isOpen,
    onClose,
    onCreate,
  }: {
    isOpen?: boolean;
    onClose?: () => void;
    onCreate?: (edge: { sourceRoomId: string; targetRoomId: string; direction: string }) => void;
  }) =>
    isOpen ? (
      <div data-testid="edge-creation-modal">
        <button data-testid="close-edge-modal" onClick={onClose}>
          Close
        </button>
        <button
          data-testid="create-edge"
          onClick={() => {
            onCreate?.({ sourceRoomId: 'room1', targetRoomId: 'room2', direction: 'north' });
          }}
        >
          Create Edge
        </button>
      </div>
    ) : null,
}));

vi.mock('../EdgeDetailsPanel', () => ({
  EdgeDetailsPanel: ({
    edge,
    onClose,
    onDelete,
    onEdit,
  }: {
    edge?: { id: string };
    onClose?: () => void;
    onDelete?: (id: string) => void;
    onEdit?: (id: string) => void;
  }) =>
    edge ? (
      <div data-testid="edge-details-panel">
        <button data-testid="close-edge-panel" onClick={onClose}>
          Close
        </button>
        <button data-testid="delete-edge" onClick={() => onDelete?.(edge.id)}>
          Delete
        </button>
        <button data-testid="edit-edge" onClick={() => onEdit?.(edge.id)}>
          Edit
        </button>
      </div>
    ) : null,
}));

vi.mock('../RoomDetailsPanel', () => ({
  RoomDetailsPanel: ({
    room,
    onClose,
    onEdit,
  }: {
    room?: { id: string; name: string };
    onClose?: () => void;
    onEdit?: (id: string) => void;
  }) =>
    room ? (
      <div data-testid="room-details-panel">
        <div data-testid="room-name">{room.name}</div>
        <button data-testid="close-room-panel" onClick={onClose}>
          Close
        </button>
        <button data-testid="edit-room" onClick={() => onEdit?.(room.id)}>
          Edit
        </button>
      </div>
    ) : null,
}));

vi.mock('../RoomEditModal', () => ({
  RoomEditModal: ({
    isOpen,
    room,
    onClose,
    onSave,
  }: {
    isOpen?: boolean;
    room?: { id: string };
    onClose?: () => void;
    onSave?: (id: string, data: { name: string }) => void;
  }) =>
    isOpen ? (
      <div data-testid="room-edit-modal">
        <button data-testid="close-room-modal" onClick={onClose}>
          Close
        </button>
        <button
          data-testid="save-room"
          onClick={() => {
            onSave?.(room?.id || '', { name: 'Updated Room' });
          }}
        >
          Save
        </button>
      </div>
    ) : null,
}));

vi.mock('../../utils/config', () => ({
  getApiBaseUrl: () => 'http://localhost:54731',
}));

vi.mock('../utils/saveMapChanges', () => ({
  saveMapChanges: vi.fn(() => Promise.resolve()),
}));
