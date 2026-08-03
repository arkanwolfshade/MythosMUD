# commands lucidity recovery

> 18 nodes

## Key Concepts

- **_mock_result_mappings_all()** (29 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_get_npc_definitions_empty()** (3 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_get_npc_definition_not_found()** (3 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_update_npc_definition_not_found()** (3 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_delete_npc_definition_not_found()** (3 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_get_spawn_rule_not_found()** (3 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_create_spawn_rule_definition_not_found()** (3 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_delete_spawn_rule_not_found()** (3 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_get_system_statistics_success()** (3 connections) — `server/tests/unit/services/test_npc_service.py`
- **Build mock result such that result.mappings().all() returns rows.** (1 connections) — `server/tests/unit/services/test_npc_service.py`
- **Test get_npc_definitions() returns empty list when no definitions.** (1 connections) — `server/tests/unit/services/test_npc_service.py`
- **Test get_npc_definition() returns None when not found.** (1 connections) — `server/tests/unit/services/test_npc_service.py`
- **Test update_npc_definition() returns None when not found.** (1 connections) — `server/tests/unit/services/test_npc_service.py`
- **Test delete_npc_definition() returns False when not found.** (1 connections) — `server/tests/unit/services/test_npc_service.py`
- **Test get_spawn_rule() returns None when not found.** (1 connections) — `server/tests/unit/services/test_npc_service.py`
- **Test create_spawn_rule() raises ValueError when definition not found.** (1 connections) — `server/tests/unit/services/test_npc_service.py`
- **Test delete_spawn_rule() returns False when not found.** (1 connections) — `server/tests/unit/services/test_npc_service.py`
- **Test get_system_statistics() successfully generates stats.** (1 connections) — `server/tests/unit/services/test_npc_service.py`

## Relationships

- [npc service services](npc_service_services.md) (9 shared connections)
- [models lucidity rationale](models_lucidity_rationale.md) (9 shared connections)
- [eventLog eventStore projector](eventLog_eventStore_projector.md) (4 shared connections)
- [realtime player event](realtime_player_event.md) (3 shared connections)
- [player event realtime](player_event_realtime.md) (2 shared connections)
- [player event room](player_event_room.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_npc_service.py`

## Audit Trail

- EXTRACTED: 62 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*