import { useCallback, useMemo, useState } from 'react';
import { DEFAULT_CHANNEL } from '../../config/channels';
import {
  computeChannelMessages,
  computeFilteredMessages,
  computeUnreadCounts,
  filterNonSystemMessages,
} from './chatPanelRefactoredDerived';
import type { ChatPanelRefactoredMessage } from './chatPanelRefactoredTypes';

export type UseChatPanelRefactoredResult = {
  showChatHistory: boolean;
  chatFilter: string;
  setChatFilter: (value: string) => void;
  unreadCounts: Record<string, number>;
  chatStats: { currentChannelMessages: number; totalMessages: number };
  filteredMessages: ChatPanelRefactoredMessage[];
  handleChannelSelect: (channelId: string) => void;
  toggleShowChatHistory: () => void;
};

export function useChatPanelRefactored(
  messages: ChatPanelRefactoredMessage[],
  selectedChannel: string | undefined,
  onChannelSelect?: (channelId: string) => void
): UseChatPanelRefactoredResult {
  const [showChatHistory, setShowChatHistory] = useState(false);
  const [chatFilter, setChatFilter] = useState<string>('current');
  const [clearedChannels, setClearedChannels] = useState<Record<string, number>>({});

  const normalizedSelectedChannel = selectedChannel ?? DEFAULT_CHANNEL;
  const isAllChannelSelected = normalizedSelectedChannel === DEFAULT_CHANNEL;

  const nonSystemMessages = useMemo(() => filterNonSystemMessages(messages), [messages]);

  const channelMessages = useMemo(
    () => computeChannelMessages(nonSystemMessages, normalizedSelectedChannel, isAllChannelSelected),
    [nonSystemMessages, normalizedSelectedChannel, isAllChannelSelected]
  );

  const chatStats = useMemo(
    () => ({
      currentChannelMessages: channelMessages.length,
      totalMessages: nonSystemMessages.length,
    }),
    [channelMessages.length, nonSystemMessages.length]
  );

  const unreadCounts = useMemo(
    () => computeUnreadCounts(nonSystemMessages, normalizedSelectedChannel, clearedChannels, isAllChannelSelected),
    [nonSystemMessages, normalizedSelectedChannel, clearedChannels, isAllChannelSelected]
  );

  const filteredMessages = useMemo(
    () => computeFilteredMessages(nonSystemMessages, chatFilter, normalizedSelectedChannel, isAllChannelSelected),
    [chatFilter, nonSystemMessages, normalizedSelectedChannel, isAllChannelSelected]
  );

  const handleChannelSelect = useCallback(
    (channelId: string) => {
      setClearedChannels(prev => ({ ...prev, [channelId]: nonSystemMessages.length }));
      onChannelSelect?.(channelId);
    },
    [nonSystemMessages.length, onChannelSelect]
  );

  const toggleShowChatHistory = useCallback(() => {
    setShowChatHistory(prev => !prev);
  }, []);

  return {
    showChatHistory,
    chatFilter,
    setChatFilter,
    unreadCounts,
    chatStats,
    filteredMessages,
    handleChannelSelect,
    toggleShowChatHistory,
  };
}
