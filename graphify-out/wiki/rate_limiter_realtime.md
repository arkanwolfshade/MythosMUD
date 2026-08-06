# rate limiter realtime

> 32 nodes

## Key Concepts

- **NPCCombatDataProvider** (39 connections) — `server/services/npc_combat_data_provider.py`
- **test_npc_combat_data_provider.py** (17 connections) — `server/tests/unit/services/test_npc_combat_data_provider.py`
- **UUID** (5 connections)
- **.get_npc_combat_data()** (5 connections) — `server/services/npc_combat_data_provider.py`
- **Any** (4 connections)
- **.get_npc_instance()** (4 connections) — `server/services/npc_combat_data_provider.py`
- **.get_player_combat_data()** (4 connections) — `server/services/npc_combat_data_provider.py`
- **.__init__()** (3 connections) — `server/services/npc_combat_data_provider.py`
- **.get_player_name()** (3 connections) — `server/services/npc_combat_data_provider.py`
- **.get_player_room_id()** (3 connections) — `server/services/npc_combat_data_provider.py`
- **.get_data_provider()** (3 connections) — `server/services/npc_combat_integration_service.py`
- **test_get_npc_instance_from_lifecycle()** (2 connections) — `server/tests/unit/services/test_npc_combat_data_provider.py`
- **test_get_npc_instance_returns_none_on_error()** (2 connections) — `server/tests/unit/services/test_npc_combat_data_provider.py`
- **test_get_npc_definition_from_persistence()** (2 connections) — `server/tests/unit/services/test_npc_combat_data_provider.py`
- **test_get_player_name_found()** (2 connections) — `server/tests/unit/services/test_npc_combat_data_provider.py`
- **test_get_player_name_unknown()** (2 connections) — `server/tests/unit/services/test_npc_combat_data_provider.py`
- **test_get_player_room_id_invalid_uuid()** (2 connections) — `server/tests/unit/services/test_npc_combat_data_provider.py`
- **test_get_player_room_id_found()** (2 connections) — `server/tests/unit/services/test_npc_combat_data_provider.py`
- **test_get_player_combat_data()** (2 connections) — `server/tests/unit/services/test_npc_combat_data_provider.py`
- **test_get_player_combat_data_missing_player()** (2 connections) — `server/tests/unit/services/test_npc_combat_data_provider.py`
- **test_get_npc_combat_data_with_get_combat_stats()** (2 connections) — `server/tests/unit/services/test_npc_combat_data_provider.py`
- **test_get_npc_combat_data_fallback_stats()** (2 connections) — `server/tests/unit/services/test_npc_combat_data_provider.py`
- **Provides data retrieval and preparation for NPC combat.** (1 connections) — `server/services/npc_combat_data_provider.py`
- **Initialize the data provider.          Args:             async_persistence: A** (1 connections) — `server/services/npc_combat_data_provider.py`
- **Get NPC instance from the spawning service.          Args:             npc_id** (1 connections) — `server/services/npc_combat_data_provider.py`
- *... and 7 more nodes in this community*

## Relationships

- [player event realtime](player_event_realtime.md) (7 shared connections)
- [Error Conversion](Error_Conversion.md) (5 shared connections)
- [subject admin controller](subject_admin_controller.md) (4 shared connections)
- [combat services service](combat_services_service.md) (3 shared connections)
- [models player rationale](models_player_rationale.md) (3 shared connections)
- [models npc rationale](models_npc_rationale.md) (2 shared connections)
- [npc database infrastructure](npc_database_infrastructure.md) (1 shared connections)
- [player look commands](player_look_commands.md) (1 shared connections)
- [game models player](game_models_player.md) (1 shared connections)
- [commands npc admin](commands_npc_admin.md) (1 shared connections)

## Source Files

- `server/services/npc_combat_data_provider.py`
- `server/services/npc_combat_integration_service.py`
- `server/tests/unit/services/test_npc_combat_data_provider.py`

## Audit Trail

- EXTRACTED: 114 (93%)
- INFERRED: 8 (7%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*