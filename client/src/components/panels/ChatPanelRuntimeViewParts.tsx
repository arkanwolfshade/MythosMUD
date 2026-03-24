import { AVAILABLE_CHANNELS, CHAT_CHANNEL_OPTIONS } from '../../config/channels';
import { ansiToHtmlWithBreaks } from '../../utils/ansiToHtml';
import { SafeHtml } from '../common/SafeHtml';
import { ChannelSelector } from '../ui/ChannelSelector';
import { EldritchIcon, MythosIcons } from '../ui/EldritchIcon';
import { TerminalButton } from '../ui/TerminalButton';
import { ChannelActivityIndicators } from './chat/ChannelActivityIndicators';
import {
  buildChatSearchHighlightHtml,
  escapeForChatHighlight,
  formatChatTimestampUtc,
  getChatPanelMessageClass,
  type ChatPanelMessage,
} from './chatPanelRuntimeUtils';
import type { ChatPanelRuntimeViewProps } from './chatPanelRuntimeViewTypes';

const fontSizeClass = 'text-sm';

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
        <EldritchIcon name={MythosIcons.chat} size={20} variant="primary" />
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
        <TerminalButton
          variant="secondary"
          size="sm"
          onClick={onOpenExport}
          className="px-2 h-8 text-xs"
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
  return (
    <div className="p-2 border-b border-gray-700 bg-mythos-terminal-background" data-testid="chat-history-toggle">
      <div className="flex items-center gap-2 flex-wrap">
        <button className="text-xs text-mythos-terminal-primary" onClick={toggleHistory} type="button">
          Chat History
        </button>
        <select
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
        <div className="flex items-center gap-1 flex-1 min-w-input">
          <EldritchIcon name={MythosIcons.search} size={14} variant="primary" />
          <input
            type="text"
            placeholder="Search messages..."
            value={searchQuery}
            onChange={e => onSearchChange(e.target.value)}
            className="flex-1 text-xs bg-mythos-terminal-surface border border-gray-700 rounded px-2 py-1 text-mythos-terminal-text focus:outline-hidden focus:border-mythos-terminal-primary"
            disabled={disabled}
          />
          {searchQuery && (
            <>
              <button
                onClick={onSearchPrevious}
                disabled={searchMatches.size === 0}
                className="text-xs px-2 py-1 bg-mythos-terminal-surface border border-gray-700 rounded hover:bg-mythos-terminal-background disabled:opacity-50"
                title="Previous match"
                type="button"
              >
                ↑
              </button>
              <button
                onClick={onSearchNext}
                disabled={searchMatches.size === 0}
                className="text-xs px-2 py-1 bg-mythos-terminal-surface border border-gray-700 rounded hover:bg-mythos-terminal-background disabled:opacity-50"
                title="Next match"
                type="button"
              >
                ↓
              </button>
              <button
                onClick={() => onSearchChange('')}
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
            <select
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
          <EldritchIcon name={MythosIcons.clock} size={12} variant="primary" />
          <span>Viewing: {viewingLabel}</span>
        </div>
        <div className="text-xs text-mythos-terminal-text-secondary">
          {currentChannelMessageCount} message{currentChannelMessageCount === 1 ? '' : 's'}
        </div>
      </div>
    </div>
  );
}

type ChatPanelMessageRowProps = {
  message: ChatPanelMessage;
  index: number;
  totalVisible: number;
  isHistoryVisible: boolean;
  searchQuery: string;
  currentSearchIndex: number;
};

function ChatPanelMessageRow({
  message,
  index,
  totalVisible,
  isHistoryVisible,
  searchQuery,
  currentSearchIndex,
}: ChatPanelMessageRowProps) {
  const shouldAnimate = !isHistoryVisible && !searchQuery && index >= totalVisible - 10;
  const animationClass = shouldAnimate ? 'animate-fade-in' : '';
  const animationDelay = shouldAnimate ? `${(index - (totalVisible - 10)) * 40}ms` : '0ms';
  const isHighlighted = currentSearchIndex === index && Boolean(searchQuery);

  return (
    <div
      className={
        `message p-3 bg-mythos-terminal-surface border rounded transition-all duration-300 ` +
        `hover:border-mythos-terminal-primary/30 hover:shadow-lg ${animationClass} ` +
        (isHighlighted
          ? 'border-mythos-terminal-warning border-2 shadow-lg shadow-mythos-terminal-warning/50'
          : 'border-gray-700')
      }
      style={{ animationDelay }}
      data-testid="chat-message"
      ref={(el: HTMLDivElement | null) => {
        if (currentSearchIndex === index && el) el.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }}
    >
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
      <div className="mb-2">
        <span className="text-xs text-mythos-terminal-text-secondary font-mono">
          {formatChatTimestampUtc(message.timestamp)}
        </span>
      </div>
      <div
        className={`message-text ${fontSizeClass} leading-relaxed ${getChatPanelMessageClass(message)}`}
        data-message-text={message.rawText ?? message.text}
        onContextMenu={e => e.preventDefault()}
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
                ? buildChatSearchHighlightHtml(message.rawText ?? message.text, searchQuery)
                : escapeForChatHighlight(message.rawText ?? message.text)
            }
            title="Right-click for options"
            style={{ whiteSpace: 'pre-wrap', wordBreak: 'break-word' }}
          />
        )}
      </div>
    </div>
  );
}

