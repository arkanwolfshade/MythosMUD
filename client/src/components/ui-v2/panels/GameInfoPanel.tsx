import React, { useEffect, useRef, useState } from 'react';
import { SafeHtml } from '../../common/SafeHtml';
import { SegmentedText } from '../components/SegmentedText';
import { EldritchIcon, MythosIcons, TerminalButton } from '../primitives';
import type { ChatMessage } from '../types';
import { getMessageCategoryClass } from '../utils/messageCategoryStyle';

interface GameInfoPanelProps {
  messages: ChatMessage[];
  onClearMessages?: () => void;
  onDownloadLogs?: () => void;
  /** Server flag: show combat strip in header (frame also uses PanelContainer className). */
  inCombat?: boolean;
}

/** Room-scoped chat categories mirrored in Game Info so E2E and players see cross-player delivery. */
const GAME_INFO_CHAT_CATEGORIES: ReadonlySet<string> = new Set(['chat.say', 'chat.local', 'chat.party']);

/** Category routing: every category shows in Game Info except chat.*, of which only say/local/party are mirrored. */
function categoryVisibleInGameInfo(category: string): boolean {
  return !category.startsWith('chat.') || GAME_INFO_CHAT_CATEGORIES.has(category);
}

/** Dropdown filter: one entry per category domain (the part before the dot). */
const MESSAGE_FILTERS: ReadonlyArray<{ value: string; label: string }> = [
  { value: 'all', label: 'All Messages' },
  { value: 'combat', label: 'Combat' },
  { value: 'status', label: 'Status' },
  { value: 'system', label: 'System' },
  { value: 'room', label: 'Room' },
  { value: 'chat', label: 'Chat' },
  { value: 'command', label: 'Commands' },
];

// Simplified game info panel without search history and time filters
// Based on findings from "Event Logging in Non-Euclidean Systems" - Dr. Armitage, 1928
export const GameInfoPanel: React.FC<GameInfoPanelProps> = ({
  messages,
  onClearMessages,
  onDownloadLogs,
  inCombat = false,
}) => {
  const messagesEndRef = useRef<HTMLDivElement>(null);
  const [messageFilter, setMessageFilter] = useState<string>('all');
  const [searchQuery, setSearchQuery] = useState('');

  // Auto-scroll to bottom when new messages arrive
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

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
    // Exclude chat from Game Info except room-scoped categories (E2E asserts on [data-message-text] here).
    if (!categoryVisibleInGameInfo(message.category)) return false;

    // Apply category-domain filter
    if (messageFilter !== 'all' && message.category.split('.')[0] !== messageFilter) {
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
      <div
        className={`flex items-center justify-between p-3 border-b border-gray-700 bg-mythos-terminal-background ${
          inCombat ? 'border-b-orange-500/50' : ''
        }`}
      >
        <div className="flex items-center space-x-2">
          <EldritchIcon name={MythosIcons.log} size={20} className="text-mythos-terminal-primary" />
          {inCombat && (
            <span
              data-testid="game-info-combat-indicator"
              className="w-2 h-2 shrink-0 rounded-full bg-orange-500"
              aria-hidden="true"
            />
          )}
          <span className="text-sm font-bold text-mythos-terminal-primary">Game Info</span>
          {inCombat && (
            <span
              className="text-xs font-semibold uppercase tracking-wide text-orange-400"
              data-testid="game-info-combat-label"
            >
              In combat
            </span>
          )}
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

      {/* Simplified Filters - Only category domain and search */}
      <div className="p-3 border-b border-gray-700 bg-mythos-terminal-background space-y-2">
        <div className="flex space-x-2">
          <select
            value={messageFilter}
            onChange={e => {
              setMessageFilter(e.target.value);
            }}
            className="bg-mythos-terminal-surface border border-gray-600 rounded px-2 py-1 text-xs"
          >
            {MESSAGE_FILTERS.map(filter => (
              <option key={filter.value} value={filter.value}>
                {filter.label}
              </option>
            ))}
          </select>
          <input
            type="text"
            placeholder="Search messages..."
            value={searchQuery}
            onChange={e => {
              setSearchQuery(e.target.value);
            }}
            className="bg-mythos-terminal-surface border border-gray-600 rounded px-2 py-1 text-xs flex-1"
          />
        </div>
      </div>

      {/* Messages */}
      <div className="flex-1 overflow-y-auto p-3 space-y-2 min-h-panel-md" style={{ minHeight: '300px' }}>
        {filteredMessages.length === 0 ? (
          <div className="text-center text-mythos-terminal-text-secondary py-8">
            <EldritchIcon name={MythosIcons.log} size={32} className="mx-auto mb-2 opacity-50" />
            <p className="text-sm">No messages to display</p>
          </div>
        ) : (
          filteredMessages.map((message, index) => (
            <div key={index} className="message message-item">
              <div className="flex items-start space-x-2">
                <span className="text-xs text-mythos-terminal-text-secondary shrink-0">
                  {formatTimestamp(message.timestamp)}
                </span>
                <div
                  className={`flex-1 ${getMessageCategoryClass(message.category) ?? 'text-mythos-terminal-text'}`}
                  data-message-text={message.text}
                >
                  {message.isHtml ? (
                    <SafeHtml html={message.text} tag="div" />
                  ) : (
                    <span style={{ whiteSpace: 'pre-wrap' }}>
                      {message.segments ? <SegmentedText segments={message.segments} /> : message.text}
                    </span>
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
