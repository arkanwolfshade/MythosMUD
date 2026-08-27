// Ref synchronization hook
// Extracted from GameClientV2Container to reduce complexity

import { useEffect } from 'react';
import type { HealthStatus } from '../../../types/health';
import type { LucidityStatus } from '../../../types/lucidity';
import type { ChatMessage, Player, Room } from '../types';
import type { GameState } from '../utils/stateUpdateUtils';

interface UseRefSynchronizationParams {
  gameState: GameState;
  healthStatus: HealthStatus | null;
  lucidityStatus: LucidityStatus | null;
  currentMessagesRef: React.MutableRefObject<ChatMessage[]>;
  currentRoomRef: React.MutableRefObject<Room | null>;
  currentPlayerRef: React.MutableRefObject<Player | null>;
  healthStatusRef: React.MutableRefObject<HealthStatus | null>;
  lucidityStatusRef: React.MutableRefObject<LucidityStatus | null>;
}

export const useRefSynchronization = (params: UseRefSynchronizationParams) => {
  const {
    gameState,
    healthStatus,
    lucidityStatus,
    currentMessagesRef,
    currentRoomRef,
    currentPlayerRef,
    healthStatusRef,
    lucidityStatusRef,
  } = params;

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
};
