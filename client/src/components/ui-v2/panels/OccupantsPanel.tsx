import React from 'react';
import { npcCategory, type NpcOccupant } from '../../../types/messageCategory';
import type { Room } from '../types';
import { getMessageCategoryClass } from '../utils/messageCategoryStyle';

interface OccupantsPanelProps {
  room: Room | null;
}

function occupantLists(room: Room | null): { players: string[]; npcs: NpcOccupant[] } {
  return { players: room?.players ?? [], npcs: room?.npcs ?? [] };
}

function EmptyColumn() {
  return <div className="text-xs text-mythos-terminal-text-secondary italic">None</div>;
}

function PlayerNames({ names }: { names: string[] }) {
  if (names.length === 0) {
    return <EmptyColumn />;
  }
  return (
    <div className="space-y-1">
      {names.map((name, index) => (
        <div key={index} className="flex items-center gap-2 text-sm text-mythos-terminal-text">
          <span className="text-mythos-terminal-primary">●</span>
          <span>{name}</span>
        </div>
      ))}
    </div>
  );
}

// The npc.<disposition> category supplies colour, glyph (::before) and the text-label mode word, so
// disposition is never carried by colour alone.
function NpcNames({ npcs }: { npcs: NpcOccupant[] }) {
  if (npcs.length === 0) {
    return <EmptyColumn />;
  }
  return (
    <div className="space-y-1">
      {npcs.map((npc, index) => (
        <div
          key={index}
          className={`text-sm ${getMessageCategoryClass(npcCategory(npc.disposition)) ?? ''}`}
          data-disposition={npc.disposition}
        >
          {npc.name}
        </div>
      ))}
    </div>
  );
}

function OccupantColumn({ title, count, children }: { title: string; count: number; children: React.ReactNode }) {
  const countSuffix = count === 0 ? '' : ` (${count})`;
  return (
    <div className="space-y-2">
      <div className="text-xs font-semibold text-mythos-terminal-primary uppercase border-b border-mythos-terminal-primary/30 pb-1">
        {title}
        {countSuffix}
      </div>
      {children}
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
        <OccupantColumn title="Players" count={players.length}>
          <PlayerNames names={players} />
        </OccupantColumn>
        <OccupantColumn title="NPCs" count={npcs.length}>
          <NpcNames npcs={npcs} />
        </OccupantColumn>
      </div>
    </div>
  );
};
