import React, { useEffect, useRef, useState } from 'react';
import { ansiToHtmlWithBreaks } from '../../utils/ansiToHtml';
import { EldritchIcon, MythosIcons } from '../ui/EldritchIcon';
import { TerminalButton } from '../ui/TerminalButton';

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

interface GameLogPanelProps {
  messages: ChatMessage[];
  onClearMessages?: () => void;
  onDownloadLogs?: () => void;
}

export const GameLogPanel: React.FC<GameLogPanelProps> = ({ messages, onClearMessages, onDownloadLogs }) => {
  const messagesEndRef = useRef<HTMLDivElement>(null);
  const [messageFilter, setMessageFilter] = useState<string>('all');
  const [showMessageGroups, setShowMessageGroups] = useState(true);
  const [searchQuery, setSearchQuery] = useState('');
  const [timeFilter, setTimeFilter] = useState<string>('all');
  const [searchHistory, setSearchHistory] = useState<string[]>([]);
  const [showSearchHistory, setShowSearchHistory] = useState(false);

  // Auto-scroll to bottom when new messages arrive
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

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

  const handleSearch = (query: string) => {
    if (query.trim()) {
      setSearchQuery(query);
      // Add to search history
      setSearchHistory(prev => {
        const newHistory = [query, ...prev.filter(item => item !== query)].slice(0, 10);
        return newHistory;
      });
    }
  };

  const clearFilters = () => {
    setMessageFilter('all');
    setTimeFilter('all');
    setSearchQuery('');
  };

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

  // Filter and categorize messages
  const filteredMessages = messages.filter(message => {
    // Apply message type filter
    if (messageFilter !== 'all' && message.messageType !== messageFilter) {
      return false;
    }

    // Apply time filter
    if (timeFilter !== 'all') {
      const messageTime = new Date(message.timestamp);
      const now = new Date();
      const diffMinutes = (now.getTime() - messageTime.getTime()) / (1000 * 60);

      switch (timeFilter) {
        case 'last5min':
          if (diffMinutes > 5) return false;
          break;
        case 'lastHour':
          if (diffMinutes > 60) return false;
          break;
        case 'today':
          if (messageTime.toDateString() !== now.toDateString()) return false;
          break;
        case 'thisWeek': {
          const weekAgo = new Date(now.getTime() - 7 * 24 * 60 * 60 * 1000);
          if (messageTime < weekAgo) return false;
          break;
        }
      }
    }

    // Apply search filter
    if (searchQuery && !message.text.toLowerCase().includes(searchQuery.toLowerCase())) {
      return false;
    }

    return true;
  });

  // Group messages by time periods (last 5 minutes, last hour, etc.)
  const groupMessagesByTime = (messages: ChatMessage[]) => {
    const now = new Date();
    const groups: { [key: string]: ChatMessage[] } = {
      'Last 5 minutes': [],
      'Last hour': [],
      Today: [],
      Earlier: [],
    };

    messages.forEach(message => {
      const messageTime = new Date(message.timestamp);
      const diffMinutes = (now.getTime() - messageTime.getTime()) / (1000 * 60);

      if (diffMinutes <= 5) {
        groups['Last 5 minutes'].push(message);
      } else if (diffMinutes <= 60) {
        groups['Last hour'].push(message);
      } else if (messageTime.toDateString() === now.toDateString()) {
        groups['Today'].push(message);
      } else {
        groups['Earlier'].push(message);
      }
    });

    return groups;
  };

  // Calculate message statistics
  const messageStats = {
    total: messages.length,
    filtered: filteredMessages.length,
    byType: {
      chat: messages.filter(m => m.messageType === 'chat').length,
      system: messages.filter(m => m.messageType === 'system').length,
      error: messages.filter(m => m.messageType === 'error').length,
      emote: messages.filter(m => m.messageType === 'emote').length,
      whisper: messages.filter(m => m.messageType === 'whisper').length,
      shout: messages.filter(m => m.messageType === 'shout').length,
    },
  };

  return (
    <div className="h-full flex flex-col font-mono">
      {/* Game Log Header */}
      <div className="flex items-center justify-between p-3 border-b border-gray-700 bg-mythos-terminal-surface">
        <div className="flex items-center gap-2">
          <EldritchIcon name={MythosIcons.system} size={20} variant="primary" />
          <h3 className="text-mythos-terminal-primary font-bold">Game Log ({messageStats.filtered} messages)</h3>
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

      {/* Filter Controls */}
      <div className="p-3 border-b border-gray-700 bg-mythos-terminal-surface">
        <div className="flex items-center gap-4 flex-wrap">
          <div className="flex items-center gap-2">
            <span className="text-sm text-mythos-terminal-text-secondary">Type:</span>
            <select
              value={messageFilter}
              onChange={e => setMessageFilter(e.target.value)}
              className="bg-mythos-terminal-background border border-gray-700 rounded px-2 py-1 text-xs text-mythos-terminal-text"
            >
              <option value="all">All Messages</option>
              <option value="chat">Chat</option>
              <option value="system">System</option>
              <option value="error">Errors</option>
              <option value="emote">Emotes</option>
              <option value="whisper">Whispers</option>
              <option value="shout">Shouts</option>
            </select>
          </div>
          <div className="flex items-center gap-2">
            <span className="text-sm text-mythos-terminal-text-secondary">Time:</span>
            <select
              value={timeFilter}
              onChange={e => setTimeFilter(e.target.value)}
              className="bg-mythos-terminal-background border border-gray-700 rounded px-2 py-1 text-xs text-mythos-terminal-text"
            >
              <option value="all">All Time</option>
              <option value="last5min">Last 5 min</option>
              <option value="lastHour">Last hour</option>
              <option value="today">Today</option>
              <option value="thisWeek">This week</option>
            </select>
          </div>
          <div className="flex items-center gap-2 relative">
            <span className="text-sm text-mythos-terminal-text-secondary">Search:</span>
            <input
              type="text"
              value={searchQuery}
              onChange={e => setSearchQuery(e.target.value)}
              onKeyDown={e => {
                if (e.key === 'Enter') {
                  handleSearch(searchQuery);
                }
              }}
              placeholder="Search messages..."
              className="bg-mythos-terminal-background border border-gray-700 rounded px-2 py-1 text-xs text-mythos-terminal-text w-32"
            />
            {searchHistory.length > 0 && (
              <TerminalButton
                variant="secondary"
                size="sm"
                onClick={() => setShowSearchHistory(!showSearchHistory)}
                className="flex items-center gap-1 text-xs px-1"
              >
                <EldritchIcon name={MythosIcons.clock} size={10} variant="primary" />
              </TerminalButton>
            )}
            {showSearchHistory && searchHistory.length > 0 && (
              <div className="absolute top-full left-0 mt-1 bg-mythos-terminal-surface border border-gray-700 rounded shadow-lg z-10 min-w-[200px]">
                {searchHistory.map((query, index) => (
                  <div
                    key={index}
                    className="px-3 py-2 hover:bg-mythos-terminal-background cursor-pointer text-xs"
                    onClick={() => {
                      setSearchQuery(query);
                      setShowSearchHistory(false);
                    }}
                  >
                    <span className="text-mythos-terminal-primary">{query}</span>
                  </div>
                ))}
              </div>
            )}
          </div>
          <TerminalButton
            variant="secondary"
            size="sm"
            onClick={clearFilters}
            className="flex items-center gap-2 text-xs"
          >
            <EldritchIcon name={MythosIcons.clear} size={12} variant="error" />
            <span>Clear</span>
          </TerminalButton>
          <TerminalButton
            variant="secondary"
            size="sm"
            onClick={() => setShowMessageGroups(!showMessageGroups)}
            className="flex items-center gap-2 text-xs"
          >
            <EldritchIcon name={MythosIcons.move} size={12} variant="primary" />
            <span>{showMessageGroups ? 'Hide' : 'Show'} Groups</span>
          </TerminalButton>
        </div>
      </div>

      {/* Game Messages Display */}
      <div className="flex-1 overflow-auto p-3 bg-mythos-terminal-background border border-gray-700 rounded">
        {filteredMessages.length === 0 ? (
          <div className="flex items-center justify-center h-full">
            <div className="text-center space-y-2">
              <EldritchIcon name={MythosIcons.system} size={32} variant="secondary" className="mx-auto opacity-50" />
              <p className="text-mythos-terminal-text-secondary text-sm">
                {messages.length === 0
                  ? 'No game events yet. Connect to the game to see activity.'
                  : 'No messages match the current filter.'}
              </p>
            </div>
          </div>
        ) : (
          <div className="space-y-3">
            {showMessageGroups
              ? // Grouped messages
                Object.entries(groupMessagesByTime(filteredMessages)).map(([groupName, groupMessages]) => {
                  if (groupMessages.length === 0) return null;
                  return (
                    <div key={groupName} className="space-y-2">
                      <div className="flex items-center gap-2 p-2 bg-mythos-terminal-surface border border-gray-700 rounded">
                        <EldritchIcon name={MythosIcons.clock} size={12} variant="primary" />
                        <span className="text-xs text-mythos-terminal-primary font-bold">
                          {groupName} ({groupMessages.length})
                        </span>
                      </div>
                      <div className="space-y-2 ml-4">
                        {groupMessages.map((message, index) => (
                          <div
                            key={index}
                            className="p-3 bg-mythos-terminal-surface border border-gray-700 rounded transition-all duration-200 hover:border-mythos-terminal-primary/30"
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
                              className={`text-sm leading-relaxed ${getMessageClass(message.messageType)}`}
                              dangerouslySetInnerHTML={{
                                __html: message.isHtml
                                  ? message.isCompleteHtml
                                    ? message.text
                                    : ansiToHtmlWithBreaks(message.text)
                                  : message.text,
                              }}
                            />
                          </div>
                        ))}
                      </div>
                    </div>
                  );
                })
              : // Ungrouped messages
                filteredMessages.map((message, index) => (
                  <div
                    key={index}
                    className="p-3 bg-mythos-terminal-surface border border-gray-700 rounded transition-all duration-200 hover:border-mythos-terminal-primary/30"
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
                      className={`text-sm leading-relaxed ${getMessageClass(message.messageType)}`}
                      dangerouslySetInnerHTML={{
                        __html: message.isHtml
                          ? message.isCompleteHtml
                            ? message.text
                            : ansiToHtmlWithBreaks(message.text)
                          : message.text,
                      }}
                    />
                  </div>
                ))}
            <div ref={messagesEndRef} />
          </div>
        )}
      </div>

      {/* Game Log Statistics */}
      <div className="p-2 border-t border-gray-700 bg-mythos-terminal-surface">
        <div className="flex items-center justify-between text-xs text-mythos-terminal-text-secondary">
          <div className="flex items-center gap-4">
            <div className="flex items-center gap-1">
              <div className="w-2 h-2 bg-mythos-terminal-success rounded-full"></div>
              <span>Connected</span>
            </div>
            <div className="flex items-center gap-1">
              <EldritchIcon name={MythosIcons.system} size={12} variant="secondary" />
              <span>
                {messageStats.filtered}/{messageStats.total} messages
              </span>
            </div>
            <div className="flex items-center gap-1">
              <EldritchIcon name={MythosIcons.chat} size={12} variant="secondary" />
              <span>
                C:{messageStats.byType.chat} S:{messageStats.byType.system} E:{messageStats.byType.error}
              </span>
            </div>
          </div>
          <div className="text-xs opacity-75">MythosMUD Terminal</div>
        </div>
      </div>
    </div>
  );
};
