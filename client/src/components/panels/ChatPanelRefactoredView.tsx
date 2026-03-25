import { ChatPanelRefactoredToolbar } from './ChatPanelRefactoredToolbar';
import { ChatHistoryToggle } from './chat/ChatHistoryToggle.jsx';
import { ChatMessagesList } from './chat/ChatMessagesList.jsx';
import { ChatStatistics } from './chat/ChatStatistics.jsx';
import type { UseChatPanelRefactoredResult } from './useChatPanelRefactored';

export type ChatPanelRefactoredChromeProps = {
  onClearMessages?: () => void;
  onDownloadLogs?: () => void;
  disabled: boolean;
  isConnected: boolean;
  selectedChannel: string;
};

export type ChatPanelRefactoredViewProps = {
  chrome: ChatPanelRefactoredChromeProps;
  panel: UseChatPanelRefactoredResult;
};

export function ChatPanelRefactoredView({ chrome, panel }: ChatPanelRefactoredViewProps) {
  const { onClearMessages, onDownloadLogs, disabled, isConnected, selectedChannel } = chrome;
  const {
    showChatHistory,
    toggleShowChatHistory,
    chatFilter,
    setChatFilter,
    chatStats,
    unreadCounts,
    filteredMessages,
    handleChannelSelect,
  } = panel;

  return (
    <div className="h-full flex flex-col font-mono">
      <ChatPanelRefactoredToolbar
        onClearMessages={onClearMessages}
        onDownloadLogs={onDownloadLogs}
        selectedChannel={selectedChannel}
        disabled={disabled}
        isConnected={isConnected}
        unreadCounts={unreadCounts}
        handleChannelSelect={handleChannelSelect}
      />
      <ChatHistoryToggle
        showChatHistory={showChatHistory}
        onToggleHistory={toggleShowChatHistory}
        chatFilter={chatFilter}
        onFilterChange={setChatFilter}
        currentChannelMessages={chatStats.currentChannelMessages}
      />
      <div
        className="min-h-panel-chat flex-1 overflow-auto rounded border border-mythos-terminal-border bg-mythos-terminal-background p-3"
        role="log"
        aria-label="Chat Messages"
      >
        <ChatMessagesList messages={filteredMessages} />
      </div>
      <ChatStatistics
        selectedChannel={selectedChannel}
        currentChannelMessages={chatStats.currentChannelMessages}
        unreadCounts={unreadCounts}
      />
    </div>
  );
}
