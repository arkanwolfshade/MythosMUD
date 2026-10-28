/// <reference lib="es2015" />

import { renderHook, waitFor } from '@testing-library/react';
import { beforeEach, describe, expect, it, vi } from 'vitest';

import { useAuthSessionRestore } from '../useAuthSessionRestore.js';
import type { CharacterInfo } from '../../types/auth.js';

const hoisted = vi.hoisted(() => ({
  restoreCharactersOnMountMock: vi.fn(),
  tokenStorage: {
    getToken: vi.fn(),
    isValidToken: vi.fn(),
    isTokenExpired: vi.fn(),
    clearAllTokens: vi.fn(),
  },
}));

vi.mock('../characterSessionApi.js', () => ({
  restoreCharactersOnMount: hoisted.restoreCharactersOnMountMock,
}));

vi.mock('../../utils/security.js', () => ({
  secureTokenStorage: hoisted.tokenStorage,
}));

function character(id: string, name: string): CharacterInfo {
  return { player_id: id, name, profession_id: 1, level: 1, created_at: '', last_active: '' };
}

function renderRestore() {
  const setters = {
    setAuthToken: vi.fn(),
    setIsAuthenticated: vi.fn(),
    setCharacters: vi.fn(),
    setSelectedCharacterName: vi.fn(),
    setSelectedCharacterId: vi.fn(),
    setShowMotd: vi.fn(),
    setShowCharacterSelection: vi.fn(),
    setCreationStep: vi.fn(),
  };
  renderHook(() =>
    useAuthSessionRestore(
      setters.setAuthToken,
      setters.setIsAuthenticated,
      setters.setCharacters,
      setters.setSelectedCharacterName,
      setters.setSelectedCharacterId,
      setters.setShowMotd,
      setters.setShowCharacterSelection,
      setters.setCreationStep
    )
  );
  return setters;
}

describe('useAuthSessionRestore', () => {
  beforeEach(() => {
    hoisted.restoreCharactersOnMountMock.mockReset();
    hoisted.tokenStorage.getToken.mockReturnValue('valid-token');
    hoisted.tokenStorage.isValidToken.mockReturnValue(true);
    hoisted.tokenStorage.isTokenExpired.mockReturnValue(false);
    hoisted.tokenStorage.clearAllTokens.mockReset();
  });

  it('resumes a single-character account straight into the game, skipping the picker and MOTD (#927)', async () => {
    hoisted.restoreCharactersOnMountMock.mockResolvedValue([character('char-1', 'Wolfshade')]);

    const s = renderRestore();

    await waitFor(() => expect(s.setSelectedCharacterId).toHaveBeenCalledWith('char-1'));
    expect(s.setSelectedCharacterName).toHaveBeenCalledWith('Wolfshade');
    expect(s.setShowCharacterSelection).toHaveBeenCalledWith(false);
    expect(s.setShowMotd).toHaveBeenCalledWith(false);
  });

  it('shows the picker for a multi-character account and selects nothing', async () => {
    hoisted.restoreCharactersOnMountMock.mockResolvedValue([
      character('char-1', 'Wolfshade'),
      character('char-2', 'Ithaqua'),
    ]);

    const s = renderRestore();

    await waitFor(() => expect(s.setShowCharacterSelection).toHaveBeenCalledWith(true));
    expect(s.setSelectedCharacterId).not.toHaveBeenCalled();
    expect(s.setShowCharacterSelection).not.toHaveBeenCalledWith(false);
  });

  it('starts character creation for an account with no characters', async () => {
    hoisted.restoreCharactersOnMountMock.mockResolvedValue([]);

    const s = renderRestore();

    await waitFor(() => expect(s.setCreationStep).toHaveBeenCalledWith('stats'));
    expect(s.setShowCharacterSelection).toHaveBeenCalledWith(false);
    expect(s.setSelectedCharacterId).not.toHaveBeenCalled();
  });

  it('clears the session when the server rejects the token', async () => {
    hoisted.restoreCharactersOnMountMock.mockResolvedValue('unauthorized');

    const s = renderRestore();

    await waitFor(() => expect(s.setIsAuthenticated).toHaveBeenLastCalledWith(false));
    expect(hoisted.tokenStorage.clearAllTokens).toHaveBeenCalled();
    expect(s.setAuthToken).toHaveBeenLastCalledWith('');
  });
});
