import React, { useMemo, useState } from 'react';
import { DEFAULT_CHANNEL } from '../../config/channels';
import { extractChannelFromMessage, isChatContent } from '../../utils/messageTypeUtils';
import {
  ChannelActivityIndicators,
  ChannelSelectorSection,
  ChatHeader,
  ChatHistoryToggle,
  ChatMessagesList,
  ChatStatistics,
} from './chat';

interface ChatMessage {
  text: string;
  timestamp: string;
  isHtml: boolean;
  isCompleteHtml?: boolean;
  messageType?: string;
  channel?: string;
  aliasChain?: Array<{
    original: string;
    expanded: string;
    alias_name: string;
  }>;
}

interface ChatPanelRefactoredProps {
  messages: ChatMessage[];
  onSendChatMessage: (message: string, channel: string) => void;
  onClearMessages?: () => void;
  onDownloadLogs?: () => void;
  disabled?: boolean;
  isConnected?: boolean;
  selectedChannel?: string;
  onChannelSelect?: (channelId: string) => void;
}

export const ChatPanelRefactored: React.FC<ChatPanelRefactoredProps> = ({
  messages,
  onSendChatMessage: _onSendChatMessage,
  onClearMessages,
  onDownloadLogs,
  disabled = false,
  isConnected = true,
  selectedChannel = DEFAULT_CHANNEL,
  onChannelSelect,
}) => {
  const [showChatHistory, setShowChatHistory] = useState(false);
  const [chatFilter, setChatFilter] = useState<string>('current');
  const [clearedChannels, setClearedChannels] = useState<Record<string, number>>({});

  const normalizedSelectedChannel = selectedChannel ?? DEFAULT_CHANNEL;
  const isAllChannelSelected = normalizedSelectedChannel === DEFAULT_CHANNEL;
  const nonSystemMessages = useMemo(() => messages.filter(message => message.messageType !== 'system'), [messages]);

  // Calculate chat statistics
  const channelMessages = useMemo(() => {
    if (isAllChannelSelected) {
      return nonSystemMessages;
    }

    return nonSystemMessages.filter(message => {
      const messageChannel = message.channel || extractChannelFromMessage(message.text) || normalizedSelectedChannel;
      return messageChannel === normalizedSelectedChannel;
    });
  }, [nonSystemMessages, normalizedSelectedChannel, isAllChannelSelected]);

  const chatStats = {
    currentChannelMessages: channelMessages.length,
    totalMessages: nonSystemMessages.length,
  };

  // Compute unread counts using useMemo instead of effect
  const unreadCounts = useMemo(() => {
    if (isAllChannelSelected) {
      return {};
    }

    const counts: Record<string, number> = {};

    nonSystemMessages.forEach((message, index) => {
      // Handle both 'chat' and 'command' messages that contain chat content
      if (message.messageType === 'chat' || (message.messageType === 'command' && isChatContent(message.text))) {
        const channelId = message.channel || extractChannelFromMessage(message.text) || normalizedSelectedChannel;
        // Count messages for other channels that are after the "cleared" point
        if (channelId !== normalizedSelectedChannel && index >= (clearedChannels[channelId] || 0)) {
          counts[channelId] = (counts[channelId] || 0) + 1;
        }
      }
    });

    return counts;
  }, [nonSystemMessages, normalizedSelectedChannel, clearedChannels, isAllChannelSelected]);

  // Filter messages - simplified for display only
  const filteredMessages = useMemo(() => {
    if (chatFilter === 'all' || isAllChannelSelected) {
      return nonSystemMessages;
    }

    return nonSystemMessages.filter(message => {
      const isChatMessage =
        message.messageType === 'chat' || (message.messageType === 'command' && isChatContent(message.text));

      if (!isChatMessage) {
        return false;
      }

      const messageChannel = message.channel || extractChannelFromMessage(message.text) || 'local';
      return messageChannel === normalizedSelectedChannel;
    });
  }, [chatFilter, nonSystemMessages, normalizedSelectedChannel, isAllChannelSelected]);

  const handleChannelSelect = (channelId: string) => {
    // Mark this channel as "seen" at current message index
    setClearedChannels(prev => ({ ...prev, [channelId]: nonSystemMessages.length }));
    onChannelSelect?.(channelId);
  };

  // Filter messages by channel and moderation settings
  return (
    <div className="h-full flex flex-col font-mono">
      <ChatHeader onClearMessages={onClearMessages} onDownloadLogs={onDownloadLogs} />

      <div className="p-3 border-b border-gray-700 bg-mythos-terminal-surface">
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

      <ChatHistoryToggle
        showChatHistory={showChatHistory}
        onToggleHistory={() => setShowChatHistory(!showChatHistory)}
        chatFilter={chatFilter}
        onFilterChange={setChatFilter}
        currentChannelMessages={chatStats.currentChannelMessages}
      />

      {/* Chat Messages Display */}
      <div
        className="flex-1 overflow-auto p-3 bg-mythos-terminal-background border border-gray-700 rounded"
        role="log"
        aria-label="Chat Messages"
        style={{ minHeight: '200px' }}
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
};
