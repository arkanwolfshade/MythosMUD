import { lazy, Suspense } from 'react';
import { AVAILABLE_CHANNELS, CHAT_CHANNEL_OPTIONS } from '../../config/channels';
import { ChannelSelector } from '../ui/ChannelSelector';
import { EldritchIcon, MythosIcons } from '../ui/EldritchIcon';
import { TerminalButton } from '../ui/TerminalButton';
import { ChannelActivityIndicators } from './chat/ChannelActivityIndicators';
import { ChatPanelMessagesLog } from './ChatPanelMessagesLog';
import type { ChatPanelRuntimeViewProps } from './chatPanelRuntimeViewTypes';

const ChatExportDialogLazy = lazy(async () => {
  const m = await import('./ChatExportDialog');
  return { default: m.ChatExportDialog };
});

type ChatPanelToolbarProps = {
  disabled: boolean;
  onClearMessages?: () => void;
  onDownloadLogs?: () => void;
  onOpenExport: () => void;
};

function ChatPanelToolbar({ disabled, onClearMessages, onDownloadLogs, onOpenExport }: ChatPanelToolbarProps) {
  return (
    <div className="flex items-center justify-between p-3 border-b border-gray-700 bg-mythos-terminal-surface">
      <div className="flex items-center gap-2">
        <EldritchIcon name={MythosIcons.chat} size={20} variant="primary" aria-hidden />
      </div>
      <div className="flex items-center gap-2">
        {onClearMessages && (
          <TerminalButton
            variant="secondary"
            size="sm"
            onClick={onClearMessages}
            className="inline-flex h-8 w-8 min-h-touch min-w-touch items-center justify-center p-2"
            data-testid="chat-panel-clear-messages"
            aria-label="Clear chat messages"
            type="button"
          >
            <EldritchIcon name={MythosIcons.clear} size={14} variant="error" aria-hidden />
          </TerminalButton>
        )}
        {onDownloadLogs && (
          <TerminalButton
            variant="secondary"
            size="sm"
            onClick={onDownloadLogs}
            className="inline-flex h-8 w-8 min-h-touch min-w-touch items-center justify-center p-2"
            data-testid="chat-panel-download-logs"
            aria-label="Download chat logs"
            type="button"
          >
            <EldritchIcon name={MythosIcons.download} size={14} variant="primary" aria-hidden />
          </TerminalButton>
        )}
        <TerminalButton
          variant="secondary"
          size="sm"
          onClick={onOpenExport}
          className="min-h-touch px-3 py-2 text-xs"
          disabled={disabled}
          data-testid="chat-panel-export"
          aria-label="Export chat messages"
          type="button"
        >
          Export
        </TerminalButton>
      </div>
    </div>
  );
}

type ChatPanelChannelSectionProps = {
  normalizedSelectedChannel: string;
  disabled: boolean;
  isConnected: boolean;
  unreadCounts: Record<string, number>;
  onChannelSelect: (channelId: string) => void;
};

function ChatPanelChannelSection({
  normalizedSelectedChannel,
  disabled,
  isConnected,
  unreadCounts,
  onChannelSelect,
}: ChatPanelChannelSectionProps) {
  return (
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
          onChannelSelect={onChannelSelect}
          disabled={disabled || !isConnected}
          className="flex-1 w-full sm:w-auto"
        />
      </div>
      <ChannelActivityIndicators
        selectedChannel={normalizedSelectedChannel}
        unreadCounts={unreadCounts}
        onChannelSelect={onChannelSelect}
      />
    </div>
  );
}

type ChatPanelHistorySearchProps = {
  disabled: boolean;
  isHistoryVisible: boolean;
  setIsHistoryVisible: (value: boolean) => void;
  visibleMessagesLength: number;
  historyEligibleLength: number;
  filteredMessagesLength: number;
  searchQuery: string;
  searchMatches: Set<number>;
  currentSearchIndex: number;
  searchFilterChannel: string;
  searchFilterType: string;
  onSearchChange: (query: string) => void;
  onSearchNext: () => void;
  onSearchPrevious: () => void;
  setSearchFilterChannel: (value: string) => void;
  setSearchFilterType: (value: string) => void;
  toggleHistory: () => void;
};

