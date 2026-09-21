// Event log module: append-only store and types for event-sourced derivation
// See EVENTS_SCHEMA.md for event schema per type
//
// This barrel is the intentional public entry for ui-v2 event-sourced state (see Vite rule:
// prefer direct leaf imports for hot paths; here one import pulls only this small surface).

export { EventStore } from './eventStore';
export { projectState } from './projector';
