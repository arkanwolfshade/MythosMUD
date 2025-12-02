import React, { useCallback, useEffect, useRef, useState } from 'react';
import { useGameConnection } from '../../hooks/useGameConnectionRefactored';
import { useContainerStore } from '../../stores/containerStore';
import type { HealthStatus } from '../../types/health';
import { determineHealthTier } from '../../types/health';
import type { MythosTimePayload, MythosTimeState } from '../../types/mythosTime';
import type { HallucinationMessage, RescueState, SanityStatus } from '../../types/sanity';
import { buildHealthStatusFromEvent } from '../../utils/healthEventUtils';
import { logger } from '../../utils/logger';
import { useMemoryMonitor } from '../../utils/memoryMonitor';
import { determineMessageType } from '../../utils/messageTypeUtils';
import { DAYPART_MESSAGES, buildMythosTimeState, formatMythosTime12Hour } from '../../utils/mythosTime';
import { buildSanityStatus } from '../../utils/sanityEventUtils';
import { inputSanitizer } from '../../utils/security';
import { convertToPlayerInterface, parseStatusResponse } from '../../utils/statusParser';
import { DeathInterstitial } from '../DeathInterstitial';
import { MainMenuModal } from '../MainMenuModal';
import { MapView } from '../MapView';
import { GameClientV2 } from './GameClientV2';
import type { ChatMessage, Player, Room } from './types';
import { useTabbedInterface } from './useTabbedInterface';

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

interface GameClientV2ContainerProps {
  playerName: string;
  authToken: string;
  onLogout?: () => void;
  isLoggingOut?: boolean;
  onDisconnect?: (disconnectFn: () => void) => void;
}

