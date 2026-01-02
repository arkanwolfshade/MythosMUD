/**
 * ASCII Map Viewer component.
 *
 * This component displays server-rendered ASCII maps for players.
 * It fetches HTML from the server and displays it in a fixed viewport.
 *
 * As documented in the Pnakotic Manuscripts, proper spatial visualization
 * is essential for navigating the eldritch architecture of our world.
 */

import React, { useCallback, useEffect, useState } from 'react';
import { getApiBaseUrl } from '../../utils/config';
import { MapControls } from './MapControls';

export interface AsciiMapViewerProps {
  /** Plane name (required) */
  plane: string;
  /** Zone name (required) */
  zone: string;
  /** Optional sub-zone name for filtering */
  subZone?: string;
  /** Current player's room ID for highlighting */
  currentRoomId?: string;
  /** API base URL */
  baseUrl?: string;
  /** Auth token for authenticated requests */
  authToken?: string;
  /** Callback when room is selected */
  onRoomSelect?: (roomId: string) => void;
  /** Viewport width in characters (default 80) */
  viewportWidth?: number;
  /** Viewport height in lines (default 24) */
  viewportHeight?: number;
}

/**
 * ASCII Map Viewer component.
 */
export const AsciiMapViewer: React.FC<AsciiMapViewerProps> = ({
  plane,
  zone,
  subZone,
  currentRoomId,
  baseUrl = '',
  authToken,
  onRoomSelect,
  viewportWidth = 80,
  viewportHeight = 24,
}) => {
  const [mapHtml, setMapHtml] = useState<string>('');
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [viewportX, setViewportX] = useState(0);
  const [viewportY, setViewportY] = useState(0);
  const [selectedPlane, setSelectedPlane] = useState(plane);
  const [selectedZone, setSelectedZone] = useState(zone);
  const [selectedSubZone, setSelectedSubZone] = useState<string | undefined>(subZone);

  // Update selected plane/zone/subZone when props change (player moved to different zone)
  useEffect(() => {
    setSelectedPlane(plane);
    setSelectedZone(zone);
    setSelectedSubZone(subZone);
    // Reset viewport when zone changes
    setViewportX(0);
    setViewportY(0);
  }, [plane, zone, subZone]);

  // Reset viewport when room changes (player moved) to trigger server-side auto-centering
  // The server always auto-centers on the player's current room when current_room_id is provided
  useEffect(() => {
    if (currentRoomId) {
      // Reset viewport - server will auto-center on player's new room
      // We'll sync the actual viewport from the server response
      setViewportX(0);
      setViewportY(0);
    }
  }, [currentRoomId]);

  // Fetch ASCII map from server
  const fetchMap = useCallback(async () => {
    setIsLoading(true);
    setError(null);

    try {
      const url = new URL(`${baseUrl || getApiBaseUrl()}/api/maps/ascii`);
      url.searchParams.set('plane', selectedPlane);
      url.searchParams.set('zone', selectedZone);
      if (selectedSubZone) {
        url.searchParams.set('sub_zone', selectedSubZone);
      }
      // Pass currentRoomId to server so it uses the most up-to-date value
      if (currentRoomId) {
        url.searchParams.set('current_room_id', currentRoomId);
      }
      url.searchParams.set('viewport_x', viewportX.toString());
      url.searchParams.set('viewport_y', viewportY.toString());
      url.searchParams.set('viewport_width', viewportWidth.toString());
      url.searchParams.set('viewport_height', viewportHeight.toString());

      const headers: HeadersInit = {
        'Content-Type': 'application/json',
      };
      if (authToken) {
        headers['Authorization'] = `Bearer ${authToken}`;
      }

      const response = await fetch(url.toString(), { headers });

      if (!response.ok) {
        throw new Error(`Failed to fetch map: ${response.statusText}`);
      }

      const data = await response.json();
      setMapHtml(data.map_html || '');

      // Sync viewport with server response (server auto-centers on player's room)
      // Only update if different to avoid unnecessary re-renders
      if (data.viewport) {
        const serverX = data.viewport.x || 0;
        const serverY = data.viewport.y || 0;
        // Update viewport if server changed it (auto-centering)
        if (serverX !== viewportX || serverY !== viewportY) {
          setViewportX(serverX);
          setViewportY(serverY);
        }
      }
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to fetch map');
      setMapHtml('');
    } finally {
      setIsLoading(false);
    }
  }, [
    baseUrl,
    selectedPlane,
    selectedZone,
    selectedSubZone,
    viewportX,
    viewportY,
    viewportWidth,
    viewportHeight,
    authToken,
    currentRoomId, // Refresh map when player moves to a new room
  ]);

  // Fetch map when dependencies change
  useEffect(() => {
    void fetchMap();
  }, [fetchMap]);

  // Handle keyboard navigation
  useEffect(() => {
    const handleKeyDown = (event: KeyboardEvent) => {
      if (event.target instanceof HTMLInputElement || event.target instanceof HTMLTextAreaElement) {
        return; // Don't handle if typing in input
      }

      switch (event.key) {
        case 'ArrowUp':
          event.preventDefault();
          setViewportY(prev => prev - 1);
          break;
        case 'ArrowDown':
          event.preventDefault();
          setViewportY(prev => prev + 1);
          break;
        case 'ArrowLeft':
          event.preventDefault();
          setViewportX(prev => prev - 1);
          break;
        case 'ArrowRight':
          event.preventDefault();
          setViewportX(prev => prev + 1);
          break;
        case 'Home':
          event.preventDefault();
          setViewportX(0);
          setViewportY(0);
          break;
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => {
      window.removeEventListener('keydown', handleKeyDown);
    };
  }, []);

  // Handle map cell click (for room selection)
  const handleMapClick = useCallback(
    (event: React.MouseEvent<HTMLDivElement>) => {
      // Extract room info from clicked element if available
      const target = event.target as HTMLElement;
      const roomId = target.getAttribute('data-room-id');
      if (roomId && onRoomSelect) {
        onRoomSelect(roomId);
      }
    },
    [onRoomSelect]
  );

  // Loading state
  if (isLoading) {
    return (
      <div className="flex items-center justify-center h-full w-full bg-mythos-terminal-background">
        <div className="text-mythos-terminal-text">Loading map...</div>
      </div>
    );
  }

  // Error state
  if (error) {
    return (
      <div className="flex flex-col items-center justify-center h-full w-full bg-mythos-terminal-background p-4">
        <div className="text-mythos-terminal-error mb-4">Error: {error}</div>
        <button
          onClick={() => fetchMap()}
          className="px-4 py-2 bg-mythos-terminal-primary text-white rounded hover:bg-mythos-terminal-primary/80"
        >
          Retry
        </button>
      </div>
    );
  }

  return (
    <div className="relative h-full w-full bg-mythos-terminal-background">
      {/* Map controls */}
      <div className="absolute top-4 left-4 z-10">
        <MapControls
          searchQuery=""
          onSearchChange={() => {}}
          plane={selectedPlane}
          zone={selectedZone}
          subZone={selectedSubZone}
          onPlaneChange={setSelectedPlane}
          onZoneChange={setSelectedZone}
          onSubZoneChange={setSelectedSubZone}
          availablePlanes={[plane]}
          availableZones={[zone]}
          availableSubZones={[]}
        />
      </div>

      {/* Viewport controls */}
      <div className="absolute top-4 right-4 z-10 flex gap-2">
        <button
          onClick={() => {
            setViewportX(prev => prev - 1);
          }}
          className="px-2 py-1 bg-mythos-terminal-background border border-mythos-terminal-border text-mythos-terminal-text rounded hover:bg-mythos-terminal-border"
          title="Scroll left"
        >
          ←
        </button>
        <button
          onClick={() => {
            setViewportX(prev => prev + 1);
          }}
          className="px-2 py-1 bg-mythos-terminal-background border border-mythos-terminal-border text-mythos-terminal-text rounded hover:bg-mythos-terminal-border"
          title="Scroll right"
        >
          →
        </button>
        <button
          onClick={() => {
            setViewportY(prev => prev - 1);
          }}
          className="px-2 py-1 bg-mythos-terminal-background border border-mythos-terminal-border text-mythos-terminal-text rounded hover:bg-mythos-terminal-border"
          title="Scroll up"
        >
          ↑
        </button>
        <button
          onClick={() => {
            setViewportY(prev => prev + 1);
          }}
          className="px-2 py-1 bg-mythos-terminal-background border border-mythos-terminal-border text-mythos-terminal-text rounded hover:bg-mythos-terminal-border"
          title="Scroll down"
        >
          ↓
        </button>
        <button
          onClick={() => {
            setViewportX(0);
            setViewportY(0);
          }}
          className="px-2 py-1 bg-mythos-terminal-background border border-mythos-terminal-border text-mythos-terminal-text rounded hover:bg-mythos-terminal-border"
          title="Reset viewport"
        >
          ⌂
        </button>
      </div>

      {/* ASCII map display */}
      <div
        className="flex items-center justify-center h-full w-full overflow-auto"
        onClick={handleMapClick}
        dangerouslySetInnerHTML={{ __html: mapHtml }}
      />

      {/* Viewport info */}
      <div className="absolute bottom-4 left-4 z-10 text-xs text-mythos-terminal-text bg-mythos-terminal-background/80 px-2 py-1 rounded">
        Viewport: ({viewportX}, {viewportY}) | Use arrow keys to scroll
      </div>
    </div>
  );
};
