// Event processing hook: event-sourced derivation via EventStore + projector
// As documented in "Event Processing Architecture" - Dr. Armitage, 1928

import { useCallback, useRef } from 'react';
import { logger } from '../../../utils/logger';
import type { GameEvent } from '../eventHandlers/types';
import { EventStore, projectState } from '../eventLog';
import type { GameState } from '../utils/stateUpdateUtils';
import { isUnusableDeathLocation } from './usePlayerStatusEffects';

interface UseEventProcessingParams {
  setGameState: React.Dispatch<React.SetStateAction<GameState>>;
  setDeathLocation?: (location: string) => void;
  lastNonLimboRoomNameRef?: React.MutableRefObject<string | null>;
}

function resolvePlayerDiedLocation(data: Record<string, unknown>, fallback: string | null): string | null {
  const extracted =
    (typeof data.death_location === 'string' && data.death_location) ||
    (typeof data.room_id === 'string' && data.room_id) ||
    'Unknown Location';
  if (!isUnusableDeathLocation(extracted)) {
    return extracted;
  }
  if (fallback && !isUnusableDeathLocation(fallback)) {
    return fallback;
  }
  return null;
}

export const useEventProcessing = ({
  setGameState,
  setDeathLocation,
  lastNonLimboRoomNameRef,
}: UseEventProcessingParams) => {
  const isProcessingEvent = useRef(false);
  const eventQueue = useRef<GameEvent[]>([]);
  const processingTimeout = useRef<number | null>(null);
  const eventStoreRef = useRef<EventStore>(new EventStore());

  // eslint-disable-next-line react-hooks/preserve-manual-memoization -- stable queue processor for setTimeout
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
      // Side-effect: death interstitial location (projector path does not call handlePlayerDied).
      if (eventType === 'player_died' || eventType === 'playerdied') {
        const d = (event.data ?? {}) as Record<string, unknown>;
        const currentDpNum = typeof d.current_dp === 'number' ? d.current_dp : NaN;
        const resolved = resolvePlayerDiedLocation(d, lastNonLimboRoomNameRef?.current ?? null);
        if (Number.isFinite(currentDpNum) && currentDpNum <= -10 && resolved) {
          setDeathLocation?.(resolved);
        }
      }
      eventQueue.current.push(event);
      if (!isProcessingEvent.current && !processingTimeout.current) {
        processingTimeout.current = window.setTimeout(() => {
          processingTimeout.current = null;
          processEventQueue();
        }, 10);
      }
    },
    [processEventQueue, setDeathLocation, lastNonLimboRoomNameRef]
  );

  const clearEventLog = useCallback(() => {
    eventStoreRef.current.clear();
  }, []);

  /** Clear pending follow request in the event log so the dialog stays closed after accept/decline. */
  const clearPendingFollowRequest = useCallback(
    (requestId: string) => {
      const store = eventStoreRef.current;
      store.append({
        event_type: 'follow_request_cleared',
        timestamp: new Date().toISOString(),
        sequence_number: 0,
        data: { request_id: requestId },
      });
      const derivedState = projectState(store.getLog());
      setGameState(prev => ({ ...derivedState, commandHistory: prev.commandHistory }));
    },
    [setGameState]
  );

  return { handleGameEvent, clearEventLog, clearPendingFollowRequest };
};
