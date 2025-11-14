import { useCallback, useEffect, useRef, useState } from 'react';
import { useGameConnection } from '../hooks/useGameConnectionRefactored';
import { logger } from '../utils/logger';
import { useMemoryMonitor } from '../utils/memoryMonitor';
import { determineMessageType } from '../utils/messageTypeUtils';
import { inputSanitizer } from '../utils/security';
import { convertToPlayerInterface, parseStatusResponse } from '../utils/statusParser';
import {
  buildSanityStatus,
  buildSanityChangeMessage,
  createHallucinationEntry,
  createRescueState,
} from '../utils/sanityEventUtils';
import type { SanityStatus, HallucinationMessage, RescueState } from '../types/sanity';

// Import GameEvent interface from useGameConnection
interface GameEvent {
  event_type: string;
  timestamp: string;
  sequence_number: number;
  player_id?: string;
  room_id?: string;
  data: Record<string, unknown>;
  alias_chain?: Array<{
    original: string;
    expanded: string;
    alias_name: string;
  }>;
}

import { CommandHelpDrawer } from './CommandHelpDrawer';
import { DeathInterstitial } from './DeathInterstitial';
import { GameTerminal } from './GameTerminal';

interface GameTerminalWithPanelsProps {
  playerName: string;
  authToken: string;
  onLogout?: () => void;
  isLoggingOut?: boolean;
  onDisconnect?: (disconnectFn: () => void) => void;
}

interface Player {
  name: string;
  profession_id?: number;
  profession_name?: string;
  profession_description?: string;
  profession_flavor_text?: string;
  stats?: {
    current_health: number;
    sanity: number;
    strength?: number;
    dexterity?: number;
    constitution?: number;
    intelligence?: number;
    wisdom?: number;
    charisma?: number;
    occult_knowledge?: number;
    fear?: number;
    corruption?: number;
    cult_affiliation?: number;
  };
  level?: number;
  experience?: number;
  xp?: number;
  current_room_id?: string;
  in_combat?: boolean;
}

interface Room {
  id: string;
  name: string;
  description: string;
  plane?: string;
  zone?: string;
  sub_zone?: string;
  environment?: string;
  exits: Record<string, string>;
  occupants?: string[];
  occupant_count?: number;
  entities?: Array<{
    name: string;
    type: string;
  }>;
}

interface ChatMessage {
  text: string;
  timestamp: string;
  isHtml: boolean;
  isCompleteHtml?: boolean;
  messageType?: string;
  channel?: string;
  type?: string;
  aliasChain?: Array<{
    original: string;
    expanded: string;
    alias_name: string;
  }>;
  rawText?: string;
  tags?: string[];
}

const GAME_LOG_CHANNEL = 'game-log';

const resolveChatTypeFromChannel = (channel: string): string => {
  switch (channel) {
    case 'whisper':
      return 'whisper';
    case 'shout':
      return 'shout';
    case 'emote':
      return 'emote';
    case 'party':
    case 'tell':
      return 'tell';
    case 'system':
    case 'game':
      return 'system';
    case 'local':
    case 'say':
    default:
      return 'say';
  }
};

const sanitizeChatMessageForState = (message: ChatMessage): ChatMessage => {
  const rawText = (message as ChatMessage & { rawText?: string }).rawText ?? message.text;
  const sanitizedText = message.isHtml ? inputSanitizer.sanitizeIncomingHtml(rawText) : rawText;

  const existingType = message.type ?? 'system';
  const existingChannel = (message as { channel?: string }).channel ?? 'system';
  const messageType = (message as { messageType?: string }).messageType ?? (existingType as unknown as string);

  return {
    ...message,
    type: existingType,
    messageType,
    channel: existingChannel,
    rawText,
    text: sanitizedText,
  };
};

const normalizeName = (value: unknown): string | null => {
  if (typeof value !== 'string') {
    return null;
  }
  const trimmed = value.trim();
  return trimmed.length > 0 ? trimmed.toLowerCase() : null;
};

type CombatParticipant = {
  name?: string;
  [key: string]: unknown;
};

const isPlayerCombatParticipant = (
  player: Player | null,
  participants: Record<string, CombatParticipant> | undefined,
  turnOrder: string[] | undefined
): boolean => {
  if (!player) {
    return false;
  }

  const playerName = normalizeName(player.name);
  if (!playerName) {
    return false;
  }

  const participantList = participants ? Object.values(participants) : [];
  if (participantList.some(participant => normalizeName(participant?.name) === playerName)) {
    return true;
  }

  if (turnOrder && participants) {
    return turnOrder.some(id => {
      const participant = participants[id];
      return participant ? normalizeName(participant.name) === playerName : false;
    });
  }

  return false;
};

interface GameState {
  player: Player | null;
  room: Room | null;
  messages: ChatMessage[];
  commandHistory: string[];
}