function ChatPanelHistorySearch({
  disabled,
  isHistoryVisible,
  setIsHistoryVisible,
  visibleMessagesLength,
  historyEligibleLength,
  filteredMessagesLength,
  searchQuery,
  searchMatches,
  currentSearchIndex,
  searchFilterChannel,
  searchFilterType,
  onSearchChange,
  onSearchNext,
  onSearchPrevious,
  setSearchFilterChannel,
  setSearchFilterType,
  toggleHistory,
}: ChatPanelHistorySearchProps) {
  const historyScopeId = 'chat-history-scope';
  const chatSearchInputId = 'chat-panel-search-messages';

  return (
    <div className="p-2 border-b border-gray-700 bg-mythos-terminal-background" data-testid="chat-history-toggle">
      <div className="flex items-center gap-2 flex-wrap">
        <button className="min-h-touch px-1 text-xs text-mythos-terminal-primary" onClick={toggleHistory} type="button">
          Chat History
        </button>
        <label htmlFor={historyScopeId} className="sr-only">
          Message history scope
        </label>
        <select
          id={historyScopeId}
          className="text-xs bg-mythos-terminal-surface border border-gray-700 rounded px-1"
          value={isHistoryVisible ? 'all' : 'current'}
          onChange={event => setIsHistoryVisible(event.target.value === 'all')}
        >
          <option value="current">Current</option>
          <option value="all">All</option>
        </select>
        <span className="text-xs text-mythos-terminal-text-secondary">
          Messages: {visibleMessagesLength} / {isHistoryVisible ? historyEligibleLength : filteredMessagesLength}
        </span>
      </div>
      <div className="mt-2 flex items-center gap-2 flex-wrap">
        <div className="flex min-w-0 flex-1 items-center gap-1">
          <EldritchIcon name={MythosIcons.search} size={14} variant="primary" aria-hidden />
          <label htmlFor={chatSearchInputId} className="sr-only">
            Search messages
          </label>
          <input
            id={chatSearchInputId}
            type="text"
            placeholder="Search messages..."
            value={searchQuery}
            onChange={e => onSearchChange(e.target.value)}
            className="min-w-0 flex-1 text-xs bg-mythos-terminal-surface border border-gray-700 rounded px-2 py-1 text-mythos-terminal-text focus:outline-hidden focus:border-mythos-terminal-primary"
            disabled={disabled}
            autoComplete="off"
          />
          {searchQuery && (
            <>
              <button
                onClick={onSearchPrevious}
                disabled={searchMatches.size === 0}
                className="min-h-touch min-w-touch text-xs px-2 py-1 bg-mythos-terminal-surface border border-gray-700 rounded hover:bg-mythos-terminal-background disabled:opacity-50"
                title="Previous match"
                aria-label="Previous search match"
                type="button"
              >
                ↑
              </button>
              <button
                onClick={onSearchNext}
                disabled={searchMatches.size === 0}
                className="min-h-touch min-w-touch text-xs px-2 py-1 bg-mythos-terminal-surface border border-gray-700 rounded hover:bg-mythos-terminal-background disabled:opacity-50"
                title="Next match"
                aria-label="Next search match"
                type="button"
              >
                ↓
              </button>
              <button
                onClick={() => onSearchChange('')}
                className="min-h-touch min-w-touch text-xs px-2 py-1 bg-mythos-terminal-surface border border-gray-700 rounded hover:bg-mythos-terminal-background"
                title="Clear search"
                aria-label="Clear search"
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
            <label htmlFor="chat-search-filter-channel" className="sr-only">
              Filter search by channel
            </label>
            <select
              id="chat-search-filter-channel"
              value={searchFilterChannel}
              onChange={e => setSearchFilterChannel(e.target.value)}
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
            <label htmlFor="chat-search-filter-type" className="sr-only">
              Filter search by message type
            </label>
            <select
              id="chat-search-filter-type"
              value={searchFilterType}
              onChange={e => setSearchFilterType(e.target.value)}
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
  );
}

type ChatPanelViewingStripProps = {
  viewingLabel: string;
  currentChannelMessageCount: number;
};

function ChatPanelViewingStrip({ viewingLabel, currentChannelMessageCount }: ChatPanelViewingStripProps) {
  return (
    <div className="p-2 border-b border-gray-700 bg-mythos-terminal-background">
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-2 text-xs text-mythos-terminal-text-secondary">
          <EldritchIcon name={MythosIcons.clock} size={12} variant="primary" aria-hidden />
          <span>Viewing: {viewingLabel}</span>
        </div>
        <div className="text-xs text-mythos-terminal-text-secondary">
          {currentChannelMessageCount} message{currentChannelMessageCount === 1 ? '' : 's'}
        </div>
      </div>
    </div>
  );
}

type ChatPanelRuntimeChatAreaProps = Pick<
  ChatPanelRuntimeViewProps,
  | 'visibleMessages'
  | 'isHistoryVisible'
  | 'searchQuery'
  | 'currentSearchIndex'
  | 'showExportDialog'
  | 'exportFormat'
  | 'isExporting'
  | 'setExportFormat'
  | 'setShowExportDialog'
  | 'onConfirmExport'
>;

function ChatPanelRuntimeChatArea({
  visibleMessages,
  isHistoryVisible,
  searchQuery,
  currentSearchIndex,
  showExportDialog,
  exportFormat,
  isExporting,
  setExportFormat,
  setShowExportDialog,
  onConfirmExport,
}: ChatPanelRuntimeChatAreaProps) {
  return (
    <>
      <div
        className="flex-1 overflow-auto p-3 bg-mythos-terminal-background border border-gray-700 rounded contain-content"
        role="log"
        aria-label="Chat Messages"
        style={{ minHeight: '200px' }}
      >
        <ChatPanelMessagesLog
          visibleMessages={visibleMessages}
          isHistoryVisible={isHistoryVisible}
          searchQuery={searchQuery}
          currentSearchIndex={currentSearchIndex}
        />
      </div>
      {showExportDialog && (
        <Suspense fallback={null}>
          <ChatExportDialogLazy
            visibleCount={visibleMessages.length}
            exportFormat={exportFormat}
            isExporting={isExporting}
            setExportFormat={setExportFormat}
            onClose={() => setShowExportDialog(false)}
            onConfirmExport={onConfirmExport}
          />
        </Suspense>
      )}
    </>
  );
}

export function ChatPanelRuntimeViewInner(props: ChatPanelRuntimeViewProps) {
  return (
    <div className="h-full flex flex-col font-mono">
      <ChatPanelToolbar
        disabled={props.disabled}
        onClearMessages={props.onClearMessages}
        onDownloadLogs={props.onDownloadLogs}
        onOpenExport={() => props.setShowExportDialog(true)}
      />
      <ChatPanelChannelSection
        normalizedSelectedChannel={props.normalizedSelectedChannel}
        disabled={props.disabled}
        isConnected={props.isConnected}
        unreadCounts={props.unreadCounts}
        onChannelSelect={props.onChannelSelect}
      />
      <ChatPanelHistorySearch
        disabled={props.disabled}
        isHistoryVisible={props.isHistoryVisible}
        setIsHistoryVisible={props.setIsHistoryVisible}
        visibleMessagesLength={props.visibleMessages.length}
        historyEligibleLength={props.historyEligibleMessagesLength}
        filteredMessagesLength={props.filteredMessagesLength}
        searchQuery={props.searchQuery}
        searchMatches={props.searchMatches}
        currentSearchIndex={props.currentSearchIndex}
        searchFilterChannel={props.searchFilterChannel}
        searchFilterType={props.searchFilterType}
        onSearchChange={props.onSearchChange}
        onSearchNext={props.onSearchNext}
        onSearchPrevious={props.onSearchPrevious}
        setSearchFilterChannel={props.setSearchFilterChannel}
        setSearchFilterType={props.setSearchFilterType}
        toggleHistory={props.toggleHistory}
      />
      <ChatPanelViewingStrip
        viewingLabel={props.viewingLabel}
        currentChannelMessageCount={props.currentChannelMessageCount}
      />
      <ChatPanelRuntimeChatArea
        visibleMessages={props.visibleMessages}
        isHistoryVisible={props.isHistoryVisible}
        searchQuery={props.searchQuery}
        currentSearchIndex={props.currentSearchIndex}
        showExportDialog={props.showExportDialog}
        exportFormat={props.exportFormat}
        isExporting={props.isExporting}
        setExportFormat={props.setExportFormat}
        setShowExportDialog={props.setShowExportDialog}
        onConfirmExport={props.onConfirmExport}
      />
    </div>
  );
}
