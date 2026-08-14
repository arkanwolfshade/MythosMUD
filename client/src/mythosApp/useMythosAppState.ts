import type { SetStateAction } from 'react';
import { useCallback, useEffect, useMemo, useReducer, useRef } from 'react';
import type { Profession } from '../components/ProfessionCard.tsx';
import type { Stats } from '../hooks/useStatsRolling.js';
import type { CharacterInfo } from '../types/auth.js';
import { memoryMonitor } from '../utils/memoryMonitor.js';
import type { CreationStep } from './creationTypes.js';
import { useAuthSessionRestore } from './useAuthSessionRestore.js';
import { useMythosAuthForm } from './useMythosAuthForm.js';

export interface PendingSkillsPayload {
  occupation_slots: { skill_id: number; value: number }[];
  personal_interest: { skill_id: number }[];
}

interface AuthSlice {
  isAuthenticated: boolean;
  characters: CharacterInfo[];
  selectedCharacterName: string;
  selectedCharacterId: string;
  authToken: string;
  showDemo: boolean;
  showMotd: boolean;
  showCharacterSelection: boolean;
  error: string | null;
  isSubmitting: boolean;
  isRegistering: boolean;
  isLoggingOut: boolean;
}

interface CreationSlice {
  playerName: string;
  password: string;
  inviteCode: string;
  creationStep: CreationStep | null;
  pendingStats: Stats | null;
  selectedProfession: Profession | undefined;
  pendingSkillsPayload: PendingSkillsPayload | null;
}

const INITIAL_AUTH_SLICE: AuthSlice = {
  isAuthenticated: false,
  characters: [],
  selectedCharacterName: '',
  selectedCharacterId: '',
  authToken: '',
  showDemo: false,
  showMotd: false,
  showCharacterSelection: false,
  error: null,
  isSubmitting: false,
  isRegistering: false,
  isLoggingOut: false,
};

const INITIAL_CREATION_SLICE: CreationSlice = {
  playerName: '',
  password: '',
  inviteCode: '',
  creationStep: null,
  pendingStats: null,
  selectedProfession: undefined,
  pendingSkillsPayload: null,
};

function authSliceReducer(state: AuthSlice, patch: Partial<AuthSlice>): AuthSlice {
  return { ...state, ...patch };
}

function creationSliceReducer(state: CreationSlice, patch: Partial<CreationSlice>): CreationSlice {
  return { ...state, ...patch };
}

function resolveNextState<T>(current: T, next: SetStateAction<T>): T {
  return typeof next === 'function' ? (next as (prev: T) => T)(current) : next;
}

function makeAuthSetter<K extends keyof AuthSlice>(
  key: K,
  authSlice: AuthSlice,
  patchAuthSlice: (patch: Partial<AuthSlice>) => void
) {
  return (value: SetStateAction<AuthSlice[K]>) => {
    patchAuthSlice({ [key]: resolveNextState(authSlice[key], value) } as Partial<AuthSlice>);
  };
}

function makeCreationSetter<K extends keyof CreationSlice>(
  key: K,
  creationSlice: CreationSlice,
  patchCreationSlice: (patch: Partial<CreationSlice>) => void
) {
  return (value: SetStateAction<CreationSlice[K]>) => {
    patchCreationSlice({ [key]: resolveNextState(creationSlice[key], value) } as Partial<CreationSlice>);
  };
}

function useAuthSliceSetters(authSlice: AuthSlice, patchAuthSlice: (patch: Partial<AuthSlice>) => void) {
  return {
    setIsAuthenticated: useCallback(
      (value: SetStateAction<AuthSlice['isAuthenticated']>) => {
        makeAuthSetter('isAuthenticated', authSlice, patchAuthSlice)(value);
      },
      [authSlice, patchAuthSlice]
    ),
    setCharacters: useCallback(
      (value: SetStateAction<AuthSlice['characters']>) => {
        makeAuthSetter('characters', authSlice, patchAuthSlice)(value);
      },
      [authSlice, patchAuthSlice]
    ),
    setSelectedCharacterName: useCallback(
      (value: SetStateAction<AuthSlice['selectedCharacterName']>) => {
        makeAuthSetter('selectedCharacterName', authSlice, patchAuthSlice)(value);
      },
      [authSlice, patchAuthSlice]
    ),
    setSelectedCharacterId: useCallback(
      (value: SetStateAction<AuthSlice['selectedCharacterId']>) => {
        makeAuthSetter('selectedCharacterId', authSlice, patchAuthSlice)(value);
      },
      [authSlice, patchAuthSlice]
    ),
    setAuthToken: useCallback(
      (value: SetStateAction<AuthSlice['authToken']>) => {
        makeAuthSetter('authToken', authSlice, patchAuthSlice)(value);
      },
      [authSlice, patchAuthSlice]
    ),
    setShowDemo: useCallback(
      (value: SetStateAction<AuthSlice['showDemo']>) => {
        makeAuthSetter('showDemo', authSlice, patchAuthSlice)(value);
      },
      [authSlice, patchAuthSlice]
    ),
    setShowMotd: useCallback(
      (value: SetStateAction<AuthSlice['showMotd']>) => {
        makeAuthSetter('showMotd', authSlice, patchAuthSlice)(value);
      },
      [authSlice, patchAuthSlice]
    ),
    setShowCharacterSelection: useCallback(
      (value: SetStateAction<AuthSlice['showCharacterSelection']>) => {
        makeAuthSetter('showCharacterSelection', authSlice, patchAuthSlice)(value);
      },
      [authSlice, patchAuthSlice]
    ),
    setError: useCallback(
      (value: SetStateAction<AuthSlice['error']>) => {
        makeAuthSetter('error', authSlice, patchAuthSlice)(value);
      },
      [authSlice, patchAuthSlice]
    ),
    setIsSubmitting: useCallback(
      (value: SetStateAction<AuthSlice['isSubmitting']>) => {
        makeAuthSetter('isSubmitting', authSlice, patchAuthSlice)(value);
      },
      [authSlice, patchAuthSlice]
    ),
    setIsRegistering: useCallback(
      (value: SetStateAction<AuthSlice['isRegistering']>) => {
        makeAuthSetter('isRegistering', authSlice, patchAuthSlice)(value);
      },
      [authSlice, patchAuthSlice]
    ),
    setIsLoggingOut: useCallback(
      (value: SetStateAction<AuthSlice['isLoggingOut']>) => {
        makeAuthSetter('isLoggingOut', authSlice, patchAuthSlice)(value);
      },
      [authSlice, patchAuthSlice]
    ),
  };
}

