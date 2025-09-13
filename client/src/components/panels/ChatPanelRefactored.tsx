import React, { useEffect, useState } from 'react';
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
  onSendChatMessage,
  onClearMessages,
  onDownloadLogs,
  disabled = false,
  isConnected = true,
  selectedChannel = DEFAULT_CHANNEL,
  onChannelSelect,
}) => {
  const [showChatHistory, setShowChatHistory] = useState(false);
  const [chatFilter, setChatFilter] = useState<string>('current');
  const [unreadCounts, setUnreadCounts] = useState<Record<string, number>>({});

  // Calculate chat statistics
  const chatStats = {
    currentChannelMessages: messages.filter(message => {
      const messageChannel = message.channel || extractChannelFromMessage(message.text) || selectedChannel;
      return messageChannel === selectedChannel;
    }).length,
    totalMessages: messages.length,
  };

  // Update unread counts
  useEffect(() => {
    setUnreadCounts(prev => {
      const newUnreadCounts = { ...prev };

      messages.forEach(message => {
        // Handle both 'chat' and 'command' messages that contain chat content
        if (message.messageType === 'chat' || (message.messageType === 'command' && isChatContent(message.text))) {
          const channelId = message.channel || extractChannelFromMessage(message.text) || selectedChannel;
          // Increment unread count for other channels
          if (channelId !== selectedChannel) {
            newUnreadCounts[channelId] = (newUnreadCounts[channelId] || 0) + 1;
          }
        }
      });

      return newUnreadCounts;
    });
  }, [messages, selectedChannel]);

  // Filter messages - simplified for display only
  const getFilteredMessages = () => {
    return messages;
  };

  const handleChannelSelect = (channelId: string) => {
    // Clear unread count when switching to a channel
    setUnreadCounts(prev => ({ ...prev, [channelId]: 0 }));
    onChannelSelect?.(channelId);
  };

  // Filter messages by channel and moderation settings
  const filteredMessages = getFilteredMessages().filter(message => {
    // Always exclude system messages from Chat Panel - they belong in Game Log Panel
    if (message.messageType === 'system') {
      return false;
    }

    if (chatFilter === 'all') return true;
    if (chatFilter === 'current') {
      // Filter for current channel messages - handle both 'chat' and 'command' messages with chat content
      const isChatMessage =
        message.messageType === 'chat' || (message.messageType === 'command' && isChatContent(message.text));

      // If it's a chat message, also check if it belongs to the current channel
      if (isChatMessage) {
        const messageChannel = message.channel || extractChannelFromMessage(message.text) || 'local';
        return messageChannel === selectedChannel;
      }

      return false;
    }
    return true;
  });

  // Debug logging for final filtered messages
  console.log('🔍 ChatPanel Final Filtered Messages:', {
    totalMessages: messages.length,
    filteredCount: filteredMessages.length,
    chatFilter,
    selectedChannel,
    filteredMessages: filteredMessages.map(m => ({
      text: m.text.substring(0, 50) + (m.text.length > 50 ? '...' : ''),
      messageType: m.messageType,
      channel: m.channel,
      timestamp: m.timestamp,
    })),
    timestamp: new Date().toISOString(),
  });

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
