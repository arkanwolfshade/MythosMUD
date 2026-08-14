/**
 * ASCII Minimap component.
 */

import React, { useCallback, useEffect, useRef, useState } from 'react';
import { fetchAsciiMinimap } from '../../api/maps';
import { SafeHtml } from '../common/SafeHtml';

export interface AsciiMinimapProps {
  plane: string;
  zone: string;
  subZone?: string;
  currentRoomId?: string;
  baseUrl?: string;
  authToken?: string;
  size?: number;
  position?: 'top-left' | 'top-right' | 'bottom-left' | 'bottom-right';
  onClick?: () => void;
  variant?: 'floating' | 'inline';
}

const POSITION_CLASSES = {
  'top-left': 'top-4 left-4',
  'top-right': 'top-4 right-4',
  'bottom-left': 'bottom-4 left-4',
  'bottom-right': 'bottom-4 right-4',
} as const;

function deriveEffectiveLocation(
  plane: string,
  zone: string,
  subZone: string | undefined,
  currentRoomId: string | undefined
): { effectivePlane: string; effectiveZone: string; effectiveSubZone: string | undefined } {
  const parts = currentRoomId ? currentRoomId.split('_') : [];
  return {
    effectivePlane: plane || parts[0] || '',
    effectiveZone: zone || (parts.length >= 2 ? parts[1] : ''),
    effectiveSubZone: subZone || (parts.length >= 3 ? parts[2] : undefined),
  };
}

function useAsciiMinimapData(params: {
  effectivePlane: string;
  effectiveZone: string;
  effectiveSubZone: string | undefined;
  currentRoomId: string | undefined;
  size: number;
  baseUrl: string;
  authToken: string | undefined;
}): { mapHtml: string; isLoading: boolean; error: string | null } {
  const { effectivePlane, effectiveZone, effectiveSubZone, currentRoomId, size, baseUrl, authToken } = params;
  const [mapHtml, setMapHtml] = useState('');
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

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
      setError(err instanceof Error ? err.message : 'Failed to fetch minimap');
      setMapHtml('');
    } finally {
      setIsLoading(false);
    }
  }, [baseUrl, effectivePlane, effectiveZone, effectiveSubZone, currentRoomId, size, authToken]);

  useEffect(() => {
    // Remote fetch; local mapHtml/isLoading/error are the natural sink for the result.
    // eslint-disable-next-line react-hooks/set-state-in-effect -- async minimap fetch updates local UI state
    void fetchMinimap();
  }, [fetchMinimap]);

  return { mapHtml, isLoading, error };
}

function MinimapNoLocation(props: { isInline: boolean; onClick?: () => void }): React.ReactElement | null {
  if (!props.isInline) return null;
  return (
    <button
      type="button"
      className="appearance-none w-full h-full min-h-20 flex items-center justify-center text-mythos-terminal-text/80 text-sm cursor-pointer border border-mythos-terminal-border rounded p-2 bg-transparent"
      onClick={props.onClick}
      title="Click to open full map"
    >
      No location — click to open map
    </button>
  );
}

interface MinimapDisplayProps {
  isInline: boolean;
  position: AsciiMinimapProps['position'];
  isLoading: boolean;
  error: string | null;
  mapHtml: string;
  onClick?: () => void;
  containerRef: React.RefObject<HTMLButtonElement | null>;
}

function MinimapDisplay(props: MinimapDisplayProps): React.ReactElement {
  const { isInline, position = 'bottom-right', isLoading, error, mapHtml, onClick, containerRef } = props;
  const className = isInline
    ? 'w-full h-full min-h-[80px] bg-mythos-terminal-background border border-mythos-terminal-border rounded p-2 ' +
      'cursor-pointer hover:border-mythos-terminal-primary transition-colors flex flex-col'
    : `fixed ${POSITION_CLASSES[position]} z-[9998] bg-mythos-terminal-background ` +
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
}

export const AsciiMinimap: React.FC<AsciiMinimapProps> = props => {
  const {
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
  } = props;
  const containerRef = useRef<HTMLButtonElement>(null);
  const location = deriveEffectiveLocation(plane, zone, subZone, currentRoomId);
  const { mapHtml, isLoading, error } = useAsciiMinimapData({
    ...location,
    currentRoomId,
    size,
    baseUrl,
    authToken,
  });
  const isInline = variant === 'inline';

  if (!currentRoomId) {
    return <MinimapNoLocation isInline={isInline} onClick={onClick} />;
  }

  return (
    <MinimapDisplay
      isInline={isInline}
      position={position}
      isLoading={isLoading}
      error={error}
      mapHtml={mapHtml}
      onClick={onClick}
      containerRef={containerRef}
    />
  );
};
