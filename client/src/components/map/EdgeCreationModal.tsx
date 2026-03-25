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

import React, { useCallback, useEffect, useMemo, useState, type Dispatch, type SetStateAction } from 'react';
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

const STANDARD_DIRECTION_SET = new Set(STANDARD_DIRECTIONS);

function isStandardExitDirection(direction: string): boolean {
  return STANDARD_DIRECTION_SET.has(direction);
}

function roomNodeMatchesSearchQuery(node: Node<RoomNodeData>, sourceRoomId: string, queryLower: string): boolean {
  if (node.id === sourceRoomId) {
    return false;
  }
  const fields = [
    node.data.name?.toLowerCase(),
    node.id.toLowerCase(),
    node.data.zone?.toLowerCase(),
    node.data.subZone?.toLowerCase(),
  ];
  return fields.some(field => field?.includes(queryLower));
}

function filterNodesForTargetSelection(
  availableNodes: Node<RoomNodeData>[],
  sourceRoomId: string,
  searchQuery: string
): Node<RoomNodeData>[] {
  if (!searchQuery.trim()) {
    return availableNodes.filter(node => node.id !== sourceRoomId);
  }
  const queryLower = searchQuery.toLowerCase();
  return availableNodes.filter(node => roomNodeMatchesSearchQuery(node, sourceRoomId, queryLower));
}

function findRoomNodeById(availableNodes: Node<RoomNodeData>[], sourceRoomId: string): Node<RoomNodeData> | undefined {
  return availableNodes.find(node => node.id === sourceRoomId);
}

type EdgeFormFields = {
  targetRoomId: string;
  direction: string;
  customDirection: string;
  flags: string[];
  description: string;
  useCustomDirection: boolean;
};

function emptyEdgeFormState(): EdgeFormFields {
  return {
    targetRoomId: '',
    direction: '',
    customDirection: '',
    flags: [],
    description: '',
    useCustomDirection: false,
  };
}

function edgeFormStateFromExisting(existingEdge: EdgeCreationData & { edgeId: string }): EdgeFormFields {
  const dir = existingEdge.direction;
  const useCustom = !isStandardExitDirection(dir);
  return {
    targetRoomId: existingEdge.targetRoomId,
    direction: useCustom ? '' : dir,
    customDirection: useCustom ? dir : '',
    flags: existingEdge.flags || [],
    description: existingEdge.description || '',
    useCustomDirection: useCustom,
  };
}

function getInitialEdgeFormState(existingEdge: (EdgeCreationData & { edgeId: string }) | undefined): EdgeFormFields {
  if (!existingEdge) {
    return emptyEdgeFormState();
  }
  return edgeFormStateFromExisting(existingEdge);
}

function toggleStringFlag(prev: string[], flag: string): string[] {
  return prev.includes(flag) ? prev.filter(f => f !== flag) : [...prev, flag];
}

function edgeFormCanSubmit(
  currentEdgeData: EdgeCreationData | null,
  validation: EdgeValidationResult | null | undefined
): boolean {
  return currentEdgeData !== null && validation?.isValid === true;
}

function deriveEdgeCreationData(
  sourceRoomId: string,
  targetRoomId: string,
  direction: string,
  customDirection: string,
  useCustomDirection: boolean,
  flags: string[],
  description: string
): EdgeCreationData | null {
  if (!targetRoomId) {
    return null;
  }
  const resolvedDirection = useCustomDirection ? customDirection : direction;
  if (!resolvedDirection) {
    return null;
  }
  return {
    sourceRoomId,
    targetRoomId,
    direction: resolvedDirection,
    flags: flags.length > 0 ? flags : undefined,
    description: description.trim() || undefined,
  };
}

function submitValidatedEdge(
  currentEdgeData: EdgeCreationData,
  onValidate: (edgeData: EdgeCreationData) => EdgeValidationResult,
  isEditMode: boolean,
  existingEdge: (EdgeCreationData & { edgeId: string }) | undefined,
  onUpdate: ((edgeId: string, edgeData: EdgeCreationData) => void) | undefined,
  onCreate: (edgeData: EdgeCreationData) => void,
  onClose: () => void
): void {
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
}

