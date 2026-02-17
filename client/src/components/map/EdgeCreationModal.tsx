/**
 * Edge Creation Modal component.
 *
 * Provides a form dialog for creating new exit edges between rooms.
 * Includes real-time validation and preview functionality.
 *
 * As documented in the Pnakotic Manuscripts, proper management of
 * dimensional connections is essential for maintaining the integrity
 * of our eldritch architecture.
 */

import React, { useCallback, useEffect, useMemo, useState } from 'react';
import type { Node } from 'reactflow';
import type { EdgeCreationData, EdgeValidationResult } from './hooks/useMapEditing';
import type { RoomNodeData } from './types';

export interface EdgeCreationModalProps {
  /** Whether the modal is open */
  isOpen: boolean;
  /** Callback when modal should close */
  onClose: () => void;
  /** Source room ID (pre-selected) */
  sourceRoomId: string;
  /** Available nodes for target selection */
  availableNodes: Node<RoomNodeData>[];
  /** Available directions */
  availableDirections: string[];
  /** Current validation result */
  validation: EdgeValidationResult | null;
  /** Callback when edge should be created */
  onCreate: (edgeData: EdgeCreationData) => void;
  /** Callback to validate edge creation */
  onValidate: (edgeData: EdgeCreationData) => EdgeValidationResult;
  /** Callback when edge data changes (for preview) */
  onPreviewChange?: (edgeData: EdgeCreationData | null) => void;
  /** Existing edge data for editing mode */
  existingEdge?: EdgeCreationData & { edgeId: string };
  /** Callback when edge should be updated (edit mode) */
  onUpdate?: (edgeId: string, edgeData: EdgeCreationData) => void;
}

/**
 * Standard exit directions.
 */
const STANDARD_DIRECTIONS = [
  'north',
  'south',
  'east',
  'west',
  'northeast',
  'northwest',
  'southeast',
  'southwest',
  'up',
  'down',
  'in',
  'out',
];

/**
 * Edge Creation Modal component.
 */
