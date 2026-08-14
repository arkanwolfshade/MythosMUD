/**
 * Room Details Panel component.
 */

import React from 'react';
import type { Room } from '../../stores/gameStore';

export interface RoomDetailsPanelProps {
  room: Room;
  onClose: () => void;
  onEditRoom?: (roomId: string) => void;
  onCreateExit?: () => void;
  isAdmin?: boolean;
}

function RoomAdminActions(props: {
  roomId: string;
  onEditRoom?: (roomId: string) => void;
  onCreateExit?: () => void;
}): React.ReactElement | null {
  if (!props.onEditRoom && !props.onCreateExit) {
    return null;
  }
  return (
    <div className="mb-4 space-y-2">
      {props.onEditRoom && (
        <button
          onClick={() => props.onEditRoom?.(props.roomId)}
          className="w-full px-3 py-2 bg-mythos-terminal-primary text-white rounded hover:bg-mythos-terminal-primary/80 text-sm"
        >
          Edit Room
        </button>
      )}
      {props.onCreateExit && (
        <button
          onClick={props.onCreateExit}
          className="w-full px-3 py-2 bg-mythos-terminal-success text-white rounded hover:bg-mythos-terminal-success/80 text-sm"
        >
          Create Exit
        </button>
      )}
    </div>
  );
}

function RoomLocationFields(props: { room: Room }): React.ReactElement {
  const { room } = props;
  return (
    <div className="mb-4 space-y-1">
      {room.plane && (
        <div>
          <span className="text-xs text-mythos-terminal-text/70">Plane:</span>
          <span className="text-sm text-mythos-terminal-text ml-2">{room.plane}</span>
        </div>
      )}
      {room.zone && (
        <div>
          <span className="text-xs text-mythos-terminal-text/70">Zone:</span>
          <span className="text-sm text-mythos-terminal-text ml-2">{room.zone}</span>
        </div>
      )}
      {room.sub_zone && (
        <div>
          <span className="text-xs text-mythos-terminal-text/70">Sub-zone:</span>
          <span className="text-sm text-mythos-terminal-text ml-2">{room.sub_zone}</span>
        </div>
      )}
      {room.environment && (
        <div>
          <span className="text-xs text-mythos-terminal-text/70">Environment:</span>
          <span className="text-sm text-mythos-terminal-text ml-2">{room.environment}</span>
        </div>
      )}
    </div>
  );
}

function RoomExitsList(props: { exits: Record<string, string> }): React.ReactElement {
  return (
    <div>
      <span className="text-xs text-mythos-terminal-text/70">Exits:</span>
      <div className="text-sm text-mythos-terminal-text mt-1 space-y-1">
        {Object.entries(props.exits).map(([direction, target]) => (
          <div key={direction} className="flex justify-between">
            <span>{direction}:</span>
            <span className="font-mono text-mythos-terminal-primary">{target}</span>
          </div>
        ))}
      </div>
    </div>
  );
}

export const RoomDetailsPanel: React.FC<RoomDetailsPanelProps> = props => {
  const { room, onClose, onEditRoom, onCreateExit, isAdmin = false } = props;

  return (
    <div className="absolute top-4 right-4 w-80 bg-mythos-terminal-background border border-mythos-terminal-border rounded shadow-lg p-4 z-20 max-h-panel overflow-y-auto">
      <div className="flex justify-between items-start mb-4">
        <h3 className="text-lg font-bold text-mythos-terminal-text">{room.name}</h3>
        <button
          onClick={onClose}
          className="text-mythos-terminal-text hover:text-mythos-terminal-error"
          aria-label="Close panel"
        >
          ×
        </button>
      </div>

      {isAdmin && <RoomAdminActions roomId={room.id} onEditRoom={onEditRoom} onCreateExit={onCreateExit} />}

      <div className="mb-2">
        <span className="text-xs text-mythos-terminal-text/70">ID:</span>
        <div className="text-sm text-mythos-terminal-text font-mono">{room.id}</div>
      </div>

      {room.description && (
        <div className="mb-4">
          <span className="text-xs text-mythos-terminal-text/70">Description:</span>
          <div className="text-sm text-mythos-terminal-text mt-1">{room.description}</div>
        </div>
      )}

      <RoomLocationFields room={room} />

      {room.occupants && room.occupants.length > 0 && (
        <div className="mb-4">
          <span className="text-xs text-mythos-terminal-text/70">
            Occupants ({room.occupant_count || room.occupants.length}):
          </span>
          <div className="text-sm text-mythos-terminal-text mt-1">{room.occupants.join(', ')}</div>
        </div>
      )}

      {room.exits && Object.keys(room.exits).length > 0 && <RoomExitsList exits={room.exits} />}
    </div>
  );
};
