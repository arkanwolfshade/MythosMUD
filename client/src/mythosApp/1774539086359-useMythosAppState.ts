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

function usePatchedSetter<T, K extends keyof T>(
  patch: (partial: Partial<T>) => void,
  key: K,
  current: T[K]
): (value: SetStateAction<T[K]>) => void {
  return useCallback(
    (value: SetStateAction<T[K]>) => {
      patch({ [key]: resolveNextState(current, value) } as unknown as Partial<T>);
    },
    [patch, key, current]
  );
}

function useAuthSliceSetters(authSlice: AuthSlice, patchAuthSlice: (partial: Partial<AuthSlice>) => void) {
  return {
    setIsAuthenticated: usePatchedSetter(patchAuthSlice, 'isAuthenticated', authSlice.isAuthenticated),
    setCharacters: usePatchedSetter(patchAuthSlice, 'characters', authSlice.characters),
    setSelectedCharacterName: usePatchedSetter(
      patchAuthSlice,
      'selectedCharacterName',
      authSlice.selectedCharacterName
    ),
    setSelectedCharacterId: usePatchedSetter(patchAuthSlice, 'selectedCharacterId', authSlice.selectedCharacterId),
    setAuthToken: usePatchedSetter(patchAuthSlice, 'authToken', authSlice.authToken),
    setShowDemo: usePatchedSetter(patchAuthSlice, 'showDemo', authSlice.showDemo),
    setShowMotd: usePatchedSetter(patchAuthSlice, 'showMotd', authSlice.showMotd),
    setShowCharacterSelection: usePatchedSetter(
      patchAuthSlice,
      'showCharacterSelection',
      authSlice.showCharacterSelection
    ),
    setError: usePatchedSetter(patchAuthSlice, 'error', authSlice.error),
    setIsSubmitting: usePatchedSetter(patchAuthSlice, 'isSubmitting', authSlice.isSubmitting),
    setIsRegistering: usePatchedSetter(patchAuthSlice, 'isRegistering', authSlice.isRegistering),
    setIsLoggingOut: usePatchedSetter(patchAuthSlice, 'isLoggingOut', authSlice.isLoggingOut),
  };
}

function useCreationSliceSetters(
  creationSlice: CreationSlice,
  patchCreationSlice: (partial: Partial<CreationSlice>) => void
) {
  return {
    setPlayerName: usePatchedSetter(patchCreationSlice, 'playerName', creationSlice.playerName),
    setPassword: usePatchedSetter(patchCreationSlice, 'password', creationSlice.password),
    setInviteCode: usePatchedSetter(patchCreationSlice, 'inviteCode', creationSlice.inviteCode),
    setCreationStep: usePatchedSetter(patchCreationSlice, 'creationStep', creationSlice.creationStep),
    setPendingStats: usePatchedSetter(patchCreationSlice, 'pendingStats', creationSlice.pendingStats),
    setSelectedProfession: usePatchedSetter(patchCreationSlice, 'selectedProfession', creationSlice.selectedProfession),
    setPendingSkillsPayload: usePatchedSetter(
      patchCreationSlice,
      'pendingSkillsPayload',
      creationSlice.pendingSkillsPayload
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
