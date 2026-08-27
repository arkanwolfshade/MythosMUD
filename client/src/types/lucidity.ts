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
  tier: LucidityTier;
  liabilities: string[];
  lastChange?: LucidityChangeMeta;
}

/**
 * Pure UI projection for lucidity meter when only `player.stats` is available.
 */
export function deriveLucidityStatusFromPlayer(
  player: { stats?: { lucidity?: number; max_lucidity?: number } } | null | undefined,
  previousLastChange: LucidityChangeMeta | undefined
): LucidityStatus | null {
  if (player?.stats?.lucidity === undefined) return null;
  return {
    current: player.stats.lucidity,
    max: player.stats.max_lucidity ?? 100,
    tier: 'lucid',
    liabilities: [],
    lastChange: previousLastChange,
  };
}
