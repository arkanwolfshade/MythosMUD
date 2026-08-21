/**
 * Room Map Editor component (Admin Edit Mode).
 *
 * This component provides admin editing capabilities for the map, including
 * node repositioning, edge creation/deletion, and property editing.
 *
 * As documented in the Pnakotic Manuscripts, proper management of dimensional
 * modifications is essential for maintaining the integrity of our eldritch architecture.
 */

import React from 'react';
import ReactFlow, {
  Background,
  Controls,
  MiniMap,
  type Edge,
  type EdgeChange,
  type Node,
  type NodeChange,
} from 'reactflow';
import 'reactflow/dist/style.css';
import { EdgeCreationModal } from './EdgeCreationModal';
import { EdgeDetailsPanel } from './EdgeDetailsPanel';
import { MapControls } from './MapControls';
import { MapEditToolbar } from './MapEditToolbar';
import { RoomDetailsPanel } from './RoomDetailsPanel';
import { RoomEditModal } from './RoomEditModal';
import { edgeTypes, nodeTypes } from './config';
import { useMapEditing } from './hooks/useMapEditing';
import type { ExitEdgeData, RoomNodeData } from './types';
import {
  MAP_EDITOR_DIRECTIONS,
  useRoomMapEditorData,
  useRoomMapEditorEditing,
  useRoomMapEditorModals,
  useRoomMapEditorSelection,
  type RoomMapEditorProps,
} from './RoomMapEditorRuntime.hooks';

export type { RoomMapEditorProps };

function RoomMapEditorFlow({
  flow,
}: {
  flow: {
    editedNodes: Node<RoomNodeData>[];
    editedEdges: Edge<ExitEdgeData>[];
    previewEdge: Edge<ExitEdgeData> | null;
    onNodesChange: (changes: NodeChange[]) => void;
    onEdgesChange: (changes: EdgeChange[]) => void;
    onNodeClick: (event: React.MouseEvent, node: Node<RoomNodeData>) => void;
    onEdgeClick: (event: React.MouseEvent, edge: Edge<ExitEdgeData>) => void;
  };
}) {
  const { editedNodes, editedEdges, previewEdge, onNodesChange, onEdgesChange, onNodeClick, onEdgeClick } = flow;
  return (
    <div
      className="relative h-full w-full"
      style={{ backgroundColor: 'var(--color-mythos-terminal-background, #0a0a0a)' }}
    >
      <ReactFlow
        nodes={editedNodes}
        edges={[...editedEdges, ...(previewEdge ? [previewEdge] : [])]}
        nodeTypes={nodeTypes}
        edgeTypes={edgeTypes}
        onNodesChange={onNodesChange}
        onEdgesChange={onEdgesChange}
        onNodeClick={onNodeClick}
        onEdgeClick={onEdgeClick}
        nodesDraggable={true}
        nodesConnectable={false}
        elementsSelectable={true}
        edgesFocusable={true}
        fitView
        className="bg-mythos-terminal-background"
        onlyRenderVisibleElements={true}
        proOptions={{ hideAttribution: true }}
      >
        <Controls className="bg-mythos-terminal-background border border-mythos-terminal-border" />
        <Background style={{ backgroundColor: 'var(--color-mythos-terminal-background, #0a0a0a)', opacity: 1 }} />
        <MiniMap
          className="bg-mythos-terminal-background border border-mythos-terminal-border"
          nodeColor={node => {
            if (node.data?.isCurrentLocation) return '#10b981';
            if (node.data?.hasUnsavedChanges) return '#fbbf24';
            return '#6b7280';
          }}
        />
      </ReactFlow>
    </div>
  );
}

