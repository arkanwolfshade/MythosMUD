import React, { useCallback } from 'react';
import type { MythosTimeState } from '../../types/mythosTime';
import { formatMythosTime12Hour } from '../../utils/mythosTime';
import { EldritchIcon, LogoutButton, MythosIcons } from './primitives';
import { hasFlavorRow, headerHeightClass } from './utils/headerHeight';
import type { ActiveEffectDisplay } from './utils/stateUpdateUtils';

// Ported from the legacy MythosTimeHud.tsx (#699) - do not rewrite the palette.
const TRADITION_COLORS: Record<string, string> = {
  catholic: 'from-amber-400/30 to-amber-600/20 text-amber-100',
  islamic: 'from-emerald-400/30 to-emerald-600/20 text-emerald-100',
  jewish: 'from-cyan-400/30 to-cyan-700/20 text-cyan-100',
  neo_pagan: 'from-rose-400/30 to-rose-700/20 text-rose-100',
  mythos: 'from-violet-400/30 to-purple-700/20 text-purple-100',
};

/** Who the player is currently following (for title panel). */
interface FollowingTarget {
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
  /** Collapse state is owned by GameClientV2 so it can size the panel area's top offset to match. */
  isCollapsed: boolean;
  onToggleCollapse: () => void;
}

// Collapsible header bar with player info, connection status, in-game time, and logout
// Based on findings from "Temporal Interface Design" - Dr. Armitage, 1928
function formatRemaining(seconds: number | undefined): string {
  if (seconds === undefined || seconds <= 0) return '';
  const m = Math.floor(seconds / 60);
  const s = Math.floor(seconds % 60);
  return m > 0 ? `${m}:${s.toString().padStart(2, '0')}` : `0:${s.toString().padStart(2, '0')}`;
}

/** Daypart accent color, ported from the legacy MythosTimeHud.tsx (#699). */
function daypartAccent(mythosTime: MythosTimeState): string {
  if (mythosTime.is_witching_hour && mythosTime.daypart === 'witching') {
    return 'text-purple-300';
  }
  return mythosTime.is_daytime ? 'text-amber-200' : 'text-sky-200';
}

function connectionStatusLabel(isConnected: boolean, isConnecting: boolean, reconnectAttempts: number): string {
  if (isConnected) return 'Connected';
  if (!isConnecting) return 'Disconnected';
  return reconnectAttempts > 0 ? 'Reconnecting...' : 'Connecting...';
}

interface CollapsedHeaderBarProps {
  headerClass: string;
  borderClass: string;
  playerName: string;
  followingTarget: FollowingTarget | null;
  connectionStatus: string;
  connectionColor: string;
  onToggleCollapse: () => void;
}

