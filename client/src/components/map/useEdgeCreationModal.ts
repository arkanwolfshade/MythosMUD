import { useCallback, useEffect, useMemo, useState } from 'react';
import type { EdgeCreationModalProps } from './EdgeCreationModal';
import {
  STANDARD_DIRECTIONS,
  applyModalBodyScrollLock,
  deriveEdgeCreationData,
  edgeFormCanSubmit,
  filterNodesForTargetSelection,
  findRoomNodeById,
  getInitialEdgeFormState,
  resetEdgeFormFields,
  runValidationAndPreviewSync,
  submitValidatedEdge,
  subscribeEscapeToClose,
  toggleStringFlag,
} from './edgeModalLogic';
import type { EdgeCreationData } from './hooks/useMapEditing';

export function useEdgeCreationModal(props: EdgeCreationModalProps) {
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
  const initialForm = getInitialEdgeFormState(existingEdge);

  const [targetRoomId, setTargetRoomId] = useState(initialForm.targetRoomId);
  const [direction, setDirection] = useState(initialForm.direction);
  const [customDirection, setCustomDirection] = useState(initialForm.customDirection);
  const [searchQuery, setSearchQuery] = useState('');
  const [flags, setFlags] = useState(initialForm.flags);
  const [description, setDescription] = useState(initialForm.description);
  const [useCustomDirection, setUseCustomDirection] = useState(initialForm.useCustomDirection);

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
    if (isOpen) return;
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
      if (!currentEdgeData) return;
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
    canSubmit: edgeFormCanSubmit(currentEdgeData, validation),
  };
}
