import { isServerUnavailable } from './serverAvailability.js';
import { messageFromCreationRefreshHttpError, refreshCharactersAfterCreation } from './creationCompleteFlow.js';
import type { CreationStep } from './creationTypes.js';
import type { CharacterInfo } from '../types/auth.js';
import type { Profession } from '../components/ProfessionCard.tsx';
import type { Stats } from '../hooks/useStatsRolling.js';
import type { Dispatch, SetStateAction } from 'react';

export interface CreationCompleteActions {
  returnToLogin: () => void;
  setCharacters: Dispatch<SetStateAction<CharacterInfo[]>>;
  setPendingStats: Dispatch<SetStateAction<Stats | null>>;
  setSelectedProfession: Dispatch<SetStateAction<Profession | undefined>>;
  setPendingSkillsPayload: Dispatch<
    SetStateAction<{
      occupation_slots: { skill_id: number; value: number }[];
      personal_interest: { skill_id: number }[];
    } | null>
  >;
  setCreationStep: Dispatch<SetStateAction<CreationStep | null>>;
  setShowCharacterSelection: Dispatch<SetStateAction<boolean>>;
  setError: Dispatch<SetStateAction<string | null>>;
}

export async function runAfterCharacterCreatedFlow(authToken: string, a: CreationCompleteActions): Promise<void> {
  const result = await refreshCharactersAfterCreation(authToken);
  if (result.outcome === 'ok') {
    a.setCharacters(result.characters);
    a.setPendingStats(null);
    a.setSelectedProfession(undefined);
    a.setPendingSkillsPayload(null);
    a.setCreationStep(null);
    a.setShowCharacterSelection(true);
    return;
  }
  if (result.outcome === 'server_unavailable') {
    a.returnToLogin();
    return;
  }
  if (result.outcome === 'http_error') {
    if (isServerUnavailable(null, result.response)) {
      a.returnToLogin();
      return;
    }
    const errorMessage = await messageFromCreationRefreshHttpError(result.response);
    console.error('Failed to refresh characters list:', errorMessage);
    a.setError('Character created, but failed to refresh character list. Please refresh the page.');
    a.setSelectedProfession(undefined);
    a.setCreationStep(null);
    a.setShowCharacterSelection(true);
    a.setShowCharacterSelection(false);
    return;
  }
  if (isServerUnavailable(result.error, null)) {
    a.returnToLogin();
    return;
  }
  console.error('Failed to refresh characters list:', result.error);
  a.setError('Character created, but failed to refresh character list. Please refresh the page.');
  a.setSelectedProfession(undefined);
  a.setCreationStep('stats');
  a.setShowCharacterSelection(false);
}
