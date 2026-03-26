import type { KeyboardEvent } from 'react';
import { useCallback, useMemo } from 'react';
import type { Profession } from '../components/ProfessionCard.tsx';
import type { Stats } from '../hooks/useStatsRolling.js';
import { logoutHandler } from '../utils/logoutHandler.js';
import { secureTokenStorage } from '../utils/security.js';
import { runAfterCharacterCreatedFlow } from './creationCompleteActions.js';
import { executeDeleteCharacterUi } from './deleteCharacterActions.js';
import { isGracePeriodServerUnavailableError, tryStartLoginGracePeriod } from './motdContinueFlow.js';
import { runSelectCharacterFlow, selectCharacterNetworkErrorMessage } from './selectCharacterFlow.js';
import { isServerUnavailable, stringIndicatesServerUnavailable } from './serverAvailability.js';
import type { useMythosAppState } from './useMythosAppState.ts';

type AppState = ReturnType<typeof useMythosAppState>;

export function useMythosAppActions(state: AppState) {
  const returnToLogin = useCallback(() => {
    state.setIsAuthenticated(false);
    state.setCharacters([]);
    state.setSelectedCharacterName('');
    state.setSelectedCharacterId('');
    state.setShowCharacterSelection(false);
    state.setShowMotd(false);
    state.setCreationStep(null);
    state.setAuthToken('');
    secureTokenStorage.clearAllTokens();
    state.setError('Server is unavailable. Please try again later.');
  }, [state]);

  const focusUsernameInput = useCallback(() => {
    setTimeout(() => {
      if (state.usernameInputRef.current) {
        state.usernameInputRef.current.focus();
      }
    }, 0);
  }, [state.usernameInputRef]);

  const deleteCharacterDeps = useMemo(
    () => ({
      returnToLogin,
      setCharacters: state.setCharacters,
      setShowCharacterSelection: state.setShowCharacterSelection,
      setCreationStep: state.setCreationStep,
      setSelectedProfession: state.setSelectedProfession,
      setError: state.setError,
    }),
    [returnToLogin, state]
  );

  const creationCompleteActions = useMemo(
    () => ({
      returnToLogin,
      setCharacters: state.setCharacters,
      setPendingStats: state.setPendingStats,
      setSelectedProfession: state.setSelectedProfession,
      setPendingSkillsPayload: state.setPendingSkillsPayload,
      setCreationStep: state.setCreationStep,
      setShowCharacterSelection: state.setShowCharacterSelection,
      setError: state.setError,
    }),
    [returnToLogin, state]
  );

  const handleProfessionSelected = useCallback(
    (profession: Profession) => {
      state.setSelectedProfession(profession);
      state.setCreationStep('skills');
    },
    [state]
  );

  const handleProfessionSelectionBack = useCallback(() => {
    state.setCreationStep('stats');
  }, [state]);

  const handleProfessionSelectionError = useCallback(
    (err: string) => {
      if (stringIndicatesServerUnavailable(err)) {
        returnToLogin();
        return;
      }
      state.setError(err);
    },
    [returnToLogin, state]
  );

  const handleStatsAccepted = useCallback(
    (stats: Stats) => {
      state.setPendingStats(stats);
      state.setCreationStep('profession');
    },
    [state]
  );

  const handleCreationComplete = useCallback(async () => {
    await runAfterCharacterCreatedFlow(state.authToken, creationCompleteActions);
  }, [state.authToken, creationCompleteActions]);

  const handleStatsError = useCallback(
    (err: string) => {
      if (stringIndicatesServerUnavailable(err)) {
        returnToLogin();
        return;
      }
      state.setError(err);
      state.setSelectedProfession(undefined);
      state.setCreationStep(null);
    },
    [returnToLogin, state]
  );

  const handleStatsRollingBack = useCallback(() => {
    state.setCreationStep(null);
    if (state.characters.length > 0) {
      state.setShowCharacterSelection(true);
    } else {
      returnToLogin();
    }
  }, [returnToLogin, state]);

  const handleCharacterSelected = useCallback(
    async (characterId: string) => {
      const result = await runSelectCharacterFlow(state.authToken, characterId);
      if (result.outcome === 'server_unavailable') {
        returnToLogin();
        return;
      }
      if (result.outcome === 'error') {
        state.setError(result.message);
        return;
      }
      if (result.outcome === 'network_error') {
        if (isServerUnavailable(result.error, null)) {
          returnToLogin();
          return;
        }
        state.setError(selectCharacterNetworkErrorMessage(result.error));
        return;
      }
      state.setSelectedCharacterName(result.selectedName);
      state.setSelectedCharacterId(result.selectedId);
      state.setShowCharacterSelection(false);
      state.setShowMotd(true);
    },
    [returnToLogin, state]
  );

  const handleDeleteCharacter = useCallback(
    async (characterId: string) => {
      await executeDeleteCharacterUi(state.authToken, characterId, deleteCharacterDeps);
    },
    [deleteCharacterDeps, state.authToken]
  );

  const handleCreateCharacter = useCallback(() => {
    state.setPendingStats(null);
    state.setSelectedProfession(undefined);
    state.setPendingSkillsPayload(null);
    state.setCreationStep('stats');
    state.setShowCharacterSelection(false);
    state.setSelectedCharacterName('');
    state.setSelectedCharacterId('');
  }, [state]);

  const handleMotdContinue = useCallback(async () => {
    if (!state.authToken) {
      state.setError('Authentication token is missing. Please log in again.');
      state.setIsAuthenticated(false);
      state.setCharacters([]);
      state.setSelectedCharacterName('');
      state.setSelectedCharacterId('');
      state.setShowMotd(false);
      state.setShowCharacterSelection(false);
      return;
    }

    if (state.selectedCharacterId) {
      try {
        await tryStartLoginGracePeriod(state.authToken, state.selectedCharacterId);
      } catch (error) {
        if (isGracePeriodServerUnavailableError(error) || isServerUnavailable(error, null)) {
          returnToLogin();
          return;
        }
        console.warn('Error starting login grace period:', error);
      }
    }

    state.setShowMotd(false);
  }, [returnToLogin, state]);

  const handleMotdReturnToLogin = useCallback(() => {
    state.setIsAuthenticated(false);
    state.setCharacters([]);
    state.setSelectedCharacterName('');
    state.setSelectedCharacterId('');
    state.setPlayerName('');
    state.setPassword('');
    state.setInviteCode('');
    state.setAuthToken('');
    state.setShowMotd(false);
    state.setShowCharacterSelection(false);
    secureTokenStorage.clearAllTokens();
    focusUsernameInput();
  }, [focusUsernameInput, state]);

  const handleDisconnectCallback = useCallback(
    (disconnectFn: () => void) => {
      state.disconnectCallbackRef.current = disconnectFn;
    },
    [state.disconnectCallbackRef]
  );

  const handleLogout = useCallback(async () => {
    if (state.isLoggingOut) {
      return;
    }
    state.setIsLoggingOut(true);
    state.setError(null);

    const clearAllState = () => {
      state.setIsAuthenticated(false);
      state.setCharacters([]);
      state.setSelectedCharacterName('');
      state.setSelectedCharacterId('');
      state.setPlayerName('');
      state.setPassword('');
      state.setInviteCode('');
      state.setAuthToken('');
      state.setError(null);
      state.setShowCharacterSelection(false);
      secureTokenStorage.clearAllTokens();
      focusUsernameInput();
    };

    try {
      await logoutHandler({
        authToken: state.authToken,
        disconnect: () => state.disconnectCallbackRef.current?.(),
        clearState: clearAllState,
        navigateToLogin: clearAllState,
        timeout: 5000,
      });
    } catch (logoutErr) {
      console.error('Logout failed:', logoutErr);
      state.setError(logoutErr instanceof Error ? logoutErr.message : 'Logout failed');
      clearAllState();
    } finally {
      state.setIsLoggingOut(false);
    }
  }, [focusUsernameInput, state]);

  const toggleMode = useCallback(() => {
    state.setIsRegistering(v => !v);
    state.setError(null);
    state.setPlayerName('');
    state.setPassword('');
    state.setInviteCode('');
  }, [state]);

  const handleKeyDown = useCallback(
    (event: KeyboardEvent) => {
      if (event.key !== 'Enter' || !state.playerName.trim() || !state.password.trim()) {
        return;
      }
      if (state.isRegistering && !state.inviteCode.trim()) {
        return;
      }
      if (state.isRegistering) {
        void state.handleRegisterClick();
      } else {
        void state.handleLoginClick();
      }
    },
    [state]
  );

  return {
    handleProfessionSelected,
    handleProfessionSelectionBack,
    handleProfessionSelectionError,
    handleStatsAccepted,
    handleCreationComplete,
    handleStatsError,
    handleStatsRollingBack,
    handleCharacterSelected,
    handleDeleteCharacter,
    handleCreateCharacter,
    handleMotdContinue,
    handleMotdReturnToLogin,
    handleDisconnectCallback,
    handleLogout,
    toggleMode,
    handleKeyDown,
  };
}
