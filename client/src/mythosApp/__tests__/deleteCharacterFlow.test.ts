import { describe, expect, it } from 'vitest';

import { nextStepForDeleteResult, type DeleteCharacterFlowResult } from '../deleteCharacterFlow.js';
import type { CharacterInfo } from '../../types/auth.js';

const mockCharacters: CharacterInfo[] = [
  {
    player_id: 'char-1',
    name: 'Wolfshade',
    profession_id: 1,
    level: 1,
    created_at: '2026-01-01T00:00:00Z',
    last_active: '2026-01-01T00:00:00Z',
  },
];

describe('nextStepForDeleteResult', () => {
  it('maps server_unavailable to return_to_login', () => {
    const result: DeleteCharacterFlowResult = { outcome: 'server_unavailable' };
    expect(nextStepForDeleteResult(result)).toEqual({ step: 'return_to_login' });
  });

  it('maps delete_failed to throw', () => {
    const result: DeleteCharacterFlowResult = { outcome: 'delete_failed', message: 'boom' };
    expect(nextStepForDeleteResult(result)).toEqual({ step: 'throw', message: 'boom' });
  });

  it('maps ok to commit with the refreshed characters', () => {
    const result: DeleteCharacterFlowResult = { outcome: 'ok', characters: mockCharacters };
    expect(nextStepForDeleteResult(result)).toEqual({ step: 'commit', characters: mockCharacters });
  });

  it('maps refresh_failed to commit_remove_locally rather than throwing (#777)', () => {
    // The DELETE itself already succeeded server-side; only the follow-up list refetch
    // failed. This must not be treated the same as delete_failed -- the caller should
    // remove the character locally instead of leaving it stranded in the UI.
    const result: DeleteCharacterFlowResult = {
      outcome: 'refresh_failed',
      message: 'Character deleted, but failed to refresh character list',
      characterId: 'char-1',
    };
    expect(nextStepForDeleteResult(result)).toEqual({
      step: 'commit_remove_locally',
      characterId: 'char-1',
      message: 'Character deleted, but failed to refresh character list',
    });
  });
});
