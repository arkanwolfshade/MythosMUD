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

/**
 * Pure UI projection for lucidity meter when only `player.stats` is available (no server tier yet).
 * Does not invent a tier -- the server is authoritative for that (server-authority.mdc).
 */
export function deriveLucidityStatusFromPlayer(
  player: { stats?: { lucidity?: number; max_lucidity?: number } } | null | undefined,
  previousLastChange: LucidityChangeMeta | undefined
): LucidityStatus | null {
  if (player?.stats?.lucidity === undefined) return null;
  return {
    current: player.stats.lucidity,
    max: player.stats.max_lucidity ?? 100,
    liabilities: [],
    lastChange: previousLastChange,
  };
}
