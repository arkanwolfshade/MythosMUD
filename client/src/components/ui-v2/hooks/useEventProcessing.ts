// Event processing hook: event-sourced derivation via EventStore + projector
// As documented in "Event Processing Architecture" - Dr. Armitage, 1928

import { useCallback, useRef } from 'react';
import { logger } from '../../../utils/logger';
import type { GameEvent } from '../eventHandlers/types';
import { EventStore, projectState } from '../eventLog';
import type { GameState } from '../utils/stateUpdateUtils';

interface UseEventProcessingParams {
  setGameState: React.Dispatch<React.SetStateAction<GameState>>;
}

export const useEventProcessing = ({ setGameState }: UseEventProcessingParams) => {
  const isProcessingEvent = useRef(false);
  const eventQueue = useRef<GameEvent[]>([]);
  const processingTimeout = useRef<number | null>(null);
  const eventStoreRef = useRef<EventStore>(new EventStore());

  const processEventQueue = useCallback(() => {
    if (isProcessingEvent.current || eventQueue.current.length === 0) {
      return;
    }

    isProcessingEvent.current = true;

    try {
      const events = [...eventQueue.current];
      eventQueue.current = [];
      const store = eventStoreRef.current;
      store.append(events);
      const derivedState = projectState(store.getLog());
      // Preserve client-only commandHistory; projector does not replay submitted commands.
      setGameState(prev => ({ ...derivedState, commandHistory: prev.commandHistory }));
    } catch (error) {
      logger.error('useEventProcessing', 'Error projecting state from event log', { error });
    } finally {
      isProcessingEvent.current = false;

      if (eventQueue.current.length > 0) {
        processingTimeout.current = window.setTimeout(processEventQueue, 10);
      }
    }
  }, [setGameState]);

  const handleGameEvent = useCallback(
    (event: GameEvent) => {
      const eventType = (event.event_type ?? '').toString().trim().toLowerCase();
      if (eventType === 'player_attacked' || eventType === 'npc_attacked') {
        logger.info('useEventProcessing', 'Combat event received', {
          event_type: eventType,
          room_id: (event as { room_id?: string }).room_id,
          has_data: !!event.data,
          data_keys: event.data ? Object.keys(event.data) : [],
        });
      }
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

  const clearEventLog = useCallback(() => {
    eventStoreRef.current.clear();
  }, []);

  return { handleGameEvent, clearEventLog };
};
