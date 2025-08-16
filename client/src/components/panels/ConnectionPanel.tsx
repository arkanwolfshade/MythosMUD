import { Download, Logout, Wifi, WifiOff } from '@mui/icons-material';
import { Alert, Box, Button, Chip, Stack, Typography } from '@mui/material';
import { styled } from '@mui/material/styles';
import React from 'react';

const StatusIndicator = styled(Box)<{ connected: boolean }>(({ theme, connected }) => ({
  display: 'flex',
  alignItems: 'center',
  gap: theme.spacing(1),
  padding: theme.spacing(1),
  borderRadius: theme.shape.borderRadius,
  backgroundColor: connected ? theme.palette.success.light : theme.palette.error.light,
  color: connected ? theme.palette.success.contrastText : theme.palette.error.contrastText,
  fontWeight: 'bold',
}));

interface ConnectionPanelProps {
  isConnected: boolean;
  isConnecting: boolean;
  error: string | null;
  reconnectAttempts: number;
  onConnect: () => void;
  onDisconnect: () => void;
  onLogout: () => void;
  onDownloadLogs: () => void;
}

export const ConnectionPanel: React.FC<ConnectionPanelProps> = ({
  isConnected,
  isConnecting,
  error,
  reconnectAttempts,
  onConnect,
  onDisconnect,
  onLogout,
  onDownloadLogs,
}) => {
  return (
    <Box sx={{ height: '100%', display: 'flex', flexDirection: 'column', gap: 2 }}>
      <Typography variant="h6" gutterBottom>
        Connection Status
      </Typography>

      {/* Status Indicator */}
      <StatusIndicator connected={isConnected}>
        {isConnected ? <Wifi /> : <WifiOff />}
        <Typography variant="body2">
          {isConnecting ? 'Connecting...' : isConnected ? 'Connected' : 'Disconnected'}
        </Typography>
      </StatusIndicator>

      {/* Error Display */}
      {error && (
        <Alert severity="error" sx={{ fontSize: '0.875rem' }}>
          {error}
        </Alert>
      )}

      {/* Reconnect Info */}
      {reconnectAttempts > 0 && (
        <Chip label={`Reconnect attempt ${reconnectAttempts}`} color="warning" variant="outlined" size="small" />
      )}

      {/* Connection Instructions */}
      {!isConnected && !isConnecting && (
        <Alert severity="info" sx={{ fontSize: '0.875rem' }}>
          <Typography variant="body2" sx={{ fontWeight: 'bold', mb: 1 }}>
            Getting Started
          </Typography>
          <Typography variant="body2">
            You are authenticated and ready to play! Click the "Connect" button below to join the game world.
          </Typography>
        </Alert>
      )}

      {/* Connection Controls */}
      <Stack spacing={1}>
        {!isConnected && !isConnecting ? (
          <Button variant="contained" color="success" startIcon={<Wifi />} onClick={onConnect} fullWidth>
            Connect to Game
          </Button>
        ) : (
          <Button variant="contained" color="error" startIcon={<WifiOff />} onClick={onDisconnect} fullWidth>
            Disconnect
          </Button>
        )}

        <Button variant="outlined" color="error" startIcon={<Logout />} onClick={onLogout} fullWidth>
          Logout
        </Button>

        <Button variant="outlined" startIcon={<Download />} onClick={onDownloadLogs} fullWidth>
          Download Logs
        </Button>
      </Stack>

      {/* Connection Stats */}
      <Box sx={{ mt: 'auto', pt: 2, borderTop: 1, borderColor: 'divider' }}>
        <Typography variant="caption" color="text.secondary">
          Status: {isConnected ? 'Online' : 'Offline'}
        </Typography>
        {reconnectAttempts > 0 && (
          <Typography variant="caption" color="text.secondary" display="block">
            Reconnect attempts: {reconnectAttempts}
          </Typography>
        )}
      </Box>
    </Box>
  );
};
