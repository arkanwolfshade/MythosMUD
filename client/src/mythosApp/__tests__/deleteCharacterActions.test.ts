/// <reference lib="es2015" />

import { beforeEach, describe, expect, it, vi } from 'vitest';

import { executeDeleteCharacterUi, type DeleteCharacterUiDeps } from '../deleteCharacterActions.js';
import type { CharacterInfo } from '../../types/auth.js';

const hoisted = vi.hoisted(() => ({
  runDeleteCharacterFlowMock: vi.fn(),
}));

vi.mock('../deleteCharacterFlow.js', async importOriginal => {
  const actual = await importOriginal<typeof import('../deleteCharacterFlow.js')>();
  return {
    ...actual,
    runDeleteCharacterFlow: hoisted.runDeleteCharacterFlowMock,
  };
});

const existingCharacters: CharacterInfo[] = [
  { player_id: 'char-1', name: 'Wolfshade', profession_id: 1, level: 1, created_at: '', last_active: '' },
  { player_id: 'char-2', name: 'Ithaqua', profession_id: 2, level: 1, created_at: '', last_active: '' },
];

function makeDeps(initialCharacters: CharacterInfo[]) {
  let characters = initialCharacters;
  const deps: DeleteCharacterUiDeps = {
    returnToLogin: vi.fn(),
    setCharacters: vi.fn(update => {
      characters =
        typeof update === 'function' ? (update as (prev: CharacterInfo[]) => CharacterInfo[])(characters) : update;
    }),
    setShowCharacterSelection: vi.fn(),
    setCreationStep: vi.fn(),
    setSelectedProfession: vi.fn(),
    setError: vi.fn(),
  };
  return { deps, getCharacters: () => characters };
}

describe('executeDeleteCharacterUi', () => {
  beforeEach(() => {
    hoisted.runDeleteCharacterFlowMock.mockReset();
  });

  it('commits the refreshed character list on success', async () => {
    hoisted.runDeleteCharacterFlowMock.mockResolvedValue({
      outcome: 'ok',
      characters: [existingCharacters[1]],
    });
    const { deps, getCharacters } = makeDeps(existingCharacters);

    await executeDeleteCharacterUi('token', 'char-1', deps);

    expect(getCharacters()).toEqual([existingCharacters[1]]);
    expect(deps.setError).not.toHaveBeenCalled();
  });

  it('removes the character locally without throwing when the post-delete refresh fails (#777)', async () => {
    // The DELETE request already succeeded server-side (the mock's outcome reflects the
    // server's confirmed truth); only the follow-up GET failed. The deleted character
    // must not be left stranded in `characters` just because that secondary read failed.
    hoisted.runDeleteCharacterFlowMock.mockResolvedValue({
      outcome: 'refresh_failed',
      message: 'Character deleted, but failed to refresh character list',
      characterId: 'char-1',
    });
    const { deps, getCharacters } = makeDeps(existingCharacters);

    await expect(executeDeleteCharacterUi('token', 'char-1', deps)).resolves.toBeUndefined();

    expect(getCharacters()).toEqual([existingCharacters[1]]);
    expect(deps.setError).not.toHaveBeenCalled();
  });

  it('resets to character creation when the last character is removed locally after a refresh failure', async () => {
    hoisted.runDeleteCharacterFlowMock.mockResolvedValue({
      outcome: 'refresh_failed',
      message: 'refresh broke',
      characterId: 'char-1',
    });
    const { deps, getCharacters } = makeDeps([existingCharacters[0]]);

    await executeDeleteCharacterUi('token', 'char-1', deps);

    expect(getCharacters()).toEqual([]);
    expect(deps.setShowCharacterSelection).toHaveBeenCalledWith(false);
    expect(deps.setCreationStep).toHaveBeenCalledWith('stats');
    expect(deps.setSelectedProfession).toHaveBeenCalledWith(undefined);
  });

  it('throws and leaves state untouched when the delete itself fails', async () => {
    hoisted.runDeleteCharacterFlowMock.mockResolvedValue({ outcome: 'delete_failed', message: 'nope' });
    const { deps, getCharacters } = makeDeps(existingCharacters);

    await expect(executeDeleteCharacterUi('token', 'char-1', deps)).rejects.toThrow('nope');

    expect(getCharacters()).toEqual(existingCharacters);
  });

  it('returns to login on server_unavailable without throwing', async () => {
    hoisted.runDeleteCharacterFlowMock.mockResolvedValue({ outcome: 'server_unavailable' });
    const { deps } = makeDeps(existingCharacters);

    await expect(executeDeleteCharacterUi('token', 'char-1', deps)).resolves.toBeUndefined();

    expect(deps.returnToLogin).toHaveBeenCalledOnce();
  });
});
