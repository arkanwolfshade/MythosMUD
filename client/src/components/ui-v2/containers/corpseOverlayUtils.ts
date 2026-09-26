// Corpse grace-period / decay countdown math. Ported from the deleted legacy
// client/src/components/containers/corpseOverlayUtils.ts (git show 018019dd0^:...), adapted to
// RoomContainerSummary. Pure functions; the component owns the setInterval tick.

import type { RoomContainerSummary } from '../types';

export interface TimeRemaining {
  hours: number;
  minutes: number;
  seconds: number;
  totalSeconds: number;
}

export function formatTimeRemaining(totalSeconds: number): string {
  if (totalSeconds <= 0) return 'Expired';
  const hours = Math.floor(totalSeconds / 3600);
  const minutes = Math.floor((totalSeconds % 3600) / 60);
  const seconds = totalSeconds % 60;
  if (hours > 0) return `${hours}h ${minutes}m`;
  if (minutes > 0) return `${minutes}m ${seconds}s`;
  return `${seconds}s`;
}

export function calculateTimeRemaining(targetDate: string | null | undefined): TimeRemaining | null {
  if (!targetDate) return null;
  const diff = Math.max(0, Math.floor((new Date(targetDate).getTime() - Date.now()) / 1000));
  return {
    hours: Math.floor(diff / 3600),
    minutes: Math.floor((diff % 3600) / 60),
    seconds: diff % 60,
    totalSeconds: diff,
  };
}

function graceMetadata(corpse: RoomContainerSummary): { start: string | undefined; seconds: number } {
  const start = corpse.metadata?.grace_period_start;
  const seconds = corpse.metadata?.grace_period_seconds;
  return {
    start: typeof start === 'string' ? start : undefined,
    seconds: typeof seconds === 'number' ? seconds : 300,
  };
}

export function isCorpseOwner(corpse: RoomContainerSummary, playerId: string | undefined): boolean {
  return corpse.owner_id === playerId;
}

export function isGracePeriodActive(corpse: RoomContainerSummary): boolean {
  const { start, seconds } = graceMetadata(corpse);
  if (!start) return false;
  const end = new Date(start).getTime() + seconds * 1000;
  return Date.now() < end;
}

export interface CorpseTiming {
  graceRemaining: TimeRemaining | null;
  decayRemaining: TimeRemaining | null;
  canOpen: boolean;
}

export function getCorpseTiming(corpse: RoomContainerSummary, playerId: string | undefined): CorpseTiming {
  const { start, seconds } = graceMetadata(corpse);
  const graceEnd = start ? new Date(new Date(start).getTime() + seconds * 1000).toISOString() : undefined;
  const graceRemaining = graceEnd ? calculateTimeRemaining(graceEnd) : null;
  const decayRemaining = calculateTimeRemaining(corpse.decay_at);
  const isOwner = isCorpseOwner(corpse, playerId);
  const graceActive = isGracePeriodActive(corpse);
  return { graceRemaining, decayRemaining, canOpen: !graceActive || isOwner };
}
