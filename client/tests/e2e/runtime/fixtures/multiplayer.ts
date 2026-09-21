/**
 * Multiplayer Fixtures
 *
 * Helper functions for managing multiple browser contexts in multiplayer scenarios.
 * Implementation is split across multiplayer-contexts / -ready / -colocated (Lizard NLOC).
 */

export {
  cleanupMultiPlayerContexts,
  createMultiPlayerContexts,
  reopenPlayerPageIfClosed,
} from './multiplayer-contexts';
export type { PlayerContext } from './multiplayer-contexts';

export {
  ensureFreshMultiPlayerContexts,
  ensurePlayerInGame,
  getPlayerMessages,
  prepareReceiverForInboundMessages,
  waitForAllPlayersInGame,
  waitForCrossPlayerMessage,
} from './multiplayer-ready';

export {
  ensureMultiplayerCoLocated,
  ensurePlayersInSameRoom,
  resetE2ePlayerRoomsInDatabase,
  waitForLookReflectedInUi,
} from './multiplayer-colocated';
