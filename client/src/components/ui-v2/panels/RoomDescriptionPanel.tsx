import React from 'react';
import type { Room } from '../types';
import { getMessageCategoryClass } from '../utils/messageCategoryStyle';

// Same vocabulary as a room.description line in Game Info; the server always sends this text as that category.
const ROOM_DESCRIPTION_CLASS = getMessageCategoryClass('room.description') ?? 'text-mythos-terminal-text';

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
      <div className={`text-sm leading-relaxed whitespace-pre-wrap ${ROOM_DESCRIPTION_CLASS}`}>
        {formatDescription(room.description)}
      </div>
    </div>
  );
};
