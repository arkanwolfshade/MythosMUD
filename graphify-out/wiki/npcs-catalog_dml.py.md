# npcs/catalog_dml.py

> 70 nodes · cohesion 0.05

## Key Concepts

- **test_combat_flee_helpers.py** (27 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **combat_flee.py** (24 connections) — `server/commands/combat_flee.py`
- **_FleeCommandHandlerLike** (16 connections) — `server/commands/combat_flee.py`
- **_resolve_flee_preconditions()** (16 connections) — `server/commands/combat_flee.py`
- **_validate_flee_combat_and_room()** (12 connections) — `server/commands/combat_flee.py`
- **FleePreconditionError** (10 connections) — `server/commands/combat_helpers.py`
- **_ensure_flee_standing()** (8 connections) — `server/commands/combat_flee.py`
- **_get_flee_player_uuid()** (8 connections) — `server/commands/combat_flee.py`
- **_get_flee_room_id()** (8 connections) — `server/commands/combat_flee.py`
- **_PlayerForFlee** (8 connections) — `server/commands/combat_flee.py`
- **run_handle_flee_command()** (7 connections) — `server/commands/combat_flee.py`
- **combat_helpers.py** (7 connections) — `server/commands/combat_helpers.py`
- **asyncio** (6 connections)
- **test_validate_flee_combat_and_room_success()** (6 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **test_resolve_flee_preconditions_player_error()** (5 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **test_validate_flee_combat_and_room_no_movement_service()** (5 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **_PlayerPositionServiceLike** (4 connections) — `server/commands/combat_flee.py`
- **UUID** (4 connections)
- **_participant()** (4 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **test_ensure_flee_standing_when_already_standing()** (4 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **test_ensure_flee_standing_when_sitting()** (4 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **test_validate_flee_combat_and_room_no_combat_service()** (4 connections) — `server/tests/unit/commands/test_combat_flee_helpers.py`
- **.check_and_interrupt_rest()** (3 connections) — `server/commands/combat_flee.py`
- **.combat_service()** (3 connections) — `server/commands/combat_flee.py`
- **.get_player_and_room()** (3 connections) — `server/commands/combat_flee.py`
- *... and 45 more nodes in this community*

## Relationships

- [PlayerPositionService](PlayerPositionService.md) (6 shared connections)
- [test_player_combat_service.py](test_player_combat_service.py.md) (6 shared connections)
- [command_parser.py](command_parser.py.md) (6 shared connections)
- [NPCLifecycleManager](NPCLifecycleManager.md) (3 shared connections)
- [InventorySchemaValidationError](InventorySchemaValidationError.md) (3 shared connections)
- [CorruptionRepository](CorruptionRepository.md) (2 shared connections)
- [apply_communication_dampening](apply_communication_dampening.md) (2 shared connections)
- [DatabaseManager](DatabaseManager.md) (2 shared connections)
- [container_endpoints_basic.py](container_endpoints_basic.py.md) (2 shared connections)
- [PlayerRespawnEventHandler](PlayerRespawnEventHandler.md) (1 shared connections)

## Source Files

- `server/commands/combat_flee.py`
- `server/commands/combat_helpers.py`
- `server/tests/unit/commands/test_combat_flee_helpers.py`

## Audit Trail

- EXTRACTED: 145 (96%)
- INFERRED: 6 (4%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*