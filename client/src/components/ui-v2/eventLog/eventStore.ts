// Append-only event store for event-sourced GameState derivation
// As documented in "Event Processing Architecture" - Dr. Armitage, 1928

import type { GameEvent } from '../eventHandlers/types';
import type { EventLog, EventLogEntry } from './types';

/**
 * Append-only store of game events. Events are never removed except by clear() (e.g. on disconnect).
 * Used by the projector to derive GameState from the full log.
 */
export interface IEventStore {
  /** Append one or more events to the log */
  append(events: GameEvent | GameEvent[]): void;
  /** Return a read-only snapshot of the current log */
  getLog(): EventLog;
  /** Clear the log (e.g. on logout) */
  clear(): void;
}

/**
 * In-memory append-only event store. Thread-safe for single-threaded JS; append is synchronous.
 */
export class EventStore implements IEventStore {
  private log: EventLogEntry[] = [];

  append(events: GameEvent | GameEvent[]): void {
    const toAppend = Array.isArray(events) ? events : [events];
    this.log.push(...toAppend);
  }

  getLog(): EventLog {
    return this.log;
  }

  clear(): void {
    this.log = [];
  }
}
