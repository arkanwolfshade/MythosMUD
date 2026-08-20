/**
 * Map View component.
 *
 * A full-screen overlay that displays the room map viewer.
 * Can be closed via ESC key or a close button.
 */

import React, { useEffect } from 'react';
import { Z_INDEX_OVERLAY_TOP } from '../constants/layout';
import { getVersionedApiBaseUrl } from '../utils/config';
import { seedFrom } from '../utils/directionHallucination';
import { AsciiMapViewer } from './map/AsciiMapViewer';

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
  isOpen: boolean;
  onClose: () => void;
  currentRoom: Room | null;
  baseUrl?: string;
  authToken?: string;
  hideHeader?: boolean;
  /** #626: when true, the map viewer shows churning ASCII noise instead of the real map. */
  hallucinate?: boolean;
  /** Player id used, with the room id, to seed the noise. */
  playerId?: string;
}

function useMapViewEffects(isOpen: boolean, onClose: () => void) {
  useEffect(() => {
    if (!isOpen) return;
    const handleEscape = (event: KeyboardEvent) => {
      if (event.key === 'Escape') onClose();
    };
    window.addEventListener('keydown', handleEscape);
    return () => window.removeEventListener('keydown', handleEscape);
  }, [isOpen, onClose]);

  useEffect(() => {
    document.body.style.overflow = isOpen ? 'hidden' : '';
    return () => {
      document.body.style.overflow = '';
    };
  }, [isOpen]);
}

function MapViewHeader({ onClose }: { onClose: () => void }) {
  return (
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
  );
}

function MapViewBody({ currentRoom, baseUrl, authToken, hideHeader, onClose, hallucinate, playerId }: MapViewProps) {
  const plane = currentRoom?.plane || 'earth';
  const zone = currentRoom?.zone || 'arkhamcity';
  const opaqueStyle = hideHeader
    ? { backgroundColor: 'var(--color-mythos-terminal-background, #0a0a0a)', opacity: 1 }
    : {
        backgroundColor: 'var(--color-mythos-terminal-background, #0a0a0a)',
        opacity: 1,
        zIndex: Z_INDEX_OVERLAY_TOP,
      };

  return (
    <div
      className={`${hideHeader ? 'h-full w-full' : 'fixed inset-0'} bg-mythos-terminal-background flex flex-col`}
      style={opaqueStyle}
    >
      {!hideHeader && <MapViewHeader onClose={onClose} />}
      <div
        className="flex-1 overflow-hidden min-h-0"
        style={{ backgroundColor: 'var(--color-mythos-terminal-background, #0a0a0a)' }}
      >
        {currentRoom ? (
          <AsciiMapViewer
            plane={plane}
            zone={zone}
            subZone={currentRoom.sub_zone}
            currentRoomId={currentRoom.id}
            baseUrl={baseUrl || getVersionedApiBaseUrl()}
            authToken={authToken}
            hallucinate={Boolean(hallucinate && playerId)}
            seed={playerId ? seedFrom(currentRoom.id, playerId) : 0}
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
}

export const MapView: React.FC<MapViewProps> = props => {
  useMapViewEffects(props.isOpen, props.onClose);
  if (!props.isOpen) return null;
  return <MapViewBody {...props} />;
};
