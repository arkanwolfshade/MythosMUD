export type SanityTier = 'lucid' | 'uneasy' | 'fractured' | 'deranged' | 'catatonic';

export interface SanityChangeMeta {
  delta: number;
  reason?: string;
  source?: string;
  timestamp: string;
}

export interface SanityStatus {
  current: number;
  max: number;
  tier: SanityTier;
  liabilities: string[];
  lastChange?: SanityChangeMeta;
}

export type HallucinationSeverity = 'minor' | 'moderate' | 'severe';

export interface HallucinationMessage {
  id: string;
  title: string;
  description?: string;
  severity: HallucinationSeverity;
  category?: string;
  timestamp: string;
}

export type RescuePhase = 'idle' | 'catatonic' | 'channeling' | 'success' | 'failed' | 'sanitarium';

export interface RescueState {
  status: RescuePhase;
  targetName?: string;
  rescuerName?: string;
  progress?: number;
  etaSeconds?: number;
  message?: string;
  timestamp: string;
}
