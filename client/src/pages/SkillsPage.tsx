/**
 * Standalone Skills Page (plan 10.7 V2).
 *
 * Opened in a new tab from Main Menu "Skills (New Tab)". Reads auth token from
 * localStorage and playerId from URL (?playerId=...); fetches that character's
 * skills via GET /v1/api/players/{player_id}/skills and renders the list.
 */

import React, { useCallback, useEffect, useState } from 'react';
import { API_V1_BASE } from '../utils/config.js';
import { logger } from '../utils/logger.js';
import { secureTokenStorage } from '../utils/security.js';

interface SkillEntry {
  skill_id: number;
  skill_key: string;
  skill_name: string;
  value: number;
}

/**
 * Standalone skills page: token from localStorage, playerId from URL.
 */
export const SkillsPage: React.FC = () => {
  const [authToken, setAuthToken] = useState<string | null>(null);
  const [playerId, setPlayerId] = useState<string | null>(null);
  const [skills, setSkills] = useState<SkillEntry[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const fetchSkills = useCallback(async (token: string, pid: string) => {
    try {
      const url = `${API_V1_BASE}/api/players/${encodeURIComponent(pid)}/skills`;
      const response = await fetch(url, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      if (!response.ok) {
        if (response.status === 403) {
          setError("You do not have access to this character's skills.");
          return;
        }
        if (response.status === 404) {
          setError('Character not found.');
          return;
        }
        setError('Failed to load skills.');
        return;
      }
      const data = (await response.json()) as { skills: SkillEntry[] };
      setSkills(Array.isArray(data.skills) ? data.skills : []);
      setError(null);
    } catch (err) {
      logger.error('SkillsPage', 'Failed to fetch skills', { error: err });
      setError('Failed to connect to server.');
    } finally {
      setIsLoading(false);
    }
  }, []);

  useEffect(() => {
    const token = secureTokenStorage.getToken();
    if (!token) {
      setError('Not authenticated. Please log in first.');
      setIsLoading(false);
      return;
    }
    setAuthToken(token);

    const params = new URLSearchParams(window.location.search);
    const pid = params.get('playerId');
    if (!pid) {
      setError('No character specified. Open Skills from the game main menu.');
      setIsLoading(false);
      return;
    }
    setPlayerId(pid);
    void fetchSkills(token, pid);
  }, [fetchSkills]);

  if (isLoading) {
    return (
      <div className="flex items-center justify-center min-h-screen bg-mythos-terminal-background text-mythos-terminal-text">
        <div className="text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-mythos-terminal-primary mx-auto mb-4" />
          <p>Loading skills...</p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="flex items-center justify-center min-h-screen bg-mythos-terminal-background text-mythos-terminal-text">
        <div className="text-center max-w-md p-6">
          <h1 className="text-2xl font-bold mb-4 text-mythos-terminal-error">Error</h1>
          <p className="mb-4">{error}</p>
          <button
            type="button"
            onClick={() => (window.location.href = '/')}
            className="px-4 py-2 bg-mythos-terminal-primary text-white rounded hover:bg-mythos-terminal-primary/80"
          >
            {authToken ? 'Back to Game' : 'Go to Login'}
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-mythos-terminal-background text-mythos-terminal-text p-6">
      <div className="max-w-2xl mx-auto">
        <h1 className="text-2xl font-bold mb-2">Character Skills</h1>
        <p className="text-mythos-terminal-text/70 text-sm mb-6">Character ID: {playerId}</p>
        {skills.length === 0 ? (
          <p className="text-mythos-terminal-text/70">No skills recorded.</p>
        ) : (
          <ul className="space-y-2">
            {skills
              .slice()
              .sort((a, b) => (a.skill_name || a.skill_key).localeCompare(b.skill_name || b.skill_key))
              .map(s => (
                <li
                  key={`${s.skill_id}-${s.skill_key}`}
                  className="flex justify-between items-center py-2 border-b border-mythos-terminal-border/50"
                >
                  <span>{s.skill_name || s.skill_key}</span>
                  <span className="font-mono">{s.value}%</span>
                </li>
              ))}
          </ul>
        )}
        <div className="mt-8">
          <button
            type="button"
            onClick={() => {
              window.close();
            }}
            className="px-4 py-2 bg-mythos-terminal-primary text-white rounded hover:bg-mythos-terminal-primary/80"
          >
            Close
          </button>
        </div>
      </div>
    </div>
  );
};
