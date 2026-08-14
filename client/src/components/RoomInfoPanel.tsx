import { logger } from '../utils/logger.js';
import './RoomInfoPanel.css';

interface Room {
  id: string;
  name: string;
  description: string;
  plane?: string;
  zone?: string;
  sub_zone?: string;
  environment?: string;
  exits?: Record<string, string | null>;
  occupants?: string[];
  players?: string[];
  npcs?: string[];
  occupant_count?: number;
}

interface RoomInfoPanelProps {
  room: Room | null;
  debugInfo?: {
    hasRoom: boolean;
    roomType: string;
    roomKeys: string[];
    timestamp: string;
  };
}

const KNOWN_LOCATION_PATTERNS: Record<string, string> = {
  arkhamcity: 'Arkham City',
  universitylibrary: 'University Library',
  cityhall: 'City Hall',
  policeheadquarters: 'Police Headquarters',
  hospital: 'Hospital',
  library: 'Library',
  university: 'University',
  arkham: 'Arkham',
};

const ROOM_DEFAULT_FIELD_FIXES: Array<{
  needsFix: (room: Room) => boolean;
  apply: (room: Room) => void;
}> = [
  {
    needsFix: room => !room.description || room.description.trim() === '',
    apply: room => {
      room.description = 'No description available';
    },
  },
  {
    needsFix: room => !room.zone,
    apply: room => {
      room.zone = 'Unknown';
    },
  },
  {
    needsFix: room => !room.sub_zone,
    apply: room => {
      room.sub_zone = 'Unknown';
    },
  },
  {
    needsFix: room => !room.exits,
    apply: room => {
      room.exits = {};
    },
  },
  {
    needsFix: room => !room.occupants,
    apply: room => {
      room.occupants = [];
    },
  },
];

function applyRoomDefaultFields(validatedRoom: Room): number {
  let fixesApplied = 0;
  for (const fix of ROOM_DEFAULT_FIELD_FIXES) {
    if (fix.needsFix(validatedRoom)) {
      fix.apply(validatedRoom);
      fixesApplied++;
    }
  }
  return fixesApplied;
}

function fixOccupantCountMismatch(validatedRoom: Room): boolean {
  if (!validatedRoom.occupants || validatedRoom.occupant_count === undefined) {
    return false;
  }
  const actualCount = validatedRoom.occupants.length;
  if (actualCount === validatedRoom.occupant_count) {
    return false;
  }
  logger.warn('RoomInfoPanel', 'Occupant count mismatch detected', {
    expected: validatedRoom.occupant_count,
    actual: actualCount,
    roomId: validatedRoom.id,
    roomName: validatedRoom.name,
  });
  validatedRoom.occupant_count = actualCount;
  return true;
}

function validateAndFixRoomData(room: Room | null): Room | null {
  if (!room) {
    logger.debug('RoomInfoPanel', 'No room data to validate');
    return null;
  }

  const validatedRoom: Room = { ...room };
  const fixesApplied = applyRoomDefaultFields(validatedRoom) + (fixOccupantCountMismatch(validatedRoom) ? 1 : 0);

  if (!validatedRoom.id || !validatedRoom.name) {
    logger.error('RoomInfoPanel', 'Critical room data missing', {
      hasId: !!validatedRoom.id,
      hasName: !!validatedRoom.name,
    });
    return null;
  }

  logger.debug('RoomInfoPanel', fixesApplied > 0 ? 'Room data validation completed' : 'Room data is valid', {
    roomId: validatedRoom.id,
    fixesApplied,
  });
  return validatedRoom;
}

function formatLocationName(location: string): string {
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
  const known = KNOWN_LOCATION_PATTERNS[location.toLowerCase()];
  if (known) return known;
  return location.charAt(0).toUpperCase() + location.slice(1).toLowerCase();
}

function formatDescription(description: string): string {
  if (!description) return 'No description available';
  return description.trim().replace(/\s+/g, ' ');
}

function formatExitDirections(exits: Record<string, string | null> | undefined): string {
  if (!exits) return 'None';
  const directions = Object.entries(exits)
    .filter(([, destination]) => destination !== null)
    .map(([direction]) => direction.charAt(0).toUpperCase() + direction.slice(1));
  return directions.length > 0 ? directions.join(', ') : 'None';
}

function OccupantList({ names, testId }: { names: string[]; testId: string }) {
  return (
    <div className="occupants-list">
      {names.map((name, index) => (
        <div key={`${testId}-${index}`} className="occupant-item">
          <span className="occupant-indicator">●</span>
          <span className="occupant-name" data-testid={testId}>
            {name}
          </span>
        </div>
      ))}
    </div>
  );
}

