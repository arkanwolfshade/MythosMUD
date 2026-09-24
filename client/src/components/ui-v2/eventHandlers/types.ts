// WebSocket event type shared across the client. The full catalog and per-type projector effects
// are documented on projectorConstants.ts (PROJECTED_EVENT_TYPES) and eventLog/EVENTS_SCHEMA.md.

export interface GameEvent {
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
