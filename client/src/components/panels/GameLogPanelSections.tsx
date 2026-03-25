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
        Clear Log
      </TerminalButton>
      <TerminalButton
        variant="secondary"
        size="sm"
        onClick={() => {
          onDownloadLogs?.();
        }}
        className="px-2 py-1 text-sm"
      >
        Download
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
}) => (
  <div className="space-y-2 border-b border-mythos-terminal-primary/20 border-l-2 border-l-mythos-terminal-primary/25 bg-mythos-terminal-background/90 bg-linear-to-b from-mythos-terminal-primary/[0.04] to-transparent p-3">
    <div className="flex flex-wrap gap-2">
      <select
        value={messageFilter}
        onChange={e => {
          onMessageFilterChange(e.target.value);
        }}
        className={getGameLogMessageFilterSelectClassName(messageFilter)}
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
          onTimeFilterChange(e.target.value);
        }}
        className={getGameLogTimeFilterSelectClassName(timeFilter)}
      >
        <option value="all">All Time</option>
        <option value="5">Last 5 min</option>
        <option value="15">Last 15 min</option>
        <option value="30">Last 30 min</option>
        <option value="60">Last hour</option>
      </select>
    </div>
    <div className="flex gap-2">
      <input
        type="text"
        placeholder="Search messages..."
        value={searchQuery}
        onChange={e => {
          onSearchQueryChange(e.target.value);
        }}
        className={getGameLogSearchInputClassName(searchQuery)}
      />
      <TerminalButton
        variant={searchQuery.trim() ? 'primary' : 'secondary'}
        size="sm"
        onClick={onSearchSubmit}
        className="px-2 py-1 text-sm"
      >
        Search
      </TerminalButton>
    </div>
  </div>
);

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
        <TerminalButton variant="secondary" size="sm" onClick={onClose} className="px-2 py-1 text-sm">
          Close
        </TerminalButton>
      </div>
      <div className="space-y-1 max-h-24 overflow-y-auto">
        {entries.map((query, index) => (
          <button
            key={index}
            type="button"
            className="w-full cursor-pointer rounded border border-mythos-terminal-primary/15 bg-mythos-terminal-surface/40 p-2 text-left font-mono text-sm leading-snug text-mythos-terminal-text-secondary hover:border-mythos-terminal-primary/35 hover:bg-mythos-terminal-surface/70 hover:text-mythos-terminal-text"
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