function runValidationAndPreviewSync(
  currentEdgeData: EdgeCreationData | null,
  targetRoomId: string,
  direction: string,
  customDirection: string,
  useCustomDirection: boolean,
  onValidate: (edgeData: EdgeCreationData) => EdgeValidationResult,
  onPreviewChange: ((edgeData: EdgeCreationData | null) => void) | undefined
): void {
  const hasDirectionInput = Boolean(direction) || (useCustomDirection && Boolean(customDirection));
  if (currentEdgeData && targetRoomId && hasDirectionInput) {
    onValidate(currentEdgeData);
    onPreviewChange?.(currentEdgeData);
  } else {
    onPreviewChange?.(null);
  }
}

function subscribeEscapeToClose(isOpen: boolean, onClose: () => void): () => void {
  if (!isOpen) {
    return () => {};
  }
  const handleEscape = (event: KeyboardEvent) => {
    if (event.key === 'Escape') {
      onClose();
    }
  };
  window.addEventListener('keydown', handleEscape);
  return () => {
    window.removeEventListener('keydown', handleEscape);
  };
}

function applyModalBodyScrollLock(isOpen: boolean): () => void {
  if (isOpen) {
    document.body.style.overflow = 'hidden';
  } else {
    document.body.style.overflow = '';
  }
  return () => {
    document.body.style.overflow = '';
  };
}

interface EdgeFormResetters {
  setTargetRoomId: (v: string) => void;
  setDirection: (v: string) => void;
  setCustomDirection: (v: string) => void;
  setSearchQuery: (v: string) => void;
  setFlags: Dispatch<SetStateAction<string[]>>;
  setDescription: (v: string) => void;
  setUseCustomDirection: (v: boolean) => void;
}

function resetEdgeFormFields(
  setters: EdgeFormResetters,
  onPreviewChange: ((edgeData: EdgeCreationData | null) => void) | undefined
): void {
  setters.setTargetRoomId('');
  setters.setDirection('');
  setters.setCustomDirection('');
  setters.setSearchQuery('');
  setters.setFlags([]);
  setters.setDescription('');
  setters.setUseCustomDirection(false);
  onPreviewChange?.(null);
}

interface EdgeModalValidationMessagesProps {
  validation: EdgeValidationResult;
}

function EdgeModalValidationMessages({ validation }: EdgeModalValidationMessagesProps) {
  return (
    <div className="space-y-2">
      {validation.errors.length > 0 ? (
        <EdgeModalMessageList title="Errors:" items={validation.errors} tone="error" />
      ) : null}
      {validation.warnings.length > 0 ? (
        <EdgeModalMessageList title="Warnings:" items={validation.warnings} tone="warning" />
      ) : null}
    </div>
  );
}

const EDGE_MODAL_MESSAGE_TONE_CLASSES: Record<'error' | 'warning', { box: string; heading: string; list: string }> = {
  error: {
    box: 'p-3 bg-mythos-terminal-error/20 border border-mythos-terminal-error rounded',
    heading: 'text-sm font-medium text-mythos-terminal-error mb-1',
    list: 'list-disc list-inside text-sm text-mythos-terminal-error space-y-1',
  },
  warning: {
    box: 'p-3 bg-yellow-900/20 border border-yellow-600 rounded',
    heading: 'text-sm font-medium text-yellow-400 mb-1',
    list: 'list-disc list-inside text-sm text-yellow-300 space-y-1',
  },
};

function EdgeModalMessageList({ title, items, tone }: { title: string; items: string[]; tone: 'error' | 'warning' }) {
  const styles = EDGE_MODAL_MESSAGE_TONE_CLASSES[tone];
  return (
    <div className={styles.box}>
      <div className={styles.heading}>{title}</div>
      <ul className={styles.list}>
        {items.map((msg, index) => (
          <li key={index}>{msg}</li>
        ))}
      </ul>
    </div>
  );
}

interface EdgeModalDirectionFieldsProps {
  useCustomDirection: boolean;
  setUseCustomDirection: (value: boolean) => void;
  direction: string;
  setDirection: (value: string) => void;
  customDirection: string;
  setCustomDirection: (value: string) => void;
  effectiveDirections: string[];
}

