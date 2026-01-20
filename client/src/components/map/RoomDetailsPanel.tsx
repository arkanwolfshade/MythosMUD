/**
 * Room Details Panel component.
 *
 * Displays detailed information about a selected room, including
 * name, ID, description, zone, subzone, plane, environment, occupants, and exits.
 *
 * As documented in the Pnakotic Manuscripts, proper documentation of
 * spatial entities is essential for understanding our eldritch architecture.
 */

import React from 'react';
import type { Room } from '../../stores/gameStore';

export interface RoomDetailsPanelProps {
  /** Room data to display */
  room: Room;
  /** Callback when panel is closed */
  onClose: () => void;
  /** Callback when edit room button is clicked (admin only) */
  onEditRoom?: (roomId: string) => void;
  /** Callback when create exit button is clicked (admin only) */
  onCreateExit?: () => void;
  /** Whether user is admin (shows edit button) */
  isAdmin?: boolean;
}

/**
 * Room Details Panel component.
 */
export const RoomDetailsPanel: React.FC<RoomDetailsPanelProps> = ({
  room,
  onClose,
  onEditRoom,
  onCreateExit,
  isAdmin = false,
}) => {
  return (
    <div className="absolute top-4 right-4 w-80 bg-mythos-terminal-background border border-mythos-terminal-border rounded shadow-lg p-4 z-20 max-h-panel overflow-y-auto">
      {/* Header */}
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

      {/* Admin buttons */}
      {isAdmin && (
        <div className="mb-4 space-y-2">
          {onEditRoom && (
            <button
              onClick={() => onEditRoom(room.id)}
              className="w-full px-3 py-2 bg-mythos-terminal-primary text-white rounded hover:bg-mythos-terminal-primary/80 text-sm"
            >
              Edit Room
            </button>
          )}
          {onCreateExit && (
            <button
              onClick={onCreateExit}
              className="w-full px-3 py-2 bg-mythos-terminal-success text-white rounded hover:bg-mythos-terminal-success/80 text-sm"
            >
              Create Exit
            </button>
          )}
        </div>
      )}

      {/* Room ID */}
      <div className="mb-2">
        <span className="text-xs text-mythos-terminal-text/70">ID:</span>
        <div className="text-sm text-mythos-terminal-text font-mono">{room.id}</div>
      </div>

      {/* Description */}
      {room.description && (
        <div className="mb-4">
          <span className="text-xs text-mythos-terminal-text/70">Description:</span>
          <div className="text-sm text-mythos-terminal-text mt-1">{room.description}</div>
        </div>
      )}

      {/* Location info */}
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

      {/* Occupants */}
      {room.occupants && room.occupants.length > 0 && (
        <div className="mb-4">
          <span className="text-xs text-mythos-terminal-text/70">
            Occupants ({room.occupant_count || room.occupants.length}):
          </span>
          <div className="text-sm text-mythos-terminal-text mt-1">{room.occupants.join(', ')}</div>
        </div>
      )}

      {/* Exits */}
      {room.exits && Object.keys(room.exits).length > 0 && (
        <div>
          <span className="text-xs text-mythos-terminal-text/70">Exits:</span>
          <div className="text-sm text-mythos-terminal-text mt-1 space-y-1">
            {Object.entries(room.exits).map(([direction, target]) => (
              <div key={direction} className="flex justify-between">
                <span>{direction}:</span>
                <span className="font-mono text-mythos-terminal-primary">{target}</span>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
};
