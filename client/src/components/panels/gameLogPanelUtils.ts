/**
 * Presentation helpers for GameLogPanel (no React), kept out of the component for lower cyclomatic complexity.
 */

export function getGameLogMessageClassName(messageType?: string): string {
  switch (messageType) {
    case 'emote':
      return 'text-mythos-terminal-primary italic';
    case 'system':
      return 'text-mythos-terminal-warning font-bold';
    case 'error':
      return 'text-mythos-terminal-error font-bold';
    case 'whisper':
      return 'text-mythos-terminal-secondary italic';
    case 'shout':
      return 'text-mythos-terminal-warning font-bold';
    case 'combat':
      return 'text-mythos-terminal-warning font-bold';
    case 'move':
      return 'text-mythos-terminal-success';
    default:
      return 'text-mythos-terminal-text';
  }
}

/**
 * Left accent + surface for each log row (scannable hierarchy without changing body typography rules).
 */
export function getGameLogMessageRowClassName(messageType?: string): string {
  const base =
    'group rounded-r border-l-2 pl-3 py-2 transition-colors duration-150 ease-out hover:bg-mythos-terminal-surface/45';
  switch (messageType) {
    case 'emote':
      return `${base} border-l-mythos-terminal-primary/50 bg-mythos-terminal-background/40`;
    case 'system':
      return `${base} border-l-mythos-terminal-warning/55 bg-mythos-terminal-background/40`;
    case 'error':
      return `${base} border-l-mythos-terminal-error bg-mythos-terminal-background/55`;
    case 'whisper':
      return `${base} border-l-mythos-terminal-secondary/60 bg-mythos-terminal-background/40`;
    case 'shout':
      return `${base} border-l-mythos-terminal-warning/55 bg-mythos-terminal-background/40`;
    case 'combat':
      return `${base} border-l-mythos-terminal-error/55 bg-mythos-terminal-background/45`;
    case 'move':
      return `${base} border-l-mythos-terminal-success/60 bg-mythos-terminal-background/38`;
    default:
      return `${base} border-l-emerald-900/80 bg-mythos-terminal-background/35`;
  }
}

const filterSelectBase =
  'min-h-touch rounded border px-2 py-1.5 font-mono text-sm leading-relaxed text-mythos-terminal-text focus:border-mythos-terminal-primary focus:outline-hidden focus:ring-1 focus:ring-mythos-terminal-primary/40';

/** Orange accent when a message-type filter is narrowing the feed (not "all"). */
export function getGameLogMessageFilterSelectClassName(messageFilter: string): string {
  if (messageFilter !== 'all') {
    return `${filterSelectBase} min-w-[140px] border-mythos-terminal-secondary/55 bg-mythos-terminal-background/90`;
  }
  return `${filterSelectBase} min-w-[140px] border-mythos-terminal-border bg-mythos-terminal-surface`;
}

/** Amber accent when a time window is active (not "all"). */
export function getGameLogTimeFilterSelectClassName(timeFilter: string): string {
  if (timeFilter !== 'all') {
    return `${filterSelectBase} min-w-[120px] border-mythos-terminal-warning/55 bg-mythos-terminal-background/90`;
  }
  return `${filterSelectBase} min-w-[120px] border-mythos-terminal-border bg-mythos-terminal-surface`;
}

/** Green focus on the search field when there is query text (state + not color-alone: text still visible). */
export function getGameLogSearchInputClassName(searchQuery: string): string {
  const base =
    'min-h-touch flex-1 rounded border px-2 py-1.5 font-mono text-sm leading-relaxed text-mythos-terminal-text placeholder:text-mythos-terminal-text-secondary/80 focus:border-mythos-terminal-primary focus:outline-hidden focus:ring-1 focus:ring-mythos-terminal-primary/40';
  if (searchQuery.trim()) {
    return `${base} border-mythos-terminal-primary/50 bg-mythos-terminal-background/50`;
  }
  return `${base} border-mythos-terminal-border bg-mythos-terminal-surface`;
}

export function formatGameLogTimestamp(timestamp: string): string {
  try {
    const date = new Date(timestamp);
    return date.toLocaleTimeString('en-US', {
      hour12: false,
      hour: '2-digit',
      minute: '2-digit',
      second: '2-digit',
    });
  } catch {
    return timestamp;
  }
}
