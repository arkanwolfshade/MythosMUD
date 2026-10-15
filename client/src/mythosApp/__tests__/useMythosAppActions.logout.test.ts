/// <reference lib="es2015" />

import { act, renderHook } from '@testing-library/react';
import { beforeEach, describe, expect, it, vi } from 'vitest';

import { useMythosAppActions } from '../useMythosAppActions.js';
import type { useMythosAppState } from '../useMythosAppState.ts';

const hoisted = vi.hoisted(() => ({ logoutHandlerMock: vi.fn() }));

vi.mock('../../utils/logoutHandler.js', () => ({ logoutHandler: hoisted.logoutHandlerMock }));

type AppState = ReturnType<typeof useMythosAppState>;

function makeState(overrides: Partial<Record<string, unknown>> = {}): AppState {
  return {
    authToken: 'token-abc',
    selectedCharacterId: 'char-123',
    isLoggingOut: false,
    disconnectCallbackRef: { current: null },
    usernameInputRef: { current: null },
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
    setShowCharacterSelection: vi.fn(),
    ...overrides,
  } as unknown as AppState;
}

describe('useMythosAppActions handleLogout', () => {
  beforeEach(() => {
    hoisted.logoutHandlerMock.mockReset();
    hoisted.logoutHandlerMock.mockResolvedValue(undefined);
  });

  it('logs out as the selected character, not the account username', async () => {
    const { result } = renderHook(() => useMythosAppActions(makeState()));

    await act(async () => {
      await result.current.handleLogout();
    });

    expect(hoisted.logoutHandlerMock).toHaveBeenCalledWith(
      expect.objectContaining({ authToken: 'token-abc', characterId: 'char-123' })
    );
  });

  it('ignores a second logout while one is already in progress', async () => {
    const { result } = renderHook(() => useMythosAppActions(makeState({ isLoggingOut: true })));

    await act(async () => {
      await result.current.handleLogout();
    });

    expect(hoisted.logoutHandlerMock).not.toHaveBeenCalled();
  });
});
