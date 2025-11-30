import React, { createContext, ReactNode, useContext } from 'react';

// Context for sharing state between compound components
interface RoomInfoContextType {
  room: {
    id: string;
    name: string;
    description: string;
    plane?: string;
    zone?: string;
    sub_zone?: string;
    environment?: string;
    exits: Record<string, string>;
    occupants?: string[];
    occupant_count?: number;
    entities?: Array<{
      name: string;
      type: string;
    }>;
  } | null;
  debugInfo?: {
    hasRoom: boolean;
    roomType: string;
    roomKeys: string[];
    timestamp: string;
  };
}

const RoomInfoContext = createContext<RoomInfoContextType | null>(null);

// Hook to use the room info context
const useRoomInfo = () => {
  const context = useContext(RoomInfoContext);
  if (!context) {
    throw new Error('useRoomInfo must be used within a RoomInfo');
  }
  return context;
};

// Main compound component
interface RoomInfoProps {
  room: RoomInfoContextType['room'];
  debugInfo?: RoomInfoContextType['debugInfo'];
  children: ReactNode;
}

export const RoomInfo: React.FC<RoomInfoProps> = ({ room, debugInfo, children }) => {
  const contextValue: RoomInfoContextType = {
    room,
    debugInfo,
  };

  return (
    <RoomInfoContext.Provider value={contextValue}>
      <div className="space-y-4">{children}</div>
    </RoomInfoContext.Provider>
  );
};

// Room name sub-component
export const RoomName: React.FC = () => {
  const { room } = useRoomInfo();

  if (!room) {
    return (
      <div className="text-center text-mythos-terminal-text-secondary py-4">
        <p className="text-sm">No room information available</p>
      </div>
    );
  }

  return (
    <div className="text-center">
      <h3 className="text-lg font-bold text-mythos-terminal-primary">{room.name}</h3>
    </div>
  );
};

// Room description sub-component
export const RoomDescription: React.FC = () => {
  const { room } = useRoomInfo();

  if (!room) return null;

  return (
    <div className="bg-mythos-terminal-surface border border-gray-700 rounded p-3">
      <p className="text-sm text-mythos-terminal-text leading-relaxed">{room.description}</p>
    </div>
  );
};

// Room location sub-component (plane, zone, sub_zone)
export const RoomLocation: React.FC = () => {
  const { room } = useRoomInfo();

  if (!room || (!room.plane && !room.zone && !room.sub_zone)) return null;

  return (
    <div className="bg-mythos-terminal-surface border border-gray-700 rounded p-3">
      <h4 className="text-sm font-bold text-mythos-terminal-primary mb-2">Location</h4>
      <div className="space-y-1 text-xs">
        {room.plane && (
          <div className="flex justify-between">
            <span className="text-mythos-terminal-text-secondary">Plane:</span>
            <span className="text-mythos-terminal-text">{room.plane}</span>
          </div>
        )}
        {room.zone && (
          <div className="flex justify-between">
            <span className="text-mythos-terminal-text-secondary">Zone:</span>
            <span className="text-mythos-terminal-text">{room.zone}</span>
          </div>
        )}
        {room.sub_zone && (
          <div className="flex justify-between">
            <span className="text-mythos-terminal-text-secondary">Sub-zone:</span>
            <span className="text-mythos-terminal-text">{room.sub_zone}</span>
          </div>
        )}
        {room.environment && (
          <div className="flex justify-between">
            <span className="text-mythos-terminal-text-secondary">Environment:</span>
            <span className="text-mythos-terminal-text">{room.environment}</span>
          </div>
        )}
      </div>
    </div>
  );
};

// Room exits sub-component
export const RoomExits: React.FC = () => {
  const { room } = useRoomInfo();

  if (!room || !room.exits || Object.keys(room.exits).length === 0) {
    return (
      <div className="bg-mythos-terminal-surface border border-gray-700 rounded p-3">
        <h4 className="text-sm font-bold text-mythos-terminal-primary mb-2">Exits</h4>
        <p className="text-xs text-mythos-terminal-text-secondary">No exits available</p>
      </div>
    );
  }

  const exitDirections = Object.keys(room.exits);
  const exitLabels = {
    north: 'North',
    south: 'South',
    east: 'East',
    west: 'West',
    northeast: 'Northeast',
    northwest: 'Northwest',
    southeast: 'Southeast',
    southwest: 'Southwest',
    up: 'Up',
    down: 'Down',
    in: 'In',
    out: 'Out',
  };

  return (
    <div className="bg-mythos-terminal-surface border border-gray-700 rounded p-3">
      <h4 className="text-sm font-bold text-mythos-terminal-primary mb-2">Exits</h4>
      <div className="flex flex-wrap gap-2">
        {exitDirections.map(direction => (
          <span
            key={direction}
            className="px-2 py-1 bg-mythos-terminal-background border border-gray-600 rounded text-xs text-mythos-terminal-text"
          >
            {exitLabels[direction as keyof typeof exitLabels] || direction}
          </span>
        ))}
      </div>
    </div>
  );
};

