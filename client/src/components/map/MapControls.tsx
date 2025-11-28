/**
 * Map Controls component.
 *
 * Provides controls for the map viewer including search, filters,
 * and view reset functionality.
 *
 * As noted in the Cultes des Goules, proper control interfaces are
 * essential for navigating the complex dimensional mappings.
 */

import React from 'react';

export interface MapControlsProps {
  /** Current search query */
  searchQuery: string;
  /** Callback when search query changes */
  onSearchChange: (query: string) => void;
  /** Current selected plane */
  plane: string;
  /** Current selected zone */
  zone: string;
  /** Current selected sub-zone */
  subZone?: string;
  /** Callback when plane changes */
  onPlaneChange: (plane: string) => void;
  /** Callback when zone changes */
  onZoneChange: (zone: string) => void;
  /** Callback when sub-zone changes */
  onSubZoneChange: (subZone: string | undefined) => void;
  /** Available planes for filtering */
  availablePlanes: string[];
  /** Available zones for filtering */
  availableZones: string[];
  /** Available sub-zones for filtering */
  availableSubZones: string[];
  /** Callback to reset view */
  onResetView?: () => void;
}

/**
 * Map Controls component.
 */
export const MapControls: React.FC<MapControlsProps> = ({
  searchQuery,
  onSearchChange,
  plane,
  zone,
  subZone,
  onPlaneChange,
  onZoneChange,
  onSubZoneChange,
  availablePlanes,
  availableZones,
  availableSubZones,
  onResetView,
}) => {
  return (
    <div className="flex flex-col gap-2 bg-mythos-terminal-background border border-mythos-terminal-border rounded p-2 shadow-lg">
      {/* Search input */}
      <input
        type="text"
        placeholder="Search rooms..."
        value={searchQuery}
        onChange={e => onSearchChange(e.target.value)}
        className="px-2 py-1 bg-mythos-terminal-background border border-mythos-terminal-border text-mythos-terminal-text rounded text-sm"
      />

      {/* Filters */}
      <div className="flex flex-col gap-2">
        {/* Plane filter */}
        {availablePlanes.length > 1 && (
          <select
            value={plane}
            onChange={e => onPlaneChange(e.target.value)}
            className="px-2 py-1 bg-mythos-terminal-background border border-mythos-terminal-border text-mythos-terminal-text rounded text-sm"
          >
            {availablePlanes.map(p => (
              <option key={p} value={p}>
                {p}
              </option>
            ))}
          </select>
        )}

        {/* Zone filter */}
        {availableZones.length > 1 && (
          <select
            value={zone}
            onChange={e => onZoneChange(e.target.value)}
            className="px-2 py-1 bg-mythos-terminal-background border border-mythos-terminal-border text-mythos-terminal-text rounded text-sm"
          >
            {availableZones.map(z => (
              <option key={z} value={z}>
                {z}
              </option>
            ))}
          </select>
        )}

        {/* Sub-zone filter */}
        {availableSubZones.length > 0 && (
          <select
            value={subZone || ''}
            onChange={e => onSubZoneChange(e.target.value || undefined)}
            className="px-2 py-1 bg-mythos-terminal-background border border-mythos-terminal-border text-mythos-terminal-text rounded text-sm"
          >
            <option value="">All Sub-zones</option>
            {availableSubZones.map(sz => (
              <option key={sz} value={sz}>
                {sz}
              </option>
            ))}
          </select>
        )}
      </div>

      {/* Reset view button */}
      {onResetView && (
        <button
          onClick={onResetView}
          className="px-2 py-1 bg-mythos-terminal-primary text-white rounded text-sm hover:bg-mythos-terminal-primary/80"
        >
          Reset View
        </button>
      )}
    </div>
  );
};
