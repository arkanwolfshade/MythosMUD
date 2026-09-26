// GameState shape shared by the projector and the container.
// As documented in "State Management Patterns" - Dr. Armitage, 1928

import type { LucidityStatus } from '../../../types/lucidity';
import type { MythosTimeState } from '../../../types/mythosTime';
import type {
  ChatMessage,
  ContainerSnapshot,
  InventoryStack,
  Player,
  QuestLogEntry,
  Room,
  RoomContainerSummary,
} from '../types';

/** A container this player currently has open (personal container.opened only). */
export interface OpenContainerState {
  container: ContainerSnapshot;
  mutationToken: string;
  /** Last applied event sequence_number, for stale-update rejection on container.updated. */
  sequenceNumber?: number;
}

/** Single active effect for header display (server-authoritative). */
export interface ActiveEffectDisplay {
  effect_type: string;
  label?: string;
  remaining_seconds?: number;
}

export interface GameState {
  player: Player | null;
  room: Room | null;
  messages: ChatMessage[];
  commandHistory: string[];
  loginGracePeriodActive?: boolean;
  loginGracePeriodRemaining?: number;
  /** Active effects for header bar (e.g. LOGIN_WARDED). When absent, derived from grace period for backward compat. */
  activeEffects?: ActiveEffectDisplay[];
  /** Derived from game_tick; used for Mythos time display. Bootstrap may set initial until first tick. */
  mythosTime?: MythosTimeState | null;
  /** Last quarter-hour minute projected (for deduplicating clock chime messages). */
  lastQuarterHourForChime?: number | null;
  /**
   * Last sequence_number applied per room_id for room_occupants.
   * Server-authoritative: ignore room_occupants with older sequence to avoid
   * stale updates (e.g. second NPC stays after death).
   */
  lastRoomOccupantsSequenceByRoom?: Record<string, number>;
  /** Pending follow request (target player only). Cleared when user accepts/declines or request expires. */
  pendingFollowRequest?: { request_id: string; requestor_name: string } | null;
  /** Pending party invite (invitee only). Cleared when user accepts/declines or invite expires. */
  pendingPartyInvite?: { invite_id: string; inviter_name: string } | null;
  /** Who the player is following (for title panel). Server-authoritative. */
  followingTarget?: { target_name: string; target_type: 'player' | 'npc' } | null;
  /** Quest log (from game_state.quest_log or GET /quests). Server-authoritative. */
  questLog?: QuestLogEntry[];
  /** Lucidity meter/tier. Server-authoritative: from game_state's lucidity_tier or a lucidity_change event. */
  lucidityStatus?: LucidityStatus | null;
  /** Set by player_died, cleared by player_respawned. Server-authoritative. */
  isDead?: boolean;
  deathLocation?: string | null;
  /** Set by rescue_update(status: 'delirium'), cleared by player_delirium_respawned. Server-authoritative. */
  isDelirious?: boolean;
  deliriumLocation?: string | null;
  /** Containers this player currently has open, keyed by container_id. Populated only from the
   * personal container.opened delivery (carries mutation_token); a room broadcast of someone
   * else's open never creates an entry here -- see .cursor/rules/server-authority.mdc. */
  openContainers?: Record<string, OpenContainerState>;
  /** This player's carried inventory. Server-authoritative via inventory_updated. */
  playerInventory?: InventoryStack[];
  /** This player's equipped-slot items, keyed by slot_type. Server-authoritative via inventory_updated. */
  playerEquipped?: Record<string, InventoryStack>;
  /** Containers known to be in the current room (corpses seen via container.created since arrival;
   * see #711 known-gap notes -- containers already in the room before arrival are not backfilled). */
  roomContainers?: RoomContainerSummary[];
}
