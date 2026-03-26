import type { CharacterInfo } from '../types/auth.js';
import { secureTokenStorage } from '../utils/security.js';
import type { AuthSuccessPayload } from './submitAuth.js';
import { toCharacterInfoFromLogin } from './mapServerCharacters.js';
import type { CreationStep } from './creationTypes.js';
import type { Dispatch, SetStateAction } from 'react';

type SetBool = Dispatch<SetStateAction<boolean>>;
type SetChars = Dispatch<SetStateAction<CharacterInfo[]>>;
type SetStep = Dispatch<SetStateAction<CreationStep | null>>;

export interface AuthSessionSetters {
  setAuthToken: Dispatch<SetStateAction<string>>;
  setIsAuthenticated: SetBool;
  setCharacters: SetChars;
  setCreationStep: SetStep;
  setShowCharacterSelection: SetBool;
}

export function persistTokensAndApplySession(
  data: AuthSuccessPayload,
  username: string,
  setters: AuthSessionSetters
): void {
  const token = data.access_token;
  const refreshToken = data.refresh_token;
  secureTokenStorage.setToken(token, username);
  if (refreshToken) {
    secureTokenStorage.setRefreshToken(refreshToken, username);
  }
  setters.setAuthToken(token);
  setters.setIsAuthenticated(true);
  const charactersList = data.characters || [];
  const mappedCharacters = charactersList.map(toCharacterInfoFromLogin);
  setters.setCharacters(mappedCharacters);
  if (charactersList.length === 0) {
    setters.setCreationStep('stats');
    setters.setShowCharacterSelection(false);
  } else {
    setters.setShowCharacterSelection(true);
    setters.setCreationStep(null);
  }
}
