/// <reference lib="es2015" />

import { beforeEach, describe, expect, it, vi } from 'vitest';

import { runAfterCharacterCreatedFlow, type CreationCompleteActions } from '../creationCompleteActions.js';
import type { CharacterInfo } from '../../types/auth.js';

const hoisted = vi.hoisted(() => ({
  refreshCharactersAfterCreationMock: vi.fn(),
  messageFromCreationRefreshHttpErrorMock: vi.fn(),
}));

vi.mock('../creationCompleteFlow.js', () => ({
  refreshCharactersAfterCreation: hoisted.refreshCharactersAfterCreationMock,
  messageFromCreationRefreshHttpError: hoisted.messageFromCreationRefreshHttpErrorMock,
}));

const REFRESH_FAILED_MESSAGE = 'Character created, but failed to refresh character list. Please refresh the page.';

const createdCharacter: CharacterInfo = {
  player_id: 'char-1',
  name: 'Wolfshade',
  profession_id: 1,
  level: 1,
  created_at: '',
  last_active: '',
};

function makeActions(): CreationCompleteActions {
  return {
    returnToLogin: vi.fn(),
    setCharacters: vi.fn(),
    setPendingStats: vi.fn(),
    setSelectedProfession: vi.fn(),
    setPendingSkillsPayload: vi.fn(),
    setCreationStep: vi.fn(),
    setShowCharacterSelection: vi.fn(),
    setError: vi.fn(),
  };
}

/** The end state every refresh-failure branch must reach: picker shown, creation flow cleared (#926). */
function expectLandedOnPicker(a: CreationCompleteActions) {
  expect(a.setError).toHaveBeenCalledWith(REFRESH_FAILED_MESSAGE);
  expect(a.setCreationStep).toHaveBeenCalledTimes(1);
  expect(a.setCreationStep).toHaveBeenCalledWith(null);
  expect(a.setPendingStats).toHaveBeenCalledWith(null);
  expect(a.setPendingSkillsPayload).toHaveBeenCalledWith(null);
  expect(a.setSelectedProfession).toHaveBeenCalledWith(undefined);
  // Exactly one call, and it is `true`: the old code called true then false, hiding the picker.
  expect(a.setShowCharacterSelection).toHaveBeenCalledTimes(1);
  expect(a.setShowCharacterSelection).toHaveBeenCalledWith(true);
  expect(a.returnToLogin).not.toHaveBeenCalled();
  expect(a.setCharacters).not.toHaveBeenCalled();
}

describe('runAfterCharacterCreatedFlow', () => {
  beforeEach(() => {
    hoisted.refreshCharactersAfterCreationMock.mockReset();
    hoisted.messageFromCreationRefreshHttpErrorMock.mockReset();
    hoisted.messageFromCreationRefreshHttpErrorMock.mockResolvedValue('refresh failed');
    vi.spyOn(console, 'error').mockImplementation(() => undefined);
  });

  it('commits the refreshed list and shows the picker on success', async () => {
    hoisted.refreshCharactersAfterCreationMock.mockResolvedValue({ outcome: 'ok', characters: [createdCharacter] });
    const a = makeActions();

    await runAfterCharacterCreatedFlow('token', a);

    expect(a.setCharacters).toHaveBeenCalledWith([createdCharacter]);
    expect(a.setCreationStep).toHaveBeenCalledWith(null);
    expect(a.setShowCharacterSelection).toHaveBeenCalledWith(true);
    expect(a.setError).not.toHaveBeenCalled();
  });

  it('returns to login when the server is unavailable', async () => {
    hoisted.refreshCharactersAfterCreationMock.mockResolvedValue({ outcome: 'server_unavailable' });
    const a = makeActions();

    await runAfterCharacterCreatedFlow('token', a);

    expect(a.returnToLogin).toHaveBeenCalledTimes(1);
    expect(a.setShowCharacterSelection).not.toHaveBeenCalled();
    expect(a.setError).not.toHaveBeenCalled();
  });

  it('lands on the picker when the refresh returns a non-5xx HTTP error (#926)', async () => {
    hoisted.refreshCharactersAfterCreationMock.mockResolvedValue({
      outcome: 'http_error',
      response: new Response(null, { status: 404 }),
    });
    const a = makeActions();

    await runAfterCharacterCreatedFlow('token', a);

    expectLandedOnPicker(a);
  });

  it('returns to login when an http_error response is a 5xx', async () => {
    hoisted.refreshCharactersAfterCreationMock.mockResolvedValue({
      outcome: 'http_error',
      response: new Response(null, { status: 503 }),
    });
    const a = makeActions();

    await runAfterCharacterCreatedFlow('token', a);

    expect(a.returnToLogin).toHaveBeenCalledTimes(1);
    expect(a.setShowCharacterSelection).not.toHaveBeenCalled();
  });

  it('lands on the picker, not the stats step, on a network_error (#926)', async () => {
    // Landing on 'stats' would invite the user to create a duplicate of a character that exists.
    hoisted.refreshCharactersAfterCreationMock.mockResolvedValue({
      outcome: 'network_error',
      error: new Error('unexpected parse failure'),
    });
    const a = makeActions();

    await runAfterCharacterCreatedFlow('token', a);

    expectLandedOnPicker(a);
  });

  it('returns to login when a network_error is a connection failure', async () => {
    hoisted.refreshCharactersAfterCreationMock.mockResolvedValue({
      outcome: 'network_error',
      error: new Error('Failed to fetch'),
    });
    const a = makeActions();

    await runAfterCharacterCreatedFlow('token', a);

    expect(a.returnToLogin).toHaveBeenCalledTimes(1);
    expect(a.setShowCharacterSelection).not.toHaveBeenCalled();
  });
});
