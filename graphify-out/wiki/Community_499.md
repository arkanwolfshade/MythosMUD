# Community 499

> 35 nodes

## Key Concepts

- **send_game_event()** (30 connections) — `server/realtime/connection_manager_api.py`
- **resolve_lazy_attr()** (12 connections) — `server/realtime/connection_manager_lazy.py`
- **broadcast_game_event()** (10 connections) — `server/realtime/connection_manager_api.py`
- **_require_manager()** (9 connections) — `server/realtime/connection_manager_api.py`
- **connection_manager_lazy.py** (9 connections) — `server/realtime/connection_manager_lazy.py`
- **_ConnectionManagerAPI** (7 connections) — `server/realtime/connection_manager_api.py`
- **send_player_status_update()** (7 connections) — `server/realtime/connection_manager_api.py`
- **send_room_description()** (7 connections) — `server/realtime/connection_manager_api.py`
- **send_system_notification()** (7 connections) — `server/realtime/connection_manager_api.py`
- **UUID** (7 connections)
- **send_room_event()** (6 connections) — `server/realtime/connection_manager_api.py`
- **test_connection_manager_lazy.py** (6 connections) — `server/tests/unit/realtime/test_connection_manager_lazy.py`
- **ConnectionManagerUnavailable** (4 connections) — `server/realtime/connection_manager_api.py`
- **test_resolve_lazy_attr_returns_api_function()** (4 connections) — `server/tests/unit/realtime/test_connection_manager_lazy.py`
- **test_resolve_lazy_attr_unknown_name_raises_attribute_error()** (3 connections) — `server/tests/unit/realtime/test_connection_manager_lazy.py`
- **.send_personal_message()** (2 connections) — `server/realtime/connection_manager_api.py`
- **.broadcast_global()** (1 connections) — `server/realtime/connection_manager_api.py`
- **.broadcast_to_room()** (1 connections) — `server/realtime/connection_manager_api.py`
- **Protocol** (1 connections)
- **RuntimeError** (1 connections)
- **parametrize** (1 connections)
- **Broadcast a game event to all connected players. Args: event_type: The type of…** (1 connections) — `server/realtime/connection_manager_api.py`
- **Send a room event to all players in a specific room. Args: room_id: The room's…** (1 connections) — `server/realtime/connection_manager_api.py`
- **Send a system notification to a player. Args: player_id: The player's ID…** (1 connections) — `server/realtime/connection_manager_api.py`
- **Send a player status update to a player. Args: player_id: The player's ID…** (1 connections) — `server/realtime/connection_manager_api.py`
- *... and 10 more nodes in this community*

## Relationships

- [Aliases & Webhook/Schema Validation](Aliases_&_Webhook-Schema_Validation.md) (14 shared connections)
- [Community 38](Community_38.md) (7 shared connections)
- [Realtime Message Handlers](Realtime_Message_Handlers.md) (3 shared connections)
- [DI Containers & API Bootstrap](DI_Containers_&_API_Bootstrap.md) (3 shared connections)
- [NPC Follow System](NPC_Follow_System.md) (2 shared connections)
- [Community 466](Community_466.md) (2 shared connections)
- [Community 110](Community_110.md) (2 shared connections)
- [Community 283](Community_283.md) (2 shared connections)
- [Community 217](Community_217.md) (2 shared connections)
- [Community 542](Community_542.md) (1 shared connections)
- [Community 808](Community_808.md) (1 shared connections)
- [Community 883](Community_883.md) (1 shared connections)

## Source Files

- `server/realtime/connection_manager_api.py`
- `server/realtime/connection_manager_lazy.py`
- `server/tests/unit/realtime/test_connection_manager_lazy.py`

## Audit Trail

- EXTRACTED: 89 (92%)
- INFERRED: 8 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*