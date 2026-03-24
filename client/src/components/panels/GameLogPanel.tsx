import React from 'react';
import { GameLogMessagesList, type GameLogListMessage } from './GameLogMessagesList';
import { GameLogPanelFilterBar, GameLogPanelHeader, GameLogSearchHistorySection } from './GameLogPanelSections';
import { useGameLogPanelState } from './useGameLogPanelState';

interface GameLogPanelProps {
  messages: GameLogListMessage[];
  onClearMessages?: () => void;
  onDownloadLogs?: () => void;
}

export const GameLogPanel: React.FC<GameLogPanelProps> = ({ messages, onClearMessages, onDownloadLogs }) => {
  const {
    messagesEndRef,
    messageFilter,
    setMessageFilter,
    searchQuery,
    setSearchQuery,
    timeFilter,
    setTimeFilter,
    searchHistory,
    showSearchHistory,
    setShowSearchHistory,
    handleSearch,
    clearFilters,
    filteredMessages,
  } = useGameLogPanelState(messages);

  return (
    <div
      className={
        'game-log-panel h-full flex flex-col overflow-hidden rounded-sm border border-mythos-terminal-primary/25 ' +
        'bg-mythos-terminal-background/95 shadow-[inset_0_1px_0_0_rgba(0,255,0,0.07)] ring-1 ring-black/50'
      }
    >
      <GameLogPanelHeader
        onClearFilters={clearFilters}
        onClearMessages={onClearMessages}
        onDownloadLogs={onDownloadLogs}
      />
      <GameLogPanelFilterBar
        messageFilter={messageFilter}
        timeFilter={timeFilter}
        searchQuery={searchQuery}
        onMessageFilterChange={setMessageFilter}
        onTimeFilterChange={setTimeFilter}
        onSearchQueryChange={setSearchQuery}
        onSearchSubmit={() => {
          handleSearch(searchQuery);
        }}
      />
      <GameLogMessagesList messages={filteredMessages} messagesEndRef={messagesEndRef} />
      <GameLogSearchHistorySection
        visible={showSearchHistory}
        entries={searchHistory}
        onSelectQuery={query => {
          setSearchQuery(query);
          setShowSearchHistory(false);
        }}
        onClose={() => {
          setShowSearchHistory(false);
        }}
      />
    </div>
  );
};
