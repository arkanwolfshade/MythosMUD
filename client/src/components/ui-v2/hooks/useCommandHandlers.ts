// Command handlers hook
// Extracted from GameClientV2Container to reduce complexity

import { useCallback } from 'react';
import { logger } from '../../../utils/logger';
import { inputSanitizer } from '../../../utils/security';
import type { GameState } from '../utils/stateUpdateUtils';

interface UseCommandHandlersParams {
  isConnected: boolean;
  sendCommand: (command: string, args?: string[]) => Promise<boolean>;
  setGameState: React.Dispatch<React.SetStateAction<GameState>>;
}

export const useCommandHandlers = ({ isConnected, sendCommand, setGameState }: UseCommandHandlersParams) => {
  const handleCommandSubmit = useCallback(
    async (command: string) => {
      if (!command.trim() || !isConnected) return;

      let normalized = command.trim();
      const lower = normalized.toLowerCase();
      const dirMap: Record<string, string> = {
        n: 'north',
        s: 'south',
        e: 'east',
        w: 'west',
        ne: 'northeast',
        nw: 'northwest',
        se: 'southeast',
        sw: 'southwest',
        u: 'up',
        d: 'down',
        up: 'up',
        down: 'down',
      };

      const parts = normalized.split(/\s+/);
      if (parts.length === 1 && dirMap[lower]) {
        normalized = `go ${dirMap[lower]}`;
      } else if (parts.length === 2) {
        const [verb, arg] = [parts[0].toLowerCase(), parts[1].toLowerCase()];
        if ((verb === 'go' || verb === 'look') && dirMap[arg]) {
          normalized = `${verb} ${dirMap[arg]}`;
        }
      }

      setGameState(prev => ({ ...prev, commandHistory: [...prev.commandHistory, normalized] }));

      const commandParts = normalized.split(/\s+/);
      const commandName = commandParts[0];
      const commandArgs = commandParts.slice(1);

      const success = await sendCommand(commandName, commandArgs);
      if (!success) {
        logger.error('GameClientV2Container', 'Failed to send command', { command: commandName, args: commandArgs });
      }
    },
    [isConnected, sendCommand, setGameState]
  );

  const handleChatMessage = useCallback(
    async (message: string, channel: string) => {
      if (!message.trim() || !isConnected) return;

      const sanitizedMessage = inputSanitizer.sanitizeChatMessage(message);
      const sanitizedChannel = inputSanitizer.sanitizeCommand(channel);

      if (!sanitizedMessage.trim()) {
        logger.warn('GameClientV2Container', 'Chat message was empty after sanitization');
        return;
      }

      const success = await sendCommand('chat', [sanitizedChannel, sanitizedMessage]);
      if (!success) {
        logger.error('GameClientV2Container', 'Failed to send chat message', {
          channel: sanitizedChannel,
          message: sanitizedMessage,
        });
      }
    },
    [isConnected, sendCommand]
  );

  const handleClearMessages = useCallback(() => {
    setGameState(prev => ({ ...prev, messages: [] }));
  }, [setGameState]);

  const handleClearHistory = useCallback(() => {
    setGameState(prev => ({ ...prev, commandHistory: [] }));
  }, [setGameState]);

  return {
    handleCommandSubmit,
    handleChatMessage,
    handleClearMessages,
    handleClearHistory,
  };
};
