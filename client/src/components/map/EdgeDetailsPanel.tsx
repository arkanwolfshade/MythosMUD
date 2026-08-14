/**
 * Edge Details Panel component.
 */

import React, { useState } from 'react';
import type { Edge } from 'reactflow';
import type { ExitEdgeData } from './types';

export interface EdgeDetailsPanelProps {
  edge: Edge<ExitEdgeData>;
  sourceRoomName?: string;
  targetRoomName?: string;
  onClose: () => void;
  onDelete?: (edgeId: string) => void;
  onEdit?: (edgeId: string) => void;
  isAdmin?: boolean;
}

interface EdgeDetailRowProps {
  label: string;
  value: string;
  mono?: boolean;
  medium?: boolean;
  className?: string;
}

interface OptionalEdgeDetailRowProps {
  label: string;
  value?: string;
  mono?: boolean;
  medium?: boolean;
  className?: string;
}

interface EdgeDetailsFieldsProps {
  edge: Edge<ExitEdgeData>;
  sourceRoomName?: string;
  targetRoomName?: string;
}

interface EdgeAdminActionsProps {
  edgeId: string;
  showDeleteConfirm: boolean;
  onEdit?: (edgeId: string) => void;
  onDelete?: (edgeId: string) => void;
  onClose: () => void;
  onConfirmDelete: () => void;
  onCancelDelete: () => void;
}

interface EdgeFieldModel {
  id: string;
  direction?: string;
  fromName: string;
  toName: string;
  flags: string[];
  description?: string;
}

interface EdgeFlagsProps {
  flags: string[];
}

interface EdgeDeleteConfirmProps {
  onConfirmDelete: () => void;
  onCancelDelete: () => void;
}

function roomLabel(name: string | undefined, fallback: string): string {
  if (name) {
    return name;
  }
  return fallback;
}

function flagsFromData(data: ExitEdgeData | undefined): string[] {
  if (!data || !data.flags) {
    return [];
  }
  return data.flags;
}

function buildEdgeFieldModel(props: EdgeDetailsFieldsProps): EdgeFieldModel {
  const data = props.edge.data;
  return {
    id: props.edge.id,
    direction: data ? data.direction : undefined,
    fromName: roomLabel(props.sourceRoomName, props.edge.source),
    toName: roomLabel(props.targetRoomName, props.edge.target),
    flags: flagsFromData(data),
    description: data ? data.description : undefined,
  };
}

function edgeDetailValueClass(mono: boolean, medium: boolean): string {
  if (mono) {
    return ' font-mono';
  }
  if (medium) {
    return ' font-medium';
  }
  return '';
}

function EdgeDetailRow(props: EdgeDetailRowProps): React.ReactElement {
  const valueClass = edgeDetailValueClass(Boolean(props.mono), Boolean(props.medium));
  const rowClass = props.className ? props.className : 'mb-2';
  return (
    <div className={rowClass}>
      <span className="text-xs text-mythos-terminal-text/70">{props.label}</span>
      <div className={`text-sm text-mythos-terminal-text${valueClass}`}>{props.value}</div>
    </div>
  );
}

function OptionalEdgeDetailRow(props: OptionalEdgeDetailRowProps): React.ReactElement | null {
  if (!props.value) {
    return null;
  }
  return (
    <EdgeDetailRow
      label={props.label}
      value={props.value}
      mono={props.mono}
      medium={props.medium}
      className={props.className}
    />
  );
}

function EdgeFlagsSection(props: EdgeFlagsProps): React.ReactElement {
  return (
    <div className="mb-4">
      <span className="text-xs text-mythos-terminal-text/70">Flags:</span>
      <div className="text-sm text-mythos-terminal-text mt-1">
        <div className="flex flex-wrap gap-1">
          {props.flags.map(flag => (
            <span
              key={flag}
              className="px-2 py-1 bg-mythos-terminal-surface border border-mythos-terminal-border rounded text-xs"
            >
              {flag}
            </span>
          ))}
        </div>
      </div>
    </div>
  );
}

function EdgeFlagsIfAny(props: EdgeFlagsProps): React.ReactElement | null {
  if (props.flags.length === 0) {
    return null;
  }
  return <EdgeFlagsSection flags={props.flags} />;
}