function EdgeModalCustomDirectionInput({
  customDirection,
  setCustomDirection,
}: {
  customDirection: string;
  setCustomDirection: (value: string) => void;
}) {
  return (
    <input
      id="custom-direction-input"
      type="text"
      value={customDirection}
      onChange={e => {
        setCustomDirection(e.target.value);
      }}
      placeholder="Enter direction (e.g., 'portal', 'secret')"
      required
      className="w-full px-3 py-2 bg-mythos-terminal-background border border-mythos-terminal-border rounded text-mythos-terminal-text"
    />
  );
}

function EdgeModalStandardDirectionSelect({
  direction,
  setDirection,
  effectiveDirections,
}: {
  direction: string;
  setDirection: (value: string) => void;
  effectiveDirections: string[];
}) {
  return (
    <select
      id="edge-direction-select"
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
  );
}

function EdgeModalDirectionFields({
  useCustomDirection,
  setUseCustomDirection,
  direction,
  setDirection,
  customDirection,
  setCustomDirection,
  effectiveDirections,
}: EdgeModalDirectionFieldsProps) {
  return (
    <div>
      <label
        htmlFor={useCustomDirection ? 'custom-direction-input' : 'edge-direction-select'}
        className="block text-sm font-medium text-mythos-terminal-text mb-2"
      >
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
        <EdgeModalCustomDirectionInput customDirection={customDirection} setCustomDirection={setCustomDirection} />
      ) : (
        <EdgeModalStandardDirectionSelect
          direction={direction}
          setDirection={setDirection}
          effectiveDirections={effectiveDirections}
        />
      )}
    </div>
  );
}

function useEdgeCreationModal(props: EdgeCreationModalProps) {
  const {
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
  } = props;

  const isEditMode = !!existingEdge;

  const [targetRoomId, setTargetRoomId] = useState(() => getInitialEdgeFormState(existingEdge).targetRoomId);
  const [direction, setDirection] = useState(() => getInitialEdgeFormState(existingEdge).direction);
  const [customDirection, setCustomDirection] = useState(() => getInitialEdgeFormState(existingEdge).customDirection);
  const [searchQuery, setSearchQuery] = useState('');
  const [flags, setFlags] = useState(() => getInitialEdgeFormState(existingEdge).flags);
  const [description, setDescription] = useState(() => getInitialEdgeFormState(existingEdge).description);
  const [useCustomDirection, setUseCustomDirection] = useState(
    () => getInitialEdgeFormState(existingEdge).useCustomDirection
  );

  const sourceRoom = useMemo(() => findRoomNodeById(availableNodes, sourceRoomId), [availableNodes, sourceRoomId]);

  const filteredNodes = useMemo(
    () => filterNodesForTargetSelection(availableNodes, sourceRoomId, searchQuery),
    [availableNodes, sourceRoomId, searchQuery]
  );

  const currentEdgeData = useMemo<EdgeCreationData | null>(
    () =>
      deriveEdgeCreationData(
        sourceRoomId,
        targetRoomId,
        direction,
        customDirection,
        useCustomDirection,
        flags,
        description
      ),
    [sourceRoomId, targetRoomId, direction, customDirection, useCustomDirection, flags, description]
  );

  useEffect(() => {
    runValidationAndPreviewSync(
      currentEdgeData,
      targetRoomId,
      direction,
      customDirection,
      useCustomDirection,
      onValidate,
      onPreviewChange
    );
  }, [currentEdgeData, targetRoomId, direction, customDirection, useCustomDirection, onValidate, onPreviewChange]);

  useEffect(() => {
    return subscribeEscapeToClose(isOpen, onClose);
  }, [isOpen, onClose]);

  useEffect(() => {
    return applyModalBodyScrollLock(isOpen);
  }, [isOpen]);

  useEffect(() => {
    if (isOpen) {
      return;
    }
    resetEdgeFormFields(
      {
        setTargetRoomId,
        setDirection,
        setCustomDirection,
        setSearchQuery,
        setFlags,
        setDescription,
        setUseCustomDirection,
      },
      onPreviewChange
    );
  }, [isOpen, onPreviewChange]);

  const handleSubmit = useCallback(
    (e: React.FormEvent) => {
      e.preventDefault();
      if (!currentEdgeData) {
        return;
      }
      submitValidatedEdge(currentEdgeData, onValidate, isEditMode, existingEdge, onUpdate, onCreate, onClose);
    },
    [currentEdgeData, onCreate, onValidate, onClose, isEditMode, existingEdge, onUpdate]
  );

  const toggleFlag = useCallback((flag: string) => {
    setFlags(prev => toggleStringFlag(prev, flag));
  }, []);

  const effectiveDirections = useMemo(
    () => (availableDirections.length > 0 ? availableDirections : STANDARD_DIRECTIONS),
    [availableDirections]
  );

  const canSubmit = edgeFormCanSubmit(currentEdgeData, validation);

  return {
    isEditMode,
    sourceRoom,
    searchQuery,
    setSearchQuery,
    targetRoomId,
    setTargetRoomId,
    filteredNodes,
    direction,
    setDirection,
    customDirection,
    setCustomDirection,
    useCustomDirection,
    setUseCustomDirection,
    flags,
    description,
    setDescription,
    toggleFlag,
    handleSubmit,
    effectiveDirections,
    canSubmit,
  };
}

