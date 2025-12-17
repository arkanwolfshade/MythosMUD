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
  // showMessageGroups and setShowMessageGroups removed - not used in current implementation
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
      case 'combat':
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
    // Always exclude chat messages from Game Log Panel - they belong in Chat Panel
    if (message.messageType === 'chat') {
      return false;
    }

    // Apply message type filter
    if (messageFilter !== 'all' && message.messageType !== messageFilter) {
      return false;
    }

    // Apply time filter
    if (timeFilter !== 'all') {
      const messageTime = new Date(message.timestamp);
      const now = new Date();
      const diffMinutes = (now.getTime() - messageTime.getTime()) / (1000 * 60);

      // Handle numeric time filter values (minutes)
      const filterMinutes = parseInt(timeFilter, 10);
      if (!isNaN(filterMinutes)) {
        if (diffMinutes > filterMinutes) return false;
      } else {
        // Handle string time filter values
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
    }

    // Apply search filter
    if (searchQuery && !message.text.toLowerCase().includes(searchQuery.toLowerCase())) {
      return false;
    }

    return true;
  });

  // groupMessagesByTime removed - not used in current implementation
  // TODO: Implement message grouping by time periods

  // messageStats removed - not used in current implementation
  // TODO: Implement message statistics display

  return (
    <div className="game-log-panel h-full flex flex-col bg-mythos-terminal-surface border border-gray-700 rounded">
      {/* Header */}
      <div className="flex items-center justify-between p-3 border-b border-gray-700 bg-mythos-terminal-background">
        <div className="flex items-center space-x-2">
          <EldritchIcon name={MythosIcons.log} size={20} className="text-mythos-terminal-primary" />
          <span className="text-sm font-bold text-mythos-terminal-primary">Game Log</span>
        </div>
        <div className="flex items-center space-x-2">
          <TerminalButton variant="secondary" size="sm" onClick={clearFilters} className="px-2 py-1 text-xs">
            Clear Filters
          </TerminalButton>
          <TerminalButton
            variant="secondary"
            size="sm"
            onClick={() => onClearMessages?.()}
            className="px-2 py-1 text-xs"
          >
            Clear Log
          </TerminalButton>
          <TerminalButton
            variant="secondary"
            size="sm"
            onClick={() => onDownloadLogs?.()}
            className="px-2 py-1 text-xs"
          >
            Download
          </TerminalButton>
        </div>
      </div>

      {/* Filters */}
      <div className="p-3 border-b border-gray-700 bg-mythos-terminal-background space-y-2">
        <div className="flex space-x-2">
          <select
            value={messageFilter}
            onChange={e => {
              setMessageFilter(e.target.value);
            }}
            className="bg-mythos-terminal-surface border border-gray-600 rounded px-2 py-1 text-xs"
          >
            <option value="all">All Messages</option>
            <option value="system">System</option>
            <option value="chat">Chat</option>
            <option value="emote">Emotes</option>
            <option value="whisper">Whispers</option>
            <option value="shout">Shouts</option>
            <option value="error">Errors</option>
            <option value="combat">Combat</option>
          </select>
          <select
            value={timeFilter}
            onChange={e => {
              setTimeFilter(e.target.value);
            }}
            className="bg-mythos-terminal-surface border border-gray-600 rounded px-2 py-1 text-xs"
          >
            <option value="all">All Time</option>
            <option value="5">Last 5 min</option>
            <option value="15">Last 15 min</option>
            <option value="30">Last 30 min</option>
            <option value="60">Last hour</option>
          </select>
        </div>
        <div className="flex space-x-2">
          <input
            type="text"
            placeholder="Search messages..."
            value={searchQuery}
            onChange={e => {
              setSearchQuery(e.target.value);
            }}
            className="bg-mythos-terminal-surface border border-gray-600 rounded px-2 py-1 text-xs flex-1"
          />
          <TerminalButton
            variant="secondary"
            size="sm"
            onClick={() => {
              handleSearch(searchQuery);
            }}
            className="px-2 py-1 text-xs"
          >
            Search
          </TerminalButton>
        </div>
      </div>

      {/* Messages */}
      <div className="flex-1 overflow-y-auto p-3 space-y-2 min-h-[300px]" style={{ minHeight: '300px' }}>
        {filteredMessages.length === 0 ? (
          <div className="text-center text-mythos-terminal-text-secondary py-8">
            <EldritchIcon name={MythosIcons.log} size={32} className="mx-auto mb-2 opacity-50" />
            <p className="text-sm">No messages to display</p>
          </div>
        ) : (
          filteredMessages.map((message, index) => (
            <div key={index} className="message message-item" data-testid="game-log-message">
              <div className="flex items-start space-x-2">
                <span className="text-xs text-mythos-terminal-text-secondary shrink-0">
                  {formatTimestamp(message.timestamp)}
                </span>
                <div className={`flex-1 ${getMessageClass(message.messageType)}`} data-message-text={message.text}>
                  {message.isHtml ? (
                    <div
                      dangerouslySetInnerHTML={{
                        __html: message.isCompleteHtml ? message.text : ansiToHtmlWithBreaks(message.text),
                      }}
                    />
                  ) : (
                    <span>{message.text}</span>
                  )}
                </div>
              </div>
              {message.aliasChain && message.aliasChain.length > 0 && (
                <div className="text-xs text-mythos-terminal-text-secondary ml-4 mt-1">
                  <span>Alias: {message.aliasChain.map(alias => alias.alias_name).join(' → ')}</span>
                </div>
              )}
            </div>
          ))
        )}
        <div ref={messagesEndRef} />
      </div>

      {/* Search History */}
      {showSearchHistory && searchHistory.length > 0 && (
        <div className="border-t border-gray-700 bg-mythos-terminal-background p-3">
          <div className="flex items-center justify-between mb-2">
            <h4 className="text-sm font-bold text-mythos-terminal-primary">Search History</h4>
            <TerminalButton
              variant="secondary"
              size="sm"
              onClick={() => {
                setShowSearchHistory(false);
              }}
              className="px-2 py-1 text-xs"
            >
              Close
            </TerminalButton>
          </div>
          <div className="space-y-1 max-h-24 overflow-y-auto">
            {searchHistory.map((query, index) => (
              <div
                key={index}
                className="text-xs text-mythos-terminal-text-secondary cursor-pointer hover:text-mythos-terminal-text p-1 rounded"
                onClick={() => {
                  setSearchQuery(query);
                  setShowSearchHistory(false);
                }}
              >
                {query}
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
};
