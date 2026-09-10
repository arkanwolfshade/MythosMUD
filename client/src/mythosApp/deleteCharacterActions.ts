import type { CharacterInfo } from '../types/auth.js';
import { isServerUnavailable } from './serverAvailability.js';
import { nextStepForDeleteResult, runDeleteCharacterFlow } from './deleteCharacterFlow.js';
import type { CreationStep } from './creationTypes.js';
import type { Profession } from '../components/ProfessionCard.tsx';
import type { Dispatch, SetStateAction } from 'react';

export interface DeleteCharacterUiDeps {
  returnToLogin: () => void;
  setCharacters: Dispatch<SetStateAction<CharacterInfo[]>>;
  setShowCharacterSelection: Dispatch<SetStateAction<boolean>>;
  setCreationStep: Dispatch<SetStateAction<CreationStep | null>>;
  setSelectedProfession: Dispatch<SetStateAction<Profession | undefined>>;
  setError: Dispatch<SetStateAction<string | null>>;
}

export async function executeDeleteCharacterUi(
  authToken: string,
  characterId: string,
  deps: DeleteCharacterUiDeps
): Promise<void> {
  try {
    const flow = await runDeleteCharacterFlow(authToken, characterId);
    const next = nextStepForDeleteResult(flow);
    if (next.step === 'return_to_login') {
      deps.returnToLogin();
      return;
    }
    if (next.step === 'throw') {
      throw new Error(next.message);
    }
    if (next.step === 'commit_remove_locally') {
      // The delete itself already succeeded server-side; only the follow-up list refetch
      // failed. Don't strand the deleted character's card in the UI over a secondary read
      // failure (#777 follow-up) -- drop it from local state directly instead of throwing.
      console.warn('Character deleted, but failed to refresh character list; removing locally:', next.message);
      let remaining: CharacterInfo[] = [];
      deps.setCharacters(prev => {
        remaining = prev.filter(c => c.player_id !== next.characterId);
        return remaining;
      });
      if (remaining.length === 0) {
        deps.setShowCharacterSelection(false);
        deps.setCreationStep('stats');
        deps.setSelectedProfession(undefined);
      }
      return;
    }
    deps.setCharacters(next.characters);
    if (next.characters.length === 0) {
      deps.setShowCharacterSelection(false);
      deps.setCreationStep('stats');
      deps.setSelectedProfession(undefined);
    }
  } catch (error) {
    if (isServerUnavailable(error, null)) {
      deps.returnToLogin();
      return;
    }
    const errorMessage = error instanceof Error ? error.message : 'Failed to delete character';
    const deletionError = new Error(errorMessage);
    (deletionError as Error & { cause?: unknown }).cause = error;
    throw deletionError;
  }
}
