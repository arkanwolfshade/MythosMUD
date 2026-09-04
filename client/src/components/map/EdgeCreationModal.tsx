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

import React from 'react';
import type { Node } from 'reactflow';
import { EdgeCreationModalView } from './EdgeCreationModalParts';
import type { EdgeCreationData, EdgeValidationResult } from './hooks/useMapEditing';
import type { RoomNodeData } from './types';
import { useEdgeCreationModal } from './useEdgeCreationModal';

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

export const EdgeCreationModal: React.FC<EdgeCreationModalProps> = props => {
  const { isOpen, onClose, sourceRoomId, validation } = props;
  const vm = useEdgeCreationModal(props);
  if (!isOpen) {
    return null;
  }
  return <EdgeCreationModalView onClose={onClose} sourceRoomId={sourceRoomId} validation={validation} vm={vm} />;
};
