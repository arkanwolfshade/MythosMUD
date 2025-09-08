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

export function RoomInfoPanel({ room, debugInfo }: RoomInfoPanelProps) {
  console.log('🔍 RoomInfoPanel render called with room:', room);
  console.log('🔍 RoomInfoPanel room type:', typeof room);
  console.log('🔍 RoomInfoPanel room keys:', room ? Object.keys(room) : []);

  // For development mode, show mock room data if no real room data is available
  const displayRoom = room || {
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

  if (!room && !debugInfo) {
    console.log('🔍 RoomInfoPanel: No room data, showing no-room message');
    return (
      <div className="room-info-panel">
        <div className="room-info-content">
          <p className="no-room">No room information available</p>
        </div>
      </div>
    );
  }

  console.log('🔍 RoomInfoPanel: Rendering room data:', {
    name: displayRoom.name,
    description: displayRoom.description,
    zone: displayRoom.zone,
    sub_zone: displayRoom.sub_zone,
    exits: displayRoom.exits,
    occupants: displayRoom.occupants,
    occupant_count: displayRoom.occupant_count,
  });

  // Debug: Log the actual occupant_count value
  console.log(
    '🔍 DEBUG: occupant_count value:',
    displayRoom.occupant_count,
    'type:',
    typeof displayRoom.occupant_count
  );
  console.log('🔍 DEBUG: occupants array:', displayRoom.occupants, 'length:', displayRoom.occupants?.length);

  const formatLocationName = (location: string): string => {
    if (!location || location === 'Unknown') return 'Unknown';
    return location
      .split('_')
      .map(word => word.charAt(0).toUpperCase() + word.slice(1).toLowerCase())
      .join(' ');
  };

  const formatDescription = (description: string): string => {
    if (!description) return 'No description available';
    return description.trim().replace(/\s+/g, ' ');
  };

  const formatOccupantName = (name: string): string => {
    return name.charAt(0).toUpperCase() + name.slice(1).toLowerCase();
  };

  return (
    <div className="room-info-panel">
      <div className="room-info-content">
        {/* Room Name */}
        <div className="room-name">
          <h4>{displayRoom.name}</h4>
        </div>

        {/* Zone */}
        <div className="room-zone">
          <span className="zone-label">Zone:</span>
          <span className="zone-value">{formatLocationName(displayRoom.zone || 'Unknown')}</span>
        </div>

        {/* Subzone */}
        <div className="room-subzone">
          <span className="subzone-label">Subzone:</span>
          <span className="subzone-value">{formatLocationName(displayRoom.sub_zone || 'Unknown')}</span>
        </div>

        {/* Description */}
        <div className="room-description">
          <span className="description-label">Description:</span>
          <p className="description-text">{formatDescription(displayRoom.description)}</p>
        </div>

        {/* Available Exits */}
        <div className="room-exits">
          <span className="exits-label">Exits:</span>
          <p className="exits-text">
            {displayRoom.exits
              ? Object.entries(displayRoom.exits)
                  .filter(([_, destination]) => destination !== null)
                  .map(([direction, _]) => direction.charAt(0).toUpperCase() + direction.slice(1))
                  .join(', ') || 'None'
              : 'None'}
          </p>
        </div>

        {/* Enhanced Room Occupants */}
        <div className="room-occupants">
          <div className="occupants-header">
            <span className="occupants-label">
              Occupants
              {typeof displayRoom.occupant_count === 'number' && (
                <span className="occupant-count-badge">({displayRoom.occupant_count})</span>
              )}
            </span>
          </div>
          <div className="occupants-content">
            {displayRoom.occupants && displayRoom.occupants.length > 0 ? (
              <div className="occupants-list">
                {displayRoom.occupants.map((occupant, index) => (
                  <div key={index} className="occupant-item">
                    <span className="occupant-indicator">●</span>
                    <span className="occupant-name">{formatOccupantName(occupant)}</span>
                  </div>
                ))}
              </div>
            ) : (
              <div className="no-occupants">
                <span className="no-occupants-text">No other players present</span>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
