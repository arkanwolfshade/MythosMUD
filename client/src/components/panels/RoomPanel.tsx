import { ExitToApp, Info, LocationOn, People } from '@mui/icons-material';
import { Box, Chip, Divider, List, ListItem, ListItemIcon, ListItemText, Typography } from '@mui/material';
import { styled } from '@mui/material/styles';
import React from 'react';

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

interface RoomPanelProps {
  room: Room | null;
}

const RoomSection = styled(Box)(({ theme }) => ({
  marginBottom: theme.spacing(2),
}));

const ExitChip = styled(Chip)(({ theme }) => ({
  margin: theme.spacing(0.5),
}));

const OccupantItem = styled(ListItem)(({ theme }) => ({
  padding: theme.spacing(0.5, 0),
  '& .MuiListItemIcon-root': {
    minWidth: 32,
  },
}));

export const RoomPanel: React.FC<RoomPanelProps> = ({ room }) => {
  if (!room) {
    return (
      <Box sx={{ height: '100%', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
        <Typography variant="body2" color="text.secondary">
          No room information available
        </Typography>
      </Box>
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

  const formatOccupantName = (name: string): string => {
    return name.charAt(0).toUpperCase() + name.slice(1).toLowerCase();
  };

  const availableExits = room.exits
    ? Object.entries(room.exits)
        .filter(([_, destination]) => destination !== null)
        .map(([direction, _]) => direction.charAt(0).toUpperCase() + direction.slice(1))
    : [];

  return (
    <Box sx={{ height: '100%', display: 'flex', flexDirection: 'column', gap: 2 }}>
      <Typography variant="h6" gutterBottom>
        Room Information
      </Typography>

      {/* Room Name */}
      <RoomSection>
        <Typography variant="h5" color="primary" gutterBottom>
          {room.name}
        </Typography>
      </RoomSection>

      {/* Location Info */}
      <RoomSection>
        <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, mb: 1 }}>
          <LocationOn color="action" fontSize="small" />
          <Typography variant="subtitle2" color="text.secondary">
            Location
          </Typography>
        </Box>
        <Box sx={{ pl: 3 }}>
          <Typography variant="body2" gutterBottom>
            <strong>Zone:</strong> {formatLocationName(room.zone || 'Unknown')}
          </Typography>
          <Typography variant="body2">
            <strong>Subzone:</strong> {formatLocationName(room.sub_zone || 'Unknown')}
          </Typography>
        </Box>
      </RoomSection>

      <Divider />

      {/* Description */}
      <RoomSection>
        <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, mb: 1 }}>
          <Info color="action" fontSize="small" />
          <Typography variant="subtitle2" color="text.secondary">
            Description
          </Typography>
        </Box>
        <Typography variant="body2" sx={{ pl: 3, fontStyle: 'italic' }}>
          {formatDescription(room.description)}
        </Typography>
      </RoomSection>

      <Divider />

      {/* Available Exits */}
      <RoomSection>
        <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, mb: 1 }}>
          <ExitToApp color="action" fontSize="small" />
          <Typography variant="subtitle2" color="text.secondary">
            Available Exits
          </Typography>
        </Box>
        <Box sx={{ pl: 3 }}>
          {availableExits.length > 0 ? (
            <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 0.5 }}>
              {availableExits.map(exit => (
                <ExitChip key={exit} label={exit} size="small" variant="outlined" color="primary" />
              ))}
            </Box>
          ) : (
            <Typography variant="body2" color="text.secondary">
              No exits available
            </Typography>
          )}
        </Box>
      </RoomSection>

      <Divider />

      {/* Room Occupants */}
      <RoomSection sx={{ flex: 1, overflow: 'hidden' }}>
        <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, mb: 1 }}>
          <People color="action" fontSize="small" />
          <Typography variant="subtitle2" color="text.secondary">
            Occupants
            {typeof room.occupant_count === 'number' && (
              <Chip label={room.occupant_count} size="small" color="primary" sx={{ ml: 1 }} />
            )}
          </Typography>
        </Box>

        <Box sx={{ pl: 3, height: 'calc(100% - 40px)', overflow: 'auto' }}>
          {room.occupants && room.occupants.length > 0 ? (
            <List dense sx={{ p: 0 }}>
              {room.occupants.map((occupant, index) => (
                <OccupantItem key={index}>
                  <ListItemIcon>
                    <Box
                      sx={{
                        width: 8,
                        height: 8,
                        borderRadius: '50%',
                        backgroundColor: 'success.main',
                      }}
                    />
                  </ListItemIcon>
                  <ListItemText primary={formatOccupantName(occupant)} primaryTypographyProps={{ variant: 'body2' }} />
                </OccupantItem>
              ))}
            </List>
          ) : (
            <Typography variant="body2" color="text.secondary">
              No other players present
            </Typography>
          )}
        </Box>
      </RoomSection>
    </Box>
  );
};
