// Logout flow for GameClientV2 (extracted for Lizard NLOC).

import { logger } from '../../../utils/logger';

/** Rest countdown is ~10s; if disconnect never arrives, force navigate to login. */
const REST_LOGOUT_FALLBACK_MS = 15000;

function forceLogoutFallback(onLogout: (() => void) | undefined, disconnect: () => void): void {
  logger.error('GameClientV2Container', 'Rest logout did not disconnect in time, falling back to immediate logout');
  if (onLogout) onLogout();
  else disconnect();
}

function stillShowingGameClient(): boolean {
  return (
    document.querySelector('[data-testid="command-input"]') !== null &&
    document.querySelector('[data-testid="username-input"]') === null
  );
}

export async function performGameClientLogout(
  isConnected: boolean,
  onLogout: (() => void) | undefined,
  disconnect: () => void,
  sendCommand: (command: string, args?: string[]) => Promise<boolean>,
  setIntentionalExit: (value: boolean) => void
): Promise<void> {
  if (!isConnected) {
    if (onLogout) onLogout();
    else disconnect();
    return;
  }
  setIntentionalExit(true);
  const success = await sendCommand('rest', []);
  if (!success) {
    logger.error('GameClientV2Container', 'Failed to send /rest command, falling back to immediate disconnect');
    if (onLogout) onLogout();
    else disconnect();
    return;
  }
  // Rest success relies on server disconnect + intentional-exit handlers. If that stalls, UI stays Connected.
  window.setTimeout(() => {
    if (stillShowingGameClient()) {
      forceLogoutFallback(onLogout, disconnect);
    }
  }, REST_LOGOUT_FALLBACK_MS);
}
