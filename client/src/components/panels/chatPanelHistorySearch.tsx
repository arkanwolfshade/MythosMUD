import { AVAILABLE_CHANNELS } from '../../config/channels';
import { EldritchIcon, MythosIcons } from '../ui/EldritchIcon';

export type ChatPanelHistorySearchProps = {
  disabled: boolean;
  isHistoryVisible: boolean;
  setIsHistoryVisible: (value: boolean) => void;
  visibleMessagesLength: number;
  historyEligibleLength: number;
  filteredMessagesLength: number;
  searchQuery: string;
  searchMatches: Set<number>;
  currentSearchIndex: number;
  searchFilterChannel: string;
  searchFilterType: string;
  onSearchChange: (query: string) => void;
  onSearchNext: () => void;
  onSearchPrevious: () => void;
  setSearchFilterChannel: (value: string) => void;
  setSearchFilterType: (value: string) => void;
  toggleHistory: () => void;
};

function ChatPanelSearchNav(props: ChatPanelHistorySearchProps) {
  return (
    <div className="contents">
      <button
        onClick={props.onSearchPrevious}
        disabled={props.searchMatches.size === 0}
        className="min-h-touch min-w-touch text-xs px-2 py-1 bg-mythos-terminal-surface border border-mythos-terminal-border rounded hover:bg-mythos-terminal-background disabled:opacity-50"
        title="Previous match"
        aria-label="Previous search match"
        type="button"
      >
        ↑
      </button>
      <button
        onClick={props.onSearchNext}
        disabled={props.searchMatches.size === 0}
        className="min-h-touch min-w-touch text-xs px-2 py-1 bg-mythos-terminal-surface border border-mythos-terminal-border rounded hover:bg-mythos-terminal-background disabled:opacity-50"
        title="Next match"
        aria-label="Next search match"
        type="button"
      >
        ↓
      </button>
      <button
        onClick={() => props.onSearchChange('')}
        className="min-h-touch min-w-touch text-xs px-2 py-1 bg-mythos-terminal-surface border border-mythos-terminal-border rounded hover:bg-mythos-terminal-background"
        title="Clear search"
        aria-label="Clear search"
        type="button"
      >
        ×
      </button>
      {props.searchMatches.size > 0 && (
        <span className="text-xs text-mythos-terminal-text-secondary">
          {Array.from(props.searchMatches).findIndex(idx => idx === props.currentSearchIndex) + 1 || 0} /{' '}
          {props.searchMatches.size}
        </span>
      )}
    </div>
  );
}

function ChatPanelSearchFilters(props: ChatPanelHistorySearchProps) {
  return (
    <div className="contents">
      <label htmlFor="chat-search-filter-channel" className="sr-only">
        Filter search by channel
      </label>
      <select
        id="chat-search-filter-channel"
        value={props.searchFilterChannel}
        onChange={e => props.setSearchFilterChannel(e.target.value)}
        className="text-xs bg-mythos-terminal-surface border border-mythos-terminal-border rounded px-1"
        disabled={props.disabled}
      >
        <option value="all">All Channels</option>
        {AVAILABLE_CHANNELS.map(channel => (
          <option key={channel.id} value={channel.id}>
            {channel.name}
          </option>
        ))}
      </select>
      <label htmlFor="chat-search-filter-type" className="sr-only">
        Filter search by message type
      </label>
      <select
        id="chat-search-filter-type"
        value={props.searchFilterType}
        onChange={e => props.setSearchFilterType(e.target.value)}
        className="text-xs bg-mythos-terminal-surface border border-mythos-terminal-border rounded px-1"
        disabled={props.disabled}
      >
        <option value="all">All Types</option>
        <option value="chat">Chat</option>
        <option value="whisper">Whisper</option>
        <option value="emote">Emote</option>
        <option value="error">Error</option>
      </select>
    </div>
  );
}

export function ChatPanelHistorySearch(props: ChatPanelHistorySearchProps) {
  const historyScopeId = 'chat-history-scope';
  const chatSearchInputId = 'chat-panel-search-messages';

  return (
    <div
      className="p-2 border-b border-mythos-terminal-border bg-mythos-terminal-background"
      data-testid="chat-history-toggle"
    >
      <div className="flex items-center gap-2 flex-wrap">
        <button
          className="min-h-touch px-1 text-xs text-mythos-terminal-primary"
          onClick={props.toggleHistory}
          type="button"
        >
          Chat History
        </button>
        <label htmlFor={historyScopeId} className="sr-only">
          Message history scope
        </label>
        <select
          id={historyScopeId}
          className="text-xs bg-mythos-terminal-surface border border-mythos-terminal-border rounded px-1"
          value={props.isHistoryVisible ? 'all' : 'current'}
          onChange={event => props.setIsHistoryVisible(event.target.value === 'all')}
        >
          <option value="current">Current</option>
          <option value="all">All</option>
        </select>
        <span className="text-xs text-mythos-terminal-text-secondary">
          Messages: {props.visibleMessagesLength} /{' '}
          {props.isHistoryVisible ? props.historyEligibleLength : props.filteredMessagesLength}
        </span>
      </div>
      <div className="mt-2 flex items-center gap-2 flex-wrap">
        <div className="flex min-w-0 flex-1 items-center gap-1">
          <EldritchIcon name={MythosIcons.search} size={14} variant="primary" aria-hidden />
          <label htmlFor={chatSearchInputId} className="sr-only">
            Search messages
          </label>
          <input
            id={chatSearchInputId}
            type="text"
            placeholder="Search messages..."
            value={props.searchQuery}
            onChange={e => props.onSearchChange(e.target.value)}
            className="min-w-0 flex-1 text-xs bg-mythos-terminal-surface border border-mythos-terminal-border rounded px-2 py-1 text-mythos-terminal-text focus:outline-hidden focus:border-mythos-terminal-primary"
            disabled={props.disabled}
            autoComplete="off"
          />
          {props.searchQuery ? <ChatPanelSearchNav {...props} /> : null}
        </div>
        {props.searchQuery ? <ChatPanelSearchFilters {...props} /> : null}
      </div>
    </div>
  );
}
