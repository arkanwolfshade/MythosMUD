// Event handler types and interfaces
// As documented in "Event Processing Architecture" - Dr. Armitage, 1928

import type { HealthStatus } from '../../../types/health';
import type { LucidityStatus, RescueState } from '../../../types/lucidity';
import type { MythosTimeState } from '../../../types/mythosTime';
import type { ChatMessage, Player, Room } from '../types';

export interface GameEvent {
  event_type: string;
  timestamp: string;
  sequence_number: number;
  player_id?: string;
  room_id?: string;
  data: Record<string, unknown>;
  alias_chain?: Array<{
    original: string;
    expanded: string;
    alias_name: string;
  }>;
}

export interface GameStateUpdates {
  player?: Player | null;
  room?: Room | null;
  messages?: ChatMessage[];
  loginGracePeriodActive?: boolean;
  loginGracePeriodRemaining?: number;
}

export interface EventHandlerContext {
  currentPlayerRef: React.MutableRefObject<Player | null>;
  currentRoomRef: React.MutableRefObject<Room | null>;
  currentMessagesRef: React.MutableRefObject<ChatMessage[]>;
  healthStatusRef: React.MutableRefObject<HealthStatus | null>;
  lucidityStatusRef: React.MutableRefObject<LucidityStatus | null>;
  lastDaypartRef: React.MutableRefObject<string | null>;
  lastHourRef: React.MutableRefObject<number | null>;
  lastHolidayIdsRef: React.MutableRefObject<string[]>;
  lastRoomUpdateTime: React.MutableRefObject<number>;
  setDpStatus: (status: HealthStatus) => void;
  setLucidityStatus: (status: LucidityStatus) => void;
  setMythosTime: (time: MythosTimeState) => void;
  setIsDead: (dead: boolean) => void;
  setIsMortallyWounded: (wounded: boolean) => void;
  setIsRespawning: (respawning: boolean) => void;
  setIsDelirious: (delirious: boolean) => void;
  setIsDeliriumRespawning: (respawning: boolean) => void;
  setDeathLocation: (location: string) => void;
  setDeliriumLocation: (location: string) => void;
  setRescueState: (state: RescueState | null) => void;
  onLogout?: () => void;
}

export type EventHandler = (
  event: GameEvent,
  context: EventHandlerContext,
  appendMessage: (message: ChatMessage) => void
) => GameStateUpdates | void;
