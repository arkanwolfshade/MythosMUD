/**
 * Presentational views for AsciiMapViewer (loading, error, main content).
 * Extracted to keep AsciiMapViewer.tsx under complexity and line-count limits.
 * Exports only components so fast refresh works.
 */

import React from 'react';

import { SafeHtml } from '../common/SafeHtml';
import { VIEWPORT_BUTTON_CLASS } from './asciiMapViewerUtils';
import { MapControls } from './MapControls';

export function AsciiMapViewerLoading(): React.ReactElement {
  return (
    <div className="flex items-center justify-center h-full w-full bg-mythos-terminal-background">
      <div className="text-mythos-terminal-text">Loading map...</div>
    </div>
  );
}

export function AsciiMapViewerError({ error, onRetry }: { error: string; onRetry: () => void }): React.ReactElement {
  return (
    <div className="flex flex-col items-center justify-center h-full w-full bg-mythos-terminal-background p-4">
      <div className="text-mythos-terminal-error mb-4">Error: {error}</div>
      <button
        onClick={onRetry}
        className="px-4 py-2 bg-mythos-terminal-primary text-white rounded hover:bg-mythos-terminal-primary/80"
      >
        Retry
      </button>
    </div>
  );
}

export interface AsciiMapViewerContentProps {
  plane: string;
  zone: string;
  mapHtml: string;
  viewport: { x: number; y: number };
  setViewportX: React.Dispatch<React.SetStateAction<number>>;
  setViewportY: React.Dispatch<React.SetStateAction<number>>;
  selectedPlane: string;
  selectedZone: string;
  selectedSubZone: string | undefined;
  setSelectedPlane: React.Dispatch<React.SetStateAction<string>>;
  setSelectedZone: React.Dispatch<React.SetStateAction<string>>;
  setSelectedSubZone: React.Dispatch<React.SetStateAction<string | undefined>>;
  onMapClick: (event: React.MouseEvent<HTMLDivElement>) => void;
}

export function AsciiMapViewerContent({
  plane,
  zone,
  mapHtml,
  viewport,
  setViewportX,
  setViewportY,
  selectedPlane,
  selectedZone,
  selectedSubZone,
  setSelectedPlane,
  setSelectedZone,
  setSelectedSubZone,
  onMapClick,
}: AsciiMapViewerContentProps): React.ReactElement {
  return (
    <div className="relative h-full w-full bg-mythos-terminal-background">
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

      <div className="absolute top-4 right-4 z-10 flex gap-2">
        <button onClick={() => setViewportX(prev => prev - 1)} className={VIEWPORT_BUTTON_CLASS} title="Scroll left">
          ←
        </button>
        <button onClick={() => setViewportX(prev => prev + 1)} className={VIEWPORT_BUTTON_CLASS} title="Scroll right">
          →
        </button>
        <button onClick={() => setViewportY(prev => prev - 1)} className={VIEWPORT_BUTTON_CLASS} title="Scroll up">
          ↑
        </button>
        <button onClick={() => setViewportY(prev => prev + 1)} className={VIEWPORT_BUTTON_CLASS} title="Scroll down">
          ↓
        </button>
        <button
          onClick={() => {
            setViewportX(0);
            setViewportY(0);
          }}
          className={VIEWPORT_BUTTON_CLASS}
          title="Reset viewport"
        >
          ⌂
        </button>
      </div>

      <SafeHtml
        html={mapHtml}
        className="flex items-center justify-center h-full w-full overflow-auto"
        tag="div"
        role="img"
        aria-label="Room map; click to select room, use arrow keys to scroll"
        onClick={onMapClick}
      />

      <div className="absolute bottom-4 left-4 z-10 text-xs text-mythos-terminal-text bg-mythos-terminal-background/80 px-2 py-1 rounded">
        Viewport: ({viewport.x}, {viewport.y}) | Use arrow keys to scroll
      </div>
    </div>
  );
}
