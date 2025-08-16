import { Clear, Help, Send } from '@mui/icons-material';
import { Box, Button, IconButton, List, ListItem, ListItemText, TextField, Tooltip, Typography } from '@mui/material';
import { styled } from '@mui/material/styles';
import React, { useEffect, useRef, useState } from 'react';

interface CommandPanelProps {
  commandHistory: string[];
  onSendCommand: (command: string) => void;
  onClearHistory?: () => void;
  disabled?: boolean;
  placeholder?: string;
}

const CommandContainer = styled(Box)(() => ({
  height: '100%',
  display: 'flex',
  flexDirection: 'column',
}));

const CommandInputArea = styled(Box)(({ theme }) => ({
  display: 'flex',
  gap: theme.spacing(1),
  padding: theme.spacing(1, 0),
  borderBottom: `1px solid ${theme.palette.divider}`,
  marginBottom: theme.spacing(1),
}));

const HistoryArea = styled(Box)(({ theme }) => ({
  flex: 1,
  overflow: 'auto',
  border: `1px solid ${theme.palette.divider}`,
  borderRadius: theme.shape.borderRadius,
  backgroundColor: theme.palette.background.default,
}));

const HistoryItem = styled(ListItem)(({ theme }) => ({
  padding: theme.spacing(1, 2),
  borderBottom: `1px solid ${theme.palette.divider}`,
  '&:last-child': {
    borderBottom: 'none',
  },
  '&:hover': {
    backgroundColor: theme.palette.action.hover,
  },
}));

const CommandText = styled(Typography)(() => ({
  fontFamily: 'monospace',
  fontSize: '0.875rem',
}));

const CommandTimestamp = styled(Typography)(({ theme }) => ({
  fontSize: '0.75rem',
  color: theme.palette.text.secondary,
  marginTop: theme.spacing(0.5),
}));

const HistoryToolbar = styled(Box)(({ theme }) => ({
  display: 'flex',
  justifyContent: 'space-between',
  alignItems: 'center',
  padding: theme.spacing(1, 2),
  borderBottom: `1px solid ${theme.palette.divider}`,
  backgroundColor: theme.palette.background.paper,
}));

export const CommandPanel: React.FC<CommandPanelProps> = ({
  commandHistory,
  onSendCommand,
  onClearHistory,
  disabled = false,
  placeholder = "Enter command (e.g., 'look' or '/look')...",
}) => {
  const [commandInput, setCommandInput] = useState('');
  const [historyIndex, setHistoryIndex] = useState(-1);
  const inputRef = useRef<HTMLInputElement>(null);

  // Focus input on mount
  useEffect(() => {
    inputRef.current?.focus();
  }, []);

  const handleCommandSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!commandInput.trim() || disabled) return;

    const command = commandInput.trim();
    onSendCommand(command);
    setCommandInput('');
    setHistoryIndex(-1);
  };

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'ArrowUp') {
      e.preventDefault();
      if (historyIndex < commandHistory.length - 1) {
        const newIndex = historyIndex + 1;
        setHistoryIndex(newIndex);
        setCommandInput(commandHistory[commandHistory.length - 1 - newIndex]);
      }
    } else if (e.key === 'ArrowDown') {
      e.preventDefault();
      if (historyIndex > 0) {
        const newIndex = historyIndex - 1;
        setHistoryIndex(newIndex);
        setCommandInput(commandHistory[commandHistory.length - 1 - newIndex]);
      } else if (historyIndex === 0) {
        setHistoryIndex(-1);
        setCommandInput('');
      }
    }
  };

  const handleHistoryClick = (command: string) => {
    setCommandInput(command);
    inputRef.current?.focus();
  };

  const formatTimestamp = (index: number) => {
    // For now, we'll use a simple index-based timestamp
    // In a real implementation, you'd store actual timestamps
    // const now = new Date();
    const timeAgo = commandHistory.length - index;
    if (timeAgo === 1) return 'Just now';
    if (timeAgo < 60) return `${timeAgo} commands ago`;
    return `${Math.floor(timeAgo / 60)}m ago`;
  };

  return (
    <CommandContainer>
      <Typography variant="h6" gutterBottom>
        Command Input
      </Typography>

      {/* Command Input */}
      <form onSubmit={handleCommandSubmit}>
        <CommandInputArea>
          <TextField
            ref={inputRef}
            fullWidth
            size="small"
            value={commandInput}
            onChange={e => setCommandInput(e.target.value)}
            onKeyDown={handleKeyDown}
            placeholder={placeholder}
            disabled={disabled}
            InputProps={{
              endAdornment: (
                <Button
                  type="submit"
                  disabled={!commandInput.trim() || disabled}
                  variant="contained"
                  size="small"
                  endIcon={<Send />}
                >
                  Send
                </Button>
              ),
            }}
          />
        </CommandInputArea>
      </form>

      {/* Command History */}
      <Box sx={{ flex: 1, display: 'flex', flexDirection: 'column' }}>
        <HistoryToolbar>
          <Typography variant="subtitle2">Command History ({commandHistory.length})</Typography>
          <Box>
            {onClearHistory && (
              <Tooltip title="Clear History">
                <IconButton size="small" onClick={onClearHistory}>
                  <Clear />
                </IconButton>
              </Tooltip>
            )}
            <Tooltip title="Command Help">
              <IconButton size="small">
                <Help />
              </IconButton>
            </Tooltip>
          </Box>
        </HistoryToolbar>

        <HistoryArea>
          {commandHistory.length === 0 ? (
            <Box sx={{ display: 'flex', alignItems: 'center', justifyContent: 'center', height: '100%', p: 2 }}>
              <Typography variant="body2" color="text.secondary" textAlign="center">
                No command history yet.
                <br />
                Start typing commands to see them here.
              </Typography>
            </Box>
          ) : (
            <List dense sx={{ p: 0 }}>
              {commandHistory
                .slice()
                .reverse()
                .map((command, index) => (
                  <HistoryItem key={index} onClick={() => handleHistoryClick(command)} sx={{ cursor: 'pointer' }}>
                    <ListItemText
                      primary={<CommandText>&gt; {command}</CommandText>}
                      secondary={<CommandTimestamp>{formatTimestamp(index)}</CommandTimestamp>}
                    />
                  </HistoryItem>
                ))}
            </List>
          )}
        </HistoryArea>
      </Box>

      {/* Quick Commands */}
      <Box sx={{ mt: 1, pt: 1, borderTop: 1, borderColor: 'divider' }}>
        <Typography variant="caption" color="text.secondary" gutterBottom>
          Quick Commands:
        </Typography>
        <Box sx={{ display: 'flex', gap: 0.5, flexWrap: 'wrap' }}>
          {['look', 'inventory', 'help', 'who'].map(cmd => (
            <Button
              key={cmd}
              size="small"
              variant="outlined"
              onClick={() => {
                setCommandInput(cmd);
                inputRef.current?.focus();
              }}
              disabled={disabled}
            >
              {cmd}
            </Button>
          ))}
        </Box>
      </Box>
    </CommandContainer>
  );
};
