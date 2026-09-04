/// <reference types="node" />

/**
 * Shared E2E bootstrap helpers: env loading, loud failure logging, and diagnostics.
 * Used by Playwright global-setup.ts; unit-tested via Vitest (tsconfig.test.json).
 */

import * as fs from 'fs';
import * as path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

/** Repository root (parent of client/). */
export const E2E_PROJECT_ROOT = path.resolve(__dirname, '..', '..', '..');

/** Local dev stack (HTTP, IPv4 loopback; matches playwright.runtime.config baseURL). */
export const E2E_SERVER_URL = 'http://127.0.0.1:54768';
export const E2E_CLIENT_URL = 'http://127.0.0.1:5173';

export const E2E_ENV_DEFAULTS: Record<string, string> = {
  DATABASE_URL: 'postgresql://postgres:Cthulhu1@localhost:5432/mythos_e2e',
  POSTGRES_SEARCH_PATH: 'mythos_e2e',
};

export const E2E_BOOTSTRAP_LOG_DIR = path.join(E2E_PROJECT_ROOT, 'logs', 'e2e_test');
export const E2E_BOOTSTRAP_ERRORS_LOG = path.join(E2E_BOOTSTRAP_LOG_DIR, 'bootstrap-errors.log');

/** Parse .env file content and return only DATABASE_URL and POSTGRES_SEARCH_PATH. */
export function parseE2eEnvContent(content: string): Record<string, string> {
  const env: Record<string, string> = {};
  for (const line of content.split('\n')) {
    const m = line.match(/^([^#][^=]+)=(.*)$/);
    if (m) {
      const key = m[1].trim();
      const value = m[2].trim();
      if (key === 'DATABASE_URL' || key === 'POSTGRES_SEARCH_PATH') env[key] = value;
    }
  }
  return env;
}

/** Load DATABASE_URL and POSTGRES_SEARCH_PATH from .env.e2e_test so seed uses same schema as E2E server. */
export function loadE2eEnv(): Record<string, string> {
  const envPath = path.join(E2E_PROJECT_ROOT, '.env.e2e_test');
  if (!fs.existsSync(envPath)) return { ...E2E_ENV_DEFAULTS };
  const content = fs.readFileSync(envPath, 'utf-8');
  const env = parseE2eEnvContent(content);
  return {
    DATABASE_URL: env.DATABASE_URL ?? E2E_ENV_DEFAULTS.DATABASE_URL,
    POSTGRES_SEARCH_PATH: env.POSTGRES_SEARCH_PATH ?? E2E_ENV_DEFAULTS.POSTGRES_SEARCH_PATH,
  };
}

/** Hide password in DATABASE_URL for operator-facing logs. */
export function redactDatabaseUrl(databaseUrl: string): string {
  try {
    const parsed = new URL(databaseUrl.replace(/^postgresql\+asyncpg:/, 'postgresql:'));
    if (parsed.password) parsed.password = '***';
    return parsed.toString();
  } catch {
    return databaseUrl.replace(/:([^:@/]+)@/, ':***@');
  }
}

export function appendBootstrapFailureLog(lines: string[]): void {
  fs.mkdirSync(E2E_BOOTSTRAP_LOG_DIR, { recursive: true });
  const stamp = new Date().toISOString();
  const block = [`\n=== E2E bootstrap failure ${stamp} ===`, ...lines, ''].join('\n');
  fs.appendFileSync(E2E_BOOTSTRAP_ERRORS_LOG, block, 'utf-8');
}

/**
 * Log to stderr, append bootstrap-errors.log, and throw so Playwright exits non-zero.
 */
export function failBootstrap(step: string, message: string, details: string[] = []): never {
  const env = loadE2eEnv();
  const header = [
    `E2E BOOTSTRAP FAILED at step: ${step}`,
    message,
    `Server URL: ${E2E_SERVER_URL}`,
    `DATABASE_URL (redacted): ${redactDatabaseUrl(env.DATABASE_URL ?? '')}`,
    `POSTGRES_SEARCH_PATH: ${env.POSTGRES_SEARCH_PATH ?? ''}`,
    `Log file: ${E2E_BOOTSTRAP_ERRORS_LOG}`,
    'Also check logs/e2e_test/errors.log and warnings.log on the running E2E server.',
    ...details,
  ];
  for (const line of header) {
    console.error(line);
  }
  appendBootstrapFailureLog(header);
  throw new Error(`${step}: ${message}`);
}

export function spawnOutputDetail(stdout: string | null | undefined, stderr: string | null | undefined): string {
  const parts = [stderr?.trim(), stdout?.trim()].filter(p => p && p.length > 0);
  return parts.join('\n') || '(no stdout/stderr captured)';
}

export function countProfessionsPayload(raw: unknown): number {
  if (Array.isArray(raw)) {
    return raw.length;
  }
  if (raw !== null && typeof raw === 'object' && 'professions' in raw) {
    const inner = (raw as { professions: unknown }).professions;
    return Array.isArray(inner) ? inner.length : 0;
  }
  return 0;
}

export function formatLoginFailure(
  status: number,
  bodyText: string,
  endpoint: string,
  env: Record<string, string>
): string[] {
  const lines = [
    `POST ${endpoint} returned HTTP ${status}`,
    `Response body: ${bodyText || '(empty)'}`,
    `Seed uses DATABASE_URL=${redactDatabaseUrl(env.DATABASE_URL ?? '')} and POSTGRES_SEARCH_PATH=${env.POSTGRES_SEARCH_PATH ?? ''}.`,
    'The process on port 54768 must use the same .env.e2e_test (mythos_e2e).',
    'If seed succeeded but login fails, restart the E2E server after seeding or run e2e.bat from this worktree.',
  ];
  if (status === 401) {
    lines.push('401 usually means wrong password or user missing in the DB the server is using.');
  }
  if (status === 400) {
    lines.push(
      '400 may mean wrong credentials, inactive user, or a non-E2E server on 54768.',
      '/v1/auth/jwt/login expects email in the OAuth2 username field; E2E bootstrap uses /v1/auth/login for MythosMUD usernames.'
    );
  }
  if (status === 503) {
    lines.push('503 may mean the server is shutting down; wait and retry or restart e2e.bat.');
  }
  return lines;
}
