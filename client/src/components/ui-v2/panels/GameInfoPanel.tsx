import React, { useEffect, useRef, useState } from 'react';
import { ansiToHtmlWithBreaks } from '../../../utils/ansiToHtml';
import { EldritchIcon, MythosIcons } from '../../ui/EldritchIcon';
import { TerminalButton } from '../../ui/TerminalButton';
import type { ChatMessage } from '../types';

interface GameInfoPanelProps {
  messages: ChatMessage[];
  onClearMessages?: () => void;
  onDownloadLogs?: () => void;
}

// Simplified game info panel without search history and time filters
// Based on findings from "Event Logging in Non-Euclidean Systems" - Dr. Armitage, 1928
export const GameInfoPanel: React.FC<GameInfoPanelProps> = ({ messages, onClearMessages, onDownloadLogs }) => {
  const messagesEndRef = useRef<HTMLDivElement>(null);
  const [messageFilter, setMessageFilter] = useState<string>('all');
  const [searchQuery, setSearchQuery] = useState('');

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

  // Filter messages - simplified (no time filter, no search history)
  const filteredMessages = messages.filter(message => {
    // Always exclude chat messages from Game Info Panel - they belong in Chat Panel
    if (message.messageType === 'chat') {
      return false;
    }

    // Apply message type filter
    if (messageFilter !== 'all' && message.messageType !== messageFilter) {
      return false;
    }

    // Apply search filter
    if (searchQuery && !message.text.toLowerCase().includes(searchQuery.toLowerCase())) {
      return false;
    }

    return true;
  });

  return (
    <div className="h-full flex flex-col bg-mythos-terminal-surface border border-gray-700 rounded">
      {/* Header */}
      <div className="flex items-center justify-between p-3 border-b border-gray-700 bg-mythos-terminal-background">
        <div className="flex items-center space-x-2">
          <EldritchIcon name={MythosIcons.log} size={20} className="text-mythos-terminal-primary" />
          <span className="text-sm font-bold text-mythos-terminal-primary">Game Info</span>
        </div>
        <div className="flex items-center space-x-2">
          <TerminalButton
            variant="secondary"
            size="sm"
            onClick={() => {
              setMessageFilter('all');
              setSearchQuery('');
            }}
            className="px-2 py-1 text-xs"
          >
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

      {/* Simplified Filters - Only message type and search */}
      <div className="p-3 border-b border-gray-700 bg-mythos-terminal-background space-y-2">
        <div className="flex space-x-2">
          <select
            value={messageFilter}
            onChange={e => setMessageFilter(e.target.value)}
            className="bg-mythos-terminal-surface border border-gray-600 rounded px-2 py-1 text-xs"
          >
            <option value="all">All Messages</option>
            <option value="system">System</option>
            <option value="emote">Emotes</option>
            <option value="whisper">Whispers</option>
            <option value="shout">Shouts</option>
            <option value="error">Errors</option>
            <option value="combat">Combat</option>
          </select>
          <input
            type="text"
            placeholder="Search messages..."
            value={searchQuery}
            onChange={e => setSearchQuery(e.target.value)}
            className="bg-mythos-terminal-surface border border-gray-600 rounded px-2 py-1 text-xs flex-1"
          />
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
            <div key={index} className="message message-item">
              <div className="flex items-start space-x-2">
                <span className="text-xs text-mythos-terminal-text-secondary flex-shrink-0">
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
    </div>
  );
};
