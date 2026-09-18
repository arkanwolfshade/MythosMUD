# Community 567

> 30 nodes

## Key Concepts

- **PlayerEventHandler** (29 connections) — `server/realtime/player_event_handlers.py`
- **.__init__()** (10 connections) — `server/realtime/player_event_handlers.py`
- **._initialize_handlers()** (8 connections) — `server/realtime/player_event_handlers.py`
- **.get_room_state_event()** (4 connections) — `server/realtime/player_event_handlers.py`
- **.handle_player_entered()** (4 connections) — `server/realtime/player_event_handlers.py`
- **.handle_player_left()** (4 connections) — `server/realtime/player_event_handlers.py`
- **.handle_player_delirium_respawned()** (3 connections) — `server/realtime/player_event_handlers.py`
- **.handle_player_died()** (3 connections) — `server/realtime/player_event_handlers.py`
- **.handle_player_dp_decay()** (3 connections) — `server/realtime/player_event_handlers.py`
- **.handle_player_dp_updated()** (3 connections) — `server/realtime/player_event_handlers.py`
- **.handle_player_respawned()** (3 connections) — `server/realtime/player_event_handlers.py`
- **.handle_player_xp_awarded()** (3 connections) — `server/realtime/player_event_handlers.py`
- **.send_occupants_snapshot_to_player()** (3 connections) — `server/realtime/player_event_handlers.py`
- **UUID** (3 connections)
- **ChatLogger** (1 connections)
- **ConnectionManager** (1 connections)
- **JsonMap** (1 connections)
- **Handle player entering a room with enhanced synchronization. Args: event: The…** (1 connections) — `server/realtime/player_event_handlers.py`
- **Handle player leaving a room with enhanced synchronization. Args: event: The…** (1 connections) — `server/realtime/player_event_handlers.py`
- **Send occupants snapshot to a player. CRITICAL: This method MUST include NPCs…** (1 connections) — `server/realtime/player_event_handlers.py`
- **Build authoritative room_state event for a room (for request/response enter-…** (1 connections) — `server/realtime/player_event_handlers.py`
- **Handle player XP award events by sending updates to the client. Args: event:…** (1 connections) — `server/realtime/player_event_handlers.py`
- **Handle player DP update events by sending updates to the client. Args: event:…** (1 connections) — `server/realtime/player_event_handlers.py`
- **Handle player death events by sending death notification to the client. Args:…** (1 connections) — `server/realtime/player_event_handlers.py`
- **Handle player DP decay events by sending decay notification to the client.…** (1 connections) — `server/realtime/player_event_handlers.py`
- *... and 5 more nodes in this community*

## Relationships

- [NPC Event Types](NPC_Event_Types.md) (8 shared connections)
- [Community 210](Community_210.md) (8 shared connections)
- [Community 139](Community_139.md) (4 shared connections)
- [Community 219](Community_219.md) (4 shared connections)
- [Community 330](Community_330.md) (2 shared connections)
- [Community 34](Community_34.md) (2 shared connections)
- [Community 88](Community_88.md) (2 shared connections)
- [Community 73](Community_73.md) (2 shared connections)
- [Combat Events](Combat_Events.md) (2 shared connections)
- [Community 92](Community_92.md) (1 shared connections)
- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (1 shared connections)
- [Community 393](Community_393.md) (1 shared connections)

## Source Files

- `server/realtime/player_event_handlers.py`

## Audit Trail

- EXTRACTED: 54 (79%)
- INFERRED: 14 (21%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*