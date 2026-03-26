import React from 'react';
import { EldritchIcon, MythosIcons } from '../ui/EldritchIcon';
import { TerminalButton } from '../ui/TerminalButton';
import {
  getGameLogMessageFilterSelectClassName,
  getGameLogSearchInputClassName,
  getGameLogTimeFilterSelectClassName,
} from './gameLogPanelUtils';

interface GameLogPanelHeaderProps {
  onClearFilters: () => void;
  onClearMessages?: () => void;
  onDownloadLogs?: () => void;
}

export const GameLogPanelHeader: React.FC<GameLogPanelHeaderProps> = ({
  onClearFilters,
  onClearMessages,
  onDownloadLogs,
}) => (
  <div className="flex items-center justify-between gap-3 border-b border-mythos-terminal-primary/25 bg-linear-to-r from-mythos-terminal-primary/[0.07] via-mythos-terminal-background to-mythos-terminal-background px-3 py-3">
    <div className="flex min-w-0 items-center gap-3">
      <span className="hidden h-10 w-1 shrink-0 rounded-sm bg-mythos-terminal-primary/45 sm:block" aria-hidden />
      <div className="flex min-w-0 items-center gap-2">
        <EldritchIcon
          name={MythosIcons.log}
          size={22}
          className="shrink-0 text-mythos-terminal-primary drop-shadow-[0_0_6px_rgba(0,255,0,0.35)]"
          aria-hidden
        />
        <div className="min-w-0">
          <div className="text-xs font-mono uppercase leading-none tracking-eldritch text-mythos-terminal-secondary/75">
            Chronicle
          </div>
          <span className="text-lg font-bold leading-tight tracking-tight text-mythos-terminal-primary">Game Log</span>
        </div>
      </div>
    </div>
    <div className="flex items-center space-x-2">
      <TerminalButton variant="secondary" size="sm" onClick={onClearFilters} className="px-2 py-1 text-sm">
        Clear Filters
      </TerminalButton>
      <TerminalButton
        variant="secondary"
        size="sm"
        onClick={() => {
          onClearMessages?.();
        }}
        className="px-2 py-1 text-sm"
      >
        Clear game log
      </TerminalButton>
      <TerminalButton
        variant="secondary"
        size="sm"
        onClick={() => {
          onDownloadLogs?.();
        }}
        className="px-2 py-1 text-sm"
      >
        Download log file
      </TerminalButton>
    </div>
  </div>
);

interface GameLogPanelFilterBarProps {
  messageFilter: string;
  timeFilter: string;
  searchQuery: string;
  onMessageFilterChange: (value: string) => void;
  onTimeFilterChange: (value: string) => void;
  onSearchQueryChange: (value: string) => void;
  onSearchSubmit: () => void;
}

export const GameLogPanelFilterBar: React.FC<GameLogPanelFilterBarProps> = ({
  messageFilter,
  timeFilter,
  searchQuery,
  onMessageFilterChange,
  onTimeFilterChange,
  onSearchQueryChange,
  onSearchSubmit,
}) => {
  const messageTypeFilterId = 'game-log-filter-message-type';
  const timeRangeFilterId = 'game-log-filter-time-range';
  const searchInputId = 'game-log-search-query';

  return (
    <div className="space-y-2 border-b border-mythos-terminal-primary/20 border-l-2 border-l-mythos-terminal-primary/25 bg-mythos-terminal-background/90 bg-linear-to-b from-mythos-terminal-primary/[0.04] to-transparent p-3">
      <div className="flex flex-wrap items-end gap-3">
        <div className="flex min-w-0 flex-col gap-0.5">
          <label htmlFor={messageTypeFilterId} className="font-mono text-xs text-mythos-terminal-text-secondary">
            Message type
          </label>
          <select
            id={messageTypeFilterId}
            value={messageFilter}
            onChange={e => {
              onMessageFilterChange(e.target.value);
            }}
            className={getGameLogMessageFilterSelectClassName(messageFilter)}
          >
            <option value="all">All types</option>
            <option value="system">System</option>
            <option value="chat">Chat</option>
            <option value="emote">Emotes</option>
            <option value="whisper">Whispers</option>
            <option value="shout">Shouts</option>
            <option value="error">Errors</option>
            <option value="combat">Combat</option>
          </select>
        </div>
        <div className="flex min-w-0 flex-col gap-0.5">
          <label htmlFor={timeRangeFilterId} className="font-mono text-xs text-mythos-terminal-text-secondary">
            Time range
          </label>
          <select
            id={timeRangeFilterId}
            value={timeFilter}
            onChange={e => {
              onTimeFilterChange(e.target.value);
            }}
            className={getGameLogTimeFilterSelectClassName(timeFilter)}
          >
            <option value="all">Any time</option>
            <option value="5">Last 5 min</option>
            <option value="15">Last 15 min</option>
            <option value="30">Last 30 min</option>
            <option value="60">Last hour</option>
          </select>
        </div>
      </div>
      <div className="flex flex-wrap items-end gap-2">
        <div className="flex min-w-0 flex-1 flex-col gap-0.5">
          <label htmlFor={searchInputId} className="font-mono text-xs text-mythos-terminal-text-secondary">
            Search text
          </label>
          <input
            id={searchInputId}
            type="search"
            placeholder="Words to find in the log"
            value={searchQuery}
            onChange={e => {
              onSearchQueryChange(e.target.value);
            }}
            className={getGameLogSearchInputClassName(searchQuery)}
            autoComplete="off"
          />
        </div>
        <TerminalButton
          variant={searchQuery.trim() ? 'primary' : 'secondary'}
          size="sm"
          onClick={onSearchSubmit}
          className="min-h-touch px-2 py-1 text-sm"
          type="button"
          aria-label="Run search and add query to history"
        >
          Search
        </TerminalButton>
      </div>
    </div>
  );
};

interface GameLogSearchHistorySectionProps {
  visible: boolean;
  entries: string[];
  onSelectQuery: (query: string) => void;
  onClose: () => void;
}

export const GameLogSearchHistorySection: React.FC<GameLogSearchHistorySectionProps> = ({
  visible,
  entries,
  onSelectQuery,
  onClose,
}) => {
  if (!visible || entries.length === 0) {
    return null;
  }

  return (
    <div className="border-t border-mythos-terminal-primary/20 bg-mythos-terminal-background/95 p-3">
      <div className="mb-2 flex items-center justify-between">
        <h4 className="text-base font-bold leading-tight tracking-tight text-mythos-terminal-primary">
          Search History
        </h4>
        <TerminalButton
          variant="secondary"
          size="sm"
          onClick={onClose}
          className="px-2 py-1 text-sm"
          type="button"
          aria-label="Close search history"
        >
          Close
        </TerminalButton>
      </div>
      <div className="space-y-1 max-h-24 overflow-y-auto">
        {entries.map((query, index) => (
          <button
            key={index}
            type="button"
            className="w-full cursor-pointer rounded border border-mythos-terminal-primary/15 bg-mythos-terminal-surface/40 p-2 text-left font-mono text-sm leading-snug text-mythos-terminal-text-secondary hover:border-mythos-terminal-primary/35 hover:bg-mythos-terminal-surface/70 hover:text-mythos-terminal-text"
            aria-label={`Use saved search: ${query}`}
            onClick={() => {
              onSelectQuery(query);
            }}
          >
            {query}
          </button>
        ))}
      </div>
    </div>
  );
};
