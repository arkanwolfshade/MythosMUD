import React, { useEffect, useState } from 'react';
import { AVAILABLE_CHANNELS, DEFAULT_CHANNEL } from '../../config/channels';
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
  selectedChannel = DEFAULT_CHANNEL,
  onChannelSelect,
}) => {
  const [showChatHistory, setShowChatHistory] = useState(false);
  const [chatFilter, setChatFilter] = useState<string>('current');
  const [unreadCounts, setUnreadCounts] = useState<Record<string, number>>({});

  // Calculate chat statistics
  const chatStats = {
    currentChannelMessages: messages.filter(message => {
      const messageChannel = message.channel || extractChannelFromMessage(message.text) || selectedChannel;
      return messageChannel === selectedChannel;
    }).length,
    totalMessages: messages.length,
  };

  // Update unread counts
  useEffect(() => {
    setUnreadCounts(prev => {
      const newUnreadCounts = { ...prev };

      messages.forEach(message => {
        // Handle both 'chat' and 'command' messages that contain chat content
        if (message.messageType === 'chat' || (message.messageType === 'command' && isChatContent(message.text))) {
          const channelId = message.channel || extractChannelFromMessage(message.text) || selectedChannel;
          // Increment unread count for other channels
          if (channelId !== selectedChannel) {
            newUnreadCounts[channelId] = (newUnreadCounts[channelId] || 0) + 1;
          }
        }
      });

      return newUnreadCounts;
    });
  }, [messages, selectedChannel]);

  // Filter messages - simplified for display only
  const getFilteredMessages = () => {
    return messages;
  };

  const handleChannelSelect = (channelId: string) => {
    // Clear unread count when switching to a channel
    setUnreadCounts(prev => ({ ...prev, [channelId]: 0 }));
    onChannelSelect?.(channelId);
  };

  // Filter messages by channel and moderation settings
  const filteredMessages = getFilteredMessages().filter(message => {
    // Always exclude system messages from Chat Panel - they belong in Game Log Panel
    if (message.messageType === 'system') {
      return false;
    }

    if (chatFilter === 'all') return true;
    if (chatFilter === 'current') {
      // Filter for current channel messages - handle both 'chat' and 'command' messages with chat content
      const isChatMessage =
        message.messageType === 'chat' || (message.messageType === 'command' && isChatContent(message.text));

      // If it's a chat message, also check if it belongs to the current channel
      if (isChatMessage) {
        const messageChannel = message.channel || extractChannelFromMessage(message.text) || 'local';
        return messageChannel === selectedChannel;
      }

      return false;
    }
    return true;
  });

  // Debug logging for final filtered messages
  console.log('🔍 ChatPanel Final Filtered Messages:', {
    totalMessages: messages.length,
    filteredCount: filteredMessages.length,
    chatFilter,
    selectedChannel,
    filteredMessages: filteredMessages.map(m => ({
      text: m.text.substring(0, 50) + (m.text.length > 50 ? '...' : ''),
      messageType: m.messageType,
      channel: m.channel,
      timestamp: m.timestamp,
    })),
    timestamp: new Date().toISOString(),
  });

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
            channels={AVAILABLE_CHANNELS}
            selectedChannel={selectedChannel}
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
                    className={`w-2 h-2 rounded-full ${getActivityColor(activityLevel)} transition-all duration-300 ${activityLevel === 'high' ? 'animate-pulse' : ''}`}
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
      <div className="p-2 border-b border-gray-700 bg-mythos-terminal-background">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-2">
            <TerminalButton
              variant="secondary"
              size="sm"
              onClick={() => setShowChatHistory(!showChatHistory)}
              className="flex items-center gap-2 text-xs"
            >
              <EldritchIcon name={MythosIcons.clock} size={12} variant="primary" />
              <span>Chat History</span>
            </TerminalButton>
            <select
              value={chatFilter}
              onChange={e => setChatFilter(e.target.value)}
              className="bg-mythos-terminal-surface border border-gray-700 rounded px-2 py-1 text-xs text-mythos-terminal-text"
            >
              <option value="all">All Messages</option>
              <option value="current">Current Channel</option>
            </select>
          </div>
          <div className="text-xs text-mythos-terminal-text-secondary">{chatStats.currentChannelMessages} messages</div>
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
                className="p-3 bg-mythos-terminal-surface border border-gray-700 rounded transition-all duration-300 hover:border-mythos-terminal-primary/30 hover:shadow-lg animate-fade-in"
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
                  className={`${getFontSizeClass()} leading-relaxed ${getMessageClass(message.messageType)}`}
                  dangerouslySetInnerHTML={{
                    __html: message.isHtml
                      ? message.isCompleteHtml
                        ? message.text
                        : ansiToHtmlWithBreaks(message.text)
                      : message.text,
                  }}
                  onContextMenu={e => {
                    e.preventDefault();
                    const username = message.aliasChain?.[0]?.original.split(' ')[0];
                    if (username && !isUserIgnored(username)) {
                      if (confirm(`Ignore messages from ${username}?`)) {
                        addIgnoredUser(username);
                      }
                    }
                  }}
                  title="Right-click to ignore user"
                />
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
              <span>Channel: {AVAILABLE_CHANNELS.find(c => c.id === selectedChannel)?.name}</span>
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
