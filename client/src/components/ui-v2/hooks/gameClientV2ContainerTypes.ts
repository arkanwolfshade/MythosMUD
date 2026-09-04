// Shared types for GameClientV2Container hook modules (avoid circular imports).

import {
  useGameClientV2GameModelState,
  useGameClientV2SurvivalAndTimeState,
  useGameClientV2UiAndTabsState,
} from './useGameClientV2ContainerState';

export interface GameClientV2ContainerProps {
  playerName: string;
  authToken: string;
  characterId?: string;
  onLogout?: () => void;
  isLoggingOut?: boolean;
  onDisconnect?: (disconnectFn: () => void) => void;
}

export type GameClientV2MergedSlice = ReturnType<typeof useGameClientV2UiAndTabsState> &
  ReturnType<typeof useGameClientV2GameModelState> &
  ReturnType<typeof useGameClientV2SurvivalAndTimeState>;
