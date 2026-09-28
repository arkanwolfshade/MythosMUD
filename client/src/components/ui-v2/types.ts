// TypeScript interfaces for UI v2 panel system
// Type definitions for UI v2 components

export interface Player {
  /** Character/player UUID from server (player_id). Used for Skills tab URL, etc. */
  id?: string;
  name: string;
  profession_id?: number;
  profession_name?: string;
  profession_description?: string;
  profession_flavor_text?: string;
  stats?: {
    current_dp: number; // Represents determination points (DP)
    max_dp?: number; // Represents max determination points (DP)
    lucidity: number;
    max_lucidity?: number;
    strength?: number;
    dexterity?: number;
    constitution?: number;
    size?: number;
    intelligence?: number;
    power?: number;
    education?: number;
    charisma?: number;
    luck?: number;
    occult?: number;
    corruption?: number;
    magic_points?: number;
    max_magic_points?: number;
    position?: string;
  };
  level?: number;
  experience?: number;
  xp?: number;
  current_room_id?: string;
  in_combat?: boolean;
}

export interface Room {
  id: string;
  name: string;
  description: string;
  plane?: string;
  zone?: string;
  sub_zone?: string;
  environment?: string;
  exits: Record<string, string>;
  // Legacy: flat list of occupant names (for backward compatibility)
  occupants?: string[];
  // New: structured occupant data with separate players and NPCs
  players?: string[];
  npcs?: string[];
  occupant_count?: number;
  entities?: Array<{
    name: string;
    type: string;
  }>;
}

/** Single quest log entry (same shape as GET /api/players/{id}/quests and game_state.quest_log). */
export interface QuestLogEntry {
  quest_id: string;
  name: string;
  title: string;
  description: string;
  goals_with_progress: Array<{
    goal_type?: string;
    target?: string;
    current?: number;
    required?: number;
    done?: boolean;
    [key: string]: unknown;
  }>;
  state: string;
}

export interface ChatMessage {
  text: string;
  timestamp: string;
  isHtml: boolean;
  isCompleteHtml?: boolean;
  messageType?: string;
  channel?: string;
  type?: string;
  /** Optional: 'npc' | 'system' when server marks non-player speakers. */
  speakerKind?: string;
  aliasChain?: Array<{
    original: string;
    expanded: string;
    alias_name: string;
  }>;
  rawText?: string;
  tags?: string[];
}

/** Weapon stats on an inventory stack (mirrors server WeaponStats). */
interface WeaponStats {
  min_damage: number;
  max_damage: number;
  modifier?: number;
  damage_types?: string[];
  magical?: boolean;
}

/** A stack of items, in a container or in a player's inventory (mirrors server InventoryStack). */
export interface InventoryStack {
  item_instance_id: string;
  prototype_id: string;
  item_id: string;
  item_name: string;
  slot_type: string;
  quantity: number;
  metadata?: Record<string, unknown>;
  weapon?: WeaponStats;
  flags?: string[];
  origin?: Record<string, unknown>;
  created_at?: string;
  inner_container?: {
    capacity_slots: number;
    items: InventoryStack[];
    lock_state?: string | null;
    allowed_roles?: string[];
  } | null;
}

type ContainerSourceType = 'environment' | 'equipment' | 'corpse';
type ContainerLockState = 'unlocked' | 'locked' | 'sealed';

/** Full container state (mirrors server ContainerComponent.model_dump()). */
export interface ContainerSnapshot {
  container_id: string;
  source_type: ContainerSourceType;
  owner_id?: string | null;
  room_id?: string | null;
  entity_id?: string | null;
  lock_state: ContainerLockState;
  capacity_slots: number;
  weight_limit?: number | null;
  decay_at?: string | null;
  allowed_roles: string[];
  items: InventoryStack[];
  metadata: Record<string, unknown>;
}

/** Room-level container summary, populated from container.created (corpse spawn). */
export interface RoomContainerSummary {
  container_id: string;
  source_type: ContainerSourceType;
  owner_id?: string | null;
  decay_at?: string | null;
  metadata?: Record<string, unknown>;
}

export interface PanelPosition {
  x: number;
  y: number;
}

export interface PanelSize {
  width: number;
  height: number;
}

export interface PanelState {
  id: string;
  title: string;
  position: PanelPosition;
  size: PanelSize;
  isMinimized: boolean;
  isMaximized: boolean;
  isVisible: boolean;
  zIndex: number;
  minSize?: PanelSize;
  maxSize?: PanelSize;
  /** When true, panel uses opaque background so it stays readable over other panels (e.g. minimap popout). */
  opaque?: boolean;
  /** Minimum content height in px so the panel does not collapse (e.g. inline map visibility). */
  minHeight?: number;
  /** Layout saved when minimizing; restored when the panel is expanded again. */
  preMinimizePosition?: PanelPosition;
  preMinimizeSize?: PanelSize;
}

export type PanelVariant = 'default' | 'eldritch' | 'elevated';

// Import MythosTimeState from the types directory
export type { MythosTimeState } from '../../types/mythosTime';
