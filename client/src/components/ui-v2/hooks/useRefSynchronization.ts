// Ref synchronization hook
// Extracted from GameClientV2Container to reduce complexity

import { useEffect } from 'react';
import type { HealthStatus } from '../../../types/health';
import type { LucidityStatus, RescueState } from '../../../types/lucidity';
import type { ChatMessage, Player, Room } from '../types';
import type { GameState } from '../utils/stateUpdateUtils';

interface UseRefSynchronizationParams {
  gameState: GameState;
  healthStatus: HealthStatus | null;
  lucidityStatus: LucidityStatus | null;
  rescueState: RescueState | null;
  setRescueState: (state: RescueState | null) => void;
  currentMessagesRef: React.MutableRefObject<ChatMessage[]>;
  currentRoomRef: React.MutableRefObject<Room | null>;
  currentPlayerRef: React.MutableRefObject<Player | null>;
  healthStatusRef: React.MutableRefObject<HealthStatus | null>;
  lucidityStatusRef: React.MutableRefObject<LucidityStatus | null>;
  rescueStateRef: React.MutableRefObject<RescueState | null>;
  rescueTimeoutRef: React.MutableRefObject<number | null>;
}

export const useRefSynchronization = ({
  gameState,
  healthStatus,
  lucidityStatus,
  rescueState,
  setRescueState,
  currentMessagesRef,
  currentRoomRef,
  currentPlayerRef,
  healthStatusRef,
  lucidityStatusRef,
  rescueStateRef,
  rescueTimeoutRef,
}: UseRefSynchronizationParams) => {
  // Keep refs in sync with state
  useEffect(() => {
    currentMessagesRef.current = gameState.messages;
  }, [gameState.messages, currentMessagesRef]);

  useEffect(() => {
    currentRoomRef.current = gameState.room;
  }, [gameState.room, currentRoomRef]);

  useEffect(() => {
    currentPlayerRef.current = gameState.player;
  }, [gameState.player, currentPlayerRef]);

  useEffect(() => {
    healthStatusRef.current = healthStatus;
  }, [healthStatus, healthStatusRef]);

  useEffect(() => {
    lucidityStatusRef.current = lucidityStatus;
  }, [lucidityStatus, lucidityStatusRef]);

  useEffect(() => {
    rescueStateRef.current = rescueState;

    if (rescueState && ['success', 'failed', 'sanitarium'].includes(rescueState.status)) {
      rescueTimeoutRef.current = window.setTimeout(() => setRescueState(null), 8_000);
    }

    return () => {
      if (rescueTimeoutRef.current) {
        window.clearTimeout(rescueTimeoutRef.current);
        rescueTimeoutRef.current = null;
      }
    };
  }, [rescueState, rescueStateRef, rescueTimeoutRef, setRescueState]);
};
