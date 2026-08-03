# position player service

> 86 nodes

## Key Concepts

- **PlayerPositionService** (47 connections) — `server/services/player_position_service.py`
- **test_player_position_service.py** (27 connections) — `server/tests/unit/services/test_player_position_service.py`
- **.change_position()** (12 connections) — `server/services/player_position_service.py`
- **Player** (8 connections)
- **PositionChangeResponse** (6 connections) — `server/services/player_position_service.py`
- **SupportsPlayerPersistence** (6 connections) — `server/services/player_position_service.py`
- **._get_player_for_position_change()** (6 connections) — `server/services/player_position_service.py`
- **._update_player_position()** (6 connections) — `server/services/player_position_service.py`
- **.save_player()** (5 connections) — `server/services/player_position_service.py`
- **SupportsConnectionManager** (5 connections) — `server/services/player_position_service.py`
- **._apply_player_info()** (5 connections) — `server/services/player_position_service.py`
- **._load_player_stats()** (5 connections) — `server/services/player_position_service.py`
- **._get_current_position()** (5 connections) — `server/services/player_position_service.py`
- **._update_connection_manager()** (5 connections) — `server/services/player_position_service.py`
- **.get_player_by_name()** (4 connections) — `server/services/player_position_service.py`
- **.__init__()** (4 connections) — `server/services/player_position_service.py`
- **._initial_response()** (4 connections) — `server/services/player_position_service.py`
- **test_change_position_database_error()** (4 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_change_position_save_error()** (4 connections) — `server/tests/unit/services/test_player_position_service.py`
- **.get_online_player_by_display_name()** (3 connections) — `server/services/player_position_service.py`
- **.ensure_default_aliases()** (3 connections) — `server/services/player_position_service.py`
- **._validate_position()** (3 connections) — `server/services/player_position_service.py`
- **test_player_position_service_init()** (3 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_player_position_service_init_none_values()** (3 connections) — `server/tests/unit/services/test_player_position_service.py`
- **test_ensure_default_aliases_no_storage()** (3 connections) — `server/tests/unit/services/test_player_position_service.py`
- *... and 61 more nodes in this community*

## Relationships

- [commands alias rationale](commands_alias_rationale.md) (8 shared connections)
- [npc populate databases](npc_populate_databases.md) (5 shared connections)
- [Memory Task Runtime](Memory_Task_Runtime.md) (3 shared connections)
- [NATS Messaging](NATS_Messaging.md) (3 shared connections)
- [rest grace period](rest_grace_period.md) (2 shared connections)
- [NPC Combat](NPC_Combat.md) (1 shared connections)

## Source Files

- `server/services/player_position_service.py`
- `server/tests/unit/services/test_player_position_service.py`

## Audit Trail

- EXTRACTED: 279 (98%)
- INFERRED: 5 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*