function RoomOccupantsSection({ room }: { room: Room }) {
  const hasStructured = room.players !== undefined || room.npcs !== undefined;
  const hasPlayers = (room.players?.length ?? 0) > 0;
  const hasNpcs = (room.npcs?.length ?? 0) > 0;

  return (
    <div className="room-occupants">
      <div className="occupants-header">
        <span className="occupants-label">
          Occupants
          {typeof room.occupant_count === 'number' && (
            <span className="occupant-count-badge" data-testid="occupant-count">
              ({room.occupant_count})
            </span>
          )}
        </span>
      </div>
      <div className="occupants-content">
        {hasStructured ? (
          <>
            {hasPlayers && (
              <div className="occupants-section">
                <div className="occupants-section-header">Players</div>
                <OccupantList names={room.players ?? []} testId="occupant-name-player" />
              </div>
            )}
            {hasNpcs && (
              <div className="occupants-section">
                <div className="occupants-section-header">NPCs</div>
                <OccupantList names={room.npcs ?? []} testId="occupant-name-npc" />
              </div>
            )}
            {!hasPlayers && !hasNpcs && (
              <div className="no-occupants">
                <span className="no-occupants-text">No other players present</span>
              </div>
            )}
          </>
        ) : room.occupants && room.occupants.length > 0 ? (
          <OccupantList names={room.occupants} testId="occupant-name" />
        ) : (
          <div className="no-occupants">
            <span className="no-occupants-text">No other players present</span>
          </div>
        )}
      </div>
    </div>
  );
}

const DEV_FALLBACK_ROOM: Room = {
  id: 'dev-room-1',
  name: 'Miskatonic University Library',
  description:
    'A vast repository of forbidden knowledge. Ancient tomes line the shelves, their leather bindings cracked with age. The air is thick with the scent of old parchment and something else... something that makes your skin crawl. Strange symbols are carved into the wooden shelves, and the shadows seem to move independently of any light source.',
  zone: 'arkham',
  sub_zone: 'university',
  plane: 'material',
  environment: 'indoor',
  exits: {
    north: 'university_hallway',
    south: 'university_entrance',
    east: 'restricted_section',
    west: 'reading_room',
  },
  occupants: ['Dr. Armitage', 'Librarian'],
  occupant_count: 2,
};

function logRoomInfoRenderDebug(room: Room | null, displayRoom: Room): void {
  if (!room) return;
  logger.debug('RoomInfoPanel', 'Rendering room data', {
    name: displayRoom.name,
    description: displayRoom.description,
    zone: displayRoom.zone,
    sub_zone: displayRoom.sub_zone,
    occupant_count: displayRoom.occupant_count,
    occupants_length: displayRoom.occupants?.length ?? 0,
  });
}

function RoomInfoEmptyState() {
  logger.debug('RoomInfoPanel', 'No room data, showing no-room message');
  return (
    <div className="room-info-panel">
      <div className="room-info-content">
        <p className="no-room">No room information available</p>
      </div>
    </div>
  );
}

export function RoomInfoPanel({ room, debugInfo }: RoomInfoPanelProps) {
  logger.debug('RoomInfoPanel', 'render called with room', {
    room,
    roomType: typeof room,
    roomKeys: room ? Object.keys(room) : [],
  });

  const validatedRoom = validateAndFixRoomData(room);
  const displayRoom = validatedRoom || DEV_FALLBACK_ROOM;
  logRoomInfoRenderDebug(room, displayRoom);

  if (!room && !debugInfo) {
    return <RoomInfoEmptyState />;
  }

  return (
    <div className="room-info-panel" data-testid="room-info-panel">
      <div className="room-info-content">
        <div className="room-name" data-testid="room-name">
          <h4>{displayRoom.name}</h4>
        </div>

        <div className="room-location">
          <span className="location-label">Location:</span>
          <span className="location-value" data-testid="location-value">
            {formatLocationName(displayRoom.zone || 'Unknown')} /{' '}
            {formatLocationName(displayRoom.sub_zone || 'Unknown')}
          </span>
        </div>

        <div className="room-description" data-testid="room-description">
          <span className="description-label">Description:</span>
          <p className="description-text">{formatDescription(displayRoom.description)}</p>
        </div>

        <div className="room-exits">
          <span className="exits-label">Exits:</span>
          <p className="exits-text">{formatExitDirections(displayRoom.exits)}</p>
        </div>

        <RoomOccupantsSection room={displayRoom} />
      </div>
    </div>
  );
}
