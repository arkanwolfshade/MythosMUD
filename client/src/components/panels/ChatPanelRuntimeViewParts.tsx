import { lazy, Suspense } from 'react';
import { CHAT_CHANNEL_OPTIONS } from '../../config/channels';
import { ChannelSelector } from '../ui/ChannelSelector';
import { EldritchIcon, MythosIcons } from '../ui/EldritchIcon';
import { TerminalButton } from '../ui/TerminalButton';
import { ChannelActivityIndicators } from './chat/ChannelActivityIndicators';
import { ChatPanelHistorySearch } from './chatPanelHistorySearch';
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
    <div className="flex items-center justify-between p-3 border-b border-mythos-terminal-border bg-mythos-terminal-surface">
      <div className="flex items-center gap-2">
        <EldritchIcon name={MythosIcons.chat} size={20} variant="primary" aria-hidden />
      </div>
      <div className="flex items-center gap-2">
        {onClearMessages && (
          <TerminalButton
            variant="secondary"
            size="sm"
            onClick={onClearMessages}
            className="inline-flex min-h-touch min-w-touch items-center justify-center p-2"
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
            className="inline-flex min-h-touch min-w-touch items-center justify-center p-2"
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
      className="p-3 border-b border-mythos-terminal-border bg-mythos-terminal-surface"
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

type ChatPanelViewingStripProps = {
  viewingLabel: string;
  currentChannelMessageCount: number;
};

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

function ChatPanelRuntimeChatArea(props: ChatPanelRuntimeChatAreaProps) {
  return (
    <>
      <div
        className="min-h-panel-chat flex-1 overflow-auto p-3 bg-mythos-terminal-background border border-mythos-terminal-border rounded contain-content"
        role="log"
        aria-label="Chat Messages"
      >
        <ChatPanelMessagesLog
          visibleMessages={props.visibleMessages}
          isHistoryVisible={props.isHistoryVisible}
          searchQuery={props.searchQuery}
          currentSearchIndex={props.currentSearchIndex}
        />
      </div>
      {props.showExportDialog && (
        <Suspense fallback={null}>
          <ChatExportDialogLazy
            visibleCount={props.visibleMessages.length}
            exportFormat={props.exportFormat}
            isExporting={props.isExporting}
            setExportFormat={props.setExportFormat}
            onClose={() => props.setShowExportDialog(false)}
            onConfirmExport={props.onConfirmExport}
          />
        </Suspense>
      )}
    </>
  );
}

function ChatPanelViewingStrip({ viewingLabel, currentChannelMessageCount }: ChatPanelViewingStripProps) {
  return (
    <div className="p-2 border-b border-mythos-terminal-border bg-mythos-terminal-background">
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
