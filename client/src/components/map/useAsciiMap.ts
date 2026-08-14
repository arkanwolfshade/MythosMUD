/**
 * Hook for ASCII map data and viewport state.
 */

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

export { useAsciiMapState as useAsciiMap } from './useAsciiMapState';
