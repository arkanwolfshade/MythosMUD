// Refs and Mythos bootstrap for GameClientV2Container.

import { useRef } from 'react';

import type { GameClientV2MergedSlice } from './gameClientV2ContainerTypes';
import { useMythosTimeBootstrap } from './useMythosTimeBootstrap';

export interface GameClientV2RefsBundle {
  sendCommandRef: React.MutableRefObject<((command: string, args?: string[]) => Promise<boolean>) | null>;
  intentionalExitInProgressRef: React.MutableRefObject<boolean>;
  roomFirstSetAtRef: React.MutableRefObject<number | null>;
  reportedRoomIdsRef: React.MutableRefObject<Set<string>>;
}

function useGameClientV2ContainerMutableRefs(): GameClientV2RefsBundle {
  const sendCommandRef = useRef<((command: string, args?: string[]) => Promise<boolean>) | null>(null);
  const intentionalExitInProgressRef = useRef(false);
  const roomFirstSetAtRef = useRef<number | null>(null);
  const reportedRoomIdsRef = useRef<Set<string>>(new Set());
  return {
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

  useMythosTimeBootstrap({
    authToken,
    setMythosTime: slice.setMythosTime,
  });

  return refs;
}
