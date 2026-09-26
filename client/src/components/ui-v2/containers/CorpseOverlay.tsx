import React, { useEffect, useState } from 'react';
import { ModalContainer } from '../primitives';
import type { RoomContainerSummary } from '../types';
import { formatTimeRemaining, getCorpseTiming } from './corpseOverlayUtils';

interface CorpseCardProps {
  corpse: RoomContainerSummary;
  playerId: string | undefined;
  onOpen: (containerId: string) => void;
}

function CorpseCard({ corpse, playerId, onOpen }: CorpseCardProps) {
  const { graceRemaining, decayRemaining, canOpen } = getCorpseTiming(corpse, playerId);
  const graceActive = graceRemaining !== null && graceRemaining.totalSeconds > 0;

  return (
    <div className="border border-mythos-terminal-border rounded p-2 bg-mythos-terminal-surface space-y-1 text-sm">
      <div className="font-medium text-mythos-terminal-text">Corpse</div>
      {graceActive ? (
        <p className="text-xs text-mythos-terminal-warning">
          Grace period: {formatTimeRemaining(graceRemaining.totalSeconds)}
          {!canOpen && <span className="block">Only the owner can access during grace period</span>}
        </p>
      ) : (
        <p className="text-xs text-mythos-terminal-text-secondary">Grace period ended - all players can access</p>
      )}
      {decayRemaining && (
        <p className="text-xs text-mythos-terminal-text-secondary">
          {decayRemaining.totalSeconds > 0
            ? `Decays in: ${formatTimeRemaining(decayRemaining.totalSeconds)}`
            : 'Corpse has decayed'}
        </p>
      )}
      <button
        type="button"
        disabled={!canOpen}
        className="text-xs px-2 py-0.5 rounded border border-mythos-terminal-border hover:bg-mythos-terminal-border/30 disabled:opacity-50"
        onClick={() => onOpen(corpse.container_id)}
      >
        Open
      </button>
    </div>
  );
}

interface CorpseOverlayProps {
  roomContainers: RoomContainerSummary[] | undefined;
  playerId: string | undefined;
  onOpen: (containerId: string) => void;
}

/**
 * Bottom-right overlay listing corpses in the current room, with a live grace/decay countdown
 * (#711). The countdown ticks locally every second; the underlying data (grace_period_start,
 * grace_period_seconds, decay_at) is server-authoritative from container.created.
 */
export const CorpseOverlay: React.FC<CorpseOverlayProps> = ({ roomContainers, playerId, onOpen }) => {
  // Unused value, only the setter matters: bumping it forces a re-render every second so the
  // countdown text stays live without storing derived time-remaining state.
  const [, forceTick] = useState(0);
  const corpses = (roomContainers ?? []).filter(c => c.source_type === 'corpse');

  useEffect(() => {
    if (corpses.length === 0) return;
    const interval = setInterval(() => forceTick(t => t + 1), 1000);
    return () => clearInterval(interval);
  }, [corpses.length]);

  if (corpses.length === 0) return null;

  return (
    <ModalContainer
      isOpen={true}
      onClose={() => {}}
      position="bottom-right"
      showCloseButton={false}
      maxWidth="sm"
      contentClassName="!bg-transparent !border-0 shadow-none p-0"
      className="space-y-2"
    >
      {corpses.map(corpse => (
        <CorpseCard key={corpse.container_id} corpse={corpse} playerId={playerId} onOpen={onOpen} />
      ))}
    </ModalContainer>
  );
};
