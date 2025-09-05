import { useCallback, useEffect, useRef, useState } from 'react';
import { useGameConnection } from '../hooks/useGameConnection';
import { logger } from '../utils/logger';
import { debugMessageCategorization, determineMessageType } from '../utils/messageTypeUtils';

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
import { GameTerminal } from './GameTerminal';

interface GameTerminalWithPanelsProps {
  playerName: string;
  authToken: string;
}

interface Player {
  name: string;
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
  current_room_id?: string;
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
  aliasChain?: Array<{
    original: string;
    expanded: string;
    alias_name: string;
  }>;
}

interface GameState {
  player: Player | null;
  room: Room | null;
  messages: ChatMessage[];
  commandHistory: string[];
}

export const GameTerminalWithPanels: React.FC<GameTerminalWithPanelsProps> = ({ playerName, authToken }) => {
  const [gameState, setGameState] = useState<GameState>({
    player: null,
    room: null,
    messages: [],
    commandHistory: [],
  });

  // Refs for stable references and event processing
  const hasAttemptedConnection = useRef(false);
  const isProcessingEvent = useRef(false);
  const lastProcessedEvent = useRef<string>('');
  const eventQueue = useRef<GameEvent[]>([]);
  const processingTimeout = useRef<number | null>(null);
  const currentMessagesRef = useRef<ChatMessage[]>([]);

  // Keep the ref in sync with the state
  useEffect(() => {
    currentMessagesRef.current = gameState.messages;
  }, [gameState.messages]);

  // Event processing function with debouncing and deduplication
  const processEventQueue = useCallback(() => {
    console.log('🚨 DEBUG: processEventQueue called', {
      isProcessing: isProcessingEvent.current,
      queueLength: eventQueue.current.length,
      queueContents: eventQueue.current.map(e => e.event_type),
    });

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
        });

        // Add critical debugging for command_response events
        if (eventType.includes('command') || eventType.includes('response')) {
          console.error('🚨 CRITICAL DEBUG: Potential command response event detected', {
            originalEventType: event.event_type,
            normalizedEventType: eventType,
            eventTypeIncludesCommand: eventType.includes('command'),
            eventTypeIncludesResponse: eventType.includes('response'),
            fullEvent: event,
          });
        }

        // Add critical debugging for ALL events to see what we're receiving
        console.error('🚨 CRITICAL DEBUG: ALL EVENT TYPES RECEIVED', {
          originalEventType: event.event_type,
          normalizedEventType: eventType,
          eventTypeLength: eventType.length,
          eventTypeCharCodes: Array.from(eventType).map(c => c.charCodeAt(0)),
          fullEvent: event,
          timestamp: new Date().toISOString(),
          willMatchCommandResponse: eventType === 'command_response',
          willMatchWelcome: eventType === 'welcome',
          willMatchRoomUpdate: eventType === 'room_update',
          switchCase: 'about_to_enter_switch',
        });

        // Add specific debugging for command_response events to see if they reach processEventQueue
        if (eventType === 'command_response') {
          console.error('🚨 CRITICAL DEBUG: command_response event REACHED processEventQueue!', {
            originalEventType: event.event_type,
            normalizedEventType: eventType,
            eventTypeExact: `"${eventType}"`,
            eventTypeLength: eventType.length,
            eventTypeCharCodes: Array.from(eventType).map(c => c.charCodeAt(0)),
            commandResponseExact: '"command_response"',
            commandResponseLength: 'command_response'.length,
            commandResponseCharCodes: Array.from('command_response').map(c => c.charCodeAt(0)),
            exactMatch: eventType === 'command_response',
            switchCase: 'about_to_enter_switch',
            timestamp: new Date().toISOString(),
          });
        }

        // Add debugging to see if processEventQueue is being called at all
        console.error('🚨 CRITICAL DEBUG: processEventQueue ENTRY POINT', {
          eventType: eventType,
          originalEventType: event.event_type,
          queueLength: eventQueue.current?.length || 0,
          isProcessing: isProcessingEvent,
          timestamp: new Date().toISOString(),
        });

        // Add exact string comparison debugging
        console.error('🚨 CRITICAL DEBUG: EXACT STRING COMPARISON', {
          eventType: eventType,
          eventTypeExact: `"${eventType}"`,
          eventTypeLength: eventType.length,
          eventTypeCharCodes: Array.from(eventType).map(c => c.charCodeAt(0)),
          commandResponseExact: '"command_response"',
          commandResponseLength: 'command_response'.length,
          commandResponseCharCodes: Array.from('command_response').map(c => c.charCodeAt(0)),
          exactMatch: eventType === 'command_response',
          includesCommand: eventType.includes('command'),
          includesResponse: eventType.includes('response'),
          switchCase: 'about_to_enter_switch',
        });

        // Add default case logging to catch unmatched events

        switch (eventType) {
          case 'game_state': {
            const playerData = event.data.player as Player;
            const roomData = event.data.room as Room;
            if (playerData && roomData) {
              updates.player = playerData;
              updates.room = roomData;
              logger.info('GameTerminalWithPanels', 'Received game state', {
                playerName: playerData.name,
                roomName: roomData.name,
                roomId: roomData.id,
              });
            }
            break;
          }
          case 'welcome': {
            const playerData = event.data.player as Player;
            const roomData = event.data.room as Room;
            if (playerData && roomData) {
              updates.player = playerData;
              updates.room = roomData;
            }
            break;
          }
          case 'room_update': {
            const roomData = event.data.room as Room;
            if (roomData) {
              updates.room = roomData;
            }
            break;
          }
          case 'room_state': {
            const roomData = event.data.room_data as Room;
            if (roomData) {
              updates.room = roomData;
            }
            break;
          }
          case 'command_response': {
            console.error('🚨 CRITICAL DEBUG: command_response case MATCHED!', {
              eventType: eventType,
              eventData: event.data,
              hasMessage: !!event.data?.message,
              messageLength: (event.data?.message as string)?.length || 0,
              timestamp: new Date().toISOString(),
            });
            const message = event.data.message as string;
            const isHtml = event.data.is_html as boolean;
            logger.info('GameTerminalWithPanels', 'Processing command response', {
              hasMessage: !!message,
              messageLength: message?.length || 0,
              isHtml,
              currentMessageCount: currentMessagesRef.current.length,
            });
            if (message) {
              // Use intelligent message type categorization
              const messageTypeResult = determineMessageType(message);
              debugMessageCategorization(message, messageTypeResult);

              const chatMessage = {
                text: message,
                timestamp: event.timestamp,
                isHtml: isHtml || false,
                messageType: messageTypeResult.type,
                channel: messageTypeResult.channel,
              };

              // Enhanced logging for debugging
              logger.info('GameTerminalWithPanels', 'Creating chat message', {
                messageText: message.substring(0, 100) + (message.length > 100 ? '...' : ''),
                messageType: messageTypeResult.type,
                channel: messageTypeResult.channel,
                timestamp: event.timestamp,
                isHtml: isHtml || false,
                messageLength: message.length,
              });

              // CRITICAL DEBUG: Track message array state
              console.log('🔍 CRITICAL DEBUG: Before adding message to updates.messages', {
                hasUpdatesMessages: !!updates.messages,
                updatesMessagesLength: updates.messages?.length || 0,
                currentMessagesRefLength: currentMessagesRef.current.length,
                messageToAdd: chatMessage,
              });

              if (!updates.messages) {
                updates.messages = [...currentMessagesRef.current];
                console.log('🔍 CRITICAL DEBUG: Created new updates.messages array', {
                  newLength: updates.messages.length,
                  copiedFrom: currentMessagesRef.current.length,
                });
              }

              updates.messages.push(chatMessage);

              console.log('🔍 CRITICAL DEBUG: After adding message to updates.messages', {
                updatesMessagesLength: updates.messages.length,
                lastMessage: updates.messages[updates.messages.length - 1],
                allMessages: updates.messages.map(m => ({
                  text: m.text.substring(0, 50) + (m.text.length > 50 ? '...' : ''),
                  messageType: m.messageType,
                  channel: m.channel,
                })),
              });

              // Debug logging for message routing
              console.log('🔍 Message Processing Debug:', {
                originalMessage: message.substring(0, 100) + (message.length > 100 ? '...' : ''),
                categorizedType: messageTypeResult.type,
                extractedChannel: messageTypeResult.channel,
                finalMessageType: chatMessage.messageType,
                finalChannel: chatMessage.channel,
                timestamp: event.timestamp,
                totalMessages: updates.messages.length,
              });
            }
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
      if (Object.keys(updates).length > 0) {
        logger.info('GameTerminalWithPanels', 'Applying state updates', {
          updateKeys: Object.keys(updates),
          messageCount: updates.messages?.length || 0,
          currentMessageCount: currentMessagesRef.current.length,
        });

        setGameState(prev => {
          const newState = {
            ...prev,
            ...updates,
            messages: updates.messages || prev.messages,
          };

          logger.info('GameTerminalWithPanels', 'State updated', {
            newMessageCount: newState.messages.length,
            hasMessages: newState.messages.length > 0,
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
  }, []);

  // Memoize the game event handler to prevent infinite re-renders
  const handleGameEvent = useCallback(
    (event: GameEvent) => {
      logger.info('GameTerminalWithPanels', 'Received game event', { event_type: event.event_type });

      // Add critical debugging for ALL events to see what's being received
      console.error('🚨 CRITICAL DEBUG: handleGameEvent called', {
        eventType: event.event_type,
        eventTypeLower: event.event_type?.toString().toLowerCase(),
        includesCommand: event.event_type?.toString().toLowerCase().includes('command'),
        includesResponse: event.event_type?.toString().toLowerCase().includes('response'),
        queueLength: eventQueue.current.length,
        isProcessing: isProcessingEvent.current,
        hasTimeout: !!processingTimeout.current,
        fullEvent: event,
      });

      // Add critical debugging for command_response events
      if (event.event_type && event.event_type.toString().toLowerCase().includes('command')) {
        console.error('🚨 CRITICAL DEBUG: handleGameEvent called for command event', {
          eventType: event.event_type,
          eventTypeLower: event.event_type.toString().toLowerCase(),
          includesCommand: event.event_type.toString().toLowerCase().includes('command'),
          queueLength: eventQueue.current.length,
          isProcessing: isProcessingEvent.current,
          hasTimeout: !!processingTimeout.current,
        });
      }

      // Add event to queue for batched processing
      eventQueue.current.push(event);

      // Process queue if not already processing
      if (!isProcessingEvent.current && !processingTimeout.current) {
        processingTimeout.current = window.setTimeout(processEventQueue, 10);
      }
    },
    [processEventQueue]
  ); // Only depend on processEventQueue

  // Memoize the connect handler
  const handleConnect = useCallback(() => {
    logger.info('GameTerminalWithPanels', 'Connected to game server');
    // Don't clear messages on connection - this was preventing message display
    // setGameState(prev => ({ ...prev, messages: [] }));
  }, []); // Empty dependency array - this function should never change

  // Memoize the disconnect handler
  const handleDisconnect = useCallback(() => {
    logger.info('GameTerminalWithPanels', 'Disconnected from game server');
  }, []); // Empty dependency array - this function should never change

  // Memoize the error handler
  const handleError = useCallback((error: string) => {
    logger.error('GameTerminalWithPanels', 'Game connection error', { error });
  }, []); // Empty dependency array - this function should never change

  // Use the game connection hook for real server communication
  const { isConnected, isConnecting, error, reconnectAttempts, connect, disconnect, sendCommand } = useGameConnection({
    playerName,
    authToken,
    onEvent: handleGameEvent,
    onConnect: handleConnect,
    onDisconnect: handleDisconnect,
    onError: handleError,
  });

  // Connect once on mount; disconnect on unmount.
  // Important: Avoid including changing dependencies (like connect/disconnect identity or state)
  // which would trigger cleanup on every render and cause immediate disconnects.
  useEffect(() => {
    // CRITICAL DEBUG: Log when useEffect executes
    console.error('🚨 CRITICAL DEBUG: GameTerminalWithPanels useEffect EXECUTED', {
      hasAttemptedConnection: hasAttemptedConnection.current,
      hasAuthToken: !!authToken,
      playerName,
      timestamp: new Date().toISOString(),
    });

    if (!hasAttemptedConnection.current) {
      hasAttemptedConnection.current = true;
      logger.info('GameTerminalWithPanels', 'Initiating connection', {
        hasAuthToken: !!authToken,
        playerName,
      });

      // CRITICAL DEBUG: Log before calling connect
      console.error('🚨 CRITICAL DEBUG: About to call connect()', {
        hasAuthToken: !!authToken,
        playerName,
        timestamp: new Date().toISOString(),
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

    // DON'T add chat messages to command history - they should only appear in ChatPanel
    // setGameState(prev => ({ ...prev, commandHistory: [...prev.commandHistory, message] }));

    // Send chat message to server
    const success = await sendCommand('chat', [channel, message]);
    if (!success) {
      logger.error('GameTerminalWithPanels', 'Failed to send chat message', { channel, message });
    }
  };

  const handleClearMessages = () => {
    setGameState(prev => ({ ...prev, messages: [] }));
  };

  const handleClearHistory = () => {
    setGameState(prev => ({ ...prev, commandHistory: [] }));
  };

  const handleLogout = () => {
    disconnect();
    // Note: App.tsx will handle the logout state
  };

  return (
    <div className="game-terminal-container">
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
        onConnect={connect}
        onDisconnect={disconnect}
        onLogout={handleLogout}
        onDownloadLogs={() => logger.downloadLogs()}
        onSendCommand={handleCommandSubmit}
        onSendChatMessage={handleChatMessage}
        onClearMessages={handleClearMessages}
        onClearHistory={handleClearHistory}
      />

      {/* Command Help Drawer */}
      <CommandHelpDrawer open={false} onClose={() => {}} />
    </div>
  );
};
