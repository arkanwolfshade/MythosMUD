// TypeScript interfaces for UI v2 panel system
// Type definitions for UI v2 components

export interface Player {
  name: string;
  profession_id?: number;
  profession_name?: string;
  profession_description?: string;
  profession_flavor_text?: string;
  stats?: {
    current_db: number; // Represents determination points (DP)
    max_health?: number; // Represents max determination points (DP)
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

export interface ChatMessage {
  text: string;
  timestamp: string;
  isHtml: boolean;
  isCompleteHtml?: boolean;
  messageType?: string;
  channel?: string;
  type?: string;
  aliasChain?: Array<{
    original: string;
    expanded: string;
    alias_name: string;
  }>;
  rawText?: string;
  tags?: string[];
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
}

export interface PanelLayout {
  panels: Record<string, PanelState>;
}

export type PanelVariant = 'default' | 'eldritch' | 'elevated';

// Import MythosTimeState from the types directory
export type { MythosTimeState } from '../../types/mythosTime';
