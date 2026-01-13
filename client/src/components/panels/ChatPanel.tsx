import React, { useEffect, useMemo, useState } from 'react';
import {
  ALL_MESSAGES_CHANNEL,
  AVAILABLE_CHANNELS,
  CHAT_CHANNEL_OPTIONS,
  DEFAULT_CHANNEL,
  getChannelById,
} from '../../config/channels';
import { ansiToHtmlWithBreaks } from '../../utils/ansiToHtml';
import { extractChannelFromMessage, isChatContent } from '../../utils/messageTypeUtils';
import { SafeHtml } from '../common/SafeHtml';
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
  tags?: string[];
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
  selectedChannel,
  onChannelSelect,
}) => {
  const [clearedChannels, setClearedChannels] = useState<Record<string, number>>({});
  const [isHistoryVisible, setIsHistoryVisible] = useState(false);
  const [currentChannel, setCurrentChannel] = useState<string>(selectedChannel ?? ALL_MESSAGES_CHANNEL.id);
  const [searchQuery, setSearchQuery] = useState<string>('');
  const [searchFilterChannel, setSearchFilterChannel] = useState<string>('all');
  const [searchFilterType, setSearchFilterType] = useState<string>('all');
  const [currentSearchIndex, setCurrentSearchIndex] = useState<number>(-1);
  const [showExportDialog, setShowExportDialog] = useState<boolean>(false);
  const [exportFormat, setExportFormat] = useState<string>('txt');
  const [isExporting, setIsExporting] = useState<boolean>(false);

  // Sync selectedChannel prop to internal state when prop changes
  // This enables controlled mode (prop-driven) while maintaining uncontrolled mode (user-initiated changes)
  useEffect(() => {
    if (selectedChannel !== undefined) {
      // Sync local state with prop changes, controlled mode requires state update when prop changes
      // eslint-disable-next-line react-hooks/set-state-in-effect
      setCurrentChannel(prev => (prev === selectedChannel ? prev : selectedChannel));
    }
  }, [selectedChannel]);

  const normalizedSelectedChannel = currentChannel ?? DEFAULT_CHANNEL;
  const isAllChannelSelected = normalizedSelectedChannel === ALL_MESSAGES_CHANNEL.id;

  const filteredMessages = useMemo(() => {
    return messages.filter(message => {
      if (message.channel === 'game-log') {
        return false;
      }

      if (message.messageType === 'system') {
        return false;
      }

      // Exclude combat messages - they belong in Game Info panel only
      if (message.messageType === 'combat') {
        return false;
      }

      if (isAllChannelSelected) {
        return true;
      }

      if (message.messageType === 'command') {
        return false;
      }

      const messageChannel = message.channel || extractChannelFromMessage(message.text) || 'local';

      if (message.messageType === 'error') {
        return messageChannel === normalizedSelectedChannel;
      }

      const isChatMessage = message.messageType === 'chat' || isChatContent(message.text);
      if (!isChatMessage) {
        return false;
      }

      if (messageChannel === 'whisper') {
        return normalizedSelectedChannel === 'whisper';
      }

      return messageChannel === normalizedSelectedChannel;
    });
  }, [messages, normalizedSelectedChannel, isAllChannelSelected]);

  const historyEligibleMessages = useMemo(
    () => messages.filter(message => message.messageType !== 'system'),
    [messages]
  );

  // Search and filter logic
  const searchFilteredMessages = useMemo(() => {
    let baseMessages = isHistoryVisible ? historyEligibleMessages : filteredMessages;

    // Apply search query
    if (searchQuery.trim()) {
      const query = searchQuery.toLowerCase();
      baseMessages = baseMessages.filter(message => {
        const text = (message.rawText ?? message.text).toLowerCase();
        return text.includes(query);
      });
    }

    // Apply channel filter
    if (searchFilterChannel !== 'all') {
      baseMessages = baseMessages.filter(message => {
        const messageChannel = message.channel || extractChannelFromMessage(message.text) || 'local';
        return messageChannel === searchFilterChannel;
      });
    }

    // Apply message type filter
    if (searchFilterType !== 'all') {
      baseMessages = baseMessages.filter(message => {
        return message.messageType === searchFilterType;
      });
    }

    return baseMessages;
  }, [filteredMessages, historyEligibleMessages, isHistoryVisible, searchQuery, searchFilterChannel, searchFilterType]);

  // Find search matches for highlighting
  const searchMatches = useMemo(() => {
    if (!searchQuery.trim()) {
      return new Set<number>();
    }
    const query = searchQuery.toLowerCase();
    const matches = new Set<number>();
    searchFilteredMessages.forEach((message, index) => {
      const text = (message.rawText ?? message.text).toLowerCase();
      if (text.includes(query)) {
        matches.add(index);
      }
    });
    return matches;
  }, [searchFilteredMessages, searchQuery]);

  const visibleMessages = searchFilteredMessages;

  const chatStats = {
    currentChannelMessages: filteredMessages.length,
    totalMessages: historyEligibleMessages.length,
  };

  const unreadCounts = useMemo(() => {
    if (isAllChannelSelected) {
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
  }, [messages, normalizedSelectedChannel, clearedChannels, isAllChannelSelected]);

  const handleChannelSelect = (channelId: string) => {
    setCurrentChannel(channelId);
    if (channelId === ALL_MESSAGES_CHANNEL.id) {
      setClearedChannels({});
    } else {
      setClearedChannels(prev => ({ ...prev, [channelId]: historyEligibleMessages.length }));
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
      // Use UTC methods to ensure consistent formatting regardless of timezone
      const hours = date.getUTCHours().toString().padStart(2, '0');
      const minutes = date.getUTCMinutes().toString().padStart(2, '0');
      const seconds = date.getUTCSeconds().toString().padStart(2, '0');
      return `${hours}:${minutes}:${seconds}`;
    } catch {
      return timestamp;
    }
  };

  const getMessageClass = (message: ChatMessage): string => {
    if (message.tags?.includes('hallucination')) {
      return 'text-fuchsia-300 italic';
    }

    if (message.tags?.includes('command-misfire')) {
      return 'text-mythos-terminal-warning font-semibold';
    }

    if (message.tags?.includes('rescue')) {
      return 'text-mythos-terminal-primary font-semibold';
    }

    switch (message.messageType) {
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
    setCurrentSearchIndex(-1);
  };

  const handleSearchNext = () => {
    if (searchMatches.size === 0) return;
    const matches = Array.from(searchMatches).sort((a, b) => a - b);
    const nextIndex = matches.findIndex(idx => idx > currentSearchIndex);
    if (nextIndex >= 0) {
      setCurrentSearchIndex(matches[nextIndex]);
    } else {
      setCurrentSearchIndex(matches[0]); // Wrap around
    }
  };

  const handleSearchPrevious = () => {
    if (searchMatches.size === 0) return;
    const matches = Array.from(searchMatches).sort((a, b) => b - a);
    const prevIndex = matches.findIndex(idx => idx < currentSearchIndex);
    if (prevIndex >= 0) {
      setCurrentSearchIndex(matches[prevIndex]);
    } else {
      setCurrentSearchIndex(matches[0]); // Wrap around
    }
  };

  const handleSearchChange = (query: string) => {
    setSearchQuery(query);
    setCurrentSearchIndex(-1);
  };

  // Export functions
  const exportToText = (messagesToExport: ChatMessage[]): string => {
    return messagesToExport
      .map(msg => {
        const timestamp = formatTimestamp(msg.timestamp);
        const text = msg.rawText ?? msg.text;
        return `[${timestamp}] ${text}`;
      })
      .join('\n');
  };

  const exportToHTML = (messagesToExport: ChatMessage[]): string => {
    const htmlMessages = messagesToExport
      .map(msg => {
        const timestamp = formatTimestamp(msg.timestamp);
        const text = msg.isHtml
          ? msg.isCompleteHtml
            ? msg.text
            : ansiToHtmlWithBreaks(msg.text)
          : (msg.rawText ?? msg.text).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
        const messageClass = getMessageClass(msg);
        return `<div class="message" style="margin-bottom: 1em;">
          <div style="font-size: 0.8em; color: #888;">[${timestamp}]</div>
          <div class="${messageClass}">${text}</div>
        </div>`;
      })
      .join('\n');
    return `<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Chat Export</title>
  <style>
    body { font-family: monospace; background: #1a1a1a; color: #e0e0e0; padding: 20px; }
    .message { padding: 10px; border-bottom: 1px solid #333; }
  </style>
</head>
<body>
  <h1>Chat Export</h1>
  ${htmlMessages}
</body>
</html>`;
  };

  const exportToJSON = (messagesToExport: ChatMessage[]): string => {
    return JSON.stringify(
      messagesToExport.map(msg => ({
        timestamp: msg.timestamp,
        text: msg.rawText ?? msg.text,
        channel: msg.channel,
        messageType: msg.messageType,
        tags: msg.tags,
      })),
      null,
      2
    );
  };

  const exportToCSV = (messagesToExport: ChatMessage[]): string => {
    const headers = ['Timestamp', 'Channel', 'Type', 'Message'];
    const rows = messagesToExport.map(msg => {
      const timestamp = formatTimestamp(msg.timestamp);
      const text = (msg.rawText ?? msg.text).replace(/"/g, '""'); // Escape quotes for CSV
      return `"${timestamp}","${msg.channel || ''}","${msg.messageType || ''}","${text}"`;
    });
    return [headers.map(h => `"${h}"`).join(','), ...rows].join('\n');
  };

  const handleExport = () => {
    if (isExporting) return;

    setIsExporting(true);
    const messagesToExport = visibleMessages;

    let content: string;
    let filename: string;
    let mimeType: string;

    switch (exportFormat) {
      case 'html':
        content = exportToHTML(messagesToExport);
        filename = `chat_export_${new Date().toISOString().split('T')[0]}.html`;
        mimeType = 'text/html';
        break;
      case 'json':
        content = exportToJSON(messagesToExport);
        filename = `chat_export_${new Date().toISOString().split('T')[0]}.json`;
        mimeType = 'application/json';
        break;
      case 'csv':
        content = exportToCSV(messagesToExport);
        filename = `chat_export_${new Date().toISOString().split('T')[0]}.csv`;
        mimeType = 'text/csv';
        break;
      case 'txt':
      default:
        content = exportToText(messagesToExport);
        filename = `chat_export_${new Date().toISOString().split('T')[0]}.txt`;
        mimeType = 'text/plain';
        break;
    }

    // Create blob and download
    const blob = new Blob([content], { type: mimeType });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = filename;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    URL.revokeObjectURL(url);

    setTimeout(() => {
      setIsExporting(false);
      setShowExportDialog(false);
    }, 500);
  };

  // Highlight search term in text (plain text only, not for HTML)
  const highlightSearchText = (text: string, query: string): string => {
    if (!query.trim()) return text;

    // Limit query length to prevent ReDoS attacks (pure operation, safe for render)
    const MAX_QUERY_LENGTH = 100;
    if (query.length > MAX_QUERY_LENGTH) {
      console.warn('Query length exceeds maximum, truncating for safety');
      query = query.substring(0, MAX_QUERY_LENGTH);
    }

    // Escape HTML entities first
    const escapedText = text
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');

    // Escape regex special characters in query to prevent ReDoS
    // All regex metacharacters are escaped: . * + ? ^ $ { } ( ) | [ ] \
    // This converts the query into a literal string match, preventing regex injection
    // After escaping, escapedQuery contains only literal characters or escaped metacharacters
    const escapedQuery = query.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');

    // Create regex for highlighting
    // SAFETY MEASURES FOR REGEXP CONSTRUCTOR:
    // 1. Query length is limited to MAX_QUERY_LENGTH (100 chars) to prevent ReDoS
    // 2. All regex metacharacters are escaped via .replace() above, converting user input to literal match
    // 3. escapedQuery can only contain: literal characters (a-z, 0-9, etc.) or escaped sequences (\., \*, etc.)
    // 4. No dangerous regex patterns can be constructed after escaping
    // This pattern is safe because the escaped query is treated as a literal string, not a regex pattern
    // nosemgrep: typescript.lang.security.audit.detect-non-literal-regexp.detect-non-literal-regexp
    const regex = new RegExp(`(${escapedQuery})`, 'gi');
    // nosemgrep: typescript.lang.security.audit.detect-non-literal-regexp.detect-non-literal-regexp
    // nosemgrep: typescript.lang.security.audit.xss.xss
    const result = escapedText.replace(regex, '<mark class="bg-yellow-500 text-black font-semibold">$1</mark>');

    return result;
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
        <div className="flex items-center gap-2 flex-wrap">
          <button className="text-xs text-mythos-terminal-primary" onClick={toggleHistory} type="button">
            Chat History
          </button>
          <select
            className="text-xs bg-mythos-terminal-surface border border-gray-700 rounded px-1"
            value={isHistoryVisible ? 'all' : 'current'}
            onChange={event => {
              setIsHistoryVisible(event.target.value === 'all');
            }}
          >
            <option value="current">Current</option>
            <option value="all">All</option>
          </select>
          <span className="text-xs text-mythos-terminal-text-secondary">
            Messages: {visibleMessages.length} /{' '}
            {isHistoryVisible ? historyEligibleMessages.length : filteredMessages.length}
          </span>
        </div>

        {/* Search Controls */}
        <div className="mt-2 flex items-center gap-2 flex-wrap">
          <div className="flex items-center gap-1 flex-1 min-w-[200px]">
            <EldritchIcon name={MythosIcons.search} size={14} variant="primary" />
            <input
              type="text"
              placeholder="Search messages..."
              value={searchQuery}
              onChange={e => {
                handleSearchChange(e.target.value);
              }}
              className="flex-1 text-xs bg-mythos-terminal-surface border border-gray-700 rounded px-2 py-1 text-mythos-terminal-text focus:outline-none focus:border-mythos-terminal-primary"
              disabled={disabled}
            />
            {searchQuery && (
              <>
                <button
                  onClick={handleSearchPrevious}
                  disabled={searchMatches.size === 0}
                  className="text-xs px-2 py-1 bg-mythos-terminal-surface border border-gray-700 rounded hover:bg-mythos-terminal-background disabled:opacity-50"
                  title="Previous match"
                  type="button"
                >
                  ↑
                </button>
                <button
                  onClick={handleSearchNext}
                  disabled={searchMatches.size === 0}
                  className="text-xs px-2 py-1 bg-mythos-terminal-surface border border-gray-700 rounded hover:bg-mythos-terminal-background disabled:opacity-50"
                  title="Next match"
                  type="button"
                >
                  ↓
                </button>
                <button
                  onClick={() => {
                    handleSearchChange('');
                  }}
                  className="text-xs px-2 py-1 bg-mythos-terminal-surface border border-gray-700 rounded hover:bg-mythos-terminal-background"
                  title="Clear search"
                  type="button"
                >
                  ×
                </button>
                {searchMatches.size > 0 && (
                  <span className="text-xs text-mythos-terminal-text-secondary">
                    {Array.from(searchMatches).findIndex(idx => idx === currentSearchIndex) + 1 || 0} /{' '}
                    {searchMatches.size}
                  </span>
                )}
              </>
            )}
          </div>
          {searchQuery && (
            <>
              <select
                value={searchFilterChannel}
                onChange={e => {
                  setSearchFilterChannel(e.target.value);
                }}
                className="text-xs bg-mythos-terminal-surface border border-gray-700 rounded px-1"
                disabled={disabled}
              >
                <option value="all">All Channels</option>
                {AVAILABLE_CHANNELS.map(channel => (
                  <option key={channel.id} value={channel.id}>
                    {channel.name}
                  </option>
                ))}
              </select>
              <select
                value={searchFilterType}
                onChange={e => {
                  setSearchFilterType(e.target.value);
                }}
                className="text-xs bg-mythos-terminal-surface border border-gray-700 rounded px-1"
                disabled={disabled}
              >
                <option value="all">All Types</option>
                <option value="chat">Chat</option>
                <option value="whisper">Whisper</option>
                <option value="emote">Emote</option>
                <option value="error">Error</option>
              </select>
            </>
          )}
        </div>
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
        {visibleMessages.length === 0 ? (
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
            {visibleMessages.map((message, index) => (
              <div
                key={index}
                className={
                  `message p-3 bg-mythos-terminal-surface border rounded transition-all duration-300 ` +
                  `hover:border-mythos-terminal-primary/30 hover:shadow-lg animate-fade-in ${
                    currentSearchIndex === index && searchQuery
                      ? 'border-mythos-terminal-warning border-2 shadow-lg shadow-mythos-terminal-warning/50'
                      : 'border-gray-700'
                  }`
                }
                style={{ animationDelay: `${index * 50}ms` }}
                data-testid="chat-message"
                ref={(el: HTMLDivElement | null) => {
                  if (currentSearchIndex === index && el) {
                    el.scrollIntoView({ behavior: 'smooth', block: 'center' });
                  }
                }}
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
                  className={`message-text ${getFontSizeClass()} leading-relaxed ${getMessageClass(message)}`}
                  data-message-text={message.rawText ?? message.text}
                  onContextMenu={e => {
                    e.preventDefault();
                    // TODO: Implement user ignore functionality
                  }}
                >
                  {message.isHtml ? (
                    <SafeHtml
                      html={message.isCompleteHtml ? message.text : ansiToHtmlWithBreaks(message.text)}
                      title="Right-click for options"
                    />
                  ) : (
                    <SafeHtml
                      html={
                        searchQuery
                          ? highlightSearchText(message.rawText ?? message.text, searchQuery)
                          : (message.rawText ?? message.text)
                              .replace(/&/g, '&amp;')
                              .replace(/</g, '&lt;')
                              .replace(/>/g, '&gt;')
                              .replace(/"/g, '&quot;')
                              .replace(/'/g, '&#39;')
                      }
                      title="Right-click for options"
                      style={{ whiteSpace: 'pre-wrap', wordBreak: 'break-word' }}
                    />
                  )}
                </div>
              </div>
            ))}
          </div>
        )}
      </div>

      {/* Export Dialog */}
      {showExportDialog && (
        <div
          className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50"
          onClick={() => !isExporting && setShowExportDialog(false)}
        >
          <div
            className="bg-mythos-terminal-surface border border-mythos-terminal-primary rounded-lg p-6 max-w-md w-full"
            onClick={e => {
              e.stopPropagation();
            }}
          >
            <h3 className="text-mythos-terminal-primary font-bold text-lg mb-4">Export Chat Messages</h3>
            <div className="space-y-4">
              <div>
                <label className="block text-sm text-mythos-terminal-text-secondary mb-2">Export Format</label>
                <select
                  value={exportFormat}
                  onChange={e => {
                    setExportFormat(e.target.value);
                  }}
                  className="w-full text-sm bg-mythos-terminal-background border border-gray-700 rounded px-2 py-1 text-mythos-terminal-text"
                  disabled={isExporting}
                >
                  <option value="txt">Plain Text (.txt)</option>
                  <option value="html">HTML (.html)</option>
                  <option value="json">JSON (.json)</option>
                  <option value="csv">CSV (.csv)</option>
                </select>
              </div>
              <div className="text-xs text-mythos-terminal-text-secondary">
                Exporting {visibleMessages.length} message{visibleMessages.length === 1 ? '' : 's'}
              </div>
              <div className="flex gap-2 justify-end">
                <button
                  onClick={() => {
                    setShowExportDialog(false);
                  }}
                  disabled={isExporting}
                  className="px-4 py-2 text-sm bg-mythos-terminal-background border border-gray-700 rounded hover:bg-mythos-terminal-surface disabled:opacity-50"
                  type="button"
                >
                  Cancel
                </button>
                <button
                  onClick={handleExport}
                  disabled={isExporting || visibleMessages.length === 0}
                  className="px-4 py-2 text-sm bg-mythos-terminal-primary text-black rounded hover:bg-mythos-terminal-primary/80 disabled:opacity-50 font-bold"
                  type="button"
                >
                  {isExporting ? 'Exporting...' : 'Export'}
                </button>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};
