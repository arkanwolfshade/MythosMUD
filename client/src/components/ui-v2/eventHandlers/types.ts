// Event handler types and interfaces
// As documented in "Event Processing Architecture" - Dr. Armitage, 1928

import type { HealthStatus } from '../../../types/health';
import type { LucidityStatus, RescueState } from '../../../types/lucidity';
import type { MythosTimeState } from '../../../types/mythosTime';
import type { ChatMessage, Player, QuestLogEntry, Room } from '../types';

/**
 * WebSocket `GameEvent` catalog and projector effects (canonical client pipeline).
 * `event_type` is normalized to lowercase before dispatch. State changes belong in
 * `projectEvent` / projector handlers; see `PROJECTED_EVENT_TYPES` in projectorConstants.ts.
 *
 * | event_type (lowercase) | Player HP/lucidity | Room | Messages | Other |
 * | --- | --- | --- | --- | --- |
 * | game_state | full player, grace, follow, quest | full room | no | mythos from tick elsewhere |
 * | quest_log_updated | no | no | no | questLog |
 * | follow_state | no | no | no | followingTarget |
 * | effects_update | grace period flags | no | no | activeEffects path via grace |
 * | room_state, room_update, room_occupants | no | merge/replace | no | seq dedupe occupants |
 * | player_update | partial stats, in_combat | no | no | |
 * | combat_started / combat_ended | in_combat | no | optional reason | |
 * | player_died | current_dp if mortally wounded | no | no | |
 * | player_respawned, player_delirium_respawned | player, room | room | optional | |
 * | player_dp_updated | current_dp, max_dp, posture | no | no | |
 * | lucidity_change | stats.current_dp from data.current_dp | no | no | legacy payload shape |
 * | command_response | player_update, room_state | nested room | result / game_log | |
 * | chat_message, room_message, system | no | no | yes | |
 * | npc_attacked | no (NPC target) | no | combat line | |
 * | player_attacked | target DP merged into player | no | combat line | |
 * | combat_started, combat_ended, combat_target_switch | flags / no | no | lines | |
 * | npc_died, combat_death | no | no | line | |
 * | game_tick | no | no | tick/chime | mythosTime |
 * | follow_request / follow_request_cleared | no | no | no | pendingFollowRequest |
 * | party_invite / party_invite_cleared | no | no | no | pendingPartyInvite |
 * | intentional_disconnect | no | no | line | |
 */
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
  /** Who the player is following (for title panel). */
  followingTarget?: { target_name: string; target_type: 'player' | 'npc' } | null;
  /** Quest log (from game_state.quest_log). */
  questLog?: QuestLogEntry[];
}

export interface EventHandlerContext {
  currentPlayerRef: React.RefObject<Player | null>;
  currentRoomRef: React.RefObject<Room | null>;
  currentMessagesRef: React.RefObject<ChatMessage[]>;
  healthStatusRef: React.RefObject<HealthStatus | null>;
  lucidityStatusRef: React.RefObject<LucidityStatus | null>;
  lastDaypartRef: React.RefObject<string | null>;
  lastHourRef: React.RefObject<number | null>;
  lastQuarterHourRef: React.RefObject<number | null>;
  lastHolidayIdsRef: React.RefObject<string[]>;
  lastRoomUpdateTime: React.RefObject<number>;
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
