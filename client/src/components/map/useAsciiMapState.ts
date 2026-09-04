import { useCallback, useEffect, useState, type Dispatch, type SetStateAction } from 'react';
import { fetchAsciiMap } from '../../api/maps';
import type { UseAsciiMapParams, UseAsciiMapResult } from './useAsciiMap';

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

interface SyncSelectionParams {
  plane: string;
  zone: string;
  subZone: string | undefined;
  setSelectedPlane: Dispatch<SetStateAction<string>>;
  setSelectedZone: Dispatch<SetStateAction<string>>;
  setSelectedSubZone: Dispatch<SetStateAction<string | undefined>>;
  setViewportX: Dispatch<SetStateAction<number>>;
  setViewportY: Dispatch<SetStateAction<number>>;
}

function syncSelectionFromProps(params: SyncSelectionParams): void {
  queueMicrotask(() => {
    params.setSelectedPlane(params.plane);
    params.setSelectedZone(params.zone);
    params.setSelectedSubZone(params.subZone);
    params.setViewportX(0);
    params.setViewportY(0);
  });
}

function resetViewportForRoom(
  currentRoomId: string | undefined,
  setViewportX: Dispatch<SetStateAction<number>>,
  setViewportY: Dispatch<SetStateAction<number>>
): void {
  if (!currentRoomId) return;
  queueMicrotask(() => {
    setViewportX(0);
    setViewportY(0);
  });
}

type AsciiMapFields = ReturnType<typeof useAsciiMapFields>;

function useAsciiMapFields(params: UseAsciiMapParams) {
  const { plane, zone, subZone, viewportWidth = 80, viewportHeight = 24, baseUrl = '', authToken } = params;
  const [mapHtml, setMapHtml] = useState('');
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [viewportX, setViewportX] = useState(0);
  const [viewportY, setViewportY] = useState(0);
  const [selectedPlane, setSelectedPlane] = useState(plane);
  const [selectedZone, setSelectedZone] = useState(zone);
  const [selectedSubZone, setSelectedSubZone] = useState<string | undefined>(subZone);
  return {
    plane,
    zone,
    subZone,
    currentRoomId: params.currentRoomId,
    viewportWidth,
    viewportHeight,
    baseUrl,
    authToken,
    mapHtml,
    setMapHtml,
    isLoading,
    setIsLoading,
    error,
    setError,
    viewportX,
    setViewportX,
    viewportY,
    setViewportY,
    selectedPlane,
    setSelectedPlane,
    selectedZone,
    setSelectedZone,
    selectedSubZone,
    setSelectedSubZone,
  };
}

function useAsciiMapPropEffects(f: AsciiMapFields): void {
  useEffect(() => {
    syncSelectionFromProps({
      plane: f.plane,
      zone: f.zone,
      subZone: f.subZone,
      setSelectedPlane: f.setSelectedPlane,
      setSelectedZone: f.setSelectedZone,
      setSelectedSubZone: f.setSelectedSubZone,
      setViewportX: f.setViewportX,
      setViewportY: f.setViewportY,
    });
  }, [
    f.plane,
    f.zone,
    f.subZone,
    f.setSelectedPlane,
    f.setSelectedZone,
    f.setSelectedSubZone,
    f.setViewportX,
    f.setViewportY,
  ]);

  useEffect(() => {
    resetViewportForRoom(f.currentRoomId, f.setViewportX, f.setViewportY);
  }, [f.currentRoomId, f.setViewportX, f.setViewportY]);
}

function useAsciiMapFetchCb(f: AsciiMapFields): () => Promise<void> {
  return useCallback(
    () =>
      runFetchMap({
        selectedPlane: f.selectedPlane,
        selectedZone: f.selectedZone,
        selectedSubZone: f.selectedSubZone,
        currentRoomId: f.currentRoomId,
        viewportX: f.viewportX,
        viewportY: f.viewportY,
        viewportWidth: f.viewportWidth,
        viewportHeight: f.viewportHeight,
        baseUrl: f.baseUrl,
        authToken: f.authToken,
        setMapHtml: f.setMapHtml,
        setError: f.setError,
        setIsLoading: f.setIsLoading,
        setViewportX: f.setViewportX,
        setViewportY: f.setViewportY,
      }),
    [
      f.baseUrl,
      f.selectedPlane,
      f.selectedZone,
      f.selectedSubZone,
      f.viewportX,
      f.viewportY,
      f.viewportWidth,
      f.viewportHeight,
      f.authToken,
      f.currentRoomId,
      f.setMapHtml,
      f.setError,
      f.setIsLoading,
      f.setViewportX,
      f.setViewportY,
    ]
  );
}

function toAsciiMapResult(f: AsciiMapFields, fetchMap: () => Promise<void>): UseAsciiMapResult {
  return {
    mapHtml: f.mapHtml,
    viewport: { x: f.viewportX, y: f.viewportY },
    setViewportX: f.setViewportX,
    setViewportY: f.setViewportY,
    isLoading: f.isLoading,
    error: f.error,
    fetchMap,
    selectedPlane: f.selectedPlane,
    selectedZone: f.selectedZone,
    selectedSubZone: f.selectedSubZone,
    setSelectedPlane: f.setSelectedPlane,
    setSelectedZone: f.setSelectedZone,
    setSelectedSubZone: f.setSelectedSubZone,
  };
}

export function useAsciiMapState(params: UseAsciiMapParams): UseAsciiMapResult {
  const f = useAsciiMapFields(params);
  useAsciiMapPropEffects(f);
  const fetchMap = useAsciiMapFetchCb(f);
  useEffect(() => {
    void fetchMap();
  }, [fetchMap]);
  return toAsciiMapResult(f, fetchMap);
}
