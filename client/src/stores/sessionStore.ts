import { create } from 'zustand';
import { devtools } from 'zustand/middleware';

export interface SessionState {
  // Authentication state
  isAuthenticated: boolean;
  hasCharacter: boolean;
  characterName: string;
  playerName: string;
  authToken: string;
  inviteCode: string;

  // Form state
  isSubmitting: boolean;
  error: string | null;

  // Session management
  lastActivity: number | null;
  sessionTimeout: number; // in milliseconds
}

export interface SessionActions {
  // Authentication actions
  setAuthenticated: (authenticated: boolean) => void;
  setHasCharacter: (hasCharacter: boolean) => void;
  setCharacterName: (name: string) => void;
  setPlayerName: (name: string) => void;

  // Token management
  setAuthToken: (token: string) => void;
  clearAuthToken: () => void;

  // Invite code management
  setInviteCode: (code: string) => void;
  clearInviteCode: () => void;

  // Form state actions
  setSubmitting: (submitting: boolean) => void;
  setError: (error: string | null) => void;
  clearError: () => void;

  // Session management
  updateLastActivity: (timestamp: number) => void;
  setSessionTimeout: (timeout: number) => void;

  // High-level actions
  logout: () => void;

  // State management
  reset: () => void;
}

export interface SessionSelectors {
  // Computed properties
  isValidToken: () => boolean;
  isValidInviteCode: () => boolean;
  isSessionExpired: () => boolean;
  getLoginFormData: () => { playerName: string; inviteCode: string };
  getSessionStatus: () => {
    isAuthenticated: boolean;
    hasCharacter: boolean;
    isSubmitting: boolean;
    hasError: boolean;
  };
  getUserInfo: () => {
    playerName: string;
    characterName: string;
    hasValidToken: boolean;
  };
  getSessionTimeoutInfo: () => {
    isExpired: boolean;
    timeRemaining: number;
    timeoutDuration: number;
  };
}

type SessionStore = SessionState & SessionActions & SessionSelectors;

const DEFAULT_SESSION_TIMEOUT = 30 * 60 * 1000; // 30 minutes

const createInitialState = (): SessionState => ({
  isAuthenticated: false,
  hasCharacter: false,
  characterName: '',
  playerName: '',
  authToken: '',
  inviteCode: '',
  isSubmitting: false,
  error: null,
  lastActivity: null,
  sessionTimeout: DEFAULT_SESSION_TIMEOUT,
});

export const useSessionStore = create<SessionStore>()(
  devtools(
    (set, get) => ({
      ...createInitialState(),

      // Authentication actions
      setAuthenticated: (authenticated: boolean) =>
        set(
          {
            isAuthenticated: authenticated,
            lastActivity: Date.now(),
          },
          false,
          'setAuthenticated'
        ),

      setHasCharacter: (hasCharacter: boolean) =>
        set(
          {
            hasCharacter,
            lastActivity: Date.now(),
          },
          false,
          'setHasCharacter'
        ),

      setCharacterName: (name: string) =>
        set(
          {
            characterName: name,
            lastActivity: Date.now(),
          },
          false,
          'setCharacterName'
        ),

      setPlayerName: (name: string) =>
        set(
          {
            playerName: name,
            lastActivity: Date.now(),
          },
          false,
          'setPlayerName'
        ),

      // Token management actions
      setAuthToken: (token: string) =>
        set(
          {
            authToken: token,
            lastActivity: Date.now(),
          },
          false,
          'setAuthToken'
        ),

      clearAuthToken: () => set({ authToken: '' }, false, 'clearAuthToken'),

      // Invite code management actions
      setInviteCode: (code: string) => set({ inviteCode: code }, false, 'setInviteCode'),

      clearInviteCode: () => set({ inviteCode: '' }, false, 'clearInviteCode'),

      // Form state actions
      setSubmitting: (submitting: boolean) => set({ isSubmitting: submitting }, false, 'setSubmitting'),

      setError: (error: string | null) => set({ error }, false, 'setError'),

      clearError: () => set({ error: null }, false, 'clearError'),

      // Session management actions
      updateLastActivity: (timestamp: number) => set({ lastActivity: timestamp }, false, 'updateLastActivity'),

      setSessionTimeout: (timeout: number) => set({ sessionTimeout: timeout }, false, 'setSessionTimeout'),

      // High-level actions
      logout: () =>
        set(
          {
            isAuthenticated: false,
            hasCharacter: false,
            characterName: '',
            playerName: '',
            authToken: '',
            inviteCode: '',
            error: null,
            lastActivity: null,
          },
          false,
          'logout'
        ),

      // State management actions
      reset: () => set(createInitialState(), false, 'reset'),

      // Selectors
      isValidToken: () => {
        const state = get();
        return state.authToken.length > 0;
      },

      isValidInviteCode: () => {
        const state = get();
        // Basic validation - invite codes should be alphanumeric and at least 6 characters
        return /^[A-Z0-9]{6,}$/.test(state.inviteCode);
      },

      isSessionExpired: () => {
        const state = get();
        if (!state.lastActivity) return false;
        return Date.now() - state.lastActivity > state.sessionTimeout;
      },

      getLoginFormData: () => {
        const state = get();
        return {
          playerName: state.playerName,
          inviteCode: state.inviteCode,
        };
      },

      getSessionStatus: () => {
        const state = get();
        return {
          isAuthenticated: state.isAuthenticated,
          hasCharacter: state.hasCharacter,
          isSubmitting: state.isSubmitting,
          hasError: state.error !== null,
        };
      },

      getUserInfo: () => {
        const state = get();
        return {
          playerName: state.playerName,
          characterName: state.characterName,
          hasValidToken: state.authToken.length > 0,
        };
      },

      getSessionTimeoutInfo: () => {
        const state = get();
        const now = Date.now();
        const timeRemaining = state.lastActivity
          ? Math.max(0, state.sessionTimeout - (now - state.lastActivity))
          : state.sessionTimeout;

        return {
          isExpired: state.isSessionExpired(),
          timeRemaining,
          timeoutDuration: state.sessionTimeout,
        };
      },
    }),
    {
      name: 'session-store',
      partialize: state => ({
        isAuthenticated: state.isAuthenticated,
        hasCharacter: state.hasCharacter,
        characterName: state.characterName,
        playerName: state.playerName,
        authToken: state.authToken,
        lastActivity: state.lastActivity,
        sessionTimeout: state.sessionTimeout,
      }),
    }
  )
);
