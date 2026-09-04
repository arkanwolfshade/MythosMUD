import React from 'react';
import type { Room } from '../types';

interface OccupantsPanelProps {
  room: Room | null;
}

function occupantLists(room: Room | null): { players: string[]; npcs: string[] } {
  return { players: room?.players ?? [], npcs: room?.npcs ?? [] };
}

function OccupantNames({ names, bulletClass }: { names: string[]; bulletClass: string }) {
  if (names.length === 0) {
    return <div className="text-xs text-mythos-terminal-text-secondary italic">None</div>;
  }
  return (
    <div className="space-y-1">
      {names.map((name, index) => (
        <div key={index} className="flex items-center gap-2 text-sm text-mythos-terminal-text">
          <span className={bulletClass}>●</span>
          <span>{name}</span>
        </div>
      ))}
    </div>
  );
}

function OccupantColumn({ title, names, bulletClass }: { title: string; names: string[]; bulletClass: string }) {
  const countSuffix = names.length === 0 ? '' : ` (${names.length})`;
  return (
    <div className="space-y-2">
      <div className="text-xs font-semibold text-mythos-terminal-primary uppercase border-b border-mythos-terminal-primary/30 pb-1">
        {title}
        {countSuffix}
      </div>
      <OccupantNames names={names} bulletClass={bulletClass} />
    </div>
  );
}

function EmptyOccupantsPanel() {
  return (
    <div className="p-4 text-mythos-terminal-text-secondary" data-testid="occupants-other-players" data-names="">
      <p>No other players present</p>
    </div>
  );
}

// Display room occupants list with separate columns for players and NPCs
// Based on findings from "Social Presence in Virtual Spaces" - Dr. Armitage, 1928
// AI Agent: Enhanced to display players and NPCs in separate columns per bug investigation
export const OccupantsPanel: React.FC<OccupantsPanelProps> = ({ room }) => {
  const { players, npcs } = occupantLists(room);
  if (!room || (players.length === 0 && npcs.length === 0)) {
    return <EmptyOccupantsPanel />;
  }

  return (
    <div className="p-4 space-y-3" data-testid="occupants-other-players" data-names={players.join('\n')}>
      <div className="grid grid-cols-2 gap-4">
        <OccupantColumn title="Players" names={players} bulletClass="text-mythos-terminal-primary" />
        <OccupantColumn title="NPCs" names={npcs} bulletClass="text-amber-500" />
      </div>
    </div>
  );
};
