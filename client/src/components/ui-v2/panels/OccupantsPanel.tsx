import React from 'react';
import type { Room } from '../types';

interface OccupantsPanelProps {
  room: Room | null;
}

// Display room occupants list with separate columns for players and NPCs
// Based on findings from "Social Presence in Virtual Spaces" - Dr. Armitage, 1928
// AI Agent: Enhanced to display players and NPCs in separate columns per bug investigation
export const OccupantsPanel: React.FC<OccupantsPanelProps> = ({ room }) => {
  const formatOccupantName = (name: string): string => {
    return name;
  };

  // Get players and NPCs from structured data, or fall back to legacy format
  const players = room?.players ?? [];
  const npcs = room?.npcs ?? [];
  const legacyOccupants = room?.occupants ?? [];

  // DEBUG: Log what we're receiving - use JSON.stringify to see full array contents
  console.log('🔍 [OccupantsPanel] Render with room:', {
    roomId: room?.id,
    hasRoom: !!room,
    players: JSON.stringify(players),
    playersCount: players.length,
    npcs: JSON.stringify(npcs),
    npcsCount: npcs.length,
    legacyOccupants: JSON.stringify(legacyOccupants),
    legacyCount: legacyOccupants.length,
    roomKeys: room ? Object.keys(room) : [],
    hasRoomNpcs: !!room?.npcs,
    roomNpcsType: typeof room?.npcs,
    roomNpcsIsArray: Array.isArray(room?.npcs),
  });

  // Use structured data if available, otherwise use legacy format
  const hasStructuredData = players.length > 0 || npcs.length > 0;
  const hasLegacyData = !hasStructuredData && legacyOccupants.length > 0;

  if (!room || (!hasStructuredData && !hasLegacyData)) {
    return (
      <div className="p-4 text-mythos-terminal-text-secondary">
        <p>No other players present</p>
      </div>
    );
  }

  return (
    <div className="p-4 space-y-3">
      {hasStructuredData ? (
        // New structured format: separate columns for players and NPCs
        <div className="grid grid-cols-2 gap-4">
          {/* Players Column */}
          <div className="space-y-2">
            <div className="text-xs font-semibold text-mythos-terminal-primary uppercase border-b border-mythos-terminal-primary/30 pb-1">
              Players {players.length > 0 && `(${players.length})`}
            </div>
            {players.length > 0 ? (
              <div className="space-y-1">
                {players.map((player, index) => (
                  <div key={index} className="flex items-center gap-2 text-sm text-mythos-terminal-text">
                    <span className="text-mythos-terminal-primary">●</span>
                    <span>{formatOccupantName(player)}</span>
                  </div>
                ))}
              </div>
            ) : (
              <div className="text-xs text-mythos-terminal-text-secondary italic">None</div>
            )}
          </div>

          {/* NPCs Column */}
          <div className="space-y-2">
            <div className="text-xs font-semibold text-mythos-terminal-primary uppercase border-b border-mythos-terminal-primary/30 pb-1">
              NPCs {npcs.length > 0 && `(${npcs.length})`}
            </div>
            {npcs.length > 0 ? (
              <div className="space-y-1">
                {npcs.map((npc, index) => (
                  <div key={index} className="flex items-center gap-2 text-sm text-mythos-terminal-text">
                    <span className="text-amber-500">●</span>
                    <span>{formatOccupantName(npc)}</span>
                  </div>
                ))}
              </div>
            ) : (
              <div className="text-xs text-mythos-terminal-text-secondary italic">None</div>
            )}
          </div>
        </div>
      ) : (
        // Legacy format: single list (backward compatibility)
        <div className="space-y-1">
          {legacyOccupants.map((occupant, index) => (
            <div key={index} className="flex items-center gap-2 text-sm text-mythos-terminal-text">
              <span className="text-mythos-terminal-primary">●</span>
              <span>{formatOccupantName(occupant)}</span>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};
