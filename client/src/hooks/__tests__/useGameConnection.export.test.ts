import { describe, expect, it } from 'vitest';

import { useGameConnection } from '../useGameConnection';
import { useGameConnection as useGameConnectionRefactored } from '../useGameConnectionRefactored';

describe('useGameConnection export wrapper', () => {
  it('re-exports the refactored hook symbol', () => {
    expect(useGameConnection).toBe(useGameConnectionRefactored);
  });
});