function EdgeDetailsFields(props: EdgeDetailsFieldsProps): React.ReactElement {
  const model = buildEdgeFieldModel(props);
  return (
    <React.Fragment>
      <EdgeDetailRow label="Edge ID:" value={model.id} mono />
      <OptionalEdgeDetailRow label="Direction:" value={model.direction} medium />
      <EdgeDetailRow label="From:" value={model.fromName} />
      <EdgeDetailRow label="To:" value={model.toName} className="mb-4" />
      <EdgeFlagsIfAny flags={model.flags} />
      <OptionalEdgeDetailRow label="Description:" value={model.description} className="mb-4" />
    </React.Fragment>
  );
}

function EdgeDeleteConfirm(props: EdgeDeleteConfirmProps): React.ReactElement {
  return (
    <div className="space-y-2">
      <div className="text-sm text-mythos-terminal-text mb-2">Are you sure you want to delete this exit?</div>
      <div className="flex gap-2">
        <button
          onClick={props.onConfirmDelete}
          className="flex-1 px-3 py-2 bg-mythos-terminal-error text-white rounded hover:bg-mythos-terminal-error/80 text-sm"
        >
          Confirm Delete
        </button>
        <button
          onClick={props.onCancelDelete}
          className="flex-1 px-3 py-2 bg-mythos-terminal-background border border-mythos-terminal-border text-mythos-terminal-text rounded hover:bg-mythos-terminal-surface text-sm"
        >
          Cancel
        </button>
      </div>
    </div>
  );
}

function EdgeAdminReadyActions(props: EdgeAdminActionsProps): React.ReactElement {
  return (
    <React.Fragment>
      {props.onEdit ? (
        <button
          onClick={() => {
            if (props.onEdit) {
              props.onEdit(props.edgeId);
            }
            props.onClose();
          }}
          className="w-full px-3 py-2 bg-mythos-terminal-primary text-white rounded hover:bg-mythos-terminal-primary/80 text-sm"
        >
          Edit Exit
        </button>
      ) : null}
      {props.onDelete ? (
        <button
          onClick={props.onConfirmDelete}
          className="w-full px-3 py-2 bg-mythos-terminal-error text-white rounded hover:bg-mythos-terminal-error/80 text-sm"
        >
          Delete Exit
        </button>
      ) : null}
    </React.Fragment>
  );
}

function EdgeAdminActions(props: EdgeAdminActionsProps): React.ReactElement {
  if (props.showDeleteConfirm) {
    return <EdgeDeleteConfirm onConfirmDelete={props.onConfirmDelete} onCancelDelete={props.onCancelDelete} />;
  }
  return <EdgeAdminReadyActions {...props} />;
}

export const EdgeDetailsPanel: React.FC<EdgeDetailsPanelProps> = props => {
  const { edge, sourceRoomName, targetRoomName, onClose, onDelete, onEdit, isAdmin = false } = props;
  const [showDeleteConfirm, setShowDeleteConfirm] = useState(false);

  const handleDelete = () => {
    if (onDelete && showDeleteConfirm) {
      onDelete(edge.id);
      setShowDeleteConfirm(false);
      onClose();
      return;
    }
    setShowDeleteConfirm(true);
  };

  return (
    <div className="absolute top-4 right-4 w-80 bg-mythos-terminal-background border border-mythos-terminal-border rounded shadow-lg p-4 z-20 max-h-panel overflow-y-auto">
      <div className="flex justify-between items-start mb-4">
        <h3 className="text-lg font-bold text-mythos-terminal-text">Exit Details</h3>
        <button
          onClick={onClose}
          className="text-mythos-terminal-text hover:text-mythos-terminal-error"
          aria-label="Close panel"
        >
          ×
        </button>
      </div>
      <EdgeDetailsFields edge={edge} sourceRoomName={sourceRoomName} targetRoomName={targetRoomName} />
      {isAdmin ? (
        <div className="space-y-2 pt-4 border-t border-mythos-terminal-border">
          <EdgeAdminActions
            edgeId={edge.id}
            showDeleteConfirm={showDeleteConfirm}
            onEdit={onEdit}
            onDelete={onDelete}
            onClose={onClose}
            onConfirmDelete={handleDelete}
            onCancelDelete={() => setShowDeleteConfirm(false)}
          />
        </div>
      ) : null}
    </div>
  );
};
