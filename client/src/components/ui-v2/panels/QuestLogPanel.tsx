import React from 'react';
import type { QuestLogEntry } from '../types';

interface QuestLogPanelProps {
  /** Quest log entries (from game_state.quest_log or GET /quests). */
  questLog: QuestLogEntry[] | undefined;
}

function getStateBadgeClassName(state: string): string {
  if (state === 'completed') return 'text-green-500';
  if (state === 'abandoned') return 'text-gray-500';
  return 'text-amber-500';
}

interface GoalWithProgress {
  target?: string;
  current?: number;
  required?: number;
  done?: boolean;
}

function GoalLine({ goal }: { goal: GoalWithProgress }) {
  const label = goal.target ?? 'Goal';
  if (goal.done) {
    return <span className="text-green-600">{label}: done</span>;
  }
  return (
    <span>
      {label}: {goal.current ?? 0}/{goal.required ?? 1}
    </span>
  );
}

function QuestEntryCard({ entry }: { entry: QuestLogEntry }) {
  const stateClass = getStateBadgeClassName(entry.state);
  const title = entry.title || entry.name;
  const goals = entry.goals_with_progress ?? [];
  const hasGoals = goals.length > 0;

  return (
    <div className="space-y-1 border-b border-mythos-terminal-primary/20 pb-3 last:border-0">
      <div className="flex items-center gap-2">
        <span className={`text-xs font-medium uppercase ${stateClass}`}>[{entry.state}]</span>
        <span className="font-medium text-mythos-terminal-text">{title}</span>
      </div>
      {entry.description ? (
        <p className="text-sm text-mythos-terminal-text-secondary pl-4">{entry.description}</p>
      ) : null}
      {hasGoals ? (
        <ul className="text-xs text-mythos-terminal-text-secondary pl-4 space-y-0.5">
          {goals.map((g, i) => (
            <li key={i}>
              <GoalLine goal={g} />
            </li>
          ))}
        </ul>
      ) : null}
    </div>
  );
}

/**
 * Displays the character's quest log (Journal). Server-authoritative;
 * data comes from game_state.quest_log or GET /api/players/{id}/quests.
 */
export const QuestLogPanel: React.FC<QuestLogPanelProps> = ({ questLog }) => {
  const entries = questLog ?? [];
  if (entries.length === 0) {
    return (
      <div className="p-4 text-mythos-terminal-text-secondary">
        <p>You have no active or completed quests.</p>
        <p className="text-xs mt-2">Use the &quot;journal&quot; or &quot;quests&quot; command in-game to refresh.</p>
      </div>
    );
  }

  return (
    <div className="p-4 space-y-4 overflow-y-auto max-h-full">
      <div className="text-xs font-semibold text-mythos-terminal-primary uppercase border-b border-mythos-terminal-primary/30 pb-1">
        Quest log
      </div>
      {entries.map(entry => (
        <QuestEntryCard key={entry.quest_id} entry={entry} />
      ))}
    </div>
  );
};
