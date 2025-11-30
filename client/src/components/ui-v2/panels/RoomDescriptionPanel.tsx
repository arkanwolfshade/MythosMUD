import React from 'react';
import type { Room } from '../types';

interface RoomDescriptionPanelProps {
  room: Room | null;
}

// Display room description
// Based on findings from "Descriptive Text in Mythos Interfaces" - Dr. Armitage, 1928
export const RoomDescriptionPanel: React.FC<RoomDescriptionPanelProps> = ({ room }) => {
  const formatDescription = (description: string): string => {
    if (!description) return 'No description available';
    return description.trim().replace(/\s+/g, ' ');
  };

  if (!room) {
    return (
      <div className="p-4 text-mythos-terminal-text-secondary">
        <p>No room description available</p>
      </div>
    );
  }

  return (
    <div className="p-4 space-y-2">
      <div className="text-sm font-bold text-mythos-terminal-primary">Description</div>
      <div className="text-sm text-mythos-terminal-text leading-relaxed whitespace-pre-wrap">
        {formatDescription(room.description)}
      </div>
    </div>
  );
};
