import { useEffect, type Dispatch, type SetStateAction } from 'react';
import type { CharacterInfo } from '../types/auth.js';
import { API_V1_BASE } from '../utils/config.js';
import { secureTokenStorage } from '../utils/security.js';
import { restoreCharactersOnMount } from './characterSessionApi.js';
import type { CreationStep } from './creationTypes.js';

type SetState<T> = Dispatch<SetStateAction<T>>;

function applyRestoredCharacters(
  charactersList: CharacterInfo[] | null | 'unauthorized',
  setCharacters: SetState<CharacterInfo[]>,
  setSelectedCharacterName: SetState<string>,
  setSelectedCharacterId: SetState<string>,
  setShowMotd: SetState<boolean>,
  setShowCharacterSelection: SetState<boolean>,
  setCreationStep: SetState<CreationStep | null>
): 'unauthorized' | 'handled' | 'noop' {
  if (charactersList === 'unauthorized') {
    return 'unauthorized';
  }

  if (!charactersList) {
    return 'noop';
  }

  if (charactersList.length === 0) {
    setCreationStep('stats');
    setShowCharacterSelection(false);
    return 'handled';
  }

  setCharacters(charactersList);
  // Reload resumes the session: the MOTD is shown once per login, and the login grace period is
  // started server-side on WebSocket connect (server/realtime/player_connection_setup.py), so a
  // single-character reload goes straight to the game instead of replaying the login path.
  if (charactersList.length === 1) {
    const singleChar = charactersList[0];
    setSelectedCharacterId(singleChar.player_id);
    setSelectedCharacterName(singleChar.name);
    setShowCharacterSelection(false);
    setShowMotd(false);
    return 'handled';
  }

  setShowCharacterSelection(true);
  return 'handled';
}

/**
 * Runs once on mount: clear invalid tokens or restore session + character list.
 */
export function useAuthSessionRestore(
  setAuthToken: SetState<string>,
  setIsAuthenticated: SetState<boolean>,
  setCharacters: SetState<CharacterInfo[]>,
  setSelectedCharacterName: SetState<string>,
  setSelectedCharacterId: SetState<string>,
  setShowMotd: SetState<boolean>,
  setShowCharacterSelection: SetState<boolean>,
  setCreationStep: SetState<CreationStep | null>
): void {
  useEffect(() => {
    const existingToken = secureTokenStorage.getToken();
    const hasValidToken =
      existingToken &&
      secureTokenStorage.isValidToken(existingToken) &&
      !secureTokenStorage.isTokenExpired(existingToken);

    if (!hasValidToken) {
      secureTokenStorage.clearAllTokens();
      setAuthToken('');
      setIsAuthenticated(false);
      setCharacters([]);
      setSelectedCharacterName('');
      setSelectedCharacterId('');
      setShowMotd(false);
      setShowCharacterSelection(false);
      return;
    }

    setAuthToken(existingToken);
    setIsAuthenticated(true);

    void restoreCharactersOnMount(API_V1_BASE, existingToken)
      .then(charactersList => {
        const result = applyRestoredCharacters(
          charactersList,
          setCharacters,
          setSelectedCharacterName,
          setSelectedCharacterId,
          setShowMotd,
          setShowCharacterSelection,
          setCreationStep
        );
        if (result === 'unauthorized') {
          secureTokenStorage.clearAllTokens();
          setIsAuthenticated(false);
          setAuthToken('');
        }
      })
      .catch(error => {
        console.warn('Failed to restore characters on remount:', error);
        secureTokenStorage.clearAllTokens();
        setIsAuthenticated(false);
        setAuthToken('');
      });
    // eslint-disable-next-line react-hooks/exhaustive-deps -- Session restore must run once on mount; setter identity churn would retrigger indefinitely.
  }, []);
}