function RoomMapEditorDetailPanels({
  editedNodes,
  validateEdgeCreation,
  selection,
  modals,
}: {
  editedNodes: Node<RoomNodeData>[];
  validateEdgeCreation: ReturnType<typeof useMapEditing>['validateEdgeCreation'];
  selection: ReturnType<typeof useRoomMapEditorSelection>;
  modals: ReturnType<typeof useRoomMapEditorModals>;
}) {
  const { selectedRoomId, selectedRoom, selectedEdge } = selection;
  const edgeSourceRoomName = selectedEdge
    ? editedNodes.find(node => node.id === selectedEdge.source)?.data.name
    : undefined;
  const edgeTargetRoomName = selectedEdge
    ? editedNodes.find(node => node.id === selectedEdge.target)?.data.name
    : undefined;

  return (
    <>
      {selectedRoom && (
        <RoomDetailsPanel
          room={selectedRoom}
          onClose={modals.handleClosePanel}
          onEditRoom={modals.handleEditRoom}
          onCreateExit={() => {
            if (selectedRoomId) modals.setIsEdgeCreationOpen(true);
          }}
          isAdmin={true}
        />
      )}
      {selectedEdge && (
        <EdgeDetailsPanel
          edge={selectedEdge}
          sourceRoomName={edgeSourceRoomName}
          targetRoomName={edgeTargetRoomName}
          onClose={modals.handleCloseEdgePanel}
          onDelete={modals.handleDeleteEdge}
          onEdit={modals.handleEditEdge}
          isAdmin={true}
        />
      )}
      {selectedRoomId && (
        <EdgeCreationModal
          isOpen={modals.isEdgeCreationOpen}
          onClose={() => {
            modals.setIsEdgeCreationOpen(false);
            modals.clearPreview();
          }}
          sourceRoomId={selectedRoomId}
          availableNodes={editedNodes}
          availableDirections={MAP_EDITOR_DIRECTIONS}
          validation={modals.edgeValidation}
          onCreate={modals.handleCreateEdge}
          onValidate={validateEdgeCreation}
          onPreviewChange={modals.handlePreviewChange}
        />
      )}
      {modals.editingEdgeData && (
        <EdgeCreationModal
          isOpen={modals.isEdgeEditOpen}
          onClose={() => {
            modals.setIsEdgeEditOpen(false);
            modals.setEditingEdgeDataState(null);
            modals.clearPreview();
          }}
          sourceRoomId={modals.editingEdgeData.sourceRoomId}
          availableNodes={editedNodes}
          availableDirections={MAP_EDITOR_DIRECTIONS}
          validation={modals.edgeValidation}
          onCreate={modals.handleCreateEdge}
          onValidate={validateEdgeCreation}
          onPreviewChange={modals.handlePreviewChange}
          existingEdge={modals.editingEdgeData}
          onUpdate={modals.handleUpdateEdge}
        />
      )}
      {modals.editingRoom && (
        <RoomEditModal
          isOpen={modals.isRoomEditOpen}
          onClose={() => {
            modals.setIsRoomEditOpen(false);
            modals.setEditingRoomId(null);
          }}
          room={modals.editingRoom}
          onUpdate={modals.handleUpdateRoom}
        />
      )}
    </>
  );
}

type MapEditorData = ReturnType<typeof useRoomMapEditorData>;
type MapEditorEditing = ReturnType<typeof useRoomMapEditorEditing>;
type MapEditorSelection = ReturnType<typeof useRoomMapEditorSelection>;
type MapEditorModals = ReturnType<typeof useRoomMapEditorModals>;

interface RoomMapEditorChromeProps {
  data: MapEditorData;
  editing: MapEditorEditing;
}

interface RoomMapEditorLoadedViewProps {
  data: MapEditorData;
  editing: MapEditorEditing;
  selection: MapEditorSelection;
  modals: MapEditorModals;
}

function uniqueSubZones(rooms: MapEditorData['rooms']): string[] {
  const values = rooms.map(r => r.sub_zone).filter((sub): sub is string => typeof sub === 'string' && sub.length > 0);
  return Array.from(new Set(values));
}

