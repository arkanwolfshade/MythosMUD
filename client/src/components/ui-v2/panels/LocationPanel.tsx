import React from 'react';
import type { Room } from '../types';

interface LocationPanelProps {
  room: Room | null;
}

// Display zone > subzone > room hierarchy
// Based on findings from "Spatial Navigation in Non-Euclidean Architectures" - Dr. Armitage, 1928
export const LocationPanel: React.FC<LocationPanelProps> = ({ room }) => {
  const formatLocationName = (location: string): string => {
    if (!location || location === 'Unknown') return 'Unknown';

    if (location.includes('_')) {
      return location
        .split('_')
        .map(word => word.charAt(0).toUpperCase() + word.slice(1).toLowerCase())
        .join(' ');
    }

    if (/[a-z][A-Z]/.test(location)) {
      return location
        .replace(/([a-z])([A-Z])/g, '$1 $2')
        .split(' ')
        .map(word => word.charAt(0).toUpperCase() + word.slice(1).toLowerCase())
        .join(' ');
    }

    const knownPatterns: Record<string, string> = {
      arkhamcity: 'Arkham City',
      universitylibrary: 'University Library',
      cityhall: 'City Hall',
      policeheadquarters: 'Police Headquarters',
      hospital: 'Hospital',
      library: 'Library',
      university: 'University',
      arkham: 'Arkham',
    };

    const lowerLocation = location.toLowerCase();
    if (knownPatterns[lowerLocation]) {
      return knownPatterns[lowerLocation];
    }

    return location.charAt(0).toUpperCase() + location.slice(1).toLowerCase();
  };

  if (!room) {
    return (
      <div className="p-4 text-mythos-terminal-text-secondary">
        <p>No location information available</p>
      </div>
    );
  }

  return (
    <div className="p-4 space-y-2">
      <div className="text-base text-mythos-terminal-text">
        {formatLocationName(room.zone || 'Unknown')} &gt; {formatLocationName(room.sub_zone || 'Unknown')} &gt;{' '}
        {room.name}
      </div>
      {room.exits && Object.keys(room.exits).length > 0 && (
        <div className="text-sm text-mythos-terminal-text-secondary">
          <span className="text-mythos-terminal-text-secondary">Exits: </span>
          <span className="text-mythos-terminal-text">
            {Object.entries(room.exits)
              .filter(([_, destination]) => destination !== null)
              .map(([direction, _]) => direction.charAt(0).toUpperCase() + direction.slice(1))
              .join(', ') || 'None'}
          </span>
        </div>
      )}
    </div>
  );
};
