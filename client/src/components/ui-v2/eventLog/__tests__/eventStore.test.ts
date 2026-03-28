import { describe, expect, it } from 'vitest';

import type { GameEvent } from '../../eventHandlers/types';
import { EventStore } from '../eventStore';

function makeEvent(sequenceNumber: number, type = 'system'): GameEvent {
  return {
    event_type: type,
    timestamp: new Date().toISOString(),
    sequence_number: sequenceNumber,
    data: {},
  };
}

describe('EventStore', () => {
  it('appends a single event', () => {
    const store = new EventStore();
    const event = makeEvent(1);

    store.append(event);

    expect(store.getLog()).toEqual([event]);
  });

  it('appends multiple events in order', () => {
    const store = new EventStore();
    const first = makeEvent(1, 'room_update');
    const second = makeEvent(2, 'player_update');

    store.append([first, second]);

    expect(store.getLog()).toEqual([first, second]);
  });

  it('clears all stored events', () => {
    const store = new EventStore();
    store.append([makeEvent(1), makeEvent(2)]);

    store.clear();

    expect(store.getLog()).toEqual([]);
  });
});
