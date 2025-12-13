// Combat-related event handlers
// As documented in "Combat Event Processing" - Dr. Armitage, 1928

import type { EventHandler } from './types';
import { sanitizeChatMessageForState } from '../utils/messageUtils';

const GAME_LOG_CHANNEL = 'game-log';

export const handleNpcAttacked: EventHandler = (event, _context, appendMessage) => {
  const attackerName = (event.data.attacker_name || event.data.npc_name) as string | undefined;
  const damage = event.data.damage as number | undefined;
  const actionType = event.data.action_type as string | undefined;
  const targetCurrentDp = event.data.target_current_dp as number | undefined;
  const targetMaxDp = event.data.target_max_dp as number | undefined;

  if (attackerName && damage !== undefined) {
    let message = `${attackerName} ${actionType || 'attacks'} you for ${damage} damage.`;
    if (targetCurrentDp !== undefined && targetMaxDp !== undefined) {
      message += ` (${targetCurrentDp}/${targetMaxDp} DP)`;
    }
    appendMessage(
      sanitizeChatMessageForState({
        text: message,
        timestamp: event.timestamp,
        messageType: 'system',
        channel: GAME_LOG_CHANNEL,
        isHtml: false,
      })
    );
  }
};

export const handlePlayerAttacked: EventHandler = (event, _context, appendMessage) => {
  const attackerName = event.data.attacker_name as string | undefined;
  const targetName = event.data.target_name as string | undefined;
  const damage = event.data.damage as number | undefined;
  const actionType = event.data.action_type as string | undefined;
  const targetCurrentDp = event.data.target_current_dp as number | undefined;
  const targetMaxDp = event.data.target_max_dp as number | undefined;

  if (attackerName && targetName && damage !== undefined) {
    let message = `You ${actionType || 'attack'} ${targetName} for ${damage} damage.`;
    if (targetCurrentDp !== undefined && targetMaxDp !== undefined) {
      message += ` (${targetCurrentDp}/${targetMaxDp} DP)`;
    }
    appendMessage(
      sanitizeChatMessageForState({
        text: message,
        timestamp: event.timestamp,
        messageType: 'system',
        channel: GAME_LOG_CHANNEL,
        isHtml: false,
      })
    );
  }
};

export const handleCombatStarted: EventHandler = (_event, context) => {
  if (context.currentPlayerRef.current) {
    return {
      player: {
        ...context.currentPlayerRef.current,
        in_combat: true,
      },
    };
  }
};

export const handleCombatEnded: EventHandler = (_event, context) => {
  if (context.currentPlayerRef.current) {
    return {
      player: {
        ...context.currentPlayerRef.current,
        in_combat: false,
      },
    };
  }
};

export const handleNpcDied: EventHandler = (event, _context, appendMessage) => {
  const npcName = event.data.npc_name as string | undefined;
  const xpReward = event.data.xp_reward as number | undefined;

  if (npcName) {
    const deathMessage = `${npcName} dies.`;
    appendMessage(
      sanitizeChatMessageForState({
        text: deathMessage,
        timestamp: event.timestamp,
        messageType: 'combat',
        channel: GAME_LOG_CHANNEL,
        isHtml: false,
      })
    );

    if (xpReward !== undefined && xpReward > 0) {
      const xpMessage = `You gain ${xpReward} experience points.`;
      appendMessage(
        sanitizeChatMessageForState({
          text: xpMessage,
          timestamp: event.timestamp,
          messageType: 'system',
          channel: GAME_LOG_CHANNEL,
          isHtml: false,
        })
      );
    }
  }
};

export const handleCombatDeath: EventHandler = (event, _context, appendMessage) => {
  const messages = event.data.messages as { death_message?: string; xp_reward?: string } | undefined;

  if (messages) {
    if (messages.death_message) {
      appendMessage(
        sanitizeChatMessageForState({
          text: messages.death_message,
          timestamp: event.timestamp,
          messageType: 'combat',
          channel: GAME_LOG_CHANNEL,
          isHtml: false,
        })
      );
    }

    if (messages.xp_reward) {
      appendMessage(
        sanitizeChatMessageForState({
          text: messages.xp_reward,
          timestamp: event.timestamp,
          messageType: 'system',
          channel: GAME_LOG_CHANNEL,
          isHtml: false,
        })
      );
    }
  }
};