export const GameTerminalWithPanels: React.FC<GameTerminalWithPanelsProps> = ({
  playerName,
  authToken,
  onLogout,
  isLoggingOut = false,
  onDisconnect: _onDisconnect,
}) => {
  const [gameState, setGameState] = useState<GameState>({
    player: null,
    room: null,
    messages: [],
    commandHistory: [],
  });

  // Death/respawn states for UI theming
  const [isMortallyWounded, setIsMortallyWounded] = useState(false);
  const [isDead, setIsDead] = useState(false);
  const [deathLocation, setDeathLocation] = useState<string>('Unknown Location');
  const [isRespawning, setIsRespawning] = useState(false);
  const [sanityStatus, setSanityStatus] = useState<SanityStatus | null>(null);
  const [hallucinationFeed, setHallucinationFeed] = useState<HallucinationMessage[]>([]);
  const [rescueState, setRescueState] = useState<RescueState | null>(null);

  // Memory monitoring for this component
  const { detector } = useMemoryMonitor('GameTerminalWithPanels');

  // Start memory monitoring for this component
  useEffect(() => {
    detector.start();
    return () => detector.stop();
  }, [detector]);

  // Refs for stable references and event processing
  const hasAttemptedConnection = useRef(false);
  const isProcessingEvent = useRef(false);
  const lastProcessedEvent = useRef<string>('');
  const eventQueue = useRef<GameEvent[]>([]);
  const processingTimeout = useRef<number | null>(null);
  const currentMessagesRef = useRef<ChatMessage[]>([]);
  const currentRoomRef = useRef<Room | null>(null);
  const currentPlayerRef = useRef<Player | null>(null);
  const activeCombatIdRef = useRef<string | null>(null);
  const sanityStatusRef = useRef<SanityStatus | null>(null);
  const rescueTimeoutRef = useRef<number | null>(null);

  // Keep the refs in sync with the state
  useEffect(() => {
    currentMessagesRef.current = gameState.messages;
  }, [gameState.messages]);

  useEffect(() => {
    console.log('🔍 DEBUG: Room state updated', {
      oldRoom: currentRoomRef.current,
      newRoom: gameState.room,
      occupantsChanged: currentRoomRef.current?.occupants?.length !== gameState.room?.occupants?.length,
    });
    currentRoomRef.current = gameState.room;
  }, [gameState.room]);

  useEffect(() => {
    currentPlayerRef.current = gameState.player;
  }, [gameState.player]);

  useEffect(() => {
    sanityStatusRef.current = sanityStatus;
  }, [sanityStatus]);

  useEffect(() => {
    const interval = window.setInterval(() => {
      setHallucinationFeed(prev =>
        prev.filter(entry => {
          const timestamp = new Date(entry.timestamp).getTime();
          return Number.isFinite(timestamp) ? Date.now() - timestamp < 60_000 : false;
        })
      );
    }, 10_000);

    return () => window.clearInterval(interval);
  }, []);

  useEffect(() => {
    if (rescueTimeoutRef.current) {
      window.clearTimeout(rescueTimeoutRef.current);
      rescueTimeoutRef.current = null;
    }

    if (rescueState && ['success', 'failed', 'sanitarium'].includes(rescueState.status)) {
      rescueTimeoutRef.current = window.setTimeout(() => setRescueState(null), 8_000);
    }

    return () => {
      if (rescueTimeoutRef.current) {
        window.clearTimeout(rescueTimeoutRef.current);
        rescueTimeoutRef.current = null;
      }
    };
  }, [rescueState]);

  // Track the last room update timestamp to prevent stale data overwrites
  const lastRoomUpdateTime = useRef<number>(0);

  // Ref to store sendCommand function for use in event handlers
  const sendCommandRef = useRef<((command: string, args?: string[]) => Promise<boolean>) | null>(null);

  // Room data validation function to prevent stale data overwrites
  const validateRoomDataForOccupants = useCallback((currentRoom: Room, event: GameEvent) => {
    // Check if the event timestamp is recent enough to be valid
    const eventTime = new Date(event.timestamp).getTime();
    const currentTime = Date.now();
    const timeDiff = currentTime - eventTime;

    logger.info('GameTerminalWithPanels', '🔍 VALIDATION DEBUG: validateRoomDataForOccupants called', {
      currentRoomId: currentRoom.id,
      currentRoomName: currentRoom.name,
      eventTimestamp: event.timestamp,
      eventTime,
      currentTime,
      timeDiff,
      lastRoomUpdateTime: lastRoomUpdateTime.current,
    });

    // If event is older than 5 seconds, it might be stale
    if (timeDiff > 5000) {
      logger.warn('GameTerminalWithPanels', '🔍 VALIDATION DEBUG: Event timestamp too old', {
        timeDiff,
        threshold: 5000,
      });
      return {
        isValid: false,
        reason: 'Event timestamp too old',
        timeDiff,
      };
    }

    // Check if this room_occupants event is older than the last room update
    if (eventTime < lastRoomUpdateTime.current) {
      logger.warn(
        'GameTerminalWithPanels',
        '🔍 VALIDATION DEBUG: Room occupants event is older than last room update',
        {
          eventTime,
          lastRoomUpdateTime: lastRoomUpdateTime.current,
          timeDiff: lastRoomUpdateTime.current - eventTime,
          currentRoomId: currentRoom.id,
          currentRoomName: currentRoom.name,
        }
      );
      return {
        isValid: false,
        reason: 'Event is older than last room update',
        eventTime,
        lastRoomUpdateTime: lastRoomUpdateTime.current,
      };
    }

    // Check if the room data seems consistent
    if (!currentRoom.id || !currentRoom.name) {
      logger.warn('GameTerminalWithPanels', '🔍 VALIDATION DEBUG: Invalid room data structure', {
        currentRoomId: currentRoom.id,
        currentRoomName: currentRoom.name,
      });
      return {
        isValid: false,
        reason: 'Invalid room data structure',
      };
    }

    logger.info('GameTerminalWithPanels', '🔍 VALIDATION DEBUG: Room data is valid', {
      currentRoomId: currentRoom.id,
      currentRoomName: currentRoom.name,
      eventTimestamp: event.timestamp,
    });

    return {
      isValid: true,
      reason: 'Room data is valid',
    };
  }, []);

  // Event processing function with debouncing and deduplication
  const processEventQueue = useCallback(() => {
    if (isProcessingEvent.current || eventQueue.current.length === 0) {
      return;
    }

    isProcessingEvent.current = true;

    try {
      const events = [...eventQueue.current];
      eventQueue.current = [];

      // Process events in batch to prevent cascading updates
      const updates: Partial<GameState> = {};

      events.forEach(event => {
        // Special handling for command_response events - don't deduplicate them
        if (event.event_type === 'command_response') {
          // For command responses, use timestamp to ensure uniqueness
          const eventKey = `${event.event_type}_${Date.now()}_${Math.random()}`;
          lastProcessedEvent.current = eventKey;
        } else {
          const eventKey = `${event.event_type}_${event.sequence_number}`;
          if (eventKey === lastProcessedEvent.current) {
            return; // Skip duplicate events
          }
          lastProcessedEvent.current = eventKey;
        }

        // Normalize event type for robust matching
        const eventType = (event.event_type || '').toString().trim().toLowerCase();

        logger.info('GameTerminalWithPanels', 'Processing event', {
          originalEventType: event.event_type,
          normalizedEventType: eventType,
          eventTypeLength: eventType.length,
          eventTypeCharCodes: Array.from(eventType).map(c => c.charCodeAt(0)),
          dataKeys: event.data ? Object.keys(event.data) : [],
          hasOccupants: !!(event.data && event.data.occupants),
          occupants: event.data?.occupants,
        });

        console.log('🔍 DEBUG: Processing event type:', eventType, event);

        const appendMessage = (message: ChatMessage) => {
          if (!updates.messages) {
            updates.messages = [...currentMessagesRef.current];
          }
          updates.messages.push(message);
        };

        const applySanityToPlayer = (sanityValue: number) => {
          const basePlayer = updates.player ?? currentPlayerRef.current;
          if (basePlayer) {
            updates.player = {
              ...basePlayer,
              stats: {
                ...basePlayer.stats,
                sanity: sanityValue,
              },
            };
          }
        };

        switch (eventType) {
          case 'game_state': {
            const playerData = event.data.player as Player;
            const roomData = event.data.room as Room;
            const occupants = event.data.occupants as string[] | undefined;
            if (playerData && roomData) {
              // Track the timestamp of this room update
              lastRoomUpdateTime.current = new Date(event.timestamp).getTime();
              updates.player = playerData;

              // Include occupants data in room data if provided
              const roomWithOccupants = {
                ...roomData,
                ...(occupants && { occupants, occupant_count: occupants.length }),
              };
              updates.room = roomWithOccupants;

              logger.info('GameTerminalWithPanels', 'Received game state', {
                playerName: playerData.name,
                roomName: roomData.name,
                roomId: roomData.id,
                hasProfessionName: !!playerData.profession_name,
                professionName: playerData.profession_name,
                hasProfessionId: !!playerData.profession_id,
                professionId: playerData.profession_id,
                playerDataKeys: Object.keys(playerData),
                occupants: occupants,
                occupantCount: occupants?.length,
                roomDataHasOccupants: !!roomData.occupants,
                roomDataOccupants: roomData.occupants,
                roomDataOccupantCount: roomData.occupant_count,
                finalRoomWithOccupants: roomWithOccupants,
              });
            }
            break;
          }
          case 'welcome': {
            const playerData = event.data.player as Player;
            const roomData = event.data.room as Room;
            const occupants = event.data.occupants as string[] | undefined;
            if (playerData && roomData) {
              // Track the timestamp of this room update
              lastRoomUpdateTime.current = new Date(event.timestamp).getTime();
              updates.player = playerData;

              // Include occupants data in room data if provided
              const roomWithOccupants = {
                ...roomData,
                ...(occupants && { occupants, occupant_count: occupants.length }),
              };
              updates.room = roomWithOccupants;
            }
            break;
          }
          case 'room_update': {
            const roomData = event.data.room as Room;
            const occupants = event.data.occupants as string[];
            const occupantCount = event.data.occupant_count as number;

            if (roomData) {
              // Track the timestamp of this room update
              lastRoomUpdateTime.current = new Date(event.timestamp).getTime();

              // Merge room data with occupants information from the event
              updates.room = {
                ...roomData,
                occupants: occupants || roomData.occupants,
                occupant_count: occupantCount !== undefined ? occupantCount : roomData.occupant_count,
              };
            }
            break;
          }
          case 'room_state': {
            const roomData = event.data.room_data as Room;
            if (roomData) {
              // Track the timestamp of this room update
              lastRoomUpdateTime.current = new Date(event.timestamp).getTime();
              updates.room = roomData;
            }
            break;
          }
          case 'sanity_change':
          case 'sanitychange': {
            const { status: updatedStatus, delta } = buildSanityStatus(
              sanityStatusRef.current,
              event.data,
              event.timestamp
            );

            setSanityStatus(updatedStatus);
            applySanityToPlayer(updatedStatus.current);

            const messageText = buildSanityChangeMessage(updatedStatus, delta, event.data);
            appendMessage(
              sanitizeChatMessageForState({
                text: `[Sanity] ${messageText}`,
                timestamp: event.timestamp,
                messageType: 'system',
                channel: 'system',
                isHtml: false,
                tags: ['sanity'],
              })
            );
            break;
          }
          case 'player_entered': {
            const playerName = event.data.player_name as string;
            const message = event.data.message as string;
            if (playerName && message) {
              logger.info('GameTerminalWithPanels', 'Player entered room', {
                playerName,
                message,
              });

              if (!updates.messages) {
                updates.messages = [...currentMessagesRef.current];
              }

              const chatMessage = {
                text: message,
                timestamp: event.timestamp,
                isHtml: false,
                messageType: 'system' as const,
                type: 'system' as const,
                channel: 'system' as const,
              };

              updates.messages.push(chatMessage);
            }
            break;
          }
          case 'player_left': {
            const playerName = event.data.player_name as string;
            const message = event.data.message as string;
            if (playerName && message) {
              logger.info('GameTerminalWithPanels', 'Player left room', {
                playerName,
                message,
              });

              if (!updates.messages) {
                updates.messages = [...currentMessagesRef.current];
              }

              const chatMessage = {
                text: message,
                timestamp: event.timestamp,
                isHtml: false,
                messageType: 'system' as const,
                type: 'system' as const,
                channel: 'system' as const,
              };

              updates.messages.push(chatMessage);
            }
            break;
          }
          case 'hallucination': {
            const hallucination = createHallucinationEntry(event.data, event.timestamp);
            setHallucinationFeed(prev => {
              const filtered = prev.filter(entry => entry.id !== hallucination.id);
              return [hallucination, ...filtered].slice(0, 5);
            });

            const hallucinationText = hallucination.description
              ? `${hallucination.title}: ${hallucination.description}`
              : hallucination.title;

            appendMessage(
              sanitizeChatMessageForState({
                text: `[Hallucination] ${hallucinationText}`,
                timestamp: event.timestamp,
                messageType: 'system',
                channel: 'system',
                isHtml: false,
                tags: ['hallucination'],
              })
            );
            break;
          }
          case 'command_misfire':
          case 'commandmisfire': {
            const originalCommand =
              typeof event.data?.original_command === 'string'
                ? (event.data.original_command as string)
                : typeof event.data?.command === 'string'
                  ? (event.data.command as string)
                  : undefined;
            const misfireMessage =
              typeof event.data?.message === 'string'
                ? (event.data.message as string)
                : 'The ritual backfires and the words twist into static.';

            const text = originalCommand
              ? `[Command Misfire] ${misfireMessage} (attempted: ${originalCommand})`
              : `[Command Misfire] ${misfireMessage}`;

            appendMessage(
              sanitizeChatMessageForState({
                text,
                timestamp: event.timestamp,
                messageType: 'system',
                channel: 'system',
                isHtml: false,
                tags: ['command-misfire'],
              })
            );
            break;
          }
          case 'command_response': {
            if (import.meta.env.MODE === 'development') {
              console.debug('command_response case MATCHED!', {
                eventType,
                eventData: event.data,
                eventDataKeys: Object.keys(event.data || {}),
                eventDataValues: Object.values(event.data || {}),
                hasResult: !!event.data?.result,
                resultLength: (event.data?.result as string)?.length || 0,
                resultValue: event.data?.result,
                timestamp: new Date().toISOString(),
              });
            }

            const suppressChat = Boolean(event.data?.suppress_chat);
            const message = typeof event.data?.result === 'string' ? (event.data.result as string) : '';
            const isHtml = Boolean(event.data?.is_html);
            const playerUpdate = event.data?.player_update as
              | { position?: string; previous_position?: string }
              | undefined;
            const explicitPosition =
              typeof event.data?.position === 'string' ? (event.data.position as string) : undefined;
            const newPosition = playerUpdate?.position || explicitPosition;
            const gameLogChannel =
              typeof event.data?.game_log_channel === 'string' && event.data.game_log_channel
                ? (event.data.game_log_channel as string)
                : GAME_LOG_CHANNEL;
            const gameLogMessage =
              (typeof event.data?.game_log_message === 'string' && event.data.game_log_message.length > 0
                ? (event.data.game_log_message as string)
                : undefined) || message;

            logger.info('GameTerminalWithPanels', 'Processing command response', {
              hasMessage: !!message,
              messageLength: message?.length || 0,
              isHtml,
              suppressChat,
              currentMessageCount: currentMessagesRef.current.length,
              hasPlayerUpdate: !!playerUpdate,
            });

            if (newPosition) {
              const currentPlayer = currentPlayerRef.current;
              const basePlayer = updates.player ?? (currentPlayer ? { ...currentPlayer } : undefined);
              const statsSource = basePlayer?.stats ?? currentPlayer?.stats;
              if (basePlayer || currentPlayer) {
                updates.player = {
                  ...(basePlayer ?? currentPlayer ?? {}),
                  position: newPosition,
                  stats: {
                    ...(statsSource ?? {}),
                    position: newPosition,
                  },
                } as Player;
              }
            }

            if (message) {
              if (message.includes('Name:') && message.includes('Health:') && message.includes('Sanity:')) {
                try {
                  const parsedPlayerData = parseStatusResponse(message);
                  const playerData = convertToPlayerInterface(parsedPlayerData);

                  logger.info('GameTerminalWithPanels', 'Parsed status response and updating player data', {
                    playerName: playerData.name,
                    hasProfession: !!playerData.profession_name,
                    professionName: playerData.profession_name,
                    hasStats: !!playerData.stats,
                  });

                  updates.player = playerData;
                } catch (error) {
                  logger.error('GameTerminalWithPanels', 'Failed to parse status response', {
                    error: error instanceof Error ? error.message : String(error),
                    message: message.substring(0, 200) + '...',
                  });
                }
              }
            }

            const shouldEmitChat = !suppressChat && message;
            const messageForLog = gameLogMessage;

            if (shouldEmitChat) {
              const messageTypeResult = determineMessageType(message);
              const chatMessage = {
                text: message,
                timestamp: event.timestamp,
                isHtml,
                messageType: messageTypeResult.type,
                channel: messageTypeResult.channel ?? 'game',
                type:
                  messageTypeResult.type === 'system'
                    ? 'system'
                    : resolveChatTypeFromChannel(messageTypeResult.channel ?? 'game'),
              };

              if (!updates.messages) {
                updates.messages = [...currentMessagesRef.current];
              }

              updates.messages.push(chatMessage);
            } else if (messageForLog) {
              if (!updates.messages) {
                updates.messages = [...currentMessagesRef.current];
              }

              updates.messages.push({
                text: messageForLog,
                timestamp: event.timestamp,
                isHtml,
                messageType: 'system',
                channel: gameLogChannel,
                type: 'system',
              });
            }
            break;
          }
          case 'player_posture_change': {
            const roomMessage = typeof event.data?.message === 'string' ? event.data.message : '';
            if (!roomMessage) {
              break;
            }

            if (!updates.messages) {
              updates.messages = [...currentMessagesRef.current];
            }

            updates.messages.push({
              text: roomMessage,
              timestamp: event.timestamp,
              isHtml: false,
              messageType: 'system',
              channel: GAME_LOG_CHANNEL,
              type: 'system',
            });
            break;
          }
          case 'system': {
            const rawMessage = typeof event.data?.message === 'string' ? event.data.message : '';
            const message = rawMessage.trim();

            if (!message) {
              logger.warn('GameTerminalWithPanels', 'System event missing message payload', {
                event_data_keys: event.data ? Object.keys(event.data) : [],
                sequence_number: event.sequence_number,
              });
              break;
            }

            const systemMessage = {
              text: message,
              timestamp: event.timestamp,
              isHtml: Boolean(event.data?.is_html),
              messageType: 'system' as const,
              type: 'system' as const,
              channel: 'system' as const,
            };

            if (!updates.messages) {
              updates.messages = [...currentMessagesRef.current];
            }
            updates.messages.push(systemMessage);
            break;
          }
          case 'player_entered_room':
          case 'player_left_room': {
            const rawMessage = typeof event.data?.message === 'string' ? event.data.message : '';
            const message = rawMessage.trim();

            if (!message) {
              logger.debug('GameTerminalWithPanels', 'Room transition event missing message content', {
                eventType,
                sequenceNumber: event.sequence_number,
                dataKeys: event.data ? Object.keys(event.data) : [],
              });
              break;
            }

            const systemMessage = {
              text: message,
              timestamp: event.timestamp,
              isHtml: false,
              messageType: 'system' as const,
              type: 'system' as const,
              channel: 'system' as const,
            };

            if (!updates.messages) {
              updates.messages = [...currentMessagesRef.current];
            }
            updates.messages.push(systemMessage);
            break;
          }
          case 'player_entered_game': {
            const playerName = event.data.player_name as string;
            if (playerName) {
              const message = {
                text: `${playerName} has entered the game.`,
                timestamp: event.timestamp,
                isHtml: false,
                messageType: 'system',
              };
              logger.info('GameTerminalWithPanels', 'Processing player entered game', {
                playerName,
                messageType: 'system',
                timestamp: event.timestamp,
              });
              if (!updates.messages) {
                updates.messages = [...currentMessagesRef.current];
              }
              updates.messages.push(message);
            }
            break;
          }
          case 'player_left_game': {
            const playerName = event.data.player_name as string;
            if (playerName) {
              const message = {
                text: `${playerName} has left the game.`,
                timestamp: event.timestamp,
                isHtml: false,
                messageType: 'system',
                type: 'system' as const,
                channel: 'system' as const,
              };
              logger.info('GameTerminalWithPanels', 'Processing player left game', {
                playerName,
                messageType: 'system',
                timestamp: event.timestamp,
              });
              if (!updates.messages) {
                updates.messages = [...currentMessagesRef.current];
              }
              updates.messages.push(message);
            }
            break;
          }
          case 'chat_message': {
            const message = event.data.message as string;
            const channel = event.data.channel as string;
            const playerName = event.data.player_name as string;
            const targetName = event.data.target_name as string;

            if (message) {
              logger.info('GameTerminalWithPanels', 'Processing chat message', {
                message: message.substring(0, 100) + (message.length > 100 ? '...' : ''),
                channel,
                playerName,
                targetName,
                timestamp: event.timestamp,
              });

              if (!updates.messages) {
                updates.messages = [...currentMessagesRef.current];
              }

              // Determine message type based on channel
              let messageType: string;
              switch (channel) {
                case 'whisper':
                  messageType = 'whisper';
                  break;
                case 'shout':
                  messageType = 'shout';
                  break;
                case 'emote':
                  messageType = 'emote';
                  break;
                case 'say':
                case 'local':
                default:
                  messageType = 'chat';
                  break;
              }

              const chatMessage = {
                text: message,
                timestamp: event.timestamp,
                isHtml: false,
                messageType: messageType,
                channel: channel,
                type: resolveChatTypeFromChannel(channel),
              };

              updates.messages.push(chatMessage);

              logger.info('GameTerminalWithPanels', 'Added chat message to updates', {
                messageType,
                channel,
                totalMessages: updates.messages.length,
              });
            }
            break;
          }
          case 'room_occupants': {
            const occupants = event.data.occupants as string[];
            const occupantCount = event.data.count as number;

            // Validate event data
            if (occupants && Array.isArray(occupants) && typeof occupantCount === 'number') {
              logger.info('GameTerminalWithPanels', 'Processing room_occupants event', {
                occupantsCount: occupants.length,
                occupantCount,
                occupants: occupants,
              });

              // Always validate the room data to prevent stale overwrites
              const currentRoom = currentRoomRef.current;
              if (currentRoom) {
                const roomDataValidation = validateRoomDataForOccupants(currentRoom, event);
                if (roomDataValidation.isValid) {
                  // Update room state with new occupant information
                  if (updates.room) {
                    // Room data already updated by room_update event - preserve it and just update occupants
                    updates.room = {
                      ...updates.room,
                      occupants: occupants,
                      occupant_count: occupantCount,
                    };
                  } else {
                    // Use current room data and update occupants
                    updates.room = {
                      ...currentRoom,
                      occupants: occupants,
                      occupant_count: occupantCount,
                    };
                  }
                } else {
                  logger.warn('GameTerminalWithPanels', 'Skipping room_occupants event due to stale room data', {
                    currentRoomId: currentRoom.id,
                    currentRoomName: currentRoom.name,
                    eventTimestamp: event.timestamp,
                    validationResult: roomDataValidation,
                  });
                  // Don't update room data at all - just skip this event
                  // Continue to next event without updating room data
                }
              }
            } else {
              logger.warn('GameTerminalWithPanels', 'Invalid room_occupants event data', {
                occupants: occupants,
                occupantCount: occupantCount,
                occupantsType: typeof occupants,
                countType: typeof occupantCount,
              });
            }
            break;
          }
          case 'heartbeat': {
            // Heartbeat events are used for connection health monitoring
            // No action needed, just acknowledge receipt
            logger.debug('GameTerminalWithPanels', 'Received heartbeat event');
            break;
          }
          case 'pong': {
            // Pong events are responses to ping messages
            // No action needed, just acknowledge receipt
            logger.debug('GameTerminalWithPanels', 'Received pong event');
            break;
          }
          case 'shutdown_notification': {
            const message = event.data.message as string;
            const secondsRemaining = event.data.seconds_remaining as number;
            const channel = event.data.channel as string;

            if (message) {
              logger.info('GameTerminalWithPanels', 'Processing shutdown notification', {
                message: message.substring(0, 100) + (message.length > 100 ? '...' : ''),
                secondsRemaining,
                channel,
                timestamp: event.timestamp,
              });

              if (!updates.messages) {
                updates.messages = [...currentMessagesRef.current];
              }

              const chatMessage = {
                text: message,
                timestamp: event.timestamp,
                isHtml: false,
                messageType: 'system' as const,
                type: 'system' as const,
                channel: channel || 'system',
              };

              updates.messages.push(chatMessage);

              logger.info('GameTerminalWithPanels', 'Added shutdown notification to updates', {
                messageType: 'system',
                channel: channel || 'system',
                totalMessages: updates.messages.length,
              });
            }
            break;
          }
          case 'shutdown_cancelled': {
            const message = event.data.message as string;
            const channel = event.data.channel as string;

            if (message) {
              logger.info('GameTerminalWithPanels', 'Processing shutdown cancellation', {
                message: message.substring(0, 100) + (message.length > 100 ? '...' : ''),
                channel,
                timestamp: event.timestamp,
              });

              if (!updates.messages) {
                updates.messages = [...currentMessagesRef.current];
              }

              const chatMessage = {
                text: message,
                timestamp: event.timestamp,
                isHtml: false,
                messageType: 'system' as const,
                type: 'system' as const,
                channel: channel || 'system',
              };

              updates.messages.push(chatMessage);

              logger.info('GameTerminalWithPanels', 'Added shutdown cancellation to updates', {
                messageType: 'system',
                channel: channel || 'system',
                totalMessages: updates.messages.length,
              });
            }
            break;
          }
          case 'game_tick': {
            const tickNumber = event.data.tick_number as number;
            const showTickVerbosity = localStorage.getItem('showTickVerbosity') === 'true';

            console.log('🔍 DEBUG: game_tick event received!', {
              tickNumber,
              showTickVerbosity,
              isEvery10th: tickNumber % 10 === 0,
            });

            // Debug logging for game tick events
            logger.debug('GameTerminalWithPanels', 'Received game_tick event', {
              tickNumber,
              showTickVerbosity,
              isEvery10th: tickNumber % 10 === 0,
            });

            // Display every 10th tick by default (or if verbosity is enabled)
            if ((showTickVerbosity || localStorage.getItem('showTickVerbosity') === null) && tickNumber % 10 === 0) {
              const message = {
                text: `[Game Tick ${tickNumber}]`,
                timestamp: event.timestamp,
                isHtml: false,
                messageType: 'system',
                type: 'system' as const,
                channel: 'system' as const,
              };

              if (!updates.messages) {
                updates.messages = [...currentMessagesRef.current];
              }
              updates.messages.push(message);

              logger.info('GameTerminalWithPanels', 'Game tick displayed', {
                tickNumber,
                showTickVerbosity,
              });
            }
            break;
          }
          case 'npc_action': {
            const npcName = event.data.npc_name as string;
            const action = event.data.action as string;
            const message = event.data.message as string;

            const messageObj = {
              text: message,
              timestamp: event.timestamp,
              isHtml: false,
              messageType: 'system' as const,
              type: 'system' as const,
              channel: 'system' as const,
            };

            if (!updates.messages) {
              updates.messages = [...currentMessagesRef.current];
            }
            updates.messages.push(messageObj);

            logger.info('GameTerminalWithPanels', 'NPC action received', {
              npcName,
              action,
              message,
            });
            break;
          }
          case 'player_attacked': {
            console.log('🔍 DEBUG: player_attacked event received!', event);
            const attackerName = event.data.attacker_name as string;
            const targetName = event.data.target_name as string;
            const damage = event.data.damage as number;
            const actionType = event.data.action_type as string;
            const targetCurrentHp = event.data.target_current_hp as number;
            const targetMaxHp = event.data.target_max_hp as number;

            // Check if this is the current player's attack
            const isCurrentPlayer = currentPlayerRef.current && currentPlayerRef.current.name === attackerName;

            let message: string;
            if (isCurrentPlayer) {
              // Format message for current player's attack with target health
              message = `You hit ${targetName} for ${damage} damage! (${targetCurrentHp}/${targetMaxHp} HP)`;
            } else {
              // Format message for other players' attacks with target health
              message =
                `${attackerName} attacks ${targetName} for ${damage} damage! ` +
                `(${targetCurrentHp}/${targetMaxHp} HP)`;
            }

            const messageObj = {
              text: message,
              timestamp: event.timestamp,
              isHtml: false,
              messageType: 'combat' as const,
              channel: 'combat' as const,
            };

            if (!updates.messages) {
              updates.messages = [...currentMessagesRef.current];
            }
            updates.messages.push(messageObj);

            logger.info('GameTerminalWithPanels', 'Player attacked event received', {
              attackerName,
              targetName,
              damage,
              actionType,
              isCurrentPlayer,
            });
            break;
          }
          case 'npc_attacked': {
            console.log('🔍 DEBUG: npc_attacked event received!', event);
            const attackerName = event.data.attacker_name as string;
            const npcName = event.data.npc_name as string;
            const damage = event.data.damage as number;
            const actionType = event.data.action_type as string;
            const targetCurrentHp = event.data.target_current_hp as number;
            const targetMaxHp = event.data.target_max_hp as number;

            console.log('🔍 DEBUG: npc_attacked data:', {
              attackerName,
              npcName,
              damage,
              targetCurrentHp,
              targetMaxHp,
            });

            // For npc_attacked events, attacker_name is the NPC and npc_name is the target player
            const playerName = normalizeName(currentPlayerRef.current?.name);
            const targetNameNormalized = normalizeName(npcName);
            const isTargeted = !!playerName && targetNameNormalized === playerName;

            const message = isTargeted
              ? `${attackerName} attacks you for ${damage} damage! (${targetCurrentHp}/${targetMaxHp} HP)`
              : `${attackerName} attacks ${npcName || 'their target'} for ${damage} damage! (${targetCurrentHp}/${targetMaxHp} HP)`;

            // Check for duplicate npc_attacked events
            // Look for any message that contains the same attack message
            const allMessages = [...currentMessagesRef.current, ...(updates.messages || [])];
            const existingMessage = allMessages.find(msg => msg.text === message);

            if (existingMessage) {
              console.log('🔍 DEBUG: Duplicate npc_attacked event detected, skipping', { message });
              break;
            }

            const messageObj = {
              text: message,
              timestamp: event.timestamp,
              isHtml: false,
              messageType: 'combat' as const,
              type: 'combat' as const,
              channel: 'game' as const,
            };

            if (!updates.messages) {
              updates.messages = [...currentMessagesRef.current];
            }
            updates.messages.push(messageObj);

            // BUGFIX: Update player health in Status panel when taking damage
            if (isTargeted && currentPlayerRef.current && currentPlayerRef.current.stats) {
              updates.player = {
                ...currentPlayerRef.current,
                stats: {
                  ...currentPlayerRef.current.stats,
                  current_health: targetCurrentHp,
                },
              };
              logger.info('GameTerminalWithPanels', 'Updated player health after taking damage', {
                oldHealth: currentPlayerRef.current.stats.current_health,
                newHealth: targetCurrentHp,
                damage,
              });
            }

            console.log('🔍 DEBUG: npc_attacked message added to updates:', messageObj);

            logger.info('GameTerminalWithPanels', 'NPC attacked event received', {
              attackerName,
              npcName,
              damage,
              actionType,
            });
            break;
          }
          case 'npc_took_damage': {
            const npcName = event.data.npc_name as string;
            const damage = event.data.damage as number;
            const currentHp = event.data.current_hp as number;
            const maxHp = event.data.max_hp as number;

            const message = `${npcName} takes ${damage} damage! (${currentHp}/${maxHp} HP)`;
            const messageObj = {
              text: message,
              timestamp: event.timestamp,
              isHtml: false,
              messageType: 'combat' as const,
              type: 'combat' as const,
              channel: 'game' as const,
            };

            if (!updates.messages) {
              updates.messages = [...currentMessagesRef.current];
            }
            updates.messages.push(messageObj);

            logger.info('GameTerminalWithPanels', 'NPC took damage event received', {
              npcName,
              damage,
              currentHp,
              maxHp,
            });
            break;
          }
          case 'player_xp_updated': {
            const xpAmount = event.data.xp_amount as number;
            const newLevel = event.data.new_level as number;
            const playerData = event.data.player as Player;

            // Update player data with new XP and level
            if (currentPlayerRef.current && playerData) {
              updates.player = {
                ...currentPlayerRef.current,
                xp: playerData.xp,
                level: playerData.level,
              };
            }

            // Add XP award message to game log
            const message = `You gained ${xpAmount} experience points!${newLevel > (currentPlayerRef.current?.level || 1) ? ` (Level up to ${newLevel}!)` : ''}`;
            const messageObj = {
              text: message,
              timestamp: event.timestamp,
              isHtml: false,
              messageType: 'combat' as const,
              type: 'combat' as const,
              channel: 'game' as const,
            };

            if (!updates.messages) {
              updates.messages = [...currentMessagesRef.current];
            }
            updates.messages.push(messageObj);

            logger.info('GameTerminalWithPanels', 'Player XP updated', {
              xpAmount,
              newLevel,
              playerData,
            });
            break;
          }
          case 'npc_died': {
            const npcName = event.data.npc_name as string;
            const xpReward = event.data.xp_reward as number;

            const message = `${npcName} has been defeated!${xpReward > 0 ? ` (+${xpReward} XP)` : ''}`;
            const messageObj = {
              text: message,
              timestamp: event.timestamp,
              isHtml: false,
              messageType: 'combat' as const,
              type: 'combat' as const,
              channel: 'game' as const,
            };

            if (!updates.messages) {
              updates.messages = [...currentMessagesRef.current];
            }
            updates.messages.push(messageObj);

            // Update player XP if reward was given and clear combat state
            if (currentPlayerRef.current && xpReward > 0) {
              updates.player = {
                ...currentPlayerRef.current,
                xp: (currentPlayerRef.current.xp || 0) + xpReward,
                in_combat: false,
              };
            } else if (currentPlayerRef.current) {
              // Clear combat state even if no XP reward
              updates.player = {
                ...currentPlayerRef.current,
                in_combat: false,
              };
            }

            // Remove NPC from room occupants
            if (currentRoomRef.current && currentRoomRef.current.occupants) {
              const originalOccupants = currentRoomRef.current.occupants;
              const filteredOccupants = originalOccupants.filter(occupant => occupant !== npcName);
              console.log('🔍 DEBUG: Removing NPC from room occupants', {
                npcName,
                originalOccupants: originalOccupants,
                filteredOccupants: filteredOccupants,
              });
              updates.room = {
                ...currentRoomRef.current,
                occupants: filteredOccupants,
              };
            }

            logger.info('GameTerminalWithPanels', 'NPC died event received', {
              npcName,
              xpReward,
            });
            break;
          }
          case 'combat_started': {
            console.log('🔍 DEBUG: combat_started event received!', event);
            const combatId = event.data.combat_id as string;
            const turnOrder = Array.isArray(event.data.turn_order) ? (event.data.turn_order as string[]) : [];
            const participants = event.data.participants as Record<string, CombatParticipant> | undefined;

            // Check if we've already processed this combat_started event
            // Look for any message that contains "Combat has begun!" and the same turn order
            // Check both current messages and pending updates
            const allMessages = [...currentMessagesRef.current, ...(updates.messages || [])];
            const existingMessage = allMessages.find(
              msg => msg.text.includes('Combat has begun!') && msg.text.includes(turnOrder.join(', '))
            );

            console.log('🔍 DEBUG: Checking for duplicate combat_started', {
              combatId,
              turnOrder,
              existingMessage: existingMessage ? existingMessage.text : null,
              currentMessagesCount: currentMessagesRef.current.length,
            });

            if (existingMessage) {
              console.log('🔍 DEBUG: Duplicate combat_started event detected, skipping', { combatId, turnOrder });
              break;
            }

            const message = `Combat has begun! Turn order: ${turnOrder.join(', ')}`;
            const messageObj = {
              text: message,
              timestamp: event.timestamp,
              isHtml: false,
              messageType: 'system' as const,
              channel: 'combat' as const,
            };

            if (!updates.messages) {
              updates.messages = [...currentMessagesRef.current];
            }
            updates.messages.push(messageObj);

            // Update player combat status only if they are part of this combat
            if (
              currentPlayerRef.current &&
              isPlayerCombatParticipant(currentPlayerRef.current, participants, turnOrder)
            ) {
              activeCombatIdRef.current = combatId;
              updates.player = {
                ...currentPlayerRef.current,
                in_combat: true,
              };
            }

            logger.info('GameTerminalWithPanels', 'Combat started event received', {
              combatId,
              turnOrder,
            });
            break;
          }
          case 'combat_ended': {
            const reason = event.data.reason as string;
            const durationSeconds = event.data.duration_seconds as number;
            const message = `Combat has ended. ${reason}${durationSeconds > 0 ? ` (Duration: ${durationSeconds}s)` : ''}`;

            // Check for duplicate combat_ended events
            const allMessages = [...currentMessagesRef.current, ...(updates.messages || [])];
            const existingMessage = allMessages.find(
              msg => msg.text.includes('Combat has ended.') && msg.text.includes(reason)
            );

            if (existingMessage) {
              console.log('🔍 DEBUG: Duplicate combat_ended event detected, skipping', { reason, durationSeconds });
              break;
            }

            const messageObj = {
              text: message,
              timestamp: event.timestamp,
              isHtml: false,
              messageType: 'system' as const,
              channel: 'combat' as const,
            };

            if (!updates.messages) {
              updates.messages = [...currentMessagesRef.current];
            }
            updates.messages.push(messageObj);

            // Update player combat status immediately when the player was involved
            const combatId = event.data.combat_id as string | undefined;
            const playerWasInCombat = currentPlayerRef.current?.in_combat;
            const shouldUpdate =
              currentPlayerRef.current && (combatId ? activeCombatIdRef.current === combatId : playerWasInCombat);

            if (shouldUpdate && currentPlayerRef.current) {
              activeCombatIdRef.current = combatId ? null : activeCombatIdRef.current;
              updates.player = {
                ...currentPlayerRef.current,
                in_combat: false,
              };
            }

            logger.info('GameTerminalWithPanels', 'Combat ended event received', {
              reason,
              durationSeconds,
            });
            break;
          }
          case 'player_mortally_wounded': {
            // Player has reached 0 HP - enter mortally wounded state
            const message = event.data.message as string;

            setIsMortallyWounded(true);

            const messageObj = {
              text: message,
              timestamp: event.timestamp,
              isHtml: false,
              messageType: 'combat' as const,
              channel: 'combat' as const,
            };

            if (!updates.messages) {
              updates.messages = [...currentMessagesRef.current];
            }
            updates.messages.push(messageObj);

            logger.info('GameTerminalWithPanels', 'Player mortally wounded', {
              message,
            });
            break;
          }
          case 'player_mortally_wounded_room': {
            // Other player became mortally wounded
            const message = event.data.message as string;

            const messageObj = {
              text: message,
              timestamp: event.timestamp,
              isHtml: false,
              messageType: 'combat' as const,
              channel: 'combat' as const,
            };

            if (!updates.messages) {
              updates.messages = [...currentMessagesRef.current];
            }
            updates.messages.push(messageObj);
            break;
          }
          case 'player_hp_decay': {
            // HP decay tick for mortally wounded player
            const message = event.data.message as string;
            const currentHp = event.data.current_hp as number;

            const messageObj = {
              text: message,
              timestamp: event.timestamp,
              isHtml: false,
              messageType: 'system' as const,
              channel: 'system' as const,
            };

            if (!updates.messages) {
              updates.messages = [...currentMessagesRef.current];
            }
            updates.messages.push(messageObj);

            // Update player HP in state
            if (currentPlayerRef.current && currentPlayerRef.current.stats) {
              updates.player = {
                ...currentPlayerRef.current,
                stats: {
                  ...currentPlayerRef.current.stats,
                  current_health: currentHp,
                },
              };
            }
            break;
          }
          case 'player_died': {
            // Player has died (reached -10 HP)
            const message = event.data.message as string;
            const eventDeathLocation = event.data.death_location as string;

            setIsDead(true);
            setIsMortallyWounded(false);
            setDeathLocation(eventDeathLocation || currentRoomRef.current?.name || 'Unknown Location');

            const messageObj = {
              text: message,
              timestamp: event.timestamp,
              isHtml: false,
              messageType: 'death' as const,
              channel: 'system' as const,
            };

            if (!updates.messages) {
              updates.messages = [...currentMessagesRef.current];
            }
            updates.messages.push(messageObj);

            logger.info('GameTerminalWithPanels', 'Player died', {
              message,
              deathLocation: eventDeathLocation,
            });
            break;
          }
          case 'player_died_room': {
            // Other player died
            const message = event.data.message as string;

            const messageObj = {
              text: message,
              timestamp: event.timestamp,
              isHtml: false,
              messageType: 'system' as const,
              channel: 'system' as const,
            };

            if (!updates.messages) {
              updates.messages = [...currentMessagesRef.current];
            }
            updates.messages.push(messageObj);
            break;
          }
          case 'player_respawned': {
            // Player has respawned
            const message = event.data.message as string;

            setIsDead(false);
            setIsMortallyWounded(false);

            const messageObj = {
              text: message,
              timestamp: event.timestamp,
              isHtml: false,
              messageType: 'system' as const,
              channel: 'system' as const,
            };

            if (!updates.messages) {
              updates.messages = [...currentMessagesRef.current];
            }
            updates.messages.push(messageObj);

            logger.info('GameTerminalWithPanels', 'Player respawned');
            break;
          }
          case 'player_respawned_room': {
            // Other player respawned
            const message = event.data.message as string;

            const messageObj = {
              text: message,
              timestamp: event.timestamp,
              isHtml: false,
              messageType: 'system' as const,
              channel: 'system' as const,
            };

            if (!updates.messages) {
              updates.messages = [...currentMessagesRef.current];
            }
            updates.messages.push(messageObj);
            break;
          }
          case 'catatonia': {
            const incomingState = createRescueState(event.data, event.timestamp);
            const finalState =
              incomingState.status === 'idle' ? { ...incomingState, status: 'catatonic' as const } : incomingState;

            setRescueState(finalState);

            const messageText =
              finalState.message ??
              (finalState.status === 'catatonic'
                ? 'Your mind collapses into static. Companions may attempt the grounding ritual.'
                : `Catatonia status: ${finalState.status}`);

            if (typeof event.data?.current_san === 'number') {
              applySanityToPlayer(event.data.current_san as number);
            }

            appendMessage(
              sanitizeChatMessageForState({
                text: `[Catatonia] ${messageText}`,
                timestamp: event.timestamp,
                messageType: 'system',
                channel: 'system',
                isHtml: false,
                tags: ['rescue'],
              })
            );

            break;
          }
          case 'rescue_update':
          case 'rescueupdate': {
            const nextState = createRescueState(event.data, event.timestamp);
            setRescueState(nextState);

            let messageText = nextState.message;
            if (!messageText) {
              switch (nextState.status) {
                case 'channeling':
                  messageText = `Rescue ritual ${
                    typeof nextState.progress === 'number' ? `${Math.round(nextState.progress)}%` : 'underway'
                  }${nextState.rescuerName ? ` by ${nextState.rescuerName}` : ''}.`;
                  break;
                case 'success':
                  messageText = 'Rescue ritual succeeds. Consciousness stabilizes.';
                  break;
                case 'failed':
                  messageText = 'Rescue ritual falters. The void resists grounding.';
                  break;
                case 'sanitarium':
                  messageText = 'Caretakers escort the target to Arkham Sanitarium for observation.';
                  break;
                default:
                  messageText = undefined;
              }
            }

            if (typeof event.data?.current_san === 'number') {
              applySanityToPlayer(event.data.current_san as number);
            }

            if (messageText) {
              appendMessage(
                sanitizeChatMessageForState({
                  text: `[Rescue] ${messageText}`,
                  timestamp: event.timestamp,
                  messageType: 'system',
                  channel: 'system',
                  isHtml: false,
                  tags: ['rescue'],
                })
              );
            }

            break;
          }
          default: {
            logger.info('GameTerminalWithPanels', 'Unhandled event type', {
              event_type: event.event_type,
              data_keys: event.data ? Object.keys(event.data) : [],
              full_event: event,
            });
            break;
          }
        }
      });

      // Apply all updates in a single state update
      if (updates.messages) {
        updates.messages = updates.messages.map(sanitizeChatMessageForState);
      }

      if (Object.keys(updates).length > 0) {
        logger.info('GameTerminalWithPanels', 'Applying state updates', {
          updateKeys: Object.keys(updates),
          messageCount: updates.messages?.length || 0,
          currentMessageCount: currentMessagesRef.current.length,
          roomUpdate: updates.room,
          roomOccupants: updates.room?.occupants,
          roomOccupantCount: updates.room?.occupant_count,
          hasPlayerUpdate: !!updates.player,
          playerHealth: updates.player?.stats?.current_health,
        });

        setGameState(prev => {
          const newState = {
            ...prev,
            ...updates,
            messages: updates.messages || prev.messages,
            player: updates.player || prev.player,
          };

          logger.info('GameTerminalWithPanels', 'State updated', {
            newMessageCount: newState.messages.length,
            hasMessages: newState.messages.length > 0,
            playerHealth: newState.player?.stats?.current_health,
          });

          return newState;
        });
      }
    } catch (error) {
      logger.error('GameTerminalWithPanels', 'Error processing events', { error });
    } finally {
      isProcessingEvent.current = false;

      // Process any new events that arrived during processing
      if (eventQueue.current.length > 0) {
        processingTimeout.current = window.setTimeout(processEventQueue, 10);
      }
    }
  }, [validateRoomDataForOccupants]);

  // Memoize the game event handler to prevent infinite re-renders
  const handleGameEvent = useCallback(
    (event: GameEvent) => {
      logger.info('GameTerminalWithPanels', 'Received game event', { event_type: event.event_type });

      // Add event to queue for batched processing
      eventQueue.current.push(event);

      // Process queue if not already processing
      if (!isProcessingEvent.current && !processingTimeout.current) {
        processingTimeout.current = window.setTimeout(() => {
          processingTimeout.current = null;
          processEventQueue();
        }, 10);
      }
    },
    [processEventQueue]
  ); // Only depend on processEventQueue

  // Handle connection loss - trigger logout flow when all connections are lost
  const handleConnectionLoss = useCallback(() => {
    logger.info('GameTerminalWithPanels', 'Connection lost, triggering logout flow');
    console.log('GameTerminalWithPanels: handleConnectionLoss called, onLogout:', !!onLogout);

    // Add connection lost message
    const connectionLostMessage: ChatMessage = sanitizeChatMessageForState({
      text: 'Connection to server lost. Returning to login screen...',
      timestamp: new Date().toISOString(),
      messageType: 'system',
      isHtml: false,
    });

    // Add message to state and wait for it to render before logout
    setGameState(prev => ({
      ...prev,
      messages: [...prev.messages, connectionLostMessage],
    }));

    // Wait for message to render before triggering logout
    setTimeout(() => {
      console.log('GameTerminalWithPanels: About to call onLogout, onLogout:', !!onLogout);
      if (onLogout) {
        console.log('GameTerminalWithPanels: Calling onLogout');
        onLogout();
      } else {
        console.log('GameTerminalWithPanels: onLogout is not available');
      }
    }, 1000); // 1 second to show the message
  }, [onLogout]);

  // Memoize the connect handler
  const handleConnect = useCallback(() => {
    logger.info('GameTerminalWithPanels', 'Connected to game server');
    // Don't clear messages on connection - this was preventing message display
    // setGameState(prev => ({ ...prev, messages: [] }));
  }, []); // Empty dependency array - this function should never change

  // Memoize the disconnect handler
  const handleDisconnect = useCallback(() => {
    logger.info('GameTerminalWithPanels', 'Disconnected from game server');
    // Trigger the connection loss handler
    handleConnectionLoss();
  }, [handleConnectionLoss]); // Include handleConnectionLoss in dependencies

  // Memoize the error handler
  const handleError = useCallback((error: string) => {
    logger.error('GameTerminalWithPanels', 'Game connection error', { error });
  }, []); // Empty dependency array - this function should never change

  // Use the game connection hook for real server communication
  const { isConnected, isConnecting, error, reconnectAttempts, connect, disconnect, sendCommand } = useGameConnection({
    authToken,
    onEvent: handleGameEvent,
    onConnect: handleConnect,
    onDisconnect: handleDisconnect,
    onError: handleError,
  });

  // Store sendCommand in ref for use in event handlers
  useEffect(() => {
    sendCommandRef.current = sendCommand;
  }, [sendCommand]);

  // Note: Connection loss handling is now done through the handleDisconnect callback
  // which is passed to the useGameConnection hook

  // Connect once on mount; disconnect on unmount.
  // Important: Avoid including changing dependencies (like connect/disconnect identity or state)
  // which would trigger cleanup on every render and cause immediate disconnects.
  useEffect(() => {
    if (!hasAttemptedConnection.current) {
      hasAttemptedConnection.current = true;
      logger.info('GameTerminalWithPanels', 'Initiating connection', {
        hasAuthToken: !!authToken,
        playerName,
      });

      connect();
    }

    return () => {
      logger.info('GameTerminalWithPanels', 'Cleaning up connection on unmount');
      disconnect();
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  const handleCommandSubmit = async (command: string) => {
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

    // Expand shorthand for movement and look
    const parts = normalized.split(/\s+/);
    if (parts.length === 1 && dirMap[lower]) {
      normalized = `go ${dirMap[lower]}`;
    } else if (parts.length === 2) {
      const [verb, arg] = [parts[0].toLowerCase(), parts[1].toLowerCase()];
      if ((verb === 'go' || verb === 'look') && dirMap[arg]) {
        normalized = `${verb} ${dirMap[arg]}`;
      }
    }

    // Add to command history
    setGameState(prev => ({ ...prev, commandHistory: [...prev.commandHistory, normalized] }));

    // Parse command for sending to server
    const commandParts = normalized.split(/\s+/);
    const commandName = commandParts[0];
    const commandArgs = commandParts.slice(1);

    // Send command to server
    const success = await sendCommand(commandName, commandArgs);
    if (!success) {
      logger.error('GameTerminalWithPanels', 'Failed to send command', { command: commandName, args: commandArgs });
    }
  };

  const handleChatMessage = async (message: string, channel: string) => {
    if (!message.trim() || !isConnected) return;

    // Sanitize chat message and channel
    const sanitizedMessage = inputSanitizer.sanitizeChatMessage(message);
    const sanitizedChannel = inputSanitizer.sanitizeCommand(channel);

    if (!sanitizedMessage.trim()) {
      logger.warn('GameTerminalWithPanels', 'Chat message was empty after sanitization');
      return;
    }

    // DON'T add chat messages to command history - they should only appear in ChatPanel
    // setGameState(prev => ({ ...prev, commandHistory: [...prev.commandHistory, message] }));

    // Send chat message to server
    const success = await sendCommand('chat', [sanitizedChannel, sanitizedMessage]);
    if (!success) {
      logger.error('GameTerminalWithPanels', 'Failed to send chat message', {
        channel: sanitizedChannel,
        message: sanitizedMessage,
      });
    }
  };

  const handleClearMessages = () => {
    setGameState(prev => ({ ...prev, messages: [] }));
  };

  const handleClearHistory = () => {
    setGameState(prev => ({ ...prev, commandHistory: [] }));
  };

  const handleRespawn = async () => {
    logger.info('GameTerminalWithPanels', 'Respawn requested');
    setIsRespawning(true);

    try {
      // Call the respawn API endpoint
      const response = await fetch('/api/players/respawn', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${authToken}`,
        },
      });

      if (!response.ok) {
        const errorData = await response.json();
        logger.error('GameTerminalWithPanels', 'Respawn failed', {
          status: response.status,
          error: errorData,
        });

        // Add error message
        const errorMessage: ChatMessage = sanitizeChatMessageForState({
          text: `Respawn failed: ${errorData.detail || 'Unknown error'}`,
          timestamp: new Date().toISOString(),
          messageType: 'error',
          isHtml: false,
        });

        setGameState(prev => ({
          ...prev,
          messages: [...prev.messages, errorMessage],
        }));

        setIsRespawning(false);
        return;
      }

      const respawnData = await response.json();
      logger.info('GameTerminalWithPanels', 'Respawn successful', {
        room: respawnData.room,
        player: respawnData.player,
      });

      // Reset death states
      setIsDead(false);
      setIsMortallyWounded(false);
      setIsRespawning(false);

      // Update game state with new room and player data
      setGameState(prev => ({
        ...prev,
        player: {
          ...prev.player,
          ...respawnData.player,
          stats: {
            ...prev.player?.stats,
            current_health: respawnData.player.hp,
          },
        } as Player,
        room: respawnData.room as Room,
      }));

      // Add respawn message
      const respawnMessage: ChatMessage = sanitizeChatMessageForState({
        text: 'You feel a chilling wind as your form reconstitutes in Arkham General Hospital...',
        timestamp: new Date().toISOString(),
        messageType: 'system',
        isHtml: false,
      });

      setGameState(prev => ({
        ...prev,
        messages: [...prev.messages, respawnMessage],
      }));
    } catch (error) {
      logger.error('GameTerminalWithPanels', 'Error calling respawn API', { error });

      // Add error message
      const errorMessage: ChatMessage = sanitizeChatMessageForState({
        text: 'Failed to respawn due to network error. Please try again.',
        timestamp: new Date().toISOString(),
        messageType: 'error',
        isHtml: false,
      });

      setGameState(prev => ({
        ...prev,
        messages: [...prev.messages, errorMessage],
      }));

      setIsRespawning(false);
    }
  };

  const handleLogout = () => {
    // Add logout confirmation message before logout (only once)
    const logoutMessage: ChatMessage = sanitizeChatMessageForState({
      text: 'You have been logged out of the MythosMUD server.',
      timestamp: new Date().toISOString(),
      messageType: 'system', // System message appears in GameLogPanel
      isHtml: false,
    });

    // Add message to state and wait for it to render before logout
    setGameState(prev => ({
      ...prev,
      messages: [...prev.messages, logoutMessage],
    }));

    // Wait for message to render in GameLogPanel before triggering logout
    // This ensures the logout confirmation is visible to the user
    setTimeout(() => {
      if (onLogout) {
        onLogout();
      } else {
        // Fallback to just disconnect if no logout handler provided
        disconnect();
      }
    }, 500); // 500ms should be enough for React to render the message
  };

  const handleDismissHallucination = useCallback((id: string) => {
    setHallucinationFeed(prev => prev.filter(entry => entry.id !== id));
  }, []);

  const handleDismissRescue = useCallback(() => {
    setRescueState(null);
  }, []);

  return (
    <div className={`game-terminal-container ${isMortallyWounded ? 'mortally-wounded' : ''} ${isDead ? 'dead' : ''}`}>
      <GameTerminal
        playerName={playerName}
        isConnected={isConnected}
        isConnecting={isConnecting}
        error={error}
        reconnectAttempts={reconnectAttempts}
        room={gameState.room}
        player={gameState.player}
        messages={gameState.messages}
        commandHistory={gameState.commandHistory}
        sanityStatus={sanityStatus}
        hallucinations={hallucinationFeed}
        rescueState={rescueState}
        onDismissHallucination={handleDismissHallucination}
        onDismissRescue={handleDismissRescue}
        onConnect={connect}
        onDisconnect={disconnect}
        onLogout={handleLogout}
        isLoggingOut={isLoggingOut}
        onDownloadLogs={() => logger.downloadLogs()}
        onSendCommand={handleCommandSubmit}
        onSendChatMessage={handleChatMessage}
        onClearMessages={handleClearMessages}
        onClearHistory={handleClearHistory}
        isMortallyWounded={isMortallyWounded}
        isDead={isDead}
      />

      {/* Command Help Drawer */}
      <CommandHelpDrawer open={false} onClose={() => {}} />

      {/* Death Interstitial Screen */}
      <DeathInterstitial
        isVisible={isDead}
        deathLocation={deathLocation}
        onRespawn={handleRespawn}
        isRespawning={isRespawning}
      />
    </div>
  );
};
