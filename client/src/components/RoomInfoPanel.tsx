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
}

interface RoomInfoPanelProps {
  room: Room | null;
}

export function RoomInfoPanel({ room }: RoomInfoPanelProps) {
  console.log('RoomInfoPanel received room:', room);

  if (!room) {
    return (
      <div className="room-info-panel">
        <div className="room-info-content">
          <p className="no-room">No room information available</p>
        </div>
      </div>
    );
  }

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

  return (
    <div className="room-info-panel">
      <div className="room-info-content">
        {/* Room Name */}
        <div className="room-name">
          <h4>{room.name}</h4>
        </div>

        {/* Zone */}
        <div className="room-zone">
          <span className="zone-label">Zone:</span>
          <span className="zone-value">{formatLocationName(room.zone || 'Unknown')}</span>
        </div>

        {/* Subzone */}
        <div className="room-subzone">
          <span className="subzone-label">Subzone:</span>
          <span className="subzone-value">{formatLocationName(room.sub_zone || 'Unknown')}</span>
        </div>

        {/* Description */}
        <div className="room-description">
          <span className="description-label">Description:</span>
          <p className="description-text">{formatDescription(room.description)}</p>
        </div>

        {/* Available Exits */}
        <div className="room-exits">
          <span className="exits-label">Exits:</span>
          <p className="exits-text">
            {room.exits
              ? Object.entries(room.exits)
                  .filter(([_, destination]) => destination !== null)
                  .map(([direction, _]) => direction.charAt(0).toUpperCase() + direction.slice(1))
                  .join(', ') || 'None'
              : 'None'}
          </p>
        </div>
      </div>
    </div>
  );
}
