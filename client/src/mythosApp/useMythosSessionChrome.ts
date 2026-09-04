import { useCallback, useRef, type KeyboardEvent } from 'react';
import { logoutHandler } from '../utils/logoutHandler.js';
import { secureTokenStorage } from '../utils/security.js';
import { isGracePeriodServerUnavailableError, tryStartLoginGracePeriod } from './motdContinueFlow.js';
import { isServerUnavailable } from './serverAvailability.js';

export function useMythosSessionChrome(
  authToken: string,
  selectedCharacterId: string,
  isLoggingOut: boolean,
  setIsLoggingOut: (v: boolean) => void,
  setError: (v: string | null) => void,
  setIsAuthenticated: (v: boolean) => void,
  setCharacters: (v: []) => void,
  setSelectedCharacterName: (v: string) => void,
  setSelectedCharacterId: (v: string) => void,
  setPlayerName: (v: string) => void,
  setPassword: (v: string) => void,
  setInviteCode: (v: string) => void,
  setAuthToken: (v: string) => void,
  setShowMotd: (v: boolean) => void,
  setShowCharacterSelection: (v: boolean) => void,
  setIsRegistering: (v: boolean | ((p: boolean) => boolean)) => void,
  returnToLogin: () => void,
  focusUsernameInput: () => void,
  isRegistering: boolean,
  playerName: string,
  password: string,
  inviteCode: string,
  handleLoginClick: () => Promise<void>,
  handleRegisterClick: () => Promise<void>
) {
  const disconnectCallbackRef = useRef<(() => void) | null>(null);

  const handleDisconnectCallback = useCallback((disconnectFn: () => void) => {
    disconnectCallbackRef.current = disconnectFn;
  }, []);

  const handleMotdContinue = useCallback(async () => {
    if (!authToken) {
      setError('Authentication token is missing. Please log in again.');
      setIsAuthenticated(false);
      setCharacters([]);
      setSelectedCharacterName('');
      setSelectedCharacterId('');
      setShowMotd(false);
      setShowCharacterSelection(false);
      return;
    }

    if (selectedCharacterId) {
      try {
        await tryStartLoginGracePeriod(authToken, selectedCharacterId);
      } catch (error) {
        if (isGracePeriodServerUnavailableError(error)) {
          returnToLogin();
          return;
        }
        if (isServerUnavailable(error, null)) {
          returnToLogin();
          return;
        }
        console.warn('Error starting login grace period:', error);
      }
    }

    setShowMotd(false);
  }, [
    authToken,
    selectedCharacterId,
    returnToLogin,
    setCharacters,
    setError,
    setIsAuthenticated,
    setSelectedCharacterId,
    setSelectedCharacterName,
    setShowCharacterSelection,
    setShowMotd,
  ]);

  const handleMotdReturnToLogin = useCallback(() => {
    setIsAuthenticated(false);
    setCharacters([]);
    setSelectedCharacterName('');
    setSelectedCharacterId('');
    setPlayerName('');
    setPassword('');
    setInviteCode('');
    setAuthToken('');
    setShowMotd(false);
    setShowCharacterSelection(false);
    secureTokenStorage.clearAllTokens();
    focusUsernameInput();
  }, [
    focusUsernameInput,
    setAuthToken,
    setCharacters,
    setInviteCode,
    setIsAuthenticated,
    setPassword,
    setPlayerName,
    setSelectedCharacterId,
    setSelectedCharacterName,
    setShowCharacterSelection,
    setShowMotd,
  ]);

  const handleLogout = useCallback(async () => {
    if (isLoggingOut) {
      return;
    }

    setIsLoggingOut(true);
    setError(null);

    const clearAllState = () => {
      setIsAuthenticated(false);
      setCharacters([]);
      setSelectedCharacterName('');
      setSelectedCharacterId('');
      setPlayerName('');
      setPassword('');
      setInviteCode('');
      setAuthToken('');
      setError(null);
      setShowCharacterSelection(false);
      secureTokenStorage.clearAllTokens();
      focusUsernameInput();
    };

    try {
      await logoutHandler({
        authToken,
        disconnect: () => {
          if (disconnectCallbackRef.current) {
            disconnectCallbackRef.current();
          }
        },
        clearState: clearAllState,
        navigateToLogin: clearAllState,
        timeout: 5000,
      });
    } catch (logoutErr) {
      console.error('Logout failed:', logoutErr);
      setError(logoutErr instanceof Error ? logoutErr.message : 'Logout failed');
      setIsAuthenticated(false);
      setCharacters([]);
      setSelectedCharacterName('');
      setSelectedCharacterId('');
      setPlayerName('');
      setPassword('');
      setInviteCode('');
      setAuthToken('');
      setShowCharacterSelection(false);
      secureTokenStorage.clearAllTokens();
      focusUsernameInput();
    } finally {
      setIsLoggingOut(false);
    }
  }, [
    authToken,
    focusUsernameInput,
    isLoggingOut,
    setAuthToken,
    setCharacters,
    setError,
    setInviteCode,
    setIsAuthenticated,
    setIsLoggingOut,
    setPassword,
    setPlayerName,
    setSelectedCharacterId,
    setSelectedCharacterName,
    setShowCharacterSelection,
  ]);

  const toggleMode = useCallback(() => {
    setIsRegistering(v => !v);
    setError(null);
    setPlayerName('');
    setPassword('');
    setInviteCode('');
  }, [setError, setInviteCode, setIsRegistering, setPassword, setPlayerName]);

  const handleKeyDown = useCallback(
    (event: KeyboardEvent) => {
      if (event.key !== 'Enter') {
        return;
      }
      if (!playerName.trim() || !password.trim()) {
        return;
      }
      if (isRegistering && !inviteCode.trim()) {
        return;
      }
      if (isRegistering) {
        void handleRegisterClick();
      } else {
        void handleLoginClick();
      }
    },
    [playerName, password, inviteCode, isRegistering, handleRegisterClick, handleLoginClick]
  );

  return {
    disconnectCallbackRef,
    handleDisconnectCallback,
    handleMotdContinue,
    handleMotdReturnToLogin,
    handleLogout,
    toggleMode,
    handleKeyDown,
  };
}
