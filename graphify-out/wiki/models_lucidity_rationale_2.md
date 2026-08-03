# models lucidity rationale

> 20 nodes

## Key Concepts

- **_def_row()** (18 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_update_npc_definition_success()** (5 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_get_npc_definitions_success()** (4 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_get_npc_definition_found()** (4 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_get_npc_definition_by_name_case_insensitive()** (4 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_get_npc_definition_by_name_not_found()** (4 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_create_npc_definition_success()** (4 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_create_spawn_rule_invalid_min_population()** (4 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_create_spawn_rule_invalid_max_population()** (4 connections) — `server/tests/unit/services/test_npc_service.py`
- **test_get_npc_definitions_by_type()** (4 connections) — `server/tests/unit/services/test_npc_service.py`
- **Build procedure result row (mappings().all()[i] or .first()) for NPCDefinition.** (1 connections) — `server/tests/unit/services/test_npc_service.py`
- **Test get_npc_definitions() successfully retrieves definitions.** (1 connections) — `server/tests/unit/services/test_npc_service.py`
- **Test get_npc_definition() returns definition when found.** (1 connections) — `server/tests/unit/services/test_npc_service.py`
- **Test get_npc_definition_by_name() matches case-insensitively.** (1 connections) — `server/tests/unit/services/test_npc_service.py`
- **Test get_npc_definition_by_name() returns None when not found.** (1 connections) — `server/tests/unit/services/test_npc_service.py`
- **Test create_npc_definition() successfully creates definition.** (1 connections) — `server/tests/unit/services/test_npc_service.py`
- **Test update_npc_definition() successfully updates definition.** (1 connections) — `server/tests/unit/services/test_npc_service.py`
- **Test create_spawn_rule() raises ValueError for invalid min population.** (1 connections) — `server/tests/unit/services/test_npc_service.py`
- **Test create_spawn_rule() raises ValueError when max < min.** (1 connections) — `server/tests/unit/services/test_npc_service.py`
- **Test get_npc_definitions_by_type() filters by type.** (1 connections) — `server/tests/unit/services/test_npc_service.py`

## Relationships

- [npc service services](npc_service_services.md) (10 shared connections)
- [commands lucidity recovery](commands_lucidity_recovery.md) (9 shared connections)
- [realtime player event](realtime_player_event.md) (3 shared connections)
- [player event realtime](player_event_realtime.md) (2 shared connections)
- [eventLog eventStore projector](eventLog_eventStore_projector.md) (1 shared connections)
- [player event room](player_event_room.md) (1 shared connections)
- [Realtime Subscribers](Realtime_Subscribers.md) (1 shared connections)

## Source Files

- `server/tests/unit/services/test_npc_service.py`

## Audit Trail

- EXTRACTED: 64 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*