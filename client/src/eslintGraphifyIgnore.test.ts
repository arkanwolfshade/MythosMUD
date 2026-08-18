import { ESLint } from 'eslint';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { describe, expect, it } from 'vitest';

describe('ESLint graphify-out ignore', () => {
  it('ignores javascript inside nested graphify venvs', async () => {
    const clientRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
    const eslint = new ESLint({ cwd: clientRoot });
    const nestedVenvJs = 'graphify-out/.venv/Lib/site-packages/urllib3/contrib/emscripten/emscripten_fetch_worker.js';

    await expect(eslint.isPathIgnored(nestedVenvJs)).resolves.toBe(true);
  });
});
