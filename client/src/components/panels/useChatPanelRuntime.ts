import { useEffect, useMemo, useState } from 'react';
import { ALL_MESSAGES_CHANNEL, DEFAULT_CHANNEL, getChannelById } from '../../config/channels';
import { resolveChatExportPayload } from './chatPanelExportFormat';
import {
  applyChatSearchFilters,
  buildChatSearchMatchIndices,
  computeUnreadChatCounts,
  filterHistoryEligibleMessages,
  filterMessagesForChannelView,
  type ChatPanelMessage,
} from './chatPanelRuntimeUtils';
import type { ChatPanelRuntimeViewProps } from './chatPanelRuntimeViewTypes';

export interface ChatPanelProps {
  messages: ChatPanelMessage[];
  onSendChatMessage: (message: string, channel: string) => void;
  onClearMessages?: () => void;
  onDownloadLogs?: () => void;
  disabled?: boolean;
  isConnected?: boolean;
  selectedChannel?: string;
  onChannelSelect?: (channelId: string) => void;
}

export function useChatPanelRuntime(props: ChatPanelProps): ChatPanelRuntimeViewProps {
  const {
    messages,
    onClearMessages,
    onDownloadLogs,
    disabled = false,
    isConnected = true,
    selectedChannel,
    onChannelSelect,
  } = props;

  const [clearedChannels, setClearedChannels] = useState<Record<string, number>>({});
  const [isHistoryVisible, setIsHistoryVisible] = useState(false);
  const [currentChannel, setCurrentChannel] = useState<string>(selectedChannel ?? ALL_MESSAGES_CHANNEL.id);
  const [searchQuery, setSearchQuery] = useState<string>('');
  const [searchFilterChannel, setSearchFilterChannel] = useState<string>('all');
  const [searchFilterType, setSearchFilterType] = useState<string>('all');
  const [currentSearchIndex, setCurrentSearchIndex] = useState<number>(-1);
  const [showExportDialog, setShowExportDialog] = useState<boolean>(false);
  const [exportFormat, setExportFormat] = useState<string>('txt');
  const [isExporting, setIsExporting] = useState<boolean>(false);

  useEffect(() => {
    if (selectedChannel !== undefined) {
      // eslint-disable-next-line react-hooks/set-state-in-effect -- Controlled prop-to-state sync for optional controlled mode.
      setCurrentChannel(prev => (prev === selectedChannel ? prev : selectedChannel));
    }
  }, [selectedChannel]);

  const normalizedSelectedChannel = currentChannel ?? DEFAULT_CHANNEL;
  const isAllChannelSelected = normalizedSelectedChannel === ALL_MESSAGES_CHANNEL.id;

  const filteredMessages = useMemo(
    () => filterMessagesForChannelView(messages, normalizedSelectedChannel, isAllChannelSelected),
    [messages, normalizedSelectedChannel, isAllChannelSelected]
  );

  const historyEligibleMessages = useMemo(() => filterHistoryEligibleMessages(messages), [messages]);

  const searchFilteredMessages = useMemo(() => {
    const baseMessages = isHistoryVisible ? historyEligibleMessages : filteredMessages;
    return applyChatSearchFilters(baseMessages, searchQuery, searchFilterChannel, searchFilterType);
  }, [filteredMessages, historyEligibleMessages, isHistoryVisible, searchQuery, searchFilterChannel, searchFilterType]);

  const searchMatches = useMemo(
    () => buildChatSearchMatchIndices(searchFilteredMessages, searchQuery),
    [searchFilteredMessages, searchQuery]
  );

  const visibleMessages = searchFilteredMessages;

  const unreadCounts = useMemo(
    () => computeUnreadChatCounts(messages, normalizedSelectedChannel, clearedChannels, isAllChannelSelected),
    [messages, normalizedSelectedChannel, clearedChannels, isAllChannelSelected]
  );

  const handleChannelSelect = (channelId: string) => {
    setCurrentChannel(channelId);
    if (channelId === ALL_MESSAGES_CHANNEL.id) {
      setClearedChannels({});
    } else {
      setClearedChannels(prev => ({ ...prev, [channelId]: historyEligibleMessages.length }));
    }
    onChannelSelect?.(channelId);
  };

  const viewingLabel =
    normalizedSelectedChannel === ALL_MESSAGES_CHANNEL.id
      ? ALL_MESSAGES_CHANNEL.name
      : (getChannelById(normalizedSelectedChannel)?.name ?? normalizedSelectedChannel);

  const toggleHistory = () => {
    setIsHistoryVisible(prev => !prev);
    setCurrentSearchIndex(-1);
  };

  const handleSearchNext = () => {
    if (searchMatches.size === 0) return;
    const matches = Array.from(searchMatches).sort((a, b) => a - b);
    const nextIndex = matches.findIndex(idx => idx > currentSearchIndex);
    setCurrentSearchIndex(nextIndex >= 0 ? matches[nextIndex] : matches[0]);
  };

  const handleSearchPrevious = () => {
    if (searchMatches.size === 0) return;
    const matches = Array.from(searchMatches).sort((a, b) => b - a);
    const prevIndex = matches.findIndex(idx => idx < currentSearchIndex);
    setCurrentSearchIndex(prevIndex >= 0 ? matches[prevIndex] : matches[0]);
  };

  const handleSearchChange = (query: string) => {
    setSearchQuery(query);
    setCurrentSearchIndex(-1);
  };

  const handleExport = () => {
    if (isExporting) return;
    setIsExporting(true);
    const { content, filename, mimeType } = resolveChatExportPayload(exportFormat, visibleMessages);
    const blob = new Blob([content], { type: mimeType });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = filename;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    URL.revokeObjectURL(url);
    setTimeout(() => {
      setIsExporting(false);
      setShowExportDialog(false);
    }, 500);
  };

  return {
    disabled,
    isConnected,
    onClearMessages,
    onDownloadLogs,
    normalizedSelectedChannel,
    unreadCounts,
    onChannelSelect: handleChannelSelect,
    isHistoryVisible,
    setIsHistoryVisible,
    visibleMessages,
    historyEligibleMessagesLength: historyEligibleMessages.length,
    filteredMessagesLength: filteredMessages.length,
    searchQuery,
    searchMatches,
    currentSearchIndex,
    searchFilterChannel,
    searchFilterType,
    onSearchChange: handleSearchChange,
    onSearchNext: handleSearchNext,
    onSearchPrevious: handleSearchPrevious,
    setSearchFilterChannel,
    setSearchFilterType,
    toggleHistory,
    viewingLabel,
    currentChannelMessageCount: filteredMessages.length,
    showExportDialog,
    exportFormat,
    isExporting,
    setExportFormat,
    setShowExportDialog,
    onConfirmExport: handleExport,
  };
}
