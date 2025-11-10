import React, { useMemo, useState } from 'react';
import {
  ALL_MESSAGES_CHANNEL,
  AVAILABLE_CHANNELS,
  CHAT_CHANNEL_OPTIONS,
  DEFAULT_CHANNEL,
  getChannelById,
} from '../../config/channels';
import { ansiToHtmlWithBreaks } from '../../utils/ansiToHtml';
import { extractChannelFromMessage, isChatContent } from '../../utils/messageTypeUtils';
import { ChannelSelector } from '../ui/ChannelSelector';
import { EldritchIcon, MythosIcons } from '../ui/EldritchIcon';
import { TerminalButton } from '../ui/TerminalButton';

// Function to get font size class
const getFontSizeClass = (): string => {
  // This would typically come from theme context
  return 'text-sm';
};

// Function to get activity color classes based on activity level
const getActivityColor = (activityLevel: string): string => {
  switch (activityLevel) {
    case 'high':
      return 'bg-red-500';
    case 'medium':
      return 'bg-yellow-500';
    case 'low':
      return 'bg-green-500';
    case 'none':
    default:
      return 'bg-gray-500';
  }
};

interface ChatMessage {
  text: string;
  timestamp: string;
  isHtml: boolean;
  isCompleteHtml?: boolean;
  messageType?: string;
  channel?: string;
  aliasChain?: Array<{
    original: string;
    expanded: string;
    alias_name: string;
  }>;
  rawText?: string; // Added for plain text messages
}

interface ChatPanelProps {
  messages: ChatMessage[];
  onSendChatMessage: (message: string, channel: string) => void;
  onClearMessages?: () => void;
  onDownloadLogs?: () => void;
  disabled?: boolean;
  isConnected?: boolean;
  selectedChannel?: string;
  onChannelSelect?: (channelId: string) => void;
}

