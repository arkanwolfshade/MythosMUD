/**
 * ASCII Map Editor component.
 *
 * This component provides an ASCII-based editing interface for admins
 * to configure room symbols, styles, and map origins.
 *
 * As documented in the Pnakotic Manuscripts, proper spatial configuration
 * is essential for maintaining the integrity of our eldritch architecture.
 */

import React, { useCallback, useState } from 'react';
import { AsciiMapViewer } from './AsciiMapViewer';

export interface AsciiMapEditorProps {
  /** Plane name (required) */
  plane: string;
  /** Zone name (required) */
  zone: string;
  /** Optional sub-zone name for filtering */
  subZone?: string;
  /** API base URL */
  baseUrl?: string;
  /** Auth token for authenticated requests */
  authToken?: string;
}

/**
 * ASCII Map Editor component.
 *
 * Note: Full editing functionality (setting symbols, styles, origins)
 * will be implemented in a future update. For now, this provides
 * a view of the ASCII map with basic controls.
 */
export const AsciiMapEditor: React.FC<AsciiMapEditorProps> = ({ plane, zone, subZone, baseUrl, authToken }) => {
  const [selectedRoomId, setSelectedRoomId] = useState<string | null>(null);
  const [isRecalculating, setIsRecalculating] = useState(false);

  // Handle room selection from map
  const handleRoomSelect = useCallback((roomId: string) => {
    setSelectedRoomId(roomId);
  }, []);

  // Trigger coordinate recalculation
  const handleRecalculate = useCallback(async () => {
    if (!baseUrl || !authToken) {
      return;
    }

    setIsRecalculating(true);
    try {
      const url = new URL(`${baseUrl}/api/maps/coordinates/recalculate`);
      url.searchParams.set('plane', plane);
      url.searchParams.set('zone', zone);
      if (subZone) {
        url.searchParams.set('sub_zone', subZone);
      }

      const response = await fetch(url.toString(), {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${authToken}`,
        },
      });

      if (!response.ok) {
        throw new Error(`Failed to recalculate: ${response.statusText}`);
      }

      const data = await response.json();
      if (data.conflict_count > 0) {
        alert(`Recalculation complete with ${data.conflict_count} conflicts. Check console for details.`);
        console.warn('Coordinate conflicts:', data.conflicts);
      } else {
        alert('Coordinates recalculated successfully.');
      }
    } catch (err) {
      alert(`Error: ${err instanceof Error ? err.message : 'Failed to recalculate'}`);
    } finally {
      setIsRecalculating(false);
    }
  }, [baseUrl, authToken, plane, zone, subZone]);

  return (
    <div className="relative h-full w-full bg-mythos-terminal-background flex flex-col">
      {/* Editor toolbar */}
      <div className="flex items-center justify-between p-4 border-b border-mythos-terminal-border bg-mythos-terminal-background">
        <h2 className="text-xl font-bold text-mythos-terminal-text">ASCII Map Editor</h2>
        <div className="flex gap-2">
          <button
            onClick={handleRecalculate}
            disabled={isRecalculating}
            className="px-4 py-2 bg-mythos-terminal-primary text-white rounded hover:bg-mythos-terminal-primary/80 disabled:opacity-50"
          >
            {isRecalculating ? 'Recalculating...' : 'Recalculate Coordinates'}
          </button>
        </div>
      </div>

      {/* Map viewer */}
      <div className="flex-1 overflow-hidden">
        <AsciiMapViewer
          plane={plane}
          zone={zone}
          subZone={subZone}
          baseUrl={baseUrl}
          authToken={authToken}
          onRoomSelect={handleRoomSelect}
        />
      </div>

      {/* Room details panel (placeholder for future editing) */}
      {selectedRoomId && (
        <div className="absolute bottom-4 left-4 right-4 bg-mythos-terminal-background border border-mythos-terminal-border rounded p-4 max-h-48 overflow-auto">
          <div className="flex items-center justify-between mb-2">
            <h3 className="text-lg font-bold text-mythos-terminal-text">Room: {selectedRoomId}</h3>
            <button
              onClick={() => {
                setSelectedRoomId(null);
              }}
              className="text-mythos-terminal-text hover:text-mythos-terminal-error"
            >
              ×
            </button>
          </div>
          <p className="text-sm text-mythos-terminal-text/70">
            Room editing functionality will be available in a future update.
          </p>
        </div>
      )}
    </div>
  );
};