function useCreationSliceSetters(
  creationSlice: CreationSlice,
  patchCreationSlice: (patch: Partial<CreationSlice>) => void
) {
  return {
    setPlayerName: useCallback(
      (value: SetStateAction<CreationSlice['playerName']>) => {
        makeCreationSetter('playerName', creationSlice, patchCreationSlice)(value);
      },
      [creationSlice, patchCreationSlice]
    ),
    setPassword: useCallback(
      (value: SetStateAction<CreationSlice['password']>) => {
        makeCreationSetter('password', creationSlice, patchCreationSlice)(value);
      },
      [creationSlice, patchCreationSlice]
    ),
    setInviteCode: useCallback(
      (value: SetStateAction<CreationSlice['inviteCode']>) => {
        makeCreationSetter('inviteCode', creationSlice, patchCreationSlice)(value);
      },
      [creationSlice, patchCreationSlice]
    ),
    setCreationStep: useCallback(
      (value: SetStateAction<CreationSlice['creationStep']>) => {
        makeCreationSetter('creationStep', creationSlice, patchCreationSlice)(value);
      },
      [creationSlice, patchCreationSlice]
    ),
    setPendingStats: useCallback(
      (value: SetStateAction<CreationSlice['pendingStats']>) => {
        makeCreationSetter('pendingStats', creationSlice, patchCreationSlice)(value);
      },
      [creationSlice, patchCreationSlice]
    ),
    setSelectedProfession: useCallback(
      (value: SetStateAction<CreationSlice['selectedProfession']>) => {
        makeCreationSetter('selectedProfession', creationSlice, patchCreationSlice)(value);
      },
      [creationSlice, patchCreationSlice]
    ),
    setPendingSkillsPayload: useCallback(
      (value: SetStateAction<CreationSlice['pendingSkillsPayload']>) => {
        makeCreationSetter('pendingSkillsPayload', creationSlice, patchCreationSlice)(value);
      },
      [creationSlice, patchCreationSlice]
    ),
  };
}

function useReducerStateSlices() {
  const [authSlice, patchAuthSlice] = useReducer(authSliceReducer, INITIAL_AUTH_SLICE);
  const [creationSlice, patchCreationSlice] = useReducer(creationSliceReducer, INITIAL_CREATION_SLICE);
  const disconnectCallbackRef = useRef<(() => void) | null>(null);
  const usernameInputRef = useRef<HTMLInputElement | null>(null);
  const authSetters = useAuthSliceSetters(authSlice, patchAuthSlice);
  const creationSetters = useCreationSliceSetters(creationSlice, patchCreationSlice);

  return {
    ...authSlice,
    ...creationSlice,
    ...authSetters,
    ...creationSetters,
    disconnectCallbackRef,
    usernameInputRef,
  };
}

export function useMythosAppState() {
  const state = useReducerStateSlices();

  useEffect(() => {
    memoryMonitor.start();
    return () => {
      memoryMonitor.stop();
    };
  }, []);

  useAuthSessionRestore(
    state.setAuthToken,
    state.setIsAuthenticated,
    state.setCharacters,
    state.setSelectedCharacterName,
    state.setSelectedCharacterId,
    state.setShowMotd,
    state.setShowCharacterSelection,
    state.setCreationStep
  );

  const authSessionSetters = useMemo(
    () => ({
      setAuthToken: state.setAuthToken,
      setIsAuthenticated: state.setIsAuthenticated,
      setCharacters: state.setCharacters,
      setCreationStep: state.setCreationStep,
      setShowCharacterSelection: state.setShowCharacterSelection,
    }),
    [state]
  );

  const { handleLoginClick, handleRegisterClick } = useMythosAuthForm(
    state.playerName,
    state.password,
    state.inviteCode,
    state.setError,
    state.setIsSubmitting,
    authSessionSetters
  );

  return {
    ...state,
    handleLoginClick,
    handleRegisterClick,
  };
}
