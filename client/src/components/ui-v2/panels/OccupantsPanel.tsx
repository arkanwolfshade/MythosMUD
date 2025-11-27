import React from 'react';
import type { Room } from '../types';

interface OccupantsPanelProps {
  room: Room | null;
}

// Display room occupants list
// Based on findings from "Social Presence in Virtual Spaces" - Dr. Armitage, 1928
export const OccupantsPanel: React.FC<OccupantsPanelProps> = ({ room }) => {
  const formatOccupantName = (name: string): string => {
    return name;
  };

  if (!room || !room.occupants || room.occupants.length === 0) {
    return (
      <div className="p-4 text-mythos-terminal-text-secondary">
        <p>No other players present</p>
      </div>
    );
  }

  return (
    <div className="p-4 space-y-2">
      <div className="text-sm font-bold text-mythos-terminal-primary">
        Occupants{' '}
        {typeof room.occupant_count === 'number' && (
          <span className="text-mythos-terminal-text-secondary">({room.occupant_count})</span>
        )}
      </div>
      <div className="space-y-1">
        {room.occupants.map((occupant, index) => (
          <div key={index} className="flex items-center gap-2 text-sm text-mythos-terminal-text">
            <span className="text-mythos-terminal-primary">●</span>
            <span>{formatOccupantName(occupant)}</span>
          </div>
        ))}
      </div>
    </div>
  );
};