// Room occupants sub-component
export const RoomOccupants: React.FC = () => {
  const { room } = useRoomInfo();

  if (!room || !room.occupants || room.occupants.length === 0) {
    return (
      <div className="bg-mythos-terminal-surface border border-gray-700 rounded p-3">
        <h4 className="text-sm font-bold text-mythos-terminal-primary mb-2">Occupants</h4>
        <p className="text-xs text-mythos-terminal-text-secondary">No one else is here</p>
      </div>
    );
  }

  return (
    <div className="bg-mythos-terminal-surface border border-gray-700 rounded p-3">
      <div className="space-y-1">
        {room.occupants.map((occupant, index) => (
          <div key={index} className="text-xs text-mythos-terminal-text">
            • {occupant}
          </div>
        ))}
      </div>
    </div>
  );
};

// Room entities sub-component
export const RoomEntities: React.FC = () => {
  const { room } = useRoomInfo();

  if (!room || !room.entities || room.entities.length === 0) {
    return (
      <div className="bg-mythos-terminal-surface border border-gray-700 rounded p-3">
        <h4 className="text-sm font-bold text-mythos-terminal-primary mb-2">Entities</h4>
        <p className="text-xs text-mythos-terminal-text-secondary">No entities present</p>
      </div>
    );
  }

  // Group entities by type
  const entitiesByType = room.entities.reduce(
    (acc, entity) => {
      if (!acc[entity.type]) {
        acc[entity.type] = [];
      }
      acc[entity.type].push(entity);
      return acc;
    },
    {} as Record<string, Array<{ name: string; type: string }>>
  );

  return (
    <div className="bg-mythos-terminal-surface border border-gray-700 rounded p-3">
      <h4 className="text-sm font-bold text-mythos-terminal-primary mb-2">Entities</h4>
      <div className="space-y-2">
        {Object.entries(entitiesByType).map(([type, entities]) => (
          <div key={type}>
            <h5 className="text-xs font-bold text-mythos-terminal-secondary uppercase">{type}</h5>
            <div className="ml-2 space-y-1">
              {entities.map((entity, index) => (
                <div key={index} className="text-xs text-mythos-terminal-text">
                  • {entity.name}
                </div>
              ))}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

// Debug info sub-component
export const DebugInfo: React.FC = () => {
  const { debugInfo } = useRoomInfo();

  if (!debugInfo) return null;

  return (
    <div className="bg-mythos-terminal-surface border border-gray-700 rounded p-3">
      <h4 className="text-sm font-bold text-mythos-terminal-primary mb-2">Debug Info</h4>
      <div className="space-y-1 text-xs">
        <div className="flex justify-between">
          <span className="text-mythos-terminal-text-secondary">Has Room:</span>
          <span className="text-mythos-terminal-text">{debugInfo.hasRoom ? 'Yes' : 'No'}</span>
        </div>
        <div className="flex justify-between">
          <span className="text-mythos-terminal-text-secondary">Room Type:</span>
          <span className="text-mythos-terminal-text">{debugInfo.roomType}</span>
        </div>
        <div className="flex justify-between">
          <span className="text-mythos-terminal-text-secondary">Room Keys:</span>
          <span className="text-mythos-terminal-text">{debugInfo.roomKeys.join(', ')}</span>
        </div>
        <div className="flex justify-between">
          <span className="text-mythos-terminal-text-secondary">Timestamp:</span>
          <span className="text-mythos-terminal-text">{debugInfo.timestamp}</span>
        </div>
      </div>
    </div>
  );
};

// Complete room info sub-component
export const CompleteRoomInfo: React.FC = () => {
  return (
    <>
      <RoomName />
      <RoomDescription />
      <RoomLocation />
      <RoomExits />
      <RoomOccupants />
      <RoomEntities />
      <DebugInfo />
    </>
  );
};
