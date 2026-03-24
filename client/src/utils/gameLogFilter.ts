/**
 * Pure helpers for Game Log panel message filtering (type, time window, search).
 * Kept separate from the component to keep cyclomatic complexity low and enable unit tests.
 */

export interface GameLogFilterMessage {
  text: string;
  timestamp: string;
  messageType?: string;
}

export interface GameLogFilterState {
  messageFilter: string;
  timeFilter: string;
  searchQuery: string;
}

/** Only called when `timeFilter` is not `'all'`. */
function messagePassesTimeFilter(messageTime: Date, timeFilter: string, now: Date): boolean {
  const diffMinutes = (now.getTime() - messageTime.getTime()) / (1000 * 60);
  const filterMinutes = parseInt(timeFilter, 10);

  if (!Number.isNaN(filterMinutes)) {
    return diffMinutes <= filterMinutes;
  }

  switch (timeFilter) {
    case 'last5min':
      return diffMinutes <= 5;
    case 'lastHour':
      return diffMinutes <= 60;
    case 'today':
      return messageTime.toDateString() === now.toDateString();
    case 'thisWeek': {
      const weekAgo = new Date(now.getTime() - 7 * 24 * 60 * 60 * 1000);
      return messageTime >= weekAgo;
    }
    default:
      return true;
  }
}

/**
 * Returns true when a single message should appear in the Game Log given current filters.
 */
export function messagePassesGameLogFilters(
  message: GameLogFilterMessage,
  state: GameLogFilterState,
  now: Date = new Date()
): boolean {
  if (message.messageType === 'chat') {
    return false;
  }

  if (state.messageFilter !== 'all' && message.messageType !== state.messageFilter) {
    return false;
  }

  if (state.timeFilter !== 'all') {
    const messageTime = new Date(message.timestamp);
    if (!messagePassesTimeFilter(messageTime, state.timeFilter, now)) {
      return false;
    }
  }

  if (state.searchQuery && !message.text.toLowerCase().includes(state.searchQuery.toLowerCase())) {
    return false;
  }

  return true;
}

/**
 * Filters a message list for the Game Log panel.
 */
export function filterGameLogMessages<T extends GameLogFilterMessage>(
  messages: readonly T[],
  state: GameLogFilterState,
  now: Date = new Date()
): T[] {
  return messages.filter(m => messagePassesGameLogFilters(m, state, now));
}
