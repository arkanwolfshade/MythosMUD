/**
 * Map View component.
 *
 * A full-screen overlay that displays the room map viewer.
 * Can be closed via ESC key or a close button.
 *
 * As documented in the Pnakotic Manuscripts, proper visualization
 * of spatial relationships is essential for understanding our
 * eldritch architecture.
 */

import React, { useEffect } from 'react';
import { RoomMapViewer } from './map/RoomMapViewer';
import { getApiBaseUrl } from '../utils/config';

// Room type compatible with both gameStore and ui-v2 types
interface Room {
  id: string;
  name: string;
  description: string;
  plane?: string;
  zone?: string;
  sub_zone?: string;
  environment?: string;
  exits: Record<string, string>;
  occupants?: string[];
  occupant_count?: number;
  map_x?: number | null;
  map_y?: number | null;
}

export interface MapViewProps {
  /** Whether the map view is visible */
  isOpen: boolean;
  /** Callback when map should close */
  onClose: () => void;
  /** Current player's room data */
  currentRoom: Room | null;
  /** API base URL */
  baseUrl?: string;
  /** Auth token for authenticated requests */
  authToken?: string;
}

/**
 * Map View component.
 */
export const MapView: React.FC<MapViewProps> = ({ isOpen, onClose, currentRoom, baseUrl, authToken }) => {
  // Handle ESC key to close map
  useEffect(() => {
    if (!isOpen) return;

    const handleEscape = (event: KeyboardEvent) => {
      if (event.key === 'Escape') {
        onClose();
      }
    };

    window.addEventListener('keydown', handleEscape);
    return () => {
      window.removeEventListener('keydown', handleEscape);
    };
  }, [isOpen, onClose]);

  // Prevent body scroll when map is open
  useEffect(() => {
    if (isOpen) {
      document.body.style.overflow = 'hidden';
    } else {
      document.body.style.overflow = '';
    }
    return () => {
      document.body.style.overflow = '';
    };
  }, [isOpen]);

  if (!isOpen) return null;

  // Extract plane and zone from current room, or use defaults
  const plane = currentRoom?.plane || 'earth';
  const zone = currentRoom?.zone || 'arkhamcity';
  const subZone = currentRoom?.sub_zone;
  const currentRoomId = currentRoom?.id;

  return (
    <div className="fixed inset-0 bg-mythos-terminal-background z-50 flex flex-col">
      {/* Header with close button */}
      <div className="flex items-center justify-between p-4 border-b border-mythos-terminal-border bg-mythos-terminal-background">
        <h2 className="text-xl font-bold text-mythos-terminal-text">Map</h2>
        <button
          onClick={onClose}
          className="px-4 py-2 bg-mythos-terminal-error text-white rounded hover:bg-mythos-terminal-error/80 transition-colors"
          aria-label="Close map"
        >
          Close (ESC)
        </button>
      </div>

      {/* Map viewer */}
      <div className="flex-1 overflow-hidden">
        {currentRoom ? (
          <RoomMapViewer
            plane={plane}
            zone={zone}
            subZone={subZone}
            currentRoomId={currentRoomId}
            baseUrl={baseUrl || getApiBaseUrl()}
            authToken={authToken}
          />
        ) : (
          <div className="flex items-center justify-center h-full">
            <div className="text-mythos-terminal-text text-center">
              <p className="mb-4">Unable to load map: No room data available.</p>
              <p className="mb-4 text-sm text-mythos-terminal-text/70">You must be in a room to view the map.</p>
              <button
                onClick={onClose}
                className="px-4 py-2 bg-mythos-terminal-primary text-white rounded hover:bg-mythos-terminal-primary/80"
              >
                Close
              </button>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};