export const EdgeCreationModal: React.FC<EdgeCreationModalProps> = ({
  isOpen,
  onClose,
  sourceRoomId,
  availableNodes,
  availableDirections,
  validation,
  onCreate,
  onValidate,
  onPreviewChange,
  existingEdge,
  onUpdate,
}) => {
  const isEditMode = !!existingEdge;

  const [targetRoomId, setTargetRoomId] = useState(existingEdge?.targetRoomId || '');
  const [direction, setDirection] = useState(existingEdge?.direction || '');
  const [customDirection, setCustomDirection] = useState(
    existingEdge && !STANDARD_DIRECTIONS.includes(existingEdge.direction) ? existingEdge.direction : ''
  );
  const [searchQuery, setSearchQuery] = useState('');
  const [flags, setFlags] = useState<string[]>(existingEdge?.flags || []);
  const [description, setDescription] = useState(existingEdge?.description || '');
  const [useCustomDirection, setUseCustomDirection] = useState(
    existingEdge ? !STANDARD_DIRECTIONS.includes(existingEdge.direction) : false
  );

  // Get source room data
  const sourceRoom = useMemo(() => {
    return availableNodes.find(node => node.id === sourceRoomId);
  }, [availableNodes, sourceRoomId]);

  // Filter nodes by search query
  const filteredNodes = useMemo(() => {
    if (!searchQuery.trim()) {
      return availableNodes.filter(node => node.id !== sourceRoomId);
    }

    const query = searchQuery.toLowerCase();
    return availableNodes.filter(
      node =>
        node.id !== sourceRoomId &&
        (node.data.name?.toLowerCase().includes(query) ||
          node.id.toLowerCase().includes(query) ||
          node.data.zone?.toLowerCase().includes(query) ||
          node.data.subZone?.toLowerCase().includes(query))
    );
  }, [availableNodes, sourceRoomId, searchQuery]);

  // Current edge data for validation
  const currentEdgeData = useMemo<EdgeCreationData | null>(() => {
    if (!targetRoomId || (!direction && !useCustomDirection) || (!useCustomDirection && !direction)) {
      return null;
    }

    return {
      sourceRoomId,
      targetRoomId,
      direction: useCustomDirection ? customDirection : direction,
      flags: flags.length > 0 ? flags : undefined,
      description: description.trim() || undefined,
    };
  }, [sourceRoomId, targetRoomId, direction, customDirection, useCustomDirection, flags, description]);

  // Validate on change
  useEffect(() => {
    if (currentEdgeData && targetRoomId && (direction || (useCustomDirection && customDirection))) {
      onValidate(currentEdgeData);
      onPreviewChange?.(currentEdgeData);
    } else {
      onPreviewChange?.(null);
    }
  }, [currentEdgeData, targetRoomId, direction, customDirection, useCustomDirection, onValidate, onPreviewChange]);

  // Handle ESC key
  useEffect(() => {
    if (!isOpen) return;

    const handleEscape = (event: KeyboardEvent) => {
      if (event.key === 'Escape') {
        onClose();
      }
    };

    window.addEventListener('keydown', handleEscape);
    return () => {
      window.removeEventListener('keydown', handleEscape);
    };
  }, [isOpen, onClose]);

  // Prevent body scroll
  useEffect(() => {
    if (isOpen) {
      document.body.style.overflow = 'hidden';
    } else {
      document.body.style.overflow = '';
    }
    return () => {
      document.body.style.overflow = '';
    };
  }, [isOpen]);

  // Reset form when modal closes
  // Note: This is a legitimate use case for setState in effect (form reset on modal close)
  // The performance impact is minimal and this pattern is commonly used
  useEffect(() => {
    if (!isOpen) {
      // Reset form state when modal closes
      // eslint-disable-next-line react-hooks/set-state-in-effect -- Reset form state on modal close
      setTargetRoomId('');

      setDirection('');

      setCustomDirection('');

      setSearchQuery('');

      setFlags([]);

      setDescription('');

      setUseCustomDirection(false);
      onPreviewChange?.(null);
    }
  }, [isOpen, onPreviewChange]);

  // Handle form submission
  const handleSubmit = useCallback(
    (e: React.FormEvent) => {
      e.preventDefault();

      if (!currentEdgeData) {
        return;
      }

      const result = onValidate(currentEdgeData);
      if (!result.isValid) {
        return;
      }

      if (isEditMode && existingEdge && onUpdate) {
        onUpdate(existingEdge.edgeId, currentEdgeData);
      } else {
        onCreate(currentEdgeData);
      }
      onClose();
    },
    [currentEdgeData, onCreate, onValidate, onClose, isEditMode, existingEdge, onUpdate]
  );

  // Toggle flag
  const toggleFlag = useCallback((flag: string) => {
    setFlags(prev => (prev.includes(flag) ? prev.filter(f => f !== flag) : [...prev, flag]));
  }, []);

  if (!isOpen) return null;

  const effectiveDirections = availableDirections.length > 0 ? availableDirections : STANDARD_DIRECTIONS;
  const canSubmit = currentEdgeData !== null && validation?.isValid === true;

  return (
    <div
      className="fixed inset-0 bg-black bg-opacity-75 flex items-center justify-center z-50"
      onClick={onClose}
      role="dialog"
      aria-modal="true"
      aria-labelledby="edge-creation-title"
    >
      <div
        className="bg-mythos-terminal-background border-2 border-mythos-terminal-border rounded-lg p-6 w-full max-w-2xl max-h-modal overflow-y-auto shadow-xl"
        onClick={e => {
          e.stopPropagation();
        }}
      >
        {/* Header */}
        <div className="flex items-center justify-between mb-6">
          <h2 id="edge-creation-title" className="text-2xl font-bold text-mythos-terminal-text">
            Create Exit
          </h2>
          <button
            onClick={onClose}
            className="text-mythos-terminal-text hover:text-mythos-terminal-error text-2xl leading-none"
            aria-label="Close dialog"
          >
            ×
          </button>
        </div>

        {/* Source room (read-only) */}
        <div className="mb-4">
          <label className="block text-sm font-medium text-mythos-terminal-text mb-2">From Room:</label>
          <div className="px-3 py-2 bg-mythos-terminal-surface border border-mythos-terminal-border rounded text-mythos-terminal-text">
            {sourceRoom?.data.name || sourceRoomId}
          </div>
        </div>

        {/* Form */}
        <form onSubmit={handleSubmit} className="space-y-4">
          {/* Target room selection */}
          <div>
            <label htmlFor="target-room" className="block text-sm font-medium text-mythos-terminal-text mb-2">
              To Room: <span className="text-mythos-terminal-error">*</span>
            </label>
            <input
              id="target-room-search"
              type="text"
              value={searchQuery}
              onChange={e => {
                setSearchQuery(e.target.value);
              }}
              placeholder="Search rooms..."
              className="w-full px-3 py-2 bg-mythos-terminal-background border border-mythos-terminal-border rounded text-mythos-terminal-text mb-2"
            />
            <select
              id="target-room"
              value={targetRoomId}
              onChange={e => {
                setTargetRoomId(e.target.value);
              }}
              required
              disabled={isEditMode} // Don't allow changing target in edit mode
              className="w-full px-3 py-2 bg-mythos-terminal-background border border-mythos-terminal-border rounded text-mythos-terminal-text disabled:opacity-50 disabled:cursor-not-allowed"
            >
              <option value="">Select target room...</option>
              {filteredNodes.map(node => (
                <option key={node.id} value={node.id}>
                  {node.data.name} ({node.id})
                </option>
              ))}
            </select>
            {isEditMode && (
              <p className="text-xs text-mythos-terminal-text/50 mt-1">
                Target room cannot be changed. Delete and recreate the exit to change the target.
              </p>
            )}
          </div>

          {/* Direction selection */}
          <div>
            <label className="block text-sm font-medium text-mythos-terminal-text mb-2">
              Direction: <span className="text-mythos-terminal-error">*</span>
            </label>
            <div className="flex items-center gap-2 mb-2">
              <input
                type="checkbox"
                id="use-custom-direction"
                checked={useCustomDirection}
                onChange={e => {
                  setUseCustomDirection(e.target.checked);
                }}
                className="w-4 h-4"
              />
              <label htmlFor="use-custom-direction" className="text-sm text-mythos-terminal-text">
                Use custom direction
              </label>
            </div>
            {useCustomDirection ? (
              <input
                type="text"
                value={customDirection}
                onChange={e => {
                  setCustomDirection(e.target.value);
                }}
                placeholder="Enter direction (e.g., 'portal', 'secret')"
                required
                className="w-full px-3 py-2 bg-mythos-terminal-background border border-mythos-terminal-border rounded text-mythos-terminal-text"
              />
            ) : (
              <select
                value={direction}
                onChange={e => {
                  setDirection(e.target.value);
                }}
                required
                className="w-full px-3 py-2 bg-mythos-terminal-background border border-mythos-terminal-border rounded text-mythos-terminal-text"
              >
                <option value="">Select direction...</option>
                {effectiveDirections.map(dir => (
                  <option key={dir} value={dir}>
                    {dir}
                  </option>
                ))}
              </select>
            )}
          </div>

          {/* Exit flags */}
          <div>
            <label className="block text-sm font-medium text-mythos-terminal-text mb-2">Exit Flags:</label>
            <div className="flex flex-wrap gap-2">
              {['one_way', 'hidden', 'locked', 'no_pick', 'no_flee'].map(flag => (
                <label key={flag} className="flex items-center gap-2 cursor-pointer">
                  <input
                    type="checkbox"
                    checked={flags.includes(flag)}
                    onChange={() => {
                      toggleFlag(flag);
                    }}
                    className="w-4 h-4"
                  />
                  <span className="text-sm text-mythos-terminal-text">{flag}</span>
                </label>
              ))}
            </div>
          </div>

          {/* Description */}
          <div>
            <label htmlFor="description" className="block text-sm font-medium text-mythos-terminal-text mb-2">
              Description (optional):
            </label>
            <textarea
              id="description"
              value={description}
              onChange={e => {
                setDescription(e.target.value);
              }}
              placeholder="Exit description..."
              rows={3}
              className="w-full px-3 py-2 bg-mythos-terminal-background border border-mythos-terminal-border rounded text-mythos-terminal-text"
            />
          </div>

          {/* Validation feedback */}
          {validation && (
            <div className="space-y-2">
              {validation.errors.length > 0 && (
                <div className="p-3 bg-mythos-terminal-error/20 border border-mythos-terminal-error rounded">
                  <div className="text-sm font-medium text-mythos-terminal-error mb-1">Errors:</div>
                  <ul className="list-disc list-inside text-sm text-mythos-terminal-error space-y-1">
                    {validation.errors.map((error, index) => (
                      <li key={index}>{error}</li>
                    ))}
                  </ul>
                </div>
              )}
              {validation.warnings.length > 0 && (
                <div className="p-3 bg-yellow-900/20 border border-yellow-600 rounded">
                  <div className="text-sm font-medium text-yellow-400 mb-1">Warnings:</div>
                  <ul className="list-disc list-inside text-sm text-yellow-300 space-y-1">
                    {validation.warnings.map((warning, index) => (
                      <li key={index}>{warning}</li>
                    ))}
                  </ul>
                </div>
              )}
            </div>
          )}

          {/* Actions */}
          <div className="flex justify-end gap-3 pt-4 border-t border-mythos-terminal-border">
            <button
              type="button"
              onClick={onClose}
              className="px-4 py-2 bg-mythos-terminal-background border border-mythos-terminal-border text-mythos-terminal-text rounded hover:bg-mythos-terminal-surface"
            >
              Cancel
            </button>
            <button
              type="submit"
              disabled={!canSubmit}
              className="px-4 py-2 bg-mythos-terminal-primary text-white rounded hover:bg-mythos-terminal-primary/80 disabled:opacity-50 disabled:cursor-not-allowed"
            >
              Create Exit
            </button>
          </div>
        </form>

        <div className="mt-4 text-xs text-mythos-terminal-text/50 text-center">Press ESC to close</div>
      </div>
    </div>
  );
};
