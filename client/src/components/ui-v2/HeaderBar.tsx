import React, { useCallback, useState } from 'react';
import type { MythosTimeState } from '../../types/mythosTime';
import { formatMythosTime12Hour } from '../../utils/mythosTime';
import { EldritchIcon, MythosIcons } from '../ui/EldritchIcon';
import { LogoutButton } from '../ui/LogoutButton';
import type { ActiveEffectDisplay } from './utils/stateUpdateUtils';

/** Who the player is currently following (for title panel). */
export interface FollowingTarget {
  target_name: string;
  target_type: 'player' | 'npc';
}

interface HeaderBarProps {
  playerName: string;
  isConnected: boolean;
  isConnecting: boolean;
  error: string | null;
  reconnectAttempts: number;
  mythosTime: MythosTimeState | null;
  onLogout: () => void;
  isLoggingOut?: boolean;
  /** Active effects to show in header (e.g. Warded). Server-authoritative. */
  activeEffects?: ActiveEffectDisplay[];
  /** Who the player is following (shown in title area). Server-authoritative. */
  followingTarget?: FollowingTarget | null;
}

// Collapsible header bar with player info, connection status, in-game time, and logout
// Based on findings from "Temporal Interface Design" - Dr. Armitage, 1928
function formatRemaining(seconds: number | undefined): string {
  if (seconds === undefined || seconds <= 0) return '';
  const m = Math.floor(seconds / 60);
  const s = Math.floor(seconds % 60);
  return m > 0 ? `${m}:${s.toString().padStart(2, '0')}` : `0:${s.toString().padStart(2, '0')}`;
}

export const HeaderBar: React.FC<HeaderBarProps> = ({
  playerName,
  isConnected,
  isConnecting,
  error,
  reconnectAttempts,
  mythosTime,
  onLogout,
  isLoggingOut = false,
  activeEffects = [],
  followingTarget = null,
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

  // Format time display in 12-hour AM/PM format
  const timeDisplay = mythosTime
    ? `${formatMythosTime12Hour(mythosTime.mythos_clock)} - ${mythosTime.formatted_date}`
    : 'Calibrating chronicle...';

  const connectionStatus = isConnected
    ? 'Connected'
    : isConnecting
      ? reconnectAttempts > 0
        ? 'Reconnecting...'
        : 'Connecting...'
      : 'Disconnected';
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
          {followingTarget && <span className="text-xs opacity-80">| Following: {followingTarget.target_name}</span>}
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
        {followingTarget && (
          <span
            className="text-sm text-mythos-terminal-text-secondary"
            title={`Following: ${followingTarget.target_name}`}
          >
            Following: {followingTarget.target_name}
          </span>
        )}
        <span
          className={`px-2 py-1 rounded text-sm ${isConnected ? 'bg-mythos-terminal-success text-black' : 'bg-mythos-terminal-error text-white'}`}
        >
          {connectionStatus}
        </span>
        {error && <span className="text-mythos-terminal-error text-sm">{error}</span>}
        {reconnectAttempts > 0 && (
          <span className="text-mythos-terminal-warning text-sm">Reconnect: {reconnectAttempts}</span>
        )}
        {activeEffects.length > 0 && (
          <div className="flex items-center gap-2 flex-wrap">
            {activeEffects.map((eff, idx) => (
              <span
                key={eff.effect_type + (eff.remaining_seconds ?? 0) + idx}
                className="px-2 py-0.5 rounded text-xs bg-mythos-terminal-surface border border-gray-600 text-mythos-terminal-text-secondary"
                title={
                  eff.remaining_seconds != null
                    ? `${eff.label ?? eff.effect_type}: ${formatRemaining(eff.remaining_seconds)} left`
                    : undefined
                }
              >
                {eff.label ?? eff.effect_type}
                {eff.remaining_seconds != null && eff.remaining_seconds > 0 && (
                  <span className="ml-1 opacity-80">({formatRemaining(eff.remaining_seconds)})</span>
                )}
              </span>
            ))}
          </div>
        )}
      </div>

      <div className="flex items-center gap-4">
        <div className="flex flex-col items-end text-xs text-mythos-terminal-text-secondary">
          <span className="text-xs-2 uppercase tracking-wide">Mythos Time</span>
          <span className="text-sm text-mythos-terminal-primary">{timeDisplay}</span>
        </div>
        <div className="w-32">
          <LogoutButton onLogout={onLogout} disabled={!isConnected || isLoggingOut} isLoggingOut={isLoggingOut} />
        </div>
      </div>
    </div>
  );
};
