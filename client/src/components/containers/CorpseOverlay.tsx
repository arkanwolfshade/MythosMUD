/**
 * CorpseOverlay component for displaying corpse containers with countdown timers.
 *
 * As documented in the restricted archives of Miskatonic University, corpse
 * overlay components provide visual indicators for fallen investigators, displaying
 * grace period countdowns and decay timers.
 */

import React, { useMemo } from 'react';
import type { ContainerComponent } from '../../stores/containerStore';
import { useContainerStore } from '../../stores/containerStore';
import { useGameStore } from '../../stores/gameStore';
import { EldritchIcon, MythosIcons } from '../ui/EldritchIcon';
import { TerminalButton } from '../ui/TerminalButton';

export interface CorpseOverlayProps {
  /** Callback when corpse container is opened */
  onOpen?: (containerId: string) => void;
  /** Custom class name */
  className?: string;
}

interface TimeRemaining {
  hours: number;
  minutes: number;
  seconds: number;
  totalSeconds: number;
}

/**
 * Format time remaining in a human-readable format.
 */
const formatTimeRemaining = (totalSeconds: number): string => {
  if (totalSeconds <= 0) {
    return 'Expired';
  }

  const hours = Math.floor(totalSeconds / 3600);
  const minutes = Math.floor((totalSeconds % 3600) / 60);
  const seconds = totalSeconds % 60;

  if (hours > 0) {
    return `${hours}h ${minutes}m`;
  } else if (minutes > 0) {
    return `${minutes}m ${seconds}s`;
  } else {
    return `${seconds}s`;
  }
};

/**
 * Calculate time remaining until a target date.
 */
const calculateTimeRemaining = (targetDate: string | undefined): TimeRemaining | null => {
  if (!targetDate) {
    return null;
  }

  const target = new Date(targetDate);
  const now = new Date();
  const diff = Math.max(0, Math.floor((target.getTime() - now.getTime()) / 1000));

  return {
    hours: Math.floor(diff / 3600),
    minutes: Math.floor((diff % 3600) / 60),
    seconds: diff % 60,
    totalSeconds: diff,
  };
};

/**
 * Check if current player is the corpse owner.
 */
const isCorpseOwner = (corpse: ContainerComponent, playerId: string | undefined): boolean => {
  return corpse.owner_id === playerId;
};

/**
 * Check if grace period is active.
 */
const isGracePeriodActive = (corpse: ContainerComponent): boolean => {
  const gracePeriodStart = corpse.metadata.grace_period_start as string | undefined;
  const gracePeriodSeconds = (corpse.metadata.grace_period_seconds as number) || 300;

  if (!gracePeriodStart) {
    return false;
  }

  const start = new Date(gracePeriodStart);
  const end = new Date(start.getTime() + gracePeriodSeconds * 1000);
  const now = new Date();

  return now < end;
};

/**
 * CorpseOverlay component displays corpse containers with countdown timers.
 *
 * Features:
 * - Grace period countdown (owner-only access)
 * - Decay countdown (cleanup timer)
 * - Item count display
 * - Open container button
 * - Keyboard accessible
 */
