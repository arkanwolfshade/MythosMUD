import React from 'react';
import type { Room } from '../types';

interface OccupantsPanelProps {
  room: Room | null;
}

function OccupantColumn({ title, names, bulletClass }: { title: string; names: string[]; bulletClass: string }) {
  return (
    <div className="space-y-2">
      <div className="text-xs font-semibold text-mythos-terminal-primary uppercase border-b border-mythos-terminal-primary/30 pb-1">
        {title} {names.length > 0 && `(${names.length})`}
      </div>
      {names.length > 0 ? (
        <div className="space-y-1">
          {names.map((name, index) => (
            <div key={index} className="flex items-center gap-2 text-sm text-mythos-terminal-text">
              <span className={bulletClass}>●</span>
              <span>{name}</span>
            </div>
          ))}
        </div>
      ) : (
        <div className="text-xs text-mythos-terminal-text-secondary italic">None</div>
      )}
    </div>
  );
}

// Display room occupants list with separate columns for players and NPCs
// Based on findings from "Social Presence in Virtual Spaces" - Dr. Armitage, 1928
// AI Agent: Enhanced to display players and NPCs in separate columns per bug investigation
export const OccupantsPanel: React.FC<OccupantsPanelProps> = ({ room }) => {
  const players = room?.players ?? [];
  const npcs = room?.npcs ?? [];
  const hasContent = players.length > 0 || npcs.length > 0;

  if (!room || !hasContent) {
    return (
      <div className="p-4 text-mythos-terminal-text-secondary">
        <p>No other players present</p>
      </div>
    );
  }

  return (
    <div className="p-4 space-y-3">
      <div className="grid grid-cols-2 gap-4">
        <OccupantColumn title="Players" names={players} bulletClass="text-mythos-terminal-primary" />
        <OccupantColumn title="NPCs" names={npcs} bulletClass="text-amber-500" />
      </div>
    </div>
  );
};
