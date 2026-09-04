// Refs, ref sync, Mythos bootstrap, hallucination cleanup for GameClientV2Container.

import { useRef } from 'react';

import type { HealthStatus } from '../../../types/health';
import type { LucidityStatus } from '../../../types/lucidity';
import type { ChatMessage, Player, Room } from '../types';
import type { GameClientV2MergedSlice } from './gameClientV2ContainerTypes';
import { useMythosTimeBootstrap } from './useMythosTimeBootstrap';
import { useRefSynchronization } from './useRefSynchronization';

export interface GameClientV2RefsBundle {
  currentMessagesRef: React.MutableRefObject<ChatMessage[]>;
  currentRoomRef: React.MutableRefObject<Room | null>;
  currentPlayerRef: React.MutableRefObject<Player | null>;
  lucidityStatusRef: React.MutableRefObject<LucidityStatus | null>;
  healthStatusRef: React.MutableRefObject<HealthStatus | null>;
  lastDaypartRef: React.MutableRefObject<string | null>;
  lastHolidayIdsRef: React.MutableRefObject<string[]>;
  sendCommandRef: React.MutableRefObject<((command: string, args?: string[]) => Promise<boolean>) | null>;
  intentionalExitInProgressRef: React.MutableRefObject<boolean>;
  roomFirstSetAtRef: React.MutableRefObject<number | null>;
  reportedRoomIdsRef: React.MutableRefObject<Set<string>>;
}

function useGameClientV2ContainerMutableRefs(): GameClientV2RefsBundle {
  const currentMessagesRef = useRef<ChatMessage[]>([]);
  const currentRoomRef = useRef<Room | null>(null);
  const currentPlayerRef = useRef<Player | null>(null);
  const lucidityStatusRef = useRef<LucidityStatus | null>(null);
  const healthStatusRef = useRef<HealthStatus | null>(null);
  const lastDaypartRef = useRef<string | null>(null);
  const lastHolidayIdsRef = useRef<string[]>([]);
  const sendCommandRef = useRef<((command: string, args?: string[]) => Promise<boolean>) | null>(null);
  const intentionalExitInProgressRef = useRef(false);
  const roomFirstSetAtRef = useRef<number | null>(null);
  const reportedRoomIdsRef = useRef<Set<string>>(new Set());
  return {
    currentMessagesRef,
    currentRoomRef,
    currentPlayerRef,
    lucidityStatusRef,
    healthStatusRef,
    lastDaypartRef,
    lastHolidayIdsRef,
    sendCommandRef,
    intentionalExitInProgressRef,
    roomFirstSetAtRef,
    reportedRoomIdsRef,
  };
}

export function useGameClientV2ContainerRefsAndBootstrap(
  authToken: string,
  slice: GameClientV2MergedSlice
): GameClientV2RefsBundle {
  const refs = useGameClientV2ContainerMutableRefs();

  useRefSynchronization({
    gameState: slice.gameState,
    healthStatus: slice.healthStatus,
    lucidityStatus: slice.lucidityStatus,
    currentMessagesRef: refs.currentMessagesRef,
    currentRoomRef: refs.currentRoomRef,
    currentPlayerRef: refs.currentPlayerRef,
    healthStatusRef: refs.healthStatusRef,
    lucidityStatusRef: refs.lucidityStatusRef,
  });

  useMythosTimeBootstrap({
    authToken,
    setMythosTime: slice.setMythosTime,
    lastDaypartRef: refs.lastDaypartRef,
    lastHolidayIdsRef: refs.lastHolidayIdsRef,
  });

  return refs;
}