export const CorpseOverlay: React.FC<CorpseOverlayProps> = ({ onOpen, className = '' }) => {
  const getCorpseContainersInRoom = useContainerStore(state => state.getCorpseContainersInRoom);
  const openContainer = useContainerStore(state => state.openContainer);
  const player = useGameStore(state => state.player);
  const room = useGameStore(state => state.room);

  // Note: Time-based updates are handled by the store, not needed here

  const corpseContainers = useMemo(() => {
    if (!room?.id) {
      return [];
    }
    return getCorpseContainersInRoom(room.id);
  }, [getCorpseContainersInRoom, room]);

  // Don't render if no corpses
  if (corpseContainers.length === 0) {
    return null;
  }

  const handleOpenCorpse = async (containerId: string) => {
    // Open container via API - mutation token will be returned
    try {
      const response = await fetch('/api/containers/open', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${localStorage.getItem('authToken') || ''}`,
        },
        body: JSON.stringify({ container_id: containerId }),
      });

      if (response.ok) {
        const data = await response.json();
        // Store mutation token in container store
        const container = data.container as ContainerComponent;
        const mutationToken = data.mutation_token as string;
        openContainer(container, mutationToken);
        onOpen?.(containerId);
      }
    } catch (error) {
      console.error('Failed to open corpse container:', error);
    }
  };

  const renderCorpse = (corpse: ContainerComponent) => {
    const gracePeriodStart = corpse.metadata.grace_period_start as string | undefined;
    const gracePeriodSeconds = (corpse.metadata.grace_period_seconds as number) || 300;
    const gracePeriodEnd = gracePeriodStart
      ? new Date(new Date(gracePeriodStart).getTime() + gracePeriodSeconds * 1000)
      : null;

    const gracePeriodRemaining = gracePeriodEnd ? calculateTimeRemaining(gracePeriodEnd.toISOString()) : null;
    const decayRemaining = calculateTimeRemaining(corpse.decay_at);

    const isOwner = isCorpseOwner(corpse, player?.id);
    const graceActive = isGracePeriodActive(corpse);
    const canOpen = !graceActive || isOwner;

    const itemCount = corpse.items.length;

    return (
      <div
        key={corpse.container_id}
        className="mb-4 p-4 border border-mythos-terminal-error rounded bg-mythos-terminal-surface/90 backdrop-blur-sm"
        role="region"
        aria-label={`Corpse of ${corpse.owner_id || 'unknown'}`}
      >
        <div className="flex items-start justify-between mb-2">
          <div className="flex items-center gap-2">
            <EldritchIcon name={MythosIcons.horror} size={20} variant="error" />
            <h3 className="text-lg font-bold text-mythos-terminal-error">Corpse</h3>
          </div>
          {corpse.owner_id && (
            <div className="text-sm text-mythos-terminal-text-secondary">Owner: {corpse.owner_id}</div>
          )}
        </div>

        {/* Grace Period Countdown */}
        {gracePeriodRemaining && gracePeriodRemaining.totalSeconds > 0 && (
          <div className="mb-2 p-2 bg-mythos-terminal-warning/20 border border-mythos-terminal-warning rounded">
            <div className="text-sm font-semibold text-mythos-terminal-warning">
              Grace Period: {formatTimeRemaining(gracePeriodRemaining.totalSeconds)}
            </div>
            {!isOwner && (
              <div className="text-xs text-mythos-terminal-text-secondary mt-1">
                Only the owner can access during grace period
              </div>
            )}
          </div>
        )}

        {gracePeriodRemaining && gracePeriodRemaining.totalSeconds <= 0 && (
          <div className="mb-2 p-2 bg-mythos-terminal-success/20 border border-mythos-terminal-success rounded">
            <div className="text-sm text-mythos-terminal-success">Grace period ended - All players can access</div>
          </div>
        )}

        {/* Decay Countdown */}
        {decayRemaining && decayRemaining.totalSeconds > 0 && (
          <div className="mb-2 p-2 bg-mythos-terminal-error/20 border border-mythos-terminal-error rounded">
            <div className="text-sm font-semibold text-mythos-terminal-error">
              Decays in: {formatTimeRemaining(decayRemaining.totalSeconds)}
            </div>
          </div>
        )}

        {decayRemaining && decayRemaining.totalSeconds <= 0 && (
          <div className="mb-2 p-2 bg-mythos-terminal-error/30 border border-mythos-terminal-error rounded">
            <div className="text-sm font-semibold text-mythos-terminal-error">Corpse has decayed</div>
          </div>
        )}

        {/* Item Count */}
        <div className="mb-2 text-sm text-mythos-terminal-text">
          {itemCount} {itemCount === 1 ? 'item' : 'items'}
        </div>

        {/* Open Button */}
        <TerminalButton
          onClick={() => {
            void handleOpenCorpse(corpse.container_id);
          }}
          disabled={!canOpen}
          variant="danger"
          className="w-full"
          aria-label={`Open corpse container ${corpse.container_id}`}
          onKeyDown={e => {
            if (e.key === 'Enter' || e.key === ' ') {
              e.preventDefault();
              if (canOpen) {
                void handleOpenCorpse(corpse.container_id);
              }
            }
          }}
        >
          {canOpen ? 'Open Corpse' : 'Grace Period Active'}
        </TerminalButton>
      </div>
    );
  };

  return (
    <div
      className={`fixed bottom-4 right-4 max-w-md z-50 ${className}`}
      role="complementary"
      aria-label="Corpse containers"
    >
      {corpseContainers.map(corpse => renderCorpse(corpse))}
    </div>
  );
};
