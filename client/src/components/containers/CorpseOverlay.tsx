/**
 * CorpseOverlay component for displaying corpse containers with countdown timers.
 */

import React, { useMemo } from 'react';
import { useShallow } from 'zustand/react/shallow';
import type { ContainerComponent } from '../../stores/containerStore';
import { useContainerStore } from '../../stores/containerStore';
import { useGameStore } from '../../stores/gameStore';
import { isOpenContainerApiResponse } from '../../utils/apiTypeGuards';
import { API_V1_BASE } from '../../utils/config';
import { EldritchIcon, MythosIcons } from '../ui/EldritchIcon';
import { TerminalButton } from '../ui/TerminalButton';
import type { TimeRemaining } from './corpseOverlayUtils';
import { formatTimeRemaining, getCorpseTiming } from './corpseOverlayUtils';

function GracePeriodBanner(props: {
  remaining: TimeRemaining;
  isOwner: boolean;
  ended: boolean;
}): React.ReactElement | null {
  if (props.remaining.totalSeconds > 0) {
    return (
      <div className="mb-2 p-2 bg-mythos-terminal-warning/20 border border-mythos-terminal-warning rounded">
        <div className="text-sm font-semibold text-mythos-terminal-warning">
          Grace Period: {formatTimeRemaining(props.remaining.totalSeconds)}
        </div>
        {!props.isOwner && (
          <div className="text-xs text-mythos-terminal-text-secondary mt-1">
            Only the owner can access during grace period
          </div>
        )}
      </div>
    );
  }
  if (props.ended) {
    return (
      <div className="mb-2 p-2 bg-mythos-terminal-success/20 border border-mythos-terminal-success rounded">
        <div className="text-sm text-mythos-terminal-success">Grace period ended - All players can access</div>
      </div>
    );
  }
  return null;
}

function DecayBanner(props: { remaining: TimeRemaining | null }): React.ReactElement | null {
  if (!props.remaining) return null;
  if (props.remaining.totalSeconds > 0) {
    return (
      <div className="mb-2 p-2 bg-mythos-terminal-error/20 border border-mythos-terminal-error rounded">
        <div className="text-sm font-semibold text-mythos-terminal-error">
          Decays in: {formatTimeRemaining(props.remaining.totalSeconds)}
        </div>
      </div>
    );
  }
  return (
    <div className="mb-2 p-2 bg-mythos-terminal-error/30 border border-mythos-terminal-error rounded">
      <div className="text-sm font-semibold text-mythos-terminal-error">Corpse has decayed</div>
    </div>
  );
}

function CorpseCard(props: {
  corpse: ContainerComponent;
  playerId: string | undefined;
  onOpenCorpse: (containerId: string) => void;
  graceRemaining: TimeRemaining | null;
  decayRemaining: TimeRemaining | null;
  canOpen: boolean;
}): React.ReactElement {
  const { corpse, onOpenCorpse, graceRemaining, decayRemaining, canOpen } = props;
  const itemCount = corpse.items.length;

  return (
    <div
      className="mb-4 p-4 border border-mythos-terminal-error rounded bg-mythos-terminal-surface/90 backdrop-blur-sm"
      role="region"
      aria-label={`Corpse of ${corpse.owner_id || 'unknown'}`}
    >
      <div className="flex items-start justify-between mb-2">
        <div className="flex items-center gap-2">
          <EldritchIcon name={MythosIcons.horror} size={20} variant="error" />
          <h3 className="text-lg font-bold text-mythos-terminal-error">Corpse</h3>
        </div>
        {corpse.owner_id && <div className="text-sm text-mythos-terminal-text-secondary">Owner: {corpse.owner_id}</div>}
      </div>
      {graceRemaining && (
        <GracePeriodBanner
          remaining={graceRemaining}
          isOwner={props.playerId === corpse.owner_id}
          ended={graceRemaining.totalSeconds <= 0}
        />
      )}
      <DecayBanner remaining={decayRemaining} />
      <div className="mb-2 text-sm text-mythos-terminal-text">
        {itemCount} {itemCount === 1 ? 'item' : 'items'}
      </div>
      <TerminalButton
        onClick={() => void onOpenCorpse(corpse.container_id)}
        disabled={!canOpen}
        variant="danger"
        className="w-full"
        aria-label={`Open corpse container ${corpse.container_id}`}
      >
        {canOpen ? 'Open Corpse' : 'Grace Period Active'}
      </TerminalButton>
    </div>
  );
}

export interface CorpseOverlayProps {
  onOpen?: (containerId: string) => void;
  className?: string;
}

export const CorpseOverlay: React.FC<CorpseOverlayProps> = props => {
  const { onOpen, className = '' } = props;
  const { openContainers } = useContainerStore(useShallow(state => ({ openContainers: state.openContainers })));
  const openContainer = useContainerStore(state => state.openContainer);
  const { player, room } = useGameStore(useShallow(state => ({ player: state.player, room: state.room })));

  const corpseContainers = useMemo(() => {
    if (!room?.id) return [];
    return Object.values(openContainers).filter(
      container => container.source_type === 'corpse' && container.room_id === room.id
    );
  }, [openContainers, room]);

  if (corpseContainers.length === 0) return null;

  const handleOpenCorpse = async (containerId: string) => {
    try {
      const response = await fetch(`${API_V1_BASE}/api/containers/open`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${localStorage.getItem('authToken') || ''}`,
        },
        body: JSON.stringify({ container_id: containerId }),
      });
      if (!response.ok) return;
      const raw: unknown = await response.json();
      if (!isOpenContainerApiResponse(raw)) return;
      openContainer(raw.container as ContainerComponent, raw.mutation_token ?? '');
      onOpen?.(containerId);
    } catch (error) {
      console.error('Failed to open corpse container:', error);
    }
  };

  return (
    <div
      className={`fixed bottom-4 right-4 max-w-md z-50 ${className}`}
      role="complementary"
      aria-label="Corpse containers"
    >
      {corpseContainers.map(corpse => {
        const timing = getCorpseTiming(corpse, player?.id);
        return (
          <CorpseCard
            key={corpse.container_id}
            corpse={corpse}
            playerId={player?.id}
            onOpenCorpse={handleOpenCorpse}
            graceRemaining={timing.graceRemaining}
            decayRemaining={timing.decayRemaining}
            canOpen={timing.canOpen}
          />
        );
      })}
    </div>
  );
};
