/**
 * Hook for ASCII map data and viewport state.
 *
 * Encapsulates fetch logic and viewport state so AsciiMapViewer can focus on
 * presentation. Improves testability (mock hook) and separation of concerns.
 */

import { useCallback, useEffect, useState } from 'react';

import { fetchAsciiMap } from '../../api/maps';

function getMapErrorMessage(err: unknown): string {
  return err instanceof Error ? err.message : 'Failed to fetch map';
}

function applyViewportFromRaw(
  raw: { viewport?: { x?: number; y?: number } },
  currentX: number,
  currentY: number,
  setViewportX: (x: number | ((prev: number) => number)) => void,
  setViewportY: (y: number | ((prev: number) => number)) => void
): void {
  if (!raw.viewport) return;
  const serverX = raw.viewport.x ?? 0;
  const serverY = raw.viewport.y ?? 0;
  if (serverX !== currentX || serverY !== currentY) {
    setViewportX(serverX);
    setViewportY(serverY);
  }
}

interface FetchMapParams {
  selectedPlane: string;
  selectedZone: string;
  selectedSubZone: string | undefined;
  currentRoomId: string | undefined;
  viewportX: number;
  viewportY: number;
  viewportWidth: number;
  viewportHeight: number;
  baseUrl: string;
  authToken: string | undefined;
  setMapHtml: (v: string) => void;
  setError: (v: string | null) => void;
  setIsLoading: (v: boolean) => void;
  setViewportX: (x: number | ((prev: number) => number)) => void;
  setViewportY: (y: number | ((prev: number) => number)) => void;
}

async function runFetchMap(params: FetchMapParams): Promise<void> {
  const { setMapHtml, setError, setIsLoading, setViewportX, setViewportY } = params;
  setIsLoading(true);
  setError(null);
  try {
    const raw = await fetchAsciiMap({
      plane: params.selectedPlane,
      zone: params.selectedZone,
      subZone: params.selectedSubZone,
      currentRoomId: params.currentRoomId,
      viewportX: params.viewportX,
      viewportY: params.viewportY,
      viewportWidth: params.viewportWidth,
      viewportHeight: params.viewportHeight,
      baseUrl: params.baseUrl,
      authToken: params.authToken,
    });
    setMapHtml(raw.map_html ?? '');
    applyViewportFromRaw(raw, params.viewportX, params.viewportY, setViewportX, setViewportY);
  } catch (err) {
    setError(getMapErrorMessage(err));
    setMapHtml('');
  } finally {
    setIsLoading(false);
  }
}

export interface UseAsciiMapParams {
  plane: string;
  zone: string;
  subZone?: string;
  currentRoomId?: string;
  viewportWidth?: number;
  viewportHeight?: number;
  baseUrl?: string;
  authToken?: string;
}

export interface UseAsciiMapResult {
  mapHtml: string;
  viewport: { x: number; y: number };
  setViewportX: React.Dispatch<React.SetStateAction<number>>;
  setViewportY: React.Dispatch<React.SetStateAction<number>>;
  isLoading: boolean;
  error: string | null;
  fetchMap: () => Promise<void>;
  selectedPlane: string;
  selectedZone: string;
  selectedSubZone: string | undefined;
  setSelectedPlane: React.Dispatch<React.SetStateAction<string>>;
  setSelectedZone: React.Dispatch<React.SetStateAction<string>>;
  setSelectedSubZone: React.Dispatch<React.SetStateAction<string | undefined>>;
}

export function useAsciiMap({
  plane,
  zone,
  subZone,
  currentRoomId,
  viewportWidth = 80,
  viewportHeight = 24,
  baseUrl = '',
  authToken,
}: UseAsciiMapParams): UseAsciiMapResult {
  const [mapHtml, setMapHtml] = useState<string>('');
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [viewportX, setViewportX] = useState(0);
  const [viewportY, setViewportY] = useState(0);
  const [selectedPlane, setSelectedPlane] = useState(plane);
  const [selectedZone, setSelectedZone] = useState(zone);
  const [selectedSubZone, setSelectedSubZone] = useState<string | undefined>(subZone);

  // Sync selected plane/zone/subZone and viewport from props when they change.
  // Defer setState so it is not synchronous in the effect (avoids cascading renders).
  useEffect(() => {
    queueMicrotask(() => {
      setSelectedPlane(plane);
      setSelectedZone(zone);
      setSelectedSubZone(subZone);
      setViewportX(0);
      setViewportY(0);
    });
  }, [plane, zone, subZone]);

  // Reset viewport when current room changes.
  useEffect(() => {
    if (!currentRoomId) return;
    queueMicrotask(() => {
      setViewportX(0);
      setViewportY(0);
    });
  }, [currentRoomId]);

  const fetchMap = useCallback(
    () =>
      runFetchMap({
        selectedPlane,
        selectedZone,
        selectedSubZone,
        currentRoomId,
        viewportX,
        viewportY,
        viewportWidth,
        viewportHeight,
        baseUrl,
        authToken,
        setMapHtml,
        setError,
        setIsLoading,
        setViewportX,
        setViewportY,
      }),
    [
      baseUrl,
      selectedPlane,
      selectedZone,
      selectedSubZone,
      viewportX,
      viewportY,
      viewportWidth,
      viewportHeight,
      authToken,
      currentRoomId,
    ]
  );

  useEffect(() => {
    void fetchMap();
  }, [fetchMap]);

  return {
    mapHtml,
    viewport: { x: viewportX, y: viewportY },
    setViewportX,
    setViewportY,
    isLoading,
    error,
    fetchMap,
    selectedPlane,
    selectedZone,
    selectedSubZone,
    setSelectedPlane,
    setSelectedZone,
    setSelectedSubZone,
  };
}
