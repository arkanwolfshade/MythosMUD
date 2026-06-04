import { describe, expect, it } from 'vitest';

import { E2E_ENV_DEFAULTS, formatLoginFailure, parseE2eEnvContent, redactDatabaseUrl } from './e2e-bootstrap';

describe('e2e-bootstrap', () => {
  it('parseE2eEnvContent reads DATABASE_URL and POSTGRES_SEARCH_PATH', () => {
    const content = [
      '# comment',
      'DATABASE_URL=postgresql://postgres:secret@localhost:5432/mythos_e2e',
      'POSTGRES_SEARCH_PATH=mythos_e2e',
      'OTHER=value',
    ].join('\n');
    expect(parseE2eEnvContent(content)).toEqual({
      DATABASE_URL: 'postgresql://postgres:secret@localhost:5432/mythos_e2e',
      POSTGRES_SEARCH_PATH: 'mythos_e2e',
    });
  });

  it('redactDatabaseUrl hides password', () => {
    const url = 'postgresql://postgres:Cthulhu1@localhost:5432/mythos_e2e';
    expect(redactDatabaseUrl(url)).not.toContain('Cthulhu1');
    expect(redactDatabaseUrl(url)).toContain('mythos_e2e');
  });

  it('formatLoginFailure includes status and body hints', () => {
    const lines = formatLoginFailure(400, '{"detail":"bad"}', '/v1/auth/jwt/login', E2E_ENV_DEFAULTS);
    expect(lines.some(l => l.includes('HTTP 400'))).toBe(true);
    expect(lines.some(l => l.includes('bad'))).toBe(true);
    expect(lines.some(l => l.includes('mythos_e2e'))).toBe(true);
  });
});
