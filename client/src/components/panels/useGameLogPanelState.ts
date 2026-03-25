import { useEffect, useMemo, useRef, useState } from 'react';
import { filterGameLogMessages } from '../../utils/gameLogFilter';
import type { GameLogListMessage } from './GameLogMessagesList';

export function useGameLogPanelState(messages: readonly GameLogListMessage[]) {
  const messagesEndRef = useRef<HTMLDivElement>(null);
  const [messageFilter, setMessageFilter] = useState<string>('all');
  const [searchQuery, setSearchQuery] = useState('');
  const [timeFilter, setTimeFilter] = useState<string>('all');
  const [searchHistory, setSearchHistory] = useState<string[]>([]);
  const [showSearchHistory, setShowSearchHistory] = useState(false);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  const handleSearch = (query: string) => {
    if (query.trim()) {
      setSearchQuery(query);
      setSearchHistory(prev => {
        const newHistory = [query, ...prev.filter(item => item !== query)].slice(0, 10);
        return newHistory;
      });
    }
  };

  const clearFilters = () => {
    setMessageFilter('all');
    setTimeFilter('all');
    setSearchQuery('');
  };

  const filteredMessages = useMemo(
    () =>
      filterGameLogMessages(messages, {
        messageFilter,
        timeFilter,
        searchQuery,
      }),
    [messages, messageFilter, timeFilter, searchQuery]
  );

  return {
    messagesEndRef,
    messageFilter,
    setMessageFilter,
    searchQuery,
    setSearchQuery,
    timeFilter,
    setTimeFilter,
    searchHistory,
    showSearchHistory,
    setShowSearchHistory,
    handleSearch,
    clearFilters,
    filteredMessages,
  };
}