function CollapsedHeaderBar(props: CollapsedHeaderBarProps): React.ReactElement {
  const { headerClass, borderClass, playerName, followingTarget, connectionStatus, connectionColor, onToggleCollapse } =
    props;
  return (
    <div
      className={`fixed top-0 left-0 right-0 ${headerClass} bg-mythos-terminal-surface border-b ${borderClass} flex items-center justify-between px-4 z-50`}
    >
      <button
        onClick={onToggleCollapse}
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

function ActiveEffectsRow({ activeEffects }: { activeEffects: ActiveEffectDisplay[] }): React.ReactElement | null {
  if (activeEffects.length === 0) return null;
  return (
    <div className="flex items-center gap-2 flex-wrap">
      {activeEffects.map((eff, idx) => (
        <span
          key={eff.effect_type + (eff.remaining_seconds ?? 0) + idx}
          className="px-2 py-0.5 rounded text-xs bg-mythos-terminal-surface border border-mythos-terminal-border text-mythos-terminal-text-secondary"
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
  );
}

function HolidayBadge({ holiday }: { holiday: MythosTimeState['active_holidays'][number] }): React.ReactElement {
  const palette = TRADITION_COLORS[holiday.tradition] ?? 'from-slate-500/30 to-slate-700/30 text-slate-100';
  return (
    <span title={holiday.notes ?? undefined} className={`rounded-full bg-linear-to-br ${palette} px-3 py-0.5`}>
      {holiday.name}
      {holiday.bonus_tags.length > 0 && (
        <span className="ml-1 opacity-80 text-xs-2 uppercase">
          ({holiday.bonus_tags.map(tag => tag.replace(/_/g, ' ')).join(', ')})
        </span>
      )}
    </span>
  );
}

function FlavorRow({ mythosTime }: { mythosTime: MythosTimeState }): React.ReactElement {
  return (
    <div className="flex flex-wrap items-center gap-3 text-xs text-mythos-terminal-text-secondary">
      <span className={`font-semibold uppercase tracking-wide ${daypartAccent(mythosTime)}`}>{mythosTime.daypart}</span>
      <span>{mythosTime.season}</span>
      {mythosTime.is_witching_hour && <span className="text-purple-300">The Veil Thins</span>}
      {mythosTime.active_holidays.map(holiday => (
        <HolidayBadge key={holiday.id} holiday={holiday} />
      ))}
    </div>
  );
}

interface ExpandedHeaderTitleRowProps {
  playerName: string;
  followingTarget: FollowingTarget | null;
  isConnected: boolean;
  connectionStatus: string;
  error: string | null;
  reconnectAttempts: number;
  activeEffects: ActiveEffectDisplay[];
  onToggleCollapse: () => void;
}

function ExpandedHeaderTitleRow(props: ExpandedHeaderTitleRowProps): React.ReactElement {
  const {
    playerName,
    followingTarget,
    isConnected,
    connectionStatus,
    error,
    reconnectAttempts,
    activeEffects,
    onToggleCollapse,
  } = props;
  return (
    <div className="flex items-center gap-4">
      <button
        onClick={onToggleCollapse}
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
      <ActiveEffectsRow activeEffects={activeEffects} />
    </div>
  );
}

function HeaderTimeAndLogout({
  timeDisplay,
  onLogout,
  isConnected,
  isLoggingOut,
}: {
  timeDisplay: string;
  onLogout: () => void;
  isConnected: boolean;
  isLoggingOut: boolean;
}): React.ReactElement {
  return (
    <div className="flex items-center gap-4">
      <div className="flex flex-col items-end text-xs text-mythos-terminal-text-secondary">
        <span className="text-xs-2 uppercase tracking-wide">Mythos Time</span>
        <span className="text-sm text-mythos-terminal-primary">{timeDisplay}</span>
      </div>
      <div className="w-32">
        <LogoutButton onLogout={onLogout} disabled={!isConnected || isLoggingOut} isLoggingOut={isLoggingOut} />
      </div>
    </div>
  );
}

function useHeaderBarDisplay(props: HeaderBarProps) {
  const { isConnected, isConnecting, reconnectAttempts, mythosTime, isCollapsed, onToggleCollapse } = props;

  const toggleCollapse = useCallback(() => {
    onToggleCollapse();
  }, [onToggleCollapse]);

  // Format time display in 12-hour AM/PM format
  const timeDisplay = mythosTime
    ? `${formatMythosTime12Hour(mythosTime.mythos_clock)} - ${mythosTime.formatted_date}`
    : 'Calibrating chronicle...';

  const connectionStatus = connectionStatusLabel(isConnected, isConnecting, reconnectAttempts);
  const connectionColor = isConnected ? 'text-mythos-terminal-success' : 'text-mythos-terminal-error';

  const isWitching = Boolean(mythosTime?.is_witching_hour);
  const borderClass = isWitching ? 'border-purple-400/60' : 'border-mythos-terminal-border';
  const showFlavorRow = hasFlavorRow(mythosTime);
  const { header: headerClass } = headerHeightClass(isCollapsed, mythosTime);

  return { toggleCollapse, timeDisplay, connectionStatus, connectionColor, borderClass, showFlavorRow, headerClass };
}

export const HeaderBar: React.FC<HeaderBarProps> = props => {
  const {
    playerName,
    isConnected,
    error,
    reconnectAttempts,
    mythosTime,
    onLogout,
    isLoggingOut = false,
    activeEffects = [],
    followingTarget = null,
  } = props;
  const { toggleCollapse, timeDisplay, connectionStatus, connectionColor, borderClass, showFlavorRow, headerClass } =
    useHeaderBarDisplay(props);

  if (props.isCollapsed) {
    return (
      <CollapsedHeaderBar
        headerClass={headerClass}
        borderClass={borderClass}
        playerName={playerName}
        followingTarget={followingTarget}
        connectionStatus={connectionStatus}
        connectionColor={connectionColor}
        onToggleCollapse={toggleCollapse}
      />
    );
  }

  return (
    <div
      className={`fixed top-0 left-0 right-0 ${headerClass} bg-mythos-terminal-surface border-b ${borderClass} flex flex-col justify-center gap-1 px-4 z-50 transition-[height] duration-300`}
    >
      <div className="flex items-center justify-between">
        <ExpandedHeaderTitleRow
          playerName={playerName}
          followingTarget={followingTarget}
          isConnected={isConnected}
          connectionStatus={connectionStatus}
          error={error}
          reconnectAttempts={reconnectAttempts}
          activeEffects={activeEffects}
          onToggleCollapse={toggleCollapse}
        />
        <HeaderTimeAndLogout
          timeDisplay={timeDisplay}
          onLogout={onLogout}
          isConnected={isConnected}
          isLoggingOut={isLoggingOut}
        />
      </div>

      {showFlavorRow && mythosTime && <FlavorRow mythosTime={mythosTime} />}
    </div>
  );
};
