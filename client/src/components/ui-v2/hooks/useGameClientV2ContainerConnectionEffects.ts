// Effects that depend on connection + room (split from network phase for Lizard NLOC).

import { useEffect, useRef } from 'react';

import type { SendMessageFn } from '../../../utils/clientErrorReporter';
import { runEmptyOccupantsReportIfNeeded } from './emptyOccupantsDiagnostics';
import type { GameClientV2MergedSlice } from './gameClientV2ContainerTypes';
import type { GameClientV2RefsBundle } from './useGameClientV2ContainerRefsAndBootstrap';

export function useGameClientV2ContainerConnectionEffects(
  slice: GameClientV2MergedSlice,
  refs: GameClientV2RefsBundle,
  isConnected: boolean,
  sendMessage: SendMessageFn,
  sendCommand: (command: string, args?: string[]) => Promise<boolean>
): void {
  const { sendCommandRef, roomFirstSetAtRef, reportedRoomIdsRef } = refs;
  const prevRoomIdRef = useRef<string | null>(null);

  useEffect(() => {
    sendCommandRef.current = sendCommand;
  }, [sendCommand, sendCommandRef]);

  useEffect(() => {
    const roomId = slice.gameState.room?.id ?? null;
    // Reset on every room change, not just null->set, so each room gets its own occupant-settle
    // grace period -- otherwise only the first room of the session had one (#776).
    if (roomId !== prevRoomIdRef.current) {
      roomFirstSetAtRef.current = roomId ? Date.now() : null;
      prevRoomIdRef.current = roomId;
    }
  }, [slice.gameState.room?.id, roomFirstSetAtRef]);

  useEffect(() => {
    runEmptyOccupantsReportIfNeeded(
      isConnected,
      slice.gameState.player ?? null,
      slice.gameState.room ?? null,
      roomFirstSetAtRef.current,
      reportedRoomIdsRef.current,
      sendMessage
    );
  }, [isConnected, slice.gameState.player, slice.gameState.room, sendMessage, roomFirstSetAtRef, reportedRoomIdsRef]);
}
