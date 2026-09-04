import type { Dispatch, SetStateAction } from 'react';
import type { Node } from 'reactflow';
import type { EdgeCreationData, EdgeValidationResult } from './hooks/useMapEditing';
import type { RoomNodeData } from './types';

// Must match server/models/command_base.py::Direction exactly -- see MAP_EDITOR_DIRECTIONS.
export const STANDARD_DIRECTIONS = [
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
];

const STANDARD_DIRECTION_SET = new Set(STANDARD_DIRECTIONS);

export function isStandardExitDirection(direction: string): boolean {
  return STANDARD_DIRECTION_SET.has(direction);
}

function roomNodeMatchesSearchQuery(node: Node<RoomNodeData>, sourceRoomId: string, queryLower: string): boolean {
  if (node.id === sourceRoomId) return false;
  const fields = [
    node.data.name?.toLowerCase(),
    node.id.toLowerCase(),
    node.data.zone?.toLowerCase(),
    node.data.subZone?.toLowerCase(),
  ];
  return fields.some(field => field?.includes(queryLower));
}

export function filterNodesForTargetSelection(
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

export function findRoomNodeById(
  availableNodes: Node<RoomNodeData>[],
  sourceRoomId: string
): Node<RoomNodeData> | undefined {
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

export function getInitialEdgeFormState(
  existingEdge: (EdgeCreationData & { edgeId: string }) | undefined
): EdgeFormFields {
  if (!existingEdge) return emptyEdgeFormState();
  return edgeFormStateFromExisting(existingEdge);
}

export function toggleStringFlag(prev: string[], flag: string): string[] {
  return prev.includes(flag) ? prev.filter(f => f !== flag) : [...prev, flag];
}

export function edgeFormCanSubmit(
  currentEdgeData: EdgeCreationData | null,
  validation: EdgeValidationResult | null | undefined
): boolean {
  return currentEdgeData !== null && validation?.isValid === true;
}

export function deriveEdgeCreationData(
  sourceRoomId: string,
  targetRoomId: string,
  direction: string,
  customDirection: string,
  useCustomDirection: boolean,
  flags: string[],
  description: string
): EdgeCreationData | null {
  if (!targetRoomId) return null;
  const resolvedDirection = useCustomDirection ? customDirection : direction;
  if (!resolvedDirection) return null;
  return {
    sourceRoomId,
    targetRoomId,
    direction: resolvedDirection,
    flags: flags.length > 0 ? flags : undefined,
    description: description.trim() || undefined,
  };
}

export function submitValidatedEdge(
  currentEdgeData: EdgeCreationData,
  onValidate: (edgeData: EdgeCreationData) => EdgeValidationResult,
  isEditMode: boolean,
  existingEdge: (EdgeCreationData & { edgeId: string }) | undefined,
  onUpdate: ((edgeId: string, edgeData: EdgeCreationData) => void) | undefined,
  onCreate: (edgeData: EdgeCreationData) => void,
  onClose: () => void
): void {
  const result = onValidate(currentEdgeData);
  if (!result.isValid) return;
  if (isEditMode && existingEdge && onUpdate) {
    onUpdate(existingEdge.edgeId, currentEdgeData);
  } else {
    onCreate(currentEdgeData);
  }
  onClose();
}

export function runValidationAndPreviewSync(
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

export function subscribeEscapeToClose(isOpen: boolean, onClose: () => void): () => void {
  if (!isOpen) return () => {};
  const handleEscape = (event: KeyboardEvent) => {
    if (event.key === 'Escape') onClose();
  };
  window.addEventListener('keydown', handleEscape);
  return () => window.removeEventListener('keydown', handleEscape);
}

export function applyModalBodyScrollLock(isOpen: boolean): () => void {
  document.body.style.overflow = isOpen ? 'hidden' : '';
  return () => {
    document.body.style.overflow = '';
  };
}

export interface EdgeFormResetters {
  setTargetRoomId: (v: string) => void;
  setDirection: (v: string) => void;
  setCustomDirection: (v: string) => void;
  setSearchQuery: (v: string) => void;
  setFlags: Dispatch<SetStateAction<string[]>>;
  setDescription: (v: string) => void;
  setUseCustomDirection: (v: boolean) => void;
}

export function resetEdgeFormFields(
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
