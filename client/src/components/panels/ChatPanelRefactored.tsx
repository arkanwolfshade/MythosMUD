import { DEFAULT_CHANNEL } from '../../config/channels';
import { ChatPanelRefactoredView } from './ChatPanelRefactoredView';
import type { ChatPanelRefactoredMessage } from './chatPanelRefactoredTypes';
import { useChatPanelRefactored } from './useChatPanelRefactored';

interface ChatPanelRefactoredProps {
  messages: ChatPanelRefactoredMessage[];
  onSendChatMessage: (message: string, channel: string) => void;
  onClearMessages?: () => void;
  onDownloadLogs?: () => void;
  disabled?: boolean;
  isConnected?: boolean;
  selectedChannel?: string;
  onChannelSelect?: (channelId: string) => void;
}

export function ChatPanelRefactored(props: ChatPanelRefactoredProps) {
  const {
    messages,
    onClearMessages,
    onDownloadLogs,
    disabled = false,
    isConnected = true,
    selectedChannel = DEFAULT_CHANNEL,
    onChannelSelect,
  } = props;

  const panel = useChatPanelRefactored(messages, selectedChannel, onChannelSelect);

  return (
    <ChatPanelRefactoredView
      chrome={{ onClearMessages, onDownloadLogs, disabled, isConnected, selectedChannel }}
      panel={panel}
    />
  );
}
