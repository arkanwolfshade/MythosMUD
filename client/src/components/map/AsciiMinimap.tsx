/**
 * ASCII Minimap component.
 *
 * This component displays a small ASCII map showing the area around
 * the player's current location. It's always visible in a corner of the screen.
 *
 * As documented in the Pnakotic Manuscripts, a constant awareness of
 * one's spatial position is essential for navigating eldritch spaces.
 */

import React, { useCallback, useEffect, useState } from 'react';
import { getApiBaseUrl } from '../../utils/config';

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
}) => {
  const [mapHtml, setMapHtml] = useState<string>('');
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  // Fetch minimap from server
  const fetchMinimap = useCallback(async () => {
    if (!currentRoomId) {
      setMapHtml('');
      setIsLoading(false);
      return;
    }

    setIsLoading(true);
    setError(null);

    try {
      const url = new URL(`${baseUrl || getApiBaseUrl()}/api/maps/ascii/minimap`);
      url.searchParams.set('plane', plane);
      url.searchParams.set('zone', zone);
      if (subZone) {
        url.searchParams.set('sub_zone', subZone);
      }
      // Pass currentRoomId to server so it uses the most up-to-date value
      if (currentRoomId) {
        url.searchParams.set('current_room_id', currentRoomId);
      }
      url.searchParams.set('size', size.toString());

      const headers: HeadersInit = {
        'Content-Type': 'application/json',
      };
      if (authToken) {
        headers['Authorization'] = `Bearer ${authToken}`;
      }

      const response = await fetch(url.toString(), { headers });

      if (!response.ok) {
        throw new Error(`Failed to fetch minimap: ${response.statusText}`);
      }

      const data = await response.json();
      setMapHtml(data.map_html || '');
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to fetch minimap');
      setMapHtml('');
    } finally {
      setIsLoading(false);
    }
  }, [baseUrl, plane, zone, subZone, currentRoomId, size, authToken]);

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

  if (!currentRoomId) {
    return null;
  }

  const className =
    `absolute ${positionClasses[position]} z-50 bg-mythos-terminal-background ` +
    `border border-mythos-terminal-border rounded p-2 shadow-lg cursor-pointer ` +
    `hover:border-mythos-terminal-primary transition-colors`;

  return (
    <div
      className={className}
      onClick={onClick}
      title="Click to open full map"
      role="button"
      tabIndex={0}
      onKeyDown={e => {
        if (e.key === 'Enter' || e.key === ' ') {
          onClick?.();
        }
      }}
    >
      {isLoading && <div className="text-xs text-mythos-terminal-text p-2">Loading...</div>}
      {error && (
        <div className="text-xs text-mythos-terminal-error p-2" title={error}>
          Map Error
        </div>
      )}
      {!isLoading && !error && mapHtml && (
        <div className="minimap-container" dangerouslySetInnerHTML={{ __html: mapHtml }} />
      )}
    </div>
  );
};
