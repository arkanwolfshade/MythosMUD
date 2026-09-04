import { act, renderHook } from '@testing-library/react';
import { beforeEach, describe, expect, it, vi } from 'vitest';

import { useMythosSessionChrome } from '../useMythosSessionChrome';

const hoisted = vi.hoisted(() => ({
  clearAllTokens: vi.fn(),
  logoutHandlerMock: vi.fn(),
  tryStartLoginGracePeriodMock: vi.fn(),
  isGracePeriodServerUnavailableErrorMock: vi.fn(),
  isServerUnavailableMock: vi.fn(),
}));

vi.mock('../../utils/security.js', () => ({
  secureTokenStorage: {
    clearAllTokens: hoisted.clearAllTokens,
  },
}));

vi.mock('../../utils/logoutHandler.js', () => ({
  logoutHandler: (...args: unknown[]) => hoisted.logoutHandlerMock(...args),
}));

vi.mock('../motdContinueFlow.js', () => ({
  tryStartLoginGracePeriod: (...args: unknown[]) => hoisted.tryStartLoginGracePeriodMock(...args),
  isGracePeriodServerUnavailableError: (...args: unknown[]) => hoisted.isGracePeriodServerUnavailableErrorMock(...args),
}));

vi.mock('../serverAvailability.js', () => ({
  isServerUnavailable: (...args: unknown[]) => hoisted.isServerUnavailableMock(...args),
}));

describe('useMythosSessionChrome', () => {
  const setters = {
    setIsLoggingOut: vi.fn(),
    setError: vi.fn(),
    setIsAuthenticated: vi.fn(),
    setCharacters: vi.fn(),
    setSelectedCharacterName: vi.fn(),
    setSelectedCharacterId: vi.fn(),
    setPlayerName: vi.fn(),
    setPassword: vi.fn(),
    setInviteCode: vi.fn(),
    setAuthToken: vi.fn(),
    setShowMotd: vi.fn(),
    setShowCharacterSelection: vi.fn(),
    setIsRegistering: vi.fn(),
    returnToLogin: vi.fn(),
    focusUsernameInput: vi.fn(),
    handleLoginClick: vi.fn(async () => undefined),
    handleRegisterClick: vi.fn(async () => undefined),
  };

  beforeEach(() => {
    vi.clearAllMocks();
    hoisted.isGracePeriodServerUnavailableErrorMock.mockReturnValue(false);
    hoisted.isServerUnavailableMock.mockReturnValue(false);
  });

  it('handles missing auth token when continuing from MOTD', async () => {
    const { result } = renderHook(() =>
      useMythosSessionChrome(
        '',
        'char-1',
        false,
        setters.setIsLoggingOut,
        setters.setError,
        setters.setIsAuthenticated,
        setters.setCharacters,
        setters.setSelectedCharacterName,
        setters.setSelectedCharacterId,
        setters.setPlayerName,
        setters.setPassword,
        setters.setInviteCode,
        setters.setAuthToken,
        setters.setShowMotd,
        setters.setShowCharacterSelection,
        setters.setIsRegistering,
        setters.returnToLogin,
        setters.focusUsernameInput,
        false,
        'player',
        'pw',
        'invite',
        setters.handleLoginClick,
        setters.handleRegisterClick
      )
    );

    await act(async () => {
      await result.current.handleMotdContinue();
    });

    expect(setters.setError).toHaveBeenCalledWith('Authentication token is missing. Please log in again.');
    expect(setters.setShowMotd).toHaveBeenCalledWith(false);
  });

  it('calls logout handler and clears state on logout', async () => {
    hoisted.logoutHandlerMock.mockResolvedValueOnce(undefined);
    const { result } = renderHook(() =>
      useMythosSessionChrome(
        'token',
        'char-1',
        false,
        setters.setIsLoggingOut,
        setters.setError,
        setters.setIsAuthenticated,
        setters.setCharacters,
        setters.setSelectedCharacterName,
        setters.setSelectedCharacterId,
        setters.setPlayerName,
        setters.setPassword,
        setters.setInviteCode,
        setters.setAuthToken,
        setters.setShowMotd,
        setters.setShowCharacterSelection,
        setters.setIsRegistering,
        setters.returnToLogin,
        setters.focusUsernameInput,
        false,
        'player',
        'pw',
        'invite',
        setters.handleLoginClick,
        setters.handleRegisterClick
      )
    );

    await act(async () => {
      await result.current.handleLogout();
    });

    expect(hoisted.logoutHandlerMock).toHaveBeenCalled();
    expect(setters.setIsLoggingOut).toHaveBeenCalledWith(true);
    expect(setters.setIsLoggingOut).toHaveBeenLastCalledWith(false);
  });
});
