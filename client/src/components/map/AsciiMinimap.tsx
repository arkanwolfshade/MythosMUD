/**
 * ASCII Minimap component.
 *
 * This component displays a small ASCII map showing the area around
 * the player's current location. It's always visible in a corner of the screen.
 *
 * As documented in the Pnakotic Manuscripts, a constant awareness of
 * one's spatial position is essential for navigating eldritch spaces.
 */

import React, { useCallback, useEffect, useRef, useState } from 'react';

import { fetchAsciiMinimap } from '../../api/maps';
import { SafeHtml } from '../common/SafeHtml';

export interface AsciiMinimapProps {
  /** Plane name (required) */
  plane: string;
  /** Zone name (required) */
  zone: string;
  /** Optional sub-zone name */
  subZone?: string;
  /** Current player's room ID */
  currentRoomId?: string;
  /** API base URL */
  baseUrl?: string;
  /** Auth token for authenticated requests */
  authToken?: string;
  /** Minimap size (3x3 or 5x5 area around player, default 5) */
  size?: number;
  /** Position on screen: 'top-left' | 'top-right' | 'bottom-left' | 'bottom-right' */
  position?: 'top-left' | 'top-right' | 'bottom-left' | 'bottom-right';
  /** Callback when minimap is clicked (opens full map) */
  onClick?: () => void;
  /** When 'inline', fit inside a container (e.g. panel); when 'floating', use fixed position in corner */
  variant?: 'floating' | 'inline';
}

/**
 * ASCII Minimap component.
 */
export const AsciiMinimap: React.FC<AsciiMinimapProps> = ({
  plane,
  zone,
  subZone,
  currentRoomId,
  baseUrl = '',
  authToken,
  size = 5,
  position = 'bottom-right',
  onClick,
  variant = 'floating',
}) => {
  const [mapHtml, setMapHtml] = useState<string>('');
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const containerRef = useRef<HTMLButtonElement>(null);

  // Fallback when plane/zone/subZone props are missing (e.g. after zone change before room_state
  // has full fields). Contract: server room.id (stable_id) format is plane_zone_subzone_... ; we
  // derive the first segments so the minimap can still request the correct zone. Prefer server-
  // provided plane/zone/sub_zone when available (room_state always includes them per server schema).
  const parts = currentRoomId ? currentRoomId.split('_') : [];
  const effectivePlane = plane || parts[0] || '';
  const effectiveZone = zone || (parts.length >= 2 ? parts[1] : '');
  const effectiveSubZone = subZone || (parts.length >= 3 ? parts[2] : undefined);

  // Fetch minimap from server via shared map API layer
  const fetchMinimap = useCallback(async () => {
    if (!currentRoomId) {
      setMapHtml('');
      setIsLoading(false);
      return;
    }

    setIsLoading(true);
    setError(null);

    try {
      const raw = await fetchAsciiMinimap({
        plane: effectivePlane,
        zone: effectiveZone,
        subZone: effectiveSubZone,
        currentRoomId,
        size,
        baseUrl,
        authToken,
      });
      setMapHtml(raw.map_html ?? '');
    } catch (err) {
      const errMsg = err instanceof Error ? err.message : 'Failed to fetch minimap';
      setError(errMsg);
      setMapHtml('');
    } finally {
      setIsLoading(false);
    }
  }, [baseUrl, effectivePlane, effectiveZone, effectiveSubZone, currentRoomId, size, authToken]);

  // Fetch minimap when dependencies change
  useEffect(() => {
    void fetchMinimap();
  }, [fetchMinimap]);

  // Position classes
  const positionClasses = {
    'top-left': 'top-4 left-4',
    'top-right': 'top-4 right-4',
    'bottom-left': 'bottom-4 left-4',
    'bottom-right': 'bottom-4 right-4',
  };

  const isInline = variant === 'inline';
  if (!currentRoomId) {
    if (isInline) {
      return (
        <button
          type="button"
          className="appearance-none w-full h-full min-h-[80px] flex items-center justify-center text-mythos-terminal-text/80 text-sm cursor-pointer border border-mythos-terminal-border rounded p-2 bg-transparent"
          onClick={onClick}
          title="Click to open full map"
        >
          No location — click to open map
        </button>
      );
    }
    return null;
  }
  const className = isInline
    ? 'w-full h-full min-h-[80px] bg-mythos-terminal-background border border-mythos-terminal-border rounded p-2 ' +
      'cursor-pointer hover:border-mythos-terminal-primary transition-colors flex flex-col'
    : `fixed ${positionClasses[position]} z-[9998] bg-mythos-terminal-background ` +
      `border border-mythos-terminal-border rounded p-2 shadow-lg cursor-pointer ` +
      `hover:border-mythos-terminal-primary transition-colors`;

  return (
    <button
      type="button"
      ref={containerRef}
      className={`appearance-none text-left ${className}`}
      onClick={onClick}
      title="Click to open full map"
    >
      {isLoading && <div className="text-xs text-mythos-terminal-text p-2">Loading...</div>}
      {error && (
        <div className="text-xs text-mythos-terminal-error p-2" title={error}>
          Map Error
        </div>
      )}
      {!isLoading && !error && mapHtml && (
        <SafeHtml
          html={mapHtml}
          className={
            isInline
              ? 'minimap-container flex-1 min-h-0 overflow-auto flex justify-center items-center text-mythos-terminal-text font-mono text-xs whitespace-pre'
              : 'minimap-container'
          }
          tag="div"
        />
      )}
    </button>
  );
};