export const ChatPanel: React.FC<ChatPanelProps> = ({
  messages,
  onClearMessages,
  onDownloadLogs,
  disabled = false,
  isConnected = true,
  selectedChannel = ALL_MESSAGES_CHANNEL.id,
  onChannelSelect,
}) => {
  const [clearedChannels, setClearedChannels] = useState<Record<string, number>>({});
  const [isHistoryVisible, setIsHistoryVisible] = useState(false);

  const normalizedSelectedChannel = selectedChannel ?? DEFAULT_CHANNEL;

  const filteredMessages = useMemo(() => {
    return messages.filter(message => {
      if (message.messageType === 'system') {
        return false;
      }

      if (normalizedSelectedChannel === ALL_MESSAGES_CHANNEL.id) {
        return true;
      }

      if (message.messageType === 'command' || message.messageType === 'error') {
        return true;
      }

      const isChatMessage = message.messageType === 'chat' || isChatContent(message.text);
      if (!isChatMessage) {
        return false;
      }

      const messageChannel = message.channel || extractChannelFromMessage(message.text) || 'local';

      if (messageChannel === 'whisper') {
        return true;
      }

      return messageChannel === normalizedSelectedChannel;
    });
  }, [messages, normalizedSelectedChannel]);

  const chatStats = {
    currentChannelMessages: filteredMessages.length,
    totalMessages: messages.filter(message => message.messageType !== 'system').length,
  };

  const unreadCounts = useMemo(() => {
    if (normalizedSelectedChannel === ALL_MESSAGES_CHANNEL.id) {
      return {};
    }

    const counts: Record<string, number> = {};

    messages.forEach((message, index) => {
      if (message.messageType === 'chat' || (message.messageType === 'command' && isChatContent(message.text))) {
        const channelId = message.channel || extractChannelFromMessage(message.text) || normalizedSelectedChannel;
        if (channelId !== normalizedSelectedChannel && index >= (clearedChannels[channelId] || 0)) {
          counts[channelId] = (counts[channelId] || 0) + 1;
        }
      }
    });

    return counts;
  }, [messages, normalizedSelectedChannel, clearedChannels]);

  const handleChannelSelect = (channelId: string) => {
    if (channelId === ALL_MESSAGES_CHANNEL.id) {
      setClearedChannels({});
    } else {
      setClearedChannels(prev => ({ ...prev, [channelId]: messages.length }));
    }
    onChannelSelect?.(channelId);
  };

  const viewingLabel =
    normalizedSelectedChannel === ALL_MESSAGES_CHANNEL.id
      ? ALL_MESSAGES_CHANNEL.name
      : (getChannelById(normalizedSelectedChannel)?.name ?? normalizedSelectedChannel);

  const formatTimestamp = (timestamp: string): string => {
    try {
      const date = new Date(timestamp);
      return date.toLocaleTimeString('en-US', {
        hour12: false,
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit',
      });
    } catch {
      return timestamp;
    }
  };

  const getMessageClass = (messageType?: string): string => {
    switch (messageType) {
      case 'emote':
        return 'text-mythos-terminal-primary italic';
      case 'system':
        return 'text-mythos-terminal-warning font-bold';
      case 'error':
        return 'text-mythos-terminal-error font-bold';
      case 'whisper':
        return 'text-mythos-terminal-secondary italic';
      case 'shout':
        return 'text-mythos-terminal-warning font-bold';
      default:
        return 'text-mythos-terminal-text';
    }
  };

  const toggleHistory = () => {
    setIsHistoryVisible(prev => !prev);
  };

  return (
    <div className="h-full flex flex-col font-mono">
      {/* Chat Header */}
      <div className="flex items-center justify-between p-3 border-b border-gray-700 bg-mythos-terminal-surface">
        <div className="flex items-center gap-2">
          <EldritchIcon name={MythosIcons.chat} size={20} variant="primary" />
          <h3 className="text-mythos-terminal-primary font-bold">Chat</h3>
        </div>
        <div className="flex items-center gap-2">
          {onClearMessages && (
            <TerminalButton variant="secondary" size="sm" onClick={onClearMessages} className="p-2 h-8 w-8">
              <EldritchIcon name={MythosIcons.clear} size={14} variant="error" />
            </TerminalButton>
          )}
          {onDownloadLogs && (
            <TerminalButton variant="secondary" size="sm" onClick={onDownloadLogs} className="p-2 h-8 w-8">
              <EldritchIcon name={MythosIcons.download} size={14} variant="primary" />
            </TerminalButton>
          )}
        </div>
      </div>

      {/* Channel Selector */}
      <div
        className="p-3 border-b border-gray-700 bg-mythos-terminal-surface"
        role="region"
        aria-label="Channel Selection"
      >
        <div className="flex flex-col sm:flex-row items-start sm:items-center gap-2">
          <span className="text-sm text-mythos-terminal-text-secondary font-mono">Channel:</span>
          <ChannelSelector
            channels={CHAT_CHANNEL_OPTIONS}
            selectedChannel={normalizedSelectedChannel}
            onChannelSelect={handleChannelSelect}
            disabled={disabled || !isConnected}
            className="flex-1 w-full sm:w-auto"
          />
        </div>

        {/* Channel Activity Indicators */}
        <div
          className="flex flex-col sm:flex-row items-start sm:items-center gap-2 sm:gap-4 mt-2"
          role="region"
          aria-label="Channel Activity Indicators"
        >
          <span className="text-xs text-mythos-terminal-text-secondary">Activity:</span>
          <div className="flex flex-wrap items-center gap-2">
            {AVAILABLE_CHANNELS.map(channel => {
              const activityLevel = 'none';
              const unreadCount = unreadCounts[channel.id] || 0;

              return (
                <div
                  key={channel.id}
                  className="flex items-center gap-1 group cursor-pointer hover:bg-mythos-terminal-background/50 rounded px-1 transition-all duration-200"
                  role="button"
                  tabIndex={0}
                  aria-label={`${channel.name} channel - ${activityLevel} activity${unreadCount > 0 ? `, ${unreadCount} unread messages` : ''}`}
                  onKeyDown={e => {
                    if (e.key === 'Enter' || e.key === ' ') {
                      e.preventDefault();
                      handleChannelSelect(channel.id);
                    }
                  }}
                >
                  <div
                    className={`w-2 h-2 rounded-full ${getActivityColor(activityLevel)} transition-all duration-300`}
                  ></div>
                  <span className="text-xs text-mythos-terminal-text-secondary group-hover:text-mythos-terminal-primary transition-colors duration-200">
                    {channel.name}
                  </span>
                  {unreadCount > 0 && (
                    <div className="bg-mythos-terminal-error text-white text-xs rounded-full px-1 min-w-[16px] h-4 flex items-center justify-center animate-bounce">
                      {unreadCount > 99 ? '99+' : unreadCount}
                    </div>
                  )}
                </div>
              );
            })}
          </div>
        </div>
      </div>

      {/* Chat History Toggle */}
      <div className="p-2 border-b border-gray-700 bg-mythos-terminal-background" data-testid="chat-history-toggle">
        <button className="text-xs text-mythos-terminal-primary" onClick={toggleHistory} type="button">
          Chat History
        </button>
        <select
          className="ml-2 text-xs bg-mythos-terminal-surface border border-gray-700 rounded px-1"
          value={isHistoryVisible ? 'all' : 'current'}
          onChange={event => setIsHistoryVisible(event.target.value === 'all')}
        >
          <option value="current">Current</option>
          <option value="all">All</option>
        </select>
        <span className="ml-2 text-xs text-mythos-terminal-text-secondary">Messages: {filteredMessages.length}</span>
      </div>

      {/* Chat Filter Summary */}
      <div className="p-2 border-b border-gray-700 bg-mythos-terminal-background">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-2 text-xs text-mythos-terminal-text-secondary">
            <EldritchIcon name={MythosIcons.clock} size={12} variant="primary" />
            <span>Viewing: {viewingLabel}</span>
          </div>
          <div className="text-xs text-mythos-terminal-text-secondary">
            {chatStats.currentChannelMessages} message{chatStats.currentChannelMessages === 1 ? '' : 's'}
          </div>
        </div>
      </div>

      {/* Chat Messages Display */}
      <div
        className="flex-1 overflow-auto p-3 bg-mythos-terminal-background border border-gray-700 rounded"
        role="log"
        aria-label="Chat Messages"
        style={{ minHeight: '200px' }}
      >
        {filteredMessages.length === 0 ? (
          <div className="flex items-center justify-center h-full">
            <div className="text-center space-y-2">
              <EldritchIcon name={MythosIcons.chat} size={32} variant="secondary" className="mx-auto opacity-50" />
              <p className="text-mythos-terminal-text-secondary text-sm">
                No messages yet. Start chatting to see messages here.
              </p>
            </div>
          </div>
        ) : (
          <div className="space-y-3">
            {filteredMessages.map((message, index) => (
              <div
                key={index}
                className="message p-3 bg-mythos-terminal-surface border border-gray-700 rounded transition-all duration-300 hover:border-mythos-terminal-primary/30 hover:shadow-lg animate-fade-in"
                style={{ animationDelay: `${index * 50}ms` }}
                data-testid="chat-message"
              >
                {/* Alias Expansion Information */}
                {message.aliasChain && message.aliasChain.length > 0 && (
                  <div className="mb-3 p-2 bg-mythos-terminal-background border border-mythos-terminal-primary/50 rounded text-xs">
                    <div className="flex items-center gap-2 mb-2">
                      <EldritchIcon name={MythosIcons.move} size={12} variant="warning" />
                      <span className="text-mythos-terminal-warning font-bold">Alias Expansion:</span>
                    </div>
                    <div className="space-y-1">
                      {message.aliasChain.map((alias, chainIndex) => (
                        <div key={chainIndex} className="flex items-center gap-2">
                          <span className="text-mythos-terminal-warning font-bold">{alias.original}</span>
                          <EldritchIcon name={MythosIcons.exit} size={10} variant="primary" />
                          <span className="text-mythos-terminal-success italic">{alias.expanded}</span>
                        </div>
                      ))}
                    </div>
                  </div>
                )}

                {/* Message Timestamp */}
                <div className="mb-2">
                  <span className="text-xs text-mythos-terminal-text-secondary font-mono">
                    {formatTimestamp(message.timestamp)}
                  </span>
                </div>

                {/* Message Content */}
                <div
                  className={`message-text ${getFontSizeClass()} leading-relaxed ${getMessageClass(
                    message.messageType
                  )}`}
                  data-message-text={message.rawText ?? message.text}
                  onContextMenu={e => {
                    e.preventDefault();
                    // TODO: Implement user ignore functionality
                  }}
                >
                  {message.isHtml ? (
                    <span
                      title="Right-click for options"
                      dangerouslySetInnerHTML={{
                        __html: message.isCompleteHtml ? message.text : ansiToHtmlWithBreaks(message.text),
                      }}
                    />
                  ) : (
                    <span style={{ whiteSpace: 'pre-wrap', wordBreak: 'break-word' }} title="Right-click for options">
                      {message.rawText ?? message.text}
                    </span>
                  )}
                </div>
              </div>
            ))}
          </div>
        )}
      </div>

      {/* Chat Statistics */}
      <div
        className="p-2 border-t border-gray-700 bg-mythos-terminal-surface"
        role="status"
        aria-label="Chat Statistics"
      >
        <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between text-xs text-mythos-terminal-text-secondary gap-2 sm:gap-0">
          <div className="flex flex-wrap items-center gap-2 sm:gap-4">
            <div className="flex items-center gap-1">
              <div className="w-2 h-2 bg-mythos-terminal-success rounded-full"></div>
              <span>Connected</span>
            </div>
            <div className="flex items-center gap-1">
              <EldritchIcon name={MythosIcons.chat} size={12} variant="secondary" />
              <span>{chatStats.currentChannelMessages} messages</span>
            </div>
            <div className="flex items-center gap-1">
              <EldritchIcon name={MythosIcons.connection} size={12} variant="secondary" />
              <span>Channel: {viewingLabel}</span>
            </div>
            <div className="flex items-center gap-1">
              <EldritchIcon name={MythosIcons.clock} size={12} variant="secondary" />
              <span>0 sent</span>
            </div>
            <div className="flex items-center gap-1">
              <div className="w-2 h-2 rounded-full bg-gray-600"></div>
              <span>Activity: none</span>
            </div>
            {Object.values(unreadCounts).reduce((sum, count) => sum + count, 0) > 0 && (
              <div className="flex items-center gap-1">
                <EldritchIcon name={MythosIcons.chat} size={12} variant="error" />
                <span>{Object.values(unreadCounts).reduce((sum, count) => sum + count, 0)} unread</span>
              </div>
            )}
          </div>
          <div className="text-xs opacity-75">MythosMUD Terminal</div>
        </div>
      </div>
    </div>
  );
};
