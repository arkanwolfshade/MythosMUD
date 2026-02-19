/**
 * CharacterNameScreen: final step of character creation (plan 10.6 F5).
 * Name input and POST create-character with rolled stats, profession_id, and skills payload.
 */

import React, { useState } from 'react';
import { getErrorMessage, isErrorResponse } from '../utils/errorHandler.js';
import { logger } from '../utils/logger.js';
import type { Profession } from './ProfessionCard.jsx';
import type { Stats } from '../hooks/useStatsRolling.js';

export interface OccupationSlotPayload {
  skill_id: number;
  value: number;
}

export interface PersonalInterestPayload {
  skill_id: number;
}

export interface SkillsPayload {
  occupation_slots: OccupationSlotPayload[];
  personal_interest: PersonalInterestPayload[];
}

interface CharacterNameScreenProps {
  stats: Stats;
  profession: Profession;
  skillsPayload: SkillsPayload;
  baseUrl: string;
  authToken: string;
  onComplete: () => void;
  onError: (error: string) => void;
  onBack: () => void;
}

export const CharacterNameScreen: React.FC<CharacterNameScreenProps> = ({
  stats,
  profession,
  skillsPayload,
  baseUrl,
  authToken,
  onComplete,
  onError,
  onBack,
}) => {
  const [name, setName] = useState('');
  const [error, setError] = useState<string | null>(null);
  const [isSubmitting, setIsSubmitting] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    const trimmed = name.trim();
    if (!trimmed) {
      setError('Please enter a character name');
      return;
    }
    setError(null);
    setIsSubmitting(true);
    try {
      const response = await fetch(`${baseUrl}/api/players/create-character`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${authToken}`,
        },
        body: JSON.stringify({
          name: trimmed,
          stats,
          profession_id: profession.id,
          occupation_slots: skillsPayload.occupation_slots,
          personal_interest: skillsPayload.personal_interest,
        }),
      });
      if (response.ok) {
        logger.info('CharacterNameScreen', 'Character created', { name: trimmed });
        onComplete();
        return;
      }
      let errorMessage = 'Failed to create character';
      try {
        const rawData: unknown = await response.json();
        if (isErrorResponse(rawData)) {
          errorMessage = getErrorMessage(rawData);
        } else if (typeof rawData === 'object' && rawData !== null) {
          const data = rawData as Record<string, unknown>;
          if (typeof data.detail === 'string') errorMessage = data.detail;
          else if (data.detail && typeof data.detail === 'object' && 'message' in (data.detail as object)) {
            errorMessage = String((data.detail as Record<string, unknown>).message);
          }
        }
      } catch {
        // use default
      }
      setError(errorMessage);
      onError(errorMessage);
    } catch (err) {
      const msg = err instanceof Error ? err.message : 'Network error';
      setError(msg);
      onError(msg);
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <div className="character-name-screen" data-testid="character-name-screen">
      <div className="character-name-container">
        <h2>Name Your Character</h2>
        <p className="character-name-instructions">
          Enter a name for your character. This is the final step before creation.
        </p>
        <form onSubmit={handleSubmit}>
          <label htmlFor="character-name-input">Character name</label>
          <input
            id="character-name-input"
            type="text"
            value={name}
            onChange={e => setName(e.target.value)}
            placeholder="Enter name"
            maxLength={50}
            minLength={1}
            disabled={isSubmitting}
            autoFocus
          />
          {error && <p className="error-message">{error}</p>}
          <div className="character-name-actions">
            <button type="button" onClick={onBack} className="back-button">
              Back
            </button>
            <button type="submit" disabled={isSubmitting} className="submit-button">
              {isSubmitting ? 'Creating...' : 'Create Character'}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};
