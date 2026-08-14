import type { ContainerComponent } from '../../stores/containerStore';

export interface TimeRemaining {
  hours: number;
  minutes: number;
  seconds: number;
  totalSeconds: number;
}

export const formatTimeRemaining = (totalSeconds: number): string => {
  if (totalSeconds <= 0) return 'Expired';
  const hours = Math.floor(totalSeconds / 3600);
  const minutes = Math.floor((totalSeconds % 3600) / 60);
  const seconds = totalSeconds % 60;
  if (hours > 0) return `${hours}h ${minutes}m`;
  if (minutes > 0) return `${minutes}m ${seconds}s`;
  return `${seconds}s`;
};

export const calculateTimeRemaining = (targetDate: string | undefined): TimeRemaining | null => {
  if (!targetDate) return null;
  const diff = Math.max(0, Math.floor((new Date(targetDate).getTime() - Date.now()) / 1000));
  return {
    hours: Math.floor(diff / 3600),
    minutes: Math.floor((diff % 3600) / 60),
    seconds: diff % 60,
    totalSeconds: diff,
  };
};

export const isCorpseOwner = (corpse: ContainerComponent, playerId: string | undefined): boolean =>
  corpse.owner_id === playerId;

export const isGracePeriodActive = (corpse: ContainerComponent): boolean => {
  const gracePeriodStart = corpse.metadata.grace_period_start as string | undefined;
  const gracePeriodSeconds = (corpse.metadata.grace_period_seconds as number) || 300;
  if (!gracePeriodStart) return false;
  const end = new Date(gracePeriodStart).getTime() + gracePeriodSeconds * 1000;
  return Date.now() < end;
};

export function getCorpseTiming(
  corpse: ContainerComponent,
  playerId: string | undefined
): {
  graceRemaining: TimeRemaining | null;
  decayRemaining: TimeRemaining | null;
  canOpen: boolean;
} {
  const gracePeriodStart = corpse.metadata.grace_period_start as string | undefined;
  const gracePeriodSeconds = (corpse.metadata.grace_period_seconds as number) || 300;
  const gracePeriodEnd = gracePeriodStart
    ? new Date(new Date(gracePeriodStart).getTime() + gracePeriodSeconds * 1000).toISOString()
    : undefined;
  const graceRemaining = gracePeriodEnd ? calculateTimeRemaining(gracePeriodEnd) : null;
  const decayRemaining = calculateTimeRemaining(corpse.decay_at);
  const isOwner = isCorpseOwner(corpse, playerId);
  const graceActive = isGracePeriodActive(corpse);
  return { graceRemaining, decayRemaining, canOpen: !graceActive || isOwner };
}
