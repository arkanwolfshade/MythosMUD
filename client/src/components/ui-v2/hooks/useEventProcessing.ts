// Event processing hook
// Extracted from GameClientV2Container to reduce complexity
// As documented in "Event Processing Architecture" - Dr. Armitage, 1928

import { useCallback, useRef } from 'react';
import { logger } from '../../../utils/logger';
import { processGameEvent } from '../eventHandlers';
import type { EventHandlerContext, GameEvent } from '../eventHandlers/types';
import type { ChatMessage } from '../types';
import type { GameState } from '../utils/stateUpdateUtils';
import { applyEventUpdates, sanitizeAndApplyUpdates } from '../utils/stateUpdateUtils';

interface UseEventProcessingParams {
  currentMessagesRef: React.MutableRefObject<ChatMessage[]>;
  setGameState: React.Dispatch<React.SetStateAction<GameState>>;
  context: EventHandlerContext;
}

export const useEventProcessing = ({ currentMessagesRef, setGameState, context }: UseEventProcessingParams) => {
  const isProcessingEvent = useRef(false);
  const lastProcessedEvent = useRef<string>('');
  const eventQueue = useRef<GameEvent[]>([]);
  const processingTimeout = useRef<number | null>(null);

  const processEventQueue = useCallback(() => {
    // Defensive check for isProcessingEvent.current is effectively unreachable in normal operation
    // because the code prevents processEventQueue from being called while processing is active.
    // This branch exists as a safety measure but cannot be tested without refactoring to expose
    // processEventQueue, which would break encapsulation.
    /* v8 ignore start */
    if (isProcessingEvent.current || eventQueue.current.length === 0) {
      return;
    }
    /* v8 ignore stop */

    isProcessingEvent.current = true;

    try {
      const events = [...eventQueue.current];
      eventQueue.current = [];
      const updates: Partial<GameState> = {};

      const appendMessage = (message: ChatMessage) => {
        if (!updates.messages) {
          updates.messages = [...currentMessagesRef.current];
        }
        updates.messages.push(message);
      };

      events.forEach((event, index) => {
        logger.info('useEventProcessing', 'OCCUPANT_DEBUG: batch event', {
          index,
          event_type: event.event_type,
          seq: event.sequence_number,
          room_before: updates.room?.occupant_count ?? 'none',
        });
        const eventUpdates = processGameEvent(event, context, appendMessage, lastProcessedEvent);
        // Convert null to undefined to match applyEventUpdates signature
        applyEventUpdates(eventUpdates ?? undefined, updates, currentMessagesRef.current);
        logger.info('useEventProcessing', 'OCCUPANT_DEBUG: after apply', {
          index,
          event_type: event.event_type,
          room_after: updates.room?.occupant_count ?? 'none',
          room_occupants_len: updates.room?.occupants?.length ?? 0,
        });
      });

      sanitizeAndApplyUpdates(updates, setGameState);
    } catch (error) {
      logger.error('useEventProcessing', 'Error processing events', { error });
    } finally {
      isProcessingEvent.current = false;

      if (eventQueue.current.length > 0) {
        processingTimeout.current = window.setTimeout(processEventQueue, 10);
      }
    }
  }, [context, currentMessagesRef, setGameState]);

  const handleGameEvent = useCallback(
    (event: GameEvent) => {
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

  return { handleGameEvent };
};