interface GameState {
  player: Player | null;
  room: Room | null;
  messages: ChatMessage[];
  commandHistory: string[];
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

// Container component that manages game state and renders GameClientV2
// Based on findings from "State Management Patterns" - Dr. Armitage, 1928
export const GameClientV2Container: React.FC<GameClientV2ContainerProps> = ({
  playerName,
  authToken,
  onLogout,
  isLoggingOut = false,
  onDisconnect: _onDisconnect,
}) => {
  const [isMainMenuOpen, setIsMainMenuOpen] = useState(false);
  const [showMap, setShowMap] = useState(false);

  // Tabbed interface for in-app tabs
  const { tabs, activeTabId, addTab, closeTab, setActiveTab } = useTabbedInterface([]);

  const [gameState, setGameState] = useState<GameState>({
    player: null,
    room: null,
    messages: [],
    commandHistory: [],
  });

  const [isMortallyWounded, setIsMortallyWounded] = useState(false);
  const [isDead, setIsDead] = useState(false);
  const [deathLocation] = useState<string>('Unknown Location');
  const [isRespawning, setIsRespawning] = useState(false);
  const [sanityStatus, setSanityStatus] = useState<SanityStatus | null>(null);
  const [healthStatus, setHealthStatus] = useState<HealthStatus | null>(null);
  const [, setHallucinationFeed] = useState<HallucinationMessage[]>([]);
  const [rescueState, setRescueState] = useState<RescueState | null>(null);
  const [mythosTime, setMythosTime] = useState<MythosTimeState | null>(null);

  // Memory monitoring
  const { detector } = useMemoryMonitor('GameClientV2Container');

  // Container store hooks - kept for future use
  // eslint-disable-next-line @typescript-eslint/no-unused-vars
  const _openContainer = useContainerStore(state => state.openContainer);
  // eslint-disable-next-line @typescript-eslint/no-unused-vars
  const _closeContainer = useContainerStore(state => state.closeContainer);
  // eslint-disable-next-line @typescript-eslint/no-unused-vars
  const _updateContainer = useContainerStore(state => state.updateContainer);
  // eslint-disable-next-line @typescript-eslint/no-unused-vars
  const _handleContainerDecayed = useContainerStore(state => state.handleContainerDecayed);
  // eslint-disable-next-line @typescript-eslint/no-unused-vars
  const _getContainer = useContainerStore(state => state.getContainer);
  // eslint-disable-next-line @typescript-eslint/no-unused-vars
  const _isContainerOpen = useContainerStore(state => state.isContainerOpen);

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
  const sanityStatusRef = useRef<SanityStatus | null>(null);
  const healthStatusRef = useRef<HealthStatus | null>(null);
  const rescueStateRef = useRef<RescueState | null>(null);
  const lastDaypartRef = useRef<string | null>(null);
  const lastHourRef = useRef<number | null>(null);
  const lastHolidayIdsRef = useRef<string[]>([]);
  const rescueTimeoutRef = useRef<number | null>(null);
  const lastRoomUpdateTime = useRef<number>(0);
  const sendCommandRef = useRef<((command: string, args?: string[]) => Promise<boolean>) | null>(null);

  // Keep refs in sync with state
  useEffect(() => {
    currentMessagesRef.current = gameState.messages;
  }, [gameState.messages]);

  useEffect(() => {
    currentRoomRef.current = gameState.room;
  }, [gameState.room]);

  useEffect(() => {
    currentPlayerRef.current = gameState.player;
  }, [gameState.player]);

  useEffect(() => {
    healthStatusRef.current = healthStatus;
  }, [healthStatus]);

  useEffect(() => {
    sanityStatusRef.current = sanityStatus;
  }, [sanityStatus]);

  useEffect(() => {
    rescueStateRef.current = rescueState;

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

  // Bootstrap Mythos time
  useEffect(() => {
    if (typeof fetch !== 'function') {
      return undefined;
    }

    let cancelled = false;

    const bootstrapMythosTime = async () => {
      try {
        const headers: HeadersInit = { Accept: 'application/json' };
        if (authToken) {
          headers.Authorization = `Bearer ${authToken}`;
        }
        const response = await fetch('/game/time', { headers });
        if (!response.ok) {
          throw new Error(`HTTP ${response.status}`);
        }
        const payload = (await response.json()) as MythosTimePayload;
        if (cancelled) {
          return;
        }
        const nextState = buildMythosTimeState(payload);
        setMythosTime(nextState);
        lastDaypartRef.current = nextState.daypart;
        lastHolidayIdsRef.current = nextState.active_holidays.map(h => h.id);
      } catch (error) {
        logger.warn('GameClientV2Container', 'Failed to bootstrap Mythos time', { error: String(error) });
      }
    };

    bootstrapMythosTime();
    return () => {
      cancelled = true;
    };
  }, [authToken]);

  // Clean up hallucination feed
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

  // Event processing - simplified version (full version would process all event types)
  // For greenfield, we'll process the essential events and can extend later
  const processEventQueue = useCallback(() => {
    if (isProcessingEvent.current || eventQueue.current.length === 0) {
      return;
    }

    isProcessingEvent.current = true;

    try {
      const events = [...eventQueue.current];
      eventQueue.current = [];
      const updates: Partial<GameState> = {};

      events.forEach(event => {
        const eventKey = `${event.event_type}_${event.sequence_number}`;
        if (eventKey === lastProcessedEvent.current) {
          return;
        }
        lastProcessedEvent.current = eventKey;

        const eventType = (event.event_type || '').toString().trim().toLowerCase();
        logger.info('GameClientV2Container', 'Processing event', { event_type: eventType });

        const appendMessage = (message: ChatMessage) => {
          if (!updates.messages) {
            updates.messages = [...currentMessagesRef.current];
          }
          updates.messages.push(message);
        };

        switch (eventType) {
          case 'player_entered_game': {
            // Handle player_entered_game events - initial connection messages
            const playerName = event.data?.player_name as string | undefined;
            if (playerName && typeof playerName === 'string' && playerName.trim()) {
              appendMessage({
                text: `${playerName} has entered the game.`,
                timestamp: event.timestamp,
                isHtml: false,
                messageType: 'system',
                channel: 'game',
                type: 'system',
              });
            }
            break;
          }
          case 'player_entered': {
            // Handle player_entered events - movement messages
            const playerName = event.data?.player_name as string;
            const messageText = event.data?.message as string;
            if (messageText && playerName) {
              appendMessage({
                text: messageText,
                timestamp: event.timestamp,
                isHtml: false,
                messageType: 'system',
                channel: 'game',
                type: 'system',
              });
            }
            break;
          }
          case 'game_state': {
            const playerData = event.data.player as Player;
            const roomData = event.data.room as Room;
            const occupants = event.data.occupants as string[] | undefined;
            if (playerData && roomData) {
              lastRoomUpdateTime.current = new Date(event.timestamp).getTime();
              updates.player = playerData;
              updates.room = {
                ...roomData,
                ...(occupants && { occupants, occupant_count: occupants.length }),
              };
            }
            break;
          }
          case 'room_update':
          case 'room_state': {
            const roomData = (event.data.room || event.data.room_data) as Room;
            if (roomData) {
              lastRoomUpdateTime.current = new Date(event.timestamp).getTime();

              // ARCHITECTURE: room_update events contain ONLY room metadata (name, description, exits, etc.)
              // Occupant data (players, npcs) comes EXCLUSIVELY from room_occupants events
              // This ensures a single authoritative source: RealTimeEventHandler._get_room_occupants()

              // Strip any occupant fields that might have leaked in (defensive)
              /* eslint-disable @typescript-eslint/no-unused-vars */
              const {
                players: _players,
                npcs: _npcs,
                occupants: _occupants,
                occupant_count: _occupant_count,
                ...roomMetadata
              } = roomData;
              /* eslint-enable @typescript-eslint/no-unused-vars */

              // Get existing room state to preserve occupant data
              // Priority: updates.room (from room_occupants in same batch) > currentRoomRef
              // Note: currentRoomRef is kept in sync with gameState.room via useEffect
              const existingRoom = updates.room || currentRoomRef.current;

              if (existingRoom) {
                // ARCHITECTURE: room_update is ONLY for room metadata (description, exits, name, etc.)
                // NPCs and players are ONLY provided by room_occupants events (authoritative source)
                // room_update should NEVER touch NPCs or players - only update room metadata
                const roomIdChanged = roomData.id !== existingRoom.id;

                // CRITICAL: Preserve ALL occupant data from existingRoom (set by room_occupants events)
                // room_update should NEVER modify NPCs, players, occupants, or occupant_count
                // These are ONLY managed by room_occupants events
                const roomUpdate: Partial<Room> = {
                  ...existingRoom,
                  ...roomMetadata,
                  // CRITICAL: Preserve ALL occupant data from existingRoom
                  // room_update does NOT include NPC/player data (server removes it)
                  // We preserve it from existingRoom to prevent loss during metadata updates
                  players: existingRoom.players ?? [],
                  npcs: existingRoom.npcs, // Preserve from existingRoom (set by room_occupants)
                  occupants: existingRoom.occupants ?? [],
                  occupant_count: existingRoom.occupant_count ?? 0,
                };

                // If room ID changed, clear occupants (will be repopulated by room_occupants for new room)
                if (roomIdChanged) {
                  roomUpdate.players = [];
                  roomUpdate.npcs = undefined; // Clear NPCs for new room
                  roomUpdate.occupants = [];
                  roomUpdate.occupant_count = 0;
                }

                updates.room = roomUpdate as Room;
              } else {
                // First room_update - initialize WITHOUT occupants (room_occupants will populate)
                // CRITICAL: Don't set npcs: [] - leave it undefined so merge logic knows there's no data yet
                updates.room = {
                  ...roomMetadata,
                  players: [],
                  // npcs: undefined (not set) - room_occupants will populate this
                  occupants: [],
                  occupant_count: 0,
                };
              }
            }
            break;
          }
          case 'sanity_change':
          case 'sanitychange': {
            const { status: updatedStatus } = buildSanityStatus(sanityStatusRef.current, event.data, event.timestamp);
            setSanityStatus(updatedStatus);
            if (currentPlayerRef.current) {
              updates.player = {
                ...currentPlayerRef.current,
                stats: {
                  ...currentPlayerRef.current.stats,
                  current_health: currentPlayerRef.current.stats?.current_health ?? 0,
                  sanity: updatedStatus.current,
                },
              };
            }
            break;
          }
          case 'player_hp_updated':
          case 'playerhpupdated': {
            logger.info('GameClientV2Container', 'Received player_hp_updated event', {
              old_hp: event.data.old_hp,
              new_hp: event.data.new_hp,
              max_hp: event.data.max_hp,
              damage_taken: event.data.damage_taken,
            });

            const { status: updatedHealthStatus } = buildHealthStatusFromEvent(
              healthStatusRef.current,
              event.data,
              event.timestamp
            );

            logger.info('GameClientV2Container', 'Updated health status', {
              current: updatedHealthStatus.current,
              max: updatedHealthStatus.max,
              tier: updatedHealthStatus.tier,
            });

            setHealthStatus(updatedHealthStatus);
            if (currentPlayerRef.current) {
              updates.player = {
                ...currentPlayerRef.current,
                stats: {
                  ...currentPlayerRef.current.stats,
                  current_health: updatedHealthStatus.current,
                  max_health: updatedHealthStatus.max,
                  sanity: currentPlayerRef.current.stats?.sanity ?? 0,
                },
              };
              logger.info('GameClientV2Container', 'Updated player stats', {
                current_health: updatedHealthStatus.current,
                max_health: updatedHealthStatus.max,
              });
            }
            break;
          }
          case 'command_response': {
            const suppressChat = Boolean(event.data?.suppress_chat);
            const message = typeof event.data?.result === 'string' ? (event.data.result as string) : '';
            const isHtml = Boolean(event.data?.is_html);
            const gameLogChannel =
              typeof event.data?.game_log_channel === 'string' && event.data.game_log_channel
                ? (event.data.game_log_channel as string)
                : GAME_LOG_CHANNEL;
            const gameLogMessage =
              (typeof event.data?.game_log_message === 'string' && event.data.game_log_message.length > 0
                ? (event.data.game_log_message as string)
                : undefined) || message;

            if (message) {
              if (message.includes('Name:') && message.includes('Health:') && message.includes('Sanity:')) {
                try {
                  const parsedPlayerData = parseStatusResponse(message);
                  const playerData = convertToPlayerInterface(parsedPlayerData);
                  updates.player = playerData;
                } catch (error) {
                  logger.error('GameClientV2Container', 'Failed to parse status response', {
                    error: error instanceof Error ? error.message : String(error),
                  });
                }
              }
            }

            // Filter out room name-only messages (these are sent by the server for room updates
            // but should not be displayed as they duplicate the Room Info panel)
            // Room names are typically just the room name without description or other content
            const isRoomNameOnly =
              message &&
              message.trim().length > 0 &&
              message.trim().length < 100 &&
              !message.includes('\n') &&
              !message.includes('Exits:') &&
              !message.includes('Description:') &&
              currentRoomRef.current &&
              message.trim() === currentRoomRef.current.name;

            if (!suppressChat && message && !isRoomNameOnly) {
              const messageTypeResult = determineMessageType(message);
              appendMessage({
                text: message,
                timestamp: event.timestamp,
                isHtml,
                messageType: messageTypeResult.type,
                channel: messageTypeResult.channel ?? 'game',
                type: resolveChatTypeFromChannel(messageTypeResult.channel ?? 'game'),
              });
            } else if (gameLogMessage && !isRoomNameOnly) {
              appendMessage({
                text: gameLogMessage,
                timestamp: event.timestamp,
                isHtml,
                messageType: 'system',
                channel: gameLogChannel,
                type: 'system',
              });
            }
            break;
          }
          case 'player_left_game': {
            // Handle player_left_game events - disconnection messages
            const playerName = event.data?.player_name as string;
            if (playerName) {
              appendMessage({
                text: `${playerName} has left the game.`,
                timestamp: event.timestamp,
                isHtml: false,
                messageType: 'system',
                channel: 'game',
                type: 'system',
              });
            }
            break;
          }
          case 'player_left': {
            // Handle player_left events - movement messages
            const messageText = event.data?.message as string;
            if (messageText) {
              appendMessage({
                text: messageText,
                timestamp: event.timestamp,
                isHtml: false,
                messageType: 'system',
                channel: 'game',
                type: 'system',
              });
            }
            break;
          }
          case 'room_message': {
            // Handle room messages (NPC movement, spawns, etc.)
            const message = typeof event.data?.message === 'string' ? (event.data.message as string) : '';
            const messageTypeFromEvent =
              typeof event.data?.message_type === 'string' ? (event.data.message_type as string) : undefined;
            const isHtml = Boolean(event.data?.is_html);

            if (message) {
              // Use message_type from event if provided, otherwise determine from content
              let messageType: string;
              let channel: string;

              if (messageTypeFromEvent === 'system') {
                // Server explicitly marked this as system message (NPC movement, etc.)
                messageType = 'system';
                channel = GAME_LOG_CHANNEL;
              } else {
                // Fall back to pattern matching
                const messageTypeResult = determineMessageType(message);
                messageType = messageTypeResult.type;
                channel = messageTypeResult.channel ?? 'game';
              }

              appendMessage({
                text: message,
                timestamp: event.timestamp,
                isHtml,
                messageType: messageType,
                channel: channel,
                type: resolveChatTypeFromChannel(channel),
              });
            }
            break;
          }
          case 'chat_message': {
            const message = event.data.message as string;
            const channel = event.data.channel as string;
            if (message) {
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

              appendMessage({
                text: message,
                timestamp: event.timestamp,
                isHtml: false,
                messageType: messageType,
                channel: channel,
                type: resolveChatTypeFromChannel(channel),
              });
            }
            break;
          }
          case 'room_occupants': {
            // Support both new structured format (players/npcs) and legacy format (occupants)
            const players = event.data.players as string[] | undefined;
            const npcs = event.data.npcs as string[] | undefined;
            const occupants = event.data.occupants as string[] | undefined; // Legacy format
            const occupantCount = event.data.count as number | undefined;
            const eventRoomId = event.room_id as string | undefined;

            // DEBUG: Console log for immediate visibility + structured logging
            console.log('🔍 [room_occupants] Received event:', {
              players,
              npcs,
              npcs_count: npcs?.length ?? 0,
              occupants,
              occupantCount,
              eventRoomId,
              hasCurrentRoom: !!currentRoomRef.current,
              currentRoomId: currentRoomRef.current?.id,
              currentRoomPlayers: currentRoomRef.current?.players,
              currentRoomNpcs: currentRoomRef.current?.npcs,
              hasUpdatesRoom: !!updates.room,
              updatesRoomId: updates.room?.id,
              updatesRoomNpcs: updates.room?.npcs,
            });

            // DEBUG: Log received data
            logger.debug('GameClientV2Container', 'Processing room_occupants event', {
              players,
              npcs,
              npcs_count: npcs?.length ?? 0,
              occupants,
              occupantCount,
              eventRoomId,
              hasCurrentRoom: !!currentRoomRef.current,
              currentRoomId: currentRoomRef.current?.id,
              currentRoomPlayers: currentRoomRef.current?.players,
              currentRoomNpcs: currentRoomRef.current?.npcs,
              hasUpdatesRoom: !!updates.room,
              updatesRoomId: updates.room?.id,
            });

            // CRITICAL FIX: Use updates.room if available (from room_update in same batch),
            // otherwise use currentRoomRef.current (it's kept in sync via useEffect)
            // This handles the case where room_update and room_occupants arrive in the same batch
            const currentRoom = updates.room || currentRoomRef.current;

            if (currentRoom) {
              // CRITICAL FIX: Only update if room IDs match, or if event doesn't have room_id (backward compatibility)
              // This prevents NPCs from wrong room being merged into current room
              if (eventRoomId && eventRoomId !== currentRoom.id) {
                logger.warn('GameClientV2Container', 'room_occupants event room_id mismatch - ignoring', {
                  eventRoomId,
                  currentRoomId: currentRoom.id,
                  npcsCount: npcs?.length ?? 0,
                });
                break;
              }

              // ARCHITECTURE: room_occupants events are the SINGLE AUTHORITATIVE SOURCE for occupant data
              // This event always uses structured format (players/npcs arrays) from
              // RealTimeEventHandler._get_room_occupants() which queries:
              // - Players: Room._players (in-memory, reliable)
              // - NPCs: NPCLifecycleManager.active_npcs (authoritative, survives re-instantiation)

              // Use structured format if available (preferred), otherwise fall back to legacy flat list
              if (players !== undefined || npcs !== undefined) {
                // Structured format: separate players and NPCs arrays
                // CRITICAL: Only use npcs/players from event if they're actually provided (not undefined)
                // If undefined, preserve from currentRoom to avoid overwriting with empty arrays
                const finalNpcs = npcs !== undefined ? npcs : (currentRoom.npcs ?? []);
                const finalPlayers = players !== undefined ? players : (currentRoom.players ?? []);

                updates.room = {
                  ...currentRoom,
                  players: finalPlayers,
                  npcs: finalNpcs,
                  // Backward compatibility: also populate flat occupants list
                  occupants: [...finalPlayers, ...finalNpcs],
                  occupant_count: occupantCount ?? finalPlayers.length + finalNpcs.length,
                };
                logger.debug('GameClientV2Container', 'Updated room with structured occupants from room_occupants', {
                  roomId: updates.room.id,
                  players_count: updates.room.players?.length ?? 0,
                  npcs_count: updates.room.npcs?.length ?? 0,
                  total_count: updates.room.occupant_count,
                });
              } else if (occupants && Array.isArray(occupants)) {
                // Legacy format: flat list (for backward compatibility)
                // Try to split into players/npcs if possible, otherwise use flat list
                updates.room = {
                  ...currentRoom,
                  occupants: occupants,
                  occupant_count: occupantCount ?? occupants.length,
                  // Preserve existing structured data if available, otherwise use flat list
                  players: currentRoom.players ?? [],
                  npcs: currentRoom.npcs ?? [],
                };
                logger.debug('GameClientV2Container', 'Updated room with legacy occupants format', {
                  roomId: updates.room.id,
                  occupants_count: updates.room.occupants?.length ?? 0,
                  occupant_count: updates.room.occupant_count,
                });
              }
            } else {
              logger.warn('GameClientV2Container', 'room_occupants event received but no room state available', {
                hasCurrentRoomRef: !!currentRoomRef.current,
                hasUpdatesRoom: !!updates.room,
              });
            }
            break;
          }
          case 'mythos_time_update': {
            const payload = event.data as unknown as MythosTimePayload;
            if (payload && payload.mythos_clock) {
              const nextState = buildMythosTimeState(payload);
              setMythosTime(nextState);

              // Extract current hour from mythos_datetime for clock chime messages
              let currentHour: number | null = null;
              if (payload.mythos_datetime) {
                try {
                  const mythosDate = new Date(payload.mythos_datetime);
                  currentHour = mythosDate.getUTCHours();
                } catch (error) {
                  logger.error('GameClientV2Container', 'Failed to parse mythos_datetime for clock chime', {
                    error: error instanceof Error ? error.message : String(error),
                    mythos_datetime: payload.mythos_datetime,
                  });
                }
              }

              // Create clock chime message on hourly tick
              if (currentHour !== null) {
                const previousHour = lastHourRef.current;
                if (previousHour !== null && previousHour !== currentHour) {
                  const formattedClock = formatMythosTime12Hour(payload.mythos_clock);
                  appendMessage(
                    sanitizeChatMessageForState({
                      text: `[Time] The clock chimes ${formattedClock} Mythos`,
                      timestamp: event.timestamp,
                      messageType: 'system',
                      channel: 'system',
                      isHtml: false,
                    })
                  );
                  logger.debug('GameClientV2Container', 'Displayed hourly clock chime message', {
                    hour: currentHour,
                    mythos_clock: payload.mythos_clock,
                  });
                }
                lastHourRef.current = currentHour;
              }

              // Create daypart change message
              const previousDaypart = lastDaypartRef.current;
              if (previousDaypart && previousDaypart !== nextState.daypart) {
                const description =
                  DAYPART_MESSAGES[nextState.daypart] ?? `The Mythos clock shifts into the ${nextState.daypart} watch.`;
                appendMessage(
                  sanitizeChatMessageForState({
                    text: `[Time] ${description}`,
                    timestamp: event.timestamp,
                    messageType: 'system',
                    channel: 'system',
                    isHtml: false,
                  })
                );
              }
              lastDaypartRef.current = nextState.daypart;
            }
            break;
          }
          case 'game_tick': {
            // Extract tick data from event
            // Note: event.data contains the tick_data object directly from broadcast_game_event
            const tickNumber = typeof event.data?.tick_number === 'number' ? event.data.tick_number : 0;

            // Display every 10th tick (tick 0, 10, 20, 30, etc.)
            // This provides a 10-second update interval since ticks run every 1 second
            if (tickNumber % 10 === 0 && tickNumber >= 0) {
              appendMessage(
                sanitizeChatMessageForState({
                  text: `[Tick ${tickNumber}]`,
                  timestamp: event.timestamp,
                  messageType: 'system',
                  channel: 'system',
                  isHtml: false,
                })
              );
              logger.debug('GameClientV2Container', 'Displayed game tick message', {
                tickNumber,
              });
            }
            break;
          }
          case 'npc_attacked': {
            // NPC attacked event - NPC attacks player
            // Note: attacker_name is the NPC's name, npc_name is also the NPC's name (redundant field)
            const attackerName = (event.data.attacker_name || event.data.npc_name) as string | undefined;
            const damage = event.data.damage as number | undefined;
            const actionType = event.data.action_type as string | undefined;

            if (attackerName && damage !== undefined) {
              // Format: "Dr. Francis Morgan attacks you for 10 damage."
              const message = `${attackerName} ${actionType || 'attacks'} you for ${damage} damage.`;
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
            break;
          }
          case 'player_attacked': {
            // Player attacked event - player attacks NPC
            const attackerName = event.data.attacker_name as string | undefined;
            const targetName = event.data.target_name as string | undefined;
            const damage = event.data.damage as number | undefined;
            const actionType = event.data.action_type as string | undefined;
            const targetCurrentHp = event.data.target_current_hp as number | undefined;
            const targetMaxHp = event.data.target_max_hp as number | undefined;

            if (attackerName && targetName && damage !== undefined) {
              // Format: "You attack Dr. Francis Morgan for 10 damage. (50/100 HP)"
              let message = `You ${actionType || 'attack'} ${targetName} for ${damage} damage.`;
              if (targetCurrentHp !== undefined && targetMaxHp !== undefined) {
                message += ` (${targetCurrentHp}/${targetMaxHp} HP)`;
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
            break;
          }
          case 'combat_started': {
            // Combat started - update player in_combat status
            if (currentPlayerRef.current) {
              updates.player = {
                ...currentPlayerRef.current,
                in_combat: true,
              };
            }
            break;
          }
          case 'combat_ended': {
            // Combat ended - update player in_combat status
            if (currentPlayerRef.current) {
              updates.player = {
                ...currentPlayerRef.current,
                in_combat: false,
              };
            }
            break;
          }
          case 'player_update': {
            // Player update event - update player data including in_combat status
            const playerData = event.data as { in_combat?: boolean; [key: string]: unknown };
            if (currentPlayerRef.current && playerData.in_combat !== undefined) {
              updates.player = {
                ...currentPlayerRef.current,
                in_combat: playerData.in_combat,
              };
            }
            break;
          }
          case 'player_died':
          case 'playerdied': {
            // Player died event - show death interstitial
            const deathData = event.data as { death_location?: string; room_id?: string; [key: string]: unknown };
            const deathLocation = deathData.death_location || deathData.room_id || 'Unknown Location';
            setIsDead(true);
            logger.info('GameClientV2Container', 'Player died event received', { deathLocation });
            break;
          }
          case 'player_respawned':
          case 'playerrespawned': {
            // Player respawned event - hide death interstitial and update player state
            const respawnData = event.data as {
              player?: Player;
              respawn_room_id?: string;
              old_hp?: number;
              new_hp?: number;
              message?: string;
              [key: string]: unknown;
            };

            setIsDead(false);
            setIsMortallyWounded(false);
            setIsRespawning(false);

            if (respawnData.player) {
              updates.player = respawnData.player as Player;
              // CRITICAL FIX: Update health status from player data in respawn event
              // The respawn event includes player_data with correct current_health, but healthStatus
              // was not being updated, causing health to remain at -10 from death state
              // As documented in "Resurrection and Health State Synchronization" - Dr. Armitage, 1930
              if (respawnData.player.stats?.current_health !== undefined) {
                const playerStats = respawnData.player.stats;
                const currentHealth = playerStats.current_health;
                const maxHealth = playerStats.max_health ?? 100;
                const healthStatusUpdate: HealthStatus = {
                  current: currentHealth,
                  max: maxHealth,
                  tier: determineHealthTier(currentHealth, maxHealth),
                  posture: playerStats.position,
                  inCombat: respawnData.player.in_combat ?? false,
                  lastChange: {
                    delta: currentHealth - (healthStatusRef.current?.current ?? 0),
                    reason: 'respawn',
                    timestamp: event.timestamp,
                  },
                };
                setHealthStatus(healthStatusUpdate);
              }
            }

            if (respawnData.message) {
              appendMessage(
                sanitizeChatMessageForState({
                  text: respawnData.message,
                  timestamp: event.timestamp,
                  messageType: 'system',
                  channel: 'system',
                  isHtml: false,
                })
              );
            }

            logger.info('GameClientV2Container', 'Player respawned event received', {
              respawn_room: respawnData.respawn_room_id,
              new_hp: respawnData.new_hp,
            });
            break;
          }
          case 'npc_died': {
            // NPC died event - display death message in Game Info panel
            // Server broadcasts npc_died events with npc_name, xp_reward, and other data
            const npcName = event.data.npc_name as string | undefined;
            const xpReward = event.data.xp_reward as number | undefined;

            if (npcName) {
              // Format: "Dr. Francis Morgan dies."
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

              // Display XP reward message if available
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
            break;
          }
          case 'combat_death': {
            // Combat death event - display formatted death messages
            // This event contains pre-formatted messages in event.data.messages
            const messages = event.data.messages as { death_message?: string; xp_reward?: string } | undefined;

            if (messages) {
              // Display death message
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

              // Display XP reward message if available
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
            break;
          }
          case 'system': {
            // Handle system event type - admin notifications, teleportation messages, etc.
            const systemMessage = event.data?.message;
            if (systemMessage && typeof systemMessage === 'string') {
              appendMessage({
                text: systemMessage,
                timestamp: event.timestamp,
                isHtml: false,
                messageType: 'system',
                channel: 'game',
                type: 'system',
              });
              logger.info('GameClientV2Container', 'Processing event', {
                event_type: 'system',
                message: systemMessage,
              });
            }
            break;
          }
          // Add more event types as needed - this is a simplified version
          default: {
            logger.info('GameClientV2Container', 'Unhandled event type', {
              event_type: event.event_type,
              data_keys: event.data ? Object.keys(event.data) : [],
            });
            break;
          }
        }
      });

      if (updates.messages) {
        updates.messages = updates.messages.map(sanitizeChatMessageForState);
      }

      if (Object.keys(updates).length > 0) {
        setGameState(prev => {
          // ARCHITECTURE: Single authoritative source for occupant data
          // - room_occupants events set players/npcs (authoritative)
          // - room_update events update metadata only (preserves existing occupants)
          // - If updates.room has occupant data, use it (from room_occupants)
          // - If updates.room doesn't have occupant data, preserve from prev.room

          let finalRoom = updates.room || prev.room;

          if (updates.room && prev.room) {
            // CRITICAL FIX: Check if room ID changed - if so, don't preserve NPCs from old room
            const roomIdChanged = updates.room.id !== prev.room.id;

            // Preserve occupant data if updates.room doesn't have populated occupant arrays
            // This handles room_update events that only update metadata
            // CRITICAL FIX: Check if arrays are populated, not just if they're defined
            // Empty arrays [] are still "defined" but should be treated as "no occupant data"
            // Also check if prev.room has populated arrays to preserve them
            const updatesHasPopulatedPlayers =
              updates.room.players !== undefined &&
              Array.isArray(updates.room.players) &&
              updates.room.players.length > 0;
            const updatesHasPopulatedNpcs =
              updates.room.npcs !== undefined && Array.isArray(updates.room.npcs) && updates.room.npcs.length > 0;
            const prevHasPopulatedPlayers =
              prev.room.players !== undefined && Array.isArray(prev.room.players) && prev.room.players.length > 0;
            const prevHasPopulatedNpcs =
              prev.room.npcs !== undefined && Array.isArray(prev.room.npcs) && prev.room.npcs.length > 0;

            // Merge strategy:
            // 1. If updates has populated data, use it (from room_occupants - authoritative)
            // 2. If room ID changed, use new room's data (even if empty) - don't preserve old room's NPCs
            // 3. If updates has empty arrays but prev has populated data AND room ID didn't change, preserve from prev
            // 4. If updates has no data (undefined), preserve from prev (only if same room)
            // CRITICAL FIX: Empty arrays [] are NOT undefined, so ?? operator won't work
            // We must explicitly check for populated arrays, not just existence

            // Calculate merged players array
            const mergedPlayers: string[] = updatesHasPopulatedPlayers
              ? (updates.room.players ?? [])
              : roomIdChanged
                ? (updates.room.players ?? []) // Room changed - use new room's players (even if empty)
                : prevHasPopulatedPlayers
                  ? (prev.room.players ?? [])
                  : (updates.room.players ?? prev.room.players ?? []);

            // Calculate merged NPCs array
            let mergedNpcs: string[];
            if (updatesHasPopulatedNpcs) {
              mergedNpcs = updates.room.npcs ?? []; // Updates has populated NPCs (from room_occupants) - use it
            } else if (roomIdChanged) {
              // CRITICAL FIX: Room ID changed - use new room's NPCs (even if empty), don't preserve old room's NPCs
              mergedNpcs = updates.room.npcs ?? []; // New room's NPCs (empty array if not set yet)
            } else if (prevHasPopulatedNpcs) {
              mergedNpcs = prev.room.npcs ?? []; // Updates has no NPCs but prev does - preserve prev (same room)
            } else {
              // Neither has populated NPCs, and room ID didn't change
              // CRITICAL: If updates explicitly set npcs: [] (empty array from room_update)
              // but prev has NPCs (from previous room_occupants), preserve prev ONLY if same room
              // (roomIdChanged check above already handles room changes)
              if (
                updates.room.npcs !== undefined &&
                updates.room.npcs.length === 0 &&
                prev.room.npcs &&
                prev.room.npcs.length > 0
              ) {
                // room_update tried to clear NPCs, but prev has them - preserve prev (same room)
                mergedNpcs = prev.room.npcs;
              } else {
                mergedNpcs = updates.room.npcs ?? prev.room.npcs ?? []; // Default fallback
              }
            }

            // Calculate merged occupants array
            const mergedOccupants = [...mergedPlayers, ...mergedNpcs];

            // Calculate occupant count from merged values (not from updates.room)
            // CRITICAL FIX: occupant_count must be calculated from merged arrays, not from updates.room
            // because the merge logic may preserve players or NPCs from prev.room
            const mergedOccupantCount = updates.room.occupant_count ?? mergedOccupants.length;

            finalRoom = {
              ...updates.room,
              players: mergedPlayers,
              npcs: mergedNpcs,
              occupants: mergedOccupants,
              occupant_count: mergedOccupantCount,
            };
          }

          return {
            ...prev,
            ...updates,
            messages: updates.messages || prev.messages,
            player: updates.player || prev.player,
            room: finalRoom,
          };
        });
      }
    } catch (error) {
      logger.error('GameClientV2Container', 'Error processing events', { error });
    } finally {
      isProcessingEvent.current = false;

      if (eventQueue.current.length > 0) {
        processingTimeout.current = window.setTimeout(processEventQueue, 10);
      }
    }
  }, []);

  const handleGameEvent = useCallback(
    (event: GameEvent) => {
      logger.info('GameClientV2Container', 'Received game event', { event_type: event.event_type });
      eventQueue.current.push(event);
      if (!isProcessingEvent.current && !processingTimeout.current) {
        processingTimeout.current = window.setTimeout(() => {
          processingTimeout.current = null;
          processEventQueue();
        }, 10);
      }
    },
    [processEventQueue]
  );

  const handleConnectionLoss = useCallback(() => {
    logger.info('GameClientV2Container', 'Connection lost, triggering logout flow');
    const connectionLostMessage: ChatMessage = sanitizeChatMessageForState({
      text: 'Connection to server lost. Returning to login screen...',
      timestamp: new Date().toISOString(),
      messageType: 'system',
      isHtml: false,
    });

    setGameState(prev => ({
      ...prev,
      messages: [...prev.messages, connectionLostMessage],
    }));

    setTimeout(() => {
      if (onLogout) {
        onLogout();
      }
    }, 1000);
  }, [onLogout]);

  const handleConnect = useCallback(() => {
    logger.info('GameClientV2Container', 'Connected to game server');
  }, []);

  const handleDisconnect = useCallback(() => {
    logger.info('GameClientV2Container', 'Disconnected from game server');
  }, []);

  const handleError = useCallback((error: string) => {
    logger.error('GameClientV2Container', 'Game connection error', { error });
  }, []);

  const { isConnected, isConnecting, error, reconnectAttempts, connect, disconnect, sendCommand } = useGameConnection({
    authToken,
    onEvent: handleGameEvent,
    onConnect: handleConnect,
    onDisconnect: handleDisconnect,
    onError: handleError,
  });

  useEffect(() => {
    sendCommandRef.current = sendCommand;
  }, [sendCommand]);

  useEffect(() => {
    if (!isConnected && !isConnecting && reconnectAttempts >= 5) {
      logger.warn('GameClientV2Container', 'All reconnection attempts failed, triggering logout');
      handleConnectionLoss();
    }
  }, [isConnected, isConnecting, reconnectAttempts, handleConnectionLoss]);

  useEffect(() => {
    if (!hasAttemptedConnection.current) {
      hasAttemptedConnection.current = true;
      logger.info('GameClientV2Container', 'Initiating connection', {
        hasAuthToken: !!authToken,
        playerName,
      });
      connect();
    }

    return () => {
      logger.info('GameClientV2Container', 'Cleaning up connection on unmount');
      disconnect();
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  // Check if player is dead based on HP or room location
  useEffect(() => {
    const player = gameState.player;
    if (!player) return;

    const currentHp = player.stats?.current_health ?? 0;
    const roomId = gameState.room?.id;
    const isInLimbo = roomId === 'limbo_death_void_limbo_death_void';

    // Player is dead if HP <= -10 or in limbo
    if (currentHp <= -10 || isInLimbo) {
      if (!isDead) {
        setIsDead(true);
        logger.info('GameClientV2Container', 'Player detected as dead', {
          currentHp,
          roomId,
          isInLimbo,
        });
      }
    } else if (isDead && currentHp > -10 && !isInLimbo) {
      // Player is no longer dead
      setIsDead(false);
      logger.info('GameClientV2Container', 'Player detected as alive', {
        currentHp,
        roomId,
      });
    }
  }, [gameState.player, gameState.room, isDead]);

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
  };

  const handleChatMessage = async (message: string, channel: string) => {
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
  };

  const handleClearMessages = () => {
    setGameState(prev => ({ ...prev, messages: [] }));
  };

  const handleClearHistory = () => {
    setGameState(prev => ({ ...prev, commandHistory: [] }));
  };

  const handleLogout = () => {
    const logoutMessage: ChatMessage = sanitizeChatMessageForState({
      text: 'You have been logged out of the MythosMUD server.',
      timestamp: new Date().toISOString(),
      messageType: 'system',
      isHtml: false,
    });

    setGameState(prev => ({
      ...prev,
      messages: [...prev.messages, logoutMessage],
    }));

    setTimeout(() => {
      if (onLogout) {
        onLogout();
      } else {
        disconnect();
      }
    }, 500);
  };

  const handleRespawn = async () => {
    logger.info('GameClientV2Container', 'Respawn requested');
    setIsRespawning(true);

    try {
      const response = await fetch('/api/players/respawn', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${authToken}`,
        },
      });

      if (!response.ok) {
        const errorData = await response.json();
        logger.error('GameClientV2Container', 'Respawn failed', {
          status: response.status,
          error: errorData,
        });

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
      logger.info('GameClientV2Container', 'Respawn successful', {
        room: respawnData.room,
        player: respawnData.player,
      });

      setIsDead(false);
      setIsMortallyWounded(false);
      setIsRespawning(false);

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
      logger.error('GameClientV2Container', 'Error calling respawn API', { error });

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

  // Handle ESC key to open/close main menu (only when map is not open)
  useEffect(() => {
    if (isDead || showMap) return;

    const handleEscape = (event: KeyboardEvent) => {
      if (event.key === 'Escape') {
        setIsMainMenuOpen(prev => !prev);
      }
    };

    window.addEventListener('keydown', handleEscape);
    return () => {
      window.removeEventListener('keydown', handleEscape);
    };
  }, [isDead, showMap]);

  return (
    <div
      className={`game-terminal-container ${isMortallyWounded ? 'mortally-wounded' : ''} ${isDead ? 'dead' : ''}`}
      data-game-container
    >
      {/* Only show game panels when no tabs are open */}
      {tabs.length === 0 && (
        <GameClientV2
          playerName={playerName}
          authToken={authToken}
          onLogout={handleLogout}
          isLoggingOut={isLoggingOut}
          player={gameState.player}
          room={gameState.room}
          messages={gameState.messages}
          commandHistory={gameState.commandHistory}
          isConnected={isConnected}
          isConnecting={isConnecting}
          error={error}
          reconnectAttempts={reconnectAttempts}
          mythosTime={mythosTime}
          healthStatus={healthStatus}
          sanityStatus={sanityStatus}
          onSendCommand={handleCommandSubmit}
          onSendChatMessage={handleChatMessage}
          onClearMessages={handleClearMessages}
          onClearHistory={handleClearHistory}
          onDownloadLogs={() => logger.downloadLogs()}
        />
      )}

      <DeathInterstitial
        isVisible={isDead}
        deathLocation={deathLocation}
        onRespawn={handleRespawn}
        isRespawning={isRespawning}
      />

      <MainMenuModal
        isOpen={isMainMenuOpen}
        onClose={() => setIsMainMenuOpen(false)}
        onMapClick={() => {
          // Add map as a tab in the tabbed interface
          if (gameState.room) {
            addTab({
              id: `map-${gameState.room.id}`,
              label: 'Map',
              content: (
                <MapView
                  isOpen={true}
                  onClose={() => closeTab(`map-${gameState.room!.id}`)}
                  currentRoom={gameState.room}
                  authToken={authToken}
                  hideHeader={true}
                />
              ),
              closable: true,
            });
          }
        }}
        onLogoutClick={handleLogout}
        currentRoom={
          gameState.room
            ? {
                id: gameState.room.id,
                plane: gameState.room.plane,
                zone: gameState.room.zone,
                subZone: gameState.room.sub_zone,
              }
            : null
        }
        openMapInNewTab={false}
      />

      {/* Tabbed Interface Overlay */}
      {tabs.length > 0 && (
        <div className="fixed inset-0 z-9999 bg-mythos-terminal-background">
          <div className="flex flex-col h-full">
            {/* Tab Bar */}
            <div className="flex items-center border-b border-mythos-terminal-border bg-mythos-terminal-background overflow-x-auto">
              {tabs.map(tab => (
                <div
                  key={tab.id}
                  className={`
                    flex items-center gap-2 px-4 py-2 border-r border-mythos-terminal-border
                    cursor-pointer transition-colors
                    ${
                      activeTabId === tab.id
                        ? 'bg-mythos-terminal-primary text-white'
                        : 'bg-mythos-terminal-background text-mythos-terminal-text hover:bg-mythos-terminal-border/50'
                    }
                  `}
                  onClick={() => setActiveTab(tab.id)}
                >
                  <span className="text-sm font-medium whitespace-nowrap">{tab.label}</span>
                  {tab.closable !== false && (
                    <button
                      onClick={e => {
                        e.stopPropagation();
                        closeTab(tab.id);
                      }}
                      className="ml-1 hover:bg-black/20 rounded p-0.5 transition-colors"
                      aria-label={`Close ${tab.label}`}
                    >
                      ×
                    </button>
                  )}
                </div>
              ))}
            </div>
            {/* Tab Content */}
            <div className="flex-1 overflow-hidden">{tabs.find(tab => tab.id === activeTabId)?.content}</div>
          </div>
        </div>
      )}

      {/* Legacy MapView for backward compatibility (can be removed later) */}
      <MapView
        isOpen={showMap && tabs.length === 0}
        onClose={() => setShowMap(false)}
        currentRoom={gameState.room}
        authToken={authToken}
      />
    </div>
  );
};
