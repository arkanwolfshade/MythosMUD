// Header active effects from game state (login warded fallback).

import type { ActiveEffectDisplay, GameState } from '../utils/stateUpdateUtils';

export function deriveActiveEffectsForHeader(gameState: GameState): ActiveEffectDisplay[] {
  if (gameState.activeEffects) {
    return gameState.activeEffects;
  }
  if (gameState.loginGracePeriodActive && gameState.loginGracePeriodRemaining !== undefined) {
    return [
      {
        effect_type: 'login_warded',
        label: 'Warded',
        remaining_seconds: gameState.loginGracePeriodRemaining,
      } satisfies ActiveEffectDisplay,
    ];
  }
  return [];
}
