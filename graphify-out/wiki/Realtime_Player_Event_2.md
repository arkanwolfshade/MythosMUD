# Realtime Player Event

> 23 nodes · cohesion 0.13

## Key Concepts

- **player_event_handlers_state.py** (22 connections) — `server/realtime/player_event_handlers_state.py`
- **_dispatch_player_dp_updated_payload()** (10 connections) — `server/realtime/player_event_handlers_state.py`
- **_send_player_death_notification()** (7 connections) — `server/realtime/player_event_handlers_state.py`
- **_player_snapshot_for_dp()** (6 connections) — `server/realtime/player_event_handlers_state.py`
- **BoundLogger** (6 connections) — `server/realtime/player_event_handlers_state.py`
- **PlayerDPUpdated** (6 connections) — `server/realtime/player_event_handlers_state.py`
- **.__init__()** (5 connections) — `server/realtime/player_event_handlers_state.py`
- **ConnectionManager** (5 connections) — `server/realtime/player_event_handlers_state.py`
- **_dp_player_update_payload()** (4 connections) — `server/realtime/player_event_handlers_state.py`
- **.handle_player_died()** (4 connections) — `server/realtime/player_event_handlers_state.py`
- **.handle_player_dp_updated()** (4 connections) — `server/realtime/player_event_handlers_state.py`
- **PlayerDiedEvent** (4 connections) — `server/realtime/player_event_handlers_state.py`
- **_dp_posture_from_stats()** (3 connections) — `server/realtime/player_event_handlers_state.py`
- **Player** (3 connections) — `server/realtime/player_event_handlers_state.py`
- **PlayerEventHandlerUtils** (3 connections) — `server/realtime/player_event_handlers_state.py`
- **Player state update event handlers.  This module handles player state updates (X** (1 connections) — `server/realtime/player_event_handlers_state.py`
- **Send player_died envelope to the deceased player's WebSocket session.** (1 connections) — `server/realtime/player_event_handlers_state.py`
- **Handle player DP update events by sending updates to the client.          Args:** (1 connections) — `server/realtime/player_event_handlers_state.py`
- **Derive posture string for DP update payloads (standing / lying / from stats).** (1 connections) — `server/realtime/player_event_handlers_state.py`
- **Handle player death events by sending death notification to the client.** (1 connections) — `server/realtime/player_event_handlers_state.py`
- **Load stats and display fields for a DP update, or fall back when player is offli** (1 connections) — `server/realtime/player_event_handlers_state.py`
- **Assemble the nested player object for a DP update WebSocket message.** (1 connections) — `server/realtime/player_event_handlers_state.py`
- **Build and send the player_dp_updated WebSocket payload.** (1 connections) — `server/realtime/player_event_handlers_state.py`

## Relationships

- [[Player Respawn Events]] (13 shared connections)
- [[Room Occupant Events]] (8 shared connections)
- [[Combat Player Broadcasts]] (4 shared connections)
- [[Player Death Service]] (2 shared connections)
- [[Player Combat XP]] (2 shared connections)
- [[Distributed Event Bus]] (1 shared connections)
- [[Player Event Handler Tests]] (1 shared connections)
- [[SQLAlchemy Model Base]] (1 shared connections)
- [[Player Domain Model]] (1 shared connections)
- [[NPC Room Event Handlers]] (1 shared connections)

## Source Files

- `server/realtime/player_event_handlers_state.py`

## Audit Trail

- EXTRACTED: 88 (88%)
- INFERRED: 12 (12%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [[index]] to navigate.*
