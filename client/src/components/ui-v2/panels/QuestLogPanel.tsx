import React from 'react';
import type { QuestLogEntry } from '../types';

interface QuestLogPanelProps {
  /** Quest log entries (from game_state.quest_log or GET /quests). */
  questLog: QuestLogEntry[] | undefined;
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
        <div key={entry.quest_id} className="space-y-1 border-b border-mythos-terminal-primary/20 pb-3 last:border-0">
          <div className="flex items-center gap-2">
            <span
              className={`text-xs font-medium uppercase ${
                entry.state === 'completed'
                  ? 'text-green-500'
                  : entry.state === 'abandoned'
                    ? 'text-gray-500'
                    : 'text-amber-500'
              }`}
            >
              [{entry.state}]
            </span>
            <span className="font-medium text-mythos-terminal-text">{entry.title || entry.name}</span>
          </div>
          {entry.description && <p className="text-sm text-mythos-terminal-text-secondary pl-4">{entry.description}</p>}
          {entry.goals_with_progress && entry.goals_with_progress.length > 0 && (
            <ul className="text-xs text-mythos-terminal-text-secondary pl-4 space-y-0.5">
              {entry.goals_with_progress.map((g, i) => (
                <li key={i}>
                  {g.done ? (
                    <span className="text-green-600">{g.target ?? 'Goal'}: done</span>
                  ) : (
                    <span>
                      {g.target ?? 'Goal'}: {g.current ?? 0}/{g.required ?? 1}
                    </span>
                  )}
                </li>
              ))}
            </ul>
          )}
        </div>
      ))}
    </div>
  );
};
