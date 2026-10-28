/**
 * ASCII Map Viewer component.
 *
 * This component displays server-rendered ASCII maps for players.
 * It fetches HTML from the server and displays it in a fixed viewport.
 *
 * As documented in the Pnakotic Manuscripts, proper spatial visualization
 * is essential for navigating the eldritch architecture of our world.
 */

import React, { useCallback, useEffect } from 'react';

import { AsciiMapViewerContent, AsciiMapViewerError, AsciiMapViewerLoading } from './AsciiMapViewerViews';
import { createViewportKeyHandler } from './asciiMapViewerUtils';
import type { UseAsciiMapResult } from './useAsciiMap';
import { useAsciiMap } from './useAsciiMap';

/** Encapsulates map state + key listener + click handler so AsciiMapViewer stays under complexity limit. */
function useAsciiMapViewerBindings(props: AsciiMapViewerProps): {
  state: UseAsciiMapResult;
  handleMapClick: (e: React.MouseEvent<HTMLDivElement>) => void;
} {
  const {
    plane,
    zone,
    subZone,
    currentRoomId,
    baseUrl = '',
    authToken,
    onRoomSelect,
    viewportWidth = 80,
    viewportHeight = 24,
  } = props;
  const state = useAsciiMap({
    plane,
    zone,
    subZone,
    currentRoomId,
    viewportWidth,
    viewportHeight,
    baseUrl,
    authToken,
  });
  useEffect(() => {
    const handleKeyDown = createViewportKeyHandler(state.setViewportX, state.setViewportY);
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [state.setViewportX, state.setViewportY]);
  const handleMapClick = useCallback(
    (e: React.MouseEvent<HTMLDivElement>) => getMapClickHandler(onRoomSelect)(e),
    [onRoomSelect]
  );
  return { state, handleMapClick };
}

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

function getMapClickHandler(
  onRoomSelect: AsciiMapViewerProps['onRoomSelect']
): (event: React.MouseEvent<HTMLDivElement>) => void {
  return (event: React.MouseEvent<HTMLDivElement>) => {
    const roomId = (event.target as HTMLElement).getAttribute('data-room-id');
    if (roomId && onRoomSelect) onRoomSelect(roomId);
  };
}

function chooseMapView(
  state: UseAsciiMapResult,
  plane: string,
  zone: string,
  onMapClick: (event: React.MouseEvent<HTMLDivElement>) => void
): React.ReactElement {
  if (state.isLoading) return <AsciiMapViewerLoading />;
  if (state.error) return <AsciiMapViewerError error={state.error} onRetry={() => state.fetchMap()} />;
  return (
    <AsciiMapViewerContent
      plane={plane}
      zone={zone}
      mapHtml={state.mapHtml}
      viewport={state.viewport}
      setViewportX={state.setViewportX}
      setViewportY={state.setViewportY}
      selectedPlane={state.selectedPlane}
      selectedZone={state.selectedZone}
      selectedSubZone={state.selectedSubZone}
      setSelectedPlane={state.setSelectedPlane}
      setSelectedZone={state.setSelectedZone}
      setSelectedSubZone={state.setSelectedSubZone}
      onMapClick={onMapClick}
    />
  );
}

/**
 * ASCII Map Viewer component.
 * All logic lives in useAsciiMapViewerBindings and chooseMapView to keep this function under complexity limit.
 */
export function AsciiMapViewer(props: AsciiMapViewerProps): React.ReactElement {
  const { state, handleMapClick } = useAsciiMapViewerBindings(props);
  return chooseMapView(state, props.plane, props.zone, handleMapClick);
}
