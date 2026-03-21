// Logout flow for GameClientV2 (extracted for Lizard NLOC).

import { logger } from '../../../utils/logger';

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
  }
}