function RoomMapEditorChrome({ data, editing }: RoomMapEditorChromeProps) {
  const {
    plane,
    zone,
    rooms,
    error,
    refetch,
    searchQuery,
    setSearchQuery,
    selectedPlane,
    selectedZone,
    selectedSubZone,
    setSelectedPlane,
    setSelectedZone,
    setSelectedSubZone,
  } = data;
  const { hasUnsavedChanges, canUndo, canRedo, undo, redo, save, reset } = editing;
  const availableSubZones = uniqueSubZones(rooms);

  return (
    <>
      {error ? (
        <div className="absolute top-0 left-0 right-0 bg-mythos-terminal-error text-white p-2 text-center z-50">
          {error}
        </div>
      ) : null}
      <div className="absolute top-4 right-4 z-10">
        <MapEditToolbar
          hasUnsavedChanges={hasUnsavedChanges}
          canUndo={canUndo}
          canRedo={canRedo}
          onUndo={undo}
          onRedo={redo}
          onSave={save}
          onReset={reset}
          onSaveFailed={() => {
            void refetch();
          }}
        />
      </div>
      <div className="absolute top-4 left-4 z-10">
        <MapControls
          searchQuery={searchQuery}
          onSearchChange={setSearchQuery}
          plane={selectedPlane}
          zone={selectedZone}
          subZone={selectedSubZone}
          onPlaneChange={setSelectedPlane}
          onZoneChange={setSelectedZone}
          onSubZoneChange={setSelectedSubZone}
          availablePlanes={[plane]}
          availableZones={[zone]}
          availableSubZones={availableSubZones}
        />
      </div>
    </>
  );
}

function RoomMapEditorLoadedView({ data, editing, selection, modals }: RoomMapEditorLoadedViewProps) {
  const { nodes: editedNodes, edges: editedEdges, onNodesChange, onEdgesChange, validateEdgeCreation } = editing;
  const { handleNodeClick, handleEdgeClick } = selection;

  return (
    <div className="relative h-full w-full bg-mythos-terminal-background">
      <RoomMapEditorChrome data={data} editing={editing} />
      <RoomMapEditorFlow
        flow={{
          editedNodes,
          editedEdges,
          previewEdge: modals.previewEdge,
          onNodesChange,
          onEdgesChange,
          onNodeClick: handleNodeClick,
          onEdgeClick: handleEdgeClick,
        }}
      />
      <RoomMapEditorDetailPanels
        editedNodes={editedNodes}
        validateEdgeCreation={validateEdgeCreation}
        selection={selection}
        modals={modals}
      />
    </div>
  );
}

export function RoomMapEditor(props: RoomMapEditorProps) {
  const data = useRoomMapEditorData(props);
  const editing = useRoomMapEditorEditing(
    data.initialLayoutNodes,
    data.rawEdges as Edge<ExitEdgeData>[],
    props.authToken,
    props.baseUrl
  );
  const selection = useRoomMapEditorSelection(data.rooms, editing.edges, props.onRoomSelect);
  const modals = useRoomMapEditorModals(data.rooms, editing.edges, editing, selection);

  if (data.isLoading) {
    return (
      <div className="flex items-center justify-center h-full w-full bg-mythos-terminal-background">
        <div className="text-mythos-terminal-text">Loading map...</div>
      </div>
    );
  }
  if (data.error) {
    return (
      <div className="flex flex-col items-center justify-center h-full w-full bg-mythos-terminal-background p-4">
        <div className="text-mythos-terminal-error mb-4">Error: {data.error}</div>
        <button
          onClick={() => data.refetch()}
          className="px-4 py-2 bg-mythos-terminal-primary text-white rounded hover:bg-mythos-terminal-primary/80"
        >
          Retry
        </button>
      </div>
    );
  }
  if (data.filteredRooms.length === 0) {
    return (
      <div className="flex flex-col items-center justify-center h-full w-full bg-mythos-terminal-background p-4">
        <div className="text-mythos-terminal-text mb-4">
          {data.searchQuery ? 'No rooms found matching your search.' : 'No rooms available in this area.'}
        </div>
        {data.searchQuery && (
          <button
            onClick={() => {
              data.setSearchQuery('');
            }}
            className="px-4 py-2 bg-mythos-terminal-primary text-white rounded hover:bg-mythos-terminal-primary/80"
          >
            Clear Search
          </button>
        )}
      </div>
    );
  }

  return <RoomMapEditorLoadedView data={data} editing={editing} selection={selection} modals={modals} />;
}
