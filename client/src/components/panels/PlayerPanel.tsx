import { Favorite, FitnessCenter, Person, Psychology, Speed, Star } from '@mui/icons-material';
import { Avatar, Box, Chip, LinearProgress, Paper, Typography } from '@mui/material';
import { styled } from '@mui/material/styles';
import React from 'react';

interface Player {
  name: string;
  stats?: {
    current_health: number;
    max_health?: number;
    sanity: number;
    max_sanity?: number;
    strength?: number;
    dexterity?: number;
    constitution?: number;
    intelligence?: number;
    wisdom?: number;
    charisma?: number;
  };
  level?: number;
}

interface PlayerPanelProps {
  player: Player | null;
}

const StatCard = styled(Paper)(({ theme }) => ({
  padding: theme.spacing(2),
  textAlign: 'center',
  height: '100%',
  display: 'flex',
  flexDirection: 'column',
  justifyContent: 'center',
}));

const StatValue = styled(Typography)(({ theme }) => ({
  fontSize: '1.5rem',
  fontWeight: 'bold',
  color: theme.palette.primary.main,
}));

const StatLabel = styled(Typography)(({ theme }) => ({
  fontSize: '0.875rem',
  color: theme.palette.text.secondary,
  textTransform: 'uppercase',
  letterSpacing: '0.5px',
}));

const ProgressContainer = styled(Box)(({ theme }) => ({
  marginTop: theme.spacing(1),
}));

const ProgressLabel = styled(Typography)(({ theme }) => ({
  fontSize: '0.75rem',
  color: theme.palette.text.secondary,
  marginBottom: theme.spacing(0.5),
}));

export const PlayerPanel: React.FC<PlayerPanelProps> = ({ player }) => {
  if (!player) {
    return (
      <Box sx={{ height: '100%', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
        <Typography variant="body2" color="text.secondary">
          No player information available
        </Typography>
      </Box>
    );
  }

  const stats = player.stats || ({} as Player['stats']);
  const maxHealth = stats?.max_health || 100;
  const maxSanity = stats?.max_sanity || 100;
  const healthPercent = ((stats?.current_health || 0) / maxHealth) * 100;
  const sanityPercent = ((stats?.sanity || 0) / maxSanity) * 100;

  const getStatColor = (value: number): string => {
    if (value >= 16) return 'success.main';
    if (value >= 12) return 'warning.main';
    return 'error.main';
  };

  const getStatIcon = (statName: string) => {
    switch (statName) {
      case 'strength':
        return <FitnessCenter fontSize="small" />;
      case 'dexterity':
        return <Speed fontSize="small" />;
      case 'constitution':
        return <Favorite fontSize="small" />;
      case 'intelligence':
      case 'wisdom':
      case 'charisma':
        return <Psychology fontSize="small" />;
      default:
        return <Star fontSize="small" />;
    }
  };

  return (
    <Box sx={{ height: '100%', display: 'flex', flexDirection: 'column', gap: 2 }}>
      {/* Player Header */}
      <Box sx={{ display: 'flex', alignItems: 'center', gap: 2, mb: 2 }}>
        <Avatar sx={{ bgcolor: 'primary.main' }}>
          <Person />
        </Avatar>
        <Box>
          <Typography variant="h6" gutterBottom>
            {player.name}
          </Typography>
          <Chip label={`Level ${player.level || 1}`} size="small" color="primary" icon={<Star />} />
        </Box>
      </Box>

      {/* Health and Sanity */}
      <Box sx={{ mb: 2 }}>
        <Typography variant="subtitle2" gutterBottom>
          Vital Statistics
        </Typography>

        <ProgressContainer>
          <ProgressLabel>
            Health: {stats?.current_health || 0} / {maxHealth}
          </ProgressLabel>
          <LinearProgress
            variant="determinate"
            value={healthPercent}
            color={healthPercent > 50 ? 'success' : healthPercent > 25 ? 'warning' : 'error'}
            sx={{ height: 8, borderRadius: 4 }}
          />
        </ProgressContainer>

        <ProgressContainer>
          <ProgressLabel>
            Sanity: {stats?.sanity || 0} / {maxSanity}
          </ProgressLabel>
          <LinearProgress
            variant="determinate"
            value={sanityPercent}
            color={sanityPercent > 70 ? 'success' : sanityPercent > 40 ? 'warning' : 'error'}
            sx={{ height: 8, borderRadius: 4 }}
          />
        </ProgressContainer>
      </Box>

      {/* Character Stats */}
      <Box sx={{ flex: 1 }}>
        <Typography variant="subtitle2" gutterBottom>
          Character Statistics
        </Typography>

        <Box sx={{ display: 'grid', gridTemplateColumns: 'repeat(2, 1fr)', gap: 1 }}>
          {['strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma'].map(stat => {
            const value = stats?.[stat as keyof typeof stats] as number;
            if (value === undefined) return null;

            return (
              <StatCard key={stat} elevation={1}>
                <Box sx={{ display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 1, mb: 1 }}>
                  {getStatIcon(stat)}
                  <StatLabel>{stat.charAt(0).toUpperCase() + stat.slice(1)}</StatLabel>
                </Box>
                <StatValue sx={{ color: getStatColor(value) }}>{value}</StatValue>
              </StatCard>
            );
          })}
        </Box>
      </Box>

      {/* Additional Info */}
      <Box sx={{ mt: 'auto', pt: 2, borderTop: 1, borderColor: 'divider' }}>
        <Typography variant="caption" color="text.secondary">
          Character Status: Active
        </Typography>
        {stats?.current_health !== undefined && (
          <Typography variant="caption" color="text.secondary" display="block">
            Health: {healthPercent.toFixed(1)}%
          </Typography>
        )}
        {stats?.sanity !== undefined && (
          <Typography variant="caption" color="text.secondary" display="block">
            Sanity: {sanityPercent.toFixed(1)}%
          </Typography>
        )}
      </Box>
    </Box>
  );
};
