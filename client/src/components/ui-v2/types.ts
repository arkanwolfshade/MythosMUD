// TypeScript interfaces for UI v2 panel system
// Based on existing game state types from GameTerminalWithPanels

export interface Player {
  name: string;
  profession_id?: number;
  profession_name?: string;
  profession_description?: string;
  profession_flavor_text?: string;
  stats?: {
    current_health: number;
    max_health?: number;
    sanity: number;
    max_sanity?: number;
    strength?: number;
    dexterity?: number;
    constitution?: number;
    intelligence?: number;
    wisdom?: number;
    charisma?: number;
    occult_knowledge?: number;
    fear?: number;
    corruption?: number;
    cult_affiliation?: number;
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
  occupants?: string[];
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
