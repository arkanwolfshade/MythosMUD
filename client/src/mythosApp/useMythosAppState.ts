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

function useReducerStateSlices() {
  const [authSlice, patchAuthSlice] = useReducer(authSliceReducer, INITIAL_AUTH_SLICE);
  const [creationSlice, patchCreationSlice] = useReducer(creationSliceReducer, INITIAL_CREATION_SLICE);
  const disconnectCallbackRef = useRef<(() => void) | null>(null);
  const usernameInputRef = useRef<HTMLInputElement | null>(null);

  const setIsAuthenticated = useCallback(
    (value: SetStateAction<boolean>) => {
      patchAuthSlice({ isAuthenticated: resolveNextState(authSlice.isAuthenticated, value) });
    },
    [authSlice.isAuthenticated]
  );
  const setCharacters = useCallback(
    (value: SetStateAction<CharacterInfo[]>) => {
      patchAuthSlice({ characters: resolveNextState(authSlice.characters, value) });
    },
    [authSlice.characters]
  );
  const setSelectedCharacterName = useCallback(
    (value: SetStateAction<string>) => {
      patchAuthSlice({ selectedCharacterName: resolveNextState(authSlice.selectedCharacterName, value) });
    },
    [authSlice.selectedCharacterName]
  );
  const setSelectedCharacterId = useCallback(
    (value: SetStateAction<string>) => {
      patchAuthSlice({ selectedCharacterId: resolveNextState(authSlice.selectedCharacterId, value) });
    },
    [authSlice.selectedCharacterId]
  );
  const setAuthToken = useCallback(
    (value: SetStateAction<string>) => {
      patchAuthSlice({ authToken: resolveNextState(authSlice.authToken, value) });
    },
    [authSlice.authToken]
  );
  const setShowDemo = useCallback(
    (value: SetStateAction<boolean>) => {
      patchAuthSlice({ showDemo: resolveNextState(authSlice.showDemo, value) });
    },
    [authSlice.showDemo]
  );
  const setShowMotd = useCallback(
    (value: SetStateAction<boolean>) => {
      patchAuthSlice({ showMotd: resolveNextState(authSlice.showMotd, value) });
    },
    [authSlice.showMotd]
  );
  const setShowCharacterSelection = useCallback(
    (value: SetStateAction<boolean>) => {
      patchAuthSlice({ showCharacterSelection: resolveNextState(authSlice.showCharacterSelection, value) });
    },
    [authSlice.showCharacterSelection]
  );
  const setError = useCallback(
    (value: SetStateAction<string | null>) => {
      patchAuthSlice({ error: resolveNextState(authSlice.error, value) });
    },
    [authSlice.error]
  );
  const setIsSubmitting = useCallback(
    (value: SetStateAction<boolean>) => {
      patchAuthSlice({ isSubmitting: resolveNextState(authSlice.isSubmitting, value) });
    },
    [authSlice.isSubmitting]
  );
  const setIsRegistering = useCallback(
    (value: SetStateAction<boolean>) => {
      patchAuthSlice({ isRegistering: resolveNextState(authSlice.isRegistering, value) });
    },
    [authSlice.isRegistering]
  );
  const setIsLoggingOut = useCallback(
    (value: SetStateAction<boolean>) => {
      patchAuthSlice({ isLoggingOut: resolveNextState(authSlice.isLoggingOut, value) });
    },
    [authSlice.isLoggingOut]
  );

  const setPlayerName = useCallback(
    (value: SetStateAction<string>) => {
      patchCreationSlice({ playerName: resolveNextState(creationSlice.playerName, value) });
    },
    [creationSlice.playerName]
  );
  const setPassword = useCallback(
    (value: SetStateAction<string>) => {
      patchCreationSlice({ password: resolveNextState(creationSlice.password, value) });
    },
    [creationSlice.password]
  );
  const setInviteCode = useCallback(
    (value: SetStateAction<string>) => {
      patchCreationSlice({ inviteCode: resolveNextState(creationSlice.inviteCode, value) });
    },
    [creationSlice.inviteCode]
  );
  const setCreationStep = useCallback(
    (value: SetStateAction<CreationStep | null>) => {
      patchCreationSlice({ creationStep: resolveNextState(creationSlice.creationStep, value) });
    },
    [creationSlice.creationStep]
  );
  const setPendingStats = useCallback(
    (value: SetStateAction<Stats | null>) => {
      patchCreationSlice({ pendingStats: resolveNextState(creationSlice.pendingStats, value) });
    },
    [creationSlice.pendingStats]
  );
  const setSelectedProfession = useCallback(
    (value: SetStateAction<Profession | undefined>) => {
      patchCreationSlice({ selectedProfession: resolveNextState(creationSlice.selectedProfession, value) });
    },
    [creationSlice.selectedProfession]
  );
  const setPendingSkillsPayload = useCallback(
    (value: SetStateAction<PendingSkillsPayload | null>) => {
      patchCreationSlice({ pendingSkillsPayload: resolveNextState(creationSlice.pendingSkillsPayload, value) });
    },
    [creationSlice.pendingSkillsPayload]
  );

  return {
    ...authSlice,
    ...creationSlice,
    setIsAuthenticated,
    setCharacters,
    setSelectedCharacterName,
    setSelectedCharacterId,
    setAuthToken,
    setShowDemo,
    setShowMotd,
    setShowCharacterSelection,
    setError,
    setIsSubmitting,
    setIsRegistering,
    setIsLoggingOut,
    setPlayerName,
    setPassword,
    setInviteCode,
    setCreationStep,
    setPendingStats,
    setSelectedProfession,
    setPendingSkillsPayload,
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
