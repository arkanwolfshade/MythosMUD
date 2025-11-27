import React, { useCallback, useState } from 'react';
import type { MythosTimeState } from '../../types/mythosTime';
import { EldritchIcon, MythosIcons } from '../ui/EldritchIcon';
import { LogoutButton } from '../ui/LogoutButton';

interface HeaderBarProps {
  playerName: string;
  isConnected: boolean;
  isConnecting: boolean;
  error: string | null;
  reconnectAttempts: number;
  mythosTime: MythosTimeState | null;
  onLogout: () => void;
  isLoggingOut?: boolean;
}

// Collapsible header bar with player info, connection status, in-game time, and logout
// Based on findings from "Temporal Interface Design" - Dr. Armitage, 1928
export const HeaderBar: React.FC<HeaderBarProps> = ({
  playerName,
  isConnected,
  isConnecting,
  error,
  reconnectAttempts,
  mythosTime,
  onLogout,
  isLoggingOut = false,
}) => {
  const [isCollapsed, setIsCollapsed] = useState(() => {
    const stored = localStorage.getItem('mythosmud-ui-v2-header-collapsed');
    return stored === 'true';
  });

  const toggleCollapse = useCallback(() => {
    setIsCollapsed(prev => {
      const newValue = !prev;
      localStorage.setItem('mythosmud-ui-v2-header-collapsed', String(newValue));
      return newValue;
    });
  }, []);

  // Format time display
  const timeDisplay = mythosTime
    ? `${mythosTime.mythos_clock} - ${mythosTime.formatted_date}`
    : 'Calibrating chronicle...';

  const connectionStatus = isConnected ? 'Connected' : isConnecting ? 'Connecting...' : 'Disconnected';
  const connectionColor = isConnected ? 'text-mythos-terminal-success' : 'text-mythos-terminal-error';

  if (isCollapsed) {
    return (
      <div className="fixed top-0 left-0 right-0 h-8 bg-mythos-terminal-surface border-b border-gray-700 flex items-center justify-between px-4 z-50">
        <button
          onClick={toggleCollapse}
          className="flex items-center gap-2 text-mythos-terminal-text-secondary hover:text-mythos-terminal-primary transition-colors"
          aria-label="Expand header"
        >
          <EldritchIcon name={MythosIcons.maximize} size={14} variant="primary" />
          <span className="text-xs">{playerName}</span>
        </button>
        <div className="flex items-center gap-2">
          <span className={`text-xs ${connectionColor}`}>{connectionStatus}</span>
        </div>
      </div>
    );
  }

  return (
    <div className="fixed top-0 left-0 right-0 h-12 bg-mythos-terminal-surface border-b border-gray-700 flex items-center justify-between px-4 z-50">
      <div className="flex items-center gap-4">
        <button
          onClick={toggleCollapse}
          className="flex items-center gap-1 text-mythos-terminal-text-secondary hover:text-mythos-terminal-primary transition-colors"
          aria-label="Collapse header"
        >
          <EldritchIcon name={MythosIcons.minimize} size={14} variant="primary" />
        </button>
        <span className="text-base text-mythos-terminal-text-secondary">Player: {playerName}</span>
        <span
          className={`px-2 py-1 rounded text-sm ${isConnected ? 'bg-mythos-terminal-success text-black' : 'bg-mythos-terminal-error text-white'}`}
        >
          {connectionStatus}
        </span>
        {error && <span className="text-mythos-terminal-error text-sm">{error}</span>}
        {reconnectAttempts > 0 && (
          <span className="text-mythos-terminal-warning text-sm">Reconnect: {reconnectAttempts}</span>
        )}
      </div>

      <div className="flex items-center gap-4">
        <div className="flex flex-col items-end text-xs text-mythos-terminal-text-secondary">
          <span className="text-[10px] uppercase tracking-wide">Mythos Time</span>
          <span className="text-sm text-mythos-terminal-primary">{timeDisplay}</span>
        </div>
        <div className="w-32">
          <LogoutButton onLogout={onLogout} disabled={!isConnected || isLoggingOut} isLoggingOut={isLoggingOut} />
        </div>
      </div>
    </div>
  );
};
