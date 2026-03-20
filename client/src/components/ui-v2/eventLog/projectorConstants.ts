// Projector constants and initial state (split from projector.ts for file-nloc)

import type { GameState } from '../utils/stateUpdateUtils';

/** Initial GameState before any events */
export function getInitialGameState(): GameState {
  return {
    player: null,
    room: null,
    messages: [],
    commandHistory: [],
    loginGracePeriodActive: false,
    loginGracePeriodRemaining: 0,
    mythosTime: null,
    lastQuarterHourForChime: null,
  };
}

/** Known event types that affect state (allowlist for projector) */
export const PROJECTED_EVENT_TYPES = new Set([
  'game_state',
  'quest_log_updated',
  'effects_update',
  'room_update',
  'room_state',
  'room_occupants',
  'player_entered_game',
  'player_entered',
  'player_left_game',
  'player_left',
  'player_died',
  'playerdied',
  'player_respawned',
  'playerrespawned',
  'player_delirium_respawned',
  'playerdeliriumrespawned',
  'player_dp_updated',
  'playerdpupdated',
  'player_update',
  'command_response',
  'chat_message',
  'room_message',
  'system',
  'npc_attacked',
  'player_attacked',
  'combat_started',
  'combat_ended',
  'npc_died',
  'combat_death',
  'combat_target_switch',
  'lucidity_change',
  'luciditychange',
  'intentional_disconnect',
  'game_tick',
  'follow_request',
  'follow_request_cleared',
  'follow_state',
  'party_invite',
  'party_invite_cleared',
]);
