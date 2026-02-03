// Event log module: append-only store and types for event-sourced derivation
// See EVENTS_SCHEMA.md for event schema per type

export type { EventLog, EventLogEntry } from './types';
export { EMPTY_LOG } from './types';
export type { IEventStore } from './eventStore';
export { EventStore } from './eventStore';
export { getInitialGameState, projectEvent, projectState } from './projector';