type ChatPanelMessagesLogProps = {
  visibleMessages: ChatPanelMessage[];
  isHistoryVisible: boolean;
  searchQuery: string;
  currentSearchIndex: number;
};

function ChatPanelMessagesLog({
  visibleMessages,
  isHistoryVisible,
  searchQuery,
  currentSearchIndex,
}: ChatPanelMessagesLogProps) {
  const total = visibleMessages.length;
  if (total === 0) {
    return (
      <div className="flex items-center justify-center h-full">
        <div className="text-center space-y-2">
          <EldritchIcon name={MythosIcons.chat} size={32} variant="secondary" className="mx-auto opacity-50" />
          <p className="text-mythos-terminal-text-secondary text-sm">
            No messages yet. Start chatting to see messages here.
          </p>
        </div>
      </div>
    );
  }
  return (
    <div className="space-y-3">
      {visibleMessages.map((message, index) => (
        <ChatPanelMessageRow
          key={index}
          message={message}
          index={index}
          totalVisible={total}
          isHistoryVisible={isHistoryVisible}
          searchQuery={searchQuery}
          currentSearchIndex={currentSearchIndex}
        />
      ))}
    </div>
  );
}

type ChatExportDialogProps = {
  visibleCount: number;
  exportFormat: string;
  isExporting: boolean;
  setExportFormat: (v: string) => void;
  onClose: () => void;
  onConfirmExport: () => void;
};

function ChatExportDialog({
  visibleCount,
  exportFormat,
  isExporting,
  setExportFormat,
  onClose,
  onConfirmExport,
}: ChatExportDialogProps) {
  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center">
      <button
        type="button"
        className="absolute inset-0 cursor-default bg-black bg-opacity-50 border-0 p-0 disabled:cursor-not-allowed"
        onClick={() => !isExporting && onClose()}
        disabled={isExporting}
        aria-label="Close export dialog"
      />
      <div className="relative z-10 bg-mythos-terminal-surface border border-mythos-terminal-primary rounded-lg p-6 max-w-md w-full mx-4">
        <h3 className="text-mythos-terminal-primary font-bold text-lg mb-4">Export Chat Messages</h3>
        <div className="space-y-4">
          <div>
            <label htmlFor="chat-export-format" className="block text-sm text-mythos-terminal-text-secondary mb-2">
              Export Format
            </label>
            <select
              id="chat-export-format"
              value={exportFormat}
              onChange={e => setExportFormat(e.target.value)}
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
            Exporting {visibleCount} message{visibleCount === 1 ? '' : 's'}
          </div>
          <div className="flex gap-2 justify-end">
            <button
              onClick={onClose}
              disabled={isExporting}
              className="px-4 py-2 text-sm bg-mythos-terminal-background border border-gray-700 rounded hover:bg-mythos-terminal-surface disabled:opacity-50"
              type="button"
            >
              Cancel
            </button>
            <button
              onClick={onConfirmExport}
              disabled={isExporting || visibleCount === 0}
              className="px-4 py-2 text-sm bg-mythos-terminal-primary text-black rounded hover:bg-mythos-terminal-primary/80 disabled:opacity-50 font-bold"
              type="button"
            >
              {isExporting ? 'Exporting...' : 'Export'}
            </button>
          </div>
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
        className="flex-1 overflow-auto p-3 bg-mythos-terminal-background border border-gray-700 rounded"
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
        <ChatExportDialog
          visibleCount={visibleMessages.length}
          exportFormat={exportFormat}
          isExporting={isExporting}
          setExportFormat={setExportFormat}
          onClose={() => setShowExportDialog(false)}
          onConfirmExport={onConfirmExport}
        />
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
