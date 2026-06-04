/**
 * Lightweight linkdead helpers for specs that need in-place heal without full relogin.
 * Full recovery lives in auth.ts (`recoverPlayableSession`, `ensurePlayableConnection`).
 */

import type { Page } from '@playwright/test';

import { assertCommandChannelReady, executeCommandWithoutRecovery } from './auth';

const RECOVER_COMMAND_READY_MS = 8000;

/** Stand + command channel ready without navigation. */
export async function tryInPlacePlayableRecovery(page: Page, timeoutMs: number): Promise<boolean> {
  await page.bringToFront().catch(() => {});
  await executeCommandWithoutRecovery(page, 'stand').catch(() => {});
  return assertCommandChannelReady(page, Math.min(timeoutMs, RECOVER_COMMAND_READY_MS));
}

export interface LinkdeadRecoveryCredentials {
  username: string;
  password: string;
}

/** In-place heal, then ensurePlayableConnection when the channel is still blocked. */
export async function ensureSessionHealthy(
  page: Page,
  creds: LinkdeadRecoveryCredentials,
  timeoutMs = 45000
): Promise<void> {
  if (await tryInPlacePlayableRecovery(page, 15000)) {
    return;
  }
  const { ensurePlayableConnection } = await import('./auth');
  await ensurePlayableConnection(page, {
    username: creds.username,
    password: creds.password,
    timeoutMs,
  });
}
