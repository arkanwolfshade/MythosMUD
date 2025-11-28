/**
 * Edge Details Panel component.
 *
 * Displays information about a selected exit edge and provides
 * deletion functionality for admins.
 *
 * As documented in the Pnakotic Manuscripts, proper management of
 * dimensional connections is essential for maintaining the integrity
 * of our eldritch architecture.
 */

import React, { useState } from 'react';
import type { Edge } from 'reactflow';
import type { ExitEdgeData } from './types';

export interface EdgeDetailsPanelProps {
  /** Edge data to display */
  edge: Edge<ExitEdgeData>;
  /** Source room name */
  sourceRoomName?: string;
  /** Target room name */
  targetRoomName?: string;
  /** Callback when panel is closed */
  onClose: () => void;
  /** Callback when edge should be deleted (admin only) */
  onDelete?: (edgeId: string) => void;
  /** Callback when edge should be edited (admin only) */
  onEdit?: (edgeId: string) => void;
  /** Whether user is admin (shows delete/edit buttons) */
  isAdmin?: boolean;
}

/**
 * Edge Details Panel component.
 */
export const EdgeDetailsPanel: React.FC<EdgeDetailsPanelProps> = ({
  edge,
  sourceRoomName,
  targetRoomName,
  onClose,
  onDelete,
  onEdit,
  isAdmin = false,
}) => {
  const [showDeleteConfirm, setShowDeleteConfirm] = useState(false);

  const handleDelete = () => {
    if (onDelete && showDeleteConfirm) {
      onDelete(edge.id);
      setShowDeleteConfirm(false);
      onClose();
    } else {
      setShowDeleteConfirm(true);
    }
  };

  const handleCancelDelete = () => {
    setShowDeleteConfirm(false);
  };

  return (
    <div className="absolute top-4 right-4 w-80 bg-mythos-terminal-background border border-mythos-terminal-border rounded shadow-lg p-4 z-20 max-h-[80vh] overflow-y-auto">
      {/* Header */}
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

      {/* Edge ID */}
      <div className="mb-2">
        <span className="text-xs text-mythos-terminal-text/70">Edge ID:</span>
        <div className="text-sm text-mythos-terminal-text font-mono">{edge.id}</div>
      </div>

      {/* Direction */}
      {edge.data?.direction && (
        <div className="mb-2">
          <span className="text-xs text-mythos-terminal-text/70">Direction:</span>
          <div className="text-sm text-mythos-terminal-text font-medium">{edge.data.direction}</div>
        </div>
      )}

      {/* Source room */}
      <div className="mb-2">
        <span className="text-xs text-mythos-terminal-text/70">From:</span>
        <div className="text-sm text-mythos-terminal-text">{sourceRoomName || edge.source}</div>
      </div>

      {/* Target room */}
      <div className="mb-4">
        <span className="text-xs text-mythos-terminal-text/70">To:</span>
        <div className="text-sm text-mythos-terminal-text">{targetRoomName || edge.target}</div>
      </div>

      {/* Flags */}
      {edge.data?.flags && edge.data.flags.length > 0 && (
        <div className="mb-4">
          <span className="text-xs text-mythos-terminal-text/70">Flags:</span>
          <div className="text-sm text-mythos-terminal-text mt-1">
            <div className="flex flex-wrap gap-1">
              {edge.data.flags.map(flag => (
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
      )}

      {/* Description */}
      {edge.data?.description && (
        <div className="mb-4">
          <span className="text-xs text-mythos-terminal-text/70">Description:</span>
          <div className="text-sm text-mythos-terminal-text mt-1">{edge.data.description}</div>
        </div>
      )}

      {/* Admin actions */}
      {isAdmin && (
        <div className="space-y-2 pt-4 border-t border-mythos-terminal-border">
          {!showDeleteConfirm ? (
            <>
              {onEdit && (
                <button
                  onClick={() => {
                    onEdit(edge.id);
                    onClose();
                  }}
                  className="w-full px-3 py-2 bg-mythos-terminal-primary text-white rounded hover:bg-mythos-terminal-primary/80 text-sm"
                >
                  Edit Exit
                </button>
              )}
              {onDelete && (
                <button
                  onClick={handleDelete}
                  className="w-full px-3 py-2 bg-mythos-terminal-error text-white rounded hover:bg-mythos-terminal-error/80 text-sm"
                >
                  Delete Exit
                </button>
              )}
            </>
          ) : (
            <div className="space-y-2">
              <div className="text-sm text-mythos-terminal-text mb-2">Are you sure you want to delete this exit?</div>
              <div className="flex gap-2">
                <button
                  onClick={handleDelete}
                  className="flex-1 px-3 py-2 bg-mythos-terminal-error text-white rounded hover:bg-mythos-terminal-error/80 text-sm"
                >
                  Confirm Delete
                </button>
                <button
                  onClick={handleCancelDelete}
                  className="flex-1 px-3 py-2 bg-mythos-terminal-background border border-mythos-terminal-border text-mythos-terminal-text rounded hover:bg-mythos-terminal-surface text-sm"
                >
                  Cancel
                </button>
              </div>
            </div>
          )}
        </div>
      )}
    </div>
  );
};
