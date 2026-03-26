import { ChannelActivityIndicators } from './chat/ChannelActivityIndicators.tsx';
import { ChannelSelectorSection } from './chat/ChannelSelectorSection.tsx';
import { ChatHeader } from './chat/ChatHeader.tsx';

type ChatPanelRefactoredToolbarProps = {
  onClearMessages?: () => void;
  onDownloadLogs?: () => void;
  selectedChannel: string;
  disabled: boolean;
  isConnected: boolean;
  unreadCounts: Record<string, number>;
  handleChannelSelect: (channelId: string) => void;
};

export function ChatPanelRefactoredToolbar({
  onClearMessages,
  onDownloadLogs,
  selectedChannel,
  disabled,
  isConnected,
  unreadCounts,
  handleChannelSelect,
}: ChatPanelRefactoredToolbarProps) {
  return (
    <>
      <ChatHeader onClearMessages={onClearMessages} onDownloadLogs={onDownloadLogs} />
      <div className="border-b border-mythos-terminal-border bg-mythos-terminal-surface p-3">
        <ChannelSelectorSection
          selectedChannel={selectedChannel}
          onChannelSelect={handleChannelSelect}
          disabled={disabled}
          isConnected={isConnected}
        />
        <ChannelActivityIndicators
          selectedChannel={selectedChannel}
          unreadCounts={unreadCounts}
          onChannelSelect={handleChannelSelect}
        />
      </div>
    </>
  );
}
