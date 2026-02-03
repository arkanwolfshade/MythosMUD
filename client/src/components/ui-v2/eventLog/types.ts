// Event log types for event-sourced GameState derivation
// See EVENTS_SCHEMA.md for event_type and data shapes

import type { GameEvent } from '../eventHandlers/types';

/** Single event in the log; same as GameEvent from handler types */
export type EventLogEntry = GameEvent;

/** Immutable view of the event log (read-only array) */
export type EventLog = readonly EventLogEntry[];

/** Initial empty log */
export const EMPTY_LOG: EventLog = [] as const;
