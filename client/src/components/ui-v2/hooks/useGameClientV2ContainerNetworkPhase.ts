// WebSocket / connection wiring for GameClientV2Container.

import type { SendMessageFn } from '../../../utils/clientErrorReporter';
import type { GameClientV2ContainerProps, GameClientV2MergedSlice } from './gameClientV2ContainerTypes';
import { useEventProcessing } from './useEventProcessing';
import { useGameClientV2ContainerConnectionEffects } from './useGameClientV2ContainerConnectionEffects';
import type { GameClientV2RefsBundle } from './useGameClientV2ContainerRefsAndBootstrap';
import { useGameConnectionManagement } from './useGameConnectionManagement';

export interface GameClientV2NetworkPhase {
  handleGameEvent: ReturnType<typeof useEventProcessing>['handleGameEvent'];
  clearPendingFollowRequest: ReturnType<typeof useEventProcessing>['clearPendingFollowRequest'];
  isConnected: boolean;
  isConnecting: boolean;
  error: string | null;
  reconnectAttempts: number;
  sendCommand: (command: string, args?: string[]) => Promise<boolean>;
  sendMessage: SendMessageFn;
  disconnect: () => void;
}

export function useGameClientV2ContainerNetworkPhase(
  props: GameClientV2ContainerProps,
  slice: GameClientV2MergedSlice,
  refs: GameClientV2RefsBundle
): GameClientV2NetworkPhase {
  const { handleGameEvent, clearPendingFollowRequest } = useEventProcessing({ setGameState: slice.setGameState });

  const { isConnected, isConnecting, error, reconnectAttempts, sendCommand, sendMessage, disconnect } =
    useGameConnectionManagement({
      authToken: props.authToken,
      playerName: props.playerName,
      characterId: props.characterId,
      onLogout: props.onLogout,
      onGameEvent: handleGameEvent,
      setGameState: slice.setGameState,
      intentionalExitInProgressRef: refs.intentionalExitInProgressRef,
    });

  useGameClientV2ContainerConnectionEffects(slice, refs, isConnected, sendMessage, sendCommand);

  return {
    handleGameEvent,
    clearPendingFollowRequest,
    isConnected,
    isConnecting,
    error,
    reconnectAttempts,
    sendCommand,
    sendMessage,
    disconnect,
  };
}
