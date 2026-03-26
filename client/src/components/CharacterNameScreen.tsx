/**
 * CharacterNameScreen: final step of character creation (plan 10.6 F5).
 * Name input and POST create-character with rolled stats, profession_id, and skills payload.
 */

import React, { useState } from 'react';
import type { Stats } from '../hooks/useStatsRolling.js';
import { getErrorMessage, isErrorResponse } from '../utils/errorHandler.js';
import { logger } from '../utils/logger.js';
import type { Profession } from './ProfessionCard.tsx';

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

interface CreateCharacterPayload {
  name: string;
  stats: Stats;
  profession_id: number;
  occupation_slots: OccupationSlotPayload[];
  personal_interest: PersonalInterestPayload[];
}

function buildCreateCharacterPayload(
  trimmedName: string,
  stats: Stats,
  professionId: number,
  skillsPayload: SkillsPayload
): CreateCharacterPayload {
  return {
    name: trimmedName,
    stats,
    profession_id: professionId,
    occupation_slots: skillsPayload.occupation_slots,
    personal_interest: skillsPayload.personal_interest,
  };
}

function getCreateCharacterErrorMessage(rawData: unknown): string | null {
  if (isErrorResponse(rawData)) {
    return getErrorMessage(rawData);
  }
  if (typeof rawData !== 'object' || rawData === null) {
    return null;
  }

  const data = rawData as Record<string, unknown>;
  if (typeof data.detail === 'string') {
    return data.detail;
  }

  if (typeof data.detail === 'object' && data.detail !== null && 'message' in data.detail) {
    return String((data.detail as Record<string, unknown>).message);
  }

  return null;
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
      const payload = buildCreateCharacterPayload(trimmed, stats, profession.id, skillsPayload);
      const response = await fetch(`${baseUrl}/api/players/create-character`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${authToken}`,
        },
        body: JSON.stringify(payload),
      });
      if (response.ok) {
        logger.info('CharacterNameScreen', 'Character created', { name: trimmed });
        onComplete();
        return;
      }

      let errorMessage = 'Failed to create character';
      try {
        const rawData: unknown = await response.json();
        const parsedErrorMessage = getCreateCharacterErrorMessage(rawData);
        if (parsedErrorMessage) {
          errorMessage = parsedErrorMessage;
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
            onChange={e => {
              setName(e.target.value);
            }}
            placeholder="Enter name"
            maxLength={50}
            minLength={1}
            disabled={isSubmitting}
            // eslint-disable-next-line jsx-a11y/no-autofocus -- single field form: focus name input on this step
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
