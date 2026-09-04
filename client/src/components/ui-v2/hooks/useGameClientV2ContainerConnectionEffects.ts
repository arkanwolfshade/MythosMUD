// Effects that depend on connection + room (split from network phase for Lizard NLOC).

import { useEffect } from 'react';

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

  useEffect(() => {
    sendCommandRef.current = sendCommand;
  }, [sendCommand, sendCommandRef]);

  useEffect(() => {
    if (slice.gameState.room?.id && roomFirstSetAtRef.current === null) {
      roomFirstSetAtRef.current = Date.now();
    }
    if (!slice.gameState.room?.id) {
      roomFirstSetAtRef.current = null;
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
