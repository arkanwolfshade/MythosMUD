export type LucidityTier = 'lucid' | 'uneasy' | 'fractured' | 'deranged' | 'catatonic';

export interface LucidityChangeMeta {
  delta: number;
  reason?: string;
  source?: string;
  timestamp: string;
}

export interface LucidityStatus {
  current: number;
  max: number;
  /** Server-authoritative (PlayerLucidity.current_tier); absent until game_state/lucidity_change supplies it. */
  tier?: LucidityTier;
  liabilities: string[];
  lastChange?: LucidityChangeMeta;
}