interface EdgeCreationModalViewProps {
  onClose: () => void;
  sourceRoomId: string;
  validation: EdgeValidationResult | null;
  vm: ReturnType<typeof useEdgeCreationModal>;
}

function EdgeCreationModalView({ onClose, sourceRoomId, validation, vm }: EdgeCreationModalViewProps) {
  const {
    isEditMode,
    sourceRoom,
    searchQuery,
    setSearchQuery,
    targetRoomId,
    setTargetRoomId,
    filteredNodes,
    direction,
    setDirection,
    customDirection,
    setCustomDirection,
    useCustomDirection,
    setUseCustomDirection,
    flags,
    description,
    setDescription,
    toggleFlag,
    handleSubmit,
    effectiveDirections,
    canSubmit,
  } = vm;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center">
      <button
        type="button"
        className="absolute inset-0 cursor-default bg-black bg-opacity-75 border-0 p-0"
        onClick={onClose}
        aria-label="Dismiss dialog (backdrop)"
      />
      <div
        className="relative z-10 bg-mythos-terminal-background border-2 border-mythos-terminal-border rounded-lg p-6 w-full max-w-2xl max-h-modal overflow-y-auto shadow-xl"
        role="dialog"
        aria-modal="true"
        aria-labelledby="edge-creation-title"
      >
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

        <div className="mb-4">
          <p className="block text-sm font-medium text-mythos-terminal-text mb-2">From Room:</p>
          <div className="px-3 py-2 bg-mythos-terminal-surface border border-mythos-terminal-border rounded text-mythos-terminal-text">
            {sourceRoom?.data.name || sourceRoomId}
          </div>
        </div>

        <form onSubmit={handleSubmit} className="space-y-4">
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
              disabled={isEditMode}
              className="w-full px-3 py-2 bg-mythos-terminal-background border border-mythos-terminal-border rounded text-mythos-terminal-text disabled:opacity-50 disabled:cursor-not-allowed"
            >
              <option value="">Select target room...</option>
              {filteredNodes.map(node => (
                <option key={node.id} value={node.id}>
                  {node.data.name} ({node.id})
                </option>
              ))}
            </select>
            {isEditMode ? (
              <p className="text-xs text-mythos-terminal-text/50 mt-1">
                Target room cannot be changed. Delete and recreate the exit to change the target.
              </p>
            ) : null}
          </div>

          <EdgeModalDirectionFields
            useCustomDirection={useCustomDirection}
            setUseCustomDirection={setUseCustomDirection}
            direction={direction}
            setDirection={setDirection}
            customDirection={customDirection}
            setCustomDirection={setCustomDirection}
            effectiveDirections={effectiveDirections}
          />

          <div>
            <p className="block text-sm font-medium text-mythos-terminal-text mb-2">Exit Flags:</p>
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

          {validation ? <EdgeModalValidationMessages validation={validation} /> : null}

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
}

/**
 * Edge Creation Modal component.
 */
export const EdgeCreationModal: React.FC<EdgeCreationModalProps> = props => {
  const { isOpen, onClose, sourceRoomId, validation } = props;
  const vm = useEdgeCreationModal(props);
  if (!isOpen) {
    return null;
  }
  return <EdgeCreationModalView onClose={onClose} sourceRoomId={sourceRoomId} validation={validation} vm={vm} />;
};
