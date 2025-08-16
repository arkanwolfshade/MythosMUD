import { Clear, Download } from '@mui/icons-material';
import { Box, IconButton, Tooltip, Typography } from '@mui/material';
import { styled } from '@mui/material/styles';
import React, { useEffect, useRef } from 'react';
import { ansiToHtmlWithBreaks } from '../../utils/ansiToHtml';

interface ChatMessage {
  text: string;
  timestamp: string;
  isHtml: boolean;
  isCompleteHtml?: boolean;
  messageType?: string;
  aliasChain?: Array<{
    original: string;
    expanded: string;
    alias_name: string;
  }>;
}

interface ChatPanelProps {
  messages: ChatMessage[];
  onClearMessages?: () => void;
  onDownloadLogs?: () => void;
}

const MessageContainer = styled(Box)(() => ({
  height: '100%',
  display: 'flex',
  flexDirection: 'column',
}));

const MessagesArea = styled(Box)(({ theme }) => ({
  flex: 1,
  overflow: 'auto',
  padding: theme.spacing(1),
  backgroundColor: '#0a0a0a', // Dark background for MythosMUD theme
  border: `1px solid ${theme.palette.divider}`,
  borderRadius: theme.shape.borderRadius,
  color: '#00ff00', // Green text for terminal feel
}));

const MessageItem = styled(Box)(({ theme }) => ({
  marginBottom: theme.spacing(1),
  padding: theme.spacing(1),
  borderRadius: theme.shape.borderRadius,
  backgroundColor: '#1a1a1a', // Darker background for message items
  border: `1px solid #333333`, // Dark border
  color: '#00ff00', // Green text
  '&:last-child': {
    marginBottom: 0,
  },
}));

const MessageTimestamp = styled(Typography)(({ theme }) => ({
  fontSize: '0.75rem',
  color: theme.palette.text.secondary,
  marginBottom: theme.spacing(0.5),
}));

const MessageContent = styled(Box)(({ theme }) => ({
  fontSize: '0.875rem',
  lineHeight: 1.4,
  wordWrap: 'break-word',
  '&.emote': {
    fontStyle: 'italic',
    color: theme.palette.primary.main,
  },
  '&.system': {
    color: theme.palette.warning.main,
    fontWeight: 'bold',
  },
  '&.error': {
    color: theme.palette.error.main,
    fontWeight: 'bold',
  },
}));

const AliasExpansion = styled(Box)(({ theme }) => ({
  backgroundColor: theme.palette.action.hover,
  border: `1px solid ${theme.palette.primary.light}`,
  borderRadius: theme.shape.borderRadius,
  padding: theme.spacing(0.5, 1),
  marginBottom: theme.spacing(0.5),
  fontSize: '0.75rem',
}));

const AliasChain = styled(Box)(({ theme }) => ({
  display: 'inline-block',
  marginRight: theme.spacing(1),
}));

const AliasOriginal = styled(Typography)(({ theme }) => ({
  color: theme.palette.warning.main,
  fontWeight: 'bold',
  fontSize: 'inherit',
}));

const AliasArrow = styled(Typography)(({ theme }) => ({
  color: theme.palette.primary.main,
  margin: `0 ${theme.spacing(0.5)}`,
  fontSize: 'inherit',
}));

const AliasExpanded = styled(Typography)(({ theme }) => ({
  color: theme.palette.success.main,
  fontStyle: 'italic',
  fontSize: 'inherit',
}));

const ChatToolbar = styled(Box)(({ theme }) => ({
  display: 'flex',
  justifyContent: 'space-between',
  alignItems: 'center',
  padding: theme.spacing(1, 0),
  borderBottom: `1px solid ${theme.palette.divider}`,
  marginBottom: theme.spacing(1),
}));

export const ChatPanel: React.FC<ChatPanelProps> = ({ messages, onClearMessages, onDownloadLogs }) => {
  const messagesEndRef = useRef<HTMLDivElement>(null);

  // Auto-scroll to bottom when new messages arrive
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  const getMessageClass = (messageType?: string): string => {
    switch (messageType) {
      case 'emote':
        return 'emote';
      case 'system':
        return 'system';
      case 'error':
        return 'error';
      default:
        return '';
    }
  };

  return (
    <MessageContainer>
      <ChatToolbar>
        <Typography variant="h6">Chat Log ({messages.length} messages)</Typography>
        <Box>
          {onClearMessages && (
            <Tooltip title="Clear Messages">
              <IconButton size="small" onClick={onClearMessages}>
                <Clear />
              </IconButton>
            </Tooltip>
          )}
          {onDownloadLogs && (
            <Tooltip title="Download Logs">
              <IconButton size="small" onClick={onDownloadLogs}>
                <Download />
              </IconButton>
            </Tooltip>
          )}
        </Box>
      </ChatToolbar>

      <MessagesArea>
        {messages.length === 0 ? (
          <Box sx={{ display: 'flex', alignItems: 'center', justifyContent: 'center', height: '100%' }}>
            <Typography variant="body2" color="text.secondary">
              No messages yet. Connect to the game to see chat activity.
            </Typography>
          </Box>
        ) : (
          messages.map((message, index) => (
            <MessageItem key={index}>
              {/* Alias Expansion Information */}
              {message.aliasChain && message.aliasChain.length > 0 && (
                <AliasExpansion>
                  <Box sx={{ display: 'flex', alignItems: 'center', gap: 0.5, mb: 0.5 }}>
                    <Typography variant="caption" sx={{ fontWeight: 'bold' }}>
                      🔗 Alias Expansion:
                    </Typography>
                  </Box>
                  {message.aliasChain.map((alias, chainIndex) => (
                    <AliasChain key={chainIndex}>
                      <AliasOriginal>{alias.original}</AliasOriginal>
                      <AliasArrow>→</AliasArrow>
                      <AliasExpanded>{alias.expanded}</AliasExpanded>
                    </AliasChain>
                  ))}
                </AliasExpansion>
              )}

              {/* Message Timestamp */}
              <MessageTimestamp>{message.timestamp}</MessageTimestamp>

              {/* Message Content */}
              <MessageContent
                className={getMessageClass(message.messageType)}
                dangerouslySetInnerHTML={{
                  __html: message.isHtml
                    ? message.isCompleteHtml
                      ? message.text
                      : ansiToHtmlWithBreaks(message.text)
                    : message.text,
                }}
              />
            </MessageItem>
          ))
        )}
        <div ref={messagesEndRef} />
      </MessagesArea>
    </MessageContainer>
  );
};